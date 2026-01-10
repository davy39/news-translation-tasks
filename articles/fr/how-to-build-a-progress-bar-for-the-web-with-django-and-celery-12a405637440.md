---
title: Comment créer une barre de progression pour le web avec Django et Celery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T22:28:04.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-progress-bar-for-the-web-with-django-and-celery-12a405637440
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nTguNDWHvIC8Tjg5.jpg
tags:
- name: Django
  slug: django
- name: open source
  slug: open-source
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment créer une barre de progression pour le web avec Django et Celery
seo_desc: 'By Cory Zue

  The surprising complexity of making something that is, on its surface, ridiculously
  simple

  Progress bars are one of the most common, familiar UI components in our lives. We
  see them every time we download a file, install software, or atta...'
---

Par Cory Zue

#### La complexité surprenante de créer quelque chose qui, en apparence, est ridiculement simple

Les barres de progression sont l'un des composants d'interface utilisateur les plus courants et familiers de notre vie quotidienne. Nous les voyons chaque fois que nous téléchargeons un fichier, installons un logiciel ou attachons quelque chose à un email. Elles sont présentes dans nos navigateurs, sur nos téléphones et même sur nos téléviseurs.

Et pourtant — créer une bonne barre de progression est une tâche surprenamment complexe !

Dans cet article, je vais décrire tous les composants nécessaires pour créer une barre de progression de qualité pour le web, et j'espère qu'à la fin, vous aurez une bonne compréhension de tout ce dont vous avez besoin pour construire la vôtre.

Cet article décrit tout ce que j'ai dû apprendre (et certaines choses que je n'ai pas apprises !) pour créer [celery-progress](https://github.com/czue/celery-progress), une bibliothèque qui, je l'espère, facilite l'ajout de barres de progression sans dépendances à vos applications Django/Celery.

Cela dit, la plupart des concepts de cet article devraient s'appliquer à tous les langages/environnements, donc même si vous n'utilisez pas Python, vous pouvez probablement apprendre quelque chose de nouveau.

### Pourquoi les barres de progression ?

Cela peut sembler évident, mais pour être clair — pourquoi utilisons-nous des barres de progression ?

La raison principale est de fournir un retour aux utilisateurs pour quelque chose qui prend plus de temps qu'ils ne sont habitués à attendre. Selon [kissmetrics](https://blog.kissmetrics.com/loading-time/), 40 % des personnes abandonnent un site web qui met plus de 3 secondes à charger ! Et bien que vous puissiez utiliser quelque chose comme un spinner pour aider à atténuer cette attente, une méthode éprouvée pour communiquer avec vos utilisateurs pendant qu'ils attendent que quelque chose se produise est d'utiliser une barre de progression.

Généralement, les barres de progression sont idéales **chaque fois que quelque chose prend plus de quelques secondes** et que vous pouvez raisonnablement estimer sa progression dans le temps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*WJEBvtRFE5PngHGD.png)
_Les barres de progression peuvent être utilisées pour montrer l'état d'avancement de quelque chose et son résultat_

Quelques exemples incluent :

* Lorsque votre application se charge pour la première fois (si elle prend beaucoup de temps à charger)
* Lors du traitement d'une grande importation de données
* Lors de la préparation d'un fichier pour le téléchargement
* Lorsque l'utilisateur est dans une file d'attente en attendant que sa demande soit traitée

### Les composants d'une barre de progression

D'accord, maintenant que cela est clair, passons à la manière de construire ces choses !

Ce n'est qu'une petite barre qui se remplit à travers un écran. À quel point cela peut-il être compliqué ?

En réalité, assez !

Les composants suivants font généralement partie de toute implémentation de barre de progression :

1. Un **front-end**, qui inclut généralement une représentation visuelle de la progression et (optionnellement) un statut basé sur du texte.
2. Un **back-end** qui effectuera réellement le travail que vous souhaitez surveiller.
3. Un ou plusieurs canaux de communication pour que le front-end transmette le travail au back-end.
4. Un ou plusieurs canaux de communication pour que le back-end communique la progression au front-end.

Nous pouvons immédiatement voir une source inhérente de complexité. Nous voulons à la fois **effectuer un travail** dans le back-end et **montrer ce travail** en cours sur le front-end. Cela signifie immédiatement que nous impliquerons plusieurs processus qui doivent interagir de manière asynchrone.

Ces canaux de communication sont là où réside une grande partie de la complexité. Dans un projet Django relativement standard, le **navigateur front-end** pourrait soumettre une requête AJAX HTTP (JavaScript) à l'**application web back-end** (Django). Cela pourrait à son tour transmettre cette requête à la **file d'attente des tâches** (Celery) via un **courtier de messages** (RabbitMQ/Redis). Ensuite, tout le processus doit se produire en sens inverse pour obtenir des informations en retour vers le front-end !

