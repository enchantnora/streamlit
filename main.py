import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

# streamlit run main.py

st.title('Streamlit')

st.write('Display')
if st.checkbox('Show Pickey'):
    img= Image.open('Pickey.png')
    st.image(img, caption='Pickey', width=img.width)

st.write('プログレスバー')
latest_iteration= st.empty()
bar= st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteration {1+i}')
    bar.progress(i+1)
    time.sleep(0.01)

l_column, r_column = st.beta_columns(2)
button= l_column.button('押す？')
if button:
    r_column.write('押したね！')

expander= st.beta_expander('見て')
expander.write('見た！')

option= st.sidebar.selectbox(
    '選べ',
    list(range(1, 11))
)
'選んだ数字は', option, 'ですね！'

text= st.sidebar.text_input('何が好き？')
text, 'が好き！'

condition= st.sidebar.slider('調子はどう？',0 ,100, 50)
'コンディションは', condition, '％くらいですね。'

st.write('DataFrame')
df= pd.DataFrame({
    '１列目': [1, 2, 3, 4],
    '２列目': [50, 60, 70, 80]
})
st.dataframe(df.style.highlight_max(axis=0))

'''
## Python
```python
import numpy as np
import pandas as pd
```
'''

df2= pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3= pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)