import streamlit as st
import mysql.connector
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta
import base64

# Connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Your MySQL password
        database='sasyam'
    )

# Initialize chat messages from the database
def load_messages():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM community WHERE timestamp >= %s ORDER BY timestamp", (datetime.now() - timedelta(days=3),))
    messages = cursor.fetchall()
    conn.close()
    return messages

# Add a new message to the database
def add_message(user, text, image):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        if image:
            # Convert image to binary
            buffered = BytesIO()
            image.save(buffered, format="PNG")
            img_binary = buffered.getvalue()
            cursor.execute("INSERT INTO community (user, text, image, timestamp) VALUES (%s, %s, %s, %s)", 
                           (user, text, img_binary, datetime.now()))
        else:
            cursor.execute("INSERT INTO community (user, text, timestamp) VALUES (%s, %s, %s)", 
                           (user, text, datetime.now()))
        conn.commit()
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
    finally:
        conn.close()

def format_timestamp(timestamp):
    now = datetime.now()
    if timestamp.date() == now.date():
        return f"<span style='color: gray; font-size: 0.8em;'>{timestamp.strftime('%I:%M %p')}</span>"  # Time only if the message is from today
    elif timestamp.date() == (now - timedelta(days=1)).date():
        return f"<span style='color: gray; font-size: 0.8em;'>Yesterday, {timestamp.strftime('%I:%M %p')}</span>"
    else:
        return f"<span style='color: gray; font-size: 0.8em;'>{timestamp.strftime('%d %B %Y, %I:%M %p')}</span>"

def app():
    st.title("Chat Community")

    # Display chat history
    
    messages = load_messages()

    # Container to hold chat messages
    chat_container = st.container()
    
    with chat_container:
        last_date = None
        for message in messages:
            message_date = message["timestamp"].date()
            if message_date != last_date:
                # Print the date header if the date has changed
                st.markdown(f"**_{message_date.strftime('%d/%m/%Y')}_**", unsafe_allow_html=True)
                last_date = message_date

            timestamp = format_timestamp(message["timestamp"])
            user_info = f"{message['user']} {timestamp}"
            
            if message["user"] == st.session_state.username:
                # Display logged-in user's messages with minimized space between username and message, and more space between messages
                st.markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: flex-start; margin-bottom: 20px;">  <!-- Added margin-bottom for space between messages -->
                        <b>{user_info}</b>
                        <div style="background-color: white; padding: 5px; border-radius: 10px; text-align: left; max-width: 70%; margin-top: 5px;">  <!-- Reduced margin-top for minimized space between username and message -->
                            {message['text']}
                        </div>
                        {f'<img src="data:image/png;base64,{base64.b64encode(message["image"]).decode()}" style="width: 300px; margin-top: 10px;"/>' if message["image"] else ''}  <!-- Display image if exists -->
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                # Display others' messages with minimized space between username and message, and more space between messages
                st.markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: flex-end; margin-bottom: 20px;">  <!-- Added margin-bottom for space between messages -->
                        <b>{user_info}</b>
                        <div style="background-color: white; padding: 5px; border-radius: 10px; text-align: right; max-width: 70%; margin-top: 5px;">  <!-- Reduced margin-top for minimized space between username and message -->
                            {message['text']}
                        </div>
                        {f'<img src="data:image/png;base64,{base64.b64encode(message["image"]).decode()}" style="width: 300px; margin-top: 10px;"/>' if message["image"] else ''}  <!-- Display image if exists -->
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Input form for sending messages
    st.subheader("Send a Message")

    # Upload image icon
    uploaded_image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"], key='uploaded_image')

    text = st.text_area("Enter your message:", key='message_input')

    # Send button
    def send_message(uploaded_image, text):
        if uploaded_image:
            image = Image.open(uploaded_image)
        else:
            image = None

        if text.strip() or image:
            add_message(st.session_state.username, text, image)
            # Clear the uploaded image by resetting the file uploader widget
        else:
            st.warning("Please enter a message or upload an image.")

    # Lambda function for the button
    st.button("Send", on_click=lambda: send_message(uploaded_image, text))

    # Automatically delete messages older than three days
    def delete_old_messages():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM community WHERE timestamp < %s", (datetime.now() - timedelta(days=3),))
        conn.commit()
        conn.close()

    delete_old_messages()

# Run the app
if __name__ == "__main__":
    app()
