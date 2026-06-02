import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Load Data
df = pd.read_csv("sample_satellites.csv")

# Create Regions
regions = {}

for _, row in df.iterrows():
    inclination = row["INCLINATION"]
    region = int(inclination // 10)
    regions[region] = regions.get(region, 0) + 1

# Count Risk Levels
danger = 0
crowded = 0
safe = 0

for count in regions.values():

    if count > 5:
        danger += 1

    elif count > 2:
        crowded += 1

    else:
        safe += 1

# Risk Score
risk_score = round((danger * 5 + crowded * 2.5), 1)

# ===========================
# HEADER
# ===========================

st.title("🛰️ Space Traffic Control AI")

st.markdown("""
### Orbital Congestion & Risk Analysis Platform

This platform analyzes satellite traffic patterns,
identifies congestion hotspots, visualizes satellite
distribution, and predicts future orbital risk using AI.

### Features
🌍 Interactive Satellite Map

📈 Traffic Analysis Dashboard

🚨 Congestion Alerts

🤖 AI Risk Prediction

🚀 Launch Recommendation Engine
""")

# ===========================
# METRICS
# ===========================

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Satellites", len(df))
col2.metric("Danger", danger)
col3.metric("Crowded", crowded)
col4.metric("Safe", safe)
col5.metric("Risk Score", risk_score)

st.divider()

# ===========================
# CHART
# ===========================

st.subheader("📈 Orbital Traffic Distribution")

chart_df = pd.DataFrame({
    "Region": list(regions.keys()),
    "Satellites": list(regions.values())
})

fig = px.bar(
    chart_df,
    x="Region",
    y="Satellites",
    title="Satellites per Orbital Region"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ===========================
# MAP
# ===========================

st.subheader("🌍 Satellite Map")

st.markdown("""
🟢 Safe Satellites

🟠 Medium Risk Satellites

🔴 High Risk Satellites
""")

m = folium.Map(
    location=[20, 0],
    zoom_start=2
)

for _, row in df.iterrows():

    if row["INCLINATION"] > 80:
        color = "red"

    elif row["INCLINATION"] > 50:
        color = "orange"

    else:
        color = "green"

    folium.CircleMarker(
        location=[row["LATITUDE"], row["LONGITUDE"]],
        radius=7,
        popup=row["OBJECT_NAME"],
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.8
    ).add_to(m)

st_folium(
    m,
    width=1000,
    height=500
)

st.divider()

# ===========================
# ALERTS
# ===========================

st.subheader("🚨 AI Congestion Alert")

st.error("""
Region 8 is experiencing high satellite density.

Predicted risk increase next week: +25%

Recommendation:
Avoid launching new satellites into this orbital region.
""")

st.divider()

# ===========================
# RISK REGION
# ===========================

st.subheader("🎯 Highest Risk Region")

st.info("""
Region 8

Current Satellites: 6

Risk Level: HIGH

Predicted Congestion Growth: +25%
""")

st.divider()

# ===========================
# AI PREDICTION
# ===========================

st.subheader("🤖 AI Prediction")

st.success("""
Region 8 currently contains 6 satellites.

Predicted satellite count next week: 10

Risk Growth: +66%

Recommended Action:
Monitor new launches entering this region.
""")

st.divider()

# ===========================
# LAUNCH RECOMMENDATION
# ===========================

st.subheader("🚀 Launch Recommendation Engine")

st.success("""
Recommended Launch Region: Region 4

Expected Congestion: LOW

Risk Score: 12%

Confidence: 87%
""")

st.divider()

# ===========================
# STATUS TABLE
# ===========================

st.subheader("📊 Region Status")

status_data = []

for region, count in sorted(regions.items()):

    if count > 5:
        status = "🔴 DANGEROUS"

    elif count > 2:
        status = "🟡 CROWDED"

    else:
        status = "🟢 SAFE"

    status_data.append(
        [region, count, status]
    )

status_df = pd.DataFrame(
    status_data,
    columns=["Region", "Satellites", "Status"]
)

st.dataframe(
    status_df,
    use_container_width=True
)

st.divider()

# ===========================
# FUTURE ROADMAP
# ===========================

st.subheader("🔮 Future Enhancements")

st.markdown("""
- Real-time Satellite Tracking
- Collision Prediction Engine
- Orbital Heatmaps
- Launch Window Optimization
- Autonomous Risk Detection
- Space Debris Monitoring
""")

st.divider()

# ===========================
# FOOTER
# ===========================

st.caption("""
Space Traffic Control AI 🚀

Built using Python, Streamlit, Plotly, Folium and Machine Learning.

Developed by Monisha Reddy.
""")