import random
import string
from django.db import models


# Create your models here.
class Password(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_password_and_save(
        self, length, use_lowercase, use_uppercase, use_digits, use_special
    ):
        characters = ""

        if use_lowercase:
            characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        self.content = "".join(random.choice(characters) for _ in range(length))
        self.save()

        return self.content
