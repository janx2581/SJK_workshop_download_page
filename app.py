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

    st.write(
        'Eksempel prompt: Vi arbejder i Ebbefos Fonden, hvis mission er at være et modtræk til mistrivsel. Visionen er et samfund, hvor alle trives og har mulighed for at udvikle sig og indgå i positive fællesskaber. Analyser hvordan vores seneste interview stemmer overens med trivselskommissionens kommisorium. Jeg vedhæfter begge to')

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

    # Add a small text at the bottom of the page
    st.markdown("_______________________")


    st.header(
        'Øvelse 2: Skriv linkedin opslag')
    
    st.write(
        'Prøv at få ChatGPT til at skrive et linkedinopslag der minder om jeres tidligere opslag om Rasmus Meyer og jeres tidligere Morgen Talk')
    st.write(
        'Link til jeres oplæg: https://www.linkedin.com/posts/ebbefosfonden_%C3%A5rets-sidste-talk-i-ebbefos-fonden-activity-7247492882666864640-4bnS?utm_source=share&utm_medium=member_desktop')

    st.write(
        'Eksempel prompt: Skriv et LinkedIn-opslag på 120-150 ord, der annoncerer den sidste Morgen Talk i året hos Ebbefos Fonden med Rasmus Meyer, Formand for trivselskommissionen. 

Hovedpunkter fra talerens oplæg: 
- hvad der skal til for at sikre børn og unge nære relationer og positive fællesskaber
- hvordan børn og unge, der har begyndende tegn på mistrivsel, opspores tidligt
- hvordan der kan skabes forudsætningerne for, at alle børn og unge kan udvikle en robusthed og en tro på egen formåen
- hvordan børn og unges digitale dannelse, sikkerhed og tryghed kan styrkes

Eventdetaljer: Dato: 10. december. Sted: Havnegade 23. Tid: 10.00 til 11.00.

Afslut med en opfordring til at tilmelde sig eventet via et link.')

    st.markdown("_______________________")
    
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

    st.markdown("_______________________")
    st.markdown("_Høegh Consulting_")


if __name__ == "__main__":
    main()
