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
        "Søren_Østergaard_interview.pdf",
        "Trivselskommissionens_kommissorium.pdf"
    ]

    
    
    st.write(
        'Download disse to filer og find ud af hvordan Fords fund af nye politiske skillelinjer kan bruges til at forstå Ryan og Ehlingers koncept "Issue Publics"')

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
