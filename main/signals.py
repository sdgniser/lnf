from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item
import requests

from django.conf import settings

DISCORD_WEBHOOK_URL = settings.DISCORD_WEBHOOK_URL


@receiver(post_save, sender=Item)
def notify_discord_on_item_change(sender, instance, created, **kwargs):
    if created:
        title = f"New {instance.kind} Item Reported!"
    else:
        title = f"{instance.kind} Item Updated!"

    embed = {
        "title": title,
        "description": instance.desc,
        "color": 0x1abc9c if instance.kind == "Found" else 0xe74c3c,  # Green for Found, Red for Lost
        "fields": [
            {"name": "Category", "value": instance.category, "inline": True},
            {"name": "Location", "value": instance.location, "inline": True},
            {"name": "Date", "value": instance.date.strftime("%A, %d %B %Y"), "inline": False},
            {"name": "Claimed", "value": "Yes" if instance.claimed else "No", "inline": True},
            {"name": "Submitter", "value": instance.submitter, "inline": True},
            {"name": "Email", "value": instance.email, "inline": False},
        ],
        "footer": {
            "text": f"Submitted on {instance.created.strftime('%A, %d %B %Y %I:%M %p')}"
        },
    }

    # Add image if available
    if instance.image:
        embed["thumbnail"] = {"url": instance.image.url}  # Ensure the image URL is accessible from the internet

    data = {
        "embeds": [embed],
    }

    # Send the embed message to Discord
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Discord: {e}")
