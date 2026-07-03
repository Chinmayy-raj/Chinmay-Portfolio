import streamlit as st
import json
from PIL import Image
import os

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Chinmay Raj | Portfolio",
    page_icon="👨‍🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ==========================================
# Navigation Bar
# ==========================================

menu_title=None,
options=[
        "Home",
        "About",
        "Skills",
        "Projects",
        "Education",
        "Certificates",
        "Achievements",
        "Contact"
    ],

icons=[
        "house",
        "person",
        "laptop",
        "folder",
        "mortarboard",
        "award",
        "trophy",
        "telephone"
    ],

default_index=0,

orientation="horizontal"
# -------------------------------
# LOAD CSS
# -------------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------------
# LOAD JSON
# -------------------------------
def load_json(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

profile = load_json("data/profile.json")
skills = load_json("data/skills.json")
projects = load_json("data/projects.json")

# -------------------------------
# HERO SECTION
# -------------------------------

col1, col2 = st.columns([1,2])

with col1:

    profile_img = Image.open("assets/profile.jpg")

    st.image(profile_img, width=260)

with col2:

    st.markdown(f"<h1>{profile['name']}</h1>", unsafe_allow_html=True)

    st.markdown(
        f"<h3 style='color:#1E88E5'>{profile['title']}</h3>",
        unsafe_allow_html=True
    )

    st.write(profile["summary"])

    st.download_button(
        " Download Resume",
        open("assets/resume.pdf", "rb"),
        file_name="Chinmay_Raj_Resume.pdf",
        use_container_width=True
    )

    c1,c2,c3 = st.columns(3)

    with c1:
        st.link_button("GitHub", profile["github"])

    with c2:
        st.link_button("LinkedIn", profile["linkedin"])

    with c3:
        st.link_button("Email", f"mailto:{profile['email']}")

st.divider()

# -------------------------------
# ABOUT
# -------------------------------


st.header(" About Me")

st.markdown(
        f"""
        <div class="about-text">
        {profile["about"]}
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# SKILLS
# -------------------------------


st.header(" Technical Skills")
st.markdown("Here are the technologies and tools I work with.")

skills_per_row = 4

for i in range(0, len(skills), skills_per_row):

    cols = st.columns(skills_per_row)

    for j, col in enumerate(cols):

        if i + j < len(skills):

            skill = skills[i + j]["name"]

            with col:

                st.markdown(
                    f"""
                    <div class="skill-box">
                        {skill}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.divider()

# -------------------------------
# PROJECTS
# -------------------------------


st.header(" Projects")

for project in projects:

    col1, col2 = st.columns([1,2])

    with col1:

        image_path = f"assets/{project['image']}"

        if os.path.exists(image_path):
            st.image(image_path)

    with col2:

        st.subheader(project["title"])

        st.write(project["description"])

        st.markdown(
            "**Tech Stack:** "
            + ", ".join(project["tech"])
        )

        c1,c2 = st.columns(2)

        with c1:
            st.link_button(
                "GitHub",
                project["github"]
            )

        with c2:
            if project["demo"] != "":
                st.link_button(
                    "Live Demo",
                    project["demo"]
                )

    st.divider()

st.header(" Education")  

education = [
    {
        "degree": "Bachelor of Engineering",
        "branch": "Information Science and Engineering",
        "college": "Malnad College of Engineering, Hassan",
        "cgpa": "8.65 CGPA",
        "year": "2022 - 2026",
        "coursework": [
            "Operating Systems",
            "Data Structures",
            "Artificial Intelligence",
            "Machine Learning",
            "Cloud Computing",
            "DBMS",
            "Computer Architecture",
            "OOP"
        ]
    },

    {
        "degree":"Pre-University",
        "branch":"PCMB",
        "college":"Vivekananda PU College, Puttur",
        "cgpa":"91.3%",
        "year":"2020-2022",
        "coursework":[]
    },

    {
        "degree":"High School",
        "branch":"SSLC",
        "college":"Pushpa English Medium School",
        "cgpa":"89.44%",
        "year":"2020",
        "coursework":[]
    }
]

for edu in education:

    st.markdown(f"""
<div class="education-card">

<h2>{edu['degree']}</h2>

<h4>{edu['branch']}</h4>

<p> <b>{edu['college']}</b></p>

<p> {edu['year']}</p>

<p> {edu['cgpa']}</p>

</div>

""", unsafe_allow_html=True)

    if len(edu["coursework"]) > 0:

        st.write("### Relevant Coursework")

        cols = st.columns(4)

        for i, subject in enumerate(edu["coursework"]):

            with cols[i%4]:

                st.markdown(f"""
<div class="course-card">

{subject}

</div>
""", unsafe_allow_html=True)
# =====================================================
# CERTIFICATIONS
# ===================================================== 
    st.divider()

st.header(" Certifications")

certifications = [

    "Data Science Internship 2026 - Prinston Smart Engineers",

    "Trainee AIML Engineer - Inventron Technologies",

    "RBI 90 Quiz - Reserve Bank of India",

    "Human Computer Interaction (HCI) (87%) - NPTEL",

    "Softskill Development - NPTEL",

    "Public Speaking - NPTEL",

    "StartUp Karnataka - Bootcamp",

    "AI for Students - NXTWAVE",

    "State level Hackathon 4th place- Kalpatharu Institute of Technology",

    "Hackathon - Atria Institute of Technology",

]

cols = st.columns(2)

for index, certificate in enumerate(certifications):

    with cols[index % 2]:

        st.markdown(f"""
        <div class="certificate-card">
             {certificate}
        </div>
        """, unsafe_allow_html=True)



# =====================================================
# ACHIEVEMENTS
# =====================================================

st.divider()

st.header(" Achievements")

achievements = [

    " Secured 4th Place in State-Level Hackathon organized by Kalpatharu Institute of Technology.",

    " Secured top positions in multiple college and external coding competitions.",

    " Technical Events Coordinator - Organized coding workshops for 60+ students.",

    " Received recognition for scoring 100/100 in 12th Grade Mathematics.",

    " Awarded Best Science Model by Mysore District Science Association."

]

for achievement in achievements:

    st.markdown(
        f"""
        <div class="achievement-card">
            {achievement}
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# CONTACT
# =====================================================

st.divider()

st.header(" Contact Me")

st.markdown(
    """
    <div class="contact-text">
        Feel free to reach out for internships, collaborations, or software development opportunities.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
 **Email:** {profile['email']}

 **Phone:** {profile['phone']}

 **Location:** {profile['location']}
"""
)

st.link_button(
    " Connect on LinkedIn",
    profile["linkedin"]
)

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    """
<div class="footer">

© 2026 Chinmay Raj, Developer.

</div>
""",
    unsafe_allow_html=True
)