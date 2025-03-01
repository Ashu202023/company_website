from django.test import SimpleTestCase
from django.urls import  reverse


class HomePageTest(SimpleTestCase):
    def test_url_exist(self):
        r=self.client.get("/")
        self.assertEqual(r.status_code,200)
    
    def test_by_url_name(self):
        r=self.client.get(reverse("home"))
        self.assertEqual(r.status_code,200)

    def test_template_name(self):
        r=self.client.get(reverse("home"))
        self.assertTemplateUsed(r,"home.html")
    
    def test_template_content(self):
        r=self.client.get(reverse("home"))
        self.assertContains(r,"<h1>Comapny Homepage</h1>")

class AboutPageTest(SimpleTestCase):
    def test_url_location(self):
        r=self.client.get("/about/")
        self.assertEqual(r.status_code,200)

    def test_url_location_by_name(self):
        r=self.client.get(reverse("about"))
        self.assertEqual(r.status_code,200)
    
    def test_template_used(self):
        r=self.client.get(reverse("about"))
        self.assertTemplateUsed(r,"about.html")
    
    def test_content_used(self):
        r=self.client.get(reverse("about"))
        self.assertContains(r,"<h1>Company About Page</h1>")
