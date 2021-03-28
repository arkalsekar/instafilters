import numpy as np
import streamlit as st
import copy
import imutils
from PIL import Image
from scipy.interpolate import UnivariateSpline
from filters import grayImage, gaussianBlur, warmImage, coldImage, spreadLookupTable, Edge, load_image, resize, Sketch, divimg

# Title Of the Page
st.title("InstaFilters Using Image Processing ")
st.write()

# Subheading of the page
st.subheader("This App Can Apply Blur, Warm, Cold, Graysclae, Edged filters to your Images.")

# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'jpeg', 'png'])

# Checking the Format of the page
if uploadFile is not None:
    st.write("Image Uploaded Successfully")
else:
    st.write("Make sure you image is in JPG/PNG Format.")

# Creating a DropDown to Select the FIlter
SltFilter = st.selectbox(label="Select the Filter Type", options=['Normal', 'Blur', 'Cold', 'Warm', 'Edge', 'GrayScale', 'Sketch', 'Crop'])

st.markdown('#####')

# Checking Whether image is Uploaded Successfully or Not
if uploadFile is None:
    st.write("Please Upload the Image Before Applying any Filter.")

else:
    # Checking and Applying the Filters 
    if SltFilter == "Blur":
        initialImage = load_image(uploadFile)
        blurredImage = gaussianBlur(copy.deepcopy(initialImage))
        st.image(blurredImage, caption="Blur Image", width=700, height=800)

    elif SltFilter ==  "Normal":
        img = load_image(uploadFile)
        st.image(img, caption="Normal Image", width=700, height=800)

    elif SltFilter == "Warm":
        ima = load_image(uploadFile)
        warmimg = warmImage(ima)
        st.image(warmimg, caption="Warm Image", width=700, height=800)
        
    elif SltFilter == "Cold":
        img = load_image(uploadFile)
        colding = coldImage(img)
        st.image(colding, caption="Cold Image", width=700, height=800)
        
    elif SltFilter == "Edge":
        img = load_image(uploadFile)
        edge = Edge(img)
        st.image(edge, caption="Edged Image", width=700, height=800)

    elif SltFilter == "GrayScale":
        ima = load_image(uploadFile)
        grayed = grayImage(ima)
        st.image(grayed, caption="GrayScale Image", width=700, height=800)

    elif SltFilter == "Crop":
        le = st.number_input(label="Left (Pixels)", min_value=1.00, max_value=2.00)
        to = st.number_input(label="Top (Pixels)", min_value=1.00, max_value=2.00)
        ri = st.number_input(label="Right (Pixels)", min_value=2.01, max_value=500.00)
        bo = st.number_input(label="bottom (Pixels)", min_value=2.01, max_value=500.00)
        im = Image.open(uploadFile)
        width, height = im.size
        Cropping = resize(im, int(le), int(to), int(ri), int(bo))
        # st.write(Cropping)
        st.image(Cropping, caption="Resized Image")
        
    elif SltFilter == "Sketch":
        im = load_image(uploadFile)
        imag = Sketch(im)
        st.image(imag, caption="Sketched Image", width=700, height=800)        
