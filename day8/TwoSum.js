// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
	let solution = []
	const hash = {}
	// Populate hash table. If hash[value] is undefined, defaults to 1, else, increment
	nums.forEach((value) => hash[value] = hash[value] + 1 || 1)
	
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

console.log(twoSum([3, 3], 6))
