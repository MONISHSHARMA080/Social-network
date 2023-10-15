import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';

export default function Following() {
    const [data, setData] = useState([]);
  
// make this endpoint dynamic
    useEffect(() => {
      fetch('http://127.0.0.1:8000/api/network/2', {})
        .then((response) => {
          if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
          }
          return response.json();
        })
        .then((json_response) => {
          setData(json_response);
        })
        .catch((err) => {
          console.error(err.message);
        });
    }, []);
  
    return (
      <>
        <h1> Following:</h1>
        <div className='post-container'> 
              {data.map((post) => (
                  <Post key={post.id} text={post.text} owner={post.owner} owner_name={post.owner_name} date={post.date} likes={post.likes} />
              ))}
        </div>
      </>
    );
  }
  