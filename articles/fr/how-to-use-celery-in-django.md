---
title: Comment utiliser Celery dans Django
subtitle: ''
author: Udemezue John
co_authors: []
series: null
date: '2025-04-18T16:37:24.801Z'
originalURL: https://freecodecamp.org/news/how-to-use-celery-in-django
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744994231247/63228755-1929-4474-9930-15f8ff1a5631.png
tags:
- name: Python
  slug: python
- name: celery
  slug: celery
- name: Django
  slug: django
seo_title: Comment utiliser Celery dans Django
seo_desc: 'You’ve probably noticed that some tasks in your Django app seem to take
  a long time. For example, maybe sending confirmation emails, resizing images, or
  processing large data files slows things down.

  The good news? You don’t have to sit around waitin...'
---

Vous avez probablement remarqué que certaines tâches dans votre application Django semblent prendre beaucoup de temps. Par exemple, peut-être que l'envoi d'e-mails de confirmation, le redimensionnement d'images ou le traitement de gros fichiers de données ralentissent les choses.

La bonne nouvelle ? Vous n'avez pas à attendre. Vous pouvez confier ces tâches à autre chose et laisser votre application continuer à faire son travail. Cet "autre chose" est Celery.

Celery vous permet d'exécuter des tâches chronophages en arrière-plan tandis que votre application reste rapide. Et si vous utilisez Django, ce n'est en fait pas si difficile à intégrer – une fois que vous comprenez comment les pièces fonctionnent ensemble.

Dans ce guide, je vais vous expliquer ce qu'est Celery, pourquoi il est utile, et exactement comment le configurer avec Django étape par étape.

## Table des matières

