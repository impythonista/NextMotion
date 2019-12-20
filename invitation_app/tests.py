import uuid
from faker import Faker

from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from invitation_app.models import Invitation

fake = Faker()


class InvitationAPIViewTestCases(APITestCase):
    """
    It's all the test cases of invitation api.
    """

    def setUp(self):
        self.username = 'nextmotion'
        self.email = 'nextmotion@example.com'
        self.password = 'password'

        self.user = User.objects.create(
            username=self.username, 
            email=self.email,
            password=make_password(self.password),
        )

        token = Token.objects.create(user=self.user)
        self.token = token.key
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        self.invitation = Invitation.objects.create(email= fake.email(), creator=self.user)

    def test_create_invitation(self):
        url = '/api/invitations/'
        email = fake.email()
        data = {'email': email}

        response = self.client.post(url, data, format='json')
        invitation_id = response.data['data']['id']

        self.assertEqual(response.data['status'], 201)
        self.assertEqual(response.data['message'], 'Successfully created invitation.')
        self.assertEqual(response.data['data']['email'], email)
        self.assertEqual(response.data['data']['used'], False)
    
    def test_invalid_email_address(self):
        url = '/api/invitations/'
        data = {'email': 'invalid@email'}

        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, 400)
    
    def test_patch_invitation(self):
        url = '/api/invitations/{0}/'.format(str(self.invitation.id))
        data = {'email': fake.email(), 'used' : True}

        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.data['message'], 'Successfully updated invitation.')
        self.assertEqual(response.data['data']['used'], True)
    
    def test_patch_invitation_invalid_id(self):
        url = '/api/invitations/{0}/'.format(str(uuid.uuid4()))
        data = {'email': fake.email(), 'used' : True}

        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.data['status'], 404)
        self.assertEqual(response.data['message'], 'Not found.')
    
    def test_patch_invitation_delete(self):
        url = '/api/invitations/{0}/'.format(str(self.invitation.id))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, 204)

