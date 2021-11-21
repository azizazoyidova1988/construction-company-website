from django.db import connection
from contextlib import closing


def get_facts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from fact""")
        facts = dict_fetchall(cursor)
        return facts


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories


def get_projects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from project """)
        products = dict_fetchall(cursor)
        return products

def get_projects_by_id(project_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select project.*,project_author.name as author_name, 
        project_author.image as author_image, project_author.description as author_desc
         FROM project left join project_author on project.project_author_id = project_author.id  
          where project.id=%s """, [project_id])
        project = dict_fetchone(cursor)
        return project

def get_services():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from service""")
        services = dict_fetchall(cursor)
        return services

def get_tags():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from tags""")
        tags = dict_fetchall(cursor)
        return tags


def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial""")
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog""")
        blogs = dict_fetchall(cursor)
        return blogs


def get_video():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from video""")
        video = dict_fetchall(cursor)
        return video


def get_blog_single(blog_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog where blog.id = %s""", [blog_id])
        blog = dict_fetchone(cursor)
        return blog


def get_categories_product(category_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * FROM project WHERE category_id =  %s """, [category_id])
        product = dict_fetchall(cursor)
        return product


def get_team():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from engineer""")
        teams = dict_fetchall(cursor)
        return teams


def get_questions():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from question""")
        questions = dict_fetchall(cursor)
        return questions

def get_commenter_by_limit():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from comment order by created_at desc limit 3""" )
        comment = dict_fetchall(cursor)
        return comment

def get_comments():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from comment """)
        comments = dict_fetchall(cursor)
        return comments


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
