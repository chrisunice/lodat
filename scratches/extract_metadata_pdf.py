import re
import xml.etree.ElementTree as ET
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1


def extract_metadata_pdf(pdf_path: str) -> dict:

    # Read the file
    with open(pdf_path, 'rb') as pdf:
        doc = PDFDocument(PDFParser(pdf))
        metadata = resolve1(doc.catalog.get('Metadata'))

    # Decode the binary data
    metadata = metadata.get_data().decode('utf-8')

    # Get the identifier
    pattern = r'xmlns:metacom="([^"]+)"'
    uid = re.findall(pattern, metadata)[0]

    # Structure as XML
    root = ET.fromstring(metadata)

    return {element.tag.lstrip('{'+uid+'}'): element.text for element in root.iter() if uid in element.tag}
