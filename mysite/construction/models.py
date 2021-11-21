from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.name


class Questions(models.Model):
    question = models.CharField(max_length=150, blank=False, null=False)
    answer = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "question"

    def __str__(self):
        return self.question


class Facts(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    fact = models.IntegerField(blank=False, null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "fact"

    def __str__(self):
        return self.name


class Engineer(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    job = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "engineer"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Project_Author(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project_author"

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description_1 = models.CharField(max_length=450, blank=False, null=False)
    description_2 = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    project_author = models.ForeignKey(Project_Author, blank=False, null=True,on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    job = models.CharField(max_length=450, blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    author = models.CharField(max_length=450, blank=True, null=True)
    description = models.CharField(max_length=450, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    video = models.FileField(upload_to='video/', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "video"

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    number = models.IntegerField(blank=False, null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    website = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.name


class For_Query(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "query"

    def __str__(self):
        return self.name

class Oficce_Contact(models.Model):
    location = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    icons = models.FileField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact"

    def __str__(self):
        return self.location