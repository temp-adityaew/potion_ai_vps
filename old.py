from ultralytics import YOLO
from PIL import Image
import io
import base64

# Load a model
model = YOLO("models/last_100epochs.pt")

def detect_image(image_path):
    # Load image
    image = Image.open(image_path)

    # Perform detection
    results = model.predict(source=image, save=True)  # save plotted images

    # Convert the detected image to bytes
    img_byte_array = io.BytesIO()
    results.imgs[0].save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()

    # Convert bytes to base64 string
    base64_image = base64.b64encode(img_byte_array).decode('utf-8')

    return base64_image

def main():
    image_path = "images/pothole3.jpg"
    base64_image = detect_image(image_path)
    print(base64_image)

if __name__ == "__main__":
    main()
