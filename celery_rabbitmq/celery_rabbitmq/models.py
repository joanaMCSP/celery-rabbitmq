from django.db import models

class Job(models.Model):

    TYPES = (
        ('map_url', 'map_url'),
        ('merge_maps', 'merge_maps'),
    )

    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    argument = models.TextField()
    result = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """Save model and schedule pending state jobs"""
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.type]
            task.delay(job_id=self.id, s=self.argument)
