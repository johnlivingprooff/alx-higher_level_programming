#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      const complete = todo.completed;
      if (complete) {
        completedTasks[todo.userId] = completedTasks[todo.userId] ? completedTasks[todo.userId] + 1 : 1;
      }
    });
    console.log(completedTasks);
  }
});
