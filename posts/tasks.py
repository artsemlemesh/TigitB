from celery import shared_task
from django.core.mail import send_mail
from .models import Post
from django.db.models.functions import Length

@shared_task
def send_notification_email(user_email, post_title):
    send_mail(
        f'New post title: {post_title}',
        'A new post has been added',
        'artem.lems@yandex.ru',
        [user_email],
        fail_silently=False,
    )

@shared_task
def cleanup_test_posts():
    #posts with title or content less than 10 char 
    short_posts = Post.objects.annotate(
        title_length=Length('title'),
        content_length=Length('content')
    ).filter(title_length__lt=5) | Post.objects.annotate(
        content_length=Length('content')
    ).filter(content_length__lt=10)
    print(f"Short posts found for deletion: {[post.title for post in short_posts]}")

    deleted_count, _ = short_posts.delete()
    return f'Deleted {deleted_count} short posts'