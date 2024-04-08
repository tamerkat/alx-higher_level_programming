#!/usr/bin/node
const ar = process.argv[2];

if (isNaN(ar)) {
  console.log('Missing size');
}

for (let i = 0; i < ar; i++) {
  for (let j = 0; j < i; j++) {
    console.log('x');
  }
}
