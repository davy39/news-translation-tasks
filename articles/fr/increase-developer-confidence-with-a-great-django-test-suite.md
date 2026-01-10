---
title: Introduction à la suite de tests Django – Comment augmenter votre confiance
  en tant que développeur Python
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-10-05T21:18:46.000Z'
originalURL: https://freecodecamp.org/news/increase-developer-confidence-with-a-great-django-test-suite
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/cover.png
tags:
- name: Django
  slug: django
- name: Testing
  slug: testing
seo_title: Introduction à la suite de tests Django – Comment augmenter votre confiance
  en tant que développeur Python
seo_desc: 'Some developers regard writing tests as a lame checkbox task – but nothing
  could be farther from the truth. Done correctly, tests are one of your application’s
  most valuable assets.

  The Django framework in particular offers your team the opportunity ...'
---

Certains développeurs considèrent l'écriture de tests comme une tâche ennuyeuse à cocher – mais rien ne pourrait être plus éloigné de la vérité. Bien faits, les tests sont l'un des atouts les plus précieux de votre application.

Le framework Django offre en particulier à votre équipe l'opportunité de créer une pratique de test efficace, basée sur la bibliothèque standard Python `unittest`.

Les tests appropriés dans Django sont rapides à écrire, plus rapides à exécuter, et peuvent vous offrir une solution d'intégration continue transparente pour prendre le pouls de votre application en développement.

Avec des tests complets, les développeurs ont plus confiance lorsqu'ils poussent des changements. J'ai vu de première main dans mes propres équipes que de bons tests peuvent augmenter la vitesse de développement comme résultat direct d'une meilleure expérience développeur.

