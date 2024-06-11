import streamlit as st
st.title("尚硅谷，学好前端很简单!")
st.header("尚硅谷前端学习教程")
st.subheader(" Visual Studio Code")
st.text("60天速成")

st.markdown("this is an image: \n \
            ![](http://www.atguigu.com/web/img/banner-wz.png)")

if st.checkbox("Show/Hide"):
    st.text("You checked the box")


status = st.radio("select gender:" ,
                  ('Male',
                   'Female'))
if status == 'Male':
    st.success("Male")
else:
    st.success("Female")

frontend_topics = st.multiselect("Select frontend topics you are interested in:",
               ['HTML', 'CSS', 'JavaScript', 'React', 'Vue', 'Angular'])
if frontend_topics:
    st.write("You selected these frontend topics:", frontend_topics)

occupation = st.multiselect("Select your occupation:", ['Teacher', 'Student', 'Professional'])
if occupation:
    st.write("You selected these occupations:", occupation)


if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write("Hello, ", name)

level = st.slider("Select your level", 1, 5)
st.write("You selected: ", level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                               type=['jpg',
                                      'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256), 
             caption="Uploaded Image")

    