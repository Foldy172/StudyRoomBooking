from django.db import models
from django.conf import settings
from django.utils import timezone

class Room(models.Model):
    number = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField()
    floor = models.IntegerField()
    equipment = models.ManyToManyField('Equipment', related_name='rooms', blank=True)

    class Meta:
        db_table = 'rooms'

class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'equipment'

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('approved', 'Подтверждено'),
        ('cancelled', 'Отменено'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    room = models.ForeignKey(Room, on_delete=models.RESTRICT, db_column='room_id')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bookings'

class PasswordResetToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column='user_id')
    token_hash = models.CharField(max_length=64, unique=True)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_reset_token'

    def is_valid(self):
        return self.used_at is None and self.expires_at > timezone.now()
