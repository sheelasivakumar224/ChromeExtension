document.getElementById('reg-btn').addEventListener('click',function(){
    document.getElementById("register-div").style.display="inline";
    document.getElementById("login-div").style.display="none";
});

document.getElementById("log-btn").addEventListener('click',function(){
    document.getElementById("register-div").style.display="none";
    document.getElementById("login-div").style.display="inline";
})



const firebaseConfig = {
    apiKey: "AIzaSyDzn1-mI_zDgCYK0WOd9IEWEsJlB-X6YgY",
    authDomain: "login-48aa5.firebaseapp.com",
    databaseURL: "https://login-48aa5-default-rtdb.firebaseio.com",
    projectId: "login-48aa5",
    storageBucket: "login-48aa5.appspot.com",
    messagingSenderId: "1088217348514",
    appId: "1:1088217348514:web:9fdd981b25afa25b085afb",
    measurementId: "G-9FQZ2ZXB56"
};
const app = firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();

const loginButton = document.getElementById("loginbtn");
  loginButton.addEventListener("click", function() {
    const email = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    auth.signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        // User logged in successfully
        const user = userCredential.user;
        alert("Welcome Home")
      })
      .catch((error) => {
        console.error("Login error:", error.message);
      });
});


const signUpButton = document.getElementById("registerbtn");
  signUpButton.addEventListener("click", function() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    auth.createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {
        // User signed up successfully
        const user = userCredential.user;
        console.log("User signed up:", user);
        alert("Welcome User!")
      })
      .catch((error) => {
        console.error("Signup error:", error.message);
      });
});
