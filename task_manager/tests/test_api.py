# import json
#
# from django.contrib.auth.models import User
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from tmapp.models import UserTask
#
#
# class BooksApiTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='test_username')
#         self.task_1 = UserTask.objects.create(title='Test task 1',
#                                               description='Test description 1',
#                                               status='Planned',
#                                               deadline="2020-09-30T17:34:58.286316Z",
#                                               owner=self.user)
#
#         self.task_2 = UserTask.objects.create(title='Test task 2',
#                                               description='Test description 2',
#                                               status='New',
#                                               deadline="2020-09-30T17:34:58.286316Z",
#                                               owner=self.user)
#
#         self.task_3 = UserTask.objects.create(title='Test task 3',
#                                               description='Test description 3',
#                                               status='Completed',
#                                               deadline="2020-09-30T17:34:58.286316Z",
#                                               owner=self.user)
#
#     def test_create(self):
#         self.assertEqual(3, UserTask.objects.all().count())
#         url = reverse('usertask-list')
#         data = {
#             "title": "test",
#             "description": "test des",
#             "status": "In Progress",
#             "deadline": "2020-10-02T22:42:00Z",
#         }
#         json_data = json.dumps(data)
#         self.client.force_login(self.user)
#         print(self.user)
#         response = self.client.post(url, data=json_data,
#                                    content_type='application/json')
#
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#         self.assertEqual(4, UserTask.objects.alpl().count())
#         self.assertEqual(self.user, UserTask.objects.last().owner)
