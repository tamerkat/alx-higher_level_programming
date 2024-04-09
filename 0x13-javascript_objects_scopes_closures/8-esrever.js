#!/usr/bin/node

exports.esrever = function (list) {
  const copylist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    copylist.push(list[i]);
  }
  return copylist;
};
