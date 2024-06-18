import fitz # type: ignore

def extract_biology_marks(pdf_path):
    total_biology_marks = 0

    # Open the PDF file
    document = fitz.open(pdf_path)

    # Loop through the pages for groups 1 to 24 (assuming each group corresponds to one page)
    for page_number in range(24):  # Pages are zero-indexed
        page = document.load_page(page_number)
        text = page.get_text("text")
        
        # Extract the marks from the text
        lines = text.split('\n')
        for line in lines:
            data = line.split()
            if len(data) >= 6:  # Assuming the structure: [Name, Subject1, Subject2, ..., Biology]
                try:
                    biology_marks = int(data[5])
                    if biology_marks >= 74:
                        total_biology_marks += biology_marks
                except ValueError:
                    # In case the data is not an integer (like header or footer text)
                    continue

    return total_biology_marks

pdf_path = "C:\\Users\\Ritesh\\Documents\\github\\tds\\week2\\data\\ga2.9.pdf"
total_biology_marks = extract_biology_marks(pdf_path)
print(f"Total Biology marks of students who scored 74 or more in Biology in groups 1-24: {total_biology_marks}")
