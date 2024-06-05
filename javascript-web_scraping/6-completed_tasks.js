#!/usr/bin/node

const request = require('request');

// Get the API URL from command-line arguments
const url = process.argv[2];

// Make a GET request to the API URL
request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status code:', response.statusCode);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    // Iterate through each todo item
    todos.forEach(todo => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 0;
        }
        completedTasksByUser[todo.userId]++;
      }
    });

    // Print users with completed tasks
    for (const userId in completedTasksByUser) {
      if (Object.prototype.hasOwnProperty.call(completedTasksByUser, userId)) {
        console.log(`'${userId}': ${completedTasksByUser[userId]}`);
      }
    }
  }
});
