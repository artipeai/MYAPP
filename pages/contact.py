import streamlit as app
from PIL import Image

#contact image
img = Image.open("assets/contact.png")
app.image(img, width=250)

#contact info
app.subheader("Get in Touch")
app.text("Here is my contact information:")

conatct = {
        "email":"artipeai@gmail.com",
        "phone / whastsapp":"+8801404373837",
        "fb":"https://www.facebook.com/itz.niloy.597655",
        "instagram":"https://www.instagram.com/itzniloy865/",
        "github":"github.com/artipeai"

    } 

app.table(conatct)