from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone

class Portfolio(models.Model):
    uid = models.URLField()
    templateid = models.URLField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="thumbnail/img/portfolios/")
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"

    def save(self, *args, **kwargs):
        # Update the updated_at field whenever the object is saved
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PortfolioTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="thumbnail/img/templates/")
    template_file = models.FileField(upload_to="thumbnail/json/template/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.name

 