import cv2

# Đường dẫn đến video
path_to_video = "Detect_vitri\\parking-space-counter\\hust_c7.mp4"

# Tạo đối tượng VideoCapture
video_capture = cv2.VideoCapture(path_to_video)

# Đọc thông tin về kích thước video
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Tạo đối tượng VideoWriter để ghi video đầu ra với kích thước đã thay đổi
output_path = "hust_c7.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter(output_path, fourcc, 30.0, (height, width))

# Đọc từng khung hình trong video và xoay 90 độ, thay đổi kích thước
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Xoay và thay đổi kích thước khung hình 90 độ
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    resized_frame = cv2.resize(rotated_frame, (height, width))

    # Ghi khung hình đã xoay và thay đổi kích thước vào video đầu ra
    output_video.write(resized_frame)

# Giải phóng tài nguyên
video_capture.release()
output_video.release()