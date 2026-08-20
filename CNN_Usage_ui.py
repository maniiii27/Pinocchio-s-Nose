import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from IPython.display import display

model = load_model("my_model.h5")
classes = ["REAL", "FAKE"]

import numpy as np

def preprocess_and_predict_image(image):
    image_rgb = image.convert('RGB')
    resized_image = image_rgb.resize((32, 32))
    resized_np = np.array(resized_image)
    normalized_image = resized_np / 255.0
    reshaped_image = normalized_image.reshape(1, 32, 32, 3)

    prediction = model.predict(reshaped_image)

    if prediction[0][0] > 0.5:
        predicted_class = "REAL"
        print(prediction[0][0])
    else:
        predicted_class = "FAKE"
        print(prediction[0][0])
    
    return predicted_class

# def login():
#     st.markdown(
#             f"""
#             <style>
#             .stApp {{
#                 background-image: url("https://media.licdn.com/dms/image/D4D12AQFbZfiSO7Hzfg/article-cover_image-shrink_720_1280/0/1697613632807?e=1718841600&v=beta&t=HcrHz0AExQDccQy8bh6BnhBI3CsPqAUnaCEMAW5Hm5s");
#                 background-attachment: fixed;
#                 background-size: cover;
#             }}
#             </style>
#             """,
#             unsafe_allow_html=True
#         )
#     st.title("Login")

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         # Check if username and password are correct (you would replace this with your actual authentication logic)
#         users=["user","admin","host","vishesh","yogesh","anushka","mani"]
#         passes=["12345","password","deepfake","police","cybercrime"]
#         if username in users and password in passes:
#             st.success("Login successful!")
#             return True
#         else:
#             st.error("Invalid username or password.")
#             return False

# if login():
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://media.licdn.com/dms/image/D4D12AQFbZfiSO7Hzfg/article-cover_image-shrink_720_1280/0/1697613632807?e=1718841600&v=beta&t=HcrHz0AExQDccQy8bh6BnhBI3CsPqAUnaCEMAW5Hm5s");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Pinocchio's Nose")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    predicted_class = preprocess_and_predict_image(image)

    st.markdown(f"<h1 style='font-size: 40px; font-weight: bold;'>The Image is {predicted_class}</h1>", unsafe_allow_html=True)
    if predicted_class == "FAKE":
        st.markdown("<p style='font-size:30px; font-weight: medium;'><a href='https://cybercrime.gov.in/Webform/Crime_AuthoLogin.aspx' target='_blank'>File A Complaint</a></p>", unsafe_allow_html=True)
