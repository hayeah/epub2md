# Epub to Plain Text Converter

This application converts an EPUB file to plain text format. You can use it as a command line interface (CLI) tool or run it as an HTTP service.

## Installation

Install the required dependencies using `pipenv`:

```
pipenv install
```

## Usage

### CLI

To convert an EPUB file to plain text using the CLI, run the following command:

```
pipenv run python3 main.py <input_epub_file>
```

Example:

```
pipenv run python3 main.py alice-in-wonderland.epub
```

The plain text output will be saved in the same directory as the input EPUB file.

### HTTP Service

To start the HTTP service, run the following command:

```
uvicorn main:app --reload
```

#### Uploading an EPUB File

To convert an EPUB file by uploading it, send a POST request with the file to the `/upload` endpoint:

```
curl -X POST -F "file=@<input_epub_file>" http://localhost:8000/upload -o <output_md_file>
```

Example:

```
curl -X POST -F "file=@alice-in-wonderland.epub" http://localhost:8000/upload -o alice.md
```

#### Providing a URL to an EPUB File

To convert an EPUB file by providing its URL, send a POST request with the URL to the `/upload` endpoint:

```
curl -X POST "http://localhost:8000/upload?url=<url_encoded_epub_url>" -o <output_md_file>
```

Example:

```
curl -X POST "http://localhost:8000/upload?url=https%3A%2F%2Fwww.gutenberg.org%2Febooks%2F11.epub.noimages" -o "alice.md"
```

# Production

```
curl -X POST "https://epub2md.vercel.app/upload?url=https%3A%2F%2Fwww.gutenberg.org%2Febooks%2F11.epub.noimages" -o "alice.md"
```

## License

This project is licensed under the terms of the MIT License.
