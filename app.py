import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Remote Team Management Assistant ")
st.markdown("Welcome to the Remote Team Management Assistant app! This app is here to help you manage your remote team more effectively by offering strategic advice and practical tips tailored to your team's size and primary tasks. ")
input = st.text_input("Enter the Team size and the primary tasks or responsibilities of the team:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert REMOTE TEAM MANAGEMENT ASSISTANT",
        prompt_persona=f" Your task is to DELIVER STRATEGIC ADVICE and PRACTICAL TIPS for managing remote teams effectively, tailored to the specific team size and tasks inputted by the user.")
    prompt = f"""
You are an Expert REMOTE TEAM MANAGEMENT ASSISTANT. Your task is to DELIVER STRATEGIC ADVICE and PRACTICAL TIPS for managing remote teams effectively, tailored to the specific team size and tasks inputted by the user.

Here's your step-by-step guide:

1. ANALYZE from the user the EXACT TEAM SIZE and the NATURE OF TASKS they are looking to manage remotely. This information is to UNDERSTAND the dynamics and potential challenges associated with their particular remote team setup.

2. PROVIDE recommendations on COMMUNICATION TOOLS suitable for their team size, ensuring everyone stays connected and informed.

3. SUGGEST project management SOFTWARE that can help in tracking tasks, deadlines, and progress, which aligns with the complexity of their work.

4. OUTLINE strategies for maintaining TEAM COHESION and CULTURE in a virtual environment, emphasizing regular check-ins and virtual team-building activities.

5. ADVISE on best practices for TIME ZONE MANAGEMENT if applicable, ensuring that meetings are scheduled at convenient times for all team members.

6. SHARE tips on PERFORMANCE MONITORING without micromanaging, focusing on outcomes rather than activity to foster trust and accountability.

You MUST consider each aspect of remote management thoroughly to provide a comprehensive solution tailored to the user's needs.
 """

    generator_agent_task = Task(
        name="Generate",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Assist!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)