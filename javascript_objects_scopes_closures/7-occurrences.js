#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  return list.filter((x) => x === searchElement).length
};

