import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';
import { useParams } from 'react-router-dom';

export default function Profile() {
  const [data, setData] = useState({ posts: [] }); // Initializing data with an empty array for posts
  const [number, setNumber] = useState(0)
  const { id } = useParams();  // from react router -- to fetch the user's data (in useEffect)

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/api/user/${id}`, {})
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

  function network(){
    fetch('http://127.0.0.1:8000/api/networks/', {

    method: 'POST',
    headers: {
        'Content-Type': 'application/json', // Set the content type to JSON
      },
    body: JSON.stringify({

        "following":`${data.id}` ,
    //make this data.requesting_user_id after auth setup
        "follower": 2
    //make this data.requesting_user_id after auth setup

    }) //bofdy of fetch
    })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((json_response) => {
      console.log(json_response); 
    })
    .catch((err) => {
      console.error(err.message);
    });
  }

  // for network/follow  api 
  useEffect(() => {
       if (number === 1){
        console.log(data.id)
        network();
       } 
  }, [number]);




  
// ADD THE FOLLOW BUTTON 


  return (
    <>
      <h1 className='text-5xl font-bold m-6 p-4 flex-shrink  text-amber-500' >All posts by {data.username} :</h1>
      <button className='button-n' onClick={()=>{setNumber(number + 1)}} >Follow {data.username}</button>
      <div className="post-container">
        {data.posts.map((post) => (
          <Post
            id={post.id}
            text={post.text}
            owner={post.owner_id}
            owner_name={post.owner_name}
            date={post.date}
            likes={post.likes}
            requesting_user_id={data.requesting_user_id}
            key={post.id}
          />
        ))}
      </div>
    </>
  );
}


