import streamlit as st

from app_store.crew import AppStoreCrew

def main():
    st.title("App Store Listing Writer")
    st.sidebar.title("Upload details")

    app_input = st.sidebar.text_area("Enter your app description", height=200)
    if st.sidebar.button("Generate App Store Listing"):
        if  app_input is not None and app_input.strip() != "":
            with open("inputs/input.txt", "w") as f:
                f.write(app_input)
            
            inputs = {"app_input": app_input}
            result = AppStoreCrew().crew().kickoff(inputs=inputs)

            copywriting_task = result.tasks_output[1].raw
            screenshot_caption = result.tasks_output[2].raw

            validation_result = "Validation Result not found."

            if "Validation Result:" in copywriting_task:
                split_content = copywriting_task.split("Validation Result:")

                copywriting_task = split_content[0].strip()

                validation_result = (
                    "Validation Result: " + split_content[1].strip()
                )

            st.subheader("Generated App Store validation result and listing:")
            st.caption(validation_result)

            st.success("App Store listing generated successfully!")
            
            tab1, tab2 = st.tabs(["Copywriting", "Screenshot Caption"])
            with tab1:
                st.text_area("Copywriting", copywriting_task, height=500)
                st.download_button("Download", copywriting_task, "copywriting_task.txt")
            with tab2:
                st.text_area("Screenshot Caption", screenshot_caption, height=500)
                st.download_button("Download", screenshot_caption, "screenshot_caption.txt")

        else:
            st.sidebar.error("Please upload a resume and enter a job description.")
if __name__ == "__main__":
    main()
