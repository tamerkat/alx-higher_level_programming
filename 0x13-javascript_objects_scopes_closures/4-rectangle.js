#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w, h) {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate (w, h) {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double (w, h) {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
