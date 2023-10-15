import React from 'react';
import './styles(post).css'; 
import  { useState, useEffect } from 'react';

export default function Post(props) {

  const [number, setNumber] = useState(0)
  const [likes, setLikes] = useState(props.likes + 1)


    const apiDateString = props.date ;
    const apiDate = new Date(apiDateString);
    
    // Formating the date as  "YYYY-MM-DD HH:mm:ss" format
    const formattedDate = apiDate.toLocaleString(); // Adjust the format as needed
    
  
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
          "likes": likes, // Send the initial state value
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
    


// for adding like/s  api 
  useEffect(() => {
    if (number === 1){
      console.log("HHHHHHHHHHHHHHHHHHHHHH________-------") 
     console.log(likes)
     console.log(props.id)
   
    } 
}, [number]);



    return (
      <div className="post-content">
        <h4 className="post-title">
          <strong>
            <a className="post-link" href="${props.owner.id}" >
              {props.owner_name}
            </a>
             <span className='said_Post_colour' > said</span>:
          </strong>
        </h4>
        <h2 className="post-text">{props.text}</h2>
        {props.editable && (
          <a className="btn btn-danger" style={{ margin: '12px', borderRadius: '12px' }} href={`{% url 'edit' ${props.id} %}`}>
            Edit
          </a>
        )}
        <span className="post-likes" onClick={like}>Likes: {likes}</span>
        <span className="post-date">On  : {formattedDate}</span>
      </div>
  );
}
