from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post
from django.contrib.auth.models import User
from .tasks import send_notification_email
print(User.objects.all())  # This should return a queryset of users
@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        print("Post created signal received")
        users = User.objects.all()
        for user in users:
            if user.email:
                print(f"Sending email to {user.email}")
                send_notification_email.delay(
                    user_email = user.email,
                    post_title = instance.title,
                )
                print(f"Email sent to {user.email}")