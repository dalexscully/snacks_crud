from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", email="tester@email.com", password="pass")

        self.new_snack = Snack.objects.create(
            name="Cheetos",
            description="cheetos description",
            purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.new_snack), "Cheetos")

    def test_new_snack_content(self):
        self.assertEqual(f"{self.new_snack.name}", "Cheetos")
        self.assertEqual(f"{self.new_snack.purchaser}", "tester")
        self.assertEqual(f"{self.new_snack.description}", "cheetos description")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cheetos")
        self.assertTemplateUsed(response, "snacks/base.html")
        self.assertTemplateUsed(response, "snacks/snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snacks/base.html")
        self.assertTemplateUsed(response, "snacks/snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Doritos",
                "description": "doritos description",
                "purchaser": self.user.id,
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snack_list"))

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name", "description": "new description", "purchaser": self.user.id},
        )
        self.assertRedirects(response, reverse("snack_list"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
