#!/usr/bin/node
const ar = process.argv[2];

if (isNaN(ar)) {
  console.log('Missing size');
}

for (let i = 0; i < ar; i++) {
  console.log('x' * ar);
}
