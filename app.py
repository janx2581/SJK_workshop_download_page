import streamlit as st
import os


def main():
    st.title("AI workshop SJ-K")

    # Display the image
    image_path = "SJK_logo.png"
    if os.path.exists(image_path):
        st.image(image_path, width=250)
    else:
        st.error("Image not found")

    # Paths to the specific files
    files = [
        "Ryan_and_Ehlinger_Issue_Publics.pdf",
        "Ford_The_Changing_Cleavage_Politics_of_Western_Europe.pdf"
    ]

    
    st.write(
        'Download techekspertgruppens anbefalinger og find ud af hvilke temaer, de har opbygget deres rapport omkring')

    # Additional file for download
    tech_file_path = "Techekspertgruppens anbefalinger om udvikling af kunstig intelligens.pdf"
    if os.path.exists(tech_file_path):
        tech_file_name = os.path.basename(tech_file_path)
        tech_button_label = f"Klik her for at downloade \n{tech_file_name}"
        with open(tech_file_path, "rb") as tech_file:
            st.download_button(
                label=tech_button_label,
                data=tech_file,
                file_name=tech_file_name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
    else:
        st.error("tech file not found!")
    
    st.markdown("_______________________")

    
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
        'Download disse mødenotater for at teste din GPT')

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
