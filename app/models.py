from django.contrib.auth.models import User


class DefaultUser(User):
    def __unicode__(self):
        return u"%s %s" % (self.last_name, self.first_name)

    class Meta:
        verbose_name = u"Пользовать"
        verbose_name_plural = u"Пользователи"
