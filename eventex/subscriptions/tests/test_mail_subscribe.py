from django.test import TestCase
from django.core import mail


class  SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Adson', cpf='1234567891',
                    email='adsonemanuels3c@gmail.com', phone='83-9999-9999')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_mail_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_mail_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_mail_to(self):
        expect = ['contato@eventex.com.br', 'adsonemanuels3c@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_mail_body(self):

        contents = [
                    'Adson',
                    '1234567891',
                    'adsonemanuels3c@gmail.com',
                    '83-9999-9999']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
