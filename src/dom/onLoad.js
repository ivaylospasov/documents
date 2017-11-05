import formDataHandler from "../handlers/form";

// When the document is ready and loaded
document.addEventListener("DOMContentLoaded", () => {
  // get the form
  const form = document.getElementById("form-correct");

  form.addEventListener("submit", e => {
    e.preventDefault();
    // console.log(`catch submit events here`);
    formDataHandler(form);
  });
});
