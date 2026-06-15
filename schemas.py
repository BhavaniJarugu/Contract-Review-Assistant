from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

class SummaryResponse(BaseModel):
    summary: str

class RiskResponse(BaseModel):
    risks: list[str]

class ContractResponse(BaseModel):
    content: str
