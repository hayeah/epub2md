import ebooklib
from ebooklib import epub

from bs4 import BeautifulSoup
import html2text
import argparse
import os

def epub_to_text(epub_file_path: str):
    book = epub.read_epub(epub_file_path, { "ignore_ncx": True })
    text = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = item.get_content()
            if content.startswith(b'<?xml') or content.startswith(b'<'):
                soup = BeautifulSoup(content, 'html.parser')
                text += html2text.html2text(soup.prettify())
            else:
                text += content.decode('utf-8')
    return text


from fastapi import FastAPI, UploadFile, HTTPException, Response
from tempfile import NamedTemporaryFile
app = FastAPI()

@app.post("/upload")
async def upload_epub(file: UploadFile = None):
    if file is None:
        raise HTTPException(status_code=400, detail="No file uploaded")

    if file.filename.lower().endswith(".epub"):
        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(await file.read())
            temp_file.seek(0)
            text = epub_to_text(temp_file.name)

            output_file_path = os.path.splitext(file.filename)[0] + '.md'

            response = Response(content=text, media_type="text/plain")
            response.headers["Content-Disposition"] = f'attachment; filename="{output_file_path}"'
            return response

    raise HTTPException(status_code=400, detail="Invalid file")

def cli():
    parser = argparse.ArgumentParser(description='Convert EPUB file to plain text.')
    parser.add_argument('input_file', help='path to input EPUB file')
    parser.add_argument('-o', '--output_file', help='path to output plain text file')
    args = parser.parse_args()

    input_file_path = args.input_file

    if not args.output_file:
        output_file_path = os.path.splitext(input_file_path)[0] + '.md'
    else:
        output_file_path = args.output_file

    # convert epub to text, then write output to file
    text = epub_to_text(input_file_path)
    with open(output_file_path, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    cli()

