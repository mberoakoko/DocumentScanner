from model.scan import Scanner, loadImage
from view.SimpleView import showImage, showSideBySide
from pathlib import Path

test_image = loadImage("D:\\Python Projects\\DocumentScanner\\data\\testImages\\random_image.jpeg")

def displayRawImage():
	showImage(image=test_image)

def scanImage():
	scanner = Scanner(test_image)
	scanned_image = scanner.scan()
	showImage(scanned_image)
	showSideBySide([test_image, scanned_image])

