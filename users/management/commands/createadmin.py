from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='testadmin@nert.ru',
            first_name='Adnin',
            last_name='Admin',
        )

        user.set_password('356645')

        user.is_staff = True
        user.is_superuser =True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'Администратор успешно создан {user.email}!'))