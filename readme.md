# PubMed Web application

---

> In this step, we must create a Web application that exposes the PubMed database content, as follows.


## Todo

---
Building on, and extending the Web application development lab, we need to write a Web application that allows to do the following:

1. Shows a start page with the distinct journals in which papers were published. As there are many journals, the start page is in fact a first page with the 200 journal titles in alphabetic order, having a “Next page” link at the bottom, which leads to the next page of 200 journal titles; this page should have a “Previous” and a “Next” page, etc., until the last page of at most 200 titles, which only has a “Previous” link. Using the Next and/or Previous links, it must be possible to navigate over all the journal titles. Each journal title should be a link to the journal’s page (see below).
2. When the user clicks on such a link, they should arrive on a journal page titled “Journal: journal name”. In this page, we should see a list, with an item for each different author that has published an article in this journal. The authors should appear in the alphabetic order of their names. Each author name should be a link (see below).
3. When the user clicks on such a link, they should arrive on an author page titled “Author: author name”. In this page, we should see a list of all the publications of this author, ordered first by the year (the most recent year first), and then by the journal name (in increasing alphabetic order). For each article, we should see:

   * The article title;
   * The year;
   * The link to the paper in Pubmed (pubmed_link field; this link should be clickable and lead to the respective Pubmed page);
   * The title of the journal (this should be a link to the journal page in your application (see 2. above);
   * The list of authors (each author name should be a link to the author page (see 3. above);
   * The grant information of the article (if any), e.g., the page may show: “Grant info: “
   followed by the text of the article grant information;
   * The conflict of interest information of the article (if any), e.g., the page may show: “Con- flict of interest: ” followed by the text of the conflict of interest information.

# What have we done:

---
1. We already had a local Pubmed database on Postgres. 
2. We spliced our database with Django's Web application development packages, using that package's models. 
3. Wrote all views, for our application to work correctly. 
4. And wrote three html files displaying our views. 
5. We also added special templatestags, as we were having problems with some magazine names during the layout process. 

# How to launch this project on your local machine.

---
If you already have a Pubmed database, you only need to change the configuration (host, database, username, password and port) in `django_postgres_site/django_postgres_site/settings.py` and `django_postgres_site/pubmed_online/views.py`
By default password = ''''. 

If not we provide you our db with all necessary files (we hope so).

Once you have configured the database you need to do the following: 
> python3 manage.py makemigrations

> python3 manage.py migrate
 
> python3 manage.py runserver   

``Enjoy!``