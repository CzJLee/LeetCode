class Solution:
	# We want O(log (m+n)) time complexity
	# The lists are sorted
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		# Try a fast insertion and then pick median

		merged_list = self.insertion(nums1, nums2)
		if len(merged_list) % 2 == 1:
			# List has odd num values
			med_index = int(len(merged_list) / 2)
			return merged_list[med_index]
		else:
			# List has even num values
			med_index = int(len(merged_list) / 2)
			avg_med = (merged_list[med_index] + merged_list[med_index - 1]) / 2
			return avg_med

	def insertion(self, list_1, list_2):
		# O(n)
		merged_list = []

		while list_1 or list_2:
			if len(list_1) == 0:
				# List is empty
				merged_list.extend(list_2)
				break
			elif len(list_2) == 0:
				merged_list.extend(list_1)
				break

			if list_1[0] <= list_2[0]:
				merged_list.append(list_1.pop(0))
			else:
				merged_list.append(list_2.pop(0))
		
		return merged_list




