import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io

from curve_fitter.class_for_for_getting_table_values import table_values
from curve_fitter.class_for_solving_equations import solving_eq

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Curve Fitting Tool",
    layout="wide",
    page_icon="🧮"
)

# ---------- CUSTOM CSS STYLING ----------
st.markdown("""
    <style>
    body {
        background-color: #fffbea;  
        color: #1e1e1e;
        font-family: "Poppins", sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #222222;
        font-weight: 700;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #256d5a;
        color: #ffffff;
        font-size: 1.1rem;
        padding: 0.6em 1.5em;
        border-radius: 12px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1c5446;
        transform: scale(1.03);
    }
    .stRadio label, .stSelectbox label {
        font-size: 1.05rem !important;
        color: #4A90E2 !important;
    }
    label, .stTextInput label, .stSlider label {
        color: #A7C7E7 !important;
    }
    .stDataFrame {
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    .stDataFrame [class^="row_heading"],
    .stDataFrame [class^="col_heading"],
    .stDataFrame [class^="cell"] {
        color: #222222 !important;
    }
    footer, footer * {
        color: #444444 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("""
    <div style="
        background-color: #fff5dc;
        border-radius: 18px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #222222;
        text-align: center;
    ">
        <h1>🧮 Curve Fitting Tool</h1>
        <p>Fit a <b>Straight Line</b>, <b>Parabola</b>, or <b>Geometric Curve</b> to your data interactively.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ---------- LAYOUT SPLIT ----------
left, right = st.columns([1, 1], gap="large")

# ================= LEFT SIDE: INPUT PANEL =================
with left:
    st.header("📥 Input Data")
    st.markdown("<br>", unsafe_allow_html=True)

    data_option = st.radio("Select input method:", ("Manual Entry", "Upload CSV", "Generate Sample Data"))

    x = y = None

    if data_option == "Manual Entry":
        col1, col2 = st.columns(2)
        x_input = col1.text_input("Enter X values (space-separated):", "1 2 3 4 5")
        y_input = col2.text_input("Enter Y values (space-separated):", "2 5 11 20 30")
        try:
            x = np.array(list(map(float, x_input.split())))
            y = np.array(list(map(float, y_input.split())))
        except:
            st.error("⚠️ Please enter valid numeric values.")
            st.stop()

    elif data_option == "Upload CSV":
        uploaded_file = st.file_uploader("Upload a CSV with columns 'x' and 'y'", type=['csv'])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            if 'x' not in df.columns or 'y' not in df.columns:
                st.error("⚠️ CSV must contain 'x' and 'y' columns.")
                st.stop()
            x, y = df['x'].to_numpy(), df['y'].to_numpy()
            st.success(f"✅ Uploaded {len(x)} data points successfully.")

    elif data_option == "Generate Sample Data":
        n = st.slider("Number of points", 5, 50, 10)
        slope = st.slider("Slope (for linear trend)", 0.1, 10.0, 2.0)
        intercept = st.slider("Intercept", 0.0, 10.0, 1.0)
        noise = st.slider("Noise level", 0.0, 2.0, 0.5)
        x = np.linspace(1, 10, n)
        y = slope * x + intercept + np.random.normal(0, noise, n)
        st.dataframe(pd.DataFrame({"x": x, "y": y}))

    if x is not None and y is not None and x.size != y.size:
        st.error("⚠️ X and Y must have the same number of values.")
        st.stop()

    st.markdown("<br>", unsafe_allow_html=True)
    curve_type = st.selectbox("Select Curve Type", ["Straight Line", "Parabola", "Geometric Curve"])
    fit_button = st.button("🎯 Fit Curve")

# ================= RIGHT SIDE: RESULTS PANEL =================
with right:
    st.header("📈 Results & Visualization")

    if 'fit_button' not in locals():
        fit_button = False

    if fit_button:
        solver = solving_eq()
        tbl = table_values(x, y)
        fig, ax = plt.subplots(figsize=(6, 4))

        if curve_type == "Straight Line":
            vals = tbl.For_straight_line()
            AB = solver.Straight_line(vals)
            df_table = pd.DataFrame({"x": tbl.x, "y": tbl.y, "x²": tbl.x2, "xy": tbl.xy})
            X_line = np.linspace(min(x), max(x), 100)
            Y_line = AB[0] * X_line + AB[1]
            ax.scatter(x, y, color='#c0392b', label='Data Points')
            ax.plot(X_line, Y_line, color='#1b5e20', linewidth=2.5, label=f"y = {round(AB[0],3)}x + {round(AB[1],3)}")
            ax.legend()
            ax.grid(True, linestyle='--', alpha=0.6)
            st.success(f"✅ Equation: **y = {round(AB[0],3)}x + {round(AB[1],3)}**")

        elif curve_type == "Parabola":
            vals = tbl.For_parabola()
            ABC = solver.Parabola_eq(vals)
            df_table = pd.DataFrame({
                "x": tbl.x, "y": tbl.y, "x²": tbl.x2, "x³": tbl.x3, "x⁴": tbl.x4, "xy": tbl.xy, "x²y": tbl.x2y
            })
            X_line = np.linspace(min(x), max(x), 100)
            Y_line = ABC[0]*(X_line**2) + ABC[1]*X_line + ABC[2]
            ax.scatter(x, y, color='#c0392b')
            ax.plot(X_line, Y_line, color='#145a32', linewidth=2.5,
                    label=f"y = {round(ABC[0],3)}x² + {round(ABC[1],3)}x + {round(ABC[2],3)}")
            ax.legend()
            ax.grid(True, linestyle='--', alpha=0.6)
            st.success(f"✅ Equation: **y = {round(ABC[0],3)}x² + {round(ABC[1],3)}x + {round(ABC[2],3)}**")

        elif curve_type == "Geometric Curve":
            vals = tbl.For_geometriCurve()
            AB = solver.Geometric_eq(vals)
            df_table = pd.DataFrame({
                "x": tbl.x, "y": tbl.y, "log(x)": tbl.logx, "log(y)": tbl.logy,
                "(log(x))²": tbl.logx2, "log(x)log(y)": tbl.logxlogy
            })
            X_line = np.linspace(min(x), max(x), 100)
            Y_line = AB[0] * (X_line ** AB[1])
            ax.scatter(x, y, color='#c0392b')
            ax.plot(X_line, Y_line, color='#0b5345', linewidth=2.5,
                    label=f"y = {round(AB[0],3)}x^({round(AB[1],3)})")
            ax.legend()
            ax.grid(True, linestyle='--', alpha=0.6)
            st.success(f"✅ Equation: **y = {round(AB[0],3)}x^({round(AB[1],3)})**")

        st.pyplot(fig)
        st.markdown("### 📊 Calculation Table")
        st.dataframe(df_table, width='stretch')
        csv_data = df_table.to_csv(index=False)
        st.download_button("⬇️ Download Table as CSV", csv_data, "table_values.csv", "text/csv")
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        st.download_button("⬇️ Download Fitted Graph", buf.getvalue(), "fitted_curve.png", "image/png")

st.markdown("<br><hr><center>Developed by <b>Alok Maurya</b> | Powered by Streamlit & NumPy</center>", unsafe_allow_html=True)
