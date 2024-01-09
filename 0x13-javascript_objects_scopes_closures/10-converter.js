#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    if (number > 0) {
      exports.converter(Math.floor(number / base));
      return (String((number % base)).toString());
    }
  };
};
