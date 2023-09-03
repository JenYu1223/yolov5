import streamlit as st
import paramiko  # 用於 SSH 連接
import time
import os
from PIL import Image
from image_crop import image_crop
from detect_bug import parse_opt, main

# SSH
ssh_host = '140.112.183.111'
ssh_port = 22
ssh_username = 'jenyu'
ssh_password = 'Cibillab105'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ssh_host, ssh_port, ssh_username, ssh_password)

# st.title("牛埔頭黏蟲紙拍攝")
st.markdown('<div style="text-align:center;"><h1>牛埔頭黏蟲紙拍攝</h1></div>',
            unsafe_allow_html=True)
#tab1, tab2 = st.tabs(["五區黏蟲紙", "黏蟲紙辨識"])
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    ["右上區黏蟲紙", "右下區黏蟲紙", "正中間黏蟲紙", "左上區黏蟲紙", "左下區黏蟲紙", "蟲紙數量辨識"])

with tab1:
    image1 = Image.open(
        './upload_images_website/29032450.jpg')
    st.image(image1)
    st.markdown("<h2 style='text-align: center;'>區域：右上</h2>", unsafe_allow_html=True)
    # image2 = Image.open(
    #     'D:/line_bot/upload_images/20230825_14-05-18.jpg')
    # image3 = Image.open(
    #     'D:/line_bot/upload_images/20230825_14-05-18.jpg')
    # image4 = Image.open(
    #     'D:/line_bot/upload_images/20230825_14-05-18.jpg')
    # image5 = Image.open(
    #     'D:/line_bot/upload_images/20230825_14-05-18.jpg')

    # # 子標題
    # image_titles = ["右上", "右下", "左上", "左下", "正中間"]

    # # 分割頁面為兩行兩列的格局
    # col1, col2, col3, col4, col5 = st.columns([2, 1, 2, 1, 2])

    # # 在每個格子中放置圖片和對應標題
    # with col1:
    #     st.image(image3, caption=image_titles[2], width=300)
    #     st.image(image4, caption=image_titles[3], width=300)

    # with col3:
    #     st.image(image5, caption=image_titles[4], width=300)

    # with col5:
    #     st.image(image1, caption=image_titles[0], width=300)
    #     st.image(image2, caption=image_titles[1], width=300)

with tab2:
    image2 = Image.open(
        './upload_images_website/29032450.jpg')
    st.image(image2)
    st.markdown("<h2 style='text-align: center;'>區域：右下</h2>", unsafe_allow_html=True)
with tab3:
    image3 = Image.open(
        './upload_images_website/29032450.jpg')
    st.image(image3)
    st.markdown("<h2 style='text-align: center;'>區域：正中間</h2>", unsafe_allow_html=True)
with tab4:
    image4 = Image.open(
        './upload_images_website/29032450.jpg')
    st.image(image4)
    st.markdown("<h2 style='text-align: center;'>區域：左上</h2>", unsafe_allow_html=True)
with tab5:
    image5 = Image.open(
        './upload_images_website/29032450.jpg')
    st.image(image5)
    st.markdown("<h2 style='text-align: center;'>區域：左下</h2>", unsafe_allow_html=True)
with tab6:
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        upload_image = uploaded_file.getvalue()
        st.image(upload_image)

        current_time = time.strftime('%Y%m%d_%H%M%S')
        # 圖片的儲存路徑
        image_save_path = f'./upload_images_website/{current_time}.png'
        with open(image_save_path, 'wb') as f:
            f.write(upload_image)
        st.success("Image saved successfully! Please wait for detection ...")

        # original_image = Image.open(image_save_path)
        # desired_resolution = (3280, 2464)  # (3280, 2464)
        # original_image = original_image.resize(desired_resolution, Image.ANTIALIAS)
        # original_image.save(image_save_path)

        # 圖片預處理，先切成 4x4 16張子圖
        image_crop()

        # 執行圖片辨識，detect_bug.py
        # 修改 opt 權重檔 --weights maybe.pt --conf 0.5 -- source D:\line_bot\crop_images
        opt = parse_opt()
        main(opt)

        # 讓 16 張圖片各別的標註數量加總並呈現
        with open('./output.txt', 'r') as f:
            content = f.read()  # 讀取整個檔案內容
            values = content.split()  # 分割內容成數值串列

        # 將字串數值轉換為整數
        class0 = int(values[0])  # 白粉蝨
        class1 = int(values[1])  # 黑粉蝨
        class2 = int(values[2])  # 薊馬
        reply = "白粉蝨：" + str(class0) + " , 久置轉黑：" + str(class1) + ", 薊馬：" + str(class2)
        st.write(reply)
