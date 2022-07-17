/*adding invalid password check*/

function validatePassword() {
  const password = document.getElementById('inputPassword');
  const confirm_password = document.getElementById('inputConfirmPassword');
  if (password.value !== confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity("");
  }
}