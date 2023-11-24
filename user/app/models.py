import uuid

import bcrypt
from tortoise.fields import (
    IntField,
    CharField, ManyToManyField, OneToOneField, UUIDField, BooleanField, BinaryField, ForeignKeyField,
)

from app.abstracts import (
    TimesBaseModel, RatingBaseModel, TypeBaseModel
)
from app.config import default_db_values
from app.types import Temail, Tuuid
from app.utils.password import generate_password


class Profile(TimesBaseModel):
    """Модель профиля."""

    work = CharField(max_length=100, default=default_db_values['profile']['work'])
    sex = CharField(max_length=100, default=default_db_values['profile']['sex'])
    age = IntField(default=default_db_values['profile']['age'])
    education = CharField(max_length=100, default=default_db_values['profile']['education'])
    hobby = CharField(max_length=100, default=default_db_values['profile']['hobby'])
    quote = CharField(max_length=180, default=default_db_values['profile']['quote'])
    phone = CharField(max_length=11, default=default_db_values['profile']['phone'])
    country = CharField(max_length=100, default=default_db_values['profile']['country'])
    website = CharField(max_length=100, default=default_db_values['profile']['website'])

    class Meta:
        """Класс с метаданными полями."""

        table = "profile"


class Rating(RatingBaseModel):
    """Модель рейтинга."""

    # override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    # override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    # override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = "rating"


class RatingPerWeek(RatingBaseModel):
    """Модель рейтинга по неделям."""

    # override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    # override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    # override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = "rating_per_week"


class RatingPerMonth(RatingBaseModel):
    """Модель рейтинга по месяцам."""

    # override
    async def add_score(self, score):
        """Метод для добавления баллов."""
        pass

    # override
    async def update_score(self, score):
        """Метод для обновления баллов."""
        pass

    # override
    async def remove_score(self, score):
        """Метод для удаления баллов."""
        pass

    class Meta:
        """Класс с метаданными полями."""

        table = "rating_per_month"


class NotificationType(TypeBaseModel):
    """Модель типа уведомления."""

    class Meta:
        """Класс с метаданными полями."""

        table = "notification_type"


class Notification(TimesBaseModel):
    """Модель уведомления."""

    title = CharField(max_length=100)
    description = CharField(max_length=100)
    notification_type = ForeignKeyField("models.NotificationType")

    class Meta:
        """Класс с метаданными полями."""

        table = "notification"


class EmailValidation(TimesBaseModel):
    """Модель валидации почты."""

    code = CharField(max_length=40)
    done = BooleanField(default=default_db_values['email_validation']['done'])

    class Meta:
        table = 'email_validation'


class AuthTypeProvider(TimesBaseModel):
    title = CharField(max_length=30)

    class Meta:
        table = 'auth_type_provider'


class AuthType(TimesBaseModel):
    type = ForeignKeyField('models.AuthTypeProvider')
    user_id = IntField(null=True)

    class Meta:
        unique_together = ('type', 'user_id')
        table = 'auth_type'


class User(TimesBaseModel):
    """Модель пользователя."""

    username = CharField(max_length=30, unique=True)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    password = BinaryField(null=True)
    email = CharField(max_length=30, unique=True)
    email_validated = BooleanField(default=False)
    uuid = UUIDField(default=uuid.uuid4, unique=True)

    profile = OneToOneField("models.Profile")
    rating = OneToOneField("models.Rating")
    rating_per_week = OneToOneField("models.RatingPerWeek")
    rating_per_month = OneToOneField("models.RatingPerMonth")

    notifications = ManyToManyField("models.Notification")
    emails = ManyToManyField("models.EmailValidation")

    auth_type = OneToOneField('models.AuthType')

    async def set_password(self, password: str) -> bool:
        """Функция для изменения пароля пользователя."""
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        self.password = password
        return True

    async def check_password(self, password: str) -> bool:
        """Функция для проверки пароля пользователя."""
        result = bcrypt.checkpw(password.encode("utf-8"), self.password)
        if result:
            return True
        return False

    async def validate_mail(self, change: bool = True) -> bool:
        """Функция валидации почты"""
        self.email_validated = True
        if change:
            self.uuid = uuid.uuid4()
        return True

    async def reset_password(self) -> str:
        """Функция востановления пароля."""
        password = await generate_password()
        await self.set_password(password)
        return password

    async def get_data_for_validate_email(self) -> (Temail, Tuuid):
        """Функция для получения информации для подтверждения почты."""
        return self.email, self.uuid

    async def get_profile(self):
        profile = await self.profile.get()
        return {
            'work': profile.work,
            'sex': profile.sex,
            'age': profile.age,
            'education': profile.education,
            'hobby': profile.education,
            'quote': profile.quote,
            'phone': profile.phone,
            'country': profile.country,
            'website': profile.website
        }

    async def json(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'pprofile': await self.get_profile()
        }

    class Meta:
        """Мета класс."""
        table = 'user'
        unique_together = ('email', 'username', 'uuid')
