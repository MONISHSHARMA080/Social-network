import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Outlet, Link } from "react-router-dom";


export default function NavBar({ user }) {
  return (<>
    <nav className="navbar navbar-expand-lg navbar-light">
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
            <Link className="nav-link" to="/">All Posts</Link>  
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/following">Following</Link>
          </li>
              <li className="nav-item">
                <a className="nav-link" href="/logout">Log Out</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/new_post">New post</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/login">Log In</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="/register">Register</a>
              </li>
        </ul>
      </div>
    </nav>
    <div id="component" ><Outlet /></div>
  </>);
}

