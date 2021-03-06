# Django Example Blog 


<table>
  <tr>
    <td>Home</td>
    <td>Registration</td>

  </tr>
  <tr>
    <td><img src="img/blogdemo1.png" width="" height="" /></td>
    <td><img src="img/blogdemor.png" width="" height=""  /> </td>
  </tr>

  <tr>
    <td>Post details</td>
    <td>Comment section</td>

  </tr>
  <tr>
    <td><img src="img/blogdemo2.png" width="300" height="250" /></td>
    <td><img src="img/blogdemo4.png" width="300" height="250"  /> </td>
  </tr>
 </table>
 <hr/>

### About the project
This Example blog is a very small yet varsatile Project.
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

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://devtest-blog.herokuapp.com/)

### Authentication endpoints
<p> Register endpoint - https://devtest-blog.herokuapp.com/auth/api/register/ </p>
<p>  Login endpoint - https://devtest-blog.herokuapp.com/auth/api/login/ </p>

## Running

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-3.8 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```
or you can use the following shortcut commands 
```
$ make runserver
$ make migrations
$ make migrate

```

Then visit `http://localhost:8000` to view the app.
