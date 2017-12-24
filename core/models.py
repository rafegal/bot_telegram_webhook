from __future__ import unicode_literals

from django.db import models

#Create your models here.

class Interaction(models.Model):
    input = models.CharField(max_length=100)
    output = models.TextField()
    script = models.TextField()
    execute_script = models.BooleanField(default=False)

    def __unicode__(self):
        return self.input

    def get_output(self, binds):
        return self.output % binds

    def execute(self):
        try:
            exec self.script
            dic = script()
            return dic
        except Exception as ex:
            return 'ERRO', str(ex)

    class Meta:
        db_table = 'interaction'