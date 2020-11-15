from django.shortcuts import render
import requests
from django.core.paginator import Paginator

# POSTS VIEW ENDPOINT


def posts(request):
    '''
    View for homapage/ all posts
    '''
    response = requests.get(
        'https://jsonplaceholder.typicode.com/posts').json()

    # Pagination
    paginator = Paginator(response, 10)
    page_number = request.GET.get('page')

    # if it is the first page, get response from page 1
    if page_number is None:
        response = paginator.page(1)
    # else, get posts of page_number
    else:
        response = paginator.page(page_number)

    return render(request, 'blog-listing.html', {'response': response})


# POST DETAILS VIEW ENDPOINT
def post_details(request, post_id):
    '''
    View for details of a post
    '''
    url = 'https://jsonplaceholder.typicode.com/posts/'+str(post_id)
    post = requests.get(url).json()

    comments = requests.get(url + '/comments').json()
    return render(request, 'blog-post.html', {'response': post, 'comments': comments})
