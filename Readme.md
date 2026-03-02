# Finance Chatbot — Demonstration & Documentation

🔗 Live Application:
https://finance-chatbot-84pb.onrender.com

👤 Created by:
Ankit Bhatt

LinkedIn: https://www.linkedin.com/in/ankit-bhatt-4a1631388/

# 1. Project Overview

The Finance Chatbot is a rule-based financial analysis chatbot built using Python.

It is designed to answer structured financial questions using company financial datasets containing revenue, net income, assets, liabilities, and derived financial ratios.

The system supports both:

Command Line Interface (CLI) chatbot

Web-based chatbot built using Flask

Cloud-deployed production version (Render)

While building a fully functional AI chatbot typically involves advanced programming and deep learning techniques, this project focuses on a streamlined prototype that demonstrates the fundamentals of chatbot development using predefined financial queries.

The objective is to combine financial analytics, backend engineering, and cloud deployment into a practical working system.

# 2. How the Chatbot Works

The chatbot operates using rule-based logic implemented through Python if–elif conditions.

Workflow

Financial data is loaded using Pandas

Data columns are standardized (lowercase, spacing removed, special characters cleaned)

User input is captured

Input is matched against predefined commands

Relevant financial computations are performed

Structured response is returned

Web Version Flow

User enters query via browser

Flask backend receives POST request

chatbot_logic module processes query

Pandas performs calculations

Response rendered using Jinja template

Gunicorn serves the application in production

# 3. Supported Queries

Users may type the number or supported keywords.

Revenue for latest year

Net income for latest year

Company with highest revenue

Company with highest net income

Revenue growth by company

Profit margin

Debt ratio

Total assets (latest year)

Company with lowest debt ratio

Operating cash flow comparison

Type exit in CLI mode to terminate the session.

# 4. Technologies Used

Python 3.11

Pandas

Flask

Gunicorn (Production WSGI Server)

Docker

Render Cloud Platform

Jupyter Notebook

CSV / Excel financial datasets

# 5. Architecture

User Browser
↓
Render Web Service
↓
Gunicorn (WSGI Production Server)
↓
Flask Application
↓
chatbot_logic Module
↓
Pandas Data Processing
↓
Structured Financial Insight Response

The production environment ensures that the application runs using Gunicorn instead of Flask’s development server.

# 6. Demonstration Steps
CLI Version

Run:

python run_cli.py

User interacts directly in terminal.

Web Version (Local)

Run:

python flask_app.py

Open browser:

http://127.0.0.1:5000

Production Version

Access via:

https://finance-chatbot-84pb.onrender.com

# 7. Data Handling Approach

To ensure robustness and avoid schema mismatch issues, the chatbot automatically:

Converts column names to lowercase

Removes extra spaces

Replaces spaces with underscores

Removes special characters

This makes the application resilient to variations in uploaded CSV/Excel files.

# 8. Example Test Results

Test scenarios include:

Revenue growth calculations

Profit margin evaluation

Highest and lowest financial performers

Debt ratio comparison

Operating cash flow aggregation

Refer to project test cases or screenshots (if included in repository).

# 9. Limitations

Current system limitations include:

Only supports predefined queries

No natural language understanding

No AI/ML model integration

No conversational memory

Requires structured dataset format

Uploaded data stored in memory (demo-oriented)

Free-tier deployment may experience cold-start delay

# 10. Future Improvements

Potential enhancements include:

Natural language query parsing

LLM integration for flexible questions

Multi-user session handling

Database-backed storage

REST API architecture

Authentication and role-based access

Integrated financial visualization dashboard

Logging and monitoring integration

Voice interface support

# 11. Project Structure

Example folder structure:

finance_chatbot_project/
│
├── analysis.ipynb
├── financial_analysis_EDA.ipynb
├── finance_clean_kpis.csv
├── chatbot_logic.ipynb
├── chatbot_logic.py
├── flask_app.py
├── requirements.txt
├── Procfile
├── Dockerfile
├── README.md

# 12. Key Learning Outcomes

Through this project, I strengthened understanding in:

Backend development using Flask

Production deployment using Gunicorn

Data preprocessing with Pandas

Financial KPI computation

Docker-based containerization

Cloud deployment workflows

Debugging real deployment issues (port binding, environment conflicts, CRLF formatting)

Designing structured rule-based chatbot systems

# 13. Conclusion

The Finance Chatbot demonstrates how financial analytics and structured chatbot logic can be combined to build an interactive financial assistant.

It represents a transition from notebook-based data analysis to a fully deployed production-ready web application accessible via a live URL.

This project showcases backend engineering fundamentals, financial data processing capabilities, and cloud deployment practices in a practical and applied manner.