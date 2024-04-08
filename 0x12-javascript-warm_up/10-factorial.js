#!/usr/bin/node
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  }
  x = x * factorial(x - 1);
}
const num = +process.argv[2];
const result = factorial(num);
console.log(result);
