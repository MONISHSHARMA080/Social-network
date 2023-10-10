import React, { useState, useEffect } from 'react';
import Post from './allPosts_home';

export default function Home() {
  const [data, setData] = useState([]);

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
        console.log(json_response);
      })
      .catch((err) => {
        console.error(err.message);
      });
  }, []);

  return (
    <>
      <h1>Ora Ora Ora Ora Ora Ora</h1>
      <h1>All Posts:</h1>

      {data.map((post) => (
        <Post key={post.id} text={post.text} owner={post.owner} date={post.date} likes={post.likes} />
      ))}
    </>
  );
}
