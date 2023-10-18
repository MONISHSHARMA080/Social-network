 import {Route ,redirect }from "react-router-dom";

//making a private route for the NewPost so that unlogged users can't access that

const PrivateRoute = ({children , ...rest })=>{
    return(
        <Route {...rest }>{children}</Route>
    )
}

export default PrivateRoute