import React from 'react'
import ReactDOM from 'react-dom/client'
import Home from './Home.jsx'
import Profile from './Profile.jsx'
import NewPost from './New_post.jsx'
import Following from './Following.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Profile />
    <Following />
    <NewPost />
    <Home />

  </React.StrictMode>,
)


