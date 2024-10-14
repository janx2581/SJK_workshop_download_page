import streamlit as st
import os


def main():
    st.title("AI workshop Ebbefos Fonden")

    # Display the image
    image_path = "Ebbefos-logo-neg-RGB-cropped.svg"
    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.error("Image not found")

    # Paths to the specific files
    files = [
        "Interview_Søren_Østergaard.pdf",
        "Trivselskommissionens_kommissorium.pdf"
    ]

    
    
    st.header(
        'Øvelse 1: Analyser tekster')
    
    st.write(
        'Download disse to filer og find ud af hvor der er overensstemmelse i perspektiverne i de to tekster')

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
    '**Eksempel prompt:** Vi arbejder i Ebbefos Fonden, hvis mission er at være et modtræk til mistrivsel. Visionen er et samfund, hvor alle trives og har mulighed for at udvikle sig og indgå i positive fællesskaber. Analyser hvordan vores seneste interview stemmer overens med trivselskommissionens kommisorium. Jeg vedhæfter begge to')

    # Add a small text at the bottom of the page
    st.markdown("_______________________")


    st.header(
        'Øvelse 2: Skriv linkedin opslag')
    
    st.write(
        'Prøv at få ChatGPT til at skrive et linkedinopslag der minder om jeres tidligere opslag om Rasmus Meyer og jeres tidligere Morgen Talk')
    st.write(
        'Link til jeres oplæg: https://www.linkedin.com/posts/ebbefosfonden_%C3%A5rets-sidste-talk-i-ebbefos-fonden-activity-7247492882666864640-4bnS?utm_source=share&utm_medium=member_desktop')

    st.markdown(
    '**Eksempel prompt:** Skriv et LinkedIn-opslag på 120-150 ord, der annoncerer den sidste Morgen Talk i året hos Ebbefos Fonden med Rasmus Meyer, Formand for trivselskommissionen. \n\n'
    'Hovedpunkter fra talerens oplæg: \n'
    '- hvad der skal til for at sikre børn og unge nære relationer og positive fællesskaber\n'
    '- hvordan børn og unge, der har begyndende tegn på mistrivsel, opspores tidligt\n'
    '- hvordan der kan skabes forudsætningerne for, at alle børn og unge kan udvikle en robusthed og en tro på egen formåen\n'
    '- hvordan børn og unges digitale dannelse, sikkerhed og tryghed kan styrkes\n\n'
    'Eventdetaljer: \n'
    'Dato: 10. december.\n'
    'Sted: Havnegade 23.\n'
    'Tid: 10.00 til 11.00.\n\n'
    'Afslut med en opfordring til at tilmelde sig eventet via et link.')
    
    st.markdown(
    '**PRØV AT TILFØJ I ET EFTERFØLGENDE PROMPT**: "Skriv opslaget i en professionel tone med et glimt i øjet"')


    st.markdown(
    '**PRØV AT TILFØJ I ENDNU ET EFTERFØLGENDE PROMPT**: "Tilføj hvordan det stemmer overens med vores arbejde i Ebbefos Fonden. Brug internettet til at lære hvem vi er"')

    
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
