import serialize from "../methods/serialize";
import trimmer from "../methods/trimmer";

export default form => {
  // Get serialized (key-value) form data representation.
  const data = serialize(form);

  // Iterate through data and work with it
  for (const formValue in data) {
    // trimmer() call is an example of a helper function
    console.log(`Trimmed version: ${trimmer(data[formValue]["value"])}`);
  }
};
