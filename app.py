from flask import Flask, request, render_template, redirect, url_for, send_file
from pdf2image import convert_from_path  # Import function to convert PDF to images
import pytesseract  # Import Tesseract OCR library
from PIL import Image  # Import Python Imaging Library to work with images
from fpdf import FPDF  # Import FPDF library to create PDF files
import os  # Import os module for file operations

app = Flask(__name__)  # Initialize Flask application

# Specify the path to the Tesseract executable (replace with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert PDF pages to images using pdf2image library
def pdf_to_images(pdf_path):
    # Specify the path to Poppler's `bin` directory (replace with your path)
    poppler_path = r'C:\Users\kmmay\Desktop\poppler\poppler-24.02.0\Library\bin'
    images = convert_from_path(pdf_path, poppler_path=poppler_path)  # Convert PDF to list of PIL.Image objects
    return images  # Return list of images

# Function to perform OCR on an image and extract text using pytesseract
def ocr_on_image(image):
    text = pytesseract.image_to_string(image)  # Use Tesseract to do OCR on image
    return text  # Return extracted text

# Function to create a PDF file from text using FPDF library
def create_pdf_from_text(text, output_path):
    pdf = FPDF()  # Create FPDF object
    pdf.add_page()  # Add a page to the PDF
    pdf.set_auto_page_break(auto=True, margin=15)  # Set automatic page break
    pdf.add_font("DejaVu", "", r"C:\Users\kmmay\pdf_to_ocr_converter\dejavu-sans\DejaVuSans.ttf", uni=True)  # Add Unicode font (optional)
    pdf.set_font("DejaVu", size=12)  # Set font with Unicode support (optional)

    for line in text.split('\n'):  # Iterate over each line of text
        pdf.multi_cell(0, 10, line.encode('latin-1', 'replace').decode('latin-1'))  # Encode/decode text to latin-1

    pdf.output(output_path)  # Output PDF to specified path

# Route for handling both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # If the request method is POST
        if 'pdf_file' not in request.files:  # If no file part in request
            return redirect(request.url)  # Redirect to the same URL
        file = request.files['pdf_file']  # Get the PDF file from the request
        if file.filename == '':  # If no selected file
            return redirect(request.url)  # Redirect to the same URL
        if file and file.filename.endswith('.pdf'):  # If file is a PDF
            file_path = os.path.join('uploads', file.filename)  # Path to save the uploaded file
            file.save(file_path)  # Save the uploaded file to disk
            images = pdf_to_images(file_path)  # Convert PDF to images
            ocr_text = ""  # Initialize empty string for OCR text
            
            # Perform OCR on each image and concatenate the results
            for img in images:
                ocr_text += ocr_on_image(img) + "\n"
            
            # Create a PDF file from the OCR text
            output_pdf_path = os.path.join('uploads', 'ocr_output.pdf')  # Path to save generated PDF
            create_pdf_from_text(ocr_text, output_pdf_path)  # Generate PDF from OCR text
            
            # Return the generated PDF file for download
            return send_file(output_pdf_path, as_attachment=True)  # Send generated PDF as an attachment
    
    # Render the HTML template with or without OCR text
    return render_template('index.html', ocr_text="")

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    if not os.path.exists('uploads'):  # If uploads directory doesn't exist
        os.makedirs('uploads')  # Create uploads directory
    app.run(debug=True)  # Run the Flask application in debug mode
