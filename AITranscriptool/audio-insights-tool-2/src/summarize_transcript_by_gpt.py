import streamlit as st
from src.openai.open_ai import OpenAI

PROMPT = """
Please provide a concise summary of the following phone sales transcript. 
Focus on the main topics discussed, including the customer's initial inquiry, key features of the product mentioned by 
the sales representative, any objections or concerns raised by the customer, how these were addressed, and the final 
outcome of the call. Highlight any specific agreements or follow-up actions agreed upon. Ensure the summary captures 
the essential details and flow of the conversation for a clear understanding of the sales interaction.

    Output in the following JSON format:
    {
        "summary": "...",
    }
    """


@st.cache_data(show_spinner=False, ttl=600, persist=None)
def summarize_transcript(transcript):
    messages = [
        {
            "role": "system",
            "content": PROMPT
        },
        {
            "role": "user",
            "content": f"Transcript: {transcript}"
        }
    ]
    try:
        response = OpenAI().create_chat_model(
            model="gpt-4o-mini",
            temperature=0.18,
            messages=messages,
            response_format={"type": "json_object"}
        )
        return response.choices[0].message.content
    except Exception as exp:
        st.error(exp)
