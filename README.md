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

- **Orchestrator Agent**: Delegates subtasks to worker agents based on customer quote requests.
- **Inventory Agent**: Checks current stock and delivery timelines using `get_stock_level`, `get_all_inventory`, `get_supplier_delivery_date`.
- **Quoting Agent**: Generates competitive quotes using `search_quote_history`, `get_cash_balance`.
- **Sales Agent**: Finalizes sales transactions using `create_transaction`.
- **Reporting Agent (Optional)**: Uses `generate_financial_report` for evaluations.

---

## 📁 Project Structure

```
Multi-Agent-PaperSolution/
├── beaver_agent_workflow.pdf          # Diagram showing agent architecture
├── multi_agent_solution.py            # Main Python implementation
├── project_starter.py                 # Provided helper functions and database
├── quote_requests.csv                 # Full set of quote requests
├── quote_requests_sample.csv          # Sample requests for testing
├── quotes.csv                         # Historical quote data
├── test_results.csv                   # Generated output after evaluation
├── .env                               # Stores your Vocareum OpenAI API key
├── .gitignore                         # Git exclusions
├── requirements.txt                   # Python dependencies
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

**Required:** The project requires the `smolagents` framework for multi-agent orchestration.

```bash
pip install -r requirements.txt
pip install smolagents
```

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

Once setup is complete, you have two options:

### Quick Start (Recommended)
```bash
python project_starter.py
```

### Full Implementation
```bash
source venv-paper-solution/bin/activate
python multi_agent_solution.py
```

Both approaches will:
- Load `quote_requests_sample.csv`
- Route requests through your agent system
- Log results to `test_results.csv`

---

## ✅ Submission Checklist

Ensure your submission includes:

- `multi_agent_solution.py` (fully working implementation)
- `beaver_agent_workflow.pdf` (workflow diagram)
- `test_results.csv` (evaluation results)
- `README.md` (this file)

---

## 🧠 Pro Tips

- Use the exact item names in the database
- Apply bulk discount logic in your quoting agent
- Include dates in all decision-making logic
- Add logging or print statements to debug agent behavior

---

Built with ❤️ using `smolagents`, `pandas`, `sqlite3`, and your brilliant brain.