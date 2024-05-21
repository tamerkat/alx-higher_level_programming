#!/usr/bin/node

const fs = require('fs');
const path = process.argv[1];
const contant = process.argv[2];

fs.writeFile(path, contant + "\n", 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
