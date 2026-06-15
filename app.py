from fastapi import FastAPI, UploadFile
from schemas import AskRequest
from document_processor import DocumentProcessor
from contract_analyzer import ContractAnalyzer

app = FastAPI(title="Contract Review Assistant")
processor = DocumentProcessor()
analyzer = ContractAnalyzer()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/summary")
async def summary(file: UploadFile):
    text = await processor.extract_text(file)
    return {"summary": analyzer.generate_summary(text)}

@app.post("/ask")
def ask(req: AskRequest):
    return {"answer": analyzer.answer_question(req.question)}
