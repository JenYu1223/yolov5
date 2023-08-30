import cv2
import os
import glob


def image_crop():

    output_folder = 'D:/line_bot/crop_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        # 如果資料夾存在，則清空資料夾內容
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # 取得資料夾中所有圖片檔案的清單
    upload_images_path = "D:/line_bot/upload_images"
    # image_files = glob.glob(os.path.join(upload_images_path, "*.jpg"))  # 可以適當地更改副檔名
    image_files = glob.glob(os.path.join(upload_images_path, "*.png"))  # 可以適當地更改副檔名

    # 如果有找到圖片檔案
    if image_files:
        image_files.sort(key=os.path.getmtime)  # 根據檔案的修改時間排序清單（最新的在最後）
        latest_image_path = image_files[-1]  # 取得最新的圖片檔案路徑
        print("最新的圖片檔案:", latest_image_path)
    else:
        print("找不到圖片檔案")

    # 讀取最新的圖片
    image = cv2.imread(latest_image_path)
    #image = cv2.resize(image, (3280, 2464))

    # 計算小圖片的寬度和高度
    num_rows = 4
    num_cols = 4
    height, width, _ = image.shape
    small_height = height // num_rows
    small_width = width // num_cols

    # 初始化小圖片的起始座標
    y_coord = 0
    for row in range(num_rows):
        x_coord = 0
        for col in range(num_cols):
            # 裁切小圖片
            small_image = image[y_coord:y_coord +
                                small_height, x_coord:x_coord + small_width]

            # 儲存或處理小圖片
            #small_image_filename = os.path.join(output_folder, f'crop_image_{row}_{col}.jpg')
            small_image_filename = os.path.join(output_folder, f'crop_image_{row}_{col}.png')
            cv2.imwrite(small_image_filename, small_image)

            # 更新 x 座標
            x_coord += small_width
        # 更新 y 座標
        y_coord += small_height


if __name__ == "__main__":
    image_crop()
