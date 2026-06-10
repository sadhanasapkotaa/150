from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email must be present!")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, phone, **kwargs):
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("User must be staff")
        if kwargs.get("is_active") is not True:
            raise ValueError("User must be active")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("User must be superuser")

        return self.create_user(email, password, **kwargs)
