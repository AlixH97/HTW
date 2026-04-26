# Energy Production Dashboard
# Mr. & Ms. DA Bootcamp Sep 2024 — HTW Berlin

# ── Imports ──────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
from PIL import Image

# ── Page Configuration ────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Energy Analysis Dashboard",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded"
)

alt.themes.enable("dark")

# ── Data Loading ──────────────────────────────────────────────────────────────
# Load the panel dataset and parse Year as datetime
data = pd.read_csv("Panel format.csv")
data["Year"] = pd.to_datetime(data["Year"], format="%Y")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🌩️ Energy Dashboard")
    st.markdown("---")

    sidebar_image = Image.open("Energy1.jpeg")
    st.sidebar.image(sidebar_image, use_container_width=True)

    country = st.sidebar.selectbox("Select a country:", data["Country"].unique())

    st.markdown("---")
    st.write("Use this dashboard to explore energy production trends over time in different countries.")
    st.markdown("---")

# ── Filter Data by Country ────────────────────────────────────────────────────
country_data = data[data["Country"] == country]

# ── Main Header ───────────────────────────────────────────────────────────────
st.title(f"Energy Production Time Series Analysis — {country}")
st.markdown("""
This dashboard provides a detailed overview of various energy production trends
in the selected country. Use the sidebar to switch between countries.
""")

main_image = Image.open("Energy.jpg")
st.image(main_image, caption="Energy Sources", use_container_width=True)


# ── Chart Function ────────────────────────────────────────────────────────────
def create_chart(data: pd.DataFrame, y: str, title: str, yaxis_title: str) -> None:
    """
    Render an interactive Plotly line chart in Streamlit.

    Args:
        data (pd.DataFrame): Filtered DataFrame for the selected country.
        y (str): Column name to plot on the y-axis.
        title (str): Title displayed above the chart.
        yaxis_title (str): Label for the y-axis.
    """
    fig = px.line(
        data,
        x="Year",
        y=y,
        title=title,
        markers=True,
        line_shape="spline",
        color_discrete_sequence=px.colors.qualitative.Dark24
    )

    # Annotate the most recent data point
    fig.add_annotation(
        x=data["Year"].iloc[-1],
        y=data[y].iloc[-1],
        text="Latest Value",
        showarrow=True,
        arrowhead=2,
        font=dict(color="#E74C3C", size=12)
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title=yaxis_title,
        template="plotly_white",
        font=dict(family="Arial, sans-serif", size=16, color="#2C3E50"),
        title=dict(text=title, font=dict(size=22)),
        margin=dict(l=0, r=0, t=80, b=0),
        legend=dict(
            title="Legend",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        hovermode="x unified",
        xaxis=dict(
            rangeslider=dict(visible=True),
            showline=True,
            linewidth=2,
            linecolor="black",
            mirror=True,
            gridcolor="LightGrey"
        ),
        yaxis=dict(
            showline=True,
            linewidth=2,
            linecolor="black",
            mirror=True,
            gridcolor="LightGrey"
        )
    )

    fig.update_traces(
        hovertemplate="<b>Year</b>: %{x}<br><b>Value</b>: %{y}<extra></extra>"
    )

    st.plotly_chart(fig, use_container_width=True)


# ── Charts ────────────────────────────────────────────────────────────────────
st.subheader("📈 Population Over Time")
create_chart(country_data, "pop", "Population over Time", "Population")

st.subheader("🌊 Hydro Energy Production Over Time")
create_chart(country_data, "hydro_ej", "Hydro Energy Production (Exajoules)", "Exajoules")

st.subheader("⚛️ Nuclear Energy Production Over Time")
create_chart(country_data, "nuclear_ej", "Nuclear Energy Production (Exajoules)", "Exajoules")

st.subheader("♻️ Renewable Energy Production Over Time")
create_chart(country_data, "ren_power_ej", "Renewable Energy Production (Exajoules)", "Exajoules")

st.subheader("☀️ Solar Energy Production Over Time")
create_chart(country_data, "solar_ej", "Solar Energy Production (Exajoules)", "Exajoules")

st.subheader("🌬️ Wind Energy Production Over Time")
create_chart(country_data, "wind_ej", "Wind Energy Production (Exajoules)", "Exajoules")