L'ensemble du processus pourrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*HyHRRP7IP2sx1FmG.png)
_La vue d'ensemble de tout ce qui est impliqué dans la création d'une bonne barre de progression_

Plongeons dans tous ces composants et voyons comment ils fonctionnent dans un exemple pratique.

### Le Front End

Le front-end est définitivement la partie la plus facile de la barre de progression. Avec seulement quelques lignes de HTML/CSS, vous pouvez rapidement créer une barre horizontale décente en utilisant les attributs de couleur de fond et de largeur. Ajoutez un peu de JavaScript pour la mettre à jour et vous êtes prêt à partir !

```js
function updateProgress(progressBarElement, progressBarMessageElement, progress) {
  progressBarElement.style.backgroundColor = '#68a9ef';
  progressBarElement.style.width = progress.percent + "%";
  progressBarMessageElement.innerHTML = progress.current + ' sur ' + progress.total + ' traités.';
}

var trigger = document.getElementById('progress-bar-trigger');
trigger.addEventListener('click', function(e) {
  var barWrapper = document.getElementById('progress-wrapper');
  barWrapper.style.display = 'inherit'; // afficher la barre
  var bar = document.getElementById("progress-bar");
  var barMessage = document.getElementById("progress-bar-message");
  for (var i = 0; i < 11; i++) {
    setTimeout(updateProgress, 500 * i, bar, barMessage, {
      percent: 10 * i,
      current: 10 * i,
      total: 100
    })
  }
})
```

### Le Backend

Le backend est tout aussi simple. Il s'agit essentiellement de code qui sera exécuté sur votre serveur pour effectuer le travail que vous souhaitez suivre. Cela serait généralement écrit dans la pile d'application que vous utilisez (dans ce cas, Python et Django). Voici une version simplifiée de ce à quoi le backend pourrait ressembler :

```python
def do_work(self, list_of_work): 
    for work_item in list_of_work: 
        do_work_item(work_item) 
    return 'le travail est terminé'
```

### Effectuer le travail

D'accord, nous avons donc notre barre de progression front-end et notre exécutant de travail. Qu'est-ce qui suit ?

Eh bien, nous n'avons pas encore dit comment ce travail sera lancé. Commençons donc par là.

#### La mauvaise façon : le faire dans l'application web

Dans un flux de travail Ajax typique, cela fonctionnerait de la manière suivante :

1. Le front-end initie une requête à l'application web
2. L'application web effectue le travail dans la requête
3. L'application web retourne une réponse une fois terminé

Dans une vue Django, cela ressemblerait à ceci :

```python
def my_view(request): 
    do_work() 
    return HttpResponse('travail terminé !')
```

#### _La mauvaise façon : appeler la fonction depuis la vue_

Le problème ici est que la fonction `do_work` peut effectuer beaucoup de travail qui prend beaucoup de temps (sinon, cela n'aurait pas de sens d'ajouter une barre de progression pour cela).

Effectuer beaucoup de travail dans une vue est généralement considéré comme une mauvaise pratique pour plusieurs raisons, notamment :

* Vous créez une mauvaise expérience utilisateur, car les gens doivent attendre que les longues requêtes se terminent
* Vous exposez votre site à des problèmes de stabilité potentiels avec de nombreuses requêtes longues et en cours d'exécution (qui pourraient être déclenchées soit malicieusement, soit accidentellement)

Pour ces raisons, et d'autres, nous avons besoin d'une meilleure approche pour cela.

#### La meilleure façon : les files d'attente de tâches asynchrones (aka Celery)

