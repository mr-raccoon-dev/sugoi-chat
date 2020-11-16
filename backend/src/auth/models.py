from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255)
    password = fields.CharField(max_length=255)

    def __str__(self):
        return self.username


class Token(Model):
    id = fields.IntField(pk=True)
    value = fields.CharField(max_length=255, unique=True)
    user = fields.ForeignKeyField('models.User', related_name='tokens')

    def __str__(self):
        return self.id
