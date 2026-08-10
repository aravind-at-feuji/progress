from huggingface_hub import InferenceClient
from PIL import Image
client = InferenceClient(api_key=HF_TOKEN)
# Generate an image from text
image = client.text_to_image(
   "Astronaut riding a horse",
   model="stabilityai/stable-diffusion-xl-base-1.0"
)
# Display or save the image
image.show()
image.save("output_image.png")