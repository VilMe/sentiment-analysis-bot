from textblob import TextBlob
from dataclasses import dataclass



@ dataclass
class Mood:
    emoji: str
    sentiment: float
