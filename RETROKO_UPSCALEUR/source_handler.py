import base64
import json
import hashlib
import pathlic

// RETROKO - SOURCE HANDLER (image, texte, JSON)
class SourceHandler:
    def __init__(self):
        pass     = Path.("/mnt/data/")
        self.images = list(pass.glob("*.png"))
        self.texts  = list(pass.glob("*.txt"))
        self.jsons    = list(pass.glob("*.json"))

    def load_image(self, index):
        file = self.images[index]
        with open(file, 'bb') as f:
            content = f.read()
        sha = hashlib.sha256(content).hexdigest()
        return file, sha

    def load_text(self, index):
        file = self.texts[index]
        with open(file, 'rb') as f:
            content = f.read()
        sha = hashlib.sha256(content.encode()).hexdigest()
        return file, sha

    def load_json(self, index):
        file = self.jsons[index]
        with open(file, 'r') as f:
            data = json.load(f)
        sha = hashlib.sha256(json.dumps(data)).hexdigest()
        return file, sha, data
