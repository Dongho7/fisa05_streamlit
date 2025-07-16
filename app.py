import streamlit as st
import pandas as pd
import pandas as np
import plotly.express as px

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)
# st.bar_chart(df.rating, x_label="x축 제목")

st.plotly_chart(fig, use_container_width = True)

#입력

if st.button('Click'):
    st.text(True)


st.data_editor(df)

st.checkbox('Option 1')

write = st.radio('Pick Country:', ['France','Germany'])
st.write(write)

st.selectbox('Select', [1,2,3])

st.multiselect('Multiselect', [1,2,3])

st.slider('Slide me', min_value=0, max_value=10)

st.select_slider('Slide to select', options=[1,'2'])

st.text_input('Enter Article')

st.number_input('Enter required number')

st.text_area('Entered article text')

st.date_input('Select date')

st.time_input('Select Time')

st.file_uploader('File CSV uploader')

data= "hello"


if data:= st.camera_input("Click a Snap"): 
    st.download_button('Download Source data', data, "my.png")

st.color_picker('Pick a color')



#출력 
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = Trues





