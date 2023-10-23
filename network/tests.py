from . models import Post,Network,User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status



class PostTestCase(APITestCase):

    """
    Test suite for Contact
    """
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testUser", email="testUser@email.com", password="testUser")
        self.client.login(username="testUser" ,  password="testUser")
        # self.data = {
        #     "name": "Billy Smith",
        #     "message": "This is a test message",
        #     "email": "billysmith@test.com"
        # }
        # self.url = "/contact/"

    def test_User_api(self):
        id = self.user.id
        url = f"/api/user/{id}/"
        p= Post(owner=self.user , text="text")
        p.save()
        response = self.client.get(url)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().text, "text")
