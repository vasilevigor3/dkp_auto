from peewee import Model, AutoField, TextField

from db.db_conn import conn


class BaseModel(Model):
    class Meta:
        database = conn


class TestModel(BaseModel):
    test_model_id = AutoField(column_name='id')
    string = TextField(column_name='String', null=True)

    class Meta:
        table_name = 'mytable'
