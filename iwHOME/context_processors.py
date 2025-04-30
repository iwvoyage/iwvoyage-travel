from post.models import Category, Tag

def sidebar_context(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # Add item_count to each for display
    for category in categories:
        category.item_count = category.post_set.count()
    for tag in tags:
        tag.item_count = tag.post_set.count()

    return {
        'categories': categories,
        'tags': tags,
        'category_url_name': 'post:posts_by_category',
        'tag_url_name': 'post:posts_by_tag',
    }
