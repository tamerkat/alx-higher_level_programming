#!/usr/bin/node
const { argv } = require('node:process');

argv.forEach((val, index) => {
    console.log(`${index}: ${val}`);
});
if (argv.length = 1){
    console.log("No argument")
}else if (argv.length = 2){
    console.log("Argument found")
}else{
    console.log("Arguments found")
}
