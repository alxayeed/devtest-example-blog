from django.shortcuts import render
import requests

# POSTS VIEW ENDPOINT


def posts(request):
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts').json()
    return render(request, 'blog-listing.html', {'response': response})


# POST DETAILS VIEW ENDPOINT
def post_details(request, post_id):
    url = 'https://jsonplaceholder.typicode.com/posts/'+str(post_id)
    post = requests.get(url).json()

    comments = requests.get(url + '/comments').json()
    return render(request, 'blog-post.html', {'response': post, 'comments': comments})
