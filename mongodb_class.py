from mongoengine import *


class User(DynamicDocument):
    log_user = StringField(required=True)
    pass_user = StringField(required=True)


class Person(DynamicDocument):
    name = StringField()
    surname = StringField()
    otchestvo = StringField()
    age = IntField()
    dolgnost = StringField()
    photo = ImageField()
    search = IntField()


class Date(DynamicDocument):
    date = StringField()
    data = ListField(ListField(StringField()))
