# app.py - With QR Code Upload Feature
import streamlit as st
import random
import datetime
from quiz_data import quiz_data
import base64
import html
import os
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="SPS ASEAN Paragliding Quiz",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        color: #0d47a1;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .question-card {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #0d47a1;
        margin-bottom: 1rem;
    }
    .ai-guidance {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #2196f3;
        margin-top: 1rem;
    }
    .score-display {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2e7d32;
        text-align: center;
        padding: 1rem;
        background-color: #e8f5e9;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #0d47a1;
        color: white;
    }
    .level-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    .beginner-badge {
        background-color: #4caf50;
        color: white;
    }
    .progressive-badge {
        background-color: #ff9800;
        color: white;
    }
    .qr-upload-section {
        background-color: #f0f7ff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px dashed #0d47a1;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'proficiency_level' not in st.session_state:
    st.session_state.proficiency_level = "beginner"
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'qr_code_uploaded' not in st.session_state:
    st.session_state.qr_code_uploaded = False
if 'qr_code_data' not in st.session_state:
    st.session_state.qr_code_data = None
if 'custom_qr_used' not in st.session_state:
    st.session_state.custom_qr_used = False

def generate_certificate(name, level, score, qr_code_data=None):
    """Generate HTML certificate with student details and QR code"""
    with open('certificate_template.html', 'r') as f:
        template = f.read()
    
    # Generate certificate ID
    cert_id = f"SPS-{random.randint(10000, 99999)}-{datetime.datetime.now().strftime('%y%m%d')}"
    
    # Fill template
    certificate = template.replace("${STUDENT_NAME}", html.escape(name))
    certificate = certificate.replace("${PROFICIENCY_LEVEL}", level.title())
    certificate = certificate.replace("${SCORE}", str(score))
    certificate = certificate.replace("${DATE}", datetime.datetime.now().strftime("%B %d, %Y"))
    certificate = certificate.replace("${CERTIFICATE_ID}", cert_id)
    
    # Add QR code if provided
    if qr_code_data and st.session_state.custom_qr_used:
        # Convert uploaded image to base64
        qr_base64 = base64.b64encode(qr_code_data).decode()
        qr_html = f'<img src="data:image/png;base64,{qr_base64}" style="width: 100px; height: 100px; object-fit: contain;">'
        certificate = certificate.replace("${QR_CODE}", qr_html)
    else:
        # Use default QR code placeholder
        qr_html = f'''
        <div style="background: #f5f5f5; border-radius: 10px; padding: 10px; text-align: center; font-size: 10px; width: 100px; height: 100px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <div style="font-weight: bold; margin-bottom: 5px;">VERIFICATION</div>
            <div>CODE</div>
            <div style="font-size: 9px; margin-top: 5px;">{cert_id}</div>
        </div>
        '''
        certificate = certificate.replace("${QR_CODE}", qr_html)
    
    return certificate

def get_ai_guidance(question_data, user_answer, correct_answer):
    """Generate AI-like guidance based on question and answer"""
    guidance = ""
    
    if user_answer == correct_answer:
        guidance += "**Excellent!** You answered correctly. "
    else:
        guidance += "**Let me help you understand this better.** "
    
    guidance += question_data['explanation']
    
    # Add additional tips based on question type
    if "speed" in question_data['question'].lower():
        guidance += "\n\n**Tip:** Always remember that airspeed is more important than groundspeed for flight control."
    elif "safety" in question_data['question'].lower() or "emergency" in question_data['question'].lower():
        guidance += "\n\n**Safety Reminder:** Practice emergency procedures regularly in safe conditions."
    elif "weather" in question_data['question'].lower():
        guidance += "\n\n**Weather Wisdom:** Always check multiple weather sources before flying."
    
    return guidance

def display_question(question_data, question_num, total_questions):
    """Display a single question with options"""
    st.markdown(f"### Question {question_num + 1} of {total_questions}")
    st.markdown(f'<div class="question-card"><h4>{question_data["question"]}</h4></div>', unsafe_allow_html=True)
    
    # Display options
    options = question_data['options']
    answer_key = f"q{question_data['id']}"
    
    if answer_key not in st.session_state.answers:
        st.session_state.answers[answer_key] = None
    
    # Create radio buttons for options
    selected_option = st.radio(
        "Select your answer:",
        options,
        key=answer_key,
        index=st.session_state.answers[answer_key] if st.session_state.answers[answer_key] is not None else 0
    )
    
    # Store answer
    st.session_state.answers[answer_key] = options.index(selected_option) if selected_option in options else 0
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if question_num > 0:
            if st.button("Previous"):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.button("Get AI Guidance"):
            st.markdown(f'<div class="ai-guidance">{get_ai_guidance(question_data, st.session_state.answers[answer_key], question_data["correct"])}</div>', unsafe_allow_html=True)
    
    with col3:
        if question_num < total_questions - 1:
            if st.button("Next"):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("Submit Quiz"):
                calculate_score()
                st.session_state.quiz_completed = True
                st.rerun()

def calculate_score():
    """Calculate the final score"""
    questions = quiz_data[st.session_state.proficiency_level]["questions"]
    total_questions = len(questions)
    correct_answers = 0
    
    for i, question in enumerate(questions):
        answer_key = f"q{question['id']}"
        if answer_key in st.session_state.answers:
            if st.session_state.answers[answer_key] == question['correct']:
                correct_answers += 1
    
    st.session_state.score = int((correct_answers / total_questions) * 100)

def main():
    # Header
    st.markdown('<div class="main-header"><h1>SPS ASEAN Paragliding Training Program</h1><h3>Interactive Knowledge Assessment Quiz</h3></div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### Quiz Navigation")
        
        if not st.session_state.quiz_started:
            st.info("Please enter your details and start the quiz.")
        else:
            level = st.session_state.proficiency_level
            badge_class = "beginner-badge" if level == "beginner" else "progressive-badge"
            st.markdown(f'Level: <span class="level-badge {badge_class}">{level.title()}</span>', unsafe_allow_html=True)
            
            # Progress bar
            total_q = len(quiz_data[level]["questions"])
            progress = (st.session_state.current_question + 1) / total_q
            st.progress(progress)
            st.caption(f"Question {st.session_state.current_question + 1} of {total_q}")
            
            # Question navigation
            st.markdown("### Jump to Question")
            for i in range(total_q):
                if st.button(f"Question {i+1}", key=f"nav_{i}", use_container_width=True):
                    st.session_state.current_question = i
                    st.rerun()
        
        st.markdown("---")
        st.markdown("### About")
        st.info("""
        This quiz is part of the SPS ASEAN Training Program.
        
        **Features:**
        - AI-powered guidance
        - Instant feedback
        - Printable certificate
        - Progress tracking
        - Custom QR code support
        """)
    
    # Main content area
    if not st.session_state.quiz_started:
        # Registration form
        st.markdown("### Welcome to the Paragliding Proficiency Quiz")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state.student_name = st.text_input("Full Name:", placeholder="Enter your full name")
        
        with col2:
            st.session_state.proficiency_level = st.selectbox(
                "Select Proficiency Level:",
                ["beginner", "progressive"],
                format_func=lambda x: "Beginner Pilot" if x == "beginner" else "Progressive Pilot"
            )
        
        st.markdown("---")
        
        # Level description
        level_desc = {
            "beginner": "**Beginner Level:** Covers fundamental knowledge including basic flight principles, safety procedures, and introductory maneuvers.",
            "progressive": "**Progressive Level:** Advanced topics including weather analysis, emergency procedures, and complex flight dynamics."
        }
        
        st.markdown(level_desc[st.session_state.proficiency_level])
        
        if st.button("Start Quiz", type="primary", use_container_width=True):
            if st.session_state.student_name.strip():
                st.session_state.quiz_started = True
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.score = 0
                st.session_state.quiz_completed = False
                st.rerun()
            else:
                st.error("Please enter your name to start the quiz.")
    
    elif st.session_state.quiz_completed:
        # Results page
        st.markdown("## Quiz Completed!")
        st.markdown(f'<div class="score-display">Your Score: {st.session_state.score}%</div>', unsafe_allow_html=True)
        
        # Detailed results
        st.markdown("### Detailed Results")
        questions = quiz_data[st.session_state.proficiency_level]["questions"]
        
        for i, question in enumerate(questions):
            answer_key = f"q{question['id']}"
            user_answer = st.session_state.answers.get(answer_key)
            is_correct = user_answer == question['correct']
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Q{i+1}:** {question['question']}")
            with col2:
                if is_correct:
                    st.success("Correct")
                else:
                    st.error("Incorrect")
            
            with st.expander("View explanation"):
                st.markdown(get_ai_guidance(question, user_answer, question['correct']))
        
        # Certificate section with QR code upload
        st.markdown("---")
        st.markdown("### Certificate of Completion")
        
        # QR Code Upload Section
        st.markdown('<div class="qr-upload-section">', unsafe_allow_html=True)
        st.markdown("#### Custom QR Code (Optional)")
        st.markdown("Upload a custom QR code image to display on your certificate. Recommended size: 100x100 pixels.")
        
        uploaded_file = st.file_uploader(
            "Choose a QR code image",
            type=['png', 'jpg', 'jpeg'],
            key="qr_uploader"
        )
        
        if uploaded_file is not None:
            # Read the uploaded file
            qr_code_data = uploaded_file.read()
            st.session_state.qr_code_data = qr_code_data
            st.session_state.qr_code_uploaded = True
            
            # Display preview
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(uploaded_file, caption="QR Code Preview", width=150)
            with col2:
                st.success("QR code uploaded successfully!")
                if st.button("Use This QR Code", key="use_qr"):
                    st.session_state.custom_qr_used = True
                    st.success("Custom QR code will be used on your certificate.")
        
        if st.session_state.qr_code_uploaded:
            if st.button("Remove QR Code", key="remove_qr"):
                st.session_state.qr_code_uploaded = False
                st.session_state.qr_code_data = None
                st.session_state.custom_qr_used = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Certificate generation
        if st.button("Generate Certificate"):
            certificate_html = generate_certificate(
                st.session_state.student_name,
                st.session_state.proficiency_level,
                st.session_state.score,
                st.session_state.qr_code_data if st.session_state.custom_qr_used else None
            )
            
            # Create download link for certificate
            b64 = base64.b64encode(certificate_html.encode()).decode()
            href = f'<a href="data:text/html;base64,{b64}" download="SPS_Certificate_{st.session_state.student_name.replace(" ", "_")}.html">Download Certificate</a>'
            st.markdown(href, unsafe_allow_html=True)
            
            # Display certificate preview
            with st.expander("Certificate Preview"):
                st.components.v1.html(certificate_html, height=600, scrolling=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Take Another Quiz"):
                st.session_state.quiz_started = False
                st.session_state.quiz_completed = False
                st.session_state.qr_code_uploaded = False
                st.session_state.qr_code_data = None
                st.session_state.custom_qr_used = False
                st.rerun()
        with col2:
            if st.button("View Statistics"):
                st.info("Statistics feature coming soon!")
    
    else:
        # Quiz in progress
        level = st.session_state.proficiency_level
        questions = quiz_data[level]["questions"]
        current_q = st.session_state.current_question
        
        # Display current question
        if current_q < len(questions):
            display_question(questions[current_q], current_q, len(questions))
        else:
            st.error("Quiz error: Question not found")
            if st.button("Return to Start"):
                st.session_state.quiz_started = False
                st.rerun()

if __name__ == "__main__":
    main()
