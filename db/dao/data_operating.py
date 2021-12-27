from db.db_models.db_models import TestModel

test_model = TestModel(string='test_string1')
test_model.save()

test_model_data = [{'string': 'test_string2'}, {'string': 'test_string3'}]
TestModel.insert_many(test_model_data).execute()

