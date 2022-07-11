from django.db import models

class Paper(models.Model):
    """
    Model of the research paper that will be manipulated in the frontend.
    """
    abstract = models.TextField()
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    paper_url = models.CharField(max_length=1000)
    published_date = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    updated = models.CharField(max_length=250)
    pdf_url = models.CharField(max_length=1000)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title

class LinearAlgebra(models.Model):
    """Model of the linear algebra expression."""
    
    expression = models.TextField()
