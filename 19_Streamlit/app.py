#comment
#Libraries
import streamlit as st 
import pandas as pd
import datetime
import io
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Streamlit Application")

st.header("Welcome to Streamlit")

st.subheader("Running a webb page")

st.write("This is a paragraph with a lot of information concerning streamlit application in data science area")



st.subheader("Buttons")

if st.button("Show image"):
    st.image("zoom2.jpg", caption="Image caption", use_column_width=True)


st.subheader("Slider")

slider_value = st.slider("Select a value:", min_value=0, max_value=100, value=50)

st.write(f"Selected value: {slider_value}")


st.subheader("Checkboxes")
checkbox_value = st.checkbox("Show content")
if checkbox_value:
    st.write("Content displayed.")


st.subheader("Text Input")

name = st.text_input("Enter your name:", "Type here")

st.write(f"Hello, {name}!")


st.subheader("Text Area")

feedback = st.text_area("Your feedback:", "Type your feedback here")
st.write(f"Thank you for your feedback: {feedback}")


st.subheader("Number Input")

age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25, step=1)
st.write(f"Your age is: {age}")

st.subheader("Date Input")

date = st.date_input("Select a date:", None)
st.write(f"Selected date is: {date}")

st.subheader("Time Input")
time = st.time_input("Select a time:", datetime.time(12, 00))
st.write(f"Selected time is: {time}")


st.subheader("Select box")
options = ["Option 1", "Option 2", "Option 3"]

choice = st.selectbox("Choose an option:", options)
st.write(f"You chose: {choice}")

st.subheader("Multiselect")
options = ["Option 1", "Option 2", "Option 3"]
selections = st.multiselect("Choose multiple options:", options)
st.write(f"You chose: {', '.join(selections)}")

st.subheader("Radio Button")
options = ["Option 1", "Option 2", "Option 3"]
choice = st.radio("Choose one option:", options)
st.write(f"You chose: {choice}")

st.subheader("File Uploader")

uploaded_file = st.file_uploader("Choose a file to upload:", type=["csv", "txt", "xlsx"])
if uploaded_file is not None:
    st.write(f"File uploaded: {uploaded_file.name}")


# st.subheader("Download")

# data = {"Column1" : [1,2,3], "Column2":[4,5,6]}
# df = pd.DataFrame(data)

# st.write("Dataframe")
# st.dataframe(df)

# csv_buffer = io.StringIO()

# df.to_csv(csv_buffer, index=False)

# csv_data = csv_buffer.getvalue()

# st.download_button(
#     label="Download CSV",
#     data=csv_data,
#     file_name="sample_data.csv",
#     mime="text/csv"
# )

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.write("Data:")
#     st.dataframe(df)

#     st.write("Bar chart:")
#     plt.bar(df['Category'], df['Latitude'])
#     plt.xlabel('Category')
#     plt.ylabel('Latitudes')
#     st.pyplot(plt)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data:")
    st.dataframe(df)

    st.write("Scatter plot:")

    fig = px.scatter(df, x='Latitude', y='Longitude', color='Category', hover_name='Category')
    st.plotly_chart(fig)


st.subheader("Columns")
col1, col2, col3 = st.columns(3)

col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")

st.sidebar.subheader("Sidebar")



st.sidebar.write("Sidebar content")


st.subheader("Expanders")
with st.expander("Section 1"):
    st.write("Content for Section 1")





