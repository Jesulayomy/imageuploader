from django.db import models

class Image(models.Model):
  photo = models.ImageField(upload_to="myimage")
  date = models.DateTimeField(auto_now_add=True)
  username = models.CharField(max_length=100, default="Anon")

  def to_dict(self):
    return {
      "photo": self.photo.url,
      "date": self.date,
      "username": self.username,
      "id": self.id,
    }
