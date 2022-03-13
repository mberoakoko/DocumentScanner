from abc import ABC, abstractmethod
import numpy as np
import cv2 as cv
from skimage.filters import (threshold_otsu, threshold_sauvola)
from skimage import color
from skimage import io
from skimage import exposure
def loadImage(path: str):
	return io.imread(path, as_gray=False)


class BaseScanner(ABC):
	@abstractmethod
	def scan(self) -> np.ndarray:
		pass


class Scanner(BaseScanner, ABC):

	def __init__(self, image: np.ndarray):
		self.image = color.rgb2gray(image)
		self.image = exposure.equalize_adapthist(self.image, clip_limit=0.03)

	@staticmethod
	def _threshold_Image(image: np.ndarray) -> np.ndarray:
		thresh = threshold_sauvola(image)
		return image > thresh

	def scan(self):
		img = Scanner._threshold_Image(self.image)
		return img