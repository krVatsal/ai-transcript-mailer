def main():
    import streamlit as st
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.prompts import PromptTemplate
    from langchain.chains import LLMChain
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    # --- Streamlit UI ---
    st.set_page_config(page_title="Transcript Summarizer & Sharer", layout="centered")
    st.title("Transcript Summarizer & Sharer")


    # API Key logic
    try:
        google_api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        google_api_key = None
    if not google_api_key:
        google_api_key = st.text_input("Enter your Gemini API Key", type="password")
        if not google_api_key:
            st.info("Please enter your Gemini API Key to use the app.")
            st.stop()

    # Upload transcript
    txt_file = st.file_uploader("Upload a text transcript (meeting notes, call transcript, etc.)", type=["txt"])

    # Custom prompt
    custom_prompt = st.text_area("Custom instruction/prompt", value="Summarize in bullet points for executives.")

    # Generate summary button
    if st.button("Generate Summary"):
        if txt_file is not None and custom_prompt.strip():
            transcript = txt_file.read().decode("utf-8")
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=google_api_key, temperature=0)
            prompt = PromptTemplate(
                input_variables=["transcript", "instruction"],
                template="""
You are an expert assistant. Here is a transcript:
{transcript}

Instruction: {instruction}

Generate a structured summary as per the instruction.
"""
            )
            chain = LLMChain(llm=llm, prompt=prompt)
            with st.spinner("Generating summary..."):
                summary = chain.run({"transcript": transcript, "instruction": custom_prompt})
            st.session_state["summary"] = summary
        else:
            st.warning("Please upload a transcript and enter a prompt.")

    # Editable summary
    if "summary" in st.session_state:
        st.subheader("Generated Summary")
        edited_summary = st.text_area("Edit the summary as needed:", value=st.session_state["summary"], height=300)
        st.session_state["edited_summary"] = edited_summary

        # Email sharing
        st.subheader("Share via Email")
        recipients = st.text_input("Recipient email addresses (comma separated)")
        sender_email = st.text_input("Your email address")
        sender_password = st.text_input("Your email password (16 digit App Password)", type="password")
        subject = st.text_input("Email subject", value="Meeting Summary")
        if st.button("Send Email"):
            if recipients and sender_email and sender_password:
                try:
                    msg = MIMEMultipart()
                    msg["From"] = sender_email
                    msg["To"] = recipients
                    msg["Subject"] = subject
                    msg.attach(MIMEText(edited_summary, "plain"))
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, [r.strip() for r in recipients.split(",")], msg.as_string())
                    server.quit()
                    st.success("Email sent successfully!")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")
            else:
                st.warning("Please fill all email fields.")


    st.markdown("---")
    st.markdown("Built by Vatsal :)")


if __name__ == "__main__":
    main()
