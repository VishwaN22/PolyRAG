from ingestion.loader import parse_file


class MockFile:
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1]

    def read(self):
        with open(self.path, "rb") as f:
            return f.read()


file = MockFile("data\\rbidsim.png")

documents = parse_file(file)


print("=" * 50)
print(documents.metadata)
print("=" * 50)
print(documents.text[:500])