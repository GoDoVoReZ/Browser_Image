# Libraries
import streamlit as st
import numpy as np  
from PIL import Image, ImageDraw, ImageFilter

# Header
st.title('----- Change your image ------') # Title of project
uploaded_file = st.file_uploader('Choose an image', ['jpg', 'jpeg', 'png']) # drag and drop window 
st.markdown('## **OR**')
use_default_image = st.checkbox('Show example') # 'Show example' button
default_image = 'lion.jpg'

# Image change functions
def gray_scale_image(path_to_image):
    image = Image.open(path_to_image)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            mid = (r + g + b) // 3
            draw.point((x, y), (mid, mid, mid))

    st.image(image)

def inverse_image(path_to_image):
    image = Image.open(path_to_image)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (255 - r, 255 - g, 255 - b))

    st.image(image)

def filter_image(path_to_image, n):
    image = Image.open(path_to_image)
    if n == 0:
        image = image.filter(ImageFilter.BLUR)
    elif n == 1:
        image = image.filter(ImageFilter.CONTOUR)
    elif n == 2:
        image = image.filter(ImageFilter.DETAIL)
    elif n == 3:
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif n == 4:
        image = image.filter(ImageFilter.EMBOSS)
    elif n == 5:
        image = image.filter(ImageFilter.FIND_EDGES)
    elif n == 6:
        image = image.filter(ImageFilter.SMOOTH)
    elif n == 7:
        image = image.filter(ImageFilter.SHARPEN)

    st.image(image, width=400)

if use_default_image:
    st.image(default_image, width=400)
    st.sidebar.markdown('## **How your need to change image?**')
    blur    = st.sidebar.button('Blur')
    contour = st.sidebar.button('CONTOUR')
    detail  = st.sidebar.button('DETAIL')
    edge    = st.sidebar.button('EDGE_ENHANCE')
    emboss  = st.sidebar.button('EMBOSS')
    find_edges = st.sidebar.button('FIND_EDGES')
    smooth  = st.sidebar.button('SMOOTH')
    sharpen = st.sidebar.button('SHARPEN')

    if blur:
        filter_image(default_image, 0)
    elif contour:
        filter_image(default_image, 1)
    elif detail:
        filter_image(default_image, 2)
    elif edge:
        filter_image(default_image, 3)
    elif emboss:
        filter_image(default_image, 4)
    elif find_edges:
        filter_image(default_image, 5)
    elif smooth:
        filter_image(default_image, 6)
    elif sharpen:
        filter_image(default_image, 7)



    