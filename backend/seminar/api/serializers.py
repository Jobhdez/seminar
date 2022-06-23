from rest_framework import serializers
from arxiv.models import Paper

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['abstract',
                  'title',
                  'author',
                  'paper_url',
                  'published_date',
                  'subject',
                  'updated',
                  'pdf_url']
