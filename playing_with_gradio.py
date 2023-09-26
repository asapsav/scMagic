# import gradio as gr
# import numpy as np
# import time

# # define core fn, which returns a generator {steps} times before returning the image
# def fake_diffusion(steps):
#     for _ in range(steps):
#         time.sleep(.1)
#         image = np.random.random((100, 100, 3))
#         yield image
#     image = "https://gradio-builds.s3.amazonaws.com/diffusion_image/cute_dog.jpg"
#     yield image


# demo = gr.Interface(fake_diffusion, inputs=gr.Slider(1, 10, 3, step =1), outputs="image")

# # define queue - required for generators
# demo.queue()

# demo.launch(share=False, auth=("admin", "pass1234"))

from fastapi import FastAPI
import gradio as gr

CUSTOM_PATH = "/gradio"

app = FastAPI()


@app.get("/")
def read_main():
    return {"message": "This is your main app"}


io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)