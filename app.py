import os
import streamlit as st
from pipeline import run_research_pipeline


if "GROQ_API_KEY" in st.secrets:
    os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

if "TAVILY_API_KEY" in st.secrets:
    os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]



# PAGE CONFIG
st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS
st.markdown("""
<style>

/* =========================
   GLOBAL APP
   ========================= */

html, body, [data-testid="stAppViewContainer"] {
    background: #0b1120 !important;
}

.stApp {
    background:
        radial-gradient(circle at 80% 10%, rgba(79,70,229,.18), transparent 30%),
        radial-gradient(circle at 10% 90%, rgba(124,58,237,.12), transparent 30%),
        #0b1120 !important;
    color: #f8fafc;
}

/* =========================
   REMOVE STREAMLIT TOP BAR
   ========================= */

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
    min-height: 0px !important;
}

[data-testid="stHeader"] > div {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

#MainMenu {
    display: none !important;
}

footer {
    display: none !important;
}

/* =========================
   MAIN CONTAINER
   ========================= */

.block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 1200px !important;
}

/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background: #080e1c !important;
    border-right: 1px solid rgba(255,255,255,.08);
}

section[data-testid="stSidebar"] > div {
    background: #080e1c !important;
}

.sidebar-brand {
    font-size: 25px;
    font-weight: 800;
    color: #ffffff;
    padding: 10px 0 20px 0;
}

.sidebar-subtitle {
    color: #60a5fa;
    font-size: 14px;
    font-weight: 600;
}

.sidebar-text {
    color: #94a3b8;
    font-size: 14px;
    line-height: 1.7;
}

.pipeline-item {
    color: #cbd5e1;
    padding: 7px 0;
    font-size: 14px;
}

/* =========================
   HERO
   ========================= */

.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 25px;
    border-radius: 25px;
    text-align: center;
    background: linear-gradient(
        135deg,
        #243b8f 0%,
        #4f46e5 50%,
        #7c3aed 100%
    );
    box-shadow:
        0 20px 50px rgba(0,0,0,.35),
        inset 0 1px rgba(255,255,255,.15);
    margin-bottom: 32px;
}

.hero:before {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    background: rgba(255,255,255,.08);
    border-radius: 50%;
    top: -120px;
    right: -60px;
}

.hero h1 {
    position: relative;
    font-size: 46px;
    font-weight: 800;
    color: white;
    margin: 0;
    letter-spacing: -1px;
}

.hero p {
    position: relative;
    font-size: 18px;
    color: #e0e7ff;
    margin: 10px 0 0;
}

/* =========================
   SECTION TITLES
   ========================= */

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #f8fafc;
    margin: 25px 0 16px;
}

/* =========================
   AGENT CARDS
   ========================= */

.agent-card {
    height: 125px;
    padding: 18px 10px;
    border-radius: 18px;
    text-align: center;

    background: rgba(30,41,59,.78);
    border: 1px solid rgba(148,163,184,.20);

    box-shadow: 0 8px 25px rgba(0,0,0,.20);

    transition: all .25s ease;
}

.agent-card:hover {
    transform: translateY(-5px);
    border-color: rgba(99,102,241,.65);
    box-shadow: 0 12px 30px rgba(79,70,229,.20);
}

.agent-icon {
    font-size: 31px;
    margin-bottom: 5px;
}

.agent-title {
    font-size: 16px;
    font-weight: 750;
    color: #f8fafc;
}

.agent-status {
    margin-top: 5px;
    color: #86efac;
    font-size: 12px;
}

/* =========================
   RESEARCH INPUT BOX
   ========================= */

.research-box {
    padding: 25px;
    border-radius: 20px;

    background: rgba(15,23,42,.80);
    border: 1px solid rgba(148,163,184,.16);

    box-shadow: 0 12px 35px rgba(0,0,0,.22);
}

/* =========================
   INPUT
   ========================= */

.stTextInput > div > div > input {
    background: #111827 !important;
    color: #f8fafc !important;

    border: 1px solid #334155 !important;
    border-radius: 12px !important;

    padding: 13px 15px !important;
    font-size: 15px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 1px #6366f1 !important;
}

.stTextInput input::placeholder {
    color: #64748b !important;
}

/* =========================
   BUTTON
   ========================= */

.stButton > button {
    width: 100%;

    border: none !important;
    border-radius: 12px !important;

    padding: 13px 20px !important;

    font-size: 16px !important;
    font-weight: 750 !important;

    color: white !important;

    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed
    ) !important;

    box-shadow: 0 8px 22px rgba(79,70,229,.25);

    transition: all .25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(99,102,241,.40);
}

/* =========================
   TABS
   ========================= */

.stTabs [data-baseweb="tab-list"] {
    gap: 7px;
    padding: 7px;

    background: rgba(15,23,42,.75);
    border-radius: 14px;

    border: 1px solid rgba(148,163,184,.12);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 10px 16px;

    color: #94a3b8;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: #4f46e5 !important;
    color: white !important;
}

/* =========================
   RESULT AREA
   ========================= */

[data-testid="stMarkdownContainer"] {
    color: #e2e8f0;
}

.result-box {
    background: rgba(15,23,42,.65);
    border: 1px solid rgba(148,163,184,.12);
    border-radius: 16px;
    padding: 20px;
}

/* =========================
   STATUS
   ========================= */

[data-testid="stStatusWidget"] {
    background: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 15px !important;
}

/* =========================
   ALERTS
   ========================= */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* =========================
   FOOTER
   ========================= */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    padding: 35px 0 10px;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR
with st.sidebar:
    st.markdown(
        '<div class="sidebar-brand">🧠 ResearchMind AI</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        '<div class="sidebar-subtitle">Multi-Agent Research Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-text">
        ResearchMind AI automatically performs:
        <br><br>
        🔎 Web Research<br>
        📖 Deep Reading<br>
        ✍️ Report Writing<br>
        🧐 Critical Review
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown(
        '<div class="sidebar-subtitle">⚙️ Research Pipeline</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="pipeline-item">01 🔎 Search Agent</div>
        <div class="pipeline-item">02 📖 Reader Agent</div>
        <div class="pipeline-item">03 ✍️ Writer Agent</div>
        <div class="pipeline-item">04 🧐 Critic Agent</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("Powered by LangChain + Groq + Tavily")


# HERO
st.markdown(
    """
    <div class="hero">
        <h1>🧠 ResearchMind AI</h1>
        <p>Multi-Agent AI Research Assistant</p>
    </div>
    """,
    unsafe_allow_html=True
)


# AGENTS
st.markdown(
    '<div class="section-title">🤖 AI Research Team</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

agents = [
    (c1, "🔎", "Search Agent", "● Web Research"),
    (c2, "📖", "Reader Agent", "● Deep Reading"),
    (c3, "✍️", "Writer Agent", "● Report Generation"),
    (c4, "🧐", "Critic Agent", "● Quality Review")
]

for col, icon, title, status in agents:
    with col:
        st.markdown(
            f"""
            <div class="agent-card">
                <div class="agent-icon">{icon}</div>
                <div class="agent-title">{title}</div>
                <div class="agent-status">{status}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

# INPUT
st.markdown(
    '<div class="section-title">🚀 Start Your Research</div>',
    unsafe_allow_html=True
)


topic = st.text_input(
    "Research Topic",
    placeholder="Example: Latest developments in Generative AI",
    label_visibility="collapsed"
)

start = st.button(
    "🚀 Start Deep Research",
    use_container_width=True
)

# RUN RESEARCH
if start:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic.")
        st.stop()

    with st.status(
        "🧠 ResearchMind AI is working...",
        expanded=True
    ) as status:

        try:
            st.write("🔎 Search Agent is finding reliable sources...")
            st.write("📖 Reader Agent is analyzing useful content...")
            st.write("✍️ Writer Agent is preparing the report...")
            st.write("🧐 Critic Agent is reviewing the report...")

            result = run_research_pipeline(topic)

            status.update(
                label="✅ Research completed successfully!",
                state="complete",
                expanded=False
            )

        except Exception as e:
            status.update(
                label="❌ Research failed",
                state="error"
            )

            st.error(f"Error: {e}")
            st.stop()

    # RESULTS
    st.markdown(
        '<div class="section-title">📊 Research Results</div>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔎 Search Results",
        "📖 Detailed Research",
        "📄 Final Report",
        "🧐 Critic Review"
    ])

    with tab1:
        st.subheader("🔎 Search Agent Output")
        st.write(result["search_results"])

    with tab2:
        st.subheader("📖 Reader Agent Output")
        st.write(result["scraped_content"])

    with tab3:
        st.subheader("📄 Final Research Report")
        st.markdown(result["report"])

    with tab4:
        st.subheader("🧐 Critic Analysis")
        st.markdown(result["feedback"])


# FOOTER
st.markdown(
    """
    <div class="footer">
        ResearchMind AI • Search → Read → Write → Critic<br>
        Built with Streamlit • LangChain • Groq • Tavily
    </div>
    """,
    unsafe_allow_html=True
)