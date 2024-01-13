from django.db import models

class Task(models.Model):

    STATE_CHOICES = {
        'PENDING': 'Pending',
        'IN_PROGRESS': 'In Progress',
        'COMPLETED': 'Completed'
    }

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=False)
    estimate = models.IntegerField(null=False)

    # Creating state as a Charfield that only has the choices of state defined before. If no state is passed, it defaults as pending.
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='PENDING')