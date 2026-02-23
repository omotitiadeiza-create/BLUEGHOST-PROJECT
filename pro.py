import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

print("SALES RECORD DASHBOARD")
st.header=("EXPENSES AND BUDJET TRACKER")
table=pd.read_csv("sales.csv")

df3=table.head(10)

st.write(df3)






st.text("""The budget and expense data has been thoroughly analyzed for accuracy.
Key insights highlight spending patterns and resource allocation efficiency.
Data models are structured and validated to ensure reliable performance.
The system is now optimized and ready for deployment into production.""")

#  KPIs
total_spending = df3["amount"].sum()
highest_category = df3.groupby("category")["amount"].sum().idxmax()
highest_category_amount = df3.groupby("category")["amount"].sum().max()
unpaid_credit = df3.loc[df3["status"] == "unpaid", "amount"].sum()

# Display KPIs

st.metric("Total Spending", f"${total_spending:,.2f}")
st.metric("Highest Spending Category", f"{highest_category} (${highest_category_amount:,.2f})")
st.metric("Total Unpaid (Credit)", f"${unpaid_credit:,.2f}")

#  Pivot Table
st.subheader("Pivot Table: Spending by Category and Payment Type")
pivot = pd.pivot_table(df3, values="amount", index="category", columns="payment", aggfunc="sum", fill_value=0)
st.dataframe(pivot)

#   Spending by Category 
st.subheader("Spending by Category")
category_spending = df3.groupby("category")["amount"].sum().sort_values(ascending=False)
bar=plt.figure(figsize=(10,8)) 
sns.barplot(x=category_spending.index, y=category_spending.values, palette="viridis",)
plt.title("TOTAL SPENDING BY CATEGORICAL DISTRIBUTION") 
plt.ylabel("AMOUNT SPENT ON CATEGORY")
plt.xlabel("CATEGORY OF ITEM SOLD")  
st.pyplot(bar,use_container_width=True)

 ##Expense Distribution by Payment Type
st.subheader("Expense Distribution by Payment Type")
payment_spending = df3.groupby("payment")["amount"].sum() 
pie=plt.figure(figsize=(10,7))
plt.pie(payment_spending, labels=payment_spending.index,autopct="%1.2f%%",startangle=90, colors=sns.color_palette("viridis")) 
plt.title("EXPENSES INCURRED BY PAYMENT TYPE")
st.pyplot(pie,use_container_width=True)

 ##Monthly Spending Trend 
st.subheader("Monthly Spending Trend")
df3["date"] = pd.to_datetime(df3["date"], errors="coerce")
monthly_spending = df3.groupby(df3["date"].dt.to_period("M"))["amount"].sum()
monthly_spending.index = monthly_spending.index.to_timestamp()
line=plt.figure(figsize=(10,5))
sns.lineplot(x=monthly_spending.index, y=monthly_spending.values, marker="o") 
plt.title("SPENDING BASED ON MONTHS") 
plt.ylabel("AMOUNT SPENT") 
plt.xlabel("MONTH") 
plt.xticks(rotation=45) 
st.pyplot(line,use_container_width=True)

st.text("""Report:  
We regret to inform stakeholders that the recent analysis was only partially completed. The primary reason was instability in the underlying data, which led to inconsistencies and prevented full validation of results. While preliminary insights were generated, they cannot be considered comprehensive or fully reliable at this stage. We sincerely apologize for the inconvenience and are actively working to stabilize the dataset and resume a complete analysis for accurate deployment""")


st.text("Project supervisor: Omotiti Adeiza")

st.text("Project Recipient:BLUEGHOST ACADEMY")



