import gradio as gr
from pipeline import generate_image

def inference(image, style):
    return generate_image(image, style)

demo = gr.Interface(
    fn=inference,
    inputs=[
        gr.Image(type="pil", label="Upload a selfie"),
        gr.Textbox(label="Enter a style prompt (e.g., 'cyberpunk portrait')")
    ],
    outputs=gr.Image(label="Generated Avatar"),
    title="Diffusion Avatar Generator",
    description="Upload a selfie and get a stylized avatar using Stable Diffusion"
)

if __name__ == "__main__":
    demo.launch()
