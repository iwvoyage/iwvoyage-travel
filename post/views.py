from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category, Tag
from adbanner.models import AdBanner
from index.models import Trend


def post_list_view(request):
    posts = Post.objects.order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]

    for category in categories:
        category.item_count = category.post_set.count()
    for tag in tags:
        tag.item_count = tag.post_set.count()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'category_url_name': 'post:posts_by_category',
        'tag_url_name': 'post:posts_by_tag',
        'banners': banners,
        'trends': trends,
    })


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]

    return render(request, 'post/post_detail.html', {
        'post': post,
        'banners': banners,
        'trends': trends,
    })


def posts_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category).order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]

    for cat in categories:
        cat.item_count = cat.post_set.count()
    for tag in tags:
        tag.item_count = tag.post_set.count()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'active_category': category,
        'banners': banners,
        'trends': trends,
        'category_url_name': 'post:posts_by_category',
        'tag_url_name': 'post:posts_by_tag',
    })


def posts_by_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag).order_by('-created_at')
    categories = Category.objects.all()
    tags_list = Tag.objects.all()
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]

    for cat in categories:
        cat.item_count = cat.post_set.count()
    for tag_item in tags_list:
        tag_item.item_count = tag_item.post_set.count()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'post/post_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags_list,
        'active_tag': tag,
        'banners': banners,
        'trends': trends,
        'category_url_name': 'post:posts_by_category',
        'tag_url_name': 'post:posts_by_tag',
    })
