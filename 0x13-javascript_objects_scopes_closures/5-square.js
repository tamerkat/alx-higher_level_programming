#!/usr/bin/node
const Rectangle = require('./rectangle.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
