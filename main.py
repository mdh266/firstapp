import streamlit as st
import openai
import ollama
import os
from typing import Iterator
import time
import os

def query_ollama(question: str) -> Iterator[str]:
    response = ollama.generate(model='llama2', 
                                        prompt= question,
                                        stream=True)
    yield "Bot: "
    for chunk in response:
        yield chunk["response"]


def query_openai(question: str) -> Iterator[str]:
    



def main():
    st.sidebar.markdown("# Main App")

    st.write("""
    # My First LLM App With Streamlit!!
            
    This is a simple Question & Answer app, give it a try!
    """)

    messages = st.container(height=200)

    if prompt := st.chat_input("Ask Me Something"):
        messages.chat_message("user").write(f"You: {prompt}")

        with st.status("Generating Response") as status:
            try:
                answer = query_ollama(prompt)
                
            except Exception as e:
                st.exception(e)

            time.sleep(2)
            status.update(label="Done!", state="complete", expanded=False)
        with messages.chat_message("assistant"):
            st.write_stream(answer)
            
        st.balloons()

if __name__ == "__main__":
    main()
