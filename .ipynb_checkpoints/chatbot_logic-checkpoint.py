#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd


# In[112]:


df = pd.read_csv("finance_clean_kpis.csv")


# In[113]:


df


# In[114]:


# now what could happen is you may write question Debt Ratio and in your df it is debt ratio..
# so remove such name cases error:

df.columns = (
    df.columns
        .str.strip()        # remove spaces at start/end
        .str.lower()        # convert to lowercase
        .str.replace(" ", "_")   # replace spaces with _
        .str.replace(r"[^\w]", "", regex=True)  # remove special chars
)


# In[115]:


df


# In[116]:


# if you see closely -> its revenue_growth_ and no (%) -> not looking good
# Special characters like '%' cannot be used in variable names, which is why it's being replaced with an underscore.


df.rename(columns={'revenue_growth_': 'revenue_growth_(%)'}, inplace=True)
df.rename(columns={'net_income_growth_': 'net_income_growth_(%)'}, inplace=True)
df.rename(columns={'profit_margin_': 'profit_margin_(%)'}, inplace=True)
df.rename(columns={'operating_cf_margin_': 'operating_cf_margin_(%)'}, inplace=True)
df.rename(columns={'asset_growth_': 'asset_growth_(%)'}, inplace=True)


# The `inplace=True` parameter is used in many pandas methods to modify the DataFrame directly without creating a new copy. 
### What `inplace=True` does:
# 1. **Modifies the original object**: Changes are applied directly to the original DataFrame
# 2. **Saves memory**: Avoids creating a new copy of potentially large DataFrames
# 3. **No need for reassignment**: You don't need to write `df = df.rename(...)`


# In[117]:


df


# # Chatbot Basic Structure based Rule based Logic
# # if else and elif used

# In[118]:


def chatbot(df):

    print("\nFinanceBot Ready!")
    print()
    print("NOTE: Type 'exit' anytime to quit.\n")

    while True:

        print("\nAvailable Questions:")
        print("1. Show revenue for latest year")
        print("2. Show net income for latest year")
        print("3. Company with highest revenue")
        print("4. Company with highest net income")
        print("5. Show revenue growth by company")
        print("6. Show profit margin")
        print("7. Show debt ratio")
        print("8. Show total assets for latest year")
        print("9. Company with lowest debt ratio")
        print("10. Compare operating cash flow")

        user = input("\nEnter question number: ")

        if user.lower() == "exit":
            print("FinanceBot: Goodbye!")
            break

        latest_year = df["year"].max()
        latest = df[df["year"] == latest_year]

        # Q1 Revenue
        if user == "1":
            print(f"\nRevenue in {latest_year}:")
            print(latest[["company", "total_revenue"]])

        # Q2 Net income
        elif user == "2":
            print(f"\nNet Income in {latest_year}:")
            print(latest[["company", "net_income"]])

        # Q3 Highest revenue
        elif user == "3":
            top = latest.loc[latest["total_revenue"].idxmax()]
            print(f"\nHighest revenue company: {top['company']}")

        # Q4 Highest net income
        elif user == "4":
            top = latest.loc[latest["net_income"].idxmax()]
            print(f"\nHighest net income company: {top['company']}")

        # Q5 Revenue growth
        elif user == "5":
            print("\nRevenue Growth:")
            print(df[["company", "year", "revenue_growth_(%)"]])

        # Q6 Profit margin
        elif user == "6":
            print("\nProfit Margin (%):")
            print(df[["company", "year", "profit_margin_(%)"]])

        # Q7 Debt ratio
        elif user == "7":
            print("\nDebt Ratio:")
            print(df[["company", "year", "debt_ratio"]])

        # Q8 Assets
        elif user == "8":
            print(f"\nTotal Assets in {latest_year}:")
            print(latest[["company", "total_assets"]])

        # Q9 Lowest debt ratio
        elif user == "9":
            safest = latest.loc[latest["debt_ratio"].idxmin()]
            print(f"\nLowest debt ratio company: {safest['company']}")

        # Q10 Cash flow comparison
        elif user == "10":
            print("\nOperating Cash Flow:")
            print(latest[["company", "cash_flow_from_operating_activities"]])

        else:
            print("Sorry, I can only provide information on predefined queries.")


# In[119]:


df


# In[120]:


# chatbot(df) ....cz if it will not let run flask app...initially to check code is fine..later remove or # it


# In[122]:


df.to_csv("chatbot_finalcsv_changes_recorded.csv")


# below: for web based app..aboveis for CLI(command line Interface):only meant for terminal run

def chatbot_web(user, df):
    """
    Web-friendly version of your chatbot.
    Takes user input (like "1", "7", "help") and RETURNS a string.
    Your original chatbot(df) remains untouched for CLI.
    """

    user = (user or "").strip().lower()

    if user in ["help", "h", "?"]:
        return (
            "Available Questions:\n"
            "1. Show revenue for latest year\n"
            "2. Show net income for latest year\n"
            "3. Company with highest revenue\n"
            "4. Company with highest net income\n"
            "5. Show revenue growth by company\n"
            "6. Show profit margin\n"
            "7. Show debt ratio\n"
            "8. Show total assets for latest year\n"
            "9. Company with lowest debt ratio\n"
            "10. Compare operating cash flow\n"
            "\nType a number (1-10)."
        )

    if user == "exit":
        return "Goodbye!"

    latest_year = df["year"].max()
    latest = df[df["year"] == latest_year]

    # Q1 Revenue
    if user == "1":
        return f"Revenue in {latest_year}:\n" + latest[["company", "total_revenue"]].to_string(index=False)

    # Q2 Net income
    elif user == "2":
        return f"Net Income in {latest_year}:\n" + latest[["company", "net_income"]].to_string(index=False)

    # Q3 Highest revenue
    elif user == "3":
        top = latest.loc[latest["total_revenue"].idxmax()]
        return f"Highest revenue company: {top['company']}"

    # Q4 Highest net income
    elif user == "4":
        top = latest.loc[latest["net_income"].idxmax()]
        return f"Highest net income company: {top['company']}"

    # Q5 Revenue growth
    elif user == "5":
        return "Revenue Growth:\n" + df[["company", "year", "revenue_growth_(%)"]].to_string(index=False)

    # Q6 Profit margin
    elif user == "6":
        return "Profit Margin (%):\n" + df[["company", "year", "profit_margin_(%)"]].to_string(index=False)

    # Q7 Debt ratio
    elif user == "7":
        return "Debt Ratio:\n" + df[["company", "year", "debt_ratio"]].to_string(index=False)

    # Q8 Assets
    elif user == "8":
        return f"Total Assets in {latest_year}:\n" + latest[["company", "total_assets"]].to_string(index=False)

    # Q9 Lowest debt ratio
    elif user == "9":
        safest = latest.loc[latest["debt_ratio"].idxmin()]
        return f"Lowest debt ratio company: {safest['company']}"

    # Q10 Cash flow comparison
    elif user == "10":
        return "Operating Cash Flow:\n" + latest[["company", "cash_flow_from_operating_activities"]].to_string(index=False)

    else:
        return "Sorry, I can only provide info on predefined queries. Type 'help'."



if __name__ == "__main__":
    chatbot(df)


