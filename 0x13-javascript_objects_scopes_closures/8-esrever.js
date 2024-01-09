#!/usr/bin/node
exports.esrever = function (list) {
  const temp = [];
  for (let i = 0, j = list.length - 1; i < list.length; i++, j--) {
    temp[i] = list[j];
  }
  return temp;
};
