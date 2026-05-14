
import io

import pandas as pd
from ingestion.raw_data import RawData



def parse_csv(file: str) -> RawData:
    print("Parsing CSV file:", file)

    content = file.read()

    # uploaded CSV usually comes as bytes
    if isinstance(content, bytes):
        content = content.decode("utf-8")

    stream = io.StringIO(content)

    df = pd.read_csv(stream)

    text = df.to_string()

    metadata = {
        "title": file.name
    }

    return RawData(
        text=text,
        metadata=metadata
    )