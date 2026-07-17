import google.generativeai as genai
import gradio as gr

genai.configure(api_key="")

def generate_blog(topic,audience,language,tone,words,terminology):
  prompt=f"""
  write a {words}-word blog.
  Topic: {topic}
  Audience: {audience}
  language: {language}
  tone: {tone}
  terminology: {terminology}
  Include:
  -Introduction
  -Fun facts
  -Advantages
  -Conclusion"""
  model = genai.GenerativeModel('gemini-pro')
  response=model.generate_content(prompt)
  return response.text

demo=gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Audience"),
        gr.Dropdown(
            ["telugu","hindi","english","kannada","marathi"],
            label="language"
            ),
        gr.Dropdown(
            ["proffessional","casual","funny","Technical","inspiration","sarcastic"],
            label="Tone"
        ),
        gr.Dropdown(
            ["simple","moderate","complex"],
            label="terminology"
        ),
        gr.Slider(100,1200,value=500,label="word count")
    ],
    outputs="markdown",
    title="AI Blog Generator (Gemini)"
        )
demo.launch()
