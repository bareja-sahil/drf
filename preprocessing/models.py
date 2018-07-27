from django.db import models


class Job(models.Model):
    model_id = models.IntegerField()
    file_id = models.IntegerField()
    run_all = models.BooleanField(default=False)
    pre_process = models.BooleanField(default=False)
    solution_process = models.BooleanField(default=False)
    post_process = models.BooleanField(default=False)
    fatigue_process = models.BooleanField(default=False)
    fracture_process = models.BooleanField(default=False)

    class Meta:
        # Get Jobs Id wise in descending order.
        ordering = ('-id',)

    def __str__(self):
        return "{}-{}".format(self.model_id, self.id)

