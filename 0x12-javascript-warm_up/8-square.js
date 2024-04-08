#!/usr/bin/node
const ar = Math.floor(+process.argv[2]);

if (isNaN(ar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < ar; i++) {
    console.log('x'.repeat(ar));
  }
}
