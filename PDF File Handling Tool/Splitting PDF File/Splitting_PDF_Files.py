'''
Install essential libraries using pip command-> !pip install PyPDF2 pdfplumber pymupdf reportlab
'''

# Splitting PDF file to multiple PDF files/Pages.
import PyPDF2


def split_pdf(pdf_path, output_dir):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = f"{output_dir}/page_{page_num + 1}.pdf"
        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
        print(f"Saved {output_path}")


# Usage
split_pdf('PDF_Merged.pdf', 'split_pdf_files')