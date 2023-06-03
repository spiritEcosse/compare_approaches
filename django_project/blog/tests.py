from django.test import TestCase

import django

from django_project.blog.models import Blog


class DjangoValuesList(TestCase):

    def test_values_list_and_all_compare(self):
        Blog.objects.values_list("id", "name")
