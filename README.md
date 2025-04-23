
# diffusion-avatar-generator
AI-powered avatar generator using Stable Diffusion

# Diffusion Avatar Generator

AI-powered tool to generate stylish avatars or artistic photos from your selfies using Stable Diffusion and prompt engineering.

## Features
- Upload a selfie or portrait
- Choose a style (Anime, Cyberpunk, Oil Painting, etc.)
- Generate artistic avatars using Stable Diffusion
- Interactive web interface with Gradio

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

## Project Structure
- `app.py`: Gradio web interface
- `pipeline.py`: Core inference logic
- `prompts/styles.json`: Predefined styles for generation
- `inputs/`: Folder for input images
- `outputs/`: Folder for generated images

Created as a self-employed OPT project by Dahai Hao.

