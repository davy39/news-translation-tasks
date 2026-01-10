---
title: Comment tester les signaux Django comme un pro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-18T05:43:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-testing-django-signals-like-a-pro-c7ed74279311
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UTaOKkC0_Ha3DgqrzrcPzw.jpeg
tags:
- name: Django
  slug: django
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Testing
  slug: testing
seo_title: Comment tester les signaux Django comme un pro
seo_desc: 'By Haki Benita

  For a better reading experience, check out this article on my website.

  Django Signals are extremely useful for decoupling modules. They allow a low-level
  Django app to send events for other apps to handle without creating a direct depe...'
---

Par Haki Benita

Pour une meilleure expérience de lecture, consultez [cet article sur mon site web](https://hakibenita.com/how-to-test-django-signals-like-a-pro).

Les [signaux Django](https://docs.djangoproject.com/en/1.10/topics/signals/) sont extrêmement utiles pour découpler les modules. Ils permettent à une application Django de bas niveau d'envoyer des événements pour que d'autres applications les gèrent sans créer de dépendance directe.

Les signaux sont faciles à configurer, mais plus difficiles à tester. Dans cet article, je vais vous guider pas à pas pour implémenter un gestionnaire de contexte pour tester les signaux Django.

### Le cas d'utilisation

Supposons que vous avez un module de paiement avec une fonction de charge. (J'[écris beaucoup sur les paiements](https://medium.com/@hakibenita/working-with-apis-the-pythonic-way-484784ed1ce0#.ji6p00af1), donc je connais bien ce cas d'utilisation.) Une fois qu'une charge est effectuée, vous voulez incrémenter un compteur de charges totales.

À quoi cela ressemblerait-il en utilisant des signaux ?

Tout d'abord, définissez le signal :

```
# signals.py
```

```
from django.dispatch import Signal
```

```
charge_completed = Signal(providing_args=['total'])
```

Ensuite, envoyez le signal lorsqu'une charge est terminée avec succès :

```
# payment.py
```

```
from .signals import charge_completed
```

```
@classmethod
def process_charge(cls, total):
```

```
    # Traiter la charge...
```

```
    if success:
        charge_completed.send_robust(
            sender=cls,
            total=total,
        )
```

Une autre application, telle qu'une application de résumé, peut connecter un gestionnaire qui incrémente un compteur de charges totales :

```
# summary.py
```

```
from django.dispatch import receiver
```

```
from .signals import charge_completed
```

```
@receiver(charge_completed)
def increment_total_charges(sender, total, **kwargs):
    total_charges += total
```

Le module de paiement n'a pas besoin de connaître le module de résumé ou tout autre module gérant les charges complétées. **Vous pouvez ajouter de nombreux récepteurs sans modifier le module de paiement.**

Par exemple, les éléments suivants sont de bons candidats pour les récepteurs :

* Mettre à jour le statut de la transaction.
* Envoyer une notification par email à l'utilisateur.
* Mettre à jour la dernière date d'utilisation de la carte de crédit.

### Tester les signaux

Maintenant que vous avez couvert les bases, écrivons un test pour `process_charge`. Vous voulez vous assurer que le signal est envoyé avec les bons arguments lorsqu'une charge est terminée avec succès.

La meilleure façon de tester si un signal a été envoyé est de s'y connecter :

```
# test.py
```

```
from django.test import TestCase
```

```
from .payment import charge
from .signals import charge_completed
```

```
class TestCharge(TestCase):
```

```
    def test_should_send_signal_when_charge_succeeds(self):
        self.signal_was_called = False
        self.total = None
```

```
        def handler(sender, total, **kwargs):
            self.signal_was_called = True
            self.total = total
```

```
        charge_completed.connect(handler)
```

```
        charge(100)
```

```
        self.assertTrue(self.signal_was_called)
        self.assertEqual(self.total, 100)
```

```
        charge_completed.disconnect(handler)
```

Nous créons un gestionnaire, nous connectons au signal, exécutons la fonction et vérifions les arguments.

Nous utilisons `self` à l'intérieur du gestionnaire pour créer une fermeture. Si nous n'avions pas utilisé `self`, la fonction de gestionnaire aurait mis à jour les variables dans sa portée locale et nous n'aurions pas accès à celles-ci. Nous y reviendrons plus tard.

Ajoutons un test pour **nous assurer que le signal n'est pas appelé si la charge a échoué** :

```
def test_should_not_send_signal_when_charge_failed(self):
    self.signal_was_called = False
```

```
    def handler(sender, total, **kwargs):
        self.signal_was_called = True
```

```
    charge_completed.connect(handler)
```

```
    charge(-1)
```

```
    self.assertFalse(self.signal_was_called)
```

```
    charge_completed.disconnect(handler)
```

Cela fonctionne, mais c'est **beaucoup de code répétitif !** Il doit y avoir une meilleure façon.

### Entrée du gestionnaire de contexte

Décomposons ce que nous avons fait jusqu'à présent :

1. Connecter un signal à un gestionnaire.
2. Exécuter le code de test et enregistrer les arguments passés au gestionnaire.
3. Déconnecter le gestionnaire du signal.

Ce modèle semble familier...

Regardons ce que fait un gestionnaire de contexte (fichier) [open](https://docs.python.org/3/library/functions.html#open) :

1. Ouvrir un fichier.
2. Traiter le fichier.
3. Fermer le fichier.

Et un gestionnaire de contexte de [transaction de base de données](https://docs.djangoproject.com/en/1.10/topics/db/transactions/#controlling-transactions-explicitly) :

1. Ouvrir la transaction.
2. Exécuter certaines opérations.
3. Fermer la transaction (commit / rollback).

Il semble qu'**un gestionnaire de contexte puisse également fonctionner pour les signaux**.

Avant de commencer, réfléchissez à la manière dont vous souhaitez utiliser un gestionnaire de contexte pour tester les signaux :

```
with CatchSignal(charge_completed) as signal_args:
    charge(100)
```

```
self.assertEqual(signal_args.total, 100)
```

Bien, essayons :

```
class CatchSignal:
    def __init__(self, signal):
        self.signal = signal
        self.signal_kwargs = {}
```

```
        def handler(sender, **kwargs):
            self.signal_kwargs.update(kwargs)
```

```
        self.handler = handler
```

```
    def __enter__(self):
        self.signal.connect(self.handler)
        return self.signal_kwargs
```

```
    def __exit__(self, exc_type, exc_value, tb):
        self.signal.disconnect(self.handler)
```

Ce que nous avons ici :

* Vous avez initialisé le contexte avec le signal que vous voulez "capturer".
* Le contexte crée une fonction de gestionnaire pour enregistrer les arguments envoyés par le signal.
* Vous créez une fermeture en mettant à jour un objet existant (`signal_kwargs`) sur `self`.
* Vous connectez le gestionnaire au signal.
* Un certain traitement est effectué (par le test) entre `__enter__` et `__exit__`.
* Vous déconnectez le gestionnaire du signal.

Utilisons le gestionnaire de contexte pour tester la fonction de charge :

```
def test_should_send_signal_when_charge_succeeds(self):
    with CatchSignal(charge_completed) as signal_args:
        charge(100)
    self.assertEqual(signal_args['total'], 100)
```

C'est mieux, mais **à quoi ressemblerait le test négatif ?**

```
def test_should_not_send_signal_when_charge_failed(self):
    with CatchSignal(signal) as signal_args:
        charge(100)
    self.assertEqual(signal_args, {})
```

Bof, ce n'est pas bien.

Reprenons un autre regard sur le gestionnaire :

* Nous voulons nous assurer que la fonction de gestionnaire a été invoquée.
* Nous voulons tester les arguments envoyés à la fonction de gestionnaire.

Attendez... **Je connais déjà cette fonction !**

### Entrée du Mock

Remplaçons notre gestionnaire par un Mock :

```
from unittest import mock
```

```
class CatchSignal:
    def __init__(self, signal):
        self.signal = signal
        self.handler = mock.Mock()
```

```
    def __enter__(self):
        self.signal.connect(self.handler)
        return self.handler
```

```
    def __exit__(self, exc_type, exc_value, tb):
        self.signal.disconnect(self.handler)
```

Et les tests :

```
def test_should_send_signal_when_charge_succeeds(self):
    with CatchSignal(charge_completed) as handler:
        charge(100)
    handler.assert_called_once_with(
        total=100,
        sender=mock.ANY,
        signal=charge_completed,
    )
```

```
def test_should_not_send_signal_when_charge_failed(self):
    with CatchSignal(charge_completed) as handler:
        charge(-1)
        handler.assert_not_called()
```

**Bien mieux !**

Vous avez utilisé le mock pour exactement ce pour quoi il devrait être utilisé, et vous n'avez pas besoin de vous soucier de la portée et de la fermeture.

Maintenant que vous avez cela qui fonctionne, **pouvez-vous le rendre encore meilleur ?**

### Entrée de contextlib

Python dispose d'un module utilitaire pour gérer les gestionnaires de contexte appelé [contextlib](https://docs.python.org/3.6/library/contextlib.html).

Réécrivons notre contexte en utilisant `contextlib` :

```
from unittest import mock
from contextlib import contextmanager
```

```
@contextmanager
def catch_signal(signal):
    """Catch django signal and return the mocked call."""
    handler = mock.Mock()
    signal.connect(handler)
    yield handler
    signal.disconnect(handler)
```

Je préfère cette approche car elle est plus facile à suivre :

* Le yield rend clair où le code de test est exécuté.
* Pas besoin d'enregistrer les objets sur `self` car le code de configuration (enter et exit) est dans la même portée.

Et c'est tout — 4 lignes de code pour les régir tous ! Profitez-en !