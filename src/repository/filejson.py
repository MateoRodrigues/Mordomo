import json
from pathlib import Path

class FileJSONRepository:
    def __init__(self):
        self.file_path = Path(__file__).parent.parent.parent / 'data' / 'service.json'