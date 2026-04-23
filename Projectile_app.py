import math
import streamlit as st

st.set_page_config(page_title="PRI Projectile Motion Calculator", page_icon="🚀")

st.title("PRI Projectile Motion Calculator")
st.write("Simplified projectile motion relationships for height H, range R, and flight time T.")

st.warning("These formulas assume equal launch and landing height and ideal projectile motion without air resistance.")

u = st.number_input("Initial speed u", min_value=0.0, value=50.0, step=1.0)
theta_deg = st.number_input("Launch angle θ (degrees)", min_value=0.1, max_value=89.9, value=45.0, step=1.0)

theta = math.radians(theta_deg)

st.subheader("Choose what you want to calculate")

choice = st.selectbox(
    "Formula Mode",
    [
        "Find H from R and θ",
        "Find H from T, u, θ",
        "Find R from H and θ",
        "Find R from T, u, θ",
        "Find T from R, u, θ",
        "Find T from H, u, θ",
    ]
)

if choice == "Find H from R and θ":
    R = st.number_input("Range R", min_value=0.0, value=100.0)
    H = (R / 4) * math.tan(theta)
    st.success(f"H = {H:.4f}")

elif choice == "Find H from T, u, θ":
    T = st.number_input("Time T", min_value=0.0, value=5.0)
    H = 0.25 * T * u * math.sin(theta)
    st.success(f"H = {H:.4f}")

elif choice == "Find R from H and θ":
    H = st.number_input("Height H", min_value=0.0, value=25.0)
    R = (4 * H) / math.tan(theta)
    st.success(f"R = {R:.4f}")

elif choice == "Find R from T, u, θ":
    T = st.number_input("Time T", min_value=0.0, value=5.0)
    R = T * u * math.cos(theta)
    st.success(f"R = {R:.4f}")

elif choice == "Find T from R, u, θ":
    R = st.number_input("Range R", min_value=0.0, value=100.0)
    T = R / (u * math.cos(theta))
    st.success(f"T = {T:.4f}")

elif choice == "Find T from H, u, θ":
    H = st.number_input("Height H", min_value=0.0, value=25.0)
    T = (4 * H) / (u * math.sin(theta))
    st.success(f"T = {T:.4f}")