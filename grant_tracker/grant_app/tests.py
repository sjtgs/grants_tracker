from django.test import TestCase
from grant_app.models import Category, Priority, Grant_Management


class CategoryTestCase(TestCase):
    def setUp(self):
        # create some test data
        Category.objects.create(category_name="Books")

    def test_category_model(self):
        # retrieve the test data
        my_model = Category.objects.get(category_name="Books")

        # check that the data was created correctly
        self.assertEqual(my_model.category_name, "Books")


class PriorityTestCase(TestCase):
    def setUp(self):
        # create some test data
        Priority.objects.create(priority_name="Books")

    def test_priority_model(self):
        # retrieve the test data
        my_model = Priority.objects.get(priority_name="Books")

        # check that the data was created correctly
        self.assertEqual(my_model.priority_name, "Books")


class Grant_ManagementTestCase(TestCase):
    def setUp(self):
        # create some test data
        category = Category.objects.create(category_name="Books")
        priority = Priority.objects.create(priority_name="Ibex")

        Grant_Management.objects.create(
            item="science",
            category=category,
            priority=priority,
            Foundation="Great Heights",
            Amount_Requested=1000,
            Amount_Received=900,
            Purpose="Interior Design",
            POC_NAME="Joshua",
            Email="a@a.com",
            Phone="123",
        )

    def test_item_model(self):
        # retrieve the test data
        category = Category.objects.get(category_name="Books")
        priority = Priority.objects.get(priority_name="Ibex")

        my_model = Grant_Management.objects.get(
            item="science",
            category=category,
            priority=priority,
            Foundation="Great Heights",
            Amount_Requested=1000,
            Amount_Received=900,
            Purpose="Interior Design",
            POC_NAME="Joshua",
            Email="a@a.com",
            Phone="123",
        )

        # check that the data was created correctly
        self.assertEqual(my_model.item, "science")
        self.assertEqual(my_model.category.category_name, "Books")
        self.assertEqual(my_model.priority.priority_name, "Ibex")
        self.assertEqual(my_model.Foundation, "Great Heights")
        self.assertEqual(my_model.Amount_Requested, 1000)
        self.assertEqual(my_model.Amount_Received, 900)
        self.assertEqual(my_model.Purpose, "Interior Design")
        self.assertEqual(my_model.POC_NAME, "Joshua")
        self.assertEqual(my_model.Email, "a@a.com")
        self.assertEqual(my_model.Phone, "123")
