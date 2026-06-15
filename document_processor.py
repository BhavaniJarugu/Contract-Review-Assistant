from pypdf import PdfReader

class DocumentProcessor:

    async def extract_text(self, upload_file):
        data = await upload_file.read()
        try:
            with open("temp.pdf","wb") as f:
                f.write(data)
            reader = PdfReader("temp.pdf")
            return " ".join(page.extract_text() or "" for page in reader.pages)
        except Exception:
            return data.decode(errors="ignore")

    def chunk_text(self, text, size=500):
        return [text[i:i+size] for i in range(0, len(text), size)]
