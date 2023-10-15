import React, { useState, useEffect } from 'react';

export default function NewPost(){

const [text, setText] = useState('');
const [number, setNumber] = useState(0);

useEffect(()=>{
   if (number> 0 && number<2 ) {
    api_call();
   }   


}), [number];



function api_call(){
    fetch('http://127.0.0.1:8000/api/post/create',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json', // Set the content type to JSON
          },
        body: JSON.stringify({
            text:`${text}`,
            likes:0
        }) //bofdy of fetch
        }) // fetch
        .then(response => response.json())
        .then(result => {
           // Print result
             console.log(result);});    
             setText('')
}



return (<>
 
    <h1 className='said_Post_colour' >Make a post:</h1>

    <div className="container">
        <div className="card">
            <h1>Add a New Post</h1>
            <form action="" method="post" onSubmit={(e)=>{e.preventDefault();setNumber(number+1)}} >

                <div className="form-group">
                    <textarea className="form-control rounded" id="text" name="text" rows="17" column="10" placeholder="Write your post here..." value={text} required onChange={(e) => {setText(e.target.value)}} ></textarea>
                </div>
                <button type="submit">Post</button>
            </form>
        </div>
    </div>


</>)}