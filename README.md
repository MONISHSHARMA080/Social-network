# Social-network

### brief intro (HTML Version)        

 Social-network is an twitter-like social media site that has
*  (vanilla) HTML,CSS
*  React frontend
*  API (using Django-rest-framework)

It allows users to
* add new post (tweets/text)
*  Like posts
*  view all the posts(on a home page)
*  follow other users 
*  a follwoing feed to show posts from the following user
*  Profile page to see all the post from the user
*  Edit button ->  ownly the owner can edit their own post (the edit button will be shown to the owner on their own post)  

#### URL Patterns in HTML implementation
- `/` - Index page
- `/login` - Login page
- `/logout` - Logout page
- `/new_post` - Page for creating a new post
- `/register` - User registration page
- `/profile/<int:id>` - User profile page
- `/follow/<int:id>` - Follow another user
- `/unfollow/<int:id>` - Unfollow another user
- `/following` - Page for viewing users you are following
- `/edit/<int:id>` - Page for editing a post

#### API Endpoints
- `/api/post` - API for getting all posts
- `/api/post/create` - API for creating a new post
- `/api/post-change/<int:pk>` - API for getting, updating, and deleting a single post
- `/api/networks/` - API for making a user follow another user
- `/api/networks-change/<int:pk>/<int:pk_user>` - API for getting, updating, and deleting a network relationship between users
- `/api/user/<int:pk>/` - API for retrieving user data, user's posts, and users following the user
- `/api/network/<int:pk>` - API for retrieving posts of all the following users
- `/api/individual_post/<int:pk>` - API for retrieving a specific post by ID
- `/api/register` - API for user registration
- `/api/token/` - API for obtaining JWT tokens
- `/api/token/refresh/` - API for refreshing JWT tokens



## [Try out  ](https://network-sigma.vercel.app/) tip-> use super as password and email for dummy user
## [The website backend for api call and html(rough version) ](https://social-network-monish.onrender.com)



## API documentation
* to get the api [click here](https://social-network-monish.onrender.com/api/post)

### Authentication (or getting auth tokens for login)
#### Get JWT Token
- **URL:** `/api/token/`
- **Method:** `POST`
- **Description:** Obtain a JWT token for authentication of registered user and also the refresh .
- **Request Body:**
  - `username` (string) - The username of the user.
  - `password` (string) - The user's password.
- **Response:**
  - `access` (string) - Access token.
  - `refresh` (string) - Refresh token.

### User Registration
#### Register
- **URL:** `/api/register/`
- **Method:** `POST`
- **Description:** Register a new user. If the user is already in the DataBase it will return an error
- **Request Body:**
  - `username` (string) - The desired username.
  - `password` (string) - The user's password.
  - `email` (string) - User's email address.
- **Response:**
  - `statue` (integer) - Status code (200 for success, 403 for failure).
  - `access` (string) - Access token.
  - `refresh` (string) - Refresh token.

### Posts
#### Get All Posts
- **URL:** `/api/post/`
- **Method:** `GET`
- **Description:** Retrieve all posts ever made .
- **Response:** List of posts.

#### Create Post
- **URL:** `/api/post/create/`
- **Method:** `POST`
- **Description:** Create a new post.
- **Request Body:**
  - `text` (string) - The content of the post.
  - `likes`-yes! you can set the default likes on your post , Someone has to make money bu selling API /s (sarcasm) .
- **Response:** The created post.
- **Note -**Requires to auth.

#### Get, Update, or Delete a Post
- **URL:** `/api/post-change/<int:pk>/`
- **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Description:** (yeaaahhh  sure !! Retrieve too ) update, or delete a specific post by ID in url.
- **Request Body:**
  - `text`: new text,
  - `owner_id`: owner_id,
  -  `date`: date,
  -  `likes`: likes that you anted to change,
  -  `id`: post id,
  -  `owner_name`: owner_name
- **Response:** The post data (for GET) or success message (for PUT, PATCH, DELETE).
- **Note** : the api user(or post owner) can also  change the likes of a post . And you requires auth.

### User Profile
#### Get User Profile and Posts
- **URL:** `/api/user/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve a user's profile and all of their posts.
- **Response:** User profile data and their posts.

### Network (Follow/Unfollow)
#### Follow a User
- **URL:** `/api/networks/`
- **Method:** `POST`
- **Description:** Follow a user.
- **Request Body:**
  - `following` (integer) - ID of the user to follow.
  - `follower` (integer) - ID of the follower.
- **Response:** Network relationship data.

#### Unfollow a User
- **URL:** `/api/networks-change/<int:pk>/<int:pk_user>/`
- **Method:** `DELETE`
- **Description:** Unfollow a user.
- **Response:** Success message.

#### Get Posts from Followed Users
- **URL:** `/api/network/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve posts from users you are following.
- **Response:** List of posts.

#### Get Individual Post
- **URL:** `/api/individual_post/<int:pk>/`
- **Method:** `GET`
- **Description:** Retrieve a specific post by ID.
- **Response:** The post data.

Please make sure to replace placeholders like `<int:pk>` with actual values in your API URLs. This documentation should help users understand the functionality and usage of your Django application's API endpoints.

## React(frontend):


