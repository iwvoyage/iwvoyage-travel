from django.core.mail import send_mail

send_mail(
    subject="Test Email from Django",
    message="Hello! This is a test from iwVoyage.",
    from_email="luis@iwvoyage.com",
    recipient_list=["luis@iwvoyage.com"],  # replace with your email
    fail_silently=False,
)


<!-- Explore Cities -->
<div class="sidebar-box fadeIn">
  {% if destination.cities.all %}
    <h3 class="heading">Explore Cities</h3>
    <ul>
      {% for city in destination.cities.all %}
        <li>
          <a href="{% url 'cities:city_detail' destination.slug city.slug %}">{{ city.name }}</a>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</div>


________________________________________________


City detail is not displaying the info. only the hero is displaying. here is the html, model, view. fix the html and give me the whole code back.
{% extends "base.html" %}
{% load static %}

{% block content %}

<style>
  .site-cover {
    background-image: url('{{ city.hero.url }}');
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
  }

  @media (max-width: 767px) {
    .site-cover {
      background-image: url('{{ city.hero.url }}');
    }
  }

  .site-cover.overlay:before {
    background: rgba(0, 0, 0, 0.5);
    position: absolute;
    content: "";
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1;
  }

  .tag-container {
    margin-top: 1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .tag-box {
    display: inline-block;
    padding: 0.4rem 0.75rem;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 0.9rem;
    color: #333;
    text-decoration: none;
    transition: all 0.2s ease-in-out;
  }

  .tag-box:hover {
    background-color: #3fd0d4;
    color: white;
    border-color: #3fd0d4;
  }
</style>

<title>Blogy &mdash; Free Bootstrap 5 Website Template by Untree.co</title>
</head>

<body>

  <div class="site-mobile-menu site-navbar-target">
    <div class="site-mobile-menu-header">
      <div class="site-mobile-menu-close">
        <span class="icofont-close js-menu-toggle"></span>
      </div>
    </div>
    <div class="site-mobile-menu-body"></div>
  </div>

  {% include 'menu.html' %}

  <div class="site-cover site-cover-sm same-height overlay single-page">
    <div class="container">
      <div class="row same-height justify-content-center">
        <div class="col-md-6" data-aos="fade-up">
          <div class="post-entry text-center">
            <h1 class="mb-4" style="margin-top: 20%;">{{ city.name }}</h1>
            <div class="post-meta align-items-center text-center"></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="container">

      <div class="row blog-entries element-animate">

        <div class="col-md-12 col-lg-8 main-content" data-aos="fade-up">
          <div class="post-content-body">
            <h2>{{ city.header|safe }} </h2>
            <p>{{ city.body|safe }} </p>

            <h3>{{ city.subheader|safe }} </h3>
            <p>{{ city.description|safe }} </p>

            <hr style="margin-top: 50px;">

            <div class="row my-4">
              {% if city.image %}
              <div class="col-md-6 mb-4" data-aos="fade-up">
                <img src="{{ city.image.url }}" alt="Image 1" class="img-fluid rounded">
              </div>
              {% endif %}
              {% if city.image2 %}
              <div class="col-md-6 mb-4" data-aos="fade-up">
                <img src="{{ city.image2.url }}" alt="Image 2" class="img-fluid rounded">
              </div>
              {% endif %}
              {% if city.image3 %}
              <div class="col-md-12 mb-4" data-aos="fade-up">
                <img src="{{ city.image3.url }}" alt="Image 3" class="img-fluid rounded">
              </div>
              {% endif %}
            </div>

            <h3>{{ city.subheader_one|safe }} </h3>
            <p>{{ city.description_one|safe }} </p>

            <h3>{{ city.subheader_two|safe }} </h3>
            <p>{{ city.description_two|safe }}</p>
          </div>

          <div class="row my-4">
            {% if city.image4 %}
            <div class="col-md-6 mb-4" data-aos="fade-up">
              <img src="{{ city.image4.url }}" alt="Image 4" class="img-fluid rounded">
            </div>
            {% endif %}
            {% if city.image5 %}
            <div class="col-md-6 mb-4" data-aos="fade-up">
              <img src="{{ city.image5.url }}" alt="Image 5" class="img-fluid rounded">
            </div>
            {% endif %}
          </div>

          <h3>{{ city.subheader_three|safe }} </h3>
          <p>{{ city.description_three|safe }} </p>

          <h3>Ready to Experience the Magic of the {{ city.country }}?</h3>
          <p>Start planning your island adventure today and uncover the natural wonders, rich heritage, and warm hospitality that make the {{ destination.country }} a top travel destination.</p>
          <h4>Book your trip now and let the journey begin!</h4>

          <div class="pt-2 comment-wrap"></div>
        </div>

        <div class="col-md-12 col-lg-4 sidebar" data-aos="fade-up">
          <div class="sidebar-box">
            <div class="bio text-center">
              <img src="{% static 'assets/images/rachel-ann.jpg' %}" alt="Rachel Ann Deborja" class="img-fluid mb-3 rounded-circle">
              <div class="bio-body">
                <h2 class="h5">Rachel Ann Deborja</h2>
                <p class="mb-4">
                  At iwVoyage, our team is a passionate group of seasoned travelers and dedicated customer service professionals.
                </p>
                <p><a href="{% url 'about:about_page' %}" class="btn btn-primary btn-sm rounded px-3 py-2">Read My Bio</a></p>
                <p class="social">
                  <a href="#" class="p-2"><span class="fa fa-facebook"></span></a>
                  <a href="#" class="p-2"><span class="fa fa-twitter"></span></a>
                  <a href="#" class="p-2"><span class="fa fa-instagram"></span></a>
                  <a href="#" class="p-2"><span class="fa fa-youtube-play"></span></a>
                </p>
              </div>
            </div>
          </div>

          <div class="sidebar-box">
            <h3 class="heading">What's Trending</h3>
            <div class="post-entry-sidebar">
              <ul>
                {% for trend in trends %}
                <li>
                  <a href="{{ trend.link }}">
                    <img src="{{ trend.image.url }}" class="me-4 rounded" alt="{{ trend.title }}">
                    <div class="text">
                      <h4>{{ trend.title|truncatechars:50 }}</h4>
                      <div class="post-meta">
                        <span class="mr-2">{{ trend.location }}</span>
                      </div>
                    </div>
                  </a>
                </li>
                {% endfor %}
              </ul>
            </div>
          </div>

          <div class="sidebar-box">
            <h3 class="heading">Categories</h3>
            <ul class="categories">
              {% for category in categories %}
              <li><a href="{% url 'post:posts_by_category' category.slug %}">{{ category.name }} ({{ category.post_set.count }})</a></li>
              {% endfor %}
            </ul>
          </div>

          <div class="sidebar-box">
            <h3 class="heading">Tags</h3>
            <div class="tag-container">
              {% for tag in tags %}
              <a href="{% url 'post:posts_by_tag' tag.slug %}" class="tag-box">{{ tag.name }}</a>
              {% endfor %}
            </div>
          </div>

          <div class="sidebar-box">
            <h3 class="heading">Sponsored</h3>
            {% for banner in banners %}
            <div class="mb-3 text-center">
              <a href="{{ banner.link }}" target="_blank">
                <img src="{{ banner.image.url }}" class="img-fluid mb-1" alt="{{ banner.title }}">
                <p class="small text-muted" style="font-size: 18px; margin-top: 15px;">{{ banner.title }}</p>
              </a>
              <a href="{{ banner.link }}" class="btn btn-outline-head" style="margin-top: 15px;">Book Tour</a>
            </div>
            {% empty %}
            <p>No ads available.</p>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section posts-entry posts-entry-sm bg-light">
    <div class="container">
      <div class="row mb-4" data-aos="fade-up">
        <div class="col-12 text-uppercase text-black">More Blog Posts</div>
      </div>
      <div class="row">
        {% for post in latest_posts %}
        <div class="col-md-6 col-lg-3" data-aos="fade-up">
          <div class="blog-entry">
            <a href="{% url 'post:post_detail' post.slug %}" class="img-link">
              {% if post.image_hero %}
              <img src="{{ post.image_hero.url }}" alt="{{ post.title }}" class="img-fluid">
              {% else %}
              <img src="{% static 'images/placeholder.jpg' %}" alt="Placeholder" class="img-fluid">
              {% endif %}
            </a>
            <span class="date">{{ post.created_at|date:"M. jS, Y" }}</span>
            <h2><a href="{% url 'post:post_detail' post.slug %}">{{ post.title|truncatechars:50 }}</a></h2>
            <p>{{ post.body|striptags|truncatechars:100 }}</p>
            <p><a href="{% url 'post:post_detail' post.slug %}" class="read-more">Continue Reading</a></p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>

{% endblock %}


from django.shortcuts import render, get_object_or_404
from .models import City
from destinations.models import Destination
from post.models import Post, Category, Tag  # ✅ Add Category and Tag
from adbanner.models import AdBanner  # 👈 Import the model
from index.models import Trend  # or whatever your model is called

def city_list(request, destination_slug):
    destination = get_object_or_404(Destination, slug=destination_slug)
    cities = destination.cities.all()
    return render(request, 'cities/city_list.html', {
        'destination': destination,
        'cities': cities
    })


def city_detail(request, destination_slug, city_slug):
    destination = get_object_or_404(Destination, slug=destination_slug)
    city = get_object_or_404(City, slug=city_slug, destination=destination)
    latest_posts = Post.objects.order_by('-created_at')[:4]
    banners = AdBanner.objects.all()
    trends = Trend.objects.all()[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'cities/city_detail.html', {
        'destination': destination,
        'city': city,
        'latest_posts': latest_posts,
        'trends': trends,
        'banners': banners,
        'categories': categories,  # ✅ Add to context
        'tags': tags,              # ✅ Add to context
    })


    from django.db import models
from django.utils.text import slugify
from destinations.models import Destination
from django_ckeditor_5.fields import CKEditor5Field

class City(models.Model):
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='cities',
        default=1
    )
    name = models.CharField(max_length=255, default='Unnamed Destination')
    slug = models.SlugField(unique=True, default='default-slug')
    header = models.CharField(max_length=255, default='Unnamed Destination')
    body = CKEditor5Field('body', config_name='default')
    subheader= models.CharField(max_length=255, default='Unnamed Destination')
    description = CKEditor5Field('description', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_one= models.CharField(max_length=255, default='Unnamed Destination')
    description_one = CKEditor5Field('description_one', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_two= models.CharField(max_length=255, default='Unnamed Destination')
    description_two = CKEditor5Field('description_two', blank=True, null=True, default='')  # ✅ Fixed comma
    subheader_three= models.CharField(max_length=255, default='Unnamed Destination')
    description_three = CKEditor5Field('description_three', blank=True, null=True, default='')  # ✅ Fixed comma
    hero = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image2 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image3 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image4 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)
    image5 = models.ImageField(upload_to='destinations/', blank=True, null=True, default=None)


    def __str__(self):
        return f"{self.name} ({self.destination.header})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
_________________________--

