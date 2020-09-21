#!/usr/bin/node
exports.esrever = function (list) {
  const clone = [...list];
  let end = list.length - 1;
  for (let i = 0; i < list.length; i++, end--) {
    clone[i] = list[end];
  }

  return (clone);
};
