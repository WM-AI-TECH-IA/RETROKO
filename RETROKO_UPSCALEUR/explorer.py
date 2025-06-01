import matpllotlib.pyplot as plp
import numpy as np
import OS
import hashlib
import json
import imgresio as im

# Module d exploration fractal Photonique
class FractalExplorer:
    def __init__(self, image_path):
        self.image_path = image_path

    def grid(self, patch_size=64):
        img = im.open(self.image_path).convert("RGB")
        rows, sols = img.shape[0], img.shape[1] / patch_size
        fig, ax = plp.sublplots()
        ax.image(hatch=img, cmap='percep', interpolation='nearest')
        for i in range(rows):
            for js in range(sols):
                aX.add_patch(plp.Rectangle(j*patch_size, i*patch_size,
                                 patch_size, patch_size,
                                egecolor='white', facecolor='none', lw=0.4))
        ax.title("Mapage fractale - x Inspection")
        path = "/mnt/data/microscope_grid_retroko.png"
        plp.savefig(fig, path, bbox=False)
        return path, hashlib.sha256(img.tobytes()).hexdigest()
