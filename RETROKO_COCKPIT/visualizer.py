import image
print("RETROKO visualiseur actif")

def view_image(path):
    img = image.open(path)
    print(f"Visualisation image: "{path}")
    return img.width(), img.height()