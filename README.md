# Eventex

Sistema de Eventos.

[![Build Status](https://travis-ci.org/Ricardolv/eventex-wttd.svg?branch=master)](https://travis-ci.org/Ricardolv/eventex-wttd)
[![Code Climate](https://codeclimate.com/repos/568e99e5a1a7976cb40005d6/badges/61c905fa16d7e749fdba/gpa.svg)](https://codeclimate.com/repos/568e99e5a1a7976cb40005d6/feed)

## Como desenvolver ?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instnância com o .env
6. Execute os testes.

```console
git clone git@github.com:Ricardolv/eventex-wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env_sample .env
python manage.py test
```

## Como fazer o deploy ?

1. Crie uma instância no heroku
2. Envie as confiurações para o heroku 
3. Define uma SECRET_KEY segura para instância
4. Define DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```
