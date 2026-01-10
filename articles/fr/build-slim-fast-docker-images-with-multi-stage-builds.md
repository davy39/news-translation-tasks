---
title: Comment construire des images Docker légères et rapides avec des builds multi-étapes
subtitle: ''
author: Daniel Adeboye
co_authors: []
series: null
date: '2025-05-14T15:06:11.140Z'
originalURL: https://freecodecamp.org/news/build-slim-fast-docker-images-with-multi-stage-builds
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1747235146559/0bce7dc3-0abe-4241-a188-1c05c773e810.png
tags:
- name: Docker
  slug: docker
- name: docker images
  slug: docker-images
- name: Dockerfile
  slug: dockerfile
seo_title: Comment construire des images Docker légères et rapides avec des builds
  multi-étapes
seo_desc: 'Apps don’t stay simple forever. More features mean more dependencies, slower
  builds, and heavier Docker images. That’s where things start to hurt.

  Docker helps, but without the right setup, your builds can quickly get bloated.

  Multi-stage builds make...'
---

Les applications ne restent pas simples pour toujours. Plus de fonctionnalités signifie plus de dépendances, des builds plus lents et des images Docker plus lourdes. C'est là que les choses commencent à poser problème.

Docker aide, mais sans la bonne configuration, vos builds peuvent rapidement devenir encombrants.

Les builds multi-étapes rendent les choses plus fluides en gardant vos images rapides, propres et prêtes pour la production. Dans ce guide, vous apprendrez à les utiliser pour optimiser votre workflow Docker.

Commençons.

## Prérequis

Pour suivre ce guide, vous devez avoir :

* Docker installé et en cours d'exécution

* Une compréhension de base de Docker

