# Beaver's Choice Paper Company - Multi-Agent System

This project implements a multi-agent system to streamline quoting and inventory management operations at the fictional Beaver’s Choice Paper Company.

## 💼 Project Overview

Beaver’s Choice struggles with delayed responses to customer inquiries and quote generation. Your task as an AI consultant is to design a multi-agent architecture using up to **five agents** to automate:

- 🔍 Inventory tracking and supplier delivery estimation
- 💸 Smart quote generation based on historical data and cash flow
- 📦 Sales processing and transaction recording
- 📊 Optional: financial reporting

Implemented using **Python 3.8+** and the **smolagents** framework.

---

## 🧠 Agent Design Overview

- **Orchestrator System**: Main orchestration function that processes customer requests and coordinates agent actions.
- **Inventory Agent**: Checks current stock levels, estimates delivery timelines, and manages inventory data.
- **Quoting Agent**: Generates competitive quotes based on historical data and applies bulk discount logic.
- **Sales Processing**: Handles transaction processing and inventory updates using integrated tool functions.
- **Reporting Agent**: Generates comprehensive financial reports including cash balance and top-selling products.

---

## 📁 Project Structure

```
Multi-Agent-PaperSolution/
├── beaver_agent_workflow.pdf          # Diagram showing agent architecture
├── project_starter.py                 # Main implementation with multi-agent system
├── quote_requests.csv                 # Full set of quote requests
├── quote_requests_sample.csv          # Sample requests for testing
├── quotes.csv                         # Historical quote data
├── test_results.csv                   # Generated output after evaluation
├── reflection.md                      # Implementation details and evaluation summary
├── requirements.txt                   # Python dependencies
├── .gitignore                         # Git exclusions
└── README.md                          # Project overview and instructions
```

---

## 🛠 Local Setup Instructions

This project features a **single-file implementation** in `project_starter.py` for easy deployment and testing. The design decisions and implementation details are documented in `reflection.md`.

### 1. Create Virtual Environment

```bash
python3 -m venv venv-paper-solution
source venv-paper-solution/bin/activate
```

### 2. Install Dependencies

Install all required packages from the requirements file:

```bash
pip install -r requirements.txt
```

This includes: pandas, openai, SQLAlchemy, python-dotenv, and smolagents.

### 3. Add OpenAI API Key

Create a `.env` file and paste your Vocareum API key:

```
UDACITY_OPENAI_API_KEY=voc-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Quick Start

To get started immediately:

```bash
python project_starter.py
```

---

## ▶️ How to Run the Project

Once setup is complete, run the main implementation:

```bash
python project_starter.py
```

This will:
- Initialize the SQLite database with sample data
- Load `quote_requests_sample.csv` for processing
- Process requests through the multi-agent system
- Generate and save results to `test_results.csv`
- Display a comprehensive financial report

---

## 📈 Project Results

Based on the evaluation documented in `reflection.md`:

- **Total Orders Processed**: 19
- **Total Revenue Generated**: $392.50
- **Final Cash Balance**: $45,059.70

### Top Selling Items
- **Cardstock**: 8 orders, 800 total units
- **Glossy paper**: 5 orders, 1000 total units
- **A4 paper**: 4 orders, 1050 total units

---

## ✅ Submission Checklist

Ensure your submission includes:

- `project_starter.py` (fully working multi-agent implementation)
- `beaver_agent_workflow.pdf` (workflow diagram)
- `test_results.csv` (evaluation results)
- `reflection.md` (implementation details and evaluation summary)
- `README.md` (this file)

---

## 🧠 Pro Tips

- Use the exact item names in the database
- Apply bulk discount logic in your quoting agent
- Include dates in all decision-making logic
- Add logging or print statements to debug agent behavior

---

Built with ❤️ using `smolagents`, `pandas`, `sqlite3`, and your brilliant brain.