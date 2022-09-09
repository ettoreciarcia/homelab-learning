calculatedaybeetween2dates = (date1, date2) => {
  const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
  const firstDate = new Date(date1);
  const secondDate = new Date(date1);
  const diffDays = Math.round(Math.abs((firstDate - secondDate) / oneDay));
  return diffDays;
}

console.log(calculatedaybeetween2dates("1996-02-15","2022-08-23"))

// find element in array
findElementInArray = (arr, element) => {
  return arr.indexOf(element) > -1;
}

//create a random array of numbers
createRandomArray = (length) => {
  const arr = [];
  for (let i = 0; i < length; i++) {
    arr.push(Math.floor(Math.random() * length));
  }
  return arr;
}

vector = createRandomArray(10);

vector.forEach(element => {
  console.log(element);
}
);

console.log(vector);

//find odd number in array
findOddNumberInArray = (arr) => {
  const oddNumber = [];
  arr.forEach(element => {
    if (element % 2 !== 0) {
      oddNumber.push(element);
    }
  }
  );
  return oddNumber;
}

onlyodd = findOddNumberInArray(vector);

console.log(onlyodd);
