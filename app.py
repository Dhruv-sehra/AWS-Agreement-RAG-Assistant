import streamlit as st
import requests

st.title("AWS RAG Assistant")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={
                "question": question
            }
        )

        data = response.json()

        st.subheader("Answer")
        # st.write(response.json())
        st.write(data["answer"])

        with st.expander("Sources"):

            for source in data["sources"]:
                st.write(source)

analytics = requests.get(
    "http://127.0.0.1:8000/analytics"
).json()


st.subheader("Most Frequent Questions")

for item in analytics["most_frequent_questions"]:
    st.write(
        f"{item['question']} ({item['count']} times)"
    )

st.write(
    analytics[
        "most_frequent_questions"
    ]
)

st.subheader(
    "No Answer Queries"
)

st.write(
    analytics[
        "no_answer_queries"
    ]
)

st.metric(
    "Average Latency",
    f"{analytics['average_latency']:.2f} sec"
)