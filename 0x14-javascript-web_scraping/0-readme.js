#!/usr/bin/node

const fs = require('fs');
const path = argv[1];

fs.readFile(path, 'utf-8', (err, data) => {
    if (err)
        console.error(err);
    else 
        console.log(data);
});
