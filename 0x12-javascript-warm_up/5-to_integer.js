#!/usr/bin/node

const val = process.argv[2];

if (typeof val === 'string') {
  console.log(`My number: ${parseInt(val)}`);
} else {
  console.log(`My number: ${val}`);
}
