import streamlit as st


def app():
    st.title("About Us")
    
    st.image("https://via.placeholder.com/800x300.png?text=Crop+Disease+Detection", caption="Crop Disease Detection App")
    
    st.header("Our Mission")
    st.write("""
        At Sasyam, our mission is to empower farmers and agricultural enthusiasts with cutting-edge technology for detecting and diagnosing crop diseases. 
        We aim to help ensure food security and sustainable farming practices by leveraging AI and machine learning.
    """)

    st.header("What We Do")
    st.write("""
        Our crop disease detection system uses advanced algorithms and image processing techniques to identify common diseases affecting crops. 
        By simply uploading a photo of a plant, our system can quickly analyze the image and provide a diagnosis with suggested remedies.
    """)

    st.header("Why It Matters")
    st.write("""
        Crop diseases can significantly impact food production, leading to losses for farmers and higher food costs for consumers. 
        Early detection and prevention are key to maintaining healthy crops, and our app aims to assist farmers in making informed decisions to protect their crops.
    """)

    st.header("Our Team")
    st.write("""
        We are a group of dedicated individuals with expertise in data science, technology. 
        Our goal is to bridge the gap between modern technology and traditional farming practices.
    """)
    st.image("img.jpeg",width=400, caption="Pratibha,")
    st.image("https://via.placeholder.com/800x300.png?text=Crop+Disease+Detection", caption="Saksham,")
    st.image("https://via.placeholder.com/800x300.png?text=Crop+Disease+Detection", caption="Richa,")
    st.image("IMG.jpg",width=300, caption="Sughandha")
    
    st.subheader("Contact Us")
    st.write("""
        Email: saysam@sasyam.com  
        Phone: +91 8563789078  
        Address: Prayagraj, U.P.
    """)
    

if __name__ == "__main__":
    app()

    