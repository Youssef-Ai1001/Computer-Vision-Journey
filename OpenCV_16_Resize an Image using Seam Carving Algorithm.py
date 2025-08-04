"""
This version only supports reducing width, not height (but it can be extended).
Very Slow Algorithm
"""

import cv2
import numpy as np
import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Seam Carving Image Resizing")
st.title('Seam Carving Image Resizing')


# Step 1: Calculate the energy map of the image
def calc_energy(img):
    """
    creates a gradient-based energy map showing important edges
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)    # Horizontal gradient
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)    # Vertical gradient
    energy = np.absolute(sobelx) + np.absolute(sobely)  # Total energy
    return energy


# Step 2: Remove one vertical seam from the image
def remove_vertical_seam(img):
    """
    finds the lowest-energy vertical seam and removes it
    """
    h, w = img.shape[:2]
    energy = calc_energy(img)

    # Initialize M (cumulative energy map) and backtrack matrix
    M = energy.copy()
    backtrack = np.zeros_like(M, dtype=np.int32)

    # Populate M and backtrack by dynamic programming
    for i in range(1, h):
        for j in range(0, w):
            # Handle the left edge
            if j == 0:
                idx = np.argmin(M[i - 1, j:j + 2])
                backtrack[i, j] = idx + j
                min_energy = M[i - 1, idx + j]
            else:
                # Handle middle and right edge
                idx = np.argmin(M[i - 1, j - 1:j + 2])
                backtrack[i, j] = idx + j - 1
                min_energy = M[i - 1, idx + j - 1]
            M[i, j] += min_energy

    # Step 3: Backtrack to find the minimum energy seam
    seam = []
    j = np.argmin(M[-1])  # Start from the bottom row
    for i in reversed(range(h)):
        seam.append(j)
        j = backtrack[i, j]

    # Step 4: Create a mask to remove the seam
    mask = np.ones((h, w), dtype=np.bool_)
    for i in range(h):
        mask[i, seam[i]] = False

    # Remove the seam from the image
    img = img[mask].reshape((h, w - 1, 3))
    return img


# Step 5: Reduce image width gradually by removing vertical seams
def seam_carve(img, new_width, new_height):
    """
    keeps removing seams until the image reaches the target width
    """
    print("Starting seam carving...")

    output = img.copy()
    while output.shape[1] > new_width:
        output = remove_vertical_seam(output)
    # Note: Height resizing not implemented in this version

    print("Finished seam carving.")

    return output


# Step 6: Streamlit file uploader
uploaded_file = st.file_uploader('Choose an image...', type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file into an image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)  # Decode the image as BGR (OpenCV format)
    st.image(img, channels="BGR", caption="Original Image")

    # Step 7: User chooses new width using slider
    new_width = st.slider("New Width", min_value=1, max_value=img.shape[1], value=img.shape[1] - 50)

    # Step 8: Apply seam carving
    resized_img = seam_carve(img, new_width, img.shape[0])

    # Step 9: Show the resized image
    st.image(resized_img, channels="BGR", caption="Resized Image with Seam Carving")