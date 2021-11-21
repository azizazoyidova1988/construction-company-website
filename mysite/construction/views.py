from django.shortcuts import render, redirect
from .models import *
from .services import *
from .forms import VideoForm, For_QueryForm, CommenterForm
from django.core.paginator import Paginator, EmptyPage


def home(request):
    firstvideo = Video.objects.last()
    print(firstvideo)
    video = firstvideo.video.url
    form = VideoForm(request.POST or None, request.FILES or None)
    if request.method == 'GET':
        if form.is_valid():
            form.save()
    facts = get_facts()
    services = get_services()
    teams = get_team()
    question = get_questions()
    testimonial = get_testimonials()
    blogs = get_blog()

    ctx = {
        "home": "active",
        "facts": facts,
        "services": services,
        "teams": teams,
        "question": question,
        "testimonial": testimonial,
        "blogs": blogs,
        "video": video,
        "form": form,
    }
    return render(request, 'construction/index.html', ctx)


def about(request):
    facts = get_facts()
    teams = get_team()
    question = get_questions()
    ctx = {
        "about": "active",
        "facts": facts,
        "teams": teams,
        "question": question,

    }
    return render(request, 'construction/about.html', ctx)


def team(request):
    teams = get_team()
    ctx = {
        "team": "active",
        "teams": teams,

    }
    return render(request, 'construction/team.html', ctx)


def service(request):
    services = get_services()
    question = get_questions()
    ctx = {
        "service": "active",
        "question": question,
        "services": services,

    }
    return render(request, 'construction/service.html', ctx)


def project(request):
    categoty = get_categories()
    projects = get_projects()
    ctx = {
        "project": "active",
        "projects": projects,
        "category": categoty,

    }
    return render(request, 'construction/portfolio.html', ctx)


def blog(request):
    blogs = get_blog()
    p = Paginator(blogs, 2)
    page_num = request.GET.get('page', 1)
    total_pages = len(blogs)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        "blog": "active",
        "blogs": blogs,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages

    }
    return render(request, 'construction/blog.html', ctx)


def contact(request):
    model = For_Query()
    form = For_QueryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    ctx = {
        "contact": "active",


    }
    return render(request, 'construction/contact.html', ctx)


def single(request, project_id):
    model = Comments()
    form = CommenterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    tags = get_tags()
    blogs = get_blog()
    projects = get_projects()
    project = get_projects_by_id(project_id=project_id)
    comments=get_comments()
    comment_limit=get_commenter_by_limit()
    comment_length=len(comments)

    ctx = {
        "single": "active",
        "project": project,
        "tags": tags,
        "blogs": blogs,
        "projects": projects,
        "comments": comments,
        "comment_limit": comment_limit,
        "comment_length": comment_length,


    }
    return render(request, 'construction/single.html', ctx)
