from dataclasses import dataclass

@dataclass
class RawData:
    """A class to represent raw data."""
    text: str
    metadata: dict