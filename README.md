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

## API documentation
* to get the api [click here](https://social-network-monish.onrender.com/api/post)

### Views.py

#### `MyTokenObtainPairSerializer`
- **Description:** Custom TokenObtainPairSerializer for adding custom claims to the JWT token.
- **Custom Claims:** It adds the 'username' claim to the token.
- **Usage:** Used for obtaining JWT tokens with custom claims.

#### `MyTokenObtainPairView`
- **Description:** Custom TokenObtainPairView for obtaining JWT tokens with custom claims.
- **Serializer:** Uses `MyTokenObtainPairSerializer` for token creation.

#### `RegisterView`
- **Description:** API view for user registration.
- **HTTP Method:** POST
- **Input Data:** User registration data.
- **Response:** Returns a JWT refresh and access token upon successful registration.
- **Errors:** Returns a 403 error if the registration data is invalid.

#### `IndividualPost_api`
- **Description:** API for retrieving a specific post by ID.
- **HTTP Method:** GET
- **Input Parameter:** Post ID in the URL.
- **Response:** Returns the specified post.

#### `Follow_api`
- **Description:** API for retrieving posts of all the following users.
- **HTTP Method:** GET
- **Input Parameter:** User ID in the URL.
- **Response:** Returns posts from users that the specified user is following.

#### `User_api`
- **Description:** API for retrieving user data, user's posts, and users following the user.
- **HTTP Method:** GET
- **Input Parameter:** User ID in the URL.
- **Response:** Returns user information along with their posts and the users following them.

#### `CreatePost`
- **Description:** API for creating a new post.
- **HTTP Method:** POST
- **Input Data:** Post data.
- **Response:** Returns the created post.
- **Authentication:** Requires user authentication.

#### `Post_api`
- **Description:** API for getting all posts.
- **HTTP Method:** GET
- **Response:** Returns all posts in descending order of date.
- **Authentication:** Allows unauthenticated users for GET requests.

#### `Post_rud_api`
- **Description:** API for getting, updating, and deleting a single post.
- **HTTP Methods:** GET, PUT, PATCH, DELETE
- **Input Parameter:** Post ID in the URL.
- **Authentication:** Requires user authentication.

#### `Network_api`
- **Description:** API for making a user follow another user.
- **HTTP Method:** POST
- **Input Data:** Follower and following user IDs.
- **Response:** Returns the created network relationship.
- **Authentication:** Requires user authentication.

#### `Network_rud_api`
- **Description:** API for getting, updating, and deleting a network relationship between users.
- **HTTP Methods:** GET, PUT, PATCH, DELETE
- **Input Parameters:** Follower and following user IDs in the URL.
- **Authentication:** Requires user authentication.

### Urls.py

#### URL Patterns
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



## [webiste (frontend react) , use super as password and email for dummy user   ](https://network-sigma.vercel.app/)
## [The website backend for api call and html(rough version) ](https://social-network-monish.onrender.com)
 
