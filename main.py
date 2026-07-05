import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# In hosted environments (e.g., Streamlit Cloud), secrets are often provided
# via st.secrets rather than a local .env file.
for key_name in ("GROQ_API_KEY", "TAVILY_API_KEY"):
    if not os.getenv(key_name):
        try:
            secret_val = st.secrets.get(key_name)
        except Exception:
            secret_val = None
        if secret_val:
            os.environ[key_name] = secret_val

from graph.workflow import build_research_graph


def run_research(query):
    with st.spinner("Planning -> Researching -> Writing -> Critiquing..."):
        try:
            graph = build_research_graph()
            result = graph.invoke({"query": query})

            st.success("✅ Research completed successfully!")

            st.subheader("📋 Final Research Report")
            st.markdown(result.get("final_report", "No report generated."))

            st.download_button(
                "📥 Download as Markdown",
                data=result.get("final_report", ""),
                file_name=f"deepdive_report.md",
                mime="text/markdown"
            )
            # PDF download (new)
            try:
                import markdown
                from weasyprint import HTML
                html_content = markdown.markdown(result.get("final_report", ""))
                pdf_bytes = HTML(string=html_content).write_pdf()
                
                st.download_button(
                    "📕 Download as PDF",
                    data=pdf_bytes,
                    file_name=f"deepdive_report.pdf",
                    mime="application/pdf"
                )
            except ImportError:
                st.info("Install weasyprint for PDF export: pip install weasyprint")
            except OSError as e:
                st.info(
                    "PDF export is unavailable in this environment (missing system libraries for WeasyPrint). "
                    "You can still download Markdown."
                )
                st.caption(f"PDF export detail: {e}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.set_page_config(page_title="DeepDive AI", page_icon="🔍", layout="centered")
st.title("🔍 DeepDive AI")
st.caption("Multi-Agent Autonomous Research Assistant")

# Example queries
examples = [
    "Latest breakthroughs in agentic AI systems in 2026",
    "Impact of AI on software engineering jobs",
    "Compare Grok 4 vs Claude 4 vs GPT-5 capabilities"
]

query = st.text_area("Enter your research topic or question:", height=120, placeholder="What would you like to research?")

col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Start Research", type="primary", use_container_width=True):
        if query:
            run_research(query)
        else:
            st.warning("Please enter a query.")

with col2:
    if st.button("Try Example", use_container_width=True):
        query = st.selectbox("Choose example:", examples)
        if query:
            run_research(query)