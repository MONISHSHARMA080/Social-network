import React , {useEffect, useState,} from "react";
import AuthContext from "./AuthContext";
import jwt_decode from "jwt-decode";
import { redirect } from "react-router-dom";
import { Navbar } from "react-bootstrap";




const AuthContextProvider = ({children})=>{
    let [authTokens, setAuthTokens] = useState(null)
    let [user, setUser] = useState(()=> localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true)
    
    // for testing only 
    useEffect(() => {
       if (user!=null){
       console.log("here comes the user---");
       console.log(  user.username)
    }

      }, [authTokens,user]);// useEffect
        
      
      async function loguserin(e) {
        e.preventDefault(); // Prevent the default form submission behavior
        
        var username = e.target.username.value;
        var password = e.target.password.value;
    
        try {
          const response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              username: username,
              password: password,
            }),// end of  body
          });// end of  fetch
    
          if (response.status === 200) {
            const data = await response.json();
            setAuthTokens(data.access)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            //   redirecting the users
            return redirect("/");
            //for testing
            // console.log("access : "+data.access);
            // console.log("access : "+data.access);
          } 
          else {
            const data = await response.json(); // Parse the response even if it's not a success status
            console.log("data.access: " + data.access);
            console.error('Error decoding token11'); 
            alert('Something went wrong!');
          }
        } 
        catch (error) {
          console.error('Error:', error.message);
        }// end of catch error
      } // end of loguserin

// Logout function
      let logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        // history.push('/login') implemnented  in Navbar
    }



      





    


//context/value same thing used to pass the in different object 
 var contextData={
     "loguserin":loguserin,
     "user":user,
     "authTokens":authTokens,
     "logoutUser":logoutUser,

 } // contextData

return(
    <AuthContext.Provider value={contextData}  >
        {children}
    </AuthContext.Provider>
)



}

export default AuthContextProvider