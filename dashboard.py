# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ───────────────────────────────────────────────────────────────
# Page configuration
# ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI-Driven QA Dashboard",
    page_icon="📊",
    layout="wide"
)

# ───────────────────────────────────────────────────────────────
# Title and introduction
# ───────────────────────────────────────────────────────────────
st.title("AI-Driven QA Pipeline Dashboard")
st.markdown("""
Intelligent defect prediction and risk-based test selection using NASA PROMISE JM1 dataset.  
This dashboard provides insights into the dataset, model performance, and simulation results of our intelligent test selection approach.""")

# ───────────────────────────────────────────────────────────────
# Load data and model (cached for performance)
# ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/processed/jm1_cleaned.csv')
        return df
    except FileNotFoundError:
        st.error("Processed dataset not found. Please run the preprocessing notebook first.")
        return None

@st.cache_resource
def load_model():
    try:
        model = joblib.load('models/jm1_rf_baseline_v1.joblib')
        return model
    except FileNotFoundError:
        st.warning("Model not found. Using placeholder data.")
        return None

df = load_data()
model = load_model()

# ───────────────────────────────────────────────────────────────
# Sidebar controls
# ───────────────────────────────────────────────────────────────
st.sidebar.header("Dashboard Controls")
show_dataset_info = st.sidebar.checkbox("Show Dataset Overview", value=True)
show_feature_importance = st.sidebar.checkbox("Show Feature Importance", value=True)
show_simulation_summary = st.sidebar.checkbox("Show Simulation Summary", value=True)
show_cumulative_curve = st.sidebar.checkbox("Show Cumulative Defects Curve", value=True)

# ───────────────────────────────────────────────────────────────
# Main layout - two columns
# ───────────────────────────────────────────────────────────────
col1, col2 = st.columns([1, 1])

# ───────────────────────────────────────────────────────────────
# Left column: Dataset & Model Info
# ───────────────────────────────────────────────────────────────
with col1:
    if show_dataset_info and df is not None:
        st.subheader("Dataset Overview")
        st.write(f"**Shape**: {df.shape}")
        st.write(f"**Total modules**: {len(df)}")
        st.write(f"**Defect rate**: {df['has_defect'].mean():.4f} ({df['has_defect'].sum()} defective modules)")
        st.write(f"**Non-defective rate**: {(1 - df['has_defect'].mean()):.4f}")

    if show_feature_importance and model is not None:
        st.subheader("Top Feature Importance")
        importances = pd.Series(
            model.feature_importances_,
            index=df.drop(columns=['has_defect']).columns if df is not None else []
        ).sort_values(ascending=False).head(10)

        fig_fi, ax_fi = plt.subplots(figsize=(8, 5))
        sns.barplot(x=importances.values, y=importances.index, palette='viridis', ax=ax_fi)
        ax_fi.set_title('Top 10 Features')
        ax_fi.set_xlabel('Importance Score')
        st.pyplot(fig_fi)

# ───────────────────────────────────────────────────────────────
# Right column: Simulation Results
# ───────────────────────────────────────────────────────────────
with col2:
    if show_simulation_summary:
        st.subheader("Intelligent Test Selection Simulation")
        simulation_data = {
            'Approach': ['Full Regression', 'Intelligent Selection (risk-based)'],
            'Tests Executed (%)': [100.0, 29.9],
            'Time Used (%)': [100.0, 60.0],
            'Defects Detected (%)': [100.0, 64.2],
            'Time Saved (%)': [0.0, 40.0],
            'Defects Missed (%)': [0.0, 35.8]
        }
        df_sim = pd.DataFrame(simulation_data)
        st.dataframe(
            df_sim.style.format({
                col: "{:.1f}%" for col in df_sim.columns if '%' in col
            }),
            use_container_width=True
        )

    if show_cumulative_curve:
        st.subheader("Cumulative Defects Detected vs. Tests Executed")
        st.markdown("**Key insight**: Captured **64.2%** of defects executing only **29.9%** of tests → **40%** time savings.")

        # Hardcoded simulation data (from your results)
        cumulative_tests_pct = [0, 10, 20, 29.9, 40, 50, 60, 70, 80, 90, 100]
        cumulative_defects_pct = [0, 20, 35, 64.2, 75, 82, 88, 92, 95, 98, 100]

        fig_curve, ax_curve = plt.subplots(figsize=(10, 6))
        ax_curve.plot(cumulative_tests_pct, cumulative_defects_pct, 
                      marker='o', linewidth=2.5, color='#1f77b4', label='Intelligent Selection')
        ax_curve.plot([0, 100], [0, 100], 'r--', linewidth=1.5, label='Random Selection (baseline)')
        ax_curve.set_xlabel('Percentage of Tests Executed')
        ax_curve.set_ylabel('Percentage of Defects Detected')
        ax_curve.set_title('Intelligent Test Selection Performance')
        ax_curve.legend()
        ax_curve.grid(True, alpha=0.3)
        ax_curve.set_xlim(0, 100)
        ax_curve.set_ylim(0, 100)
        st.pyplot(fig_curve)

# ───────────────────────────────────────────────────────────────
# Footer
# ───────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Project by Cris N. | Senior QA Engineer | Master's in Data Science & AI")
st.caption("Last update: March 2026")