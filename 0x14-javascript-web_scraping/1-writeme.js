#!/usr/bin/node
/*script that display the status code of a GET request.*/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
