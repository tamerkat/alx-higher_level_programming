#!/usr/bin/node

exports.converter = function (base) {
  function convert (m) {
    return m.tostring(base);
  }
  return convert;
};
