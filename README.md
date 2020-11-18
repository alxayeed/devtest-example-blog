# Blog Django Example App

### About the project
This Example blog is an assessment Project by GraySpace It. This is a very small yet varsatile Project.
Because with it's limited requirements, the project has involved different development stacks. 
This projects fetches posts , posts details and comment of the post from an external API and displayes them using Django.
I really enjoyed and wish to continue on this to add more features.


### Stacks

  - Python
  - Django
  - Django Rest Framework
  - AJAX
  - React(under development)
  - Deployment (Heroku)
  - Containerization(Docker)
  - Version Control System(Git/GitHub)

### Features
 - User Registration,Login  with Validation
 - User Registration,Login  with API
 - Display Postlist, details and comments of the post from external API
 - Ajax- Logged in User can add own comment to a post without refreshing the whole page
 - Live Demo on Heroku
 



### Live Demo
Click the link to see live demo

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://al-example-blog.herokuapp.com/)

### Authentication endpoints
<p> Register endpoint - https://al-example-blog.herokuapp.com/auth/api/register/ </p>
<p>  Login endpoint - https://al-example-blog.herokuapp.com/auth/api/login/ </p>

### Post and comments endpoint
<p> Post list - https://jsonplaceholder.typicode.com/posts </p>
<p> Post Details - https://jsonplaceholder.typicode.com/posts/[id] </p>
<p> Comments of a post - https://jsonplaceholder.typicode.com/posts/[id] </p>

### Comments endpoint
<p> Cimment list - http://localhost:8000/api/comments/ </p>
<p> Comment Details - http://localhost:8000/api/comments/[id] </p>
<p> Add comment - http://localhost:8000/api/comments/add/ </p>
<p> Update comment - http://localhost:8000/api/comments/[id]/update/ </p>
<p> Delete Comment - http://localhost:8000/api/comments/[id]/delete/ </p>

## Running

It is best to use the python `virtualenv` tool to build locally:
please change directory to backend(where the manage.py file is)

Now create/activate virtual environment and install all dependency
```sh
$ virtualenv-3.8 venv
$ source venv/bin/activate
$ pip install -r requirements.txt

```
run the server(don;t forget to cd backend/)

or you can use the following shortcut commands 
```
$ DEVELOPMENT=1 python manage.py runserver ( or make runserver)
```
### Shortcut for commands
```
$ make runserver
$ make migrations
$ make migrate

```

Then visit `http://localhost:8000` to view the app.
