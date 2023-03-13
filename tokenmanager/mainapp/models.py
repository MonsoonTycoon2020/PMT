from algosdk.constants import address_len, hash_len, max_asset_decimals, metadata_length
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.http import Http404
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .helpers import account_balance, account_transactions, passphrase_from_private_key


class Account(models.Model):
    """Base model class for standalone and wallet Algorand accounts."""

    address = models.CharField(max_length=address_len)
    private_key = models.CharField(max_length=address_len + hash_len)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def instance_from_address(cls, address):
        """Return model instance from provided account address."""
        try:
            return cls.objects.get(address=address)
        except ObjectDoesNotExist:
            raise Http404

    def balance(self):
        """Return this instance's balance in microAlgos."""
        return account_balance(self.address)

    @property
    def passphrase(self):
        """Return account's mnemonic."""
        return passphrase_from_private_key(self.private_key)

    def transactions(self):
        """Return all the transactions involving this account."""
        return account_transactions(self.address)

    def __str__(self):
        """Account's human-readable string representation."""
        return self.address


class Asset(models.Model):
    """Model class for Algorand assets."""

    asset_id = models.IntegerField(blank=False)
    creator = models.CharField(max_length=address_len, blank=False)
    name = models.CharField(max_length=hash_len, blank=True)
    unit = models.CharField(max_length=8, blank=True)
    total = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(1)],
    )
    decimals = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(max_asset_decimals)],
    )
    frozen = models.BooleanField(blank=False, default=False)
    url = models.URLField(blank=True)
    metadata = models.CharField(max_length=metadata_length, blank=True)
    manager = models.CharField(max_length=address_len, blank=True)
    reserve = models.CharField(max_length=address_len, blank=True)
    freeze = models.CharField(max_length=address_len, blank=True)
    clawback = models.CharField(max_length=address_len, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Asset's human-readable string representation."""
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(
        User, related_name="transactions", on_delete=models.DO_NOTHING
    )
    passphrase = models.CharField(max_length=200, default="")
    receiver = models.CharField(max_length=address_len, default="")
    sender = models.CharField(max_length=address_len, default="")
    amount = models.IntegerField(default="100000")
    asset_id = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=140, default="optional note")
    result = models.CharField(max_length=400, default='')

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.date:%Y-%m-%d %H:%M}): "
            f"{self.asset_id[:30]}..."
            f"{self.receiver[:5]}..."
            f"{self.amount}"
            f"{self.note}"
            f"{self.result[:100]}"
        )

class Profile(models.Model):
    """Model class for Profiles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()

class Request(models.Model):
    user = models.ForeignKey(
        User, related_name="requests", on_delete=models.DO_NOTHING
    )
    receiver = models.CharField(max_length=address_len, default="monsoon")
    amount = models.IntegerField(default="100000")
    body = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.date:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
            f"{self.receiver[:5]}..."
            f"{self.amount}"
        )
    
class Wallet(models.Model):
    """Model class for wallets."""

    wallet_id = models.CharField(max_length=hash_len)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def instance_from_id(cls, wallet_id):
        """Return model instance from provided wallet's ID."""
        try:
            return cls.objects.get(wallet_id=wallet_id)
        except ObjectDoesNotExist:
            raise Http404

    def __str__(self):
        """Wallet's human-readable string representation."""
        return self.name


class WalletAccount(Account):
    """Model class for accounts belonging to wallets."""

    wallet = models.ForeignKey(Wallet, default=None, on_delete=models.CASCADE)