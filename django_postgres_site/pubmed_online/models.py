
from django.db import models

class PubmedArticle(models.Model):
    article_id = models.IntegerField(primary_key=True)
    title = models.TextField(null=False)
    journal_title = models.TextField(null=False)
    doi = models.CharField(max_length=500, null=False)
    pubmed_link = models.TextField(null=False)
    year = models.IntegerField(null=False)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'pubmed_article'
        ordering = ['journal_title']


class PubmedAffiliation(models.Model):
    affil_id = models.AutoField(primary_key=True)
    norm_affil = models.TextField(null=False)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'pubmed_affiliation'
class PubmedAuthor(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.TextField(null=False)
    affil_id = models.ForeignKey(PubmedAffiliation, on_delete=models.CASCADE)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'pubmed_author'

class ArticleAuthor(models.Model):
    article_id = models.ForeignKey(PubmedArticle, on_delete=models.CASCADE)
    author_id = models.ForeignKey(PubmedAuthor, on_delete=models.CASCADE)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'article_author'

class GrantInfo(models.Model):
    grant_id = models.AutoField(primary_key=True)
    grant_val = models.TextField(null=False)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'grant_info'

class ArticleGrant(models.Model):
    article_id = models.ForeignKey(PubmedArticle, on_delete=models.CASCADE)
    grant_id = models.ForeignKey(GrantInfo, on_delete=models.CASCADE)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'article_grant'

class ArticleCOI(models.Model):
    article_id = models.ForeignKey(PubmedArticle, on_delete=models.CASCADE)
    coi_id = models.AutoField(primary_key=True)
    coi_text = models.TextField(null=False)

    class Meta:
        # Set managed to False to inform Django not to manage this table
        managed = False
        # Set db_table to the name of your existing table
        db_table = 'article_coi'
