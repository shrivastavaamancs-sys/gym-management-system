from django.contrib import admin
from .models import Trainer, Offer, Member, ContactMessage

admin.site.register(Trainer)
admin.site.register(Offer)
admin.site.register(Member)
admin.site.register(ContactMessage)