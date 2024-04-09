#!/usr/bin/node

let called = -1;
exports.logMe = function (item) {
  called++;
  console.log(called + ': ' + item);
};
