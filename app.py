import streamlit as st
import os

def exercise_1():    
    st.header(
        'Exercise 1: Draft a slide deck outline introducing the Inner Strength Programme for stakeholders')

    st.markdown(
        '**Goal:**\n\n' 
        'To create a flexible and reuseable prompt, Human Practice Foundation can use to draft a deck for the Inner Strength Programme.\n')

    st.markdown(
        '**Step 1:**\n\n' 
        'Create the prompt')
    
    
    st.markdown(
        '**Prompt:**\n\n' 
        'I am preparing a presentation for [school administrators/donors/teachers] to introduce the Inner Strength Programme, an initiative by the Human Practice Foundation. Please create a well-structured and engaging presentation outline that covers the following [insert points below]. Ensure the tone is [formal, persuasive, or informative] and the structure flows logically. Use this format:\n'
        '- Introduction: [e.g., Overview of the Inner Strength Programme and its importance]\n'
        '- Problem Statement: [e.g., Rising mental dissatisfaction among Danish youth and the need for intervention].\n'
        '- Goals: [e.g., Improving self-worth, focus, and relationships in children].\n'
        '- Solution: [e.g., Description of the holistic Inner Strength approach and its implementation].\n'
        '- Impact: [e.g., Results from pilot projects and testimonials from stakeholders].\n'
        '- Impact: [e.g., Results from pilot projects and testimonials from stakeholders].\n'
        '- Call to Action: [e.g., Why this audience’s support is crucial].\n\n'
        '- **Attach the Inner Strength Presentation**')
        
    st.write(
        'Examples of what to include:')
    
    st.markdown(
    '- Statistics on mental health challenges among Danish Youth\n'
    '- The holistic approach (adressing children, schools, teachers, and parents)\n'
    '- Success stories or testimonials from previous participants\n'
    '- Upcoming goals (e.g. expansion to 30 schools in 2025\n'
    '- Specific asks or calls to action tailored to the audience (e.g. funding, adoption in school)\n')

    st.markdown(
        '**Step 2:**\n\n' 
        'Iterate')
    
    st.write(
        'Examples on how to iterate:')
    
    st.markdown(
    '- "Focus on the fact that children need to feel their inner guiding light"\n'
    '- "Make the solution paragraph more free flowing without bullet points to increase persuasiveness"\n'
    '- "Combine the goals and solutions slides for me as well as a description of visual elements to include"\n'
    '- "I am a great presenter, and can capture a rooms attention. Make it less wordy"\n')

def jan_drafting_prompt():
    st.header("Jan's Prompt for Drafting")
    st.markdown(
        '**Prompt:**\n\n'
        'I am preparing a presentation for a potential investor to introduce the Inner Strength Programme, an initiative by the Human Practice Foundation. Please create a well-structured and engaging presentation outline that covers the following points below. Ensure the tone is persuasive and the structure flows logically. Use these points:\n'
        '- Introduction: An overview of the Inner Strength Programme and its importance.\n' 
        '- Problem Statement: Rising mental dissatisfaction among Danish youth and the need for intervention.\n' 
        '- Goals: Improving self-worth, focus, and relationships in children.\n' 
        '- Solution: Description of the holistic Inner Strength approach and its implementation.\n' 
        '- Impact: Results from pilot projects and testimonials from stakeholders as well as support from A.P Møller Foundation of DKK 15 million.\n' 
        '- Call to Action: Your support can enhance a digital learning platform, which is crusial for the programmes success. Asking for a donation of 200.000 DKK.\n\n'
        '- **Attach the Inner Strength Presentation**')
    
    st.markdown(
        '**Iteration 1:**\n\n'
        'Combine the Goals and solution to a single slide and write out the slides for me as well as a description of visual elements \n')
    
    st.markdown(
    '**Iteration 2:**\n\n'
        'I am a great presenter, and I can capture a rooms attention. Make it less wordy\n')

def exercise_2():
    st.header("Exercise 2: Write an Op-Ed")
    st.write(
        "Use ChatGPT to write an op-ed based on the Danish Foundation Analysis 2024."
    )
    st.markdown(
        """
        **Example Prompt:** I work at Kraft & Partners and need to write an op-ed for Altinget, discussing the findings of the Danish Foundation Analysis 2024.
        - Provide 5 main points to highlight in the op-ed.
        - Write 3 sentences for each point.
        """
    )
    st.write("Try adding this in a subsequent prompt: **Write it as a complete op-ed using the provided tone-of-voice.**")

def jan_reviewing_prompt():
    st.header("Jan's Prompt for Reviewing")
    st.write(
        "Summarize meeting notes into structured meeting minutes."
    )
    st.markdown(
        """
        **Example Prompt:** I have unstructured meeting notes and need them organized into clear, structured minutes. Use the following structure:
        - Meeting Date
        - Participants
        - Agenda Items
        - Key Discussions
        - Decisions
        - Action Points
        - Follow-Ups
        """
    )
    st.markdown(
        "Ensure to highlight inconsistencies or missing information."
    )

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Exercise 1", "Jan's Prompt for Drafting", "Exercise 2", "Jan's Prompt for Reviewing"])

    st.title("AI Workshop - Human Practice Foundation")
    image_path = "kplogo_white.png"
    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.error("Logo not found.")

    if page == "Exercise 1":
        exercise_1()
    elif page == "Jan's Prompt for Drafting":
        jan_drafting_prompt()
    elif page == "Exercise 2":
        exercise_2()
    elif page == "Jan's Prompt for Reviewing":
        jan_reviewing_prompt()

if __name__ == "__main__":
    main()
