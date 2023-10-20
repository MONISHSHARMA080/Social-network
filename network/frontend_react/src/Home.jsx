import React, { useState, useEffect , useContext } from 'react';
import Post from './allPosts_home';
import AuthContext from './context/AuthContext';

export default function Home() {
  const [data, setData] = useState([]);
  let {authTokens} = useContext(AuthContext)

// here using this to get all post on home page
  useEffect(() => {
    const headers = {
      'Content-Type': 'application/json',
    };
    
    if (authTokens) {
      headers.Authorization = `Bearer ${authTokens.access}`;
    }

    console.log("headers from Home ???@@%@*%@%*!(%!(!^(_____--------")
    console.log(headers)
    fetch('http://127.0.0.1:8000/api/post', {

    method: 'GET',
    headers,

    })
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
     <h1 className="text-5xl font-bold m-6 p-4 flex-shrink  text-amber-500 ">All Posts:</h1>

      <div className='post-container'> 
            {data.map((post) => (
                          <Post
                          id={post.id}
                          text={post.text}
                          owner={post.owner_id}
                          owner_name={post.owner_name}
                          date={post.date}
                          likes={post.likes}
                          key={post.id}
                        />         
                          ))}
      </div>
    </>
  );
}
