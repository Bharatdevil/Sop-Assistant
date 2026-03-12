import streamlit as st
import requests

st.title("DocuMind Enterprise - RAG Assistant")

# store conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# chat input box
question = st.chat_input("Ask a question about the documents")

if question:

    # show user question
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    # call FastAPI
    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={"question": question}
    )

    data = response.json()

    # handle rate limit or errors
    if "answer" not in data:
        with st.chat_message("assistant"):
            st.error(data.get("error", "Something went wrong"))

        st.session_state.messages.append(
            {"role": "assistant", "content": data.get("error", "Something went wrong")}
        )

    else:
        answer = data["answer"]

        sources_text = ""

        if data["sources"]:
            sources_text = "\n\n**Sources:**\n"
            for s in data["sources"]:
                sources_text += f"- Page {s['page']} – {s['document']}\n"

        final_answer = answer + sources_text

        with st.chat_message("assistant"):
            st.markdown(final_answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": final_answer}
        )