import cv2
import pickle
import numpy as np
from PIL import Image, ImageDraw, ImageFont

width, height = 107, 48

try:
    font_title = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 16)
    font_stat = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 13)
    font_badge = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 11)
    HAS_PIL_FONTS = True
except Exception:
    HAS_PIL_FONTS = False

cap = cv2.VideoCapture('carPark.mp4')

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except (FileNotFoundError, EOFError):
    posList = []

def process_frame(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    return cv2.dilate(imgMedian, kernel, iterations=1)

def draw_modern_ui(img, imgDilate):
    overlay = img.copy()
    free_count = 0
    occupied_count = 0

    for pos in posList:
        x, y = pos
        imgCrop = imgDilate[y:y+height, x:x+width]
        count = cv2.countNonZero(imgCrop)

        if count < 800:
            free_count += 1
            cv2.rectangle(overlay, (x, y), (x + width, y + height), (46, 204, 113), -1)
            cv2.rectangle(img, (x, y), (x + width, y + height), (46, 204, 113), 2)
        else:
            occupied_count += 1
            cv2.rectangle(overlay, (x, y), (x + width, y + height), (60, 64, 235), -1)
            cv2.rectangle(img, (x, y), (x + width, y + height), (60, 64, 235), 2)

    alpha = 0.28
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    if HAS_PIL_FONTS:
        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil, 'RGBA')

        hud_x = 20
        hud_y = 10
        hud_w = 720
        hud_h = 58

        draw.rounded_rectangle([hud_x, hud_y, hud_x + hud_w, hud_y + hud_h],
                               radius=14, fill=(15, 23, 42, 240), outline=(255, 255, 255, 60), width=1)

        draw.text((hud_x + 16, hud_y + 11), 'PARKING VISION AI', font=font_title, fill=(255, 255, 255, 255))
        draw.ellipse([hud_x + 16, hud_y + 36, hud_x + 24, hud_y + 44], fill=(46, 204, 113, 255))
        draw.text((hud_x + 28, hud_y + 33), 'REAL-TIME MONITORING', font=font_badge, fill=(46, 204, 113, 255))

        total_spaces = len(posList)
        occupancy_rate = int((occupied_count / total_spaces) * 100) if total_spaces > 0 else 0

        draw.ellipse([hud_x + 230, hud_y + 16, hud_x + 242, hud_y + 28], fill=(46, 204, 113, 255))
        draw.text((hud_x + 248, hud_y + 13), f'LIVRES: {free_count}/{total_spaces}', font=font_stat, fill=(240, 240, 240, 255))

        draw.ellipse([hud_x + 365, hud_y + 16, hud_x + 377, hud_y + 28], fill=(235, 64, 60, 255))
        draw.text((hud_x + 383, hud_y + 13), f'OCUPADAS: {occupied_count}/{total_spaces}', font=font_stat, fill=(240, 240, 240, 255))

        draw.ellipse([hud_x + 535, hud_y + 16, hud_x + 547, hud_y + 28], fill=(59, 130, 246, 255))
        draw.text((hud_x + 553, hud_y + 13), f'TAXA: {occupancy_rate}%', font=font_stat, fill=(240, 240, 240, 255))

        pb_x, pb_y, pb_w, pb_h = hud_x + 230, hud_y + 38, 465, 8
        draw.rounded_rectangle([pb_x, pb_y, pb_x + pb_w, pb_y + pb_h], radius=4, fill=(40, 50, 65, 255))
        fill_w = int(pb_w * (occupied_count / total_spaces))
        if fill_w > 0:
            draw.rounded_rectangle([pb_x, pb_y, pb_x + fill_w, pb_y + pb_h], radius=4, fill=(235, 64, 60, 255))

        for pos in posList:
            x, y = pos
            imgCrop = imgDilate[y:y+height, x:x+width]
            count = cv2.countNonZero(imgCrop)
            is_free = count < 800

            bg_color = (46, 204, 113, 230) if is_free else (235, 64, 60, 230)
            text_str = 'LIVRE' if is_free else 'OCUPADO'

            bw, bh = 54, 16
            bx, by = x + width - bw - 4, y + height - bh - 4
            draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4, fill=bg_color)

            tx = bx + 11 if is_free else bx + 3
            draw.text((tx, by + 1), text_str, font=font_badge, fill=(255, 255, 255, 255))

        img = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return img

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    if not success:
        break

    imgDilate = process_frame(img)
    img = draw_modern_ui(img, imgDilate)

    cv2.imshow("Parking Vision AI", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()