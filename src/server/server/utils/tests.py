from django.test.runner import DiscoverRunner
from django.test import TestCase


fixtures = ['user', 'alternativename', 'country', 'region', 'city', 'address', 'store', 'category', 'tag', 'brand', 'product', 'currency', 'price',
            'scrapedproduct', 'scraper', 'searchandreplace']

class BaseTestCase(TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)


class TestRunner(DiscoverRunner):

    def teardown_test_environment(self, *args, **kwargs):
        super(TestRunner, self).teardown_test_environment(*args, **kwargs)
