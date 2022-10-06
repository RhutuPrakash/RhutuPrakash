import cv2

# content of test_tmp_path.py
CONTENT = "content"

def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
#    assert 0

def load_image(image):
    return cv2.imread("ss.png",0)

# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    #img = img.flatten()
    cv2.imshow("dummy", img)