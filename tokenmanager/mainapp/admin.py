from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Transaction, Request, Profile, Account, Asset, Wallet
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Profile)
admin.site.register(Request)
admin.site.register(Account)
admin.site.register(Asset)
admin.site.register(Wallet)
admin.site.register(Transaction)