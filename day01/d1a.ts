import { readFile } from "../util";

const nums = readFile("./day01/d1in.txt").map(line => parseInt(line));
const numSet = new Set(nums);

for (const n of numSet) {
  const diff = 2020 - n;

  if (numSet.has(diff)) {
    console.log(diff * n);
    break;
  }
}
