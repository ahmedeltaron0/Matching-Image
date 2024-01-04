    const firebaseConfig = {
      apiKey: "AIzaSyCunO6iQEo-nQK0ksMY0HFbiONZMbSafdY",
      authDomain: "image-match-a3cca.firebaseapp.com",
      projectId: "image-match-a3cca",
      storageBucket: "image-match-a3cca.appspot.com",
      messagingSenderId: "290895252240",
      appId: "1:290895252240:web:b294ef541eaef5f2f9b395",
      measurementId: "G-LERF1Z925V"
    };
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
  