Dans cet article, je vais partager mes propres expériences dans la création de tests utiles pour les applications Django, des bases à la meilleure exécution possible. Si vous utilisez Django ou construisez avec dans votre organisation, vous pourriez aimer lire ma [série Django sur Victoria.dev](https://victoria.dev/series/django/).

## Qu'est-ce qu'il faut tester

Les tests sont extrêmement importants. Bien au-delà de simplement vous faire savoir si une fonction fonctionne, les tests peuvent former la base de la compréhension de votre équipe sur la manière dont votre application est *censée* fonctionner.

Voici le principal objectif : si vous vous cognez la tête et oubliez tout sur le fonctionnement de votre application demain, vous devriez pouvoir retrouver la plupart de votre compréhension en lisant et en exécutant les tests que vous écrivez aujourd'hui.

Voici quelques questions qui peuvent être utiles à poser lorsque vous décidez quoi tester :

* Que doit pouvoir faire votre client ?
* Que ne doit *pas* pouvoir faire votre client ?
* Que doit accomplir cette méthode, vue ou flux logique ?
* Quand, comment ou où cette fonctionnalité doit-elle s'exécuter ?

Les tests qui ont du sens pour votre application peuvent aider à renforcer la confiance des développeurs.

Avec ces sauvegardes sensées en place, les développeurs apportent des améliorations plus facilement et se sentent confiants à introduire des solutions innovantes aux besoins du produit. Le résultat est une application qui se construit plus rapidement, et des fonctionnalités qui sont livrées souvent et avec confiance.

![Une bande dessinée pour les tests de sandwich au beurre de cacahuète et à la gelée](https://victoria.dev/blog/increase-developer-confidence-with-a-great-django-test-suite/pbj-tests.png)
*Une bande dessinée créée par un programmeur et un mathématicien, si vous ne l'aviez pas deviné.*

## Où placer les tests

Si vous n'avez que quelques tests, vous pouvez organiser vos fichiers de test de manière similaire au [modèle d'application par défaut de Django](https://docs.djangoproject.com/en/3.1/ref/django-admin/#startapp) en les mettant tous dans un fichier appelé `tests.py`. Cette approche simple est la meilleure pour les petites applications.

À mesure que votre application grandit, vous pourriez vouloir diviser vos tests en différents fichiers ou modules de test. Une méthode consiste à utiliser un répertoire pour organiser vos fichiers, comme `projectroot/app/tests/`. Le nom de chaque fichier de test dans ce répertoire doit commencer par `test`, par exemple, `test_models.py`.

En plus d'être bien nommés, Django trouvera ces fichiers en utilisant la [découverte de tests intégrée](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) basée sur le module `unittest`. Tous les fichiers dans votre application dont les noms commencent par `test` seront collectés dans une suite de tests.

Cette découverte de tests pratique vous permet de placer des fichiers de test n'importe où cela a du sens pour votre application. Tant qu'ils sont correctement nommés, l'utilitaire de test de Django peut les trouver et les exécuter.

## Comment documenter un test

Utilisez des [docstrings](https://www.python.org/dev/peps/pep-0257/) pour expliquer ce qu'un test est censé vérifier à un niveau élevé. Par exemple :

```python
def test_create_user(self):
    """La création d'un nouvel objet utilisateur doit également créer un objet de profil associé"""
    # ...

```

Ces docstrings vous aident à comprendre rapidement ce qu'un test est censé faire. En plus de naviguer dans la base de code, cela aide à rendre évident lorsqu'un test ne vérifie pas ce que la docstring dit qu'il devrait.

Les docstrings sont également affichées lorsque les tests sont exécutés, ce qui peut être utile pour la journalisation et le débogage.

## Ce dont un test a besoin pour fonctionner

Les tests Django peuvent être rapidement configurés en utilisant des données créées dans la [méthode `setUpTestData()`](https://docs.djangoproject.com/en/3.1/topics/testing/tools/#django.test.TestCase.setUpTestData). Vous pouvez utiliser diverses approches pour créer vos données de test, comme l'utilisation de fichiers externes, ou même le codage en dur de phrases ridicules ou des noms de votre personnel.

Personnellement, je préfère beaucoup utiliser une bibliothèque de génération de fausses données, comme [`faker`](https://github.com/joke2k/faker/).

La bonne configuration de données de test arbitraires peut vous aider à vous assurer que vous testez la fonctionnalité de votre application au lieu de tester accidentellement des données de test. Parce que des générateurs comme `faker` ajoutent un certain degré d'imprévisibilité à vos entrées, cela peut être plus représentatif de l'utilisation dans le monde réel.

Voici un exemple de configuration pour un test :

```python
from django.test import TestCase
from faker import Faker

from app.models import MyModel, AnotherModel

fake = Faker()


class MyModelTest(TestCase):
    def setUpTestData(cls):
        """Configurer rapidement les données pour l'ensemble du TestCase"""
        cls.user_first = fake.first_name()
        cls.user_last = fake.last_name()

    def test_create_models(self):
        """La création d'un objet MyModel doit également créer un objet AnotherModel"""
        # Dans les méthodes de test, utilisez les variables créées ci-dessus
        test_object = MyModel.objects.create(
            first_name=self.user_first,
            last_name=self.user_last,
            # ...
        )
        another_model = AnotherModel.objects.get(my_model=test_object)
        self.assertEqual(another_model.first_name, self.user_first)
        # ...

```

Les tests réussissent ou échouent en fonction du résultat des méthodes d'assertion. Vous pouvez utiliser les [méthodes `unittest` de Python](https://docs.python.org/3/library/unittest.html#assert-methods), et les [méthodes d'assertion de Django](https://docs.djangoproject.com/en/3.1/topics/testing/tools/#assertions).

Pour plus de conseils sur l'écriture de tests, voir [Testing in Django](https://docs.djangoproject.com/en/3.1/topics/testing/).

## Meilleure exécution possible pour exécuter vos tests

La suite de tests de Django est exécutée manuellement avec :

```shell
./manage.py test

```

Je lance rarement mes tests Django de cette manière.

La meilleure, ou la plus efficace, pratique de test est celle qui se produit sans que vous ou vos développeurs ne pensiez jamais : « Je dois d'abord exécuter les tests. »

La beauté de la configuration presque sans effort de la suite de tests de Django est qu'elle peut être exécutée de manière transparente dans le cadre des activités régulières des développeurs. Cela pourrait être dans un hook de pré-commit, ou dans un flux de travail d'intégration ou de déploiement continu.

J'ai précédemment écrit sur la façon d'utiliser les hooks de pré-commit pour [améliorer l'ergonomie des développeurs](https://victoria.dev/blog/technical-ergonomics-for-the-efficient-developer/) et économiser à votre équipe quelques efforts mentaux. Les tests rapides de Django peuvent être exécutés de cette manière, et ils deviennent particulièrement efficaces si vous pouvez [exécuter des tests en parallèle](https://docs.djangoproject.com/en/3.1/ref/django-admin/#cmdoption-test-parallel).

Les tests qui s'exécutent dans le cadre d'un flux de travail CI/CD, par exemple, [sur les pull requests avec GitHub Actions](https://victoria.dev/blog/django-project-best-practices-to-keep-your-developers-happy/#continuous-testing-with-github-actions), ne nécessitent aucun effort régulier de la part de vos développeurs pour se souvenir d'exécuter les tests. Je ne suis pas sûr de pouvoir le dire plus clairement – celui-ci est littéralement un no-brainer.

## Tester votre chemin vers une grande application Django

Les tests sont extrêmement importants et sous-estimés. Ils peuvent attraper des erreurs logiques dans votre application. Ils peuvent aider à expliquer et à valider comment les concepts et fonctionnalités de votre produit fonctionnent réellement. Le meilleur de tout, les tests peuvent renforcer la confiance des développeurs et la vitesse de développement en conséquence.

Les meilleurs tests sont ceux qui sont pertinents, aident à expliquer et à définir votre application, et sont exécutés en continu sans une seconde pensée. J'espère avoir maintenant montré comment les tests dans Django peuvent vous aider à atteindre ces objectifs pour votre équipe !