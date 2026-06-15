from risk_analyzer import RiskAnalyzer

class ContractAnalyzer:

    def __init__(self):
        self.risk = RiskAnalyzer()

    def generate_summary(self, text):
        return text[:500]

    def extract_clauses(self, text):
        clauses = []
        for key in ["payment","termination","renewal"]:
            if key in text.lower():
                clauses.append(key)
        return clauses

    def answer_question(self, question):
        return f"Generated answer for: {question}"
