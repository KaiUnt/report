from fpdf import FPDF
import tempfile
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime
import os
from typing import List, Optional, Dict
import requests
from io import BytesIO
from ..data.models import RankingsData, SeriesResult
from .components import PDFComponents
from .styles import PDFStyles
import unicodedata

class RankingsPDF(FPDF):
    """Enhanced PDF class with Unicode support and safe text handling."""
    
    def __init__(self):
        super().__init__(orientation='L', unit='mm', format='A4')
        self.set_auto_page_break(auto=True, margin=15)
        self.styles = PDFStyles()
        self.components = PDFComponents(self)
        
        # Initialize Unicode fonts
        self.add_unicode_fonts()
        
    def header(self):
        """Add header to each page."""
        self.use_unicode_font('bold', 12)
        self.cell(0, 10, 'FWT Rankings Report', 0, 0, 'R')
        self.ln(10)

    def add_unicode_fonts(self):
        """Add fonts with Unicode support."""
        fonts_dir = os.path.join(os.path.dirname(__file__), 'fonts')
        os.makedirs(fonts_dir, exist_ok=True)
        
        self.unicode_fonts = {
            'normal': {
                'name': 'NotoSans',
                'file': 'NotoSans-Regular.ttf',
                'url': 'https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSans/NotoSans-Regular.ttf'
            },
            'bold': {
                'name': 'NotoSans-Bold',
                'file': 'NotoSans-Bold.ttf',
                'url': 'https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSans/NotoSans-Bold.ttf'
            }
        }

        for style, font_info in self.unicode_fonts.items():
            font_path = os.path.join(fonts_dir, font_info['file'])
            
            if not os.path.exists(font_path):
                try:
                    response = requests.get(font_info['url'])
                    response.raise_for_status()
                    with open(font_path, 'wb') as f:
                        f.write(response.content)
                except Exception as e:
                    print(f"Error downloading font {font_info['name']}: {e}")
                    continue

            self.add_font(font_info['name'], style='', fname=font_path, uni=True)
            if style == 'bold':
                self.add_font(font_info['name'], style='B', fname=font_path, uni=True)

    def use_unicode_font(self, style='normal', size=10):
        """Set the appropriate Unicode font."""
        font_info = self.unicode_fonts.get(style)
        if font_info:
            self.set_font(font_info['name'], 'B' if style == 'bold' else '', size)

    def safe_text(self, text: str) -> str:
        """Prepare text for safe output while maintaining Unicode characters."""
        if not text:
            return ''
        
        normalized = unicodedata.normalize('NFKC', str(text))
        cleaned = ''.join(char for char in normalized 
                         if unicodedata.category(char)[0] != 'C' 
                         or char in '\n\r\t')
        return cleaned

    def safe_cell(self, w, h, txt, border=0, ln=0, align='', fill=False):
        """Enhanced safe cell output with Unicode support."""
        safe_txt = self.safe_text(txt)
        self.cell(w, h, safe_txt, border, ln, align, fill)

class RankingsReportGenerator:
    """Main class for generating ranking reports."""
    
    def __init__(self):
        self.pdf = RankingsPDF()
        self.temp_files = []
        self.components = PDFComponents(self.pdf)

    def _download_image(self, url: str, athlete_name: str) -> Optional[str]:
        """Download and save athlete image temporarily."""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
                img.convert('RGB').save(temp_file.name, 'JPEG')
                self.temp_files.append(temp_file.name)
                return temp_file.name
        except Exception as e:
            print(f"Error downloading image for {athlete_name}: {e}")
        return None

    def _create_performance_chart(self, series_results: List[SeriesResult]) -> Optional[str]:
        """Create performance development chart."""
        try:
            placements = {}
            for series in series_results:
                if series.series_year not in placements:
                    placements[series.series_year] = float('inf')
                placements[series.series_year] = min(
                    placements[series.series_year],
                    float(series.place) if series.place else float('inf')
                )

            if placements:
                years = sorted(placements.keys())
                places = [placements[year] for year in years]

                plt.figure(figsize=(4, 2))
                plt.plot(years, places, marker='o', linestyle='-', linewidth=2)
                plt.gca().invert_yaxis()
                plt.title('Performance Development')
                plt.xlabel('Year')
                plt.ylabel('Place')
                plt.grid(True)

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
                plt.savefig(temp_file.name, bbox_inches='tight')
                plt.close()

                self.temp_files.append(temp_file.name)
                return temp_file.name

        except Exception as e:
            print(f"Error creating chart: {e}")
        return None
    
    def calculate_age(self, dob: datetime) -> Optional[int]:
        """Calculate age from date of birth."""
        if not dob:
            return None
        today = datetime.now()
        age = today.year - dob.year
        # Korrigiere das Alter, wenn der Geburtstag dieses Jahr noch nicht war
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            age -= 1
        return age

    def _add_athlete_section(self, data: RankingsData, image_width: float, text_width: float):
        """Add athlete information section."""
        # Title with Unicode support
        self.pdf.use_unicode_font('bold', 14)
        title_text = f"Profile of {data.athlete.name}"
        if data.athlete.bib:
            title_text = f"Profile of {data.athlete.name} (BIB #{data.athlete.bib})"
        self.pdf.safe_cell(0, 10, title_text, ln=True, align='C')

        # Athlete image
        if data.athlete.image:
            image_file = self._download_image(data.athlete.image, data.athlete.name)
            if image_file:
                try:
                    self.pdf.image(image_file,
                                 x=self.pdf.w - self.pdf.r_margin - image_width,
                                 y=self.pdf.t_margin,
                                 w=image_width)
                except Exception as e:
                    print(f"Error adding image: {e}")

        # Basic Info Box
        info_box_height = 35
        self.pdf.set_fill_color(245, 245, 245)
        self.pdf.rect(self.pdf.l_margin, self.pdf.get_y(), text_width, info_box_height, 'F')

        start_y = self.pdf.get_y() + 2
        self.pdf.set_xy(self.pdf.l_margin + 5, start_y)

        # Info Content
        self.pdf.use_unicode_font('bold', 12)
        self.pdf.safe_cell(text_width-10, 6, data.athlete.name, ln=True)

        self.pdf.use_unicode_font('normal', 10)
        if data.athlete.nationality:
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6, f"Nationality: {data.athlete.nationality}", ln=True)

        if data.athlete.dob:
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6, f"Date of Birth: {data.athlete.dob.strftime('%Y-%m-%d')}", ln=True)

            # Neue Zeile für das Alter
            age = self.calculate_age(data.athlete.dob)
            if age is not None:
                self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
                self.pdf.safe_cell(text_width-10, 6, f"Age: {age} years", ln=True)

    def _add_stats_section(self, data: RankingsData):
        """Add statistics section to the PDF with safe handling of missing data."""
        # Basis-Überprüfung
        if not data or not data.stats:
            return

        self.pdf.ln(10)
        self.pdf.use_unicode_font('bold', 14)
        self.pdf.safe_cell(0, 10, "Career Statistics", ln=True)

        # Box Setup
        text_width = self.pdf.w - self.pdf.l_margin - self.pdf.r_margin
        self.pdf.set_fill_color(240, 248, 255)
        
        # Dynamische Box-Höhe basierend auf verfügbaren Daten
        available_stats = sum([
            bool(data.stats.best_result and (data.stats.best_result.get('by_points') or 
                                        data.stats.best_result.get('by_rank'))),
            bool(data.stats.best_series_place),
            bool(data.stats.best_pro_place),
            bool(data.stats.best_challenger_place),
            bool(data.stats.best_pro_event),
            bool(data.stats.best_challenger_event),
            True  # Für Total Events/Series (immer vorhanden)
        ])
        
        # Dynamisch die benötigte Höhe berechnen
        lines = 0

        # Zähle Zeilen basierend auf vorhandenen Daten
        if data.stats.best_result:
            if data.stats.best_result.get('by_points'):
                lines += 1
            if data.stats.best_result.get('by_rank'):
                lines += 1

        if data.stats.oldest_result:
            lines += 1

        if data.stats.best_series_place:
            lines += 1
        
        if data.stats.best_challenger_event:
            lines += 1

        if data.stats.best_pro_event:
            lines += 1
        
        if data.stats.total_events:
            lines += 1

        # Setze minimale Höhe (z. B. 20mm) oder passe dynamisch an Zeilenanzahl an
        line_height = 8  # Höhe jeder Textzeile in mm
        box_height = max(20, lines * line_height)

        # Zeichne den dynamischen Rahmen
        self.pdf.rect(self.pdf.l_margin, self.pdf.get_y(), text_width, box_height, 'F')


        # Content positioning
        start_y = self.pdf.get_y() + 2
        self.pdf.set_xy(self.pdf.l_margin + 5, start_y)
        self.pdf.use_unicode_font('normal', 10)

        # Best Results - mit Null Checks
        if data.stats.best_result:
            best_points = data.stats.best_result.get('by_points')
            if best_points and best_points.points and best_points.event_name:
                self.pdf.safe_cell(text_width-10, 6,
                    f"Best Result by Points: {best_points.points} points at {best_points.event_name}", ln=True)

            best_rank = data.stats.best_result.get('by_rank')
            if best_rank and best_rank.place and best_rank.event_name:
                self.pdf.safe_cell(text_width-10, 6,
                    f"Best Result by Rank: {best_rank.place}. Place at {best_rank.event_name}", ln=True)

        # Oldest Result hinzufügen
        if data.stats.oldest_result:
            oldest_result = data.stats.oldest_result
            self.pdf.safe_cell(text_width-10, 6,
                f"Oldest Result: {oldest_result.event_name} on {oldest_result.date.strftime('%Y-%m-%d')} "
                f"(Place: {oldest_result.place}, Points: {oldest_result.points})", ln=True)
        
        # Series Results - mit Null Checks
        if data.stats.best_series_place and data.stats.best_series_place.place and data.stats.best_series_place.series_name:
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Overall Series: {data.stats.best_series_place.place}. Place in {data.stats.best_series_place.series_name}", ln=True)

        if data.stats.best_pro_place and data.stats.best_pro_place.place and data.stats.best_pro_place.series_name:
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Pro Series: {data.stats.best_pro_place.place}. Place in {data.stats.best_pro_place.series_name}", ln=True)

        if data.stats.best_challenger_place and data.stats.best_challenger_place.place and data.stats.best_challenger_place.series_name:
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Challenger Series: {data.stats.best_challenger_place.place}. Place in {data.stats.best_challenger_place.series_name}", ln=True)

        # Summary Statistics - immer vorhanden (defaults to 0)
        total_events = getattr(data.stats, 'total_events', 0)
        total_series = getattr(data.stats, 'total_series', 0)
        
        if total_events == 0 and total_series == 0:
            self.pdf.safe_cell(text_width-10, 6, "New Athlete - No competition history yet", ln=True)
        else:
            self.pdf.safe_cell(text_width-10, 6,
                f"Total Events: {total_events} | Total Series: {total_series}", ln=True)

        # Best Events in Pro/Challenger - mit Null Checks
        if (data.stats.best_pro_event and 
            data.stats.best_pro_event.points and 
            data.stats.best_pro_event.event_name):
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Pro Event: {data.stats.best_pro_event.points} points at {data.stats.best_pro_event.event_name}", ln=True)

        if (data.stats.best_challenger_event and 
            data.stats.best_challenger_event.points and 
            data.stats.best_challenger_event.event_name):
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Challenger Event: {data.stats.best_challenger_event.points} points at {data.stats.best_challenger_event.event_name}", ln=True)
    
    def _add_series_results(self, series_results: List[SeriesResult]):
        """Add series results section."""
        self.pdf.ln(10)
        self.pdf.use_unicode_font('bold', 14)
        self.pdf.safe_cell(0, 10, "Series Results", ln=True)

        # Sort by year (newest first) and place
        sorted_results = sorted(
            series_results,
            key=lambda x: (-x.series_year, x.place if x.place is not None else float('inf'))
        )

        for result in sorted_results:
            # Series Header
            self.pdf.set_fill_color(230, 230, 230)
            self.pdf.use_unicode_font('bold', 12)
            self.pdf.safe_cell(0, 8, result.series_name, ln=True, fill=True)

            self.pdf.use_unicode_font('normal', 10)
            self.pdf.safe_cell(0, 6, f"Division: {result.division_name}", ln=True)
            self.pdf.safe_cell(0, 6, f"Place: {result.place}  Points: {result.points}", ln=True)

            if result.results:
                self._add_event_results_table(result.results)

            self.pdf.ln(5)

    def _add_event_results_table(self, events: List[SeriesResult]):
        """Add event results table."""
        self.pdf.ln(2)
        # Table Header
        self.pdf.set_fill_color(240, 240, 240)
        self.pdf.use_unicode_font('bold', 9)
        self.pdf.cell(120, 6, 'Event Name', 1, 0, 'L', True)
        self.pdf.cell(30, 6, 'Date', 1, 0, 'C', True)
        self.pdf.cell(20, 6, 'Place', 1, 0, 'C', True)
        self.pdf.cell(20, 6, 'Points', 1, 1, 'C', True)

        # Sort events by place
        sorted_events = sorted(
            events,
            key=lambda x: x.place if x.place is not None else float('inf')
        )

        # Table Content
        self.pdf.use_unicode_font('normal', 9)
        for i, event in enumerate(sorted_events):
            fill = i % 2 == 0
            if fill:
                self.pdf.set_fill_color(250, 250, 250)

            self.pdf.safe_cell(120, 6, event.event_name, 1, 0, 'L', fill)
            self.pdf.cell(30, 6, event.date.strftime('%Y-%m-%d'), 1, 0, 'C', fill)
            self.pdf.cell(20, 6, str(event.place), 1, 0, 'C', fill)
            self.pdf.cell(20, 6, str(event.points), 1, 1, 'C', fill)


    def _filter_series(self, series_results: List[SeriesResult]) -> List[SeriesResult]:
        """Filter out unwanted series like seeding lists and national rankings."""
        excluded_terms = [
            "National Rankings",
            "Seeding List"
        ]
        
        filtered = [
            series for series in series_results
            if not any(term.lower() in series.series_name.lower() for term in excluded_terms)
        ]
            
        return filtered

    def generate_report(self, rankings_data: List[RankingsData], output_file: str):
        """Generate complete PDF report."""
        try:
            # Sort athletes by BIB number
            sorted_athletes = sorted(
                rankings_data,
                key=lambda x: int(x.athlete.bib) if x.athlete.bib and x.athlete.bib.isdigit() else float('inf')
            )

            for data in sorted_athletes:
                # Filter series before processing
                filtered_series = self._filter_series(data.series_results)
                if not filtered_series:
                    print(f"Skipping {data.athlete.name} - no relevant series found")
                    continue
                    
                # Replace original series with filtered ones
                data.series_results = filtered_series
                
                self.pdf.add_page()

                # Layout calculations
                image_width = 60
                text_width = self.pdf.w - self.pdf.l_margin - self.pdf.r_margin - image_width - 10

                # Add main sections
                self._add_athlete_section(data, image_width, text_width)
                self._add_stats_section(data)
                
                # Performance Chart
                chart_file = self._create_performance_chart(data.series_results)
                if chart_file:
                    self.pdf.image(chart_file,
                                 x=self.pdf.w - self.pdf.r_margin - image_width,
                                 y=self.pdf.t_margin + image_width + 5,
                                 w=image_width)

                # Add series results
                self._add_series_results(data.series_results)

            # Save the PDF
            self.pdf.output(output_file)
            print(f"Report generated: {output_file}")

        finally:
            # Cleanup
            plt.close('all')
            for temp_file in self.temp_files:
                try:
                    if os.path.exists(temp_file):
                        os.unlink(temp_file)
                except Exception as e:
                    print(f"Warning: Could not delete temporary file {temp_file}: {e}")