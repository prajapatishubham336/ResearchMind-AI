# ResearchMind-AI
ResearchMind AI is a multi-agent research assistant built with LangChain, Groq, Tavily, and Streamlit that searches the web, reads sources, generates research reports, and critically reviews the results.


# 🧠 ResearchMind AI

### Multi-Agent AI Research Assistant

ResearchMind AI is an AI-powered multi-agent research system that automatically performs web research, reads relevant sources, generates a structured research report, and reviews the final report using a critic agent.

The project combines **LangChain, Groq, Tavily, BeautifulSoup, and Streamlit** to create a practical AI research workflow.

---

## 🚀 Features

- 🔎 **Web Search Agent** — Searches the web for recent and reliable information.
- 📖 **Reader Agent** — Scrapes relevant web pages and extracts useful content.
- ✍️ **Writer Agent** — Generates a structured and professional research report.
- 🧐 **Critic Agent** — Reviews the generated report and provides feedback.
- 🧠 **Multi-Agent Workflow** — Multiple AI components work together.
- 🎨 **Modern Streamlit UI** — Clean and responsive research dashboard.
- 📊 **Separate Research Results** — Search, detailed research, report, and critic output are displayed separately.
- ⚡ **Groq LLM** — Fast LLM inference using Groq.
- 🌐 **Tavily Search** — Web search for research information.

---

## 🏗️ Project Workflow

```text
                User Research Topic
                       │
                       ▼
                🔎 Search Agent
                       │
                       ▼
                📖 Reader Agent
                       │
                       ▼
                ✍️ Writer Agent
                       │
                       ▼
                🧐 Critic Agent
                       │
                       ▼
              📄 Final Research Report
```

---

## 🖥️ User Interface

ResearchMind AI provides a simple research dashboard with:

- Research topic input
- AI Research Team cards
- Research pipeline status
- Search results
- Detailed scraped research
- Final report
- Critic review

---

<img width="1359" height="650" alt="image" src="https://github.com/user-attachments/assets/33072207-2c1f-4239-a80f-0eea99eeb6a0" />

---
## 🤖 AI Agents

### 1. 🔎 Search Agent

The Search Agent uses the Tavily search tool to find relevant web information about the given research topic.

It returns:

- Title
- URL
- Search snippet

---

### 2. 📖 Reader Agent

The Reader Agent selects a relevant URL from the search results and uses the scraping tool to extract deeper content from the source.

---

### 3. ✍️ Writer Agent

The Writer Agent combines the collected research and generates a structured report containing:

- Introduction
- Key Findings
- Conclusion
- Sources

---

### 4. 🧐 Critic Agent

The Critic Agent evaluates the generated report and provides:

- Score
- Strengths
- Areas to Improve
- Final Verdict

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| LangChain | AI application framework |
| LangChain Agents | Multi-agent workflow |
| Groq | LLM inference |
| Tavily | Web search |
| BeautifulSoup | Web scraping |
| Requests | HTTP requests |
| Streamlit | User Interface |
| python-dotenv | Environment configuration |

The project requirements include the LangChain/Groq ecosystem, Tavily, BeautifulSoup, Requests, dotenv and supporting Python packages. :contentReference[oaicite:2]{index=2}

---

## 📁 Project Structure

```text
ResearchMind-AI/
│
├── app.py
├── Agent.py
├── pipeline.py
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Important Files

**`app.py`**

Streamlit frontend for the ResearchMind AI application.

**`Agent.py`**

Contains the Search Agent, Reader Agent, Writer Chain, and Critic Chain. :contentReference[oaicite:3]{index=3}

**`pipeline.py`**

Controls the complete research workflow:

```text
Search → Reader → Writer → Critic
```

:contentReference[oaicite:4]{index=4}

**`tools.py`**

Contains:

- Tavily web search tool
- URL scraping tool

:contentReference[oaicite:5]{index=5}

**`requirements.txt`**

Contains the project dependencies.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/prajapatishubham336/ResearchMind-AI.git
cd ResearchMind-AI
```

### 2. Create Environment

Using Conda:

```bash
conda create -n llmapp python=3.11
conda activate llmapp
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If Streamlit is not included:

```bash
pip install streamlit
```

---

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Do not commit `.env` to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Testing Examples

### Example 1

```text
What are the latest developments in Generative AI?
```

### Example 2

```text
What are the latest trends in AI agents?
```

### Example 3

```text
Research LangGraph and explain its main features, use cases, and advantages.
```

### Example 4

```text
Research the latest applications of AI in Data Science.
```

### Full Pipeline Test

```text
Research the latest developments in Generative AI, explain the key technologies and real-world applications, write a detailed professional report, and critically review the report.
```

---

## 📊 Research Output

After completing the research, the application provides four sections:

```text
🔎 Search Results
        ↓
📖 Detailed Research
        ↓
📄 Final Report
        ↓
🧐 Critic Review
```

---

## 🔒 Security

- API keys are stored in environment variables.
- `.env` should not be committed to GitHub.
- Sensitive credentials should never be hardcoded.
- Production deployments should use platform secret management.

---

## 🌐 Deployment

ResearchMind AI can be deployed using **Streamlit Community Cloud**.

Basic deployment flow:

```text
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
Configure Secrets
        ↓
Deploy
        ↓
Live ResearchMind AI App
```

For deployment, add the required environment variables through the hosting platform's secret management instead of uploading `.env`.

---

## ⭐ Advantages

- Multi-agent architecture
- Automated research workflow
- Real-time web research
- Source-based research
- Automated report generation
- Automated report criticism
- Simple and attractive UI
- Easy to extend with additional agents and tools

---

## 🔮 Future Scope

Possible future improvements:

- 📚 PDF and document research
- 🗄️ Research history
- 📑 Automatic PDF report export
- 🔗 Better source citation
- 🌐 Multiple search providers
- 💬 Research chatbot
- 📊 Research analytics
- 👥 More specialized AI agents
- 🔄 Human-in-the-loop review
- ☁️ Cloud deployment

---

## 🎯 Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models
- LangChain
- AI Agents
- Multi-Agent Systems
- Tool Calling
- Web Search
- Web Scraping
- Prompt Engineering
- LLM-based Report Generation
- AI-based Criticism
- Streamlit Application Development
- API Integration

---

## 💡 Why ResearchMind AI?

Traditional research requires manually searching multiple websites, reading different sources, collecting information, writing a report, and reviewing the final content.

ResearchMind AI automates this workflow using multiple specialized AI components.

```text
Manual Research
      ↓
Search → Read → Write → Review
      ↓
       AI
      ↓
ResearchMind AI
```

---

## 📌 Project Status

**Status:** 🟢 Active Development

The core multi-agent research pipeline and Streamlit interface are implemented.

---

## 👨‍💻 Author

**Shubham Prajapati**

AI / ML / Generative AI 

---

## 📄 License

This project is intended for educational and portfolio purposes.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
