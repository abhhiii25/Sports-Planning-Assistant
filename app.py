import streamlit as st
from crew_setup import crew


st.set_page_config(
    page_title="Sports Planning Assistant",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Sports Planning Assistant Agent")

goal = st.text_input(
    "Enter your sports goal",
    placeholder="Example: Show IPL match statistics for CSK vs MI"
)


if st.button("Generate Plan"):

    if goal.strip() == "":
        st.warning("Please enter a goal")

    else:

        with st.spinner("Agents analyzing sports data..."):

            try:

                result = crew.kickoff(
                    inputs={"goal": goal}
                )

                final_output = result.raw

                st.success("Analysis Complete")

                st.markdown("### 📊 Sports Analysis")
                st.markdown(final_output)

            except Exception as e:

                st.error("Error occurred")
                st.write(e)