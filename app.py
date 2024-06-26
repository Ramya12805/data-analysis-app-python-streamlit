import streamlit as st
import pandas as pd
import seaborn as sns
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

#Upload Dataset
upload=st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
    data=pd.read_csv(upload)
    
#Preview Dataset
if upload is not None:
    if st.checkbox("Preview DataSet"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
#Finding data types for each column
if upload is not None:
    if st.checkbox("Datatypes for Each Column"):
        st.write("DataTypes")
        st.write(data.dtypes)

#Find the shape of rows or columns
if upload is not None:
    data_shape=st.radio("What dimension Do You Want To Check?",('Rows','Columns'))
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

#Find Null values in the dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!! No missing values")

#Find the duplicates and remove if needed
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This data set contains duplicated values")
        choice=st.selectbox("Do You want to remove duplicated values??",("Select One","Yes","No"))
        if choice=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate values are removed")
        if choice=="No":
            st.text("okay")
    else:
        st.success("No dulicate values in the dataset")

#Summary of the dataset
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))

#About the app
if st.button("About App"):
    st.text("Built with streamlit\n Thank you")
