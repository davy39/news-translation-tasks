---
title: Comment planifier des tâches dans une application Django en utilisant Heroku
  Scheduler
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T07:59:00.000Z'
originalURL: https://freecodecamp.org/news/scheduling-jobs-in-a-django-application-using-heroku-scheduler-13c971a22979
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U6htRSu-GZiU0wo_uStebQ.jpeg
tags:
- name: Django
  slug: django
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Web Development
  slug: web-development
seo_title: Comment planifier des tâches dans une application Django en utilisant Heroku
  Scheduler
seo_desc: 'By Alfarhan Zahedi

  Recently, I published my first Django application on Heroku.

  The application is fairly simple — it lists the score associated with every classical
  problem on SPOJ.


  SPOJ — Sphere Online Judge — is a problemset archive, online judge...'
---

Par Alfarhan Zahedi

Récemment, j'ai publié ma première application Django sur Heroku.

L'application est assez simple — elle liste le score associé à chaque problème **classique** sur [SPOJ](http://www.spoj.com/).

> [**SPOJ**](http://www.spoj.com/) — Sphere Online Judge — est une archive de problèmes, un juge en ligne et un service d'hébergement de concours acceptant des solutions dans de nombreuses langues.

Vous pouvez trouver l'application en direct [ici](https://spojscore.alfarhanzahedi.com).

L'application utilise les bibliothèques Python `[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)` et `[requests](http://docs.python-requests.org/en/master/)` pour scraper le contenu du site mentionné, obtenir les détails nécessaires pour chaque problème (à savoir — code du problème, nom du problème, utilisateurs et **score**), et les stocker dans une base de données.

Maintenant, le score associé aux problèmes sur [SPOJ](http://spoj.com) est dynamique. Il est calculé en utilisant la formule suivante :

80 / (40 + nombre_de_personnes_ayant_résolu_le_problème)

Ainsi, le score associé aux problèmes sur [SPOJ](http://spoj.com) change lorsque le nombre_de_personnes_ayant_résolu_le_problème change.

Par conséquent, les données collectées par mon application deviendront inutiles après un certain intervalle de temps. J'ai besoin de configurer un planificateur pour garder ma base de données à jour.

Maintenant, c'est une application très simple. Donc, je voulais configurer le planificateur avec le moins de configuration et de code possible.

### _Les commandes de gestion Django personnalisées et Heroku Scheduler à la rescousse !_

Comprenons nos deux sauveurs.

#### 1. Commandes de gestion Django personnalisées

Les commandes de gestion Django personnalisées sont structurées comme des classes Python qui héritent de leurs propriétés et comportements de la classe `django.core.management.base.BaseCommand`.

Elles sont utilisées pour ajouter une action `manage.py` pour une application Django. `runserver` ou `migrate` sont deux exemples de telles actions.

Un exemple typique d'une telle classe serait :

```
from django.core.management.base import BaseCommand
```

```
class Command(BaseCommand):    help = "<texte d'aide approprié ici>"    def handle(self, *args, **options):        self.stdout.write("Bonjour, le monde !")
```

La classe doit être nommée `Command`, et sous-classer `BaseCommand`.

`help` doit contenir une courte description de la commande, qui sera imprimée dans les messages d'aide.

`handle(self, *args, **options)` définit la logique réelle de la commande. Dans ce cas, nous écrivons simplement la chaîne `Bonjour, le monde !` dans la sortie standard. Dans mon cas, `handle(self, *args, **options)` effectue la tâche de scraper le site — [spoj.com](http://spoj.com) et de mettre à jour la base de données si le **score** associé à l'un des problèmes change.

`handle(self, *args, **options)` est automatiquement exécuté chaque fois que la commande suivante est utilisée :

`python manage.py <nom du script python contenant la classe de gestion>`

Si le nom du script est, par exemple, `script.py`, alors la commande serait :

`python manage.py script`

Remarquez que la méthode handle déclare trois arguments d'entrée : `self` pour référencer l'instance de la classe, `*args` pour référencer les arguments de la méthode elle-même, et `**option` pour référencer les arguments passés dans le cadre de la commande de gestion.

**Où dans la structure du projet ce `script.py` doit-il aller ?**

(Ici, `script.py` fait référence au nom du script contenant la commande de gestion Django personnalisée.)

C'est assez simple. La [documentation officielle](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/) l'explique bien :

> _Il suffit d'ajouter un répertoire `**management/commands**` à l'application. Django enregistrera une commande `**manage.py**` pour chaque module Python dans ce répertoire dont le nom ne commence pas par un soulignement._

> _Par exemple :_

```
polls/    __init__.py    models.py    management/        __init__.py        commands/            __init__.py            _private.py            closepoll.py    tests.py    views.py
```

> _Dans cet exemple, la commande `**closepoll**` sera disponible pour tout projet qui inclut l'application `**polls**` dans `[**INSTALLED_APPS**](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS)`._

> _Le module `**_private.py**` ne sera pas disponible en tant que commande de gestion._

> _Le module `**closepoll.py**` n'a qu'une seule exigence — il doit définir une classe `**Command**` qui étend `[**BaseCommand**](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/#django.core.management.BaseCommand)` ou l'une de ses [sous-classes](https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/#ref-basecommand-subclasses)._

> _Et donc, si nous exécutons la commande suivante dans notre terminal :_

> `_python manage.py closepoll_ _,_

> `_handle(self, *args, **options)_` _à l'intérieur de `closepoll.py` sera exécuté, et toute logique/tâche contenue à l'intérieur de la fonction mentionnée sera exécutée._

La structure de mon projet est la suivante :

```
spojscore│   .gitignore│   manage.py│   Procfile│   README.md│   requirements.txt│   runtime.txt│└───core│   │   admin.py│   │   apps.py│   │   models.py│   │   tests.py│   │   views.py│   │   __init__.py│   │└───management│   │   │   __init__.py│   │   │└───commands│   │   │       script.py│   │   │       __init__.py│   │└───static│   │   └───core│   │       └───css│   │           style.css│   │       └───img│   │               favicon.png│   │               logo.png│   │└───templates│       └───core│               core.html└───spojscore        settings.py        urls.py        wsgi.py        __init__.py
```

Ici, `script.py` contient la commande de gestion personnalisée — le code Python pour scraper [spoj.com](http://spoj.com), collecter les détails de tous les problèmes **classiques**, et mettre à jour la base de données en conséquence.

Comme vous pouvez le voir, il est situé dans `core\management\commands`.

Si vous êtes intéressé, vous pouvez trouver `script.py` [ici](https://github.com/alfarhanzahedi/spojscore/blob/master/core/management/commands/script.py).

Je pense qu'il est clair maintenant que je peux scraper spoj.com et obtenir les données souhaitées en exécutant simplement `python manage.py script` depuis le terminal.

Ainsi, pour garder ma base de données à jour, je dois simplement exécuter la commande ci-dessus au moins une fois par jour.

#### 2. Heroku Scheduler

Selon [le site de Heroku](https://devcenter.heroku.com/articles/scheduler) :

> [_Scheduler_](https://elements.heroku.com/addons/scheduler) _est un add-on gratuit pour exécuter des tâches sur votre application à des [intervalles de temps planifiés](https://devcenter.heroku.com/articles/scheduled-jobs-custom-clock-processes), un peu comme `cron` dans un environnement de serveur traditionnel._

> _Un tableau de bord vous permet de configurer des tâches pour qu'elles s'exécutent toutes les 10 minutes, toutes les heures, ou tous les jours, à une heure spécifiée. Lorsqu'elles sont invoquées, ces tâches s'exécuteront en tant que [dynos ponctuels](https://devcenter.heroku.com/articles/one-off-dynos) et apparaîtront dans vos logs sous le nom de dyno comme `scheduler.X`._

Une fois que vous avez déployé l'application, installez l'add-on Heroku Scheduler.

Pour planifier une fréquence et une heure pour une tâche, ouvrez le tableau de bord Heroku Scheduler en trouvant l'application dans [Mes Applications](https://dashboard.heroku.com/apps), en cliquant sur « Overview », puis en sélectionnant « Heroku Scheduler » dans la liste des add-ons installés.

Sur le tableau de bord Scheduler, cliquez sur « Add Job… », entrez une tâche, sélectionnez une fréquence, [taille du dyno](https://devcenter.heroku.com/articles/dyno-types), et l'heure de la prochaine exécution.

Dans mon cas, la tâche est `python manage.py script`, qui doit être exécutée quotidiennement (fréquence) en utilisant mes dynos gratuits (taille du dyno) à 00:00 UTC (heure de la prochaine exécution).

![Image](https://cdn-media-1.freecodecamp.org/images/08G0BBZMqdmB8njFB4vZzLvPfU5Yy6Wbmi65)

C'est tout !

Ma base de données sera mise à jour à 00:00 UTC tous les jours, et je n'ai pas eu à installer de bibliothèques Python supplémentaires, ni à écrire de morceaux de code supplémentaires. Hourra !

Si vous êtes bloqué quelque part, laissez un commentaire et je ferai de mon mieux pour vous aider.

### Quelques notes finales :

* [Le site officiel de Heroku](https://devcenter.heroku.com/articles/scheduler) dit que — « _L'exécution des tâches du planificateur est attendue mais pas garantie. Le planificateur est connu pour occasionnellement (mais rarement) manquer l'exécution des tâches planifiées. Si les tâches planifiées sont un composant critique de votre application, **il est recommandé de** [**exécuter un processus d'horloge personnalisé**](https://devcenter.heroku.com/articles/scheduled-jobs-custom-clock-processes) à la place pour plus de fiabilité, de contrôle et de visibilité._ » Ce point doit être gardé à l'esprit lors de l'utilisation de Heroku Scheduler.
  
La mienne est une application très simple qui utilise Heroku Scheduler pour exécuter un script simple une fois par jour. Donc, je suppose qu'il fera un excellent travail !
* Mon application, je suppose, est utile pour les programmeurs compétitifs. Pourquoi ? Je l'ai expliqué en détail [ici](https://discuss.codechef.com/questions/113220/value-points-of-spoj-problems).
* Vous pouvez trouver le code source de mon application [ici](https://github.com/alfarhanzahedi/spojscore).

### Une réflexion de mes musings personnels :

Je ne suis qu'un autre programmeur autodidacte.

J'écris du code depuis quelques années maintenant, et j'ai toujours voulu écrire sur mes expériences, mes efforts, mes échecs et mes succès.

Mais hélas, je n'ai pas pu.

Je pensais que mes efforts n'étaient pas assez excitants ou que mes expériences n'allaient pas aider qui que ce soit. Et donc, je me suis retenu d'écrire à leur sujet.

Pour être honnête, je pense la même chose maintenant.

Alors, comment se fait-il que j'ai écrit cet article ?

Eh bien, ce sera le premier de mes nombreux articles.

Et la raison du changement, me demandez-vous ?

Une newsletter.

La semaine dernière, comme d'habitude, j'ai reçu la newsletter hebdomadaire de CSS-Tricks — « _Cette semaine dans la conception et le développement Web_ ».

Voici un extrait de celle-ci :

> C'est fou d'avoir autant de ressources utiles disponibles pour nous aider à tout moment : des articles de blog et des livres aux conférences aléatoires sur node.js qui n'ont que 8 vues et dont 7 sont maintenant les miennes. Donc, je pense que ce week-end a renforcé ma foi dans le blogging et le partage de ce que vous savez, où des notes aléatoires laissées sur l'ancien blog d'un développeur m'ont énormément aidé.

> En tout cas, sur une note similaire, j'ai beaucoup pensé à la façon dont les réseaux sociaux privilégient la célébrité à la valeur. Si vous publiez quelque chose sur Medium par exemple et qu'il n'obtient qu'un seul applaudissement, alors cela vous donne l'impression de, _pourquoi se donner la peine_ ? Quel est l'intérêt si personne ne lit cette chose ? Mais je pense que nous devons lutter contre cette inclination à être séduits par la célébrité et la notoriété des réseaux sociaux parce que je me demande combien d'articles de blog et de vidéos utiles n'ont pas été réalisés simplement parce que quelqu'un pensait qu'ils n'allaient pas obtenir un demi-million de likes ou de retweets.

> Mon conseil après avoir appris de tant de personnes utiles ce week-end est le suivant : si vous pensez à écrire quelque chose qui explique quelque chose avec lequel vous avez lutté, faites-le ! Ne vous inquiétez pas des vues, des likes et des câlins d'Internet. Si vous avez lutté pour comprendre cette chose bizarre, notez-la, même si elle n'est pas éditée et qu'elle utilise trop de virgules et que vous n'aimez pas le ton.

> C'est parce que quelqu'un comme moi est susceptible de trouver ce que vous avez écrit et cela rendra son week-end beaucoup moins stressant qu'il n'aurait pu l'être.

C'est tout. Ces quelques lignes m'ont inspiré pour écrire sur mes efforts et expériences.

**Peut-être que vous devriez aussi.**