from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=90)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/speakers/%s' % self.slug

class Subject(models.Model):
    name = models.CharField(max_length=90)
    slug = models.SlugField(max_length=90)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/subjects/%s' % self.slug

class Episode(models.Model):
    number = models.PositiveIntegerField()
    sub_episode = models.CharField(max_length=5, null=True, blank=True)
    date = models.DateField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    def __unicode__(self):
        if self.sub_episode:
            return "%s(%s) - %s" % (str(self.number), self.sub_episode, self.title)
        else:
            return "%s - %s" % (str(self.number), self.title)
    
    def get_absolute_url(self):
        return '/episodes/%s' % self.slug
    
class Segment(models.Model):
    episode = models.ForeignKey(Episode)
    title = models.CharField(max_length=90)
    slug = models.SlugField(max_length=90)
    is_top_story = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/segments/%s' % self.slug
    
class Mention(models.Model):
    subject = models.ForeignKey(Subject)
    segment = models.ForeignKey(Segment)
    speaker = models.ForeignKey(Speaker)
    minute = models.PositiveIntegerField()
    seconds = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.subject.name
    
    def start_marker(self):
        return "%s:%s" % (str(self.minute), str(self.seconds))
