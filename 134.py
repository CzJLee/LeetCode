# https://leetcode.com/problems/gas-station/
import numpy as np

class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		gas = np.array(gas)
		cost = np.array(cost)
		diff = gas - cost
		n = len(diff)

		if np.sum(diff) < 0:
			# Guaranteed to not have enough gas
			return -1
		else:
			# Guaranteed to have enough, just need to find start
			check = 0
			while check < n:
				circuit = np.hstack((diff[check:], diff[:check]))
				tank = 0
				for i, x in enumerate(circuit):
					tank += x
					if tank < 0:
						check += i + 1
						break
					elif i == n - 1:
						return check
