---
title: J'ai construit une zone membres sur mon site web avec Python et Django. Voici
  ce que j'ai appris.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T15:40:01.000Z'
originalURL: https://freecodecamp.org/news/i-built-a-members-area-on-my-website-with-python-and-django-heres-what-i-learned
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b12740569d1a4ca2983.jpg
tags:
- name: Django
  slug: django
- name: Python
  slug: python
seo_title: J'ai construit une zone membres sur mon site web avec Python et Django.
  Voici ce que j'ai appris.
seo_desc: "By Nick McCullum\nI decided it was time to upgrade my personal website\
  \ in order to allow visitors to buy and access my courses through a new portal.\
  \ \nSpecifically, I wanted a place for visitors to sign up for an account, view\
  \ my available courses, and..."
---

Par Nick McCullum

J'ai décidé qu'il était temps de mettre à niveau mon site web personnel afin de permettre aux visiteurs d'acheter et d'accéder à [mes cours](https://courses.nickmccullum.com/courses/) via un nouveau portail. 

Plus précisément, je voulais un endroit où les visiteurs pourraient s'inscrire pour un compte, voir mes cours disponibles et acheter ces cours. Une fois qu'un utilisateur avait acheté un cours, il pourrait accéder à tout le contenu du cours pour toujours.   
  
Cela peut sembler simple en théorie. Cependant, sans utiliser un site ecommerce comme Shopify, les sites d'adhésion sont surprenamment complexes. 

Dans cet article, je vais vous guider à travers les décisions que j'ai prises et la pile technologique que j'ai utilisée pour construire ce nouveau site, y compris :

1. Comment commencer ?
2. Démarrer un projet Django
3. Comment configurer les modèles Django
4. Intégration des paiements [Stripe](https://stripe.com/en-ca)
5. Déploiement de mon nouveau site sur une instance AWS EC2
6. Comment cloner le CSS d'une page existante 

![Image](https://lh5.googleusercontent.com/VcTBavKxXlNR907_Gc8lRLWvXPC_8avJogGeEGw7ykM6d9WwZskU6GPvsZjAepF4glzURlMkeKBjdw5yhAcjupP_9AFZEdWVEJEEGRgJs33VbIY2gME4MOk5imvszBkpxBmPBeXJ)

## Comment commencer ?

Lors de l'ajout d'une nouvelle section à votre site web avec un ensemble de fonctionnalités complètement nouvelles, il est logique d'organiser ce site comme un sous-domaine de votre site original.  
  
Un sous-domaine est exactement ce à quoi il ressemble. C'est _un domaine qui fait partie d'un autre domaine (principal)_. Les sous-domaines apparaissent comme une nouvelle section de votre URL de domaine _avant_ l'URL du domaine principal.

Plus précisément :

* Mon domaine _principal_ est : [https://nickmccullum.com](http://www.nickmccullum.com)
* Mon nouveau sous-domaine _cours_ est : [https://courses.nickmccullum.com](https://courses.nickmccullum.com/courses/)

Le principal avantage d'un sous-domaine est qu'ils sont gratuits ! Sans parler du fait qu'un sous-domaine attaché à un site déjà bien classé est rapidement indexé et bénéficie du succès de son parent.

Je savais que j'aurais besoin d'un serveur pour héberger mon nouveau site. J'aurais également besoin d'attacher ce serveur à une adresse IP élastique. 

Une adresse IP élastique est une IP statique qui ne changera jamais. Cela signifie qu'elle peut être accessible par le public 24/7.

La manière la plus rapide de mettre un serveur en marche de nos jours est de l'héberger dans le cloud. Il existe de nombreuses options pour le cloud computing, notamment [AWS d'Amazon](https://aws.amazon.com/), [Droplets de DigitalOcean](https://www.digitalocean.com/products/droplets/), ou [Conteneurs d'Azure](https://azure.microsoft.com/en-ca/). En termes de prix, les options disponibles sont toutes assez égales, donc cela n'a pas trop influencé ma décision.

J'avais déjà une expérience avec [AWS (Amazon Web Services)](https://aws.amazon.com/) - un service basé sur le cloud pour l'hébergement d'infrastructures. Naturellement, j'ai choisi d'héberger mon serveur ici. Pour être plus précis, j'héberge le site sur une instance [EC2](https://aws.amazon.com/ec2/). Nous en parlerons plus tard.

D'accord, donc maintenant je savais où je voulais héberger mon nouveau site web, quelle est la prochaine étape ?   
  
Il était temps de réfléchir à la pile technologique pour le site. Lorsque l'on pense à la technologie à utiliser pour construire son site web, il est important de considérer ces sujets majeurs :  


1. Ce que vous maîtrisez
2. Choisir des technologies frontend et backend qui s'harmonisent bien ensemble
3. La performance du site

Vous devriez répondre à ces questions et essayer de choisir une pile technologique qui convient à vos besoins et à vos capacités. Pour moi, je maîtrise surtout Python, donc [Django 3.0](https://www.djangoproject.com/) était un choix naturel !

J'avais déjà travaillé sur une application Django ([Passiv](https://getpassiv.com/)) donc j'étais globalement familier avec l'infrastructure. Cependant, je n'avais jamais construit un projet Django à partir de zéro. 

À cause de cela, j'avais quelques lectures à faire. Alors que j'apprenais davantage sur ce framework populaire, je n'arrêtais pas de le comparer à PHP, l'outil de programmation web populaire. J'ai travaillé sur plusieurs sites Wordpress par le passé, et Wordpress est construit sur PHP, donc c'était une comparaison naturelle (au moins pour moi).

Selon leur documentation et divers posts sur Stackoverflow, voici les principales différences entre le framework Django et les principaux frameworks PHP :

* Django est plus axé sur la sécurité par défaut et fournit des pratiques de sécurité intégrées pour aider les programmeurs à gagner du temps pendant le développement.
* Django est axé sur la vitesse. Il est connu comme un framework qui aide les développeurs à lancer leurs sites aussi rapidement que possible.
* Django a une performance légèrement inférieure par rapport à la plupart des frameworks basés sur PHP. 

J'aimerais aborder ce dernier point. Python est un langage interprété et est communément associé à une performance inférieure à celle des autres langages de programmation. Lorsqu'un nouveau programmeur entend quelque chose comme cela, il peut penser que Python est bien pire que les autres choix de langage en raison de l'importance de la performance en informatique. 

Bien que Python ait des normes de performance inférieures à celles des autres langages, c'est une déclaration extrêmement vague. En fait, la différence entre Django et Laravel (un framework populaire basé sur PHP) est si faible qu'elle est considérée comme négligeable. 

Pour que cette différence de performance soit importante pour vous, vous devriez écrire une application hautement dépendante de la performance avec des millions d'utilisateurs. J'ai été encouragé d'apprendre que beaucoup des plus grandes applications web du monde sont construites sur Django. En d'autres termes, si Django est assez bon pour [Instagram](https://www.instagram.com/), alors il était certainement assez performant pour mon site.

En fin de compte, j'ai décidé de construire mon site de cours en utilisant Django principalement parce que j'ai de l'expérience avec [Python](https://nickmccullum.com/best-python-libraries-quantitative-finance/). Apprendre un nouveau framework web était un bonus agréable.

Ensuite, je savais que j'aurais besoin d'une base de données pour ce site. Ayant de l'expérience avec MySQL et [PostgreSQL](https://nickmccullum.com/sql/sql-installation/), j'allais initialement utiliser à nouveau ici. Cependant, Django est livré par défaut avec un service de base de données SQLite3 qui nécessite une configuration minimale. Je n'avais jamais utilisé SQLite, donc j'ai fait quelques recherches supplémentaires.

Sur la base des performances et des besoins de stockage de données, la base de données [SQLite3](https://www.sqlite.org/index.html) par défaut livrée avec Django serait plus que suffisamment puissante pour mon site. J'ai été surpris de constater qu'une version plus légère d'un service de base de données pouvait être si puissante !

Pour ceux qui ne connaissent pas cette technologie (comme moi), SQLite3 est une base de données relationnelle avec de grandes performances pour les sites avec des niveaux de trafic faibles à moyens (~100K visites par jour). SQLite3 peut être exécuté sur le même serveur que le site web sans impacter les performances. Cela signifie que je n'avais pas besoin de lancer une instance Amazon RDS séparée, ce qui économise de l'argent lors de la phase de déploiement.

## Démarrer un projet Django

![Image](https://lh5.googleusercontent.com/d5I_NnBMYltwX71zwpcZJ6Fx54w-AU-WR2GRRzrJgw70jY5Xd3oTAEZnmfnslPwM-EeZ-na8_KHOjrlk-Z9VH9gGKvuF8UXz4fOgewIA8dD1-baCKsEMwRaxIRUszVS1z9Ggdux6)

Django est un framework web Python de haut niveau avec pour objectif principal de permettre un **développement rapide** et de fournir une sécurité par défaut. Il prend en charge de nombreuses tâches fastidieuses du développement web, réduisant les pratiques de codage répétitives.

L'une des meilleures parties de l'utilisation de Django est qu'il est absolument gratuit.

Django est conçu pour aider les développeurs à lancer leurs sites web rapidement (ce qui est l'une des principales raisons pour lesquelles je l'ai choisi pour ce projet). L'une de mes fonctionnalités préférées de ce framework (comme pour la plupart des autres) est leur système de templating frontend.   
  
Les [Django Templates](https://docs.djangoproject.com/en/3.0/topics/templates/) vous permettent d'écrire du code dynamique qui génère ensuite le HTML et le CSS souhaités. Cela vous donne la capacité d'utiliser des structures telles que des boucles et des instructions if afin de créer du code HTML dynamique (ce qui signifie qu'il se rend différemment pour chaque utilisateur) qui peut ensuite être servi comme un fichier statique.   
  
Par exemple :

```html
# course_titles_template.html
{% for course in courses_list %}
<h1>{{ course.course_title }} </h1>
{% endfor %}
```

Créerait un en-tête pour chaque variable de cours trouvée dans l'objet `courses_list`. Ce code rendrait un fichier HTML avec une balise `<h1>` qui contient le titre de chaque cours, comme ceci :

```html
<h1> Fondamentaux de Python </h1>
<h1> Python avancé pour la finance et la science des données</h1>
<h1> Comment exécuter des scripts Python </h1>
<h1> Comment créer une classe Python </h1>
```

Le système de templating vous évite beaucoup de travail manuel. Permettre au HTML de se rendre dynamiquement vous évite les maux de tête de mise à jour de votre code chaque fois que vous ajoutez un nouvel objet.   
  
Ce système de templating permet également à l'application web de se mettre à jour au fil du temps à mesure que j'ajoute plus de contenu. Donc dans ce cas, si j'ajoutais un nouveau cours à ma base de données, ce modèle n'aurait pas besoin d'être changé. Il rendrait simplement le titre de mon nouveau cours dans une nouvelle balise d'en-tête.  
  
Django rend également extrêmement facile de commencer un projet. Une fois que vous avez installé Django, vous êtes en mesure d'utiliser `django-admin` afin de démarrer un projet et même de configurer vos applications.

Attendez une seconde, des applications ? Des projets ? Quelle est la différence ?  
  
Une application est une application web qui remplit une certaine fonctionnalité. Il peut s'agir d'un blog, _d'un système de connexion,_ ou même d'un serveur de fichiers. Un projet est une collection d'applications et de configurations qui ensemble forment un site web.

### Installation de Django :

La manière la plus simple d'installer est avec pip, le gestionnaire de paquets Python.

```bash
python -m pip install Django
```

Pour un guide d'installation complet, consultez la [Documentation Officielle de Django](https://docs.djangoproject.com/en/3.0/intro/install/).

### Démarrer un Projet :

Une fois que vous avez installé Django, vous aurez accès à l'outil `django-admin` qui aide les développeurs à configurer des projets et des applications et fournit également d'autres outils pratiques.  
  
Exécuter `django-admin startproject myproject` créera un nouveau dossier dans le répertoire courant où votre projet résidera. Il créera également de nombreux fichiers nécessaires dont vous aurez besoin pour commencer.

Voici à quoi ressemblera votre répertoire après avoir exécuté cette commande :

> myproject/  
>     manage.py   
>     myproject/  
>         __init__.py  
>         settings.py  
>         urls.py  
>         asgi.py  
>         wsgi.py

À l'intérieur du dossier `myproject`, vous trouverez un fichier `manage.py`, qui est extrêmement utile et fournit de nombreuses utilités pratiques. Il y aura un autre dossier nommé `myproject` où vous définirez vos configurations pour le projet.   
  
Le répertoire racine externe myproject/ est un conteneur pour votre projet, son nom n'a pas vraiment d'importance et si vous trouvez cela confus, vous pouvez le renommer comme vous le souhaitez.  
  
Le répertoire interne myproject/ est le package Python réel pour votre projet. Son nom est le nom du package Python que vous devrez utiliser pour importer quoi que ce soit à l'intérieur.

Les fichiers importants à noter ici sont `myproject/settings.py`, où vos paramètres spécifiques à Django et à l'application sont configurés, et `myproject/urls.py`. 

Le fichier `urls.py` est utilisé pour créer des URL au sein de votre site web et les pointer vers un emplacement pour servir la demande. Cette image fait un excellent travail en expliquant comment Django gère les demandes :

![Image](https://lh3.googleusercontent.com/sSrqigM9D-JRg3XQg_sh9WvtehX-UKJnnOmygeIn4u8-Ht2xcv_y0jZ1toPcg8mgoA4BIC_7Y14AG4DKKJ6CIV3IzON06BtmjLp-cTyL8GJ7CvHRr-odmE1Yofo0cGYzhuPbgXQI)

Félicitations à [Ryan Nevius](https://www.ryannevius.com/) pour avoir créé une telle visualisation merveilleuse.

Le fichier `myproject/urls.py` décrit la résolution d'URL pour l'ensemble du site web. Chaque application que vous ajoutez à votre site web contiendra son propre fichier `urls.py` qui décrit la résolution d'URL au sein de cette application spécifique.

Maintenant que vous avez une idée de l'utilisation de certains de ces fichiers, plongeons dans le démarrage d'un projet avec les commandes du script de gestion.

Une commande à noter serait la commande `startapp` utilisée pour créer une application à l'intérieur de votre projet de la même manière que vous avez créé l'application. `python manage.py startapp myapp` créera un nouveau dossier et certains des fichiers nécessaires pour créer une nouvelle application dans votre projet.

> myapp/     
>     __init__.py  
>     admin.py  
>     apps.py  
>     migrations/  
>         __init__.py  
>     models.py  
>     tests.py  
>     views.py

La principale différence ici est la présence des fichiers models et views, qui sont utilisés pour définir la base de données et la fonctionnalité frontend de l'application, respectivement.

Les modèles sont des classes qui définissent vos tables de base de données. Nous discuterons des modèles plus en détail plus tard dans ce tutoriel.

Les vues contrôlent la structure et la fonctionnalité frontend de l'application en prenant une requête web et en retournant une réponse web.   
  
Probablement la commande la plus importante à retenir est la commande runserver :   
`python manage.py runserver`. Cela exécutera votre projet sur votre localhost au port par défaut, 8000.

C'est tout ! En trois étapes simples, vous verrez une page d'accueil de bienvenue vous montrant que l'installation a fonctionné.

![Image](https://lh3.googleusercontent.com/przKJhywBTWAxqF7H1D7YbreiryXuAE4k1a_3ZmGQ0zu7ByEFTI-LBW-PsyBJlT7sUSmWXvycmlZcwAkK0QoOe-bi3zmPmF61KbGsUfNtUE1WVlkSnaCjIgE_00Kn0i8osx1Ipb_)

Il existe un tutoriel extrêmement bien écrit dans la documentation de Django fournissant une marche à suivre bien plus approfondie pour démarrer un projet. Il peut être trouvé ici : [Démarrer un Projet](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)

## Comment configurer les modèles

Comme de nombreux autres frameworks web, Django dispose d'une implémentation du concept de mappage objet-relationnel (**ORM**). Dans Django, cette implémentation est appelée modèles.

Les modèles sont un sujet très important à comprendre lors du développement d'un projet dans Django. Dans leur forme la plus basique, les modèles peuvent être considérés comme des enveloppes pour les tables de base de données.  
  
Autrement dit, un modèle Django est utilisé pour définir vos données. Il contient les champs et les comportements des données que vous stockez. Chaque modèle correspond à une seule table dans votre base de données et les champs dans votre modèle correspondent aux champs dans votre base de données.

Lors de l'écriture de modèles, vous avez accès à des types de champs intégrés puissants qui font beaucoup de travail pour vous. Oubliez l'écriture de code SQL manuellement pour construire votre base de données. Vous pouvez simplement écrire une classe de modèle et exécuter les commandes de migration pour avoir un script SQL entièrement fonctionnel chargé dans votre base de données.   


![Image](https://lh3.googleusercontent.com/CVP_WO8s02EEdmC8_A0w6gbAFmH4AbZ5Z65XatAvx9j31rLjJ1oQMgW4EmBMTlOz0hRWjiybiqnYgadFVX4rlCKLBZGX8pEbhYKbsYwCXwEClo444j6eRt3UeTYurZPg047u5-LH)

Django offre un [Modèle Utilisateur](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/#user-model) dans le cadre de son système d'authentification intégré qui vous permet d'ignorer le côté backend de toutes les connexions/inscriptions et de la gestion des mots de passe. 

Lors de la conception des modèles pour mon nouveau site, j'avais besoin des trois modèles suivants :

* Profile - une classe enveloppe autour du modèle Utilisateur pour ajouter des informations non liées à l'authentification (souvent appelée [Modèle de Profil](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#extending-the-existing-user-model))
* Course - pour stocker toutes les informations sur chaque cours
* Document - un modèle qui stocke les informations sur les fichiers attribués à chaque cours. Je voulais spécifiquement télécharger des documents Markdown, car c'est [comment mon blog public est déjà construit](https://nickmccullum.com/blog-like-a-hacker/)

Voici un exemple de modèle :

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    			
    enrolled_courses = models.ManyToManyField(Course)
```

Un Modèle de Profil est un outil utile pour étendre la fonctionnalité du modèle utilisateur existant afin de stocker des informations sur l'utilisateur, au-delà des simples données d'authentification. Dans mon cas, j'ai créé un _modèle de profil_ nommé Profile pour stocker les cours auxquels l'utilisateur est inscrit.

Voici mon Modèle de Cours :

```python
class Course(models.Model):   
    course_title = models.CharField(max_length=200)   
    course_description = models.CharField(max_length=500)   
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
```

Mon modèle de cours est assez simple. Je n'avais besoin de stocker que 3 informations sur chaque cours pour la logistique, tandis que le contenu réel du cours est géré par le modèle Document.

```python
class Document(models.Model):   
    course = models.ForeignKey(Course,on_delete=models.PROTECT)   
    file = models.FileField (
upload_to=markdown_upload_location,
default='default.md'
)
```

Ici, je tire parti de certaines fonctionnalités intégrées de Python, où je passe la fonction `markdown_upload_location` dans le constructeur `FileField`. 

Cette fonction est utilisée pour déterminer où le fichier téléchargé doit être stocké sur le système de fichiers. Passer la fonction dans le constructeur permet à la fonction d'être exécutée chaque fois qu'un nouveau fichier est téléchargé, au lieu d'être exécutée une seule fois et le même résultat étant utilisé à nouveau.

Essentiellement, lorsqu'un administrateur (moi) télécharge un nouveau cours sur le site, un nouveau dossier est créé pour ce cours et tous les fichiers markdown pour ce cours y sont stockés. Le modèle Document enregistre les liens de ces fichiers vers l'enregistrement du cours dans la base de données. 

Une chose que j'ai retenue de la configuration de ces modèles est la facilité avec laquelle le processus de conception de ma base de données est devenu. Fini les jours de MySQL Workbench et des diagrammes ERR, ou l'écriture de SQL ligne par ligne et l'exécution de mises à jour douloureuses des schémas.

## Intégration des paiements Stripe

[Stripe](https://stripe.com/en-ca) est une plateforme utilisée par de nombreux sites web dans le monde pour recevoir des paiements de la part des clients. Elle est sécurisée, facile à utiliser pour les clients et, surtout, elle est facile à configurer pour nous, les développeurs ! 

Les prix sont également assez justes par rapport à la concurrence, actuellement à 2,9 % + 0,30 CAD par transaction. Ce tarif s'applique aux paiements ponctuels ainsi qu'aux inscriptions par abonnement.

Pour utiliser Stripe en tant que développeur, vous devez créer un compte et consulter leurs pages pour développeurs afin de passer en revue les options. Ils disposent de caisses préconstruites, de bibliothèques et de SDK complets pour construire votre propre caisse personnalisée. Stripe propose également des plugins préexistants pour les frameworks web (Wordpress, Drupal, etc.)

J'ai décidé d'utiliser leur outil [Checkout](https://stripe.com/docs/payments/checkout), qui est une page de paiement sécurisée, hébergée par Stripe, qui m'a permis d'éviter d'avoir à construire une page de paiement. Cela permet non seulement d'économiser le temps de développement de la page frontend pour collecter les informations de paiement, mais aussi le casse-tête de sécuriser le paiement dans le backend.

La sécurité est un sujet énorme de nos jours et les clients sont méfiants quant à l'endroit où ils donnent les détails de leur carte de crédit, donc pour moi, utiliser Stripe était une évidence. Je ne stocke aucune des données des utilisateurs. Au lieu de cela, elles sont envoyées directement à Stripe où elles peuvent être traitées en toute sécurité.

Avec quelques lignes de code, j'ai pu importer le module de caisse préconstruit JavaScript de Stripe. Voici la balise de script :

```javascript
<script 
src="https://checkout.stripe.com/checkout.js"    
class="stripe-button"    
data-key="{{ key }}"    
data-description="Payment: {{ course.course_title }}"    
data-amount="{% multiply course.course_price 100 %}"    
data-locale="auto">
</script>
```

Ici, la data-key est définie sur la clé publique Stripe, similaire à toute clé API de développeur. La description est ce qui apparaîtra dans votre tableau de bord Stripe pour le paiement reçu et le montant est le nombre de centimes pour l'achat. Cette simple inclusion importe cette page de paiement sous forme de modale sur le site web :

![Image](https://lh6.googleusercontent.com/ZoLSCpczDEDUwno0TaWc8jYVl4dTnBxnL1bZBMNjyVJ46UDPbP271hBWancYSPPWA9IDPZHxg6YWSEQEyrcIyNkb4eMpg5iIMHnl0NSJ1oiF4QZluZ8YarjqWStmUc3c0-2hvY3c)

Une fois qu'un client a rempli les informations de paiement, vous n'avez besoin que de regrouper les informations de paiement dans une requête et de les envoyer à Stripe. Ensuite, Stripe est en mesure de traiter les informations et d'approuver le paiement en quelques secondes. 

```python
# Envoyer la charge à Stripe
charge = stripe.Charge.create(    
amount=amount,
currency=currency,    
description=f"Payment for course: {courseTitle}",    source=self.request.POST['stripeToken']
)
```

## Déploiement de mon nouveau site sur une instance EC2

![Image](https://lh3.googleusercontent.com/uRaS5Pqadp9Z-dGeRfXf12DaLLZLpcfQum70RzmQRNUWfcN9JM3Gc46pjCj8KIReqmP922jI9hWQRYDWG0i8r_eBOb5zNh6a0zrO7PXm4qzPPBVRRAsHsjjok2IyxcmsCG1UofJM)

Une fois que j'ai terminé de développer mon nouveau site sur mon localhost, j'ai dû trouver un endroit pour le déployer. J'avais déjà une expérience avec AWS et j'avais déjà un compte, donc cela a rendu la décision facile.   
  
Le cloud élastique d'Amazon - généralement appelé EC2 - permet une abondance de configurations, je suis simplement allé avec la configuration la plus simple. Plus précisément, une machine Ubuntu fonctionnant sur un serveur T2 Micro serait une performance amplement suffisante pour ce site.

La configuration du serveur a été la partie la plus facile du déploiement, j'ai configuré un serveur en moins de 10 minutes. Ensuite, j'ai dû attacher une adresse IP élastique à l'instance et mettre à jour mes enregistrements DNS dans [Route53](https://aws.amazon.com/route53/) (où mon domaine réside).  
  
Après avoir configuré le serveur, j'ai dû déterminer comment j'allais servir le site web aux visiteurs. J'avais déjà une expérience avec Apache, donc c'était un choix naturel. Il s'avère qu'Apache et Django s'harmonisent très bien.

Django est servi via son WSGI (Web Server Gateway Interface) - une interface CGI rapide pour Python, cela est similaire au FPM de PHP si vous êtes familier avec cela. En termes simples, le WSGI est une couche entre Django et le serveur web qui agit comme une interface pour servir les pages web. 

Comme vous le savez peut-être déjà, Python est normalement exécuté dans un `virtualenv`. Cela crée un environnement virtuel où les dépendances d'un projet particulier peuvent vivre sans interférer avec la version système de python. 

Si vous souhaitez en savoir un peu plus sur virtualenv, consultez le [Guide de l'autostoppeur pour Python](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/).

En gros, cela est important uniquement pour configurer les configurations Apache. Pour servir correctement les fichiers, vous devez créer un Daemon WSGI pour votre projet Django comme suit :

```bash
# /etc/apache2/sites-available/mysite.conf:

WSGIProcessGroup courses.nickmccullum.com

WSGIDaemonProcess course python-path=/home/ubuntu/django/courses-website python-home=/home/ubuntu/django/courses-website-venv


WSGIProcessGroup course


WSGIScriptAlias / /home/ubuntu/django/courses-website/courses-website/wsgi.py


<VirtualHost *:80>
        ServerName courses.nickmccullum.com
</VirtualHost>
```

Cela indique à Apache d'utiliser le daemon WSGI afin de servir correctement les fichiers du projet Django. Une fois cela configuré, j'ai dû redémarrer Apache, attendre les 24 heures nécessaires pour que les enregistrements DNS se mettent à jour, puis - voilà :  


![Image](https://lh4.googleusercontent.com/rPc_HYj7M-kwBTan4LUTk4pqkYBYsU4PKksK6gfYo0tV9WzX128fl67Iu0m_xz2-TVmfhRNYvMx4OWzrJP_nr5DE2ECQUXQ6Ym1P1gVFhVpLYH2_3_PE6_JcMLNBZBvWemwNDCuY)

Une dernière étape, j'ai dû sécuriser mon site avec SSL (Secure Socket Layer). Après tout, je demande aux gens de faire des paiements sur mon site, donc les clients s'attendront à ce que le site soit sécurisé !

La manière la plus simple d'activer SSL sur un site, à mon avis, est via [Lets Encrypt](https://letsencrypt.org/). Ils offrent un outil appelé [Certbot](https://certbot.eff.org/) gratuitement, qui peut être activé sur votre serveur pour renouveler automatiquement un certificat de serveur et maintenir votre serveur en fonctionnement avec SSL 24/7 toute l'année.

C'est aussi simple que les trois étapes suivantes :  
  
1. Installer Certbot :

`sudo apt-get install certbot python3-certbot-apache`

**NOTE** : Ce script regardera le paramètre ServerName dans votre fichier de configuration apache pour créer le certificat, assurez-vous donc de l'avoir défini avant de l'exécuter.

2. Obtenir le certificat et dire à certbot de mettre à jour la configuration apache automatiquement :

`sudo certbot --apache`

3. Tester le renouvellement automatique :

`sudo certbot renew --dry-run`

Une fois que vous avez configuré SSL, vous pouvez tester pour vous assurer que le certificat a été installé correctement en vérifiant ce site web : [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/).

Après avoir sécurisé mon site avec SSL, j'ai ouvert les règles de sécurité de l'instance EC2 pour permettre au site d'être public. Avec mon nouveau site en fonctionnement sur mon instance EC2, je suis maintenant en mesure de vendre mes cours en toute sécurité aux clients qui souhaitent apprendre divers sujets en développement logiciel. 

## Réflexions finales

Je suis reconnaissant pour toute l'expérience que j'ai acquise tout au long de ce projet, de la navigation dans un nouveau framework web à l'intégration de l'API Stripe - j'ai certainement appris beaucoup ! 

Apprendre un nouveau sujet comme Django peut être accablant, mais j'ai trouvé que leur documentation était très solide par rapport à d'autres que j'ai lues (erhm, AWS).

Si je devais donner un seul conseil, je vous dirais que la ressource la plus précieuse avec tout outil est la documentation officielle. Cela est particulièrement vrai lorsqu'elle est bien écrite. Mais peu importe l'outil que vous utilisez, n'ayez jamais peur des docs et habituez-vous à les lire afin de trouver des réponses à vos problèmes.

Cet article a été écrit par Nick McCullum, qui enseigne les cours de [Python](https://nickmccullum.com/python-course/), [JavaScript](https://nickmccullum.com/javascript/), et [Data Science](https://nickmccullum.com/advanced-python/) sur son site web.