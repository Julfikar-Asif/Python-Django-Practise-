from django.shortcuts import render

posts  = [
    {
        'author' : 'guru',
        'title' : 'Blog Post 1',
        'content' : 'Hobe arki ekta kisu ',
        'date_posted' : 'January 1, 2026'
    },
    {
        'author' : 'bolla guru',
        'title' : 'Blog Post 2',
        'content' : 'bolla ekhono post kore nai ',
        'date_posted' : 'January 2, 2026'
    }
]


def home(request):
    context ={
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title' : 'Contact'})



#  blog -> templates -> blog -> template.html
# view → URL → template।