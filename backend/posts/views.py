from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
import requests
from django.core.paginator import Paginator
from .models import Comment

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

    # else, get posts of specific page_number
    else:
        response = paginator.page(page_number)

    return render(request, 'build/index.html')


# POST DETAILS VIEW ENDPOINT
# @csrf_exempt
def post_details(request, post_id):
    '''
    View for details of a post
    '''
    url = 'https://jsonplaceholder.typicode.com/posts/'+str(post_id)
    post = requests.get(url).json()

    # if user post a comment
    if request.method == 'POST':
        postId = request.POST.get('postId')
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        print(postId)

        # save to database
        comment = Comment(post_id=postId, name=name, email=email, body=body)
        comment.save()

    # comment by the user from databse
    user_comment = Comment.objects.filter(post_id=post['id'])

    # comment from external api
    comments = requests.get(url + '/comments').json()

    context = {
        'response': post,
        'comments': comments,
        'user_comment': user_comment
    }

    if request.is_ajax():
        html = render_to_string('comment.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'build/index.html', context)
