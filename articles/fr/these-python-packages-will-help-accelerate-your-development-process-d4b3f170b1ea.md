---
title: 10 packages Python externes que vous allez adorer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T15:22:39.000Z'
originalURL: https://freecodecamp.org/news/these-python-packages-will-help-accelerate-your-development-process-d4b3f170b1ea
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Metg2GPm6OTYWKZh
tags:
- name: code
  slug: code
- name: development
  slug: development
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: 10 packages Python externes que vous allez adorer
seo_desc: 'By Adam Goldschmidt


  Python is an experiment in how much freedom programmers need. Too much freedom and
  nobody can read another’s code; too little and expressiveness is endangered. - Guido
  van Rossum


  This freedom that Guido talks about is part of wh...'
---

Par Adam Goldschmidt

> Python est une expérience sur la quantité de liberté dont les programmeurs ont besoin. Trop de liberté et personne ne peut lire le code d'un autre ; trop peu et l'expressivité est en danger. - Guido van Rossum

Cette liberté dont parle Guido fait partie de ce qui rend Python si populaire. Cette popularité, entre autres, est ce qui attire de plus en plus de développeurs à utiliser le langage - conduisant finalement à certains projets open source vraiment incroyables.

Je me surprends généralement à chasser des projets sur GitHub une fois par jour. Tout au long de cet article, je vais essayer de couvrir 10 packages merveilleux que vous connaissez peut-être ou non. Je vais commencer par les moins tendance et finir par... eh bien, Flask.

### Commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/oGpPuDrsAM6KYONzQCrIZXv1xAEIv-oVuIUT)

#### [Loguru](https://github.com/Delgan/loguru) — Journalisation simplifiée

![Image](https://cdn-media-1.freecodecamp.org/images/DWrohhPZvoWbH4s8apMbg8nXZOtf3m0lAhvk)

Ce package est vraiment génial et je l'utilise régulièrement dans mes projets. Il se décrit comme « une bibliothèque qui vise à apporter une journalisation agréable en Python ». Ce package vous permet simplement de configurer facilement vos journaux dès la sortie de la boîte.

Tout ce que vous avez à faire après l'installation est d'importer le module :

```
from loguru import logger
```

Et vous êtes libre de l'utiliser dès la sortie de la boîte :

```
logger.debug("Bonjour, débogueur cool")
```

La documentation est bonne et il y a de nombreuses options de personnalisation.

#### [more-itertools](https://github.com/erikrose/more-itertools)

Une variété de méthodes intéressantes qui peuvent parfois s'avérer très utiles, comme `peekable` :

```
>>> p = peekable(['a', 'b'])
>>> p.peek()
'a'
>>> next(p)
'a'
```

ou `chunked` :

```
>>> list(chunked([1, 2, 3, 4, 5, 6], 3))
[[1, 2, 3], [4, 5, 6]]
```

#### [MonkeyType](https://github.com/Instagram/MonkeyType) — Générateur d'annotations de types statiques

```
monkeytype run myscript.py
```

Ce package génère automatiquement des annotations de types pour vous, soit dans un fichier stub, soit dans le code source lui-même, en collectant les types d'exécution. Oui, Python ne vous oblige pas à utiliser des annotations — mais je crois qu'elles sont très importantes pour la lisibilité du code (et parfois pour éviter des erreurs), ce qui explique également pourquoi il y a 2 autres packages dans cette liste qui gèrent les annotations de types :)

#### [Pyright](https://github.com/Microsoft/pyright) — Vérificateur de types statiques

