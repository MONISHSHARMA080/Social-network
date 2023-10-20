import React, { useState, useEffect , useContext } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import AuthContext from './context/AuthContext';
import './styles(post).css';
import { useNavigate } from "react-router-dom";





// rm hardcoding of the value in views.py--CreatePost and make a new query param.   
export default function NewPost(){
const [text, setText] = useState('');
const [number, setNumber] = useState(0);
const {user} = useContext(AuthContext)
const navigate = useNavigate(); 
useEffect(()=>{
    // client side routing to not allow unauthintiacated users to make post
    if (user === null){
       navigate("/");
    }


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
 
    <h1 className='text-5xl font-bold m-6 p-4 flex-shrink  text-amber-500' >Make a post:</h1>

    <div className="container-n">
        <div className="card-n">
            <h1>Add a New Post</h1>
            <form action="" method="post" onSubmit={(e)=>{e.preventDefault();setNumber(number+1)}} >

                <div className="form-group-n">
                <textarea
                        className="form-control rounded"
                        id="text"
                        name="text"
                        rows="17"
                        column="10" 
                        placeholder="Write your post here..."
                        value={text}
                        required
                        onChange={(e) => {
                            setText(e.target.value);
                        }}
                        style={{ width: "100%" }} ></textarea>            
               </div>
                <button className='btn btn-danger rounded-pill w-25 ' type="submit">Post</button>
            </form>
        </div>
    </div>


</>)}