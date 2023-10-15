import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';

export default function Home() {
  const [data, setData] = useState([]);

// here using this to get all post on home page
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/post', {})
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
      <h1>All Posts:</h1>
      <div className='post-container'> 
            {data.map((post) => (
                          <Post
                          key={post.id}
                          text={post.text}
                          owner={post.owner_id}
                          owner_name={post.owner_name}
                          date={post.date}
                          likes={post.likes}
                          id={post.id}
                        />         
                          ))}
      </div>
    </>
  );
}
