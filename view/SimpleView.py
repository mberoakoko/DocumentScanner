import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np
from typing import Tuple, List

def showImage(image: np.ndarray, fig_size: Tuple[int, int]=(10, 10), is_gray: bool=False):
	plt.figure(figsize=fig_size)
	plt.imshow(image) if is_gray else plt.imshow(image, cmap="gray")
	plt.axis("off")
	plt.show()

def showSideBySide(images: List[np.ndarray], fig_size: Tuple[int, int] = (10, 10), is_gray: bool = False):
	if len(images) > 2:
		raise Exception("Can only compare two images")

	fig: Figure = plt.figure(figsize=fig_size)
	for i, image in enumerate(images, start=1):
		ax: Axes = fig.add_subplot(1, 2, i)
		ax.imshow(image) if is_gray else ax.imshow(image, cmap="gray")
		ax.axis("off")

	plt.tight_layout()
	plt.show()