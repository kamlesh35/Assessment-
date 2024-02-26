from django.test import TestCase
from rest_framework.test import APIClient

# Create your tests here.


class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        # Write your test case to create an invoice via API
        pass

    def test_create_invoice_detail(self):
        # Write your test case to create an invoice detail via API
        pass

    # Add more test cases as needed