import streamlit as st
import pandas as pd
import pandas as np

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

dict1 = dict(zip(ani_list, img_list))

if aa:=st.text_input('Enter Article'):
    for i, j in dict1.items():
        if aa in i:
            st.image(dict1[i])
            break
    else:
        st.write("다시")