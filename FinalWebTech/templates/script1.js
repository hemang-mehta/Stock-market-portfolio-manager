// Function to validate the signup form and append user data to local storage
function appendUserToLocalStorage(userData) {
  const storedData = JSON.parse(localStorage.getItem("usersData")) || [];
  storedData.push(userData);
  localStorage.setItem("usersData", JSON.stringify(storedData));
}

// Function to validate the signup form
function validateSignupForm() {
  const firstName = document.getElementById("firstn").value;
  const lastName = document.getElementById("lastn").value;
  const email = document.getElementById("email").value;
  const address = document.getElementById("address").value;
  const city = document.getElementById("city").value;
  const pincode = document.getElementById("pc").value;
  const password = document.getElementById("password").value;

  // Check if all fields are filled
  if (
    firstName === "" ||
    lastName === "" ||
    email === "" ||
    address === "" ||
    city === "" ||
    pincode === "" ||
    password === ""
  ) {
    alert("All fields are required.");
    return false;
  }

  // Check if the email is valid
  if (!validateEmail(email)) {
    alert("Invalid email address.");
    return false;
  }

  // Check if pincode is exactly 6 digits
  if (!/^\d{6}$/.test(pincode)) {
    alert("Pincode must be exactly 6 digits.");
    return false;
  }

  // Check for duplicate email addresses (example)
  if (isDuplicateEmail(email)) {
    alert("This email is already registered.");
    return false;
  }

  // Store user data in local storage
  const userData = {
    firstName,
    lastName,
    email,
    address,
    city,
    pincode,
    password,
  };

  appendUserToLocalStorage(userData);

  return true;
}

// Function to validate email format
function validateEmail(email) {
  const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
  return emailPattern.test(email);
}

// Dummy function to check for duplicate emails (replace with your server-side check)
function isDuplicateEmail(email) {
  // You should perform a server-side check to verify if the email is unique
  // This is a dummy example and should be replaced with your server-side logic
  const existingEmails = ["user1@example.com", "user2@example.com", "user3@example.com"];
  return existingEmails.includes(email);
}

// Add event listener to the form submit button
const submitButton = document.querySelector("button[type='submit']");
submitButton.addEventListener("click", (event) => {
  if (!validateSignupForm()) {
    event.preventDefault(); // Prevent form submission if validation fails
  }
});
