from django.db import models


class Position(models.Model):
    class Meta:
        verbose_name_plural = 'Positions'

    title = models.CharField(max_length=255, unique=True, verbose_name='Title')
    rate = models.IntegerField(verbose_name='Rate')

    def __unicode__(self):
        return self.title


class Employee(models.Model):
    class Meta:
        verbose_name_plural = 'Employees'

    position = models.ForeignKey(Position, verbose_name='Position')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    first_name = models.CharField(max_length=255, verbose_name='First name')
    middle_name = models.CharField(max_length=255, verbose_name='Middle name')
    birthday = models.DateField(verbose_name='Birthday')

    def __unicode__(self):
        return self.last_name + ' ' + self.last_name


class ProjectType(models.Model):
    class Meta:
        verbose_name_plural = 'Project types'

    title = models.CharField(max_length=255, verbose_name='Title')

    def __unicode__(self):
        return self.title


class Work(models.Model):
    class Meta:
        verbose_name_plural = 'Works'

    title = models.CharField(max_length=255, verbose_name='Title')

    def __unicode__(self):
        return self.title


class Project(models.Model):
    class Meta:
        verbose_name_plural = 'Projects'

    title = models.CharField(max_length=255, unique=True, verbose_name='Title')
    deadline = models.DateField(verbose_name='Deadline')
    manager = models.ForeignKey(Employee, verbose_name='Manager')
    price = models.IntegerField(verbose_name='Price')
    type = models.ForeignKey(ProjectType, verbose_name='Project type')
    details = models.TextField(verbose_name='Details')

    def __unicode__(self):
        return self.title


class Procurance(models.Model):
    class Meta:
        verbose_name_plural = 'Procurances'

    project = models.ForeignKey(Project, verbose_name='Project')
    employee = models.ForeignKey(Employee, verbose_name='Employee')
    work = models.ForeignKey(Work, verbose_name='Work')
    work_amount = models.IntegerField(verbose_name='Work amount')
    start_date = models.DateField(verbose_name='Start date')
    planned_end_date = models.DateField(verbose_name='Planned end date')
    real_end_date = models.DateField(verbose_name='Real end date', null=True)

    def __unicode__(self):
        return self.project.title + '/' + self.work.title
