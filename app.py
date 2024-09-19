import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech to Text Converter")
    
    recognizer = sr.Recognizer()

    if st.button("Start Recording"):
        with st.spinner("Listening..."):
            # Use the microphone as the source
            with sr.Microphone() as source:
                # Adjust for ambient noise and record
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source)

        st.success("Recording completed!")

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            st.text_area("You said:", text)
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from the speech recognition service: {e}")

if __name__ == "__main__":
    main()
