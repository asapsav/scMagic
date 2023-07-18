#This code is a fork from Langchain and Streamlit's Agent repo:
#https://github.com/langchain-ai/streamlit-agent/tree/main
#Credit to these amazing open source developers

from pathlib import Path

import streamlit as st

from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.callbacks import StreamlitCallbackHandler
from langchain.llms import OpenAI

from callbacks.capturing_callback_handler import playback_callbacks
from clear_results import with_clear_container

st.set_page_config(
    page_title="scMagic", page_icon="🧬🦜", layout="wide", initial_sidebar_state="collapsed"
)

# Setup credentials in Streamlit
user_openai_api_key = st.sidebar.text_input(
    "OpenAI API Key", type="password", help="Set this to run your own custom questions."
)

if user_openai_api_key:
    openai_api_key = user_openai_api_key
    enable_custom = True
else:
    openai_api_key = "not_supplied"
    enable_custom = False

# Tools setup
llm = OpenAI(temperature=0, openai_api_key=openai_api_key, streaming=True)

def read_book():
    # looks up
    pass
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions",
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math",
    )#,
    #Tool(
    #    name="FooBar DB",
    #    func=db_chain.run,
    #    description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context",
    #),
]

# Initialize agent
mrkl = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

with st.form(key="form"):
    if not enable_custom:
        "Ask one of the sample questions, or enter your API Key in the sidebar to ask your own custom questions."
    prefilled = st.selectbox("Sample questions", sorted(SAVED_SESSIONS.keys())) or ""
    user_input = ""

    if enable_custom:
        user_input = st.text_input("Or, ask your own question")
    if not user_input:
        user_input = prefilled
    submit_clicked = st.form_submit_button("Submit Question")

output_container = st.empty()
if with_clear_container(submit_clicked):
    output_container = output_container.container()
    output_container.chat_message("user").write(user_input)

    answer_container = output_container.chat_message("assistant", avatar="🦜")
    st_callback = StreamlitCallbackHandler(answer_container)

    # If we've saved this question, play it back instead of actually running LangChain
    # (so that we don't exhaust our API calls unnecessarily)
    if user_input in SAVED_SESSIONS:
        session_name = SAVED_SESSIONS[user_input]
        session_path = Path(__file__).parent / "runs" / session_name
        print(f"Playing saved session: {session_path}")
        answer = playback_callbacks([st_callback], str(session_path), max_pause_time=2)
    else:
        answer = mrkl.run(user_input, callbacks=[st_callback])

    answer_container.write(answer)