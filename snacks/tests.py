from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", email="tester@email.com", password="pass")

        self.snack = Snack.objects.create(title="cashews", purchaser=self.user, description="cashews description")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), "cashews")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "cashews")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "cashews description")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cashews")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Description")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "cashews",
                "purchaser": "tester",
                "description": self.user.id,
            }, follow=True,

        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cashews")
        # self.assertRedirects(response, reverse("snack_list"))

    def test_snack_update_bad_url(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "Updated title", "purchaser": self.user.id, "description": "test description"}
        )

        self.assertEqual(response.status_code, 302)

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

        # you can also tests models directly
    def test_model(self):
        snack = Snack.objects.create(title="cashews", purchaser=self.user)
        self.assertEqual(snack.title, "cashews")

