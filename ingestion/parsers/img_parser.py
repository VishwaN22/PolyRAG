from PIL import Image
import pytesseract
from ingestion.raw_data import RawData
from ingestion.utils import config


pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH

def parse_image(file: str) -> RawData:
    """Parse an image file and return its text content."""
    image = Image.open(file)
    text = pytesseract.image_to_string(image)
    return RawData(text=text, metadata={"title": file})