import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# ----------------- Page Setup -----------------
st.set_page_config(page_title="Model Evaluation Dashboard", layout="centered")
st.title("🧠 Model Evaluation Dashboard")

# ----------------- Load Logo ------------------
try:
    logo = Image.open("LOGO.png")  # Make sure this file is in the same folder
    st.image(logo, width=150)
except FileNotFoundError:
    st.warning("⚠️ LOGO.png not found. Please make sure the file is in the app directory.")

# ----------------- Load Model Evaluation CSV ------------------
try:
    results = pd.read_csv("model_comparison_summary.csv")
    
    st.subheader("📋 Model Performance Summary")
    st.dataframe(results)

    # ----------------- Metric Dropdown ------------------
    metric = st.selectbox("📊 Select Metric to Compare", results.columns[1:])

    # ----------------- Barplot ------------------
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Model', y=metric, data=results, ax=ax, palette="pastel")
    ax.set_title(f"{metric} Comparison Across Models")
    ax.set_ylabel(metric)
    ax.set_xlabel("Model")
    plt.xticks(rotation=15)
    st.pyplot(fig)

except FileNotFoundError:
    st.error("🚫 Could not find 'model_comparison_summary.csv'. Please upload the file.")

# ----------------- Footer ------------------
st.markdown("---")
st.markdown("👨‍💻 Developed by **Gaurang Kumbhar** | Powered by Streamlit")

