import { createContext, useState, useEffect } from 'react'
import jwt_decode from "jwt-decode";
import { useHistory } from 'react'

const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({children}) => {

    let [authToken ,setAuthToken] = useState(null)
    //for storing decoded data from auth token
    let [user ,setUser] = useState(null)
  
    // function to log the user in --here(context api) to store/pass in other components 
    const Login = () => {
        const handleSubmit = (e) => {
          e.preventDefault();
          var username = e.target.username.value;
          var password = e.target.password.value;
          fetch('http://localhost:8000/api/token/',{
            method: 'POST',
            headers: {
                'Content-Type':'application/json' // Setting the content type to JSON
              },
            body: JSON.stringify({
     
                "username": `${username}`,
                "password": `${password}`
                    
            }) // body of fetch
          }) // fetch
          .then(response => {
            let data = response.json()
            if(response.status === 200){
                setAuthTokens(data)
                setUser(jwt_decode(data.access))
                localStorage.setItem('authTokens', JSON.stringify(data))
                history.push('/')
            }
            //remove it in production environment
            else{
                alert('Something went wrong!')
            }
          }) // response
          .then(result => {
             // Print result
             console.log(result);
           }) // fetch end
        } // Close Login function
    } // Close AuthProvider function
  
    var contextData = {
        user:user,
        // authTokens:authTokens,
        // // loginUser:loginUser,
        // logoutUser:logoutUser,
    }
  
    return (
        <AuthContext.Provider value={contextData} >
          { children}
        </AuthContext.Provider>
    )  
  }
  
  