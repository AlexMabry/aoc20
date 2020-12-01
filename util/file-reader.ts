import fs from "fs";

export function readFile(path: string) {
  const lines = fs.readFileSync(path, "utf8");

  // split the contents by new line
  return lines.split(/\r?\n/);
}
