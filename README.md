# ChatWithPdf

ChatWithPdf (AskMyPDF in the app) is a local Streamlit demo for finding relevant passages in a PDF. PyMuPDF extracts the text, Sentence Transformers encodes the passages, and ChromaDB ranks them by relevance to your question. The app shows excerpts from the document.

## Run locally

Use Python 3.11 or 3.12. On first run, Sentence Transformers downloads the `all-MiniLM-L6-v2` model from Hugging Face.

```sh
git clone https://github.com/samrudhi-builds/ChatWithPdf.git
cd ChatWithPdf
```

Create and activate a virtual environment.

**Linux or macOS**

```sh
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies and start Streamlit from the repository root.

```sh
python -m pip install -r requirements.txt
python -m streamlit run askmypdf/app.py --server.address 127.0.0.1
```

Open [http://127.0.0.1:8501](http://127.0.0.1:8501).

## Try it

1. Upload a PDF with selectable text. Scanned pages need OCR before upload.
2. Enter a question and read the matching passage excerpts.
3. Use **Reset (Upload New PDF)** before uploading a revised file with the same name.

## Local data

The demo is designed for one local user. It saves the uploaded file as `temp.pdf` and stores extracted passages in `chroma_db/` in the working directory. Indexing a new document replaces the previous index contents. To clear the saved data, stop Streamlit and delete `temp.pdf` and `chroma_db/`.
