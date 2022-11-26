/**
 * Validate user input
 * @return true if user input is accepted and false otherwise
 */
function validate_form() {
  let inputValue = document.getElementById("string").value;
  for (let i = 0; i < inputValue.length; i++) {
    if (inputValue[i] != "a" && inputValue[i] != "b") {
      alert("String tidak valid! Hanya diperbolehkan kombinasi a dan/atau b!");
      return false;
    }
  }
  return true;
}