import requests
from django.core.management.base import BaseCommand
from ...models import Paper
from ...aux import get_research_papers

url = 'http://export.arxiv.org/api/query?search_query=cat:cs.PL&max_results=500'

def seed(url):
    """
    Adds the rsearch papers to the database.
    """
    for paper in get_research_papers(url):
        
        if isinstance(paper['author'], dict):
            authors_name = paper['author']['name']
        else:
            authors_name = paper['author'][0]['name']
            
        pl_paper = Paper(abstract = paper['summary'],
                         title = paper['title'],
                         author = authors_name,
                         paper_url = paper['link'][0]['@href'],
                         published_date = paper['published'],
                         subject =  paper['arxiv:primary_category']['@term'],
                         updated = paper['updated'],
                         pdf_url = paper['link'][1]['@href'],)
        pl_paper.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        seed(url)
        print("\nSeeding Completed.")
