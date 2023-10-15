import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Home from './Home.jsx'
import Profile from './Profile.jsx'
import NewPost from './New_post.jsx'
import Following from './Following.jsx' 
import ErrorPage from './error-page.jsx' 

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
    errorElement: <ErrorPage />,
  },
  {
    path: "following",
    element: <Following />,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
     <RouterProvider router={router} />
    {/* <Profile />
    <Following />
    <NewPost />
    <Home /> */}

  </React.StrictMode>,
)