1. [Qu'est-ce que Celery et pourquoi l'utiliser dans Django ?](#heading-quest-ce-que-celery-et-pourquoi-lutiliser-dans-django)
    
2. [Comment fonctionne Celery (version simplifiée)](#heading-comment-fonctionne-celery-version-simplifiee)
    
3. [Comment utiliser Celery dans Django](#comment-utiliser-celery-dans-django)
    
    * [1\. Installer les bons packages](#heading-1-installer-les-bons-packages)
        
    * [2\. Créer un fichier](#heading-2-creer-un-fichier-celerypy-dans-votre-dossier-de-projet) [celery.py](http://celery.py) [dans votre dossier de projet](#heading-2-creer-un-fichier-celerypy-dans-votre-dossier-de-projet)
        
    * [3\. Ajouter Celery à](#heading-3-ajouter-celery-a-initpy) [**init**.py](http://init.py)
        
    * [4\. Définir l'URL du broker dans vos paramètres](#heading-4-definir-lurl-du-broker-dans-vos-parametres)
        
    * [5\. Écrire votre première tâche](#heading-5-ecrire-votre-premiere-tache)
        
    * [6\. Appeler la tâche depuis vos vues](#heading-6-appeler-la-tache-depuis-vos-vues)
        
    * [7\. Exécuter le worker Celery](#heading-7-executer-le-worker-celery)
        
4. [Optionnel : Utiliser Django Admin pour surveiller les tâches](#heading-optionnel-utiliser-django-admin-pour-surveiller-les-taches)
    
5. [FAQ](#heading-faq)
    
    * [Que se passe-t-il si Redis tombe en panne ?](#heading-que-se-passe-t-il-si-redis-tombe-en-panne)
        
    * [Puis-je réessayer les tâches échouées ?](#heading-puis-je-reessayer-les-taches-echouees)
        
    * [Celery est-il la seule option ?](#heading-celery-est-il-la-seule-option)
        
6. [Conclusion](#heading-conclusion)
    
7. [Lectures et ressources supplémentaires](#heading-lectures-et-ressources-supplementaires)
    

## Qu'est-ce que Celery et pourquoi l'utiliser dans Django ?

Imaginez que vous gérez une boutique en ligne. Quelqu'un passe une commande. Vous voulez :

* Enregistrer la commande dans la base de données
    
* Lui envoyer une facture par e-mail
    
* Notifier votre entrepôt
    
* Peut-être même commencer à imprimer une étiquette d'expédition
    

Si votre application essaie de tout faire en même temps, votre utilisateur va se retrouver à fixer un écran de chargement. Au lieu de cela, que se passerait-il si vous enregistriez uniquement la commande immédiatement – et passiez le reste à Celery pour qu'il s'en occupe en arrière-plan ?

C'est exactement ce que fait Celery.

C'est une file d'attente de tâches – ce qui signifie simplement qu'elle exécute les choses plus tard, afin que votre application principale n'ait pas à attendre. C'est particulièrement utile pour :

* Envoyer des e-mails
    
* Importer/exporter des données
    
* Exécuter des modèles de machine learning
    
* Extraire des données
    
* Générer des rapports
    

Et oui, cela fonctionne très bien avec Django.

## Comment fonctionne Celery (version simplifiée)

Celery est composé de plusieurs parties :

1. **Producteur de tâches (votre application Django)** – C'est là que vous appelez une tâche.
    
2. **Broker (généralement Redis)** – C'est l'intermédiaire. Il prend la tâche et la conserve jusqu'à ce qu'un worker puisse la récupérer.
    
3. **Worker** – C'est le processus en arrière-plan de Celery qui récupère les tâches du broker et les exécute.
    

Voici le flux :

```plaintext
Application Django → Redis → Worker Celery → Terminé ✅
```

Maintenant, configurons cela.

## Comment utiliser Celery dans Django

### 1\. Installer les bons packages

Vous aurez besoin de `celery` et d'un broker de messages. Redis est un choix populaire.

```bash
pip install celery redis
```

Assurez-vous également que Redis est en cours d'exécution. Vous pouvez l'installer localement via Homebrew (`brew install redis`) ou utiliser un conteneur Docker.

Si vous utilisez Docker :

```bash
docker run -p 6379:6379 redis
```

### 2\. Créer un fichier `celery.py` dans votre dossier de projet

Disons que votre projet Django s'appelle `myproject`. Dans ce même dossier (où se trouve `settings.py`), créez un fichier appelé `celery.py`.

```python
# myproject/celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
```

Voici ce qui se passe :

* `os.environ...` configure les paramètres de Django.
    
* `Celery("myproject")` crée une nouvelle application Celery avec le nom de votre projet.
    
* `app.config_from_object(...)` indique à Celery de lire la configuration depuis le fichier de paramètres de Django.
    
* `autodiscover_tasks()` indique à Celery de trouver les tâches dans vos applications Django automatiquement.
    

### 3\. Ajouter Celery à `__init__.py`

Toujours dans votre dossier `myproject/`, ouvrez `__init__.py` et ajoutez :

```python
from .celery import app as celery_app

__all__ = ("celery_app",)
```

Cela garantit que Celery démarre avec Django.

### 4\. Définir l'URL du broker dans vos paramètres

Ouvrez `settings.py` et ajoutez :

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
```

Cela indique à Celery d'utiliser Redis comme broker.

### 5\. Écrire votre première tâche

Allez dans l'une de vos applications Django (disons que vous avez une application appelée `shop`), et créez un fichier appelé `tasks.py`.

```python
# shop/tasks.py
from celery import shared_task

@shared_task
def send_invoice_email(order_id):
    # Imaginez que cela envoie un e-mail
    print(f"Envoi de l'e-mail de facture pour la commande {order_id}")
```

Le décorateur `@shared_task` indique à Celery que ceci est une tâche en arrière-plan.

### 6\. Appeler la tâche depuis vos vues

Voici comment vous l'utiliseriez dans une vue Django :

```python
# shop/views.py

from .tasks import send_invoice_email
from django.shortcuts import render

def place_order(request):
    # prétendez que cela enregistre une commande
    order_id = 1234  # cela viendrait de votre modèle

    # exécuter la tâche en arrière-plan
    send_invoice_email.delay(order_id)

    return render(request, "order_complete.html")
```

Remarquez le `.delay()` – c'est ce qui envoie la tâche à Celery.

### 7\. Exécuter le worker Celery

Ouvrez maintenant un terminal et démarrez le worker :

```bash
celery -A myproject worker --loglevel=info
```

Vous devriez voir le worker démarrer et attendre les tâches. Lorsque vous passez une commande, il imprimera quelque chose comme :

```css
Envoi de l'e-mail de facture pour la commande 1234
```

## Optionnel : Utiliser Django Admin pour surveiller les tâches

Si vous souhaitez surveiller l'état des tâches dans l'admin, vous pouvez utiliser [django-celery-results](https://github.com/celery/django-celery-results).

```bash
pip install django-celery-results
```

Puis mettez à jour votre `settings.py` :

```python
INSTALLED_APPS += ["django_celery_results"]

CELERY_RESULT_BACKEND = "django-db"
```

Exécutez les migrations :

```bash
python manage.py migrate
```

Maintenant Celery enregistrera les résultats des tâches dans votre base de données, et vous pourrez les voir dans l'admin Django.

## FAQ

### **Que se passe-t-il si Redis tombe en panne ?**

Vos tâches ne seront ni envoyées ni récupérées. Mais une fois Redis revenu, les choses devraient reprendre.

### **Puis-je réessayer les tâches échouées ?**

Oui ! Celery prend en charge les réessais. Vous pouvez définir combien de fois une tâche doit être réessayée et à quelle fréquence. Exemple :

```python
@shared_task(bind=True, max_retries=3)

def risky_task(self):
    try:
        # Faire quelque chose de risqué
        pass
    except Exception as e:
        raise self.retry(exc=e, countdown=60)
```

### **Celery est-il la seule option ?**

Non. Il y a aussi Django Q, Dramatiq et Huey. Mais Celery est le plus mature et possède la plus grande communauté.

## Conclusion

Utiliser Celery dans Django ne fait pas que accélérer les choses – cela aide également à améliorer l'expérience pour vos utilisateurs.

Déléguer les tâches lourdes ou lentes rend votre application plus réactive et plus fiable.

Une fois que vous maîtrisez les bases, vous trouverez de nombreuses utilisations pour Celery.

### Lectures et ressources supplémentaires

* [Documentation Celery](https://docs.celeryq.dev/en/stable/)
    
* [Guide de démarrage rapide Redis](https://redis.io/docs/latest/develop/get-started/)
    
* [django-celery-results](https://github.com/celery/django-celery-results)
    
* [Tâches asynchrones dans Django (Real Python)](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
    
* [Surveillance Celery avec Flower](https://flower.readthedocs.io/en/latest/)