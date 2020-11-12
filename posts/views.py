from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser


# POSTS VIEW ENDPOINT
def posts(request):
    print(request.user == AnonymousUser)
    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    return render(request, 'blog-post.html')
