from dataclasses import dataclass

@dataclass
class Contract:
    name: str
    content: str

@dataclass
class Clause:
    title: str
    text: str

@dataclass
class Risk:
    level: str
    description: str
