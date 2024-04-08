#!/usr/bin/node

const val = process.argv[2];

if (typeof val === 'string') {
  console.log(parseInt(val));
} else {
  console.log(val);
}
