import { useParams, useNavigate } from "react-router-dom";
import React, { useEffect, useState ,useContext} from "react";
import './styles(post).css'; 
import AuthContext from "./context/AuthContext";


export default function Edit(){
    const { id } = useParams();  // from react router -- to fetch the user's data (in useEffect)
    var [text , setText] = useState("")
    var [data , setData] = useState()
    const {user , authTokens} = useContext(AuthContext)
    const navigate = useNavigate();
    // for both apis
    const headers = {
        'Content-Type': 'application/json',
      };
      
      if (authTokens) {
        headers.Authorization = `Bearer ${authTokens.access}`;
      } 

useEffect(()=>{
    if (user === null){
        navigate("/");
     }
    fetch(`http://127.0.0.1:8000/api/individual_post/${id}`,{
        //auth
        //chatgpt to set it in loader function
        method: 'GET',
        headers,
    })
    .then(response => response.json())
    .then(data => {
        setText(data[0].text);
        setData(data[0])
    })//then
    .catch(error => {
        console.error('Error fetching data:', error);
    });//catch


},[])
useEffect(()=>{

 console.log("***************")
 console.log(text)
 console.log("***************")
},[text])



function change(e){
    e.preventDefault();
    fetch(`http://127.0.0.1:8000/api/post-change/${id}`,{
        //auth
        //chatgpt to set it in loader function
        method: 'PUT',
        headers,
        body: JSON.stringify({
            text: text,
            owner_id: data.owner_id,
            date: data.date,
            likes: data.likes,
            id: data.id,
            owner_name: data.owner_name
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })//then
    .catch(error => {
        console.error('Error fetching data:  ', error);
    });//catch


}



 return (<><h1 className="bg-orange-950 w-2/5 rounded-4xl  h-14 text-center  rounded-full"> Edit your post   {id} </h1>
 
 
 
 
 <div className="container-n ">
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
                <button className='btn btn-danger rounded-pill w-25 ' type="submit" onClick={(e)=>{change(e)}} >Post</button>
            </form>
        </div>
    </div>

 
 
 
 
 
 
 
 
 </>)

}