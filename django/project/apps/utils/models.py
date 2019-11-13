from django.db.models import Model, BooleanField


# Base Model to project
class BaseModel(Model):
    available = BooleanField(default=True)

    def get_absolute_url(self):
        return self.getAbsoluteUrl()

    class Meta:
        abstract = True
