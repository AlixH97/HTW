# 🔋 Energy Production Dashboard

An interactive Streamlit dashboard for exploring energy production trends by country over time.

## 🚀 Live App
[View on Streamlit](https://cykdiehpb4k2jglb2b3kur.streamlit.app/)

## 📊 Features
- Filter by country using the sidebar
- Time series charts for: Population, Hydro, Nuclear, Renewable, Solar, and Wind energy

## 📁 Data
Data sourced from [BP Statistical Review of World Energy] (or whatever your source is).
Columns include: `hydro_ej`, `nuclear_ej`, `ren_power_ej`, `solar_ej`, `wind_ej` (all in Exajoules).

## ⚙️ Setup
```bash
pip install -r requirements.txt
streamlit run final.py
```

**Priority 2 — Fix the deprecated Streamlit warning** by replacing both instances of `use_column_width=True` with `use_container_width=True` in `final.py`.

**Priority 3 — Add a repo description on GitHub** — click the gear icon on the repo page and add something like: *"Interactive Streamlit dashboard for country-level energy production analysis"*. Also add topics like `streamlit`, `python`, `data-visualization`, `energy`.

**Priority 4 — Add a docstring to `create_chart()`**:
```python
def create_chart(data, y, title, yaxis_title):
    """
    Renders a Plotly line chart in Streamlit.
    
    Args:
        data (DataFrame): Filtered country data
        y (str): Column name to plot on y-axis
        title (str): Chart title
        yaxis_title (str): Y-axis label
    """
```


