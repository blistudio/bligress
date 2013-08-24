from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=1024)
    start_date = models.DateTimeField('start date')
    done_date = models.DateTimeField('done date', null=True, blank=True)
    description = models.TextField(default="")
    hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    owner = models.ForeignKey(User)
    group = models.ManyToManyField(User, related_name='u+', null=True, blank=True)
    phase = models.ForeignKey('Phase', null=False, default=0)
    PRIORITIES = (
        ("LO", "Low"),
        ("NO", "Normal"),
        ("HI", "High"),
        ("AS", "ASAP"),
    )
    priority = models.CharField(max_length=2, choices=PRIORITIES, default="NO")
    queue_number = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def get_priority(self):
        for p in self.PRIORITIES:
            if p[0] == self.priority:
                return p[1]
        return self.priority

class Phase(models.Model):
    name = models.CharField(max_length=256)
    size = models.IntegerField()
    order = models.IntegerField()

    def __unicode__(self):
        return self.name

class Board(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField('start date')
    task = models.ManyToManyField('Task', related_name='task+', null=True, blank=True)
    phases = models.ManyToManyField('Phase', related_name='phase+', null=True, blank=True)

    def __unicode__(self):
        return self.name

class PhaseStatistics(models.Model):
    board = models.ForeignKey('Board')
    phase = models.ForeignKey('Phase')
    num_items = models.IntegerField()
    entry_avg = models.FloatField()
    leave_avg = models.FloatField()

class Statistics(models.Model):
    round_time = models.FloatField()
    board = models.ForeignKey('Board')
    phase = models.ForeignKey('PhaseStatistics')
