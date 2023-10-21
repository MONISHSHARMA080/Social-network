import React from 'react'
import ReactDOM from 'react-dom/client'
import {createRoutesFromElements,Route,createBrowserRouter,RouterProvider,} from "react-router-dom";
import Home  from './Home.jsx';
import Profile from './Profile.jsx'
import NewPost from './New_post.jsx'
import Following from './Following.jsx' 
import ErrorPage from './error-page.jsx' 
import NavBar from './Navbar.jsx';
import Login from './login.jsx';
import Register from './register.jsx';
import AuthContextProvider from './context/AuthContextProvider.jsx';
import Edit from './Edit.jsx';


// const router = createBrowserRouter([
//   {
//     path: "/",
//     element: <NavBar />,
//     errorElement: <ErrorPage />,
//     children:[

//       {
//         path: "/",
//         element: <Home />,
//         errorElement: <ErrorPage />,
//       },
//       {
//         path: "following",
//         element: <Following />,
//         errorElement: <ErrorPage />,
//       },
//       {
//         path: "New-post",
//         element: <NewPost />,
//         errorElement: <ErrorPage />,
//       },
//       {
//         path: "profile",
//         element: <Profile />,
//         errorElement: <ErrorPage />,
//       },

//     ],//childern
//   }//children  
// ]);

const router = createBrowserRouter(
// make profile id dynamic on following -->>https://reactrouter.com/en/main/router-components/browser-router#basename
createRoutesFromElements(
  <Route path="/" element={<NavBar />}>
    <Route path="/" element={<Home />}  />
    <Route path="following" element={<Following />} />
    <Route path="New-post" element={<NewPost />} />
    <Route path="profile/:id" element={<Profile />} exact />
    <Route path="login" element={<Login />} />
    <Route path="register" element={<Register />} />
    <Route path="edit/:id" element={<Edit />} />
  </Route>
)
);

ReactDOM.createRoot(document.getElementById('root')).render(
<React.StrictMode>
   <AuthContextProvider> 
    <RouterProvider router={router} />
   </ AuthContextProvider> 
</React.StrictMode>,
);












// ------------------------Learning react router NOTES (for me)------------------------

// (1.> when making childrens (component that are  updating on the screen and and other are constant) for eg. navHedder is const and element ui(etc.(lie post and new post)) is child  
//        how to do it---------->>>>> 
// const router = createBrowserRouter([
//   {
//     path: "/",
//     element: <Root />,
//     errorElement: <ErrorPage />,
//     children: [
//       {
//         path: "contacts/:contactId",
//         element: <Contact />,
//       },
//     ],
//   },
// ]);

// (1.2.> we need to tell the Root route where to render the child and we do if by Outlet tag that . To rednder the child 
// component we put  outlet tag inside parent componets (inside the component file return HTML(JSX) ) 
// eg. of root.jsx ->import { Outlet } from "react-router-dom";

// export default function Root() {
//   return (
//     <>
//       {/* all the other elements */}
//       <div id="detail">
//         <Outlet />
//       </div>
//     </>
//   );
// }

//--------- even though we did all this but still browser is still refereshing ----------
// import React from 'react';
// import ReactDOM from 'react-dom/client';
// import { BrowserRouter as Router, Route, Routes } from "react-router-dom"; // Updated imports
// import Home from './Home.jsx';
// import Profile from './Profile.jsx';
// import NewPost from './New_post.jsx';
// import Following from './Following.jsx';
// import ErrorPage from './error-page.jsx';
// import NavBar from './Navbar.jsx';

// ReactDOM.createRoot(document.getElementById('root')).render(
//   <React.StrictMode>
//     <Router>
//       <NavBar />
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/following" element={<Following />} />
//       </Routes>
//     </Router>
//   </React.StrictMode>
// );
// // Learning react router NOTES 
// // (1.> when making childrens (component that are  updating on the screen and and other are constant) for eg. navHedder is const and element ui(etc.(lie post and new post)) is child  
// //        how to do it---------->>>>> 
// // const router = createBrowserRouter([
// //   {
// //     path: "/",
// //     element: <Root />,
// //     errorElement: <ErrorPage />,
// //     children: [
// //       {
// //         path: "contacts/:contactId",
// //         element: <Contact />,
// //       },
// //     ],
// //   },
// // ]);

// // (1.2.> we need to tell the Root route where to render the child and we do if by Outlet tag that . To rednder the child 
// // component we put  outlet tag inside parent componets (inside the component file return HTML(JSX) ) 
// // eg. of root.jsx ->import { Outlet } from "react-router-dom";

// // export default function Root() {
// //   return (
// //     <>
// //       {/* all the other elements */}
// //       <div id="detail">
// //         <Outlet />
// //       </div>
// //     </>
// //   );
// // }

// //--------- even though we did all this but still browser is still refereshing ----------