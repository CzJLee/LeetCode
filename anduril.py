# In some machine learning and computer vision applications, it is useful to find the Intersection Over Union (IOU). 
# Implement the intersection over union of two bounding boxes. 
# Consider an image, and a machine learning program outputs the coordinates of bounding boxes within the image. 
# We want to find the ratio of intersected area vs union area. 
# 
# |---------------|
# |               |
# |        --------------|
# |      |        |      |
# |---------------|      |
#        |               |
#        |---------------|

def iou(roi1, roi2):
	# Format for roi = [(top_left_x, top_left_y), (bottom_right_x, bottom_right_y)]
	# Find intersection as the mid points
	x_sorted = sorted([roi1[0][0], roi1[1][0], roi2[0][0], roi2[1][0]])
	y_sorted = sorted([roi1[0][1], roi1[1][1], roi2[0][1], roi2[1][1]])
	intersection_corners = [(x_sorted[1], y_sorted[1]), (x_sorted[2], y_sorted[2])] 

	# Check if no intersection
	# If midpoint of intersection is not in the roi, then no intersection
	midpoint_x = (intersection_corners[0][0] + intersection_corners[1][0]) / 2
	midpoint_y = (intersection_corners[0][1] + intersection_corners[1][1]) / 2
	if midpoint_x >= roi1[0][0] and midpoint_x <= roi1[1][0] and midpoint_y >= roi1[0][1] and midpoint_y <= roi1[1][1]:
		# Midpoint in the ROI, thus, intersection
		pass
	else:
		# No intersection
		return 0
	
	intersection_area = abs( (intersection_corners[1][0] - intersection_corners[0][0])*(intersection_corners[1][1] - intersection_corners[0][1]) )

	# Calculate union area
	area_1 = (roi1[1][0] - roi1[0][0])*(roi1[1][1] - roi1[0][1])
	area_2 = (roi2[1][0] - roi2[0][0])*(roi2[1][1] - roi2[0][1])
	
	union_area = area_1 + area_2 - intersection_area
	
	return intersection_area / union_area

if __name__ == "__main__":
	# Case: 1 intersection
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 2], [6, 6]]
	print(iou(roi1, roi2))

	# Case: No intersection
	roi1 = [[0, 0], [1, 1]]
	roi2 = [[2, 2], [10, 10]]
	print(iou(roi1, roi2))

	# Case: Full intersection
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 2], [4, 4]]
	print(iou(roi1, roi2))

	# Case: Overlap
	roi1 = [[1, 2], [4, 4]]
	roi2 = [[1, 2], [4, 4]]
	print(iou(roi1, roi2))

	# Case: 2 intersection
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[2, 0], [6, 4]]
	print(iou(roi1, roi2))

	# Case: Shared edge
	roi1 = [[0, 0], [4, 4]]
	roi2 = [[4, 0], [6, 4]]
	print(iou(roi1, roi2))