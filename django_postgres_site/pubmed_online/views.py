# Importing necessary packages

import psycopg2
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote_plus, unquote_plus
from django.shortcuts import render
from .models import PubmedArticle


host = "localhost"
database = "pubmed"
user = "sanek_tarasov"
password = ""
port = 5432


def journal_list(request):
    all_journals = PubmedArticle.objects.values('journal_title').distinct().order_by('journal_title')
    # print(all_journals)

    # Configure pagination
    paginator = Paginator(all_journals, 200)
    page = request.GET.get('page', 1)

    try:
        journals = paginator.page(page)
    except PageNotAnInteger:
        journals = paginator.page(1)
    except EmptyPage:
        journals = paginator.page(paginator.num_pages)

    # print(journals.object_list)
    return render(request, 'pubmed_online/journal_list.html', {'journals': journals})

def journal_page(request, journal_title):
    con = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)
    journal_title = unquote_plus(journal_title)
    query_titles = """SELECT DISTINCT
                            pauth.author_name
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pa.journal_title = %s
                        ORDER BY
                            pauth.author_name;"""
    with con.cursor() as cur:
        cur.execute(query_titles, (journal_title,))
        authors = cur.fetchall()
    authors = [authors[i][0] for i in range(len(authors))]
    # print(authors)
    return render(request, 'pubmed_online/journal_page.html', {'journal_title': journal_title, 'authors': authors})

def author_page(request, author_name):
    con = psycopg2.connect(host=host, database=database, user=user, password=password, port=port)

    query_titles = """SELECT DISTINCT pa.title, pa.year, pa.pubmed_link, pa.journal_title
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pauth.author_name = %s
                        ORDER BY
                            pa.year;"""

    query_authors = """SELECT pa.title, pauth.author_name
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pa.title IN (SELECT DISTINCT pa.title
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pauth.author_name = %s);"""

    query_grant = """SELECT DISTINCT pa.title, ginfo.grant_val
                        FROM
                            pubmed_article pa
                        JOIN
                            article_grant agrant ON pa.article_id = agrant.article_id
                        JOIN
                            grant_info ginfo ON agrant.grant_id = ginfo.grant_id
                        WHERE
                            pa.title IN (SELECT DISTINCT pa.title
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pauth.author_name = %s);"""

    query_coi = """SELECT DISTINCT pa.title, acoi.coi_text
                        FROM
                            pubmed_article pa
                        JOIN
                            article_coi acoi ON pa.article_id = acoi.article_id
                        WHERE
                            pa.title IN (SELECT DISTINCT pa.title
                        FROM
                            pubmed_article pa
                        JOIN
                            article_author aauth ON pa.article_id = aauth.article_id
                        JOIN
                            pubmed_author pauth ON aauth.author_id = pauth.author_id
                        WHERE
                            pauth.author_name = %s);"""

    with con.cursor() as cur:
        cur.execute(query_titles, (author_name,))
        articles = cur.fetchall()

        cur.execute(query_coi, (author_name,))
        coi_info = cur.fetchall()

        cur.execute(query_grant, (author_name,))
        grant_info = cur.fetchall()

        cur.execute(query_authors, (author_name,))
        author_names = cur.fetchall()
        # print(author_names)

    journals_list_encoded = [
        (journal_tuple[0], journal_tuple[1], journal_tuple[2], journal_tuple[3], quote_plus(journal_tuple[3])) for
        journal_tuple in articles]

    context = {
        'author_name': author_name,
        'articles': articles,
        'coi_info': coi_info,
        'grant_info': grant_info,
        'author_names': author_names,
        'journals_list_encoded': journals_list_encoded,
    }


    return render(request, 'pubmed_online/author_page.html', context)