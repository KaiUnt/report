import PyPDF2
import re

def extract_athlete_sections(pdf_path, source_name):
    """Extrahiere die Abschnitte der Athleten basierend auf BIB-Nummern."""
    reader = PyPDF2.PdfReader(pdf_path)
    sections = []
    current_start = None
    current_bib = None

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        match = re.search(r"Profile of .* \(BIB #(\d+)\)", text)
        if match:
            bib_number = int(match.group(1))
            if current_start is not None:
                sections.append((current_bib, source_name, current_start, page_num - 1))
            current_start = page_num
            current_bib = bib_number

    if current_start is not None:
        sections.append((current_bib, source_name, current_start, len(reader.pages) - 1))

    return sections, reader

def merge_and_sort_athletes(pdf1_path, pdf2_path, output_path):
    """Merge und sortiere PDFs nach BIB-Nummern."""
    sections1, reader1 = extract_athlete_sections(pdf1_path, "pdf1")
    sections2, reader2 = extract_athlete_sections(pdf2_path, "pdf2")

    all_sections = sections1 + sections2
    all_sections.sort(key=lambda x: x[0])  # Sortiere nach BIB-Nummer

    writer = PyPDF2.PdfWriter()
    for bib, source, start, end in all_sections:
        reader = reader1 if source == "pdf1" else reader2
        for page_num in range(start, end + 1):
            writer.add_page(reader.pages[page_num])

    with open(output_path, "wb") as output_file:
        writer.write(output_file)
    print(f"Sortiertes und zusammengeführtes PDF erstellt: {output_path}")

# Beispielnutzung
pdf1_path = r"C:\Users\kaiun\Downloads\report_325526 (1).pdf"
pdf2_path = r"C:\Users\kaiun\Downloads\report_325660 (1).pdf"
output_path = r"C:\Users\kaiun\Downloads\merged_sorted.pdf"

merge_and_sort_athletes(pdf1_path, pdf2_path, output_path)
