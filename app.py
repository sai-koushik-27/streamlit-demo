import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


st.title("Phone pe project")
st.subheader("This is phone pe second heading")

st.write("Insurance analysis")

df = pd.read_csv('agg_trans.csv')

categories = st.selectbox("Select Category Column", df.columns)
subcategories = st.selectbox("Select Subcategory Column", df.columns)
values = st.selectbox("Select Values Column", df.columns)

# Plot grouped bar chart

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x=categories, y=values, hue=subcategories, ax=ax)
ax.set_title("Grouped Bar Plot", fontsize=16)
ax.set_xlabel(categories, fontsize=12)
ax.set_ylabel(values, fontsize=12)
st.pyplot(fig)

# insurance = df.groupby("Quarter")['Transaction_amount'].sum().reset_index()
# fig,ax = plt.subplots(figsize=(10, 6))


# sns.barplot(data =insurance,x = 'Quarter',y='Transaction_amount')
# st.pyplot(fig)

