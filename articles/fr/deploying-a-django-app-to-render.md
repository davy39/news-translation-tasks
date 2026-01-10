---
title: Comment déployer une application Django sur Render
subtitle: ''
author: Sophia Iroegbu
co_authors: []
series: null
date: '2023-08-09T14:13:39.000Z'
originalURL: https://freecodecamp.org/news/deploying-a-django-app-to-render
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Blog-Banner
seo_title: Comment déployer une application Django sur Render
---

Template--6-.png
tags:
- name: Django
  slug: django
- name: Python
  slug: python
- name: Hébergement Web
  slug: web-hosting
seo_title: null
seo_desc: 'Render est une plateforme d\'hébergement qui vous aide à déployer vos applications facilement. Que vous construisiez des serveurs web, des sites statiques, des tâches cron ou des conteneurs, cet outil peut vous aider à rationaliser le processus.

Si vous êtes un développeur en début de carrière et que vous avez besoin de construire un CV, un r9sum9 ou un portfolio convaincant, Render propose un niveau gratuit qui offre 1 Go de capacité de stockage. 

Dans ce guide, nous allons explorer comment déployer une application Django sur la plateforme Render. Le projet que nous allons créer vous aidera à mettre en valeur vos compétences en codage et vos projets de manière efficace tout en apprenant le déploiement.

## Prérequis

Pour suivre ce guide, vous devrez avoir quelques éléments configurés :

* Un compte sur la plateforme [Render](https://render.com/)
* Un compte [Git](https://www.freecodecamp.org/news/introduction-to-git-and-github/)
* [PostgreSQL](https://www.postgresql.org/docs/) installé
* Un compte [GitHub](https://github.com/)

Maintenant, apprenons comment déployer un serveur web Django gratuitement. 🚀

## Comment configurer une base de données PostgreSQL

Tout d\'abord, rendez-vous sur votre tableau de bord Render et créez une base de données PostgreSQL. Cliquez sur le bouton **New +**, survolez PostgreSQL et cliquez dessus. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/SmOWvHI.png)
_Tableau de bord Render – création d\'une base de données PostgreSQL_

Ensuite, définissez les paramètres de votre base de données en donnant un nom à votre instance de base de données. Vous pouvez choisir de laisser Render définir un nom pour une base de données et un utilisateur ou de le définir vous-même. 

Ce guide est pour les débutants, nous allons seulement définir le nom de l\'instance.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-28-070509.png)
_Création d\'une nouvelle base de données PostgreSQL_

Sélectionnez le niveau gratuit et cliquez sur **Create Database.** 

Note : Chaque base de données gratuite créée sur Render expire 90 jours après sa création. Prenez-en note et mettez à niveau si c\'est un projet important. Vous pouvez voir les tarifs [ici](https://render.com/pricing). 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/V4O1Sin.png)
_Création d\'une nouvelle base de données PostgreSQL_

Une fois que le statut de votre base de données indique **Available**, cela signifie que la base de données a été créée avec succès et est prête à être utilisée. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Utirlzn.png)
_Vérification du statut d\'une nouvelle base de données PostgreSQL_

Faites défiler cette page pour voir les paramètres de votre base de données. Vous utiliserez ces paramètres pour configurer votre application Django. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/GKfYcUX.png)
_Informations sur la base de données_

Ensuite, le contrôle d\'accès vous permet de choisir une adresse IP pour accéder à votre base de données. 

Une fois votre base de données créée, elle est livrée avec une route de contrôle d\'accès prédéfinie qui vous permet d\'y accéder depuis n\'importe où dans le monde en utilisant une seule (1) adresse IP. Cependant, vous ne pouvez pas définir une autre route puisque vous utilisez un plan gratuit sur Render. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/Screenshot-2023-07-28-072323.png)
_Informations sur le contrôle d\'accès PostgreSQL_

Vous pouvez choisir de changer cela ou de le laisser par défaut. 

Maintenant que nous avons créé une base de données, configurons-la sur un projet Django.

## Comment connecter votre base de données

Une fois la base de données configurée, vous devez la connecter à votre projet Django dans le fichier `settings.py`. 

Rendez-vous dans votre base de code et connectez-la. 

Tout d\'abord, installez dj-database-url 



```python
pip install dj-database-url
```

Il existe différentes façons de connecter votre base de données à votre projet d\'application. Ce guide utilise l\'URL de connexion externe. 

Rendez-vous dans les paramètres de votre base de données sur Render et copiez l\'**External Database URL**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/dJqwIy4.png)
_Obtention de l\'URL de la base de données externe_

Ensuite, importez [_dj-database-url_](https://pypi.org/project/dj-database-url/) dans votre `settings.py` et définissez l\'URL de la base de données (de Render) comme votre base de données. 

Note : Il est toujours judicieux d\'ajouter des informations sensibles à un fichier .env pour des raisons de sécurité. 

```python
import dj-database-url
import os

DATABASES = {
	"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}
```

Ensuite, migrez vos tables vers votre nouvelle base de données pour vous assurer que la connexion a réussi. 

Si vous n\'avez pas effectué de migrations vers db.sqlite localement, assurez-vous de faire des migrations d\'abord ou vous ne créerez pas de tables lorsque vous exécuterez `python manage.py migrate`. 

```python
# Pour faire des migrations si c\'est la première fois que vous vous connectez à une base de données 
python manage.py makemigrations

#Pour migrer les tables définies dans vos dossiers de migrations
python manage.py migrate
```

Si la connexion a réussi et que vous migrez toutes vos tables, la sortie de votre terminal devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/nXVd604.png)
_Migration réussie_

Vous n\'êtes plus qu\'à une étape du déploiement de votre projet Django ! 🎉

N\'oubliez pas de pousser votre base de code vers un dépôt Git avec des commits significatifs. 

## Comment créer un service Web

C\'est la dernière étape pour rendre votre projet accessible en ligne.

Rendez-vous sur votre tableau de bord Render. Cliquez sur **New +** et sélectionnez **Web Service**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/wbse.png)
_Création d\'un nouveau service Web_

Connectez votre GitHub si vous ne l\'avez pas déjà fait. Cela devrait ressembler à ceci une fois connecté :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/MMk3GWX.png)
_Connexion de votre Git à la plateforme Render_

Recherchez le dépôt que vous souhaitez déployer et cliquez sur le bouton **Connect**. Cela devrait fonctionner sans problème. 

Ensuite, définissez les paramètres de votre dépôt. Donnez un nom à votre application et assurez-vous de vous connecter à la bonne branche. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/deploy.png)
_Configuration du serveur Web Django_

