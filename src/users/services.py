from django.db import transaction

from users.models import User


@transaction.atomic
def user_create(*, email: str, password: str, **extra_fields) -> User:
    """
    Creates and saves a new user.

    Args:
        email: The email address of the user.
        password: The user's password.
        extra_fields: Additional fields for the user model.

    Returns:
        The created User instance.
    """
    user = User(email=email, username=email, **extra_fields)
    user.set_password(password)

    user.full_clean()
    user.save()

    return user