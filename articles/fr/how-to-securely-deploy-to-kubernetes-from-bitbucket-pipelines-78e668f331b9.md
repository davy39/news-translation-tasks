---
title: Comment déployer en toute sécurité sur Kubernetes depuis Bitbucket Pipelines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T18:56:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines-78e668f331b9
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca305740569d1a4ca58a3.jpg
tags:
- name: Bitbucket
  slug: bitbucket
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: Comment déployer en toute sécurité sur Kubernetes depuis Bitbucket Pipelines
seo_desc: 'By Dane Stevens


  Over 100,000 GitHub repos have leaked API or cryptographic keys - ZDNet

  Hands up if this has happened to you. You''re reading a well-written article on
  one of countless topics, and you get to the line that goes something like this:

  //...'
---

Par Dane Stevens

![Verrouillage](https://cdn.tueri.io/274877906995/lock-it-down.jpg)

[Plus de 100 000 dépôts GitHub ont divulgué des clés API ou cryptographiques
-
ZDNet](https://www.zdnet.com/article/over-100000-github-repos-have-leaked-api-or-cryptographic-keys/)

Levez la main si cela vous est arrivé. Vous lisez un article bien écrit sur l'un des innombrables sujets, et vous tombez sur la ligne qui ressemble à ceci :

```javascript
// NE FAITES PAS CELA DANS UNE APPLICATION DE PRODUCTION
const API_KEY = '<api-key-displayed-in-plain-text>'

```

D'accord, alors comment devriez-vous faire cela ? Malheureusement, il n'existe pas d'approche universelle pour sécuriser vos secrets. Différents langages de programmation déployés dans différents environnements gèrent tous les secrets à leur manière.

Il suffit de dire que vous ne devriez jamais stocker de secrets dans votre code ou votre dépôt. Les secrets doivent être passés à votre application via des variables d'environnement au dernier moment possible.

## Bitbucket Pipelines
-
Livraison Continue

J'utilise [Bitbucket Pipelines](https://medium.com/r/?url=https%3A%2F%2Fbitbucket.org%2Fproduct%2Ffeatures%2Fpipelines%3Futm_source%3DMedium%26utm_medium%3DPost%26utm_campaign%3DTueri%26utm_content%3DKubernetes) depuis qu'il était en version Alpha et je dois dire, c'est fantastique. C'est sans doute le moyen le plus rapide et le plus facile de configurer la livraison continue directement depuis votre dépôt.

Les Pipelines sont configurés avec des fichiers YAML et peuvent être très simples ou extrêmement complexes selon vos besoins.

### Configuration des Pipelines

J'aime diviser mes tâches de construction en étapes pour plusieurs raisons :

* Si une étape échoue, vous pouvez relancer des étapes individuelles.
* Chaque étape est isolée des autres. Seuls votre dépôt de base et les "artifacts" que vous déclarez seront transmis à l'étape suivante.

Voici un fichier bitbucket-pipelines.yml en 3 étapes qui prend un site create-react-app, le package en tant qu'image Docker et le déploie sur un cluster Kubernetes :

```yaml
options:
  # Activer docker pour le Pipeline
  docker: true

pipelines:
  branches:
    master:
      - step:
          name: Construire l'application pour la Production (create-react-app)
          image: mhart/alpine-node:10
          caches:
            - node
          script:
            # Installer les dépendances
            - npm install
            # Exécuter nos tests
            - npm run test
            # Packager l'application pour la production
            - npm run build
          artifacts:
            # Passer le répertoire "build" à l'étape suivante
            - build/**
      - step:
          name: Construire l'image Docker
          script:
            # NOTE: Définir $DOCKER_HUB_USERNAME et $DOCKER_HUB_PASSWORD comme secrets d'environnement dans les paramètres du dépôt Bitbucket
            # Utiliser $BITBUCKET_COMMIT pour tagger notre image docker
            - export IMAGE_NAME=<docker-username>/<docker-image>:$BITBUCKET_COMMIT
            # Construire l'image Docker (cela utilisera le Dockerfile à la racine du dépôt)
            - docker build -t $IMAGE_NAME .
            # S'authentifier avec le registre Docker Hub
            - docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD
            # Pousser la nouvelle image Docker vers le registre Docker
            - docker push $IMAGE_NAME
      - step:
          # trigger: manual
          name: Déployer sur Kubernetes
          image: atlassian/pipelines-kubectl
          script:
            # NOTE: $KUBECONFIG est un secret stocké sous forme de chaîne encodée en base64
            # Décoder notre fichier kubeconfig en base64 dans un fichier temporaire kubeconfig.yml (celui-ci sera automatiquement détruit après l'exécution de cette étape)
            - echo $KUBECONFIG | base64 -d > kubeconfig.yml
            # Dire à notre déploiement Kubernetes d'utiliser le nouveau tag de l'image Docker
            - kubectl --kubeconfig=kubeconfig.yml --namespace=<namespace> set image deployment/<deployment-name> <deployment-name>=<docker-username>/<docker-image>:$BITBUCKET_COMMIT


```

_bitbucket-pipelines.yml_

```dockerfile
FROM mhart/alpine-node:10
WORKDIR /app
EXPOSE 5000

# Installer le serveur http
RUN yarn global add serve

# Bundler la source de l'application
COPY build /app/build

# Exécuter serve
CMD [ "serve", "-n", "-s", "build" ]

```

_Dockerfile_

Voici la partie importante de tout cela :

```yaml
- echo $KUBECONFIG | base64 -d > kubeconfig.yml

```

Notre fichier kubeconfig est stocké sous forme de chaîne encodée en Base64 dans un secret Bitbucket nommé `$KUBECONFIG`.

_Les secrets Bitbucket sont stockés chiffrés et déchiffrés lorsque vous appelez la variable dans les pipelines._

Nous décodons la variable `$KUBECONFIG` et la stockons dans un fichier temporaire appelé kubeconfig.yml qui est automatiquement supprimé dès que cette étape est terminée.

## Décomposition

### Étape 1

1. Installer les dépendances
2. Exécuter les tests
3. Construire
4. Passer le répertoire de construction à l'étape 2

### Étape 2

1. Nommer l'image Docker
2. Construire l'image Docker
3. Pousser l'image vers Docker Hub

### Étape 3

1. Décoder kubeconfig
2. Définir l'image de déploiement

## Performance de construction

Cette construction complète prend moins d'1 minute 40 secondes et en utilisant Alpine Node, l'image Docker ne fait que 29 Mo.

## Conclusion

Sécuriser vos secrets n'est pas difficile, mais cela commence par savoir où chercher.

Quelques conseils pour sécuriser les secrets dans différents environnements Node.js :

* Node.js (Développement) : utilisez des fichiers .env et .gitignore pour garder les fichiers .env hors de votre dépôt.
* Node.js (Production) : utilisez Kubernetes Secrets, Docker Secrets et passez-les en tant que variables d'environnement dans le conteneur.

### Rappelez-vous cette règle :

* Ne stockez pas de secrets dans votre code, votre dépôt ou votre image docker.

Bon codage !

---

_Originalement publié sur [Tueri.io](https://tueri.io/blog/2019-04-04-how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines/?utm_source=FreeCodeCamp&utm_medium=Post&utm_campaign=Continuous%20Deployment)_