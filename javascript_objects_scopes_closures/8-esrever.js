#!/usr/bin/node

exports.esrever = function (list) {
  // Initialize pointers for the start and end of the list
  let start = 0;
  let end = list.length - 1;

  // Iterate until start pointer is less than end pointer
  while (start < end) {
    // Swap elements at start and end positions
    const temp = list[start];
    list[start] = list[end];
    list[end] = temp;

    // Move start pointer forward and end pointer backward
    start++;
    end--;
  }

  // Return the reversed list
  return list;
};
