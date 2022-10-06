import pytest
import cv2

def compute_expensive_image():
    img = cv2.imread('ss.png', cv2.IMREAD_GRAYSCALE)
    return img
#use same image file for multipurpose
@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    #img = compute_expensive_image()
    fn = tmp_path_factory.mktemp("data") / "ss.png"
    #cv2.imwrite("img.png", fn)
    #img.save(str(fn))
    return fn

