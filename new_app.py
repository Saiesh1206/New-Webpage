import streamlit as st
from streamlit_lottie import st_lottie
import json

# Function to load Lottie animation from a local file
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Lottie animation (assuming Animation.json is in the same directory as app.py)
lottie_animation = load_lottie_file("Animation.json")

# Set page configuration
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Header section
st.subheader("Hi, I am Saiesh :wave:")
st.title("I am an Electronics Engineer from KJ SOMAIYA COLLEGE OF ENGINEERING ")
st.write("Welcome to my webpage!")

# Lottie animation
st_lottie(lottie_animation, height=300, key="animation")

# Add a brief introduction
st.write("""
Highly motivated and detail-oriented Electronics student with a solid foundation in circuit design, PCB making and Hardware development. 
Have basic knowledge in utilizing various electronic tools and software such as LT SPICE and Arduino for practical applications.
Demonstrates a strong analytical mindset with a keen interest in innovative technologies and problem-solving. Possesses excellent 
teamwork and communication skills honed through collaborative projects and internships. Eager to contribute to cutting-edge projects and 
gain further experience in the field of electronics engineering. Feel free to explore my work and get in touch!
""")

# Add a link
st.write("[Learn More >](https://pythonandvba.com)")

# Additional content (optional)
st.header("Projects")
st.write("""
- Project 1: Smart Irrigation System
- Project 2: Smart Switch Board for home automation
- Project 3: Smart wearable vest for Industrial Workers
""")

st.header("Work Experience")
st.write("""
- Intern at Simtek Medico Systems, [Mumbai]:
  Assisted in the design and testing of electronic circuits for consumer electronics.
  Performed SMD components soldering, machine wiring and product finishing.
  Conducted quality checks and developed technical reports and presented findings to senior engineers.
""")

st.header("Skills")
st.write("""
- Soldering & PCB Design
- Circuit Design & Analysis
- Arduino & NodeMCU Development
- Hardware skills
- Basic Coding skills
- Team Collaboration & Project Management
- Problem-solving skills
- PLC coding
""")

st.header("Contact")
st.write("You can reach me via [email](mailto:saieshchikne@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com).")
