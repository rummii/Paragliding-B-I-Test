# app.py - Enhanced UI Version
import streamlit as st
import random
import datetime
from quiz_data import quiz_data
import base64
from io import BytesIO
import html

# Page configuration
st.set_page_config(
    page_title="SPS ASEAN Paragliding Quiz",
    page_icon="🪂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with enhanced UI
st.markdown("""
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .main-container {
        background-color: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        min-height: 90vh;
    }
    
    /* Header Styles */
    .main-header {
        background: linear-gradient(90deg, #0d47a1 0%, #1976d2 100%);
        color: white;
        text-align: center;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
        background-size: 30px 30px;
        animation: float 20s linear infinite;
    }
    
    @keyframes float {
        0% { transform: translate(0, 0) rotate(0deg); }
        100% { transform: translate(0, 0) rotate(360deg); }
    }
    
    .header-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        position: relative;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        position: relative;
    }
    
    /* Question Card */
    .question-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 1.5rem;
        border: 2px solid #e3f2fd;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .question-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.12);
    }
    
    .question-number {
        background: linear-gradient(45deg, #0d47a1, #2196f3);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        display: inline-block;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .question-text {
        font-size: 1.3rem;
        color: #333;
        line-height: 1.6;
        font-weight: 500;
    }
    
    /* Options Styling */
    .stRadio > div {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stRadio > div:hover {
        background: #e3f2fd;
        border-color: #2196f3;
        transform: translateX(5px);
    }
    
    /* AI Guidance */
    .ai-guidance {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #2196f3;
        margin-top: 1.5rem;
        animation: slideIn 0.5s ease;
    }
    
    @keyframes slideIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Score Display */
    .score-display {
        background: linear-gradient(45deg, #4CAF50, #8BC34A);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 5px 15px rgba(76, 175, 80, 0.3);
    }
    
    .score-value {
        font-size: 3rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    
    /* Badges */
    .level-badge {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .beginner-badge {
        background: linear-gradient(45deg, #4CAF50, #2E7D32);
        color: white;
    }
    
    .progressive-badge {
        background: linear-gradient(45deg, #FF9800, #F57C00);
        color: white;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #0d47a1, #1976d2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(13, 71, 161, 0.2);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(13, 71, 161, 0.3);
        background: linear-gradient(45deg, #1976d2, #2196f3);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .sidebar-header {
        color: white;
        text-align: center;
        padding: 1rem;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #4CAF50, #8BC34A);
    }
    
    /* Results Cards */
    .result-correct {
        background: linear-gradient(45deg, #E8F5E9, #C8E6C9);
        border-left: 5px solid #4CAF50;
    }
    
    .result-incorrect {
        background: linear-gradient(45deg, #FFEBEE, #FFCDD2);
        border-left: 5px solid #F44336;
    }
    
    /* Certificate Button */
    .certificate-btn {
        background: linear-gradient(45deg, #FF9800, #FF5722) !important;
        font-size: 1.1rem !important;
        padding: 1rem 2rem !important;
    }
    
    /* Floating Elements */
    .paraglider-icon {
        position: absolute;
        font-size: 2rem;
        animation: floatIcon 3s ease-in-out infinite;
    }
    
    @keyframes floatIcon {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
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

def generate_certificate(name, level, score):
    """Generate HTML certificate with student details"""
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
    
    return certificate

def get_ai_guidance(question_data, user_answer, correct_answer):
    """Generate AI-like guidance based on question and answer"""
    guidance = ""
    
    # Create emoji-based feedback
    if user_answer == correct_answer:
        emoji = random.choice(["🎯", "🌟", "💪", "🔥", "🏆"])
        guidance += f"{emoji} **Excellent!** Your answer is correct. "
    else:
        emoji = random.choice(["📚", "💡", "🎓", "🔍", "🧠"])
        guidance += f"{emoji} **Let me help you understand this better.** "
    
    guidance += question_data['explanation']
    
    # Add contextual tips with emojis
    if "speed" in question_data['question'].lower():
        guidance += "\n\n⚡ **Pro Tip:** Remember that maintaining proper airspeed is critical for control and safety. Too slow risks stall, too fast reduces control."
    elif "safety" in question_data['question'].lower() or "emergency" in question_data['question'].lower():
        guidance += "\n\n🛡️ **Safety First:** Always prioritize conservative decisions. When in doubt, choose the safer option and practice emergencies regularly."
    elif "weather" in question_data['question'].lower():
        guidance += "\n\n🌤️ **Weather Wisdom:** Develop a habit of checking multiple reliable weather sources. Learn to recognize visual cues of changing conditions."
    elif "landing" in question_data['question'].lower():
        guidance += "\n\n🛬 **Landing Insight:** Good landings start with good approaches. Plan your pattern early and maintain visual references."
    
    # Add learning resource suggestion
    guidance += f"\n\n📖 **Want to learn more?** This concept is covered in depth in the SPS ASEAN Training Manual, Chapter {random.randint(1, 10)}."
    
    return guidance

def display_question(question_data, question_num, total_questions):
    """Display a single question with enhanced options"""
    st.markdown(f"""
    <div class="question-card">
        <div class="question-number">Question {question_num + 1} of {total_questions}</div>
        <div class="question-text">{question_data['question']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Display options with better styling
    options = question_data['options']
    answer_key = f"q{question_data['id']}"
    
    if answer_key not in st.session_state.answers:
        st.session_state.answers[answer_key] = None
    
    # Create custom radio options
    option_letters = ['A', 'B', 'C', 'D']
    selected_option = st.radio(
        "**Select your answer:**",
        options,
        key=answer_key,
        index=st.session_state.answers[answer_key] if st.session_state.answers[answer_key] is not None else 0,
        format_func=lambda x: f"{option_letters[options.index(x)]}. {x}" if x in options else x
    )
    
    # Store answer
    st.session_state.answers[answer_key] = options.index(selected_option) if selected_option in options else 0
    
    # Navigation buttons with icons
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if question_num > 0:
            if st.button("⬅️ Previous Question", use_container_width=True):
                st.session_state.current_question -= 1
                st.rerun()
    
    with col2:
        if st.button("🤖 Get AI Guidance", type="secondary", use_container_width=True):
            st.markdown(f'<div class="ai-guidance">{get_ai_guidance(question_data, st.session_state.answers[answer_key], question_data["correct"])}</div>', unsafe_allow_html=True)
    
    with col3:
        if question_num < total_questions - 1:
            if st.button("Next Question ➡️", type="primary", use_container_width=True):
                st.session_state.current_question += 1
                st.rerun()
        else:
            if st.button("🚀 Submit Quiz", type="primary", use_container_width=True):
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
    # Main container with white background
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Header with enhanced design
    st.markdown("""
    <div class="main-header">
        <h1 class="header-title">🪂 SPS ASEAN Paragliding Training Program</h1>
        <p class="header-subtitle">Interactive Knowledge Assessment & Certification System</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with enhanced design
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <h2>📊 Quiz Dashboard</h2>
            <p>Navigate & Monitor Progress</p>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.quiz_started:
            st.info("👋 Welcome! Please register to begin your assessment.")
        else:
            level = st.session_state.proficiency_level
            badge_class = "beginner-badge" if level == "beginner" else "progressive-badge"
            st.markdown(f"""
            <div style="text-align: center; margin: 1rem 0;">
                <div style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">Current Level</div>
                <span class="level-badge {badge_class}">{level.title()} Pilot</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress bar with stats
            total_q = len(quiz_data[level]["questions"])
            progress = (st.session_state.current_question + 1) / total_q
            
            st.markdown("### 📈 Progress")
            st.progress(progress)
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Questions", f"{st.session_state.current_question + 1}/{total_q}")
            with col2:
                if st.session_state.quiz_completed:
                    st.metric("Score", f"{st.session_state.score}%")
            
            # Question navigation
            st.markdown("### 🧭 Quick Navigation")
            cols = st.columns(2)
            for i in range(total_q):
                with cols[i % 2]:
                    status = "✅" if f"q{quiz_data[level]['questions'][i]['id']}" in st.session_state.answers else "⭕"
                    if st.button(f"{status} Q{i+1}", key=f"nav_{i}", use_container_width=True):
                        st.session_state.current_question = i
                        st.rerun()
        
        st.markdown("---")
        st.markdown("### 🏆 Achievements")
        if st.session_state.quiz_completed:
            st.success("✅ Quiz Completed!")
            if st.session_state.score >= 80:
                st.balloons()
                st.success("🎉 Excellent Performance!")
            elif st.session_state.score >= 60:
                st.info("👍 Good Effort!")
        
        st.markdown("### ℹ️ Program Info")
        with st.expander("About SPS ASEAN"):
            st.write("""
            **Safety & Proficiency Standards (SPS) ASEAN Training Program**
            
            - Internationally recognized certification
            - AI-powered learning assistance
            - Comprehensive knowledge assessment
            - Professional certificate issuance
            """)
    
    # Main content area
    if not st.session_state.quiz_started:
        # Enhanced registration form
        st.markdown("### 🎯 Begin Your Journey")
        st.markdown("Start your paragliding proficiency assessment by providing your details below.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("#### 📝 Registration Form")
            st.session_state.student_name = st.text_input(
                "**Full Name:**",
                placeholder="Enter your full name",
                help="This name will appear on your certificate"
            )
            
            st.session_state.proficiency_level = st.selectbox(
                "**Select Proficiency Level:**",
                ["beginner", "progressive"],
                format_func=lambda x: {
                    "beginner": "🟢 Beginner Pilot (Fundamentals)",
                    "progressive": "🟠 Progressive Pilot (Advanced)"
                }[x],
                help="Choose the level that matches your current skills"
            )
        
        with col2:
            st.markdown("#### 🎓 Level Preview")
            if st.session_state.proficiency_level == "beginner":
                st.info("""
                **Beginner Level:**
                - Basic flight principles
                - Safety procedures
                - Introductory maneuvers
                - 10 questions
                """)
            else:
                st.info("""
                **Progressive Level:**
                - Advanced weather analysis
                - Emergency procedures
                - Complex flight dynamics
                - 10 challenging questions
                """)
        
        st.markdown("---")
        
        # Start quiz button with animation
        if st.button("🚀 Start Assessment Now", type="primary", use_container_width=True, use_container_width=True):
            if st.session_state.student_name.strip():
                st.session_state.quiz_started = True
                st.session_state.current_question = 0
                st.session_state.answers = {}
                st.session_state.score = 0
                st.session_state.quiz_completed = False
                st.rerun()
            else:
                st.error("❌ Please enter your name to start the assessment.")
    
    elif st.session_state.quiz_completed:
        # Enhanced results page
        st.markdown("## 🏁 Assessment Complete!")
        
        # Score display with emoji based on performance
        if st.session_state.score >= 80:
            score_emoji = "🏆"
            score_color = "#4CAF50"
        elif st.session_state.score >= 60:
            score_emoji = "🎯"
            score_color = "#FF9800"
        else:
            score_emoji = "📚"
            score_color = "#F44336"
        
        st.markdown(f"""
        <div class="score-display" style="background: linear-gradient(45deg, {score_color}, {score_color}88);">
            <div style="font-size: 1.2rem; opacity: 0.9;">Your Final Score</div>
            <div class="score-value">{score_emoji} {st.session_state.score}%</div>
            <div style="font-size: 1rem; opacity: 0.9;">
                {st.session_state.student_name} • {st.session_state.proficiency_level.title()} Level
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Performance feedback
        col1, col2, col3 = st.columns(3)
        questions = quiz_data[st.session_state.proficiency_level]["questions"]
        correct_count = sum(1 for i, q in enumerate(questions) 
                          if st.session_state.answers.get(f"q{q['id']}") == q['correct'])
        
        with col1:
            st.metric("📊 Accuracy", f"{(correct_count/len(questions)*100):.0f}%")
        with col2:
            st.metric("✅ Correct", f"{correct_count}/{len(questions)}")
        with col3:
            st.metric("⏱️ Time", datetime.datetime.now().strftime("%H:%M"))
        
        # Detailed results with expandable sections
        st.markdown("### 📋 Detailed Results Analysis")
        
        for i, question in enumerate(questions):
            answer_key = f"q{question['id']}"
            user_answer = st.session_state.answers.get(answer_key)
            is_correct = user_answer == question['correct']
            
            result_class = "result-correct" if is_correct else "result-incorrect"
            result_icon = "✅" if is_correct else "❌"
            
            with st.expander(f"{result_icon} Question {i+1}: {question['question'][:50]}..."):
                st.markdown(f"""
                <div style="padding: 1rem; border-radius: 10px; {'' if is_correct else ''}">
                    <h4>Your Answer: {question['options'][user_answer] if user_answer is not None else 'Not answered'}</h4>
                    <h4 style="color: {'#4CAF50' if is_correct else '#F44336'}">
                        Correct Answer: {question['options'][question['correct']]}
                    </h4>
                    <div style="margin-top: 1rem; padding: 1rem; background: #f5f5f5; border-radius: 5px;">
                        {get_ai_guidance(question, user_answer, question['correct'])}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Certificate section
        st.markdown("---")
        st.markdown("### 🏅 Official Certification")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            #### 📜 Generate Your Certificate
            
            Your performance qualifies you for an official SPS ASEAN Training Program certificate. 
            This certificate can be:
            
            - 🖨️ Printed for your records
            - 📁 Added to your professional portfolio
            - 🏢 Submitted for training credits
            - 📱 Shared digitally
            
            *Certificate includes unique ID for verification*
            """)
        
        with col2:
            if st.button("🎖️ Generate Certificate", type="primary", use_container_width=True, key="cert_btn"):
                certificate_html = generate_certificate(
                    st.session_state.student_name,
                    st.session_state.proficiency_level,
                    st.session_state.score
                )
                
                # Create download link
                b64 = base64.b64encode(certificate_html.encode()).decode()
                href = f'''
                <a href="data:text/html;base64,{b64}" 
                   download="SPS_Certificate_{st.session_state.student_name.replace(" ", "_")}.html"
                   style="text-decoration: none;">
                    <button style="
                        background: linear-gradient(45deg, #FF9800, #FF5722);
                        color: white;
                        border: none;
                        padding: 1rem 2rem;
                        border-radius: 10px;
                        font-weight: bold;
                        font-size: 1.1rem;
                        cursor: pointer;
                        width: 100%;
                        margin-top: 1rem;
                    ">
                        📥 Download Certificate
                    </button>
                </a>
                '''
                st.markdown(href, unsafe_allow_html=True)
                
                # Preview
                with st.expander("👁️ Certificate Preview"):
                    st.components.v1.html(certificate_html, height=600, scrolling=True)
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                st.session_state.quiz_started = False
                st.session_state.quiz_completed = False
                st.rerun()
        with col2:
            if st.button("📊 View Statistics", use_container_width=True):
                st.info("Statistics feature coming soon!")
    
    else:
        # Quiz in progress
        level = st.session_state.proficiency_level
        questions = quiz_data[level]["questions"]
        current_q = st.session_state.current_question
        
        # Display current question with timer
        if current_q < len(questions):
            # Quiz header with progress
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### 📝 Question {current_q + 1} of {len(questions)}")
            with col2:
                time_elapsed = datetime.datetime.now().strftime("%H:%M")
                st.markdown(f"**⏱️ Started:** {time_elapsed}")
            
            # Display question
            display_question(questions[current_q], current_q, len(questions))
        else:
            st.error("An error occurred. Please restart the quiz.")
            if st.button("🔄 Restart Quiz"):
                st.session_state.quiz_started = False
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.markdown("""
        <div style="text-align: center; color: #666; font-size: 0.9rem; padding: 1rem;">
            <p>© 2024 SPS ASEAN Training Program • All Rights Reserved</p>
            <p>🪂 Promoting Safety & Excellence in Paragliding</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
