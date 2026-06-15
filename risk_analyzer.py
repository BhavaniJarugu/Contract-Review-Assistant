class RiskAnalyzer:

    keywords = [
        "unlimited liability",
        "automatic renewal",
        "indemnification",
        "penalty"
    ]

    def analyze(self, text):
        risks = []
        for item in self.keywords:
            if item in text.lower():
                risks.append(item)
        return risks

    def score(self, text):
        return len(self.analyze(text)) * 10
