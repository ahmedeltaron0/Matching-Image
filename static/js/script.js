
  document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('.login-form form');
    const signupForm = document.querySelector('.signup-form form');
  
    loginForm.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const email = loginForm.querySelector('input[name="email"]').value;
      const password = loginForm.querySelector('input[name="password"]').value;
  
    });
  
    signupForm.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const email = signupForm.querySelector('input[name="email"]').value;
      const password = signupForm.querySelector('input[name="password"]').value;
  
    });
  });
  