from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='teacher/', blank=False, null=False)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}'


class TeacherAssistant(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='teacher/', blank=True, null=True)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}'


class Book(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False)
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='book/', blank=False, null=False)


class Course(models.Model):
    TYPE_CHOICES = [
        ('Finished', 'Finished'),
        ('Open', 'Open'),
    ]
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='course/', blank=False, null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    semester = models.CharField(max_length=6, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False, max_length=4)
    status = models.CharField(max_length=8, choices=TYPE_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, Semester: {self.year} {self.year}, Teacher: {self.teacher}'


class Announcement(models.Model):
    text = models.TextField(null=False, blank=False)
    link = models.URLField(null=True, blank=True)
    link_text = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f'ID: {self.pk}'


class Schedule(models.Model):
    TYPE_CHOICES = [
        ('Event', 'Event'),
        ('Assignment', 'Assignment'),
        ('Due', 'Due'),
        ('Exam', 'Exam'),
    ]
    DAY_CHOICES = [
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    type = models.CharField(choices=TYPE_CHOICES, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    day = models.CharField(null=False, blank=False, choices=DAY_CHOICES)
    text = models.TextField(null=False, blank=False, max_length=60)
    slide = models.URLField(null=True, blank=True)
    ta_note = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'ID: {self.pk}, Date: {self.date} {self.day}'


class Lecture(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='lecture/', blank=False, null=False)
    note = models.URLField(blank=True, null=True)
    slide = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}'


class CourseMaterial(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    link_text = models.CharField(max_length=100, null=True, blank=True)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.text}, Course: {self.course.name}'


class Assignment(models.Model):
    pdf_link = models.URLField(null=False, blank=False)
    assignment_number = models.IntegerField(max_length=2, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    attachment_link = models.URLField(null=True, blank=True)
    solution_link = models.URLField(null=True, blank=True)
    due_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, Due: {self.due_date}'


class Policy(models.Model):
    text = models.TextField(null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'ID: {self.pk}, Course: {self.course}, text: {self.text[:20]}'
