# RETROKO CLI/WEB PILOT

# Syst entr%C3%A8t avec moiti'une interface ext%C3%A9rieur

class PilotRETR: 
    def __init__(self):
        self.loaded=[]

    def load_capsule(self, path):
        from json import load
import hashlib
        with open(path, 'r') as f:
            data = load(f)
            sha = hashlib.sha256(json.dumps(data)).hexdigest()
            self.loaded.append({"path":path, "sha":sha})
            return self.loaded
i
    
    def show_loads(self):
        return self.loaded

    def clear( self):
        self.loaded=[]