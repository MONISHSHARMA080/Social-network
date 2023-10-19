import React , {useEffect, useState,} from "react";
import AuthContext from "./AuthContext";
import jwt_decode from "jwt-decode";


const AuthContextProvider = ({children})=>{
    let [authTokens, setAuthTokens] = useState(null)
    let [user, setUser] = useState(null)
    let [loading, setLoading] = useState(true)
    useEffect(() => {
       console.log("authtokens : "+authTokens);
       console.log("here comes the user---");
       console.log(  user)


      }, [authTokens,user]);


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
            setAuthTokens(jwt_decode(data.access))
            setUser(jwt_decode(data.access).username)


            //for testing
            console.log("access : "+data.access);
            console.log("access : "+data.access);
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






      





    


//context/value same thing used to pass the in different object 
 var contextData={
     "loguserin":loguserin,

 } // contextData

return(
    <AuthContext.Provider value={contextData}  >
        {children}
    </AuthContext.Provider>
)



}

export default AuthContextProvider