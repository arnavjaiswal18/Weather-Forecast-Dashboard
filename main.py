import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="Select the number of days you want to forecast.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2024-10-28", "2024-10-29", "2024-10-30"]
    temperatures = [13, 12, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


# d, t = get_data(days)  # Put d and t equal to x and y respectively
figure = px.line(x=get_data(days)[0], y=get_data(days)[1], labels={"x": "Date", "y": "Temperature(C)"})
st.plotly_chart(figure)
