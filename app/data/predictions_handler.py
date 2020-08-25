import os
from PIL import Image


def get_prediction(model_input):
    model_output = model_input * 2
    return model_output


if __name__ == "__main__":
    test_input = input("is this a test? y/n ")
    if str(test_input) == "y":
        with os.scandir('data/test_imgs') as images:
            for image in images:
                image_pil = Image.open(f"data/test_imgs/{image.name}")
                # 1. load up test_imgs directory with images
                # 2. uncomment prediction lines below once everything is set up to test
                # --->
                # prediction = get_prediction(image_pil)
                # print(prediction)
    print("done")
