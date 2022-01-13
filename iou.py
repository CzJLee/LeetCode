# In some machine learning and computer vision applications, it is useful to find the Intersection Over Union (IOU). 
# Implement the intersection over union of two bounding boxes. 
# Consider an image, and a machine learning program outputs the coordinates of bounding boxes within the image. 
# We want to find the ratio of the two bounding boxes intersected area vs union area. 
# Each bounding box has the format roi = [(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)] describing the coordinates of the top left corner and bottom right corner. 
# ROI stands for "Region of Interest"
# For images, the origin (0, 0) is the top left corner, and the positive x-axis is to the right, and the positive y-axis is down. 
# 
# |---------------|
# |               |
# |      |---------------|
# |      |        |      |
# |---------------|      |
#        |               |
#        |---------------|

def iou(roi1, roi2):
	"""
	Calculate the ratio of intersection area over union area

	Args:
		roi1 (list): ROI 1 Coordinates [(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)]
		roi2 (list): ROI 2 Coordinates [(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)]

	Returns:
		float: Intersecton over union ratio
	"""
	
	# Your Code Here
	





if __name__ == "__main__":
	# Case: 1
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 2], [6, 6]]
	assert round(iou(roi1, roi2), 2) == round(0.1428, 2), "Test Case 1 Failed"

	# Case: 2
	roi1 = [[0, 0], [1, 1]]
	roi2 = [[2, 2], [10, 10]]
	assert round(iou(roi1, roi2), 2) == round(0, 2), "Test Case 2 Failed"

	# Case: 3
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 2], [4, 4]]
	assert round(iou(roi1, roi2), 2) == round(0.25, 2), "Test Case 3 Failed"

	# Case: 4
	roi1 = [[1, 2], [4, 4]]
	roi2 = [[1, 2], [4, 4]]
	assert round(iou(roi1, roi2), 2) == round(1.0, 2), "Test Case 4 Failed"

	# Case: 5
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 0], [6, 4]]
	assert round(iou(roi1, roi2), 2) == round(0.333, 2), "Test Case 5 Failed"

	# Case: 6
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[4, 0], [6, 4]]
	assert round(iou(roi1, roi2), 2) == round(0, 2), "Test Case 6 Failed"

	print("All Test Cases Passed.")