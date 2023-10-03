from django.test import SimpleTestCase
from django.urls import reverse , resolve
from home.views import home , about , contact 
from blog.views import blog , todo , post_detail
import json

class TestUrls(SimpleTestCase) :

    def test_bloglist_url_resolve(self):
        url = reverse('blog:blog')
        self.assertEquals(resolve(url).func , blog)

    def test_todo_url_resolve(self):
        url = reverse('blog:todo')
        self.assertEquals(resolve(url).func , todo)

    def test_detail_url_resolve(self):
        url = reverse('blog:detail',args=['1'])
        self.assertEquals(resolve(url).func , post_detail)

    def test_home_url_resolve(self):
        url = reverse('home:home')
        self.assertEquals(resolve(url).func , home)

    def test_about_url_resolve(self):
        url = reverse('home:about')
        self.assertEquals(resolve(url).func , about)

    def test_contact_url_resolve(self):
        url = reverse('home:contact')
        self.assertEquals(resolve(url).func , contact)