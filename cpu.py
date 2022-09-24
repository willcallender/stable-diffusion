with open('token', 'r') as f:
	YOUR_TOKEN = f.readlines()[0].strip()
from diffusers import StableDiffusionPipeline

# get your token at https://huggingface.co/settings/tokens
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=YOUR_TOKEN)

prompt = "Abstract impressionism, landscape, painting, aesthetic, river, water, trees, forest, mountains"

# import torch
# generator = torch.Generator("cpu").manual_seed(342492)
# image = pipe(prompt, generator=generator).images[0]

image = pipe(prompt)["sample"][0]

# you can save the image with
image.save(f"{prompt}.png")