Installez gunicorn et modifiez votre fichier requirements.txt dans votre projet Django. En exécutant **pip freeze > requirements.txt**, vous pouvez mettre à jour les packages installés dans votre fichier requirements.txt. Cela modifie automatiquement la liste des fichiers requis de votre projet.

Gunicorn est un serveur web Python léger qui fait office de passerelle entre une application web et Internet. Il est conçu pour le déploiement car il gère efficacement les requêtes web entrantes.

Ensuite, poussez vos modifications vers Git. N\'oubliez pas que vous avez connecté Git à votre service web, donc Render surveille le dépôt et déploie automatiquement lorsqu\'il détecte des modifications. 

```python
pip install gunicorn

pip freeze > requirements.txt # Pour mettre à jour votre fichier requirements.txt
```

Assurez-vous d\'ajouter votre service web Render à **ALLOWED_HOSTS** dans votre fichier settings.py. 

Ensuite, assurez-vous de définir le bon fichier `requirements.txt` comme vous pouvez le voir dans l\'image ci-dessous. Assurez-vous également d\'utiliser le bon runtime Python et définissez les paramètres gunicorn de votre projet sur la plateforme Render.

Une fois terminé, faites défiler vers le bas et sélectionnez **Create Web Service**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/req-1.png)
_Création d\'un service Web_

Retournez au tableau de bord Render et cliquez sur le service Web déployé pour voir votre lien en direct.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/final.png)
_Service Web et base de données déployés_

C\'est tout ! Vous avez déployé votre première application Django sur une plateforme gratuite. Profitez de votre serveur Web pendant les 90 prochains jours. 😎

## Conclusion

En résumé, déployer une application ou un serveur Django, ou tout autre serveur sur Render, est facile et efficace. 

En tirant parti des fonctionnalités de Render comme l\'intégration continue et la surveillance intégrée, les développeurs peuvent se concentrer davantage sur la construction de l\'application et de ses fonctionnalités plutôt que de s\'inquiéter de l\'infrastructure et de la gestion de l\'application.'