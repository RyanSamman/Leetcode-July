/**
 * @param {number[]} cells
 * @param {number} N
 * @return {number[]}
 */
var prisonAfterNDays = function(cells, N) {
	const y = []
	const z = []

	const searchForArray = (array, N) => {
		z.push(array)
		let icell = arrayToInt(array)
		let index = y.findIndex((cell) => cell === icell)
		if (index === -1) {
			y.push(icell);
			return
		}
		let newIndex = y.push(icell) - 1;
		console.log(index, newIndex, '<-')
		console.log(((N - index) % newIndex) - 1)
		let foundIndex = ((N - index) % newIndex) - 1
		if (foundIndex < 0) return newIndex - index + foundIndex
		return foundIndex
	}

	const arrayToInt = (array) => {
		//console.log(array)
		let bin = 0
		array.forEach((cell, index) => {
			bin += cell * (10 ** (7 - index))
		})
		let i = parseInt(bin, 2)
		//console.log(intToArray(parseInt(bin, 2)))
		return i
	}

	const intToArray = i => {
		let newArray = i.toString(2).split('').map((cell) => parseInt(cell, 10))
		while (newArray.length < 8) {
			newArray.unshift(0)
		}
		return newArray	
	}

	const newState = (arr, i) => {
		//          000 001 010 100 
		//          000 001 010 011 100 101 110 111
		let state = [1,  0,  1,  0,  0,  1,  0,  1];
		let stateIndex = parseInt(100 * arr[i - 1] + 10 * arr[i] + arr[i + 1], 2);
		//console.log(arr[i - 1], arr[i], arr[i + 1],':', state[stateIndex], stateIndex);
		return state[stateIndex];
	}

	for (let i = 0; i < N; i++) {
		cells = cells.map((_cell, index, array) => {
			if (index === 0 || index === 7) return 0;
			let newCell = newState(array, index);
			return newCell;
		});

		console.log(JSON.stringify(cells), i)

		let found = searchForArray(cells, N)

		if (found === -1) continue

		if (found != undefined) {
			console.log(JSON.stringify(z[found])), found;
			console.log('^')
			return z[found];
		}
	}

	return cells;
}

let arr = [0,0,0,1,1,0,1,0];
// [0,0,0,1,1,0,1,0]
console.log(JSON.stringify(prisonAfterNDays(arr, 574)))