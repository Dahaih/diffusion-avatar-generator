from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(input_image, prompt):
    image = pipe(prompt=prompt, image=input_image).images[0]
    return image
