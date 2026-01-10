---
title: Comment déployer votre projet Django sur une machine EC2 en utilisant GitHub
  Actions
subtitle: ''
author: Muhammad Haseeb
co_authors: []
series: null
date: '2024-01-30T15:40:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-django-project-on-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Deploying-Django-Project-on-EC2-Machine-using-GitHub-Actions.png
tags:
- name: Django
  slug: django
- name: ec2
  slug: ec2
- name: GitHub Actions
  slug: github-actions
seo_title: Comment déployer votre projet Django sur une machine EC2 en utilisant GitHub
  Actions
seo_desc: 'Deploying a Django application can be streamlined and automated using GitHub
  Actions.

  This article provides a comprehensive guide on how to set up a continuous deployment
  pipeline for a Django project hosted on an AWS EC2 instance.

  By leveraging GitH...'
---

Le déploiement d'une application Django peut être rationalisé et automatisé en utilisant GitHub Actions.

Cet article fournit un guide complet sur la façon de configurer un pipeline de déploiement continu pour un projet Django hébergé sur une instance AWS EC2.

En tirant parti de GitHub Actions, les développeurs peuvent automatiser leur processus de déploiement, le rendant plus efficace et sans erreur.

## Prérequis

* Un projet Django hébergé dans un dépôt GitHub.
* Une instance AWS EC2 configurée pour héberger une application Django.
* Une familiarité de base avec YAML et les workflows GitHub.

## Comment configurer l'instance EC2

Avant de plonger dans GitHub Actions, assurez-vous que votre instance EC2 est prête à héberger votre application Django.

Utilisez la commande suivante pour vous connecter à votre instance EC2 :

```
ssh -i /path/to/your-key.pem ec2-user@your-ec2-instance-public-dns
```

Vous pouvez mettre à jour les paquets de votre système en utilisant ces commandes :

```
sudo apt-get update
sudo apt-get upgrade
```

Ensuite, si ce n'est pas déjà fait, installez Python et Pip :

```
sudo apt-get install python3
sudo apt-get install python3-pip
```

Puis installez Django en utilisant cette commande :

```
pip3 install django

```

## Comment configurer un serveur web

Dans cette section, vous verrez comment configurer votre serveur web.

Tout d'abord, installez Nginx :

```
sudo apt-get install nginx

```

Ensuite, configurez Nginx pour Django. Commencez par créer un nouveau fichier de configuration pour votre projet Django.

```
sudo nano /etc/nginx/sites-available/mydjangoapp

```

Puis ajoutez le bloc serveur suivant :

```
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/django/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/gunicorn.sock;
    }
}

```

Enfin, activez la configuration Nginx :

```
sudo ln -s /etc/nginx/sites-available/mydjangoapp /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

```

## Comment configurer une base de données

Vous pouvez installer PostgreSQL en utilisant cette commande :

```
sudo apt-get install postgresql postgresql-contrib

```

Après l'installation, créez une base de données et un utilisateur en utilisant cette commande :

```
sudo -u postgres psql

```

Exécutez cette requête SQL pour créer une nouvelle base de données et ajouter un nouvel utilisateur :

```sql
CREATE DATABASE mydjangodb;
CREATE USER mydjangouser WITH PASSWORD 'password';
ALTER ROLE mydjangouser SET client_encoding TO 'utf8';
ALTER ROLE mydjangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydjangouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mydjangodb TO mydjangouser;
\q

```

Ensuite, configurez Django pour utiliser PostgreSQL. Dans votre fichier `settings.py` de Django, mettez à jour le paramètre `DATABASES` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydjangodb',
        'USER': 'mydjangouser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Le workflow GitHub Actions pour déployer un projet Django implique plusieurs étapes clés :

### Étape #1 - Checkout et préparation

La première étape de votre workflow consiste à extraire le dernier code de votre dépôt GitHub et à configurer l'environnement pour le déploiement.

```yaml
name: Déployer Django sur EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Extraire le dépôt
      uses: actions/checkout@v2

```

### Étape #2 - Script de déploiement

Le script de déploiement implique de récupérer le dernier code, d'installer les dépendances, d'exécuter les migrations et de redémarrer les serveurs web et WSGI.

Créez un nouveau fichier `deploy_script.sh` sur votre machine EC2 et ajoutez le code ci-dessous :

```bash
#!/bin/bash

DRY_RUN=$1

echo "Récupération du dernier code depuis le dépôt..."
# Sauter l'extraction réelle du code en mode dry run
[ "$DRY_RUN" != "true" ] && git pull origin main

echo "Installation des dépendances..."
# Sauter l'installation réelle en mode dry run
[ "$DRY_RUN" != "true" ] && pip install -r requirements.txt

echo "Exécution des migrations..."
# Sauter les migrations réelles en mode dry run
[ "$DRY_RUN" != "true" ] && python manage.py migrate

echo "Redémarrage du serveur..."
# Sauter le redémarrage réel en mode dry run
[ "$DRY_RUN" != "true" ] && sudo systemctl restart myapp

echo "Déploiement terminé."

```

### Étape #3 - Créer une étape pour exécuter le script de déploiement

Utilisez GitHub Actions pour vous connecter en SSH à votre instance EC2. Vous devrez stocker la clé SSH de votre instance EC2 en tant que secret GitHub.

```yaml
- name: Exécuter le déploiement
  run: |
    ssh -i ${{ secrets.EC2_SSH_KEY }} ec2-user@your-ec2-instance 'bash -s' < deploy_script.sh
  env:
    ACTIONS_RUNNER_DEBUG: false
```

## Considérations de sécurité

Voici quelques considérations de sécurité à garder à l'esprit :

* **Clés SSH** : Stockez vos clés privées SSH en toute sécurité dans les secrets GitHub.
* **Permissions minimales** : Assurez-vous que le rôle IAM de l'instance EC2 a les permissions minimales nécessaires pour le déploiement.

## Tests et validation

Avant de mettre en œuvre complètement ce workflow, testez-le avec un environnement de développement ou de pré-production pour vous assurer que le processus de déploiement fonctionne comme prévu.

**Déploiement en mode dry run** : Implémentez une étape dans votre workflow GitHub Actions qui effectue un "dry run" du processus de déploiement. Cela peut aider à valider les scripts de déploiement sans affecter l'instance EC2 en production. Ajoutez l'étape ci-dessous pour passer `dry_run = true` dans le script de déploiement.

```yaml
- name: Déploiement en mode dry run
  run: |
    ssh -i ${{ secrets.EC2_SSH_KEY }} ec2-user@your-ec2-instance 'bash -s' < deploy_script.sh true
  env:
    ACTIONS_RUNNER_DEBUG: true
```

**Journalisation et surveillance** : Vous pouvez voir les logs actuels de la capture des actions du processus de déploiement depuis `deploy_script.sh`, qui peuvent être examinés si des problèmes surviennent.

## Conclusion

Automatiser les déploiements Django en utilisant GitHub Actions offre une manière rationalisée et fiable de gérer la livraison des applications.

En suivant les étapes décrites ci-dessus, les développeurs peuvent configurer un pipeline de déploiement robuste qui pousse leur dernier code Django vers une instance EC2 de manière transparente à chaque push sur la branche principale.