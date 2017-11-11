import serialize from "../methods/serialize";
import trimmer from "../methods/trimmer";
import removeSymbols from "../methods/removeSymbols";
import Save from "../dom/Save";

export default form => {
  // Get serialized (key-value) form data representation.
  const data = serialize(form);

  // Iterate through the form data to work with it
  for (const form in data) {
    // This is the field name, same as the id
    const input = data[0].name;

    // Initial value of the field value
    const text = data[0].value;
    // Remove unnecessary spaces.
    let correction = trimmer(text);
    // Remove unnecessary symbols.
    correction = removeSymbols(correction);

    Save(input, correction);
  }
};
