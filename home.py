import streamlit as app
from PIL import Image

#sidebar
app.sidebar.title("Fahim's web")
app.sidebar.success("select pages above")
app.sidebar.text("Coded by Fahim soft labs")

#app title
app.title("Welcome to my website")
app.header("About me")

#my image
img = Image.open("assets/profile.jpg")
app.image(img, width=250)

#personal info
my_info = {
    "text":"Hello! My name is Fahim. I am a software developer with a passion for creating web applications and exploring new technologies. In my free time, I enjoy hiking, reading books, and experimenting with new programming languages.",
}
app.text(my_info["text"])