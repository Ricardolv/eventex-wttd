from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
         data = dict(name= 'Ricardo Luiz Viana', cpf= '12345678901',
                    email='richardluizv@gmail.com', phone='31-98426-0143')
         self.client.post('/inscricao/', data)
         self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect,  self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect,  self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'richardluizv@gmail.com']

        self.assertEqual(expect,  self.email.to)

    def test_subscription_email_body(self):
        contets = ['Ricardo Luiz Viana',
                   '12345678901',
                   'richardluizv@gmail.com',
                   '31-98426-0143']

        for contet in contets:
            with self.subTest():
                self.assertIn(contet, self.email.body)