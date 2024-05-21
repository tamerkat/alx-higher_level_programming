#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, {method: 'GET'}, (err, response) => {
    if (err) {
        return console.error(err);
    } else {
        console.log(`code: ${response}`);
    }
});
