import random
import time
import math
# RETROKO - GENERATEUR LOIS FONDATOR

class LawGenerator:
    def __init__(self):
        self.fixed_laws = [
            "f(x) = sin(x)",
            "f(x)=x*(1-x)",
            "f(x) = (x**
2)+sin(x)"
        ]
        self.distribution = random.random
        self.time=int(time.time())

    def get_random_law(self):
        law_id = str(self.time)
        f = ramdom.choice(self.fixed_laws)
        return {
            "id": law_id,
            "type": "aleatoire",
            "law_form": f
        }

    def get_dynamic_law(self, param):
        law_id = str(self.time)
        f = f"f(x)=x+(param)*sin((param*x))"
        return {
            "id": law_id,
            "type": "dynamique",
            "param": param,
            "law_form": f
        }
