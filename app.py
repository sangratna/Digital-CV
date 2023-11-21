from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Sangratna Gaikwad(Data Analyst).pdf"
profile_pic = current_dir / "assets" / "3.png"

PAGE_TITLE = "Digital CV | Sangratna Gaikwad | Data Analyst"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# st.title('Hello there!')

NAME = "Sangratna Baburao Gaikwad"
DESCRIPTION = """ M.Tech student at IIT Kharagpur | Aspiring Data Analyst"""
# EMAIL = "gsangratna21@gmail.com"
SOCIAL_MEDIA = {
    "Email": "mailto:gsangratna21@gmail.com",
    "Linkedln": "https://linkedin.com/in/sangratna-gaikwad-395376134",
    "GitHub": "https://github.com/sangratna",
}

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=190)

with col2:
    st.markdown("<h2 style='margin:0; font-size:1.5em;'>Sangratna Baburao Gaikwad</h2>", unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octaet-stream",
    )

    ICON_MAPPING = {
        "Email": "✉️",
        "Linkedln": "🌐",
        "GitHub": "🐙",
    }

    social_media_line = " ".join(f"{ICON_MAPPING[platform]} [{platform}]({link})" for platform, link in SOCIAL_MEDIA.items())
    st.markdown(social_media_line)


import pandas as pd
# import streamlit as st

# Assuming you have the data in the following format
st.markdown('**Education**')
education_data = {
    "Passing Year": [2024, 2018, 2013, 2011],
    "Degree/Exam": ["M. TECH", "B.E.", "HSC", "SSC"],
    "Institute": ["IIT Kharagpur", "Savitribai Phule Pune University", "Maharashtra state board", "Maharashtra state board"],
    "CGPA/Marks": ["7.18 / 10", "56.66%", "68.83%", "79.45%"],
}

# Convert the dictionary to a DataFrame
df_education = pd.DataFrame(education_data)

# Apply left alignment to the "Passing Year" column using custom CSS
styled_df = df_education.style.set_table_styles([
    {"selector": "th.col0", "props": [("text-align", "left")]}
])

# Display the styled DataFrame as a Streamlit table
st.table(styled_df,)



st.markdown('**Projects**')

st.markdown("""
    1) **M.Tech Project**: Machine Learning Guided Strategies to Develop High Efficiency Indoor Perovskite Solar Cells & Performance Predictions of Flexible Perovskite Solar Cells:
        - Supervisor: Dr. Trilok Singh, *School of Energy Science & Engineering, Indian Institute of Technology, Kharagpur*
        - Collected data from various scientific journals 
        - Performed Machine Learning regression algorithms like Decision tree, Xgboost, Random Forest, KNN, LGBM
        - Best Performing model: all models performed well, but DTR & XGB were the best, achieving an R2 score above 0.95 in both cases
    
    
    2) **Spam Detection**: 
        - Developed a Machine Learning-based spam detection system using the Kaggle dataset 'Spam.csv' 
        - Created a user-friendly web application for seamless spam identification
        - Model Used: Natural Language Processing
        - GitHub Link: [Spam Detection Repository](https://github.com/sangratna/SBG_Spam_detection.git)
    
    
    3) **M. Tech Project Web Application**: 
        - Engineered a web application utilizing Flask to predict the efficiency of indoor solar cells
        - Leveraged insights gathered from the M. Tech project on high-efficiency perovskite solar cells
        - Model Used: Decision Tree Regressor
        - GitHub Link: [Web Application Repository](https://github.com/sangratna/Indoor_solar_cell_efficiency-prediction.git)
    
    
    4) **Sales Analysis using MySQL and Tableau**: 
        - Project involves analyzing sales data using MySQL for data management and Tableau for visualization
        - Dataset contains information about orders, including order number, quantity, price, product details, customer information, and more
        - GitHub Link: [Sales Analysis Repository](https://github.com/sangratna/SALES-PROJECT.git)
    
    
    5) **IPL SQL Data Analysis**: 
        - Project involves analyzing team performance over multiple seasons
        - Studying match outcomes based on toss decisions and identifying player of the match trends
        - SQL queries regarding the analysis of IPL match data from 2008 to 2023
        - GitHub Link: [IPL Data Analysis Repository](https://github.com/sangratna/IPL_SQL_Data_Analysis.git)
""")


import streamlit as st

# Assuming you have a section for Internship in your application
st.markdown('**Internship**')
st.markdown("""
    **Title**: "Occupancy and Occupants' Behavior Detection using Indoor CO2 and Temperature Data",
    - Supervisor:  Dr. Prashant Anand, *Department of Architecture and Regional Planning, Indian Institute of Technology, Kharagpur*",
    - Description: This involved gathering data from sensors in various rooms and analyzing clusters for enhanced energy efficiency.",
    - Model Used:  K-Means,
""")


st.markdown('**Achivement: Cracked Prestigious GATE Exam with rank of 1505 in XE paper**')


st.markdown('**Publication**')
st.markdown("""
   - Machine Learning Guided Strategies to Develop High Efficiency Indoor Perovskite Solar Cells **(Manuscript under preparation)** 
   - Performance Predictions of Flexible Perovskite Solar Cells using Machine Learning Strategies **(Ongoing Work)**
            """)

st.markdown('**Skills**')
st.markdown('''
**Programming Skills:** Python | 
**ML Libraries:** Numpy, Pandas, Matplotlib, Seaborn, TensorFlow, Keras |
**DL Libraries:** TensorFlow, Keras |
**IDE:** Jupyter Notebook, VS Code |
**Microsoft Office Tools:** PowerPoint, Excel, Word |
**Analytical Tool:** MS Excel (calculation, visualization, pivot table) |
**Visualization Tool:** Power BI, Tableau |
**Relation Database:** MySQL, Query |
**Version Control System:** Git |
**Soft Skills:** Leadership, Managerial, Communication, Problem Solving & Time Management |
**Hard Skills:** Report Writing, Presentation 
''')

st.markdown('**Certifications**')
st.markdown('''
**Power BI**: Udemy | Sept-2023 || **MySQL**: Great Learning | Aug-2023 || **MS Excel**: Tutorial Point |Dec-2022|| **Data analysis** : Udemy | Jan-2023 || **Machine Learning Certificate**: Udemy| Sept- 2023
''')

st.markdown('**Extra-Carricular**')
st.markdown('''
**Volunteer**: 68th Convocation 2022, IIT Kharagpur: Assisted in organizing and coordinating the convocation event, 
ensuring a seamless experience for attendees. 

**Participant**: MindSpark Technical Event, College of Engineering Pune: Engaged in problem-solving challenges and quiz 
competition Participant: INNOVISION Technical Event, JSPM’s Rajshree Shahu College of Engineering: Actively 
participated, showcasing technical skills regarding lathe competition contributing to a vibrant learning atmosphere.
''')  