![Image](https://cdn-media-1.freecodecamp.org/images/B5KVRNqA90q0PqVY18dvfvc7m7rbjYYVf1EP)

Nouveau package passionnant venant de Microsoft. Le commit initial date de seulement 17 jours ! Ce package est le concurrent de Mypy (également dans cette liste). Pour être honnête, je n'ai pas encore eu l'occasion de l'utiliser, mais je prévois définitivement de le faire. J'utilise actuellement mypy comme vérificateur de types, mais je vais essayer celui-ci !

#### [requests-async](https://github.com/encode/requests-async) — support pour la syntaxe `async`/`await` pour `requests`

Ce package est nouveau et je l'ai découvert l'autre jour sur GitHub, et il semble très prometteur. Nous connaissons tous le package [requests](https://github.com/kennethreitz/requests), qui nous permet de gérer facilement les requêtes HTTP dans notre code. Eh bien, ce package implémente les mots `async` et `await` pour ces requêtes :

```
import requests_async as requests
response = await requests.get('https://example.org')
print(response.status_code)
print(response.text)
```

Plutôt cool, non ?

#### [HTTPie](https://github.com/jakubroztocil/httpie) — cURL moderne en ligne de commande

![Image](https://cdn-media-1.freecodecamp.org/images/UAD--5ZtcqjDRRKA4Y1oXEWzob6GTM94sXGa)

Ceux d'entre vous qui ont utilisé cURL auparavant doivent savoir que ce n'est pas très amusant. Devoir se souvenir des noms des paramètres, s'assurer que vos données sont encapsulées... Eh bien, HTTPie vise à rendre cela beaucoup plus facile. Voici l'un de leurs exemples, pour soumettre des données de formulaire :

```
http -f POST example.org hello=World
```

#### [pipenv](https://github.com/pypa/pipenv) — Meilleur packaging pour Python

Lorsque je commence un nouveau projet, je crée toujours un nouvel environnement `virtualenv` et j'installe quelques packages de base avec `pip`. Je dois ensuite enregistrer ces noms de packages dans un fichier, qu'il s'agisse de `setup.py` ou de `requirements.txt`. Ceux d'entre vous qui ont travaillé avec `npm` savent que c'est beaucoup plus simple là-bas. Tout ce que vous avez à faire est d'écrire `npm --save` et le nom du package est enregistré dans votre `package.json`. C'est pourquoi j'ai d'abord créé [pypkgfreeze](https://github.com/AdamGold/pypkgfreeze), un package simple pour « geler » les versions de vos packages `pip` actuellement utilisés dans `setup.py`.

En tout cas, pipenv est une solution intéressante qui vise à fusionner les deux mondes - Ils le décrivent le mieux dans leur page de dépôt :

Il crée et gère automatiquement un virtualenv pour vos projets, ainsi qu'ajoute/supprime des packages de votre `Pipfile` lorsque vous installez/désinstallez des packages. Il génère également le très important `Pipfile.lock`, qui est utilisé pour produire des builds déterministes.

Vous pouvez l'essayer [ici](https://rootnroll.com/d/pipenv/).

#### [mypy](https://github.com/python/mypy) — Vérificateur de types statiques

Comme je l'ai dit auparavant, c'est le package que j'utilise actuellement comme mon vérificateur de types statiques standard. Il m'aide à garder mon code lisible et élégant (je pense).

#### [black](https://github.com/ambv/black)

![Image](https://cdn-media-1.freecodecamp.org/images/dQoUny7l5N6sWs2GCECZKHALf59t9398hNNp)

J'ai essayé de nombreux formateurs Python, et `black` est clairement mon préféré. La syntaxe semble soignée, et la ligne de commande s'exécute rapidement et peut soit vérifier les fichiers, soit les éditer réellement - très utile pour le CI/CD. Vous pouvez même l'essayer [ici !](https://www.freecodecamp.org/news/these-python-packages-will-help-accelerate-your-development-process-d4b3f170b1ea/%5Bhttps://black.now.sh%5D(https://black.now.sh/))

#### [flask](https://github.com/pallets/flask)

Je ne suis pas sûr d'avoir quelque chose à écrire ici qui n'a pas déjà été écrit auparavant. Vous connaissez probablement ce micro framework étonnant, et si ce n'est pas le cas... vous devriez définitivement le vérifier.

### Avant de partir...

Merci d'avoir lu ! Vous pouvez suivre mon compte [GitHub](https://github.com/AdamGold) pour plus de dépôts cool. J'ai tendance à mettre une étoile à chaque chose cool que je vois :)

Si vous avez aimé cet article, veuillez maintenir le bouton d'applaudissements ? enfoncé pour aider les autres à le trouver. Plus vous le maintenez enfoncé, plus vous donnez d'applaudissements !

Et n'hésitez pas à partager vos pensées dans les commentaires ci-dessous.