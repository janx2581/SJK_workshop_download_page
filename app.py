import streamlit as st
import os

def exercise_1():    
    st.header(
        'Exercise 1: Draft a slide deck outline introducing the Inner Strength Programme for stakeholders')

    st.markdown(
        '**Goal:**\n\n' 
        'To create a flexible and reuseable prompt, Human Practice Foundation can use to draft a deck for the Inner Strength Programme.\n')

    st.markdown("_______________________")
    
    st.markdown(
        '**Download the Inner Strength Programme description:**\n\n' 
        'https://www.humanpractice.org/wp-content/uploads/2024/04/Inner-Strength-Case-website-April-2024.pdf')

    st.markdown("_______________________")
    
    st.header(
        'Step 1 - create the prompt')
    
    
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
        '- *Attach the Inner Strength description*')

    st.markdown("_______________________")

    st.write(
        'Examples of what to include in the prompt:')
    
    st.markdown(
    '- Statistics on mental health challenges among Danish Youth\n'
    '- The holistic approach (adressing children, schools, teachers, and parents)\n'
    '- Success stories or testimonials from previous participants\n'
    '- Upcoming goals (e.g. expansion to 30 schools in 2025\n'
    '- Specific asks or calls to action tailored to the audience (e.g. funding, adoption in school)\n')

    st.markdown("_______________________")
    
    st.header(
        'Step 2 - iterate')
    
    st.write(
        'Examples on how to iterate:')
    
    st.markdown(
    '- "Focus on the fact that children need to feel their inner guiding light"\n'
    '- "Make the solution paragraph more free flowing without bullet points to increase persuasiveness"\n'
    '- "Combine the goals and solutions slides for me as well as a description of visual elements to include"\n'
    '- "I am a great presenter, and can capture a rooms attention. Make it less wordy"\n')

def jan_drafting_prompt():
    st.header("My prompt for drafting")
    st.markdown(
        '**Prompt:**\n\n'
        'I am preparing a presentation for a potential investor to introduce the Inner Strength Programme, an initiative by the Human Practice Foundation. Please create a well-structured and engaging presentation outline that covers the following points below. Ensure the tone is persuasive and the structure flows logically. Use these points:\n'
        '- Introduction: An overview of the Inner Strength Programme and its importance.\n' 
        '- Problem Statement: Rising mental dissatisfaction among Danish youth and the need for intervention.\n' 
        '- Goals: Improving self-worth, focus, and relationships in children.\n' 
        '- Solution: Description of the holistic Inner Strength approach and its implementation.\n' 
        '- Impact: Results from pilot projects and testimonials from stakeholders as well as support from A.P Møller Foundation of DKK 15 million.\n' 
        '- Call to Action: Your support can enhance a digital learning platform, which is crusial for the programmes success. Asking for a donation of 200.000 DKK.\n\n'
        '- *Attach the Inner Strength description*')

    st.markdown("_______________________")

    st.header(
        'Iteration 1')
    
    st.markdown(
        'Combine the Goals and solution to a single slide and write out the slides for me as well as a description of visual elements \n')

    st.header(
        'Iteration 2')
        
    st.markdown(
        'I am a great presenter, and I can capture a rooms attention. Make it less wordy\n')

def exercise_2():
    # Paths to the specific files
    files = [
        "PPT_example_HPF.pptx"]

    st.header(
        'Exercise 2: Review a slide deck')

    st.markdown(
        '**Goal:**\n\n' 
        'To create a flexible and reuseable prompt, Human Practice Foundation can use to review a deck for the Inner Strength Programme\n')
    
    st.markdown("_______________________")

    # Paths to the specific files
    files = [
        "PPT_example_HPF.pptx"]

    st.write(
        'If you dont have your own slide deck, you can download my example below')

    # Display download buttons for each file
    for file_path in files:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            button_label = f"Click here to download: \n{file_name}"
            with open(file_path, "rb") as file:
                st.download_button(
                    label=button_label,
                    data=file,
                    file_name=file_name,
                    mime="application/pdf"
                )

    
    st.markdown("_______________________")
    
    st.header(
        'Step 1 - create the prompt')
    
    
    st.markdown(
        '**Prompt:**\n\n' 
        'I have created a draft presentation on [insert topic] for [insert audience]. Please review the slides and provide detailed feedback based on the following [insert key points below]: Use this format for your feedback:\n'
        '- Overall feedback: [e.g. General comments on structure and tone]\n'
        '- Slide-specific feedback: [e.g. Suggestions for improveing for each slide such as clarity, visuals or messaging]\n'
        '- Questions or concerns: [e.g anticipate audience questions or areas of confusion]\n'
        '- Suggestions for improvement: [e.g. tips to make the presentation more engaging or persuassive]\n\n'
        '- *Attach your slide deck*')

    st.markdown("_______________________")

    st.write(
        'Examples of feedback areas to include:')
    
    st.markdown(
    '- Effectiveness of cisual and text balance\n'
    '- Clarity of messaging and alignment with audience needs\n'
    '- Flow and logical structure of the presentation\n'
    '- Recommendations for improving engagement or persuasiveness\n')

    st.markdown("_______________________")

    st.header(
        'Step 2 - Get feedback on individiual slide')
    
    st.write(
        'You can get feedback on the visuals of a single slide by uploading a screenshot')
    
    st.markdown(
    '**Prompt:**\n\n'
        '- "Give me feedback on this specific slide. Focus on the visual impact and structure of the slide" *Insert a screenshot of your slide*')

def jan_reviewing_prompt():
    st.header("My prompt for reviewing")
    st.markdown(
        '**Prompt:**\n\n'
        'I have created a draft presentation for a pitch for potential investors. Please review the slides and provide detailed feedback based on the following: \n'
        '- Clarity of messaging and alignment with audience needs\n' 
        '- Flow and logical structure\n' 
        '- Recommendations for improving persuasiveness and effectiveness of visual and text balance\n\n' 
        'Use this format for your feedback\n' 
        '- Overall feedback: General comments on structure and tone\n' 
        '- Questions or concerns: Anticipate audience questions or ares of confusion\n'
        '- Suggestions for improvement: Tips to make the presentaion more engaging or persuasive\n\n'
        '- *Attach the slide deck*')

    st.markdown("_______________________")
    
    st.markdown(
        '**Prompt for feedback on specific slide:**\n\n'
        'Give me feedback on this specific slide. Focus on the visual impact and structure of the slide. *Insert screenshot*')

    st.markdown("_______________________")
    
    st.header(
        'Iteration 1')

    st.markdown(
        '"Focus more on the persuasiveness of the slides"')

    st.header(
        'Iteration 2')
    
    st.markdown(
        '"What would be a better argument?"')
    
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Exercise 1", "My prompt for drafting", "Exercise 2", "My prompt for reviewing"])

    st.title("AI Workshop - Human Practice Foundation")
    image_path = "logo_HPF.png"
    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.error("Logo not found.")

    if page == "Exercise 1":
        exercise_1()
    elif page == "My prompt for drafting":
        jan_drafting_prompt()
    elif page == "Exercise 2":
        exercise_2()
    elif page == "My prompt for reviewing":
        jan_reviewing_prompt()

if __name__ == "__main__":
    main()
