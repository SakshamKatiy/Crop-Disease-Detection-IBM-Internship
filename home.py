import streamlit as st
import tensorflow as tf
import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def reset_tensorflow_graph():
    if tf.__version__.startswith('2.'):
        tf.compat.v1.reset_default_graph()
    else:
        tf.reset_default_graph()

reset_tensorflow_graph()

if 'username' not in st.session_state:
    st.session_state.username = None  
    st.session_state.user_type = None  
    st.session_state.page = 'home' 
    st.session_state.sidebar_visible = True  

def app():
    st.title("Welcome to Sasyam")

    if st.session_state.username:
        st.markdown(f"**Logged in as:** {st.session_state.username} ({st.session_state.user_type})")

        if st.button('Logout', on_click=lambda: logout()):
            pass

    else:
        st.subheader("Enter Your Details")
        username = st.text_input("Enter your username")
        user_type = st.radio(
            "Which of the following best describes you?",
            ("Crop Adviser", "Farmer", "Student", "Researcher")
        )
        if st.button("Proceed", on_click=lambda: proceed(username, user_type)):
            pass
        
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.image('img/a.png', width=250)
        st.write(f"Instant Disease Detection")
    with col2:
        st.image('img/b.png', width=250)
        st.write('Helping Growing Tips')
    with col3:
        st.image('img/c.png', width=250)
        st.write('Supportive Farming Community')   
    
    st.markdown("""
        ### How It Works
        Sasyam helps you detect crop diseases using advanced image processing techniques. 
        Follow the steps below to learn how to use the platform effectively:
        1. **Upload an Image**: Go to the **Disease Detection** page and upload an image of the crop leaf.
        2. **Enhance Image**: Use the **Enhance Image** button to improve image clarity and highlight details.
        3. **Segment Image**: Click the **Segment Image** button to highlight areas of interest and disease on the leaf.
        4. **Get Diagnosis**: The system will analyze the image and provide a diagnosis along with recommendations for treatment.
    """)

def proceed(username, user_type):
    if username and user_type:
        st.session_state.username = username
        st.session_state.user_type = user_type
        st.session_state.page = "Disease detection"
        st.session_state.sidebar_visible = True
    else:
        st.warning("Please enter your username and select a description.")

def logout():
    st.session_state.pop('username', None)
    st.session_state.pop('user_type', None)
    st.session_state.page = 'home'
    st.session_state.sidebar_visible = False

if __name__ == "__main__":
    app()
