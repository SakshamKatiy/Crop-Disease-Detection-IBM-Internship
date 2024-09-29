import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

def app():
    st.markdown("""
        <style>
            .sidebar .sidebar-content {
                background-color: #f7f7f7;
                padding: 20px;
            }
            .stFileUploader label {
                color: #28a745; /* Green color for label */
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 20px;
                text-align: center;
            }
            .stImage img {
                width: 100%; /* Make the uploaded image width match the file uploader width */
            }
            .stButton>button {
                background-color: #95BF44; 
                color: white;
                border-radius: 25px;
                font-size: 18px;
                padding: 12px;
                width: 100%;
                border: none;
                margin: 10px;
                transition: background-color 0.3s ease, transform 0.2s ease;
                cursor: pointer;
            }
            .stButton>button:hover {
                background-color: #4B5A31; /* Darker green on hover */
                transform: scale(1.05);
            }
            .stButton>button:active {
                background-color: #1e7e34; /* Even darker green on click */
                transform: scale(0.95);
            }
            .arrow1{
            margin-top:50px;
            position:relative;right:22px;
            font-size:40px;
            }

            .arrow{
            margin-top:50px;
            font-size:40px}
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns([1, 0.1, 1, 0.1, 1])
    




    with col1:
        st.image('img/1.png', width=200)
    with col2:
        st.markdown('<p class="arrow1">➔</p>',unsafe_allow_html=True)   
    with col3:
        st.image('img/2.png', width=200)
    with col4:
        st.markdown('<p class="arrow">➔</p>',unsafe_allow_html=True)   
    with col5:
        st.image('img/3.png', width=200)

    st.header("Upload an image of a rice disease-infected crop leaf for disease detection")
    uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        uploaded_image = Image.open(uploaded_file).convert('RGB')
        
        if 'original_image' not in st.session_state:
            st.session_state.original_image = uploaded_image
            st.session_state.current_image = uploaded_image
            st.session_state.show_enhanced = False
            st.session_state.show_segmented = False
            st.session_state.enhanced_image = None
            st.session_state.segmented_image = None

        if st.session_state.show_enhanced and st.session_state.enhanced_image is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.image(st.session_state.original_image, caption="Original Image", use_column_width=True)
            with col2:
                st.image(st.session_state.enhanced_image, caption="Enhanced Image", use_column_width=True)
        elif st.session_state.show_segmented and st.session_state.segmented_image is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.image(st.session_state.original_image, caption="Original Image", use_column_width=True)
            with col2:
                st.image(st.session_state.segmented_image, caption="Segmented Image", use_column_width=True)
        else:
            st.image(st.session_state.current_image, caption="Current Image", use_column_width=True)

        result_index = show_about_disease(uploaded_file)
        class_name = ['Bacterial Leaf Blight', 'Brown Spot', 'Healthy Rice Leaf', 'Leaf Blast']
        st.markdown(f"### Detected Disease: {class_name[result_index]}")
        show_recommendations_and_treatment(result_index)

        if result_index != 2:  
            percentage_disease, volume_cm3 = calculate_disease_percentage_and_volume(st.session_state.original_image)
            st.write(f"### Percentage of Leaf Area Affected by Disease: {percentage_disease:.2f}%")
            st.write(f"### Estimated Volume of Disease Affected Area: {volume_cm3:.2f} cm³")
            
            if percentage_disease <= 20:
                st.success(f"- **If infection is around 20%:** Continue with routine fungicide application. Ensure proper nutrient management and avoid excess watering.")
            elif 20 < percentage_disease <= 50:
                st.warning(f"- **If infection is around 20-50%:** Increase fungicide application frequency. Consider using a combination of treatments. Improve soil management and crop rotation practices.")
            elif percentage_disease > 50:
                st.error(f"- **If infection exceeds 50%:** Immediate intervention is required. Remove heavily infected plants and apply a stronger treatment. Seek advice from an agricultural expert and consider replanting if necessary.")
        else:
            st.write("### No affected area detected. The leaf appears to be healthy.")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button("Enhance Image", on_click=lambda: enhance_button_click())
        with col2:
            st.button("Segment Image", on_click=lambda: segment_button_click())
        with col3:
            st.button("Reset", on_click=lambda: reset_state())
        with col4:
            st.button("Exit", on_click=lambda: exit_app())

def show_about_disease(test_image):
    model = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=[128, 128])
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

def show_recommendations_and_treatment(disease_index):
    recommendations = {
        0: ("Bacterial Leaf Blight", 
            "### Bacterial Leaf Blight\n\n"
            "#### Symptoms:\n"
            "- Grayish-green streaks on leaves\n"
            "- Yellowing and wilting of leaves\n"
            "- Mily ooze drops from leaves\n\n"
            "#### Recommended Treatment:\n"
            "- Apply copper-based fungicides\n"
            "- Manage water levels\n"
            "- Remove infected plant debris\n\n"
            "#### Action Based on Infection Percentage:\n"
            f"- **If infection is around 20%:** Monitor closely and continue with fungicide application. Improve field drainage and avoid overhead irrigation.\n"
            f"- **If infection is around 50%:** Increase fungicide application frequency. Consider using bactericides if the situation worsens. Improve crop rotation and field sanitation.\n"
            f"- **If infection exceeds 70%:** Immediate intervention is required. Remove heavily infected plants and apply a stronger treatment. Seek advice from an agricultural expert and consider replanting if necessary.\n\n"
            "This disease can severely impact yield if not managed effectively. Regular monitoring and prompt action are key."
        ),
        1: ("Brown Spot", 
            "### Brown Spot\n\n"
            "#### Symptoms:\n"
            "- Dark brown, round spots with yellow halos\n"
            "- Small, dark lesions on the leaves\n\n"
            "#### Recommended Treatment:\n"
            "- Ensure adequate soil nutrients\n"
            "- Apply appropriate fungicides\n"
            "- Rotate crops and avoid excess nitrogen\n\n"
            "#### Action Based on Infection Percentage:\n"
            f"- **If infection is around 20%:** Continue with routine fungicide application. Ensure proper nutrient management and avoid excess watering.\n"
            f"- **If infection is around 50%:** Increase fungicide frequency and consider using a combination of treatments. Improve soil management and crop rotation practices.\n"
            f"- **If infection exceeds 70%:** Extensive control measures are needed. Remove infected plants and apply stronger fungicides. Reassess soil and nutrient management practices.\n\n"
            "Managing Brown Spot effectively requires proactive measures and regular monitoring to prevent extensive damage."
        ),
        2: ("Healthy Rice Leaf", 
            "### Healthy Rice Leaf\n\n"
            "#### Status:\n"
            "- No treatment required\n\n"
            "#### Observations:\n"
            "- The leaf appears healthy and free of disease.\n\n"
            "#### Recommendations:\n"
            "- Continue regular monitoring of the crop.\n"
            "- Maintain good field hygiene and proper agronomic practices to prevent future infections.\n\n"
            "Keeping your crop healthy through preventive measures will help avoid potential disease outbreaks."
        ),
        3: ("Leaf Blast", 
            "### Leaf Blast\n\n"
            "#### Symptoms:\n"
            "- Water-soaked lesions on leaves\n"
            "- Lesions with gray centers and dark brown margins\n\n"
            "#### Recommended Treatment:\n"
            "- Apply systemic fungicides\n"
            "- Ensure good field hygiene\n"
            "- Avoid high nitrogen fertilization\n\n"
            "#### Action Based on Infection Percentage:\n"
            f"- **If infection is around 20%:** Monitor closely and apply fungicides as a preventive measure. Improve field sanitation and manage water levels.\n"
            f"- **If infection is around 50%:** Increase fungicide application frequency and consider additional treatments. Enhance field hygiene practices and adjust fertilization strategies.\n"
            f"- **If infection exceeds 70%:** Take immediate action. Remove severely infected plants and apply stronger fungicides. Consult with experts for advanced treatment options and consider replanting if necessary.\n\n"
            "Effective management of Leaf Blast involves timely intervention and strategic treatment to mitigate damage."
        )
    }
    st.markdown(recommendations[disease_index][1])

def enhance_button_click():
    st.session_state.enhanced_image = enhance_image(st.session_state.original_image)
    st.session_state.show_enhanced = True
    st.session_state.current_image = st.session_state.enhanced_image
    st.session_state.show_segmented = False

def segment_button_click():
    st.session_state.segmented_image, _ = segment_image(st.session_state.current_image)
    st.session_state.show_segmented = True
    st.session_state.show_enhanced = False

def enhance_image(image):
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image_cv = cv2.detailEnhance(image_cv, sigma_s=10, sigma_r=0.15)
    enhanced_image = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
    return enhanced_image

def segment_image(image):
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    hsv_img = cv2.cvtColor(image_cv, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([25, 255, 255])
    
    disease_mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

    gray_img = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
    _, leaf_mask = cv2.threshold(gray_img, 120, 255, cv2.THRESH_BINARY)

    leaf_mask_inv = cv2.bitwise_not(leaf_mask)
    holes_within_leaf = cv2.bitwise_and(leaf_mask_inv, leaf_mask_inv, mask=disease_mask)

    contours, _ = cv2.findContours(holes_within_leaf, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output_img = image_cv.copy()

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50: 
            cv2.drawContours(output_img, [contour], -1, (0, 0, 255), 5)

    segmented_image = Image.fromarray(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))

    return segmented_image, None

def reset_state():
    st.session_state.current_image = st.session_state.original_image
    st.session_state.show_enhanced = False
    st.session_state.show_segmented = False
    st.session_state.enhanced_image = None
    st.session_state.segmented_image = None

def exit_app():
    st.session_state.page = 'home'
    st.session_state.sidebar_visible = True
   
def calculate_disease_percentage_and_volume(image):
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    img = cv2.resize(image_cv, (500, 400))

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lb, lg, lr = 25, 0, 0
    ub, ug, ur = 70, 255, 255

    dlb, dlg, dlr = 0, 0, 0
    dub, dug, dur = 25, 255, 255

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, leaf_mask = cv2.threshold(gray_img, 240, 255, cv2.THRESH_BINARY_INV)

    disease_mask = cv2.inRange(hsv_img, np.array([dlb, dlg, dlr]), np.array([dub, dug, dur]))

    disease_mask = cv2.bitwise_and(disease_mask, disease_mask, mask=leaf_mask)

    total_leaf_area = cv2.countNonZero(leaf_mask)
    affected_area = cv2.countNonZero(disease_mask)

    reference_length_cm = 10 
    reference_length_pixels = 100  

    cm_per_pixel = reference_length_cm / reference_length_pixels

    total_area_cm2 = total_leaf_area * (cm_per_pixel ** 2)
    disease_area_cm2 = affected_area * (cm_per_pixel ** 2)

    thickness_cm = 0.5 
    volume_cm3 = disease_area_cm2 * thickness_cm

    percentage_disease_in_leaf = (disease_area_cm2 / total_area_cm2) * 100 if total_area_cm2 > 0 else 0

    return percentage_disease_in_leaf, volume_cm3

if __name__ == "__main__":
    app()
