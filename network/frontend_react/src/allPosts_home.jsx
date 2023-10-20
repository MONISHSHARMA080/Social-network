import React from 'react';
import './styles(post).css'; 
import  { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useContext } from 'react';
import AuthContext from './context/AuthContext';

export default function Post(props) {

  const [number, setNumber] = useState(0)
  const [likes, setLikes] = useState(props.likes + 1)
  const {user} = useContext(AuthContext) // from react router -- provide the login user's id
  const req_user_id = user ? user.user_id : null;

    const apiDateString = props.date ;
    const apiDate = new Date(apiDateString);
    
    // Formating the date as  "YYYY-MM-DD HH:mm:ss" format
    const formattedDate = apiDate.toLocaleString(); 
  
    function like() {
      
      fetch(`http://127.0.0.1:8000/api/post-change/${props.id}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          "text": props.text,
          "owner_id": props.owner,
          "date": props.date,
          "likes": likes, 
          "id": props.id,
          "owner_name": props.owner_name
        })
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((json_response) => {
          // Update likes state after a successful API response
          setLikes(likes + 1);
          console.log(json_response);
        })
        .catch((err) => {
          console.error(err.message);
        });
    }
// null cause it is not being send by drf
// console.log("props.requesting_user_id : " +props.requesting_user_id)

// for adding like/s  api 
  useEffect(() => {
    if (number === 1){

      console.log(props.id)
   
    } 
}, [number]);

// make sure to add backend validation too
function edit(){}


    return (
      <div className="post-content">
        <h4 className="post-title">
          <strong>
            <Link className="post-link"   to={`profile/${props.owner}`} >
              {props.owner_name}
            </Link>
             <span className='said_Post_colour' > said</span>:
          </strong>
        </h4>
        <h2 className="post-text">{props.text}</h2>
        { req_user_id ? ( // Check if req_user_id is not null
req_user_id === props.owner ? (
  <span>
    <button className="btn btn-danger rounded-pill w-20" onClick={edit}>
      Edit
    </button>
  </span>
) : null
      ) : null}
        
        <span className="post-likes" onClick={like}>Likes: {likes}</span>
        <span className="post-date">On : {formattedDate}</span>
      </div>
  );
}
