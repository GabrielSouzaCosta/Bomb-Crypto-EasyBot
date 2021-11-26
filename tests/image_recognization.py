import cv2 as cv
import numpy as np

print(cv.__version__)

bomb_img = cv.imread('bomb.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('images/wallet.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(bomb_img, needle_img, cv.TM_CCOEFF_NORMED)

# cv.imshow('Result', result)
# cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
print(f"Match position {max_loc}")
print(f'Best match confidence: {max_val}')

threshold = 0.8
if max_val >= threshold:
    print('Found needle')
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(bomb_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    # cv.imshow('result', bomb_img)
    # cv.waitKey()
    cv.imwrite('result.png', bomb_img)

else:
    print('needle not found')

def main():
    pass