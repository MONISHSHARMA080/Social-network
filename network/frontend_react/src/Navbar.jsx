import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Outlet, Link } from "react-router-dom";
import { useContext } from 'react';
import AuthContext from './context/AuthContext';
import './styles(post).css';
import { useNavigate } from "react-router-dom";


export default function NavBar() {

  const navigate = useNavigate();

  const {logoutUser} = useContext(AuthContext)
  function logout(){
    console.log("logout-----");
    logoutUser();
    // Redirect to login.
    navigate("/login");
  }

  return (<>
    <nav className="navbar navbar-expand-lg navbar-light bg-">
      <span
        className="navbar-brand"
        style={{
          backgroundImage: 'linear-gradient(to right, #ffd700, #ff0000)',
          WebkitBackgroundClip: 'text',
          backgroundClip: 'text',
          color: 'transparent',
        }}
      >
        Network
      </span>

      <div>
        <ul className="navbar-nav mr-auto">
          <li className="nav-item">
            <Link className="nav-link flowing-gradient" to="/">All Posts</Link>  
          </li>
          <li className="nav-item">
            <Link className="nav-link flowing-gradient" to="/following">Following</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link flowing-gradient" to="New-post">New post</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link flowing-gradient" to="/login">Log In</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link flowing-gradient" to="/register">Register</Link>
          </li>
          <li className="nav-item">
            <button className="nav-link flowing-gradient" onClick={(e)=>{e.preventDefault;logout()}} >Log Out</button>
          </li>
        </ul>
      </div>
    </nav>
    <div id="component" ><Outlet /></div>
  </>);
}

