# AI Transcript Summarizer & Mailer

## Overview
This project is a full-stack Streamlit application that allows users to upload meeting transcripts, input custom summarization instructions, generate structured summaries using Google Gemini (via LangChain), edit the summaries, and share them via email. The app is designed for ease of use and secure deployment on Streamlit Cloud.

---

## Approach & Process

### 1. Requirements Gathering
- Enable users to upload text transcripts (e.g., meeting notes, call transcripts).
- Allow custom summarization instructions (e.g., "Summarize in bullet points for executives").
- Use an LLM to generate a structured summary.
- Make the summary editable before sharing.
- Allow sharing the summary via email.
- Ensure secure and easy deployment on Streamlit Cloud.

### 2. Technology Selection
- **Frontend/UI:** Streamlit (for rapid, interactive web UI)
- **LLM Integration:** LangChain (for prompt templating and LLM orchestration)
- **LLM Provider:** Google Gemini (via `langchain-google-genai`)
- **Email:** Python's `smtplib` and `email` libraries
- **Deployment:** Streamlit Cloud

### 3. Implementation Steps
- Set up Streamlit app structure and UI components (file uploader, text areas, buttons).
- Integrate LangChain with Gemini for flexible prompt-based summarization.
- Add editable summary field for user review and modification.
- Implement email sending with clear instructions for Gmail App Passwords.
- Handle API key input securely (via Streamlit secrets or UI prompt).
- Prepare `requirements.txt` for Python dependencies.
- Remove unnecessary system package files (e.g., `packages.txt`).
- Update `pyproject.toml` to disable Poetry package mode for cloud deployment.
- Test locally and on Streamlit Cloud, iterating based on errors and feedback.

---

## Tech Stack

| Layer         | Technology                | Purpose                                    |
|---------------|--------------------------|--------------------------------------------|
| UI            | Streamlit                | Web app, file upload, user interaction     |
| LLM Orchestration | LangChain            | Prompt templating, LLM integration         |
| LLM Provider  | Google Gemini (via LangChain) | Summarization AI                    |
| Email         | smtplib, email           | Sending summaries via email                |
| Deployment    | Streamlit Cloud          | Hosting and public access                  |

---

## Key Features
- **Transcript Upload:** Accepts `.txt` files for summarization.
- **Custom Instructions:** Users can specify how the summary should be generated.
- **LLM Summarization:** Uses Gemini via LangChain for high-quality, prompt-driven summaries.
- **Editable Output:** Users can review and edit the generated summary before sharing.
- **Email Integration:** Securely send summaries via email (Gmail App Passwords recommended).
- **Cloud Ready:** Designed for seamless deployment on Streamlit Cloud.

---

## Security & Best Practices
- API keys are handled via Streamlit secrets or secure UI input.
- Email sending uses App Passwords for Gmail (not main account password).
- No sensitive data is stored on the server.

---

## How to Deploy
1. Add your dependencies to `requirements.txt`.
2. (Optional) Add your Gemini API key to Streamlit secrets, or enter it in the UI.
3. Push your code to GitHub and connect to Streamlit Cloud.
4. The app will install dependencies and launch automatically.

---

## Future Improvements
- OAuth-based email sending for broader provider support.
- Support for more file formats (PDF, DOCX, etc.).
- User authentication and summary history.
- More advanced prompt templates and LLM options.

---

## Author
Vatsal + GitHub Copilot :)
