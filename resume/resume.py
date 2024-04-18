from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.docx"
profile_pic = current_dir / "assets" / "profile.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Yonatan Refael"
PAGE_ICON = "🙋🏻‍♂️"
NAME = "Yonatan Refael"
DESCRIPTION = """
Software Developer, 3rd year student at Holon Institute of Technology.
"""
EMAIL = "Yonatanref007@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/yonatan-refael-a0a132303",
    "GitHub": "https://github.com/yonatanref007",
}
PROJECTS = [
    "✔️ Cost Dashboard - Using indexedDB to Follow your spending and get reports",
    "✔️ Calorie Count - Serverside project using mongoDB to Follow your daily consumption",
    "✔️ Writing web - Clientside project that lets the user write with Fonts and download it to a docx",
    "✔️ price tracker - Using Selenium to get the history of Sales of websites"
]


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as Docx_file:
    Docxbyte = Docx_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=Docxbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE ---
st.write('\n')
st.subheader("EXPERIENCE")
st.write("---")

# --- Army
st.write("📑", "Monitering Department")
st.write(
    """
- ► Used python to automate and organized reports that were done manually.
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")
    

# --- SKILLS & Intrests---
st.write('\n')
st.subheader("SKILLS & Intrests")
st.write("---")
st.write('●	Skills:')
st.write(
    """
- 👩‍💻 Web Development (JS, HTML, Django, Streamlib)
- 📚 Familiar with C++, C#, Python and technologies such as SQL, Selenium
- 🗣️ Fluent in Hebrew and English
"""
)
st.write('●	Intrests:')
st.write(
    """
- 💪 Working on my own coding projects while learning new technologies and interactions between computer languages.
- 😎 Music and Tennis.
"""
)
