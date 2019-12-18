from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from account.models import OutGo


class TestIndex(TestCase):
    def test_get(self):
        OutGo.objects.create(category='食費', name="お菓子", price=100)
        OutGo.objects.create(category='日用品', name="ハンガー", price=100)

        res = self.client.get(reverse('index'))
        self.assertTemplateUsed(res, 'account/index.html')
        self.assertContains(res, '食費')
        self.assertContains(res,"お菓子")
        self.assertContains(res, '100円')
        self.assertContains(res, "今月の支出: 200円")
        self.assertEqual(len(res.context['data']), 2)
        