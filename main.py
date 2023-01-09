import streamlit as st
#import numpy as np
#import pandas as pd 
#from PIL import Image
import time


st.title ('Streamlit入門')

st.write('Interactive Widgets')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'DONE!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#name = st.text_input('あなたの趣味を教えてください')
#st.write(name)

#text = st.slider('あなたの調子は？', 0, 10, 5)
#'コンディション:', text

#if st.checkbox('Show Image'):
#    img = Image.open('スクリーンショット 2021-08-02 18.43.50.png')
#    st.image(img, caption='Kohei Imanishi', use_column_width=True)


#動的な表の表示
#st.dataframe(df.style.highlight_max(axis=1))
#静的な表の表示
#st.table(df.style.highlight_max(axis=1))


#"""
## 章
### 節
#### 項
#
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd 
#```
#"""