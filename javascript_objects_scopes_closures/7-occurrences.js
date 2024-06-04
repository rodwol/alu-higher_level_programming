#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initialize a counter for the number of occurrences
  let count = 0;

  // Loop through each element in the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element matches the search element
    if (list[i] === searchElement) {
      // If it matches, increment the counter
      count++;
    }
  }
  return count;
};
