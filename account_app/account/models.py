from django.db import models
from django.utils import timezone


class OutGo(models.Model):
    CATEGORY = [
        ('その他', 'その他'),
        ('食費', '食費'),
        ('光熱費', '光熱費'),
        ('家賃', '家賃'),
        ('交際費', '交際費'),
        ('日用品', '日用品'),
        ('通信料', '通信料'),
        ('交通費', '交通費'),
        ('ファッション', 'ファッション'),
        ('趣味', '趣味'),
    ]

    category = models.CharField('カテゴリ', max_length=10, choices=CATEGORY)
    name = models.CharField('買った物', max_length=100)
    price = models.IntegerField('値段', default=0)
    created_at = models.DateField('日付', default=timezone.now)

    class Meta:
        db_table = 'outgo'
        verbose_name = verbose_name_plural = '支出'

    def __str__(self):
        return str(self.category) + ', ' + str(self.name) + ', ' +\
            str(self.price) + '円, ' + str(self.created_at)
