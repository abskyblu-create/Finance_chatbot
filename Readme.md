**Finance Chatbot — Demonstration & Documentation**


# 1. Project Overview

The Finance Chatbot is a ***rule-based chatbot built using Python to answer financial questions*** using company financial data. It supports both:

**Command Line Interface (CLI) chatbot**

**Web-based chatbot using Flask**

The chatbot uses cleaned financial data containing **revenue, net income, assets, liabilities, and derived financial ratios** to answer predefined queries.

The goal: Building a fully functional AI chatbot for financial analysis is a complex process involving advanced programming and deep learning techniques. However, to fit the learning objectives and time constraints, this is a streamlined version that introduces to the basics of chatbot development, focusing on creating a prototype that responds to predefined financial queries. 

# 2. How the Chatbot Works

The chatbot works using **rule-based logic** implemented with Python if–elif statements.

**Workflow**

- Financial data is loaded using pandas.

- Data columns are standardized (lowercase, spaces removed).

- User input is captured.

- Input is matched with predefined commands.

- Relevant data is extracted.

- Response is displayed to user.


**For the web version:**

- User enters query in browser.

- Flask backend processes input.

- Response is displayed on webpage.

# 3. Supported Queries

The chatbot currently responds to predefined financial questions:

**Option Query: Users may type the number or supported keywords. 
1	Revenue for latest year
2	Net income for latest year
3	Company with highest revenue
4	Company with highest net income
5	Revenue growth by company
6	Profit margin
7	Debt ratio
8	Total assets (latest year)
9	Company with lowest debt ratio
10	Operating cash flow comparison
type 'exit' to exit the system**

# 4. Technologies Used

Python

Pandas

Flask (web interface)

Jupyter Notebook

CSV financial dataset

# 5. Demonstration Steps

CLI Version

Run:

**python run_cli.py**


User interacts in terminal.

Web Version

Run:

**python flask_app.py**


Open browser:

http://127.0.0.1:5000

# 6. Example Test Results

- Refer to the images directory for test results.

# 7. Limitations

Current chatbot limitations:

Only supports predefined queries.

Does not understand complex natural language.

No AI/ML model used.

No conversational memory.

Requires structured dataset format.

Error handling limited for unexpected inputs.

# 8. Future Improvements

Possible upgrades:

Natural language understanding

AI/ML integration

Chat memory

Data visualization inside chat

Deployment to cloud

Voice interface

# 9. Project Structure

Example folder:

finance_chatbot_project/
│
├── analysis.ipynb
├── output.csv
├── financial_analysis_EDA.ipynb
├── finance_clean_kpis.csv
├── chatbot_logic.ipynb
├── chatbot_logic.py
├── flask_app.py
├── README.md

# 10. Conclusion

The project demonstrates how financial analytics and chatbot logic can be combined to build an interactive financial assistant.