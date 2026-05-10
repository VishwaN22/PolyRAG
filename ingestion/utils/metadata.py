from datetime import datetime


def normalize_datetime(dt: datetime) -> str:
    """Normalize datetime to ISO format."""
    return dt.isoformat()