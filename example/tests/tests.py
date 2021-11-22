"""Unit Tests for the Example module"""

import logging

from django.test import TestCase

LOGGER = logging.getLogger(name="example")


class ExampleTestCase(TestCase):
    """Test Case for Social Profile"""

    def setUp(self):
        """Set up common assets for tests"""
        LOGGER.debug("Example Tests setUp")

    def tearDown(self):
        """Remove Test Data"""
        LOGGER.debug("Example Tests tearDown")

    def test_admin_urls(self):
        """Test that redirects kicking in when trying to go to secure page."""
        LOGGER.debug("Example Test Redirect URLs")
        response = self.client.get("/admin/", follow=True)
        self.assertRedirects(response, "http://testserver/admin/login/?next=/admin/")