* Quelques connaissances en Python (ou dans n'importe quel langage, vraiment)

* Une familiarité avec le terminal

## **Voici ce que nous allons couvrir :**

1. [Qu'est-ce que les images Docker ?](#heading-quest-ce-que-les-images-docker)

2. [Comment implémenter les builds multi-étapes](#heading-comment-implementer-les-builds-multi-etapes)

3. [Le build mono-étage encombrant](#heading-le-build-mono-etage-encombrant)

4. [Quand utiliser les builds multi-étapes](#heading-quand-utiliser-les-builds-multi-etapes)

5. [Conclusion](#heading-conclusion)

## Qu'est-ce que les images Docker ?

Avant de plonger dans l'optimisation, clarifions rapidement ce que sont réellement les images Docker.

Une image Docker est un package léger et autonome qui contient tout ce dont votre application a besoin pour fonctionner – code, dépendances, variables d'environnement et fichiers de configuration. Considérez-la comme une capture instantanée de votre application, prête à être déployée n'importe où.

Lorsque vous exécutez une image, Docker la transforme en un conteneur : un environnement autonome qui se comporte de la même manière sur votre machine, en staging ou en production. Cette cohérence est un énorme avantage pour le développement et le déploiement.

Maintenant que nous avons les bases, parlons de rendre ces images plus petites et plus rapides.

## **Comment implémenter les builds multi-étapes**

Mettons-nous au travail en créant une application Flask basique et en utilisant un build multi-étapes pour garder notre image Docker légère.

### Étape 1 : Créer [`app.py`](http://app.py)

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour, Docker Multi-stage Builds! 603"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Étape 2 : Installer et sauvegarder les dépendances

Installez Flask et Gunicorn en utilisant pip :

```bash
pip install flask gunicorn
```

Puis, gélez votre environnement dans un fichier `requirements.txt` :

```bash
pip freeze > requirements.txt
```

Ce fichier est ce que Docker utilisera pour installer les dépendances à l'intérieur de votre conteneur.

### Étape 3 : Créer le `Dockerfile` multi-étapes

```docker
# Étape 1 : Étape de build
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN python -m venv /opt/venv && \\
    . /opt/venv/bin/activate && \\
    pip install --no-cache-dir -r requirements.txt

# Étape 2 : Étape de production
FROM python:3.9-slim

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app

COPY . .

ENV PATH="/opt/venv/bin/:$PATH"

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Dans le Dockerfile ci-dessus, nous avons défini à la fois une étape de développement et une étape de production pour notre application. La première étape, l'**Étape de Build**, utilise l'image de base `python:3.9-slim`, configure un répertoire de travail, ajoute tous les fichiers nécessaires et crée un environnement virtuel. Toutes les dépendances sont installées à l'intérieur de cet environnement virtuel.

Dans l'**Étape de Production**, nous commençons à nouveau par `python:3.9-slim`, mais cette fois nous copions uniquement l'environnement virtuel de l'étape de build ainsi que le code de l'application. Ensuite, nous configurons l'environnement pour utiliser cet environnement virtuel et exécutons l'application en utilisant Gunicorn.

Maintenant, dans un build multi-étapes, vous pouvez expérimenter avec l'utilisation de différentes versions de Python à travers les étapes – mais voici pourquoi je n'ai pas choisi cette voie :

* Certains packages peuvent avoir des dépendances différentes, selon la version de Python.

* Mon fichier `requirements.txt` contient des dépendances spécifiques à une version, donc rester sur la même version de Python à travers les deux étapes aide à éviter les problèmes de compatibilité.

Une fois le Dockerfile multi-étapes prêt, allez-y et construisez les images. Vous verrez clairement la différence de taille.

### Étape 4 : Construire et exécuter votre image

Pour construire et exécuter votre conteneur d'image, utilisez la commande suivante :

```bash
# Construire l'image
docker build -t my-python-app .

# Exécuter le conteneur
docker run -p 5000:5000 my-python-app
```

Si tout fonctionne correctement, votre application Flask devrait maintenant être en ligne à l'adresse [`http://localhost:5000`](http://localhost:5000) dans votre navigateur.

Vous saurez que votre build a réussi lorsque Docker se termine sans erreurs et démarre le conteneur. Vous devriez voir les logs du terminal de Gunicorn indiquant que l'application est opérationnelle.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746875902903/9e8348ac-d21c-4371-bb42-e514457a12ff.png align="center")

## Le build mono-étage encombrant

Comparons avec un build Docker traditionnel à une seule étape qui inclut tout en une seule fois :

```docker
FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \\
    build-essential \\
    python3-dev \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Le Dockerfile ci-dessus utilise un processus de build simple : il commence par l'image `python:3.9-slim`, définit un répertoire de travail, installe les dépendances système, crée un environnement virtuel, installe les packages Python, copie le code de l'application, expose le port 5000 et exécute l'application en utilisant Gunicorn. Ce type de Dockerfile est courant et fonctionne bien, mais il peut conduire à des images inutilement grandes et encombrantes.

Construisons notre image pour comparer la taille avec celle du build multi-étapes :

```bash
docker build -t my-chunky-app .
```

Vous remarquerez que ce Dockerfile prend plus de temps à construire par rapport au précédent, qui était beaucoup plus rapide.

Avant de continuer, confirmez que votre image Docker a été construite avec succès.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746886030667/5b83915e-b5b5-4927-9981-f35dad8fb1ff.png align="center")

Maintenant, comparons les tailles des builds :

```bash
docker images | grep 'my-'
```

Au cas où vous vous demanderiez pourquoi nous avons utilisé "my" pour rechercher les images, c'est parce que nous avons nommé nos images Docker `my-python-app` et `my-chunky-app`, donc utiliser "my" comme mot-clé facilite leur filtrage.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746885989703/1e3667ad-b2fd-4fff-a0e2-31d4705582a7.png align="center")

L'image ci-dessus compare les tailles des builds de nos images Docker mono-étage et multi-étapes. Comme vous pouvez le voir, `my-python-app` – le build multi-étapes – est petit et léger, tandis que `my-chunky-app` est significativement plus grand. Si vous creusez un peu plus, vous remarquerez que l'image multi-étapes a été construite en seulement 1,2 seconde, alors que celle en mono-étage a pris une minute et 21 secondes. Une différence assez impressionnante, n'est-ce pas ?

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1746885947258/9584255b-c6aa-4d25-8a4a-e4a841808b57.png align="center")

À mon avis, ce sont des raisons solides d'utiliser un build multi-étapes – mais ce n'est pas toujours nécessaire. Il y a des cas où un build mono-étage a plus de sens. Examinons ceux-ci.

## Quand utiliser les builds multi-étapes

**Utilisez les builds multi-étapes si :**

* Votre application a besoin d'outils de build (par exemple, des compilateurs, des dépendances de développement)

* Vous voulez des images Docker plus petites et plus rapides

* Vous vous souciez de la sécurité et des performances des images

**Utilisez les builds mono-étage si :**

* Vous êtes en train de tester ou de prototyper

* Votre application est minuscule et n'a pas besoin d'outils externes

* Vous apprenez encore les bases

Choisissez ce qui convient à l'échelle et à la complexité de votre projet.

## Conclusion

Les builds multi-étapes sont une victoire facile. Ils aident à garder vos images Docker propres, rapides et sécurisées – surtout lorsque votre application grandit.

Tous les projets n'en ont pas besoin, mais lorsqu'ils sont nécessaires, ils font une grande différence. Alors, la prochaine fois que vous Dockerisez quelque chose de sérieux, optez pour le multi-étapes. Votre vous futur vous remerciera.