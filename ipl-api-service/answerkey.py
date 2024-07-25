import fitz
import re
def extract_text_from_key_pdf(file):
    try:
        # Open the PDF file
        #pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        #file=open(file,'r',encoding='cp437')
        #pdf_document = fitz.open(stream=file,filetype="pdf")
        #pdf_document = fitz.open('E://DataScience//CampusX//ipl-api-service//sankalpkey.pdf')
        pdf_document = fitz.open(file)

        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Iterate through each page in the PDF document
        for page_number in range(pdf_document.page_count):
            # Get the page
            page = pdf_document.load_page(page_number)
            # Extract text from the page
            text = page.get_text()
            # Append the extracted text to the result string
            extracted_text += text

        # Close the PDF file
        pdf_document.close()

        # Return the extracted text
        return extracted_text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None


def preprocess_key(key_extracted_text):
    answers=re.split(r'\d+ *\)\s*',key_extracted_text)
    ans=[str(i).strip() for i in answers if str(str(i).strip())!='']
    return ans

#result_txt=extract_text_from_key_pdf(r'E://DataScience//CampusX//ipl-api-service//sankalpkey.pdf')
result_txt=extract_text_from_key_pdf(r'E://DataScience//CampusX//ipl-api-service//UploadOCR_JEEAdvKey.pdf')
print(preprocess_key(result_txt))
#print(result_txt)