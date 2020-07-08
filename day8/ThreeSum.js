/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
	solutions = []
	const hash = {}
	// Populate hash table. If hash[value] is undefined, defaults to 1, else, increment
	nums.forEach((value) => hash[value] = hash[value] + 1 || 1)

	const twoSum = function(nums, target) {
		nums.find((integer, index) => {
			const expectedValue = target - integer
			// 
			hash[integer] -= 1
			if (hash[expectedValue] && hash[expectedValue] > 0) {
				let expectedIndex = nums.findIndex((value, i) => {
					if (i === index) return false
					return value === expectedValue
				})
				solution = [index, expectedIndex]
				return solution
			}
			hash[integer] += 1
		})
		return solution || []
	};
};