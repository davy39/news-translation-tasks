---
title: 'Docker 101 : Fondamentaux et Pratique'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-14T22:54:17.000Z'
originalURL: https://freecodecamp.org/news/docker-101-fundamentals-and-practice-edb047b71a51
coverImage: https://cdn-media-1.freecodecamp.org/images/0*mgaoUlIJzr502lhY.jpg
tags:
- name: Docker
  slug: docker
- name: nginx
  slug: nginx
- name: Productivity
  slug: productivity
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Docker 101 : Fondamentaux et Pratique'
seo_desc: 'By Guilherme Pejon

  If you''re tired of hearing your coworkers praise Docker and its benefits at every
  chance they get, or you''re tired of nodding your head and walking away every time
  you find yourself in one of these conversations, you''ve come to the...'
---

Par Guilherme Pejon

Si vous en avez assez d'entendre vos collègues vanter Docker et ses avantages à chaque occasion, ou si vous en avez assez de hocher la tête et de vous éloigner chaque fois que vous vous retrouvez dans une de ces conversations, vous êtes au bon endroit.

De plus, si vous cherchez une nouvelle excuse pour vous éloigner sans vous faire virer, continuez à lire et vous me remercierez plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/GXyh0RbblBFolxVst-ZN6DWd3CnUk5aREezM)
_Source : [developermemes](http://www.developermemes.com" rel="noopener" target="_blank" title=")_

### Docker

Voici la définition de Docker, selon [Wikipedia](https://en.wikipedia.org/wiki/Docker_(software)) :

> Docker est un programme informatique qui effectue de la virtualisation au niveau du système d'exploitation.

Assez simple, n'est-ce pas ? Eh bien, pas exactement. Voici ma définition de ce qu'est Docker :

> Docker est une plateforme pour créer et exécuter des **conteneurs** à partir d'**images**.

Toujours perdu ? Pas de souci, c'est probablement parce que vous ne savez pas ce que sont les **conteneurs** ou les **images**.

Les **images** sont des fichiers uniques contenant toutes les dépendances et configurations nécessaires pour exécuter un programme, tandis que les **conteneurs** sont les instances de ces images. Allons-y et voyons un exemple de cela en pratique pour clarifier les choses.

> **Note importante :** Avant de continuer, assurez-vous d'[installer Docker](https://docs.docker.com/install/) en utilisant les étapes recommandées pour votre système d'exploitation.

### Partie 1. "Hello, World!" à partir d'une image Python

Imaginons que vous n'avez pas Python installé sur votre machine — ou au moins pas la dernière version — et que vous avez besoin de Python pour afficher "Hello, World!" dans votre terminal. Que faites-vous ? Vous utilisez Docker !

Allez-y et exécutez la commande suivante :

```
docker run --rm -it python:3 python
```

Ne vous inquiétez pas, je vais expliquer cette commande dans un instant, mais pour l'instant, vous voyez probablement quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/i7DalGXQXEQYdUQS2FMMsn0x62Kz1KSq8Igx)
_Cela peut prendre quelques instants pour que cette commande s'exécute pour la première fois_

Cela signifie que nous sommes actuellement à l'intérieur d'un **conteneur Docker** créé à partir d'une **image Docker** Python 3, exécutant la commande `python`. Pour terminer l'exemple, tapez `print("Hello, World!")` et regardez la magie opérer.

![Image](https://cdn-media-1.freecodecamp.org/images/A-pKIHg3d-pdx9vDt50v3bmW6z0JTTde5X-P)
_Un "Hello, World!". Wow !_

D'accord, vous l'avez fait, mais avant de vous féliciter, prenons un peu de recul et comprenons comment cela a fonctionné.

#### **Décortiquons cela**

Commençons par le début. La commande `docker run` est l'outil standard de Docker pour vous aider à démarrer et exécuter vos conteneurs.

Le drapeau `--rm` est là pour dire au démon Docker de nettoyer le conteneur et de supprimer le système de fichiers après la sortie du conteneur. Cela vous aide à économiser de l'espace disque après avoir exécuté des conteneurs éphémères comme celui-ci, que nous avons démarré uniquement pour afficher "Hello, World!".

Le drapeau `-t (ou --tty)` indique à Docker d'allouer une session de terminal virtuel dans le conteneur. Cela est couramment utilisé avec l'option `-i (ou --interactive)`, qui maintient STDIN ouvert même en mode détaché (plus à ce sujet plus tard).

> **Note :** Ne vous inquiétez pas trop de ces définitions pour l'instant. Sachez simplement que vous utiliserez le drapeau `-it` chaque fois que vous voudrez taper des commandes sur votre conteneur.

Enfin, `python:3` est l'image de base que nous avons utilisée pour ce conteneur. Pour l'instant, cette image contient Python version 3.7.3 installé, entre autres. Vous vous demandez peut-être d'où vient cette image et ce qu'elle contient. Vous pouvez trouver les réponses à ces deux questions juste [ici](https://hub.docker.com/_/python/), ainsi que toutes les autres images Python que nous aurions pu utiliser pour cet exemple.

Enfin, mais non des moindres, `python` était la commande que nous avons demandée à Docker d'exécuter à l'intérieur de notre image `python:3`, ce qui a démarré un shell Python et permis à notre appel `print("Hello, World!")` de fonctionner.

#### Une dernière chose

Pour quitter Python et terminer notre conteneur, vous pouvez utiliser CTRL/CMD + D ou `exit()`. Allez-y et faites cela maintenant. Après cela, essayez d'exécuter à nouveau notre commande `docker run` et vous verrez quelque chose de légèrement différent, et beaucoup plus rapide.

![Image](https://cdn-media-1.freecodecamp.org/images/PjuutqjPnUNWh3q5mgQjJ0hs9qEqfPgJAlG1)
_Bien plus rapide. Wow !_

C'est parce que nous avons déjà téléchargé l'image `python:3`, donc notre conteneur démarre beaucoup plus rapidement maintenant.

### Partie 2. "Hello World!" automatisé à partir d'une image Python

Quoi de mieux que d'écrire "Hello, World!" dans votre terminal une fois ? Vous l'avez deviné, l'écrire deux fois !

Puisque nous ne pouvons pas attendre de voir "Hello, World!" imprimé à nouveau dans notre terminal, et que nous ne voulons pas nous donner la peine d'ouvrir Python et de taper `print` à nouveau, allons-y et automatisons un peu ce processus. Commencez par créer un fichier `hello.py` n'importe où vous le souhaitez.

```
# hello.py
```

```
print("Hello, World!")
```

Ensuite, allez-y et exécutez la commande suivante à partir de ce même dossier.

```
docker run --rm -it -v $(pwd):/src python:3 python /src/hello.py
```

Voici le résultat que nous recherchons :

![Image](https://cdn-media-1.freecodecamp.org/images/NEXiMrDxjadvG2DEDuGRSXg05HsDuqA5QAju)
_Génial ! YAHW (Yet Another "Hello World!")_

> **Note :** J'ai utilisé `ls` avant la commande pour vous montrer que j'étais dans le même dossier que celui où j'ai créé le fichier `hello.py`.

Comme nous l'avons fait précédemment, prenons un peu de recul et comprenons comment cela a fonctionné.

#### Décortiquons cela

Nous exécutons presque la même commande que celle que nous avons exécutée dans la dernière section, à l'exception de deux choses.

L'option `-v $(pwd):/src` indique au démon Docker de démarrer un **volume** dans notre conteneur. Les volumes sont le meilleur moyen de persister des données dans Docker. Dans cet exemple, nous disons à Docker que nous voulons que le répertoire courant — récupéré à partir de `$(pwd)` — soit ajouté à notre conteneur dans le dossier `/src`.

> **Note :** Vous pouvez utiliser n'importe quel autre nom ou dossier que vous souhaitez, pas seulement `/src`.

Si vous voulez vérifier que `/src/hello.py` existe réellement à l'intérieur de notre conteneur, vous pouvez changer la fin de notre commande de `python hello.py` à `bash`. Cela ouvrira un shell interactif à l'intérieur de notre conteneur, et vous pourrez l'utiliser comme vous l'attendez.

![Image](https://cdn-media-1.freecodecamp.org/images/IbjkecLbC0HhtIFcvHz7IYEEubn05ZU1Gnkt)
_Ce n'est pas fou ?_

> **Note :** Nous pouvons utiliser `bash` ici parce qu'il est préinstallé dans l'image `python:3`. Certaines images sont si simples qu'elles n'ont même pas `bash`. Cela ne signifie pas que vous ne pouvez pas l'utiliser, mais vous devrez l'installer vous-même si vous le souhaitez.

Le dernier morceau de notre commande est l'instruction `python /src/hello.py`. En l'exécutant, nous disons à notre conteneur de chercher à l'intérieur de son dossier `/src` et d'exécuter le fichier `hello.py` en utilisant `python`.

Peut-être pouvez-vous déjà voir les merveilles que vous pouvez faire avec ce pouvoir, mais je vais les souligner pour vous quand même. En utilisant ce que nous venons d'apprendre, nous pouvons exécuter **n'importe quel code** à partir de **n'importe quel langage** à l'intérieur de **n'importe quel ordinateur** sans avoir à installer **aucune dépendance** sur la machine hôte — sauf Docker, bien sûr. C'est beaucoup de **texte en gras** pour une seule phrase, alors assurez-vous de la lire deux fois !

### Partie 3. Le "Hello, World!" le plus simple possible à partir d'une image Python en utilisant Dockerfile

En avez-vous assez de dire bonjour à notre belle planète ? C'est dommage, car nous allons le faire à nouveau !

La dernière commande que nous avons apprise était un peu verbeuse, et je peux déjà me voir me lasser de taper tout ce code chaque fois que je veux dire "Hello, World!" Automatisons un peu plus les choses maintenant. Créez un fichier nommé `Dockerfile` et ajoutez le contenu suivant :

```
# Dockerfile
```

```
FROM python:3
```

```
WORKDIR /src/app
```

```
COPY . .
```

```
CMD [ "python", "./hello.py" ]
```

Maintenant, exécutez cette commande dans le même dossier où vous avez créé le `Dockerfile` :

```
docker build -t hello .
```

Il ne reste plus qu'à utiliser ce code :

```
docker run hello
```

![Image](https://cdn-media-1.freecodecamp.org/images/xkJM8U1zy7RgVHoFgMXr1ZbRxRmynsDIz1Jr)
_Notez que vous n'avez même plus besoin d'être dans le même dossier_

Vous savez déjà comment cela fonctionne. Prenons un moment pour comprendre comment fonctionne un Dockerfile maintenant.

#### Décortiquons cela

Commençons par notre Dockerfile, la première ligne `FROM python:3` indique à Docker de tout commencer avec l'image de base que nous connaissons déjà, `python:3`.

La deuxième ligne, `WORKDIR /src/app`, définit le répertoire de travail à l'intérieur de notre conteneur. Cela est pour certaines instructions que nous exécuterons plus tard, comme `CMD` ou `COPY`. Vous pouvez voir le reste des instructions prises en charge pour `WORKDIR` juste [ici](https://docs.docker.com/engine/reference/builder/#workdir).

La troisième ligne, `COPY . .` indique essentiellement à Docker de copier tout depuis notre dossier courant (premier `.`), et de le coller dans `/src/app` (deuxième `.`). L'emplacement de collage a été défini avec la commande `WORKDIR` juste au-dessus.

> **Note :** Nous aurions pu obtenir les mêmes résultats en supprimant l'instruction `WORKDIR` et en remplaçant l'instruction `COPY . .` par `COPY . /src/app`. Dans ce cas, nous devrions également changer la dernière instruction, `CMD ["python", "./hello.py"]` en `CMD ["python", "/src/app/hello.py"]`.

Enfin, la dernière ligne `CMD ["python", "./hello.py"]` fournit la commande par défaut pour notre conteneur. Elle dit essentiellement que chaque fois que nous exécutons un conteneur à partir de cette configuration, il doit exécuter `python ./hello.py`. Gardez à l'esprit que nous exécutons implicitement `/src/app/hello.py` au lieu de simplement `hello.py`, puisque c'est là que nous avons pointé notre `WORKDIR`.

> **Note :** La commande `CMD` peut être écrasée à l'exécution. Par exemple, si vous voulez exécuter `bash` à la place, vous feriez `docker run hello bash` après avoir construit le conteneur.

Avec notre Dockerfile terminé, nous lançons notre processus de `build`. La commande `docker build -t hello .` lit toute la configuration que nous avons ajoutée à notre Dockerfile et crée une **image Docker** à partir de celle-ci. C'est exact, tout comme l'image `python:3` que nous avons utilisée pour cet article entier. Le `.` à la fin indique à Docker que nous voulons exécuter un Dockerfile à notre emplacement actuel, et l'option `-t hello` donne à cette image le nom `hello`, afin que nous puissions facilement la référencer à l'exécution.

Après tout cela, tout ce que nous avons à faire est d'exécuter l'instruction habituelle `docker run`, mais cette fois avec le nom de l'image `hello` à la fin de la ligne. Cela démarrera un conteneur à partir de l'image que nous avons récemment construite et imprimera enfin le bon vieux "Hello, World!" dans notre terminal.

#### Étendre notre image de base

Que faisons-nous si nous avons besoin d'une dépendance pour exécuter notre code qui n'est pas préinstallée avec notre image de base ? Pour résoudre ce problème, Docker dispose de l'instruction `RUN` [instruction](https://docs.docker.com/engine/reference/builder/#run).

En suivant notre exemple Python, si nous avions besoin de la bibliothèque `numpy` pour exécuter notre code, nous pourrions ajouter l'instruction `RUN` juste après notre commande `FROM`.

```
# Dockerfile
```

```
FROM python:3
```

```
# NOUVELLE LIGNERUN pip3 install numpy
```

```
WORKDIR /src/app
```

```
COPY . .
```

```
CMD [ "python", "./hello.py" ]
```

L'instruction `RUN` donne essentiellement une commande à exécuter par le terminal du conteneur. Ainsi, puisque notre image de base contient déjà `pip3` installé, nous pouvons utiliser `pip3 install numpy`.

> **Note :** Pour une vraie application Python, vous ajouteriez probablement toutes les dépendances dont vous avez besoin à un fichier `requirements.txt`, vous le copieriez dans le conteneur, puis vous mettriez à jour l'instruction `RUN` en `RUN pip3 install -r requirements.txt`.

### Partie 4. "Hello, World!" à partir d'une image Nginx en utilisant un conteneur détaché de longue durée

Je sais que vous en avez probablement assez de m'entendre le dire, mais j'ai encore un "Hello" à dire avant de partir. Allez-y et utilisons notre nouveau pouvoir Docker pour créer un simple conteneur de longue durée, au lieu de ces conteneurs éphémères que nous avons utilisés jusqu'à présent.

Créez un fichier `index.html` dans un nouveau dossier avec le contenu suivant.

```
# index.html
```

```
<h1>Hello, World!</h1>
```

Maintenant, créons un nouveau Dockerfile dans le même dossier.

```
# Dockerfile
```

```
FROM nginx:alpine
```

```
WORKDIR /usr/share/nginx/html
```

```
COPY . .
```

Construisez l'image et donnez-lui le nom `simple_nginx`, comme nous l'avons fait précédemment.

```
docker build -t simple_nginx .
```

Enfin, exécutons notre image nouvellement créée avec la commande suivante :

```
docker run --rm -d -p 8080:80 simple_nginx
```

Vous pensez peut-être qu'il ne s'est rien passé parce que vous êtes de retour à votre terminal, mais examinons de plus près avec la commande `docker ps`.

![Image](https://cdn-media-1.freecodecamp.org/images/dc8GKlsLJ6mKsn7r-6Z6LQQIlKoy9kjUhvxO)
_J'ai dû rogner la sortie, mais vous verrez quelques autres colonnes là-bas_

La commande `docker ps` montre tous les conteneurs en cours d'exécution sur votre machine. Comme vous pouvez le voir sur l'image ci-dessus, j'ai un conteneur nommé `simple_nginx` qui s'exécute sur ma machine en ce moment. Ouvrons un navigateur web et voyons si `nginx` fait son travail en accédant à `localhost:8080`.

![Image](https://cdn-media-1.freecodecamp.org/images/BuDs3TFSrsnUeN3VggrmWNi3GjKTdL5WnQTx)
_Hourra ! (c'est la dernière fois, je promets)_

Tout semble fonctionner comme prévu, et nous servons une page statique via `nginx` qui s'exécute à l'intérieur de notre conteneur. Prenons un moment pour comprendre comment nous avons accompli cela.

#### Décortiquons cela

Je vais sauter l'explication du Dockerfile car nous avons déjà appris ces commandes dans la dernière section. La seule "nouveauté" dans cette configuration est l'image `nginx:alpine`, que vous pouvez lire plus en détail [ici](https://hub.docker.com/_/nginx).

En dehors de ce qui est nouveau, cette configuration fonctionne parce que `nginx` utilise le dossier `usr/share/nginx/html` pour rechercher un fichier `index.html` et commencer à le servir, donc puisque nous avons nommé notre fichier `index.html` et configuré le `WORKDIR` pour être `usr/share/nginx/html`, cette configuration fonctionnera dès la sortie de la boîte.

La commande `build` est exactement comme celle que nous avons utilisée dans la dernière section également, nous utilisons simplement la configuration du Dockerfile pour construire une image avec un certain nom.

Maintenant, pour la partie amusante, l'instruction `docker run --rm -d -p 8080:80 simple_nginx`. Ici, nous avons deux nouveaux drapeaux. Le premier est le drapeau détaché (`-d`), ce qui signifie que nous voulons exécuter ce conteneur en arrière-plan, et c'est pourquoi nous sommes de retour à notre terminal juste après avoir utilisé la commande `docker run`, même si notre conteneur est toujours en cours d'exécution.

Le deuxième nouveau drapeau est l'option `-p 8080:80`. Comme vous l'avez peut-être deviné, il s'agit du drapeau `port`, et il mappe essentiellement le port `8080` de notre machine locale au port `80` à l'intérieur de notre conteneur. Vous auriez pu utiliser n'importe quel autre port au lieu de `8080`, mais vous ne pouvez pas changer le port `80` sans ajouter un paramètre supplémentaire à l'image `nginx`, puisque `80` est le port standard que l'image `nginx` expose.

> **Note :** Si vous voulez arrêter un conteneur détaché comme celui-ci, vous pouvez utiliser la commande `docker ps` pour obtenir le **nom du conteneur** (pas l'image), puis utiliser l'instruction `docker stop` avec le nom du conteneur souhaité à la fin de la ligne.

### Partie 5. La fin

C'est tout ! Si vous lisez encore ceci, vous avez toutes les bases pour commencer à utiliser Docker dès aujourd'hui sur vos projets personnels ou votre travail quotidien.

Faites-moi savoir ce que vous avez pensé de cet article dans les commentaires, et je m'assurerai d'écrire un article de suivi couvrant des sujets plus avancés comme `docker-compose` quelque part dans un avenir proche.

Si vous avez des questions, n'hésitez pas à me le faire savoir.

À votre santé !