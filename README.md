# 🔋 Energy Production Dashboard

An interactive data visualization dashboard built with **Python** and **Streamlit** for exploring global energy production trends by country over time.

🌐 **Live App:** [View on Streamlit](https://chdqof8bnnqcvz6p2eqdgv.streamlit.app/)

---

## 📊 Features

- **Country selector** — filter all charts by any country in the dataset using the interactive sidebar
- **6 time series charts** covering:
  - 👥 Population over time
  - 🌊 Hydro energy production (Exajoules)
  - ⚛️ Nuclear energy production (Exajoules)
  - ♻️ Renewable energy production (Exajoules)
  - ☀️ Solar energy production (Exajoules)
  - 🌬️ Wind energy production (Exajoules)
- **Interactive Plotly charts** with hover tooltips, range sliders, and latest value annotations
- **Dark-themed UI** powered by Altair and Streamlit

---

## 🗂️ Project Structure

```
HTW/
├── app.py                # Main Streamlit application
├── Panel format.csv      # Energy dataset (panel format, by country & year)
├── Energy.jpg            # Main banner image
├── Energy1.jpeg          # Sidebar image
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/AlixH97/HTW.git
cd HTW
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Launch the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| streamlit | latest | Web app framework |
| pandas | latest | Data manipulation |
| numpy | latest | Numerical operations |
| plotly | 5.24.1 | Interactive charts |
| Pillow | latest | Image handling |
| altair | latest | Theming |

---

## 📁 Dataset

The dataset (`Panel format.csv`) is structured in panel format with one row per country per year. Key columns:

| Column | Description |
|---|---|
| `Country` | Country name |
| `Year` | Year of observation |
| `pop` | Population |
| `hydro_ej` | Hydro energy production (Exajoules) |
| `nuclear_ej` | Nuclear energy production (Exajoules) |
| `ren_power_ej` | Renewable energy production (Exajoules) |
| `solar_ej` | Solar energy production (Exajoules) |
| `wind_ej` | Wind energy production (Exajoules) |

> Data source: BP Statistical Review of World Energy

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) — dashboard framework
- [Plotly](https://plotly.com/python/) — interactive visualizations
- [Pandas](https://pandas.pydata.org/) — data processing
- [Altair](https://altair-viz.github.io/) — theming

---

## 👤 Author

**Alix H** — Data Analytics Student @ HTW Berlin  
Built as part of the Mr. & Ms. DA Bootcamp (Sep 2024)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
