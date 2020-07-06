let arr = [
	[0, 0, 1, 0, 0, 0, 1, 0],
	[0, 0, 1, 0, 1, 0, 1, 0],
	[0, 0, 1, 1, 1, 1, 1, 0],
	[0, 0, 0, 1, 1, 1, 0, 0],
	[0, 1, 0, 0, 1, 0, 0, 0],
	[0, 1, 0, 0, 1, 0, 1, 0],
	[0, 1, 0, 0, 1, 1, 1, 0],
	[0, 1, 0, 0, 0, 1, 0, 0],
	[0, 1, 0, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 0, 0],
	[0, 0, 1, 1, 1, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 1, 0],
	[0, 1, 0, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 0, 0, 1, 0],
	[0, 0, 1, 0, 0, 0, 1, 0]
];

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

const y = [];

const searchForArray = (array, N) => {
	let icell = arrayToInt(array)
	let index = y.findIndex((cell) => cell === icell)
	if (index === -1) {
		y.push(icell);
		return
	}

	let newIndex = y.push(icell) - 1;
	//console.log(index, newIndex)
	console.log((N - index) % newIndex)
	return intToArray(y[index])
}

arr.forEach((x) => {
	let found = searchForArray(x, 27)
	if (!found) return
	//console.log(found)
})
