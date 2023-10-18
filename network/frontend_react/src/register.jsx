import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Register = () => {
  // const [message, setMessage] = useState('');

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   // You can add your registration logic here and update the message accordingly.
  //   setMessage('Registration failed. Please try again.'); // Replace with your actual registration logic.
  // };
  {/* {
        {message && <div>{message}</div>} }
   onSubmit={handleSubmit} */}

  return (
    <div >
      <h2 className='m-4' >Register</h2>
      <form className='w-11/12' >
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
            type="email"
            name="email"
            placeholder="Email Address"
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
        <div className="form-group">
          <input
            className="form-control m-3"
            type="password"
            name="confirmation"
            placeholder="Confirm Password"
          />
        </div>
        <input className="btn btn-primary m-2" type="submit" value="Register" />
      </form>

      <h4 className='m-2'>
        Already have an account?<Link className="btn btn-danger m-3" to="/login">Log In here.</Link>
      </h4 >
    </div>
  );
};

export default Register;
