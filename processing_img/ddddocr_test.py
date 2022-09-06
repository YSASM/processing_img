import ddddocr

def recognize():
    ocr = ddddocr.DdddOcr()
    with open('image_store/3_img_1662457761.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)
recognize()
