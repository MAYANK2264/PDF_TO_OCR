# PDF_TO_OCR
JUST LEARNING NEW THINGS AND MAKING A PROGRAM TO CONVERT A NON EDITABLE PDF TO AN OCR PDF
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PDF to OCR Converter Setup Guide</title>
</head>
<body>

<h1>PDF to OCR Converter Web Application</h1>

<p>This web application converts PDF files to searchable text using Optical Character Recognition (OCR). It allows users to upload PDFs, extract text using Tesseract OCR, and download the extracted text as a new PDF.</p>

<h2>Prerequisites</h2>

<ol>
  <li><strong>Python Installation:</strong>
    <ul>
      <li>Install Python from <a href="https://www.python.org/downloads/">python.org</a>.</li>
      <li>Make sure to add Python to your system PATH during installation.</li>
    </ul>
  </li>
  
  <li><strong>Install Required Packages:</strong>
    <ul>
      <li>Open a command prompt or terminal.</li>
      <li>Install necessary Python packages using pip:
        <pre><code>pip install flask pdf2image pytesseract Pillow fpdf</code></pre>
      </li>
    </ul>
  </li>
  
  <li><strong>Install Tesseract OCR:</strong>
    <ul>
      <li>Download and install Tesseract OCR from <a href="https://github.com/tesseract-ocr/tesseract">GitHub</a>.</li>
      <li>Add Tesseract to your system PATH during installation.</li>
    </ul>
  </li>
  
  <li><strong>Install Poppler:</strong>
    <ul>
      <li>Download Poppler from <a href="https://poppler.freedesktop.org/">poppler.freedesktop.org</a>.</li>
      <li>Extract the Poppler archive to a directory (e.g., <code>C:\poppler-xx.xx.x\</code>).</li>
      <li>Add the <code>bin</code> directory inside Poppler to your system PATH.</li>
    </ul>
  </li>
  
  <li><strong>Optional: Download DejaVu Fonts:</strong>
    <ul>
      <li>If using Unicode characters, download DejaVu fonts (e.g., DejaVu Sans) and place the <code>.ttf</code> file in a directory accessible to Python.</li>
    </ul>
  </li>
</ol>

<h2>Setup Instructions</h2>

<ol>
  <li><strong>Clone Repository:</strong>
    <ul>
      <li>Clone this repository to your local machine:
        <pre><code>git clone https://github.com/your-username/pdf-to-ocr-converter.git</code></pre>
      </li>
    </ul>
  </li>
  
  <li><strong>Configure Paths:</strong>
    <ul>
      <li>Open <code>app.py</code> in a text editor.</li>
      <li>Modify the following paths in <code>app.py</code>:
        <ul>
          <li><code>pytesseract.pytesseract.tesseract_cmd</code>: Path to Tesseract executable (<code>tesseract.exe</code>).</li>
          <li><code>poppler_path</code>: Path to Poppler's <code>bin</code> directory.</li>
        </ul>
      </li>
    </ul>
  </li>
  
  <li><strong>Run the Application:</strong>
    <ul>
      <li>Open a command prompt or terminal.</li>
      <li>Navigate to the project directory:
        <pre><code>cd pdf-to-ocr-converter</code></pre>
      </li>
      <li>Run the Flask application:
        <pre><code>python app.py</code></pre>
      </li>
    </ul>
  </li>
  
  <li><strong>Access the Application:</strong>
    <ul>
      <li>Open a web browser and go to <code>http://127.0.0.1:5000/</code>.</li>
      <li>You should see the home page of the PDF to OCR converter.</li>
    </ul>
  </li>
</ol>

<h2>Usage</h2>

<ol>
  <li><strong>Upload a PDF File:</strong>
    <ul>
      <li>Click "Choose File" and select a PDF to upload.</li>
      <li>Click "Upload" to initiate the conversion process.</li>
    </ul>
  </li>
  
  <li><strong>Convert PDF to OCR:</strong>
    <ul>
      <li>The application converts the PDF to images, performs OCR using Tesseract, and extracts text.</li>
      <li>Extracted text is displayed on the web page.</li>
    </ul>
  </li>
  
  <li><strong>Download Extracted Text:</strong>
    <ul>
      <li>Click "Download PDF" to download a new PDF file containing the extracted text.</li>
    </ul>
  </li>
</ol>

<h2>Notes</h2>

<ul>
  <li><strong>File Storage:</strong> Uploaded PDFs are stored temporarily in the <code>uploads</code> directory. Ensure this directory is writable by the application.</li>
  <li><strong>Adjustments:</strong> Modify configurations and paths in <code>app.py</code> as per your environment setup.</li>
</ul>

</body>
</html>

