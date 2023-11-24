import tortoise


class Log(tortoise.Model):
    time_created = tortoise.fields.DatetimeField(auto_now=True)
    project = tortoise.fields.CharField(max_length=100)
    service = tortoise.fields.CharField(max_length=100)
    level = tortoise.fields.CharField(max_length=20)
    message = tortoise.fields.CharField(max_length=300)
    code = tortoise.fields.IntField(default=0)