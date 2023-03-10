import gradio as gr
import pyshorteners

def shortenurl(name):
    shortener = pyshorteners.Shortener()
    return (shortener.tinyurl.short(name))




app = gr.Interface(fn=shortenurl, inputs="text", outputs="text")

app.launch()  
