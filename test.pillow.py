from PIL import Image

# Tworzymy przykładowy obraz
img = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Zapisujemy obraz
img.save('test_image.jpg')

print("Image created successfully!")