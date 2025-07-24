import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech
import os

def main():
    st.title("🎙️ Multilingual AI Assistant")

    st.markdown(
        """
        This assistant can listen to your voice, process your query using LLM, and speak the response back.
        """
    )

    # Optional: Sidebar for model selection
    model_name = st.sidebar.selectbox(
        "Choose LLM Model",
        options=["default"],  # Extend with more models if llm_model_object supports it
    )

    if st.button("🎤 Ask me anything"):
        with st.spinner("Listening..."):
            try:
                text = voice_input()
                st.success(f"You said: {text}")

                response = llm_model_object(text)
                text_to_speech(response)

                # Read and play generated speech.mp3
                with open("speech.mp3", "rb") as audio_file:
                    audio_bytes = audio_file.read()

                st.text_area(label="📝 Response:", value=response, height=250)
                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="⬇️ Download Speech",
                    data=audio_bytes,
                    file_name="speech.mp3",
                    mime="audio/mp3"
                )

                # Optional: Clean up file after sending
                os.remove("speech.mp3")

            except Exception as e:
                st.error(f"⚠️ An error occurred: {e}")

if __name__ == '__main__':
    main()
