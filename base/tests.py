from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Resource, Progress


# Create your tests here.
class SettingsTestCase(TestCase):
    def setUp(self):
    	r = Resource()
    	r.title='test'
    	r.save()
    	u = User()
    	u.username='testuser'
    	u.save()

    def test_if_resource_assigned(self):
    	r = Resource.objects.first()
    	self.assertEqual(r.title,'test')
    	u = User.objects.first()
    	p = Progress()
    	p.resource = r
    	p.user = u
    	p.save()
    	self.assertEqual(p.user.username,'testuser')
    	p1=Progress.objects.get(user=u, resource=r)
    	self.assertEqual(p1.user.username,'testuser')
