class PDFStyles:
    def __init__(self):
        # Colors
        self.colors = {
            'header_bg': (52, 152, 219),      # Light blue
            'stats_bg': (240, 248, 255),      # Light blue background
            'info_bg': (245, 245, 245),       # Light gray
            'table_header': (230, 230, 230),  # Gray
            'table_alt_row': (250, 250, 250), # Light gray
        }
        
        # Font configurations
        self.fonts = {
            'title': ('Arial', 'B', 16),
            'header': ('Arial', 'B', 14),
            'subheader': ('Arial', 'B', 12),
            'normal': ('Arial', '', 10),
            'small': ('Arial', '', 9)
        }
        
        # Layout settings
        self.margins = {
            'left': 10,
            'right': 10,
            'top': 10,
            'cell_height': 6,
            'section_spacing': 5
        }

    def apply_title_style(self, pdf):
        font, style, size = self.fonts['title']
        pdf.set_font(font, style, size)
        
    def apply_header_style(self, pdf):
        font, style, size = self.fonts['header']
        pdf.set_font(font, style, size)
        pdf.set_fill_color(*self.colors['header_bg'])
        
    def apply_subheader_style(self, pdf):
        font, style, size = self.fonts['subheader']
        pdf.set_font(font, style, size)
        
    def apply_normal_style(self, pdf):
        font, style, size = self.fonts['normal']
        pdf.set_font(font, style, size)

    def apply_table_header_style(self, pdf):
        font, style, size = self.fonts['small']
        pdf.set_font(font, 'B', size)
        pdf.set_fill_color(*self.colors['table_header'])