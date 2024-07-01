'''
Install essential libraries using pip command-> !pip install PyPDF2 pdfplumber pymupdf reportlab
'''

# Extract images from the PDF File.
import fitz # PyMuPDF
def extract_images(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)
    for page_index in range(len(pdf_document)):
        page = pdf_document.load_page(page_index)
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = f"{output_dir}/image_{page_index + 1}_{img_index + 1}.{image_ext}"
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
            print(f"Saved {image_filename}")
# Usage
extract_images('PDF_Merged.pdf', 'Final_Extracted_Images')