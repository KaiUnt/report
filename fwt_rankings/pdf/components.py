class PDFComponents:
    def __init__(self, pdf):
        self.pdf = pdf
        
    def add_athlete_header(self, athlete_data):
        """Add detailed athlete header section."""
        text_width = self.pdf.w - self.pdf.l_margin - self.pdf.r_margin - 70  # 70mm for image
        cell_height = 6
        
        # Athlete info box
        self.pdf.set_fill_color(245, 245, 245)
        self.pdf.rect(self.pdf.l_margin, self.pdf.get_y(), text_width, 30, 'F')
        
        start_y = self.pdf.get_y() + 2
        self.pdf.set_xy(self.pdf.l_margin + 5, start_y)
        
        # Basic Info
        self.pdf.set_font('Arial', 'B', 14)
        self.pdf.safe_cell(text_width-10, cell_height, athlete_data['name'], ln=True)
        
        self.pdf.set_font('Arial', '', 10)
        if athlete_data.get('nationality'):
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, cell_height-2, 
                             f"Nationality: {athlete_data['nationality']}", ln=True)
            
        if athlete_data.get('dob'):
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, cell_height-2, 
                             f"Date of Birth: {athlete_data['dob']}", ln=True)
                             
        self.pdf.ln(5)

    def add_statistics_section(self, stats, text_width):
        """Add detailed statistics section."""
        # Stats box
        self.pdf.set_fill_color(240, 248, 255)  # Light blue background
        box_height = 40
        self.pdf.rect(self.pdf.l_margin, self.pdf.get_y(), text_width, box_height, 'F')
        
        start_y = self.pdf.get_y() + 2
        self.pdf.set_xy(self.pdf.l_margin + 5, start_y)
        
        # Title
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.safe_cell(text_width-10, 7, "Career Statistics", ln=True)
        
        # Stats content
        self.pdf.set_font('Arial', '', 10)

        # Best Result: by_points and by_rank
        if stats.get('best_result'):
            best_by_points = stats['best_result'].get('by_points')
            best_by_rank = stats['best_result'].get('by_rank')
            
            if best_by_points:
                self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
                self.pdf.safe_cell(text_width-10, 6,
                    f"Best Result by Points: {best_by_points.points} points at {best_by_points.event_name} (Place: {best_by_points.place})", ln=True)
            
            if best_by_rank:
                self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
                self.pdf.safe_cell(text_width-10, 6,
                    f"Best Result by Rank: {best_by_rank.place}. Place at {best_by_rank.event_name} (Points: {best_by_rank.points})", ln=True)
            
        #Oldest result
        if stats.get('oldest_result'):
            oldest_result = stats['oldest_result']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(
                text_width - 10, 6,
                f"Oldest Result: {oldest_result.event_name} on {oldest_result.date.strftime('%Y-%m-%d')} "
                f"(Place: {oldest_result.place}, Points: {oldest_result.points})", ln=True
            )

        # Best Series: Place
        if stats.get('best_series_place'):
            best_series = stats['best_series_place']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Series: {best_series.place}. Place in {best_series.series_name} ({best_series.points} points)", ln=True)

        # Best Pro Series: Overall Place and Event by Points
        if stats.get('best_pro_place'):
            best_pro_place = stats['best_pro_place']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Pro Series: {best_pro_place.place}. Place in {best_pro_place.series_name} ({best_pro_place.points} points)", ln=True)

        if stats.get('best_pro_event'):
            best_pro_event = stats['best_pro_event']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Event in Pro Series: {best_pro_event.points} points at {best_pro_event.event_name} (Place: {best_pro_event.place})", ln=True)

        # Best Challenger Series: Overall Place and Event by Points
        if stats.get('best_challenger_place'):
            best_challenger_place = stats['best_challenger_place']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Challenger Series: {best_challenger_place.place}. Place in {best_challenger_place.series_name} ({best_challenger_place.points} points)", ln=True)

        if stats.get('best_challenger_event'):
            best_challenger_event = stats['best_challenger_event']
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width-10, 6,
                f"Best Event in Challenger Series: {best_challenger_event.points} points at {best_challenger_event.event_name} (Place: {best_challenger_event.place})", ln=True)

        if stats.get('total_events'):
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width - 10, 6,
                f"Total Events: {stats['total_events']}", ln=True)

        if stats.get('total_series'):
            self.pdf.set_xy(self.pdf.l_margin + 5, self.pdf.get_y() + 2)
            self.pdf.safe_cell(text_width - 10, 6,
                f"Total Series: {stats['total_series']}", ln=True)


        self.pdf.ln(5)
