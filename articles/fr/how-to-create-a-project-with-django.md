---
title: Comment créer un projet avec Django
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-15T23:33:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-project-with-django
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c90740569d1a4ca32eb.jpg
tags:
- name: Django
  slug: django
- name: toothbrush
  slug: toothbrush
seo_title: Comment créer un projet avec Django
seo_desc: 'Now that we know how to create virtual environments and use pip, we can
  begin building our project. In this article, we will create our first Django project,
  write tests, and start our development server.

  Creating the Virtual Environment

  First, let’s...'
---

Maintenant que nous savons comment créer des environnements virtuels et utiliser pip, nous pouvons commencer à construire notre projet. Dans cet article, nous allons créer notre premier projet Django, écrire des tests et démarrer notre serveur de développement.

## **Création de l'environnement virtuel**

Tout d'abord, créons un nouvel environnement virtuel pour ce projet. (Si vous ne l'avez pas déjà fait, désactivez l'environnement virtuel précédent en tapant `deactivate` dans le terminal). Pour plus d'informations sur les environnements virtuels et comment les utiliser, visitez [cette page](https://www.freecodecamp.org/news/python-virtual-environments-explained-with-examples/).

Naviguez jusqu'au répertoire où vous voulez le projet Django et tapez ce qui suit dans le terminal :

```text
mkvirtualenv taskplanner --python=/usr/bin/python3
```

Vous devrez peut-être changer votre chemin Python s'il est différent de celui ci-dessus.

L'invite de commande devrait maintenant ressembler à ce qui suit, indiquant que vous êtes dans un environnement virtuel.

```text
(taskplanner)<a href='https://sites.google.com/a/chromium.org/chromedriver/downloads' target='_blank' rel='nofollow'>munsterberg@Lenovo ~/workspace] $
```

Si ce n'est pas le cas, tapez simplement :

```text
workon taskplanner
```

Nous pouvons maintenant installer Django :

```text
pip install Django
```

## **Créer notre projet Django**

Avec Django installé, nous pouvons créer notre projet :

```text
django-admin.py startproject taskplanner
```

Ensuite, naviguez dans notre nouveau projet en tapant :

```text
cd taskplanner
```

Avant de faire quoi que ce soit, définissons ce répertoire comme notre répertoire de travail en utilisant virtualenvwrapper :

```text
setvirtualenvproject
```

**Note** : Pour une liste des commandes virtualenvwrapper, tapez `virtualenvwrapper` dans votre terminal.

Maintenant, lorsque nous sommes dans notre environnement virtuel, nous pouvons taper `cdproject` pour naviguer directement vers notre répertoire de travail.

Votre répertoire de projet devrait ressembler à ceci :

```text
taskplanner // notre répertoire de travail principal
|--- manage.py // similaire au script django-admin, vous verrez ceci utilisé
               // beaucoup tout au long de notre projet
|--- taskplanner
    |--- __init__.py // cela indique simplement à python de traiter ce répertoire comme un package
    |--- settings.py // fichier de configuration principal pour notre projet
    |--- urls.py // nous utiliserons ceci pour configurer les urls
    |--- wsgi.py // ceci est utilisé pour déployer notre projet sur un serveur de production
```

## **Tests fonctionnels**

Le développement piloté par les tests est une meilleure pratique largement utilisée dans le développement de logiciels. Basiquement, nous voulons écrire un test d'abord qui est voué à échouer, puis écrire le moins de code possible pour passer ce test. Avec Django, notre objectif est d'écrire à la fois des tests fonctionnels (également connus sous le nom de tests d'intégration, tests de bout en bout, etc.) et des tests unitaires tout au long du développement. Ne vous inquiétez pas, les tests ne sont pas aussi difficiles qu'ils en ont l'air !

Mais d'abord, nous devons créer un nouvel environnement virtuel dédié aux tests. Ouvrez un nouvel onglet dans votre terminal, naviguez jusqu'à votre répertoire de projet taskplanner et tapez :

```text
mkvirtualenv taskplanner_test --python=/usr/bin/python3
```

Vous devriez maintenant avoir 2 onglets ouverts dans votre terminal, l'un dans l'environnement virtuel (taskplanner), et l'autre dans l'environnement virtuel (taskplanner_test).

Si vous tapez `pip freeze` dans notre nouvel environnement de test (taskplanner_test), vous remarquerez que rien n'apparaît. Cela est dû au fait que nous n'avons encore rien installé dans notre nouvel environnement.

Alors, installons Django d'abord dans notre environnement de test (taskplanner_test) :

```text
pip install Django
```

Pour créer nos tests fonctionnels, nous allons avoir besoin de quelques choses. Tout d'abord, nous devons avoir le navigateur web Firefox installé sur notre machine. Si vous n'avez pas Firefox, installez-le maintenant.

**Note** : Vous pouvez utiliser Chrome pour les tests d'intégration, mais vous devez télécharger le pilote [ici](https://sites.google.com/a/chromium.org/chromedriver/downloads) et suivre [cette question stack overflow](https://stackoverflow.com/questions/13724778/how-to-run-selenium-webdriver-test-cases-in-chrome). Firefox a historiquement eu de meilleures performances que Chrome lors de l'exécution de tests d'intégration, ce qui est une considération très importante puisque, comparés aux tests unitaires, les tests d'intégration sont extrêmement lents.

Cela est dû au fait que les tests d'intégration testent l'**ensemble** du système, plutôt que des "unités" (petits composants). Dans le monde réel, parfois il est préférable d'éviter les tests d'intégration en raison du long temps de développement pour les créer, du temps d'exécution lent, des erreurs ambiguës, et d'autres raisons que vous découvrirez avec le temps.

Cependant, ils valent toujours la peine d'être considérés lors du développement d'une application réelle, et peuvent être très utiles en termes de fiabilité malgré les inconvénients de performance.

Ensuite, nous devons installer un package appelé [Selenium](https://www.selenium.dev/). Ce package nous fournira un WebDriver afin que nous puissions contrôler un navigateur avec nos tests. Selenium est généralement utilisé pour automatiser votre navigateur.

```text
pip install selenium
```

Maintenant que nous avons installé cela, nous aurons besoin d'un répertoire pour créer nos tests :

```text
mkdir functional_tests
```

Dans le répertoire `taskplanner`, vous devriez maintenant voir ce qui suit :

```text
taskplanner
|-- functional_tests
|--- manage.py
|--- taskplanner
    ...
```

Nous devons maintenant créer quelques fichiers dans notre dossier `functional_tests`. Nous allons créer un fichier `__init__.py` (celui-ci indiquera à python de traiter `functional_tests` comme un package), et un fichier `test_all_users.py` pour contenir nos tests.

Faisons cela maintenant :

```text
touch functional_tests/__init__.py
touch functional_tests/test_all_users.py
```

**Note** : `__init__.py` est presque toujours un fichier vide. Pour plus d'informations sur son utilisation, voir [cette réponse stackoverflow](https://stackoverflow.com/questions/448271/what-is-init-py-for).

Nous pouvons enfin commencer à écrire notre premier test fonctionnel ! Les tests fonctionnels sont destinés à tester des morceaux de fonctionnalités dans notre application web. TDD avec Python décrit les tests fonctionnels comme "comment l'application fonctionne du point de vue de l'utilisateur".

Alors, ouvrons le fichier `test_all_users.py` dans notre éditeur de texte. Tout d'abord, nous voulons importer le webdriver de selenium, et pour faciliter cela, Django fournit quelque chose appelé StaticLiveServerTestCase pour les tests en direct. Importons les deux maintenant :

```text
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
```

Puisque nous testons du point de vue de l'utilisateur, nommons ces tests NewVisitorTest. Ajoutez ce qui suit :

```text
class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()
```

Tout d'abord, nous créons une classe StaticLiveServerTestCase nommée NewVisitorTest, celle-ci contiendra nos tests que nous voulons exécuter pour un nouveau visiteur. Ensuite, nous avons deux méthodes nommées setUp et tearDown. La méthode setUp est initialisée lorsque nous exécutons nos tests. Donc, pour chaque test que nous exécutons, nous ouvrons Firefox et attendons 2 secondes pour que la page se charge. tearDown s'exécute après chaque test, cette méthode ferme le navigateur pour nous après chaque test.

Maintenant, nous pouvons écrire notre premier test et avoir Firefox qui s'ouvre et se ferme automatiquement pour nous. Écrivons notre test maintenant en dessous de la méthode tearDown.

```text
    def test_home_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)
```

Notre premier test, combien c'est excitant ! Passons-le en revue. Chaque test que nous voulons créer doit commencer par 'test'. Par exemple, si je voulais créer un test pour mon css, j'appellerais la méthode `test_h2_css`. Ici, nous avons nommé le test `test_home_title`. C'est assez explicite, ce qui est exactement ce que nous voulons pour nos tests. La méthode amène d'abord Firefox à l'url `http://localhost:8000`, puis elle vérifie si 'Welcome to Django' est dans les balises title du head html.

Exécutons ce test maintenant et voyons ce qui se passe :

```text
python manage.py test functional_tests
```

Tout d'abord, que tapons-nous exactement ici ? Le script manage.py nous fournit quelque chose appelé 'test', nous l'utiliserons pour exécuter tous nos tests. Ici, nous l'exécutons sur notre package `functional_tests` que nous avons créé avec le fichier `__init__.py`.

Après avoir exécuté cela, vous devriez voir quelque chose comme ce qui suit dans votre terminal :

```text
F
======================================================================
FAIL: test_home_title (functional_tests.test_all_users.NewVisitorTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/username/url/to/project/taskplanner/functional_tests/test_all_users.py", line 15, in test_home_title
    self.assertIn('Welcome to Django', self.browser.title)
AssertionError: 'Welcome to Django' not found in 'Problem loading page'

----------------------------------------------------------------------
Ran 1 test in 4.524s

FAILED (failures=1)
```

Donc, il a échoué, mais il nous a donné quelques conseils utiles. Tout d'abord, l'AssertionError. 'Welcome to Django' non trouvé dans 'Problem loading page'. Donc, cela signifie que le titre de `http://localhost:8000` était 'Problem loading page'. Si vous naviguez vers l'url, vous verrez que la page web n'était pas disponible.

Essayons d'exécuter notre serveur Django pour faire passer le test. Revenez à l'onglet du terminal qui est dans l'environnement virtuel `taskplanner` et exécutez notre serveur.

```text
python manage.py runserver
```

Vous devriez voir quelque chose comme ce qui suit :

```text
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

March 06, 2016 - 20:53:38
Django version 1.9.4, using settings 'taskplanner.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Ne vous inquiétez pas du message sur les migrations non appliquées pour l'instant.

Maintenant que nous avons un serveur qui s'exécute sur `http://localhost:8000`, exécutons notre test à nouveau.

Revenez à l'autre onglet du terminal qui est dans l'environnement virtuel `taskplanner_test` et exécutez ce qui suit une fois de plus :

```text
python manage.py test functional_tests
```

Vous devriez voir ce qui suit.

```text
Creating test database for alias 'default'...
.
----------------------------------------------------------------------
Ran 1 test in 4.033s

OK
Destroying test database for alias 'default'...
```

## **Ce que nous avons fait jusqu'à présent**

Notre premier test réussi !

Nous avons couvert beaucoup de choses dans cet article. Nous avons créé notre premier projet, configuré des environnements virtuels à des fins de développement et de test, écrit notre premier test fonctionnel, et suivi le processus de développement piloté par les tests en écrivant un test échouant, puis en le faisant passer.

## **Utilisation de modèles de démarrage**

Vous pouvez gagner beaucoup de temps en démarrant votre projet avec un modèle de démarrage Django. Ces projets utilisent les meilleures pratiques qui vous éviteront des maux de tête plus tard lorsque votre projet grandira. Certains des projets les plus populaires sont

* [Cookiecutter](https://github.com/cookiecutter/cookiecutter-django)
* [Hackathon starter](https://github.com/DrkSephy/django-hackathon-starter)
* [Edge](https://github.com/arocks/edge)