# https://leetcode.com/problems/richest-customer-wealth/
import numpy as np
class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		accounts = np.array(accounts)
		accounts = np.sum(accounts, axis=1)
		return np.max(accounts)