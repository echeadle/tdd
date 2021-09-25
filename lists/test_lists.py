from django.test import TestCase

# Create your tests here.


class SmokeTest(TestCase):
    """Example Testcase for using django testcase"""

    def test_bad_maths(self):
        """Simple math testcase"""
        self.assertEqual(1 + 1, 3)