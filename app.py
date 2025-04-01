import streamlit as st
import requests

st.title("Công cụ tạo nội dung mạng xã hội")

# Sidebar bên trái để upload và nhập thông tin
with st.sidebar:
    st.header("Upload dữ liệu")
    uploaded_files = st.file_uploader("Chọn ảnh hoặc video", accept_multiple_files=True, type=["jpg", "jpeg", "png", "mp4", "mov"])
    social_platform = st.text_input("Nền tảng mạng xã hội", "Tất cả")

# Bên phải: Các chức năng xử lý
st.header("Chức năng xử lý")

API_URL = "http://tekup.dongnamduocgl.com"

# Khu vực tạo tiêu đề
if st.button("Tạo tiêu đề"):
    if uploaded_files:
        files_data = [("files", file) for file in uploaded_files]
        data = {"social_media": social_platform}
        response = requests.post(f"{API_URL}/create-title", files=files_data, data=data)
        result = response.json()['title']
        st.text(f"Tiêu đề được tạo: {result}")
    else:
        st.warning("Vui lòng tải lên ít nhất một tệp.")

# Khu vực tinh chỉnh tiêu đề
title_input = st.text_input("Tiêu đề tinh chỉnh:", "")
if st.button("Tinh chỉnh tiêu đề"):
    if uploaded_files and title_input:
        files_data = [("files", file) for file in uploaded_files]
        data = {"social_media": social_platform, "title": title_input}
        response = requests.post(f"{API_URL}/create-title", files=files_data, data=data)
        result = response.json()['title']
        st.text(f"Tiêu đề tinh chỉnh: {result}")
    else:
        st.warning("Vui lòng tải lên tệp và nhập tiêu đề.")

# Khu vực tạo nội dung
content_input = st.text_input("Tiêu đề:", "")
if st.button("Tạo nội dung"):
    if uploaded_files:
        files_data = [("files", file) for file in uploaded_files]
        data = {"social_media": social_platform, "title": content_input}
        response = requests.post(f"{API_URL}/create-content", files=files_data, data=data)
        result = response.json()['content']
        st.text(f"Nội dung được tạo: {result}")
    else:
        st.warning("Vui lòng tải lên tệp.")
