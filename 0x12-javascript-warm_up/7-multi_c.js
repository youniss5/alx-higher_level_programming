#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let y = 0;
  while (y < x) {
    console.log('C is fun');
    y++;
  }
}
