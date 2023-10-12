import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';

export default function Profile() {
  const [data, setData] = useState({ posts: [] }); // Initialize data with an empty array for posts

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/user/3', {})
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


// ADD THE FOLLOW BUTTON 


  return (
    <>
      <h1 className='all_post_by' >All posts by {data.username} :</h1>
      <div className="post-container">
        {data.posts.map((post) => (
          <Post
            key={post.id}
            text={post.text}
            owner={post.owner_id}
            owner_name={post.owner_name}
            date={post.date}
            likes={post.likes}
          />
        ))}
      </div>
    </>
  );
}

