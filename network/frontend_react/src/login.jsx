import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useContext } from 'react';
import AuthContext from './context/AuthContext';
// import AuthContext from './context/AuthContext';



export default function Login() {
    
    const {loguserin} = useContext(AuthContext)




  return (
    <div>
      <h2 className='m-4'>Login</h2>

      <form className='w-11/12' onSubmit={(e) => loguserin(e)}>
        <div className="form-group">
          <input
            autoFocus
            className="form-control m-3"
            type="text"
            name="username"
            placeholder="Username"
          />
        </div>
        <div className="form-group">
          <input
            className="form-control m-3"
            type="password"
            name="password"
            placeholder="Password"
          />
        </div>
        <input className="btn btn-primary m-3" type="submit" value="Login" />
      </form>

      <h4 className='m-2'>
        Don't have an account?<Link className='btn btn-danger m-3' to="/register">Register here.</Link>
      </h4>
    </div>
  );
}