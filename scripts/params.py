import gradio as gr
import modules.scripts as scripts
from modules.scripts import PostprocessImageArgs


from modules import scripts, scripts_postprocessing
from modules.processing import (
    StableDiffusionProcessing
)


class ManualParamsScript(scripts.Script):
    def title(self):
        return f"manual_params"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Accordion(f"Manual Parameters", open=False):
            with gr.Row():
                enable = gr.Checkbox(label="Enable", value=False)
                key = gr.Textbox(label="Key")
                value = gr.Textbox(label="Value")
        return [
            enable,
            key,
            value
        ]

    def postprocess_image(self, p: StableDiffusionProcessing, script_pp: PostprocessImageArgs, enable, key, value, *args):
        self.enable = enable
        self.key = key
        self.value = value

        if (not self.enable):
            return
        
        image = script_pp.image
        p.extra_generation_params[key] = value
        pp = scripts_postprocessing.PostprocessedImage(image)
        pp.info = {}
        script_pp.image = pp.image
