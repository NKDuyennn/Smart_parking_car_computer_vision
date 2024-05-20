import os
import cv2
import matplotlib.pyplot as plt

output_dir = 'C:\\Users\\Admin\\Documents\\GitHub\\Smart_parking_car_computer_vision\\Detect_vitri\\parking-space-counter\\data\\all'
mask_path = 'Detect_vitri\\parking-space-counter\\mask_hust_c7.png'
original_image_path = 'Detect_vitri\\parking-space-counter\\original.jpg'

mask = cv2.imread(mask_path, 0)
original_image = cv2.imread(original_image_path)

analysis = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
(totalLabels, label_ids, values, centroid) = analysis

slots = []
for i in range(1, totalLabels):
    # Area of the component
    area = values[i, cv2.CC_STAT_AREA]

    # Now extract the coordinate points
    x1 = values[i, cv2.CC_STAT_LEFT]
    y1 = values[i, cv2.CC_STAT_TOP]
    w = values[i, cv2.CC_STAT_WIDTH]
    h = values[i, cv2.CC_STAT_HEIGHT]

    # Coordinate of the bounding box
    pt1 = (x1, y1)
    pt2 = (x1 + w, y1 + h)
    (X, Y) = centroid[i]

    slots.append([x1, y1, w, h])

# Save each slot as a separate image
for i, slot in enumerate(slots):
    slot_number = i + 1  # Slot number starts from 1
    x1, y1, w, h = slot

    # Crop the slot from the original image
    slot_image = original_image[y1:y1+h, x1:x1+w]

    # Save the slot image to the output directory
    slot_output_path = os.path.join(output_dir, f'slot_{slot_number}.jpg')
    cv2.imwrite(slot_output_path, slot_image)

    # Optionally, display the slot image
    plt.imshow(cv2.cvtColor(slot_image, cv2.COLOR_BGR2RGB))
    plt.show()