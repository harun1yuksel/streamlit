
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title("This is a title")
st.text('This is some text.')
st.markdown("Streamlit is **_really_ cool** :+1:")
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.header('This is a header')
st.subheader('This is a subheader')

st.success('This is a success message!')
st.info('This is a purely informational message')
st.error('This is an error')

st.help(range)
st.write('Hello, *World!* :sunglasses:')

# Image
img = Image.open("images.jpeg")
st.image(img,caption="cattie")
st.image(img,caption="cattie",width=300)

# video
# my_video = open(r"path",'rb')
st.video(r'https://youtu.be/3gK_2XdjOdY')

# checkbox
cbox = st.checkbox("Hide and Seek")
if cbox:
    st.write("Hide")
else:
    st.write("Seek")
    
# radio
status = st.radio("Select a color",("blue","orange","yellow"))

st.write(f'Choosing color: {status}')
st.write("Your favourite color is", status)

#buton
if st.button('press Me!'):
    st.success('Analyze Results are...')

# selectbox
occupation = st.selectbox("Your occupation", ["Programmer", "DataScientist","Doctor"])
st.write(f'Your occupation is {occupation}')

# multiselect
multi_select = st.multiselect("Select multiple numbers",[1,2,3,4,5])

# slider
option1 = st.slider("Select a number", min_value=5, max_value=70, value=30, step=5)
option2 = st.slider("Select a number", min_value=0.2, max_value=30.2, value=5.2, step=0.2)

result=option1*option2
st.write("multiplication of two options is:",result)

#text_input
name = st.text_input("Enter your name", placeholder="Your name here")
if st.button("Submit"):
    st.write("Hello {}".format(name.title()))
    
#code
st.code("import pandas as pd")
st.code("import pandas as pd\nimport numpy as np")

with st.echo():
    import pandas as pd
    import numpy as np
    df = pd.DataFrame({"a":[1,2,3], "b":[4,5,6]})
    df
    
#date input
import datetime
today=st.date_input("Today is", datetime.datetime.now())

#time input
the_time=st.time_input("The time is", datetime.time(8,45))
the_time=st.time_input("The time is", datetime.time())

#sidebar
st.sidebar.title("Sidebar title")
st.sidebar.header("Sidebar header")

a=st.sidebar.slider("input",0,5,2,1)
x=st.sidebar.slider("input2")
st.write("# sidebar input result")
st.success(a*x)

# DataFram
st.write("# dataframes")
df = pd.read_csv("Advertising.csv", nrows=(100))
st.table(df.head())
st.write(df.head()) #dynamic, you can sort
st.dataframe(df.head())#dynamic, you can sort

import pickle
filename = 'my_model'
model = pickle.load(open(filename, 'rb'))

TV = st.sidebar.number_input("TV:",min_value=5, max_value=300)
radio = st.sidebar.number_input("radio:",min_value=1, max_value=50)
newspaper = st.sidebar.number_input("newspaper:",min_value=0, max_value=120)

d = pd.DataFrame.from_dict({'TV':TV, 'radio':radio, 'newspaper':newspaper}, orient='index').T

st.write(d)

# buton
if st.button('predict'):
    st.success(f'Analyze Predict:&emsp;{model.predict(d)[0].round(2)}')
    
    
html_temp = """
<div style="background-color:tomato;padding:1.5px">
<h1 style="color:white;text-align:center;">Single Customer </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

st.write("hello23")
