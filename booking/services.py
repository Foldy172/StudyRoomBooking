import hashlib
import secrets
from datetime import timedelta
from django.utils import timezone
from .models import PasswordResetToken

def create_reset_token(user):
    raw_token = secrets.token_urlsafe(32)
    token_hash = hashlib.sha256(raw_token.encode('utf-8')).hexdigest()
    
    PasswordResetToken.objects.create(
        user=user,
        token_hash=token_hash,
        expires_at=timezone.now() + timedelta(minutes=30),
    )
    return raw_token
