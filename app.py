import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="My Personal Page",
    page_icon="👋",
    layout="centered"
)

# Add custom CSS
st.markdown("""
<style>
.main-container {
    padding: 2rem;
}
.profile-container {
    text-align: center;
    padding: 2rem;
    border-radius: 10px;
    background-color: #f8f9fa;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
}
.message-container {
    padding: 2rem;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
h1 {
    color: #2c3e50;
    margin-bottom: 1rem;
}
.profile-image {
    border-radius: 50%;
    max-width: 250px;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="profile-container">', unsafe_allow_html=True)

# Title
st.title("Welcome to My Page")

# Use the specific image path provided
image_path = "/Users/mugilarasan/Pictures/Backup Photos/iCloud Photos/9238e2bf-742d-4c9e-abd7-7b7fc0febb5f.jpg"
if os.path.exists(image_path):
    image = Image.open(image_path)
    st.image(image, width=250, output_format="JPEG", caption="", use_column_width=False)
else:
    st.error(f"Image not found at: {image_path}")
    st.markdown("### Image Not Found")

st.markdown('</div>', unsafe_allow_html=True)

# Personal message
st.markdown('<div class="message-container">', unsafe_allow_html=True)
st.markdown("## My Message")
st.markdown("""
Hello! This is my personal Streamlit page. I'm passionate about technology and innovation.
            
I created this page to share a bit about myself and my interests. Feel free to connect with me
to discuss ideas or collaborate on projects.

### About Me
- 🌱 I'm currently working on exciting projects
- 💡 I love learning new technologies
- 🎯 I'm focused on making a positive impact

Thank you for visiting my page!
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2025 | Created with Streamlit")
