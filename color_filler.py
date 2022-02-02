import cv2
from PIL import Image
import numpy as np

bg_color_list = [(9, 50, 239), (22, 30, 100), (28, 28, 183), (79, 14, 136), (140, 20, 74), (146, 27, 49), (32, 94, 27),
                 (126, 35, 26), (123, 137, 0), (0, 84, 211), (141, 97, 31)]

width = 1920 * 2
height = 1080 * 2
image = np.zeros((height, width, 3), np.uint8)


def writing_number(text):
    if text == ".":
        bg_color = bg_color_list[10]
    else:
        bg_color = bg_color_list[int(text)]

    # Fill image with color
    image[:] = bg_color
    h, w, c = image.shape
    thickness = 15
    cv2.putText(image, str(text), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, thickness, (255, 255, 255), 4)
    cv2.namedWindow("test",cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("test",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("test", image)
    if cv2.waitKey(100) & 0xff == ord('q'):
        cv2.destroyAllWindows()
        return "b"
