
import streamlit
import pandas
streamlit.title('My Parents needs Healthy Dinner')
streamlit.title('This is my first application with GITHUB and Streamlit')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
