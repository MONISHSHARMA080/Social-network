import React from 'react';
import './styles(post).css'; 

export default function Post(props) {

    const apiDateString = props.date ;
    const apiDate = new Date(apiDateString);
    
    // Formating the date as  "YYYY-MM-DD HH:mm:ss" format
    const formattedDate = apiDate.toLocaleString(); // Adjust the format as needed
    console.log(props.id)

    return (
      <div className="post-content">
        <h4 className="post-title">
          <strong>
            <a className="post-link" href="${props.owner.id}" >
              {props.owner_name}
            </a>
             <span className='said_Post_colour' > said</span>:
          </strong>
        </h4>
        <h2 className="post-text">{props.text}</h2>
        {props.editable && (
          <a className="btn btn-danger" style={{ margin: '12px', borderRadius: '12px' }} href={`{% url 'edit' ${props.id} %}`}>
            Edit
          </a>
        )}
        <span className="post-likes">Likes: {props.likes}</span>
        <span className="post-date">On  : {formattedDate}</span>
      </div>
  );
}
