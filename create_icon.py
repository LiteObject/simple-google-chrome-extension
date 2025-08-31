from PIL import Image, ImageDraw, ImageFont
import os

# Create a 128x128 image with green background
img = Image.new('RGB', (128, 128), color='#4CAF50')
draw = ImageDraw.Draw(img)

# Try to use a font, fallback to default if not available
try:
    font = ImageFont.truetype("arial.ttf", 72)
except:
    font = ImageFont.load_default()

# Draw white 'H' in the center
text = "H"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (128 - text_width) // 2
y = (128 - text_height) // 2
draw.text((x, y), text, fill='white', font=font)

# Save the image
img.save('icon.png')
print("Icon created successfully!")
