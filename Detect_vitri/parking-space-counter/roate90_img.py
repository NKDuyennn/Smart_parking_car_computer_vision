from PIL import Image

# Đường dẫn đến ảnh
path_to_image = "Detect_vitri\\parking-space-counter\\mask_hust_c7.png"

# Đọc ảnh
image = Image.open(path_to_image)

# Xoay ảnh 90 độ theo chiều kim đồng hồ
rotated_image = image.rotate(-90, expand=True)

# Lưu ảnh đã xoay vào tệp mới
output_path = "mask_hust_c7.png"
rotated_image.save(output_path)