La plupart des frameworks web modernes ont créé des **files d'attente de tâches asynchrones** pour traiter ce problème. En Python, le plus courant est [Celery](http://www.celeryproject.org/). En Rails, il y a [Sidekiq](https://sidekiq.org/) ([parmi d'autres](http://blog.scoutapp.com/articles/2016/02/16/which-ruby-background-job-framework-is-right-for-you)).

Les détails entre ces frameworks varient, mais les principes fondamentaux sont les mêmes. Basiquement, au lieu d'effectuer un travail dans une requête HTTP qui pourrait prendre un temps arbitrairement long — et être déclenchée avec une fréquence arbitraire — vous placez ce travail dans une file d'attente et vous avez des processus en arrière-plan — souvent appelés **workers** — qui prennent les tâches et les exécutent.

Cette architecture asynchrone présente plusieurs avantages, notamment :

* Ne pas effectuer de travail long dans les processus web
* Permettre la limitation du débit du travail effectué — le travail peut être limité par le nombre de processus workers disponibles
* Permettre au travail de se faire sur des machines optimisées pour cela, par exemple, des machines avec un grand nombre de CPU

### Les mécanismes des tâches asynchrones

Les mécanismes de base d'une architecture asynchrone sont relativement simples et impliquent trois composants principaux : **le(s) client(s)**, le(s) **worker(s)**, et le **courtier de messages**.

Le **client** est principalement responsable de la création de nouvelles tâches. Dans notre exemple, le client est l'application Django, qui crée des tâches sur l'entrée de l'utilisateur via une requête web.

Les **workers** sont les processus réels qui effectuent le travail. Ce sont nos workers Celery. Vous pouvez avoir un nombre arbitraire de workers en cours d'exécution sur autant de machines que vous le souhaitez, ce qui permet une haute disponibilité et une mise à l'échelle horizontale du traitement des tâches.

Le client et la file d'attente des tâches communiquent entre eux via un **courtier de messages**, qui est responsable de l'acceptation des tâches du ou des clients et de leur livraison aux workers. Le courtier de messages le plus courant pour Celery est RabbitMQ, bien que Redis soit également un courtier de messages couramment utilisé et complet.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JObuxAwuSA1juG4N.png)
_Flux de travail de base pour transmettre des messages à un processus worker asynchrone_

Lors de la création d'une application Celery standard, vous développerez généralement le code client et worker, mais le courtier de messages sera une pièce d'infrastructure que vous devrez simplement mettre en place (et au-delà de cela, vous pourrez [pour la plupart] l'ignorer).

#### Un exemple

Bien que cela semble plutôt compliqué, Celery fait un bon travail pour nous faciliter la tâche grâce à de belles abstractions de programmation.

Pour convertir notre fonction de travail en quelque chose qui peut être exécuté de manière asynchrone, tout ce que nous avons à faire est d'ajouter un décorateur spécial :

```python
from celery import task 
# ce décorateur est tout ce dont vous avez besoin pour dire à celery que ceci est une
# tâche worker
@task 
def do_work(self, list_of_work): 
    for work_item in list_of_work: 
        do_work_item(work_item) 
    return 'le travail est terminé'
```

#### _Annotation d'une fonction de travail pour être appelée depuis Celery_

De même, l'appel de la fonction de manière asynchrone depuis le client Django est tout aussi simple :

```python
def my_view(request): 
    # l'appel .delay() ici est tout ce dont vous avez besoin
    # pour convertir la fonction en appel asynchrone     
    do_work.delay() 
    # nous ne pouvons plus dire 'travail terminé' ici
    # car tout ce que nous avons fait, c'est le lancer 
    return HttpResponse('travail lancé !')
```

#### _Appel de la fonction de travail de manière asynchrone_

Avec seulement quelques lignes de code supplémentaires, nous avons converti notre travail en une architecture asynchrone ! Tant que vous avez configuré et lancé vos processus worker et broker, cela devrait _simplement fonctionner_.

### Suivi de la progression

D'accord, nous avons enfin notre tâche qui s'exécute en arrière-plan. Mais maintenant, nous voulons suivre sa progression. Alors, comment cela fonctionne-t-il exactement ?

Nous devrons à nouveau faire quelques choses. D'abord, nous aurons besoin d'un moyen de suivre la progression dans le travail du worker. Ensuite, nous devrons communiquer cette progression jusqu'à notre front-end afin de pouvoir mettre à jour la barre de progression sur la page. Une fois de plus, cela s'avère être bien plus compliqué que vous ne le pensez !

#### Utilisation d'un objet observateur pour suivre la progression dans le worker

Les lecteurs du livre séminal [Design Patterns du Gang of Four](https://www.amazon.com/gp/product/0201633612/) pourraient être familiers avec le [modèle observateur](https://en.wikipedia.org/wiki/Observer_pattern). Le modèle observateur typique inclut un **sujet** qui suit l'état, ainsi qu'un ou plusieurs **observateurs** qui font quelque chose en réponse à l'état. Dans notre scénario de progression, le sujet est le processus/fonction worker qui effectue le travail, et l'observateur est la chose qui va suivre la progression.

Il existe de nombreuses façons de lier le sujet et l'observateur, mais la plus simple est de simplement passer l'observateur en tant qu'argument à la fonction qui effectue le travail.

Cela ressemble à ceci :

```
@task 
def do_work(self, list_of_work, progress_observer):     
    total_work_to_do = len(list_of_work)     
    for i, work_item in enumerate(list_of_work):             
        do_work_item(work_item)         
        # dire à l'observateur de progression combien d'éléments sur le total
        # nous avons traités
        progress_observer.set_progress(i, total_work_to_do)        
    return 'le travail est terminé'
```

#### _Utilisation d'un observateur pour surveiller la progression du travail_

Maintenant, tout ce que nous avons à faire est de passer un `progress_observer` valide et voilà, notre progression sera suivie !

### Obtenir la progression de retour vers le client

Vous pourriez penser _"attendez une minute... vous venez d'appeler une fonction appelée set_progress, vous n'avez rien fait en réalité !"_

Vrai ! Alors, comment cela fonctionne-t-il _réellement_ ?

Rappelez-vous — notre objectif est d'obtenir ces informations de progression jusqu'à la page web afin que nous puissions montrer à nos utilisateurs ce qui se passe. Mais le suivi de la progression se fait entièrement dans le processus worker ! Nous sommes maintenant confrontés à un problème similaire à celui que nous avions avec la transmission de la tâche asynchrone précédemment.

Heureusement, Celery fournit également un mécanisme pour transmettre des messages **en retour** au client. Cela se fait via un mécanisme appelé [result backends](http://docs.celeryproject.org/en/latest/userguide/tasks.html#result-backends), et, comme les [brokers](http://docs.celeryproject.org/en/latest/getting-started/brokers/), vous avez le choix entre plusieurs backends différents. RabbitMQ et Redis peuvent être utilisés comme brokers et result backends et sont des choix raisonnables, bien qu'il n'y ait techniquement aucun couplage entre le broker et le result backend.

En tout cas, comme pour les brokers, les détails ne se posent généralement pas à moins que vous ne fassiez quelque chose de assez avancé. Mais l'idée est que vous stockez le résultat de la tâche _quelque part_ (avec l'ID unique de la tâche), et ensuite d'autres processus peuvent obtenir des informations sur les tâches par ID en demandant au backend.

Dans Celery, cela est bien abstrait via l'`state` associé à la tâche. L'`state` nous permet de définir un statut global, ainsi que d'attacher des métadonnées arbitraires à la tâche. C'est un endroit parfait pour stocker notre progression actuelle et totale.

#### Définir l'état

```python
task.update_state( 
    state=PROGRESS_STATE, 
    meta={'current': current, 'total': total} 
)
```

#### Lire l'état

```python
from celery.result import AsyncResult 
result = AsyncResult(task_id) 
print(result.state) # sera défini sur PROGRESS_STATE print(result.info) # les métadonnées seront ici
```

### Obtenir les mises à jour de progression vers le front-end

Maintenant que nous pouvons obtenir des mises à jour de progression depuis les workers/tâches et les transmettre à n'importe quel autre client, la dernière étape consiste simplement à obtenir ces informations vers le front-end et à les afficher à l'utilisateur.

Si vous voulez faire quelque chose de plus sophistiqué, vous pouvez utiliser quelque chose comme les websockets pour le faire en temps réel. Mais la version la plus simple consiste simplement à interroger une URL de temps en temps pour vérifier la progression. Nous pouvons simplement servir les informations de progression sous forme de JSON via une vue Django et les traiter et les rendre côté client.

Vue Django :

```python
def get_progress(request, task_id): 
    result = AsyncResult(task_id) 
    response_data = { 
        'state': result.state, 
        'details': self.result.info,
    } 
    return HttpResponse(
        json.dumps(response_data), 
        content_type='application/json'
    )
```

**Vue Django pour retourner la progression en JSON.**

Code JavaScript :

```python
function updateProgress (progressUrl) {
    fetch(progressUrl).then(function(response) { 
        response.json().then(function(data) { 
            // mettre à jour les composants UI appropriés 
            setProgress(data.state, data.details); 
            // et le refaire toutes les demi-secondes
            setTimeout(updateProgress, 500, progressUrl); 
        }); 
    }); 
}
```

**Code JavaScript pour interroger la progression et mettre à jour l'UI.**

### Mettre tout ensemble

Cela a été beaucoup de détails sur quelque chose qui — en apparence — est une partie très simple et quotidienne de notre vie avec les ordinateurs ! J'espère que vous avez appris quelque chose.

Si vous avez besoin d'une manière simple de créer des barres de progression pour vos applications Django/Celery, vous pouvez consulter [celery-progress](https://github.com/czue/celery-progress) — une bibliothèque que j'ai écrite pour aider à rendre tout cela un peu plus facile. Il y a aussi [une démonstration de son fonctionnement sur Build with Django](https://buildwithdjango.com/projects/celery-progress/).

Merci d'avoir lu ! Si vous souhaitez être informé chaque fois que je publie du contenu comme celui-ci sur la construction de choses avec Python et Django, veuillez vous inscrire pour recevoir des mises à jour ci-dessous !

_Originalement publié sur [buildwithdjango.com](https://buildwithdjango.com/blog/post/celery-progress-bars/).