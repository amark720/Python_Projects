'''
Install essential libraries using pip command-> !pip install PyPDF2 pdfplumber pymupdf reportlab
'''

# Extract Text from the PDF File.
import pdfplumber
def extract_text(pdf_path, output_txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'
        with open(output_txt_path, 'w') as f:
            f.write(full_text)
        print(f"Extracted text saved as {output_txt_path}")
# Usage
extract_text('PDF_Merged.pdf', 'output.txt')