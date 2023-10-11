import React from 'react';
import './styles(post).css'; 

export default function Post(props) {
  return (
    <div className="post-container">
      <div className="post-content">
        <h4 className="post-title">
          <strong>
            <a className="post-link" href={`{% url 'profile' ${props.owner.id} %}`}>
              {props.owner_name} said:
            </a>
          </strong>
        </h4>
        <h2 className="post-text">{props.text}</h2>
        {props.editable && (
          <a className="btn btn-danger" style={{ margin: '12px', borderRadius: '12px' }} href={`{% url 'edit' ${props.id} %}`}>
            Edit
          </a>
        )}
        <span className="post-likes">Likes: {props.likes}</span>
        <span className="post-date">{props.date}</span>
      </div>
    </div>
  );
}
