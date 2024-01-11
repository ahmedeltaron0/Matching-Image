   // Import the functions you need from the SDKs you need
   import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
   import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-analytics.js";
   // TODO: Add SDKs for Firebase products that you want to use
   // https://firebase.google.com/docs/web/setup#available-libraries
 
   // Your web app's Firebase configuration
   // For Firebase JS SDK v7.20.0 and later, measurementId is optional
   const firebaseConfig = {
     apiKey: "AIzaSyCunO6iQEo-nQK0ksMY0HFbiONZMbSafdY",
     authDomain: "image-match-a3cca.firebaseapp.com",
     projectId: "image-match-a3cca",
     storageBucket: "image-match-a3cca.appspot.com",
     messagingSenderId: "290895252240",
     appId: "1:290895252240:web:b294ef541eaef5f2f9b395",
     measurementId: "G-LERF1Z925V"
   };
 
   // Initialize Firebase
   const app = initializeApp(firebaseConfig);
   const analytics = getAnalytics(app);
  firebase.initializeApp(firebaseConfig);
  
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
  function redirectToLogin() {
    window.location.href = "/login/"; /* Replace with your actual login page URL */
  }
  
  function redirectToSignup() {
    window.location.href = "/signup/"; /* Replace with your actual signup page URL */
  }
