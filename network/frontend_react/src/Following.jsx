import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';
import { useContext } from 'react';
import AuthContext from './context/AuthContext';
import { useNavigate } from "react-router-dom";


export default function Following() {

    const [data, setData] = useState([]);
    const {user} = useContext(AuthContext)
    const navigate = useNavigate();

    useEffect(() => {
      // client side routing as unauth. users don't  have following
      if (user === null){
        navigate("/");
     }
      fetch(`http://127.0.0.1:8000/api/network/${user.user_id}`, {})
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
        <h1 className='text-5xl font-bold m-6 p-4 flex-shrink  text-amber-500' > Following:</h1>
        <div className='post-container'> 
              {data.map((post) => (
                  <Post
                  id={post.id}
                  text={post.text}
                  owner={post.owner_id}
                  owner_name={post.owner_name}
                  date={post.date}
                  likes={post.likes}
                  key={post.id} />
              ))}
        </div>
      </>
    );
  }
  