from django.contrib.auth.base_user import BaseUserManager
from django.http import JsonResponse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            return JsonResponse({'Error': 'Super user must have is_staff equals to True'})

        return self.create_user(email=email, password=password, **other_fields)
