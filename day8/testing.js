const arr = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]

function addSolution(newSolution) {
	if (newSolution.length !== 3) return
	newSolution.sort()
	isDuplicate = solutions.every(solution => {
		if (!solution) return true
		return !solution.every((value, index) => value === newSolution[index])
	})
	if (isDuplicate) solutions.push(newSolution)
}

function twoSum(nums, target) {
	let solution = []
	nums.find((integer) => {
		const expectedValue = target - integer
		if (hash[integer] < 1) return
		hash[integer] -= 1
		if (hash[expectedValue] && hash[expectedValue] > 0) {
			solution.push([integer, expectedValue])
		}
		hash[integer] += 1
	})
	console.log(solution)
	return solution || []
}


const solutions = []
const hash = {}
// Populate hash table. If hash[value] is undefined, defaults to 1, else, increment
arr.forEach((value) => hash[value] = hash[value] + 1 || 1)

for (i in arr) {
	const difference = 0 - arr[i]
	hash[arr[i]] -= 1
	// TODO: Change the arr back to num btw
	let x = twoSum(arr, difference)
	x && x.forEach((solution) => addSolution([arr[i], ...solution]))
	hash[arr[i]] -= 1
}
console.log(solutions)
