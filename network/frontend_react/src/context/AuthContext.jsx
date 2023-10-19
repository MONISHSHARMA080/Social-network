import { createContext, useState, useEffect } from 'react';
import jwt_decode from 'jwt-decode';
import { redirect } from "react-router-dom";


const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  let [authToken, setAuthToken] = useState(null);
  // For storing decoded data from auth token
  let [user, setUser] = useState(null);
  useEffect(() => {
  
    console.log("user from useEffect : "+user)
    }, [user]);
    

  // Function to log the user in -- here (context API) to store/pass in other components
  const loginUser = (e) => {
    console.log('Login function initiated');
    e.preventDefault();
    var username = e.target.username.value;
    var password = e.target.password.value;
    fetch('http://127.0.0.1:8000/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Setting the content type to JSON
      },
      body: JSON.stringify({
        username: `${username}`,
        password: `${password}`,
      }), // body of fetch
    }) // fetch
      .then((response) => {
        let data = response.json();
        if (response.status === 200) {
          setAuthToken(data);
          try {
            setUser(jwt_decode(data.access));
          } catch (error) {
            console.error('Error decoding token:', error.message); // Log the error message
          }
          console.log("hhhhh"+user);
          localStorage.setItem('authTokens', JSON.stringify(data));
          return redirect('/');
        }
        // Remove it in a production environment
        else {
          alert('Something went wrong!');
        }
      }) // response
      
      .then((result) => {
        // Print result
        console.log(result);
      }); // then end
  }; // Close Login function

  var contextData = {
    "user": user,
    "loginUser": loginUser,
  };

  return (
    <AuthContext.Provider value={contextData}>
      {children}
    </AuthContext.Provider>
  );
}; // Close AuthProvider function
