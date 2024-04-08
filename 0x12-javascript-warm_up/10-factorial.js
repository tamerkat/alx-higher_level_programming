#!/usr/bin/node
if (!process.argv[2]) {
  console.log(1);
} else {
  function factorial (x) {
    for (let i = 0; i < x; i++) {
      console.log(x * (x - 1));
    }
  }
  const num = +process.argv[2];
  factorial(num);
}
