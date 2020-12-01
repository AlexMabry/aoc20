import { readFile } from "../util";

const nums = readFile("./day01/d1in.txt").map(line => parseInt(line));
const numSet = new Set<number>(nums.filter(n => n));

function makePair(a: number, b: number): [number, number] {
  return [Math.min(a, b), Math.max(a, b)];
}

const pairs = nums.map(na => nums.map(nb => makePair(na, nb))).flat(1);
const pairSet = new Set<[number, number]>(pairs);

for (const [na, nb] of pairSet) {
  const nc = 2020 - (na + nb);

  if (numSet.has(nc)) {
    console.log(na * nb * nc);
    break;
  }
}
