from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	posted_date = models.DateTimeField(default=timezone.now)
	authore = models.ForeignKey(User, on_delete=models.CASCADE)

	# override methods #
	def __str__(self):
		return "• {} By {}. ".format(self.title, self.authore)
