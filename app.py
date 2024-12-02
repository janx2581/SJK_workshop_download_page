import streamlit as st
import os


def main():
    st.title("AI workshop Human Practice Foundation")

    # Display the image
    image_path = "kplogo_white.png"
    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.error("Image not found")

    # Paths to the specific files
    files = [
        "Uddannelse og folkeoplysning 2022 analyse.pdf",
        "Vidensmobilisering og vidensbrobygning – en oversigt over modeller og metoder.pdf"
    ]

    
    
    st.header(
        'Exercise 1: Draft a slide deck outline introducing the Inner Strength Programme for stakeholders')

    st.write(
        'Goal: To create a flexible and reuseable prompt, Human Practice Foundation can use to draft a deck for the Inner Strength Programme.')

    st.markdown(
    '**Prompt:** I am preparing a presentation for [school administrators/donors/teachers] to introduce the Inner Strength Programme, an initiative by the Human Practice Foundation. Please create a well-structured and engaging presentation outline that covers the following [insert points below]. Ensure the tone is [formal, persuasive, or informative] and the structure flows logically. Use this format: \n\n'
    '- Introduction: [e.g., Overview of the Inner Strength Programme and its importance]\n'
    '- Problem Statement: [e.g., Rising mental dissatisfaction among Danish youth and the need for intervention].\n'
    '- Goals: [e.g., Improving self-worth, focus, and relationships in children].\n'
    '- Solution: [e.g., Description of the holistic Inner Strength approach and its implementation].\n'
    '- Impact: [e.g., Results from pilot projects and testimonials from stakeholders].\n'
    '- Impact: [e.g., Results from pilot projects and testimonials from stakeholders].\n'
    '- Call to Action: [e.g., Why this audience’s support is crucial].\n'
    '**Attach the Inner Strength Presentation**')
    
    st.write(
        'Download disse to filer og find ud af hvordan de fire modeller i artiklen kan beskrive fundene i analysen.')

    # Display download buttons for each file
    for file_path in files:
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)
            button_label = f"Klik her for at downloade \n{file_name}"
            with open(file_path, "rb") as file:
                st.download_button(
                    label=button_label,
                    data=file,
                    file_name=file_name,
                    mime="application/pdf"
                )

    st.markdown(
    '**Eksempel prompt:** Opsummer denne artikel med fokus på fonde (indsæt artiklen)')

    st.markdown(
    '**Næste forespørgsel:** Opsummer denne analyse (indsæt analysen)')

    st.markdown(
    '**Næste forespørgsel:** Hvordan kan analysen forstås ud fra de fire modeller præsenteret i artiklen?')

    # Add a small text at the bottom of the page
    st.markdown("_______________________")


    st.header(
        'Øvelse 2: Skriv kronik')
    
    st.write(
        'Få ChatGPT til at skrive en kronik baseret på Fondsanalysen 2024')
    st.write(
        'Link til Fondsanalysen 2024: https://www.kraft-partners.dk/den-danske-fondsanalyse-2024/')
    st.write(
        'Link til en tidligere kronik: https://www.altinget.dk/civilsamfund/artikel/markus-bjoern-kraft-transparens-er-afgoerende-for-de-danske-fonde')

    st.markdown(
    '**Eksempel prompt:** Jeg arbejder i Kraft & Partners og skal skrive en kronik til Altinget, hvor jeg diskuterer fundene for Den Danske Fondsanalyse 2024. \n\n'
    'Giv mig 5 hovedpointer jeg kan benytte. Giv mig derudover 3 sætninger til hver pointe, så jeg får hovedpointerne igennem på en intelligent måde \n'
    'Det her hvad vi skriver om i Fondsanalysen:\n'
    '(Indsæt beskrivelsen fra hjemmesiden)')
    
    st.markdown(
    '**PRØV AT TILFØJ I ET EFTERFØLGENDE PROMPT**: "Skriv det til en kronik. Jeg vedhæfter en tidligere kronik, så du ved hvilken tone-of-voice jeg vil have (Indsæt kronik)"')


    st.markdown(
    '**PRØV AT TILFØJ I ENDNU ET EFTERFØLGENDE PROMPT**: " Lad der være lidt mere glimt i øjet i tonen i kronikken"')

    
    st.markdown("_______________________")

    st.header(
        'Øvelse 3: Opsummer disse mødenotater til et referat')
    
    st.write(
        'Download disse mødenotater for at teste hvordan mødenoter kan struktureres')

    # Additional file for download
    additional_file_path = "ClosedAI_mødenotater_mock_up.docx"
    if os.path.exists(additional_file_path):
        additional_file_name = os.path.basename(additional_file_path)
        additional_button_label = f"Klik her for at downloade \n{additional_file_name}"
        with open(additional_file_path, "rb") as additional_file:
            st.download_button(
                label=additional_button_label,
                data=additional_file,
                file_name=additional_file_name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.error("Additional file not found!")

    st.markdown('''
**EKSEMPEL PROMPT**: 

Jeg har nogle ustrukturerede mødenotater, som jeg gerne vil have organiseret i et klart og struktureret format. Formålet er at få en oversigt over, hvem der har sagt hvad, beslutninger, og hvilke action points der skal tages. Jeg vedhæfter mødenotaterne. Gør det derudover klart, hvis der er uoverensstemmelser i mødenotaterne eller hvis du mangler mere information.

Brug nedenstående struktur til at omdanne notaterne:

Strukturerede Mødenotater:

**Mødedato:** [Indsæt dato]  
**Deltagere:** [Indsæt navne på deltagere]  

1. **Dagsorden og emner**  
Kort oversigt over mødeemner og diskussionspunkter.

2. **Uddybning af hvad der blev sagt under hvert punkt**  

3. **Beslutninger**  
Beslutninger truffet under mødet.

- **Beslutning 1:** [Beskrivelse af beslutningen]  
- **Beslutning 2:** [Beskrivelse af beslutningen]

4. **Action Points**

| Action Point | Ansvarlig | Deadline | Status |
|--------------|-----------|----------|--------|
| [Beskrivelse af action point] | [Navn på ansvarlig] | [Dato] | [Status] |
| [Beskrivelse af action point] | [Navn på ansvarlig] | [Dato] | [Status] |

5. **Opfølgning**  
Eventuelle opfølgningspunkter fra tidligere møder eller som er blevet drøftet under dette møde.

6. **Uklarheder og hvor der er behov for mere information**
''')


    st.markdown("_______________________")
    st.markdown("_Høegh Consulting_")


if __name__ == "__main__":
    main()
