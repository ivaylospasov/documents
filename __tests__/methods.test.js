import trimmer from "../src/methods/trimmer";
import removeSymbols from "../src/methods/removeSymbols";

test("Trimmer trims strings", () => {
  expect(trimmer(`             Hello World!`)).toBe(`Hello World!`);
});

test("removeSymbols removes ¤", () => {
  expect(removeSymbols(`¤World!`)).toBe(`World!`);
});

test("removeSymbols removes the whole ¤W when it's in the beginning of the word", () => {
  expect(removeSymbols(`¤World!`)).toBe(`orld!`);
});

test("removeSymbols removes {M} when it's in the beginning of the word", () => {
  expect(removeSymbols(`{M}y World!`)).toBe(`y World!`);
});
