import streamlit as st
st.title("今天晚饭吃什么!")
st.header("我好想吃晚饭")
st.subheader(" 饿死啦")
st.text("怎么还不下课")

st.markdown("this is an image: \n \
            ![](https://upload.shejihz.com/2020/02/881308c347f4fe6175b6c2ef6d32ad8d.jpg)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

food_wishlist = ["宫保鸡丁", "鱼香肉丝", "红烧茄子", "红烧肉"]
st.write("想吃的食物：", ", ".join(food_wishlist))

if st.button("about"):
    st.text("Streamlit is a great tool")

# 用户输入姓名
name = st.text_input("请输入你的名字:")
if st.button("提交"):
    st.write("你好, ", name)

# 吃饭地点选择
dining_hall = st.selectbox("选择去哪吃饭:", 
                           ["一食堂", "二食堂", "风味食廊"])
st.write("你选择了: ", dining_hall)

# 吃饭幸福度滑块
happiness_level = st.slider("选择你的吃饭幸福度", 1, 5)
st.write("你的吃饭幸福度是: ", happiness_level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    