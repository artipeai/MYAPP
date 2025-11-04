import streamlit as app
from PIL import Image
import datetime
import json
import os
#import pyrebase

#firebase settings

#config = dict(app.secrets["firebase"])

#initialize firebase
#firebase = pyrebase.initialize_app(config)
#db = firebase.database()


img = Image.open("assets/msg.png")
app.image(img, width=250)

app.subheader("Send me a Message")
app.text("Feel free to send me a message regarding any inquiries or collaborations.")

#message_data 
msg = {}

name = app.text_input("Your Name")
email = app.text_input("Your Email")
message = app.text_area("Your Message")

send = app.button("Send Message")

if send:
    msg["name"] = name
    msg["email"] = email
    msg["message"] = message
    msg["timestamp"] = str(datetime.datetime.now())

    #db.child("messages").push(msg)

    # Save message to JSON file
    folder_path = "msgs"
    file_path = os.path.join(folder_path, "msg.json")

    # Create folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Load existing data safely
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as json_file:
            all_data = json.load(json_file)
    else:
        all_data = []

    # Append new message
    all_data.append(msg)

    # Save back to JSON
    with open(file_path, "w") as json_file:
        json.dump(all_data, json_file, indent=4)

    app.success("Message sent successfully!")

else:
    app.warning("Please fill out the form and click 'Send Message' to submit your message.")
