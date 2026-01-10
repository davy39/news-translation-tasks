---
title: 'Le manuel d''architecture Serverless : Comment publier une image Docker Node
  Js sur AWS ECR et déployer le conteneur sur AWS Lambda'
subtitle: ''
author: Prince Onukwili
co_authors: []
series: null
date: '2025-04-17T02:19:13.327Z'
originalURL: https://freecodecamp.org/news/serverless-architecture-with-aws-lambda
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744843935296/c359998f-1657-482f-adf4-5ab023cb1c02.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
- name: ecr
  slug: ecr
seo_title: 'Le manuel d''architecture Serverless : Comment publier une image Docker
  Node Js sur AWS ECR et déployer le conteneur sur AWS Lambda'
seo_desc: 'Imagine you’re tasked with building a web application that can handle incoming
  traffic surges as your users grow without accumulating too much cost. Sounds like
  a dream, right?

  But here’s the thing: traditionally, to do this, you would have to manage...'
---

Imaginez que vous êtes chargé de construire une application web capable de gérer les pics de trafic à mesure que vos utilisateurs augmentent, sans accumuler trop de coûts. Cela semble être un rêve, n'est-ce pas ?

Mais voici le problème : traditionnellement, pour faire cela, vous deviez gérer beaucoup d'infrastructure – des ressources sur lesquelles votre application sera déployée – ce qui peut être un vrai casse-tête. Vous aviez des serveurs (instances VM ou ordinateurs physiques) à configurer, des bases de données à mettre à l'échelle, des équilibreurs de charge à surveiller... c'est beaucoup de travail 😩

C'est là que l'architecture Serverless vient à la rescousse. Avec le modèle Serverless, vous pouvez déployer vos applications pour gérer des milliers d'utilisateurs sans avoir à vous soucier d'engendrer trop de coûts, de gérer l'infrastructure, les serveurs, le réseau, etc.

Dans cet article, vous apprendrez tout sur l'architecture Serverless : de quoi il s'agit, et comment déployer votre propre application en utilisant AWS Lambda. Nous allons parcourir tout le processus étape par étape :

* Comment cloner le dépôt de votre application en utilisant Git.

* Comment construire une image de votre application en utilisant Docker.

* Comment installer l'AWS CLI sur votre machine locale et créer des utilisateurs AWS IAM avec les bonnes permissions pour pousser votre image Docker vers AWS Elastic Container Registry (ECR).

Une fois l'image en cours d'exécution sur ECR, nous la connecterons à AWS Lambda et déployerons le conteneur sur Lambda pour une expérience entièrement serverless. 💡✨

Prêt à passer au serverless ? C'est parti ! 🚀

## Table des matières

1. [Qu'est-ce que l'architecture Serverless ?](#heading-quest-ce-que-larchitecture-serverless)

2. [Différences entre Serverless et autres modèles de déploiement ⚡](#heading-differences-entre-serverless-et-autres-modeles-de-deploiement)

3. [🧑‍💻 Prérequis – Ce que vous devez savoir avant de suivre !](#heading-prerequis-ce-que-vous-devez-savoir-avant-de-suivre)

4. [Comment configurer l'application en utilisant Git 🐙](#heading-comment-installer-lapplication-en-utilisant-git)

5. [Comprendre la base de code 🔍](#heading-comprendre-la-base-de-code)

6. [Comment créer une image Docker de l'application 🐳](#heading-comment-creer-une-image-docker-de-lapplication)

7. [Comment créer un registre de conteneurs sur AWS Elastic Container Registry (ECR) 📁](#heading-comment-creer-un-registre-de-conteneurs-sur-aws-elastic-container-registry-ecr)

8. [IAM avec AWS : Comment créer un utilisateur sur AWS IAM pour permettre l'accès à votre AWS ECR 👨‍💻🔑](#heading-iam-avec-aws-comment-creer-un-utilisateur-sur-aws-iam-pour-permettre-lacces-a-votre-aws-ecr)

9. [Comment télécharger votre image Docker vers le dépôt AWS ECR ⤶️](#heading-comment-telecharger-votre-image-docker-vers-le-depot-aws-ecr)

10. [Comment déployer le conteneur de l'application sur AWS Lambda à partir de l'image sur AWS ECR 🚀](#heading-comment-deployer-le-conteneur-de-lapplication-sur-aws-lambda-a-partir-de-limage-sur-aws-ecr)

11. [Avantages de l'adoption du modèle Serverless dans les entreprises 📜](#heading-avantages-de-ladoption-du-modele-serverless-dans-les-entreprises)

12. [Inconvénients du modèle Serverless 🚫](#heading-inconvenients-du-modele-serverless)

13. [Quand adopter le modèle Serverless 🤔](#heading-quand-adopter-le-modele-serverless)

14. [Conclusion 📝](#heading-conclusion)

15. [À propos de l'auteur 👨‍💻](#heading-a-propos-de-lauteur)

## Qu'est-ce que l'architecture Serverless ?

Avant d'aller plus loin, décomposons ce que nous entendons par serveurs. Dans le monde de la tech, les serveurs sont des ordinateurs puissants qui stockent, traitent et gèrent les données. Considérez-les comme les travailleurs de l'ombre qui :

* **Stockent vos données** : Comme un classeur central pour vos documents numériques.

* **Exécutent vos applications** : Ils exécutent le code qui maintient votre application ou site web en fonctionnement.

* **Gèrent les requêtes** : Les serveurs répondent aux requêtes des utilisateurs – comme le chargement d'une page web ou le traitement d'une connexion.

D'accord, parlons maintenant de l'architecture Serverless – mais d'abord, clarifions une idée reçue courante. Lorsque la plupart des gens entendent le mot "Serverless", ils pensent immédiatement, "Attendez… pas de serveurs ? Comment cela fonctionne-t-il ?!" 😅

Voici la vérité : Serverless ne signifie pas qu'il n'y a pas de serveurs impliqués (surprise, surprise ! 😉). Au lieu de cela, cela signifie que vous, en tant que développeur, n'avez pas à vous soucier de la gestion des serveurs sur lesquels votre application s'exécute. L'infrastructure côté serveur est entièrement gérée par le fournisseur de cloud – dans ce cas, AWS Lambda. Vous vous concentrez uniquement sur l'écriture de code et son déploiement, et AWS s'occupe du reste.

### Alors, quel est l'intérêt du Serverless ?

Dans une configuration traditionnelle, lorsque vous déployez votre application, vous êtes responsable de choses comme :

* **L'approvisionnement des serveurs** (combien de serveurs avez-vous besoin ? Quelle taille ?)

* **La mise à l'échelle des ressources** (comment gérer les pics de trafic sans trop payer ?)

* **La surveillance** et le maintien de tout en fonctionnement.

Cela semble être beaucoup, n'est-ce pas ? 🤯 Eh bien, l'architecture Serverless simplifie tout cela en vous permettant de vous concentrer uniquement sur le code de votre application. Avec Lambda, vous pouvez exécuter du code en réponse à des événements (comme une requête HTTP, un téléchargement de fichier ou une modification de base de données) sans vous soucier de l'infrastructure derrière. AWS met automatiquement à l'échelle les ressources de calcul selon les besoins, en vous facturant uniquement pour le temps où votre code est réellement en cours d'exécution. ⏳💰

Imaginez que vous êtes dans un restaurant. Au lieu de gérer la cuisine vous-même (comme gérer vos propres serveurs), vous passez simplement une commande (votre code) et le chef (AWS Lambda) la prépare pour vous, à la demande, en fonction de ce dont vous avez besoin. 🍽️🍴

## Différences entre Serverless et autres modèles de déploiement ⚡

Maintenant que vous comprenez comment fonctionne Serverless, faisons un petit détour et explorons les autres modèles utilisés pour déployer des applications. Après tout, Serverless n'est pas le seul modèle sur le marché, et cela vous donnera une perspective importante lorsque vous choisirez le bon modèle pour votre cas d'utilisation. 👀

Lorsque vous construisez une application, vous avez besoin d'un endroit pour l'héberger – un foyer pour que votre code vive et s'exécute. Au fil des ans, le monde de la tech a inventé différentes façons de gérer cela, et chacune vous donne un niveau différent de contrôle (et de responsabilité) sur vos serveurs.

Décomposons cela.

### 🏠 Infrastructure as a Service (IaaS)

Avec l'IaaS, les fournisseurs de cloud comme AWS, Google Cloud ou Microsoft Azure vous donnent les éléments de base – des serveurs virtuels (également appelés instances), du stockage et des outils de mise en réseau – mais c'est toujours à vous de tout configurer.

C'est comme louer un appartement vide. Vous obtenez les murs, les portes et le toit, mais vous devez encore apporter vos propres meubles, configurer votre Wi-Fi et nettoyer régulièrement l'endroit. 🏡🧹

Lorsque vous choisissez l'IaaS, vous êtes responsable de :

* La configuration des serveurs (choix de la taille, du système d'exploitation et de l'installation des logiciels).

* La gestion des mises à jour, des correctifs et de la sécurité.

* La mise à l'échelle vers le haut ou vers le bas lorsque le trafic change.

**Exemple :** Amazon EC2 (Elastic Compute Cloud) est un service IaaS classique. Vous louez une machine virtuelle, vous la configurez vous-même et vous la gérez comme un propriétaire numérique.

### 🏭 Platform as a Service (PaaS)

Ensuite, nous avons le PaaS – une configuration plus aboutie.

Dans ce modèle, le fournisseur de cloud s'occupe de l'infrastructure et du système d'exploitation sous-jacent, donc vous n'avez pas à le faire. Vous téléchargez simplement votre code, configurez quelques paramètres, et la plateforme exécute votre application.

C'est comme emménager dans un appartement entièrement meublé – la cuisine fonctionne, les lumières sont allumées et le Wi-Fi est déjà connecté. Vous arrivez simplement avec vos bagages et vous mettez au travail ! 🏠✨

**Exemple :** AWS Elastic Beanstalk, Heroku ou Google App Engine.

### ☁️ Serverless : Le PaaS Spécial

Maintenant, voici où les choses deviennent intéressantes : Serverless relève en fait de l'ombrelle PaaS, mais il mérite sa propre lumière. Pourquoi ? Parce qu'il prend la commodité du PaaS et la pousse au niveau supérieur.

Dans un modèle PaaS traditionnel (comme AWS Fargate ou Heroku), votre application fonctionne 24h/24 et 7j/7, que vous ayez des visiteurs qui l'utilisent ou non. Vous payez pour l'espace réservé et la puissance de calcul tout au long du mois, comme si vous louiez un appartement. Même si vous n'y avez pas dormi tout le mois, la facture arrive quand même à la fin. 💰🏠

Mais avec Serverless, les règles changent. Vous ne payez que lorsque votre code est réellement utilisé.

#### Comment les applications fonctionnent dans le modèle Serverless ⚙️

Dans un modèle Serverless, votre application n'est pas simplement là à fonctionner toute la journée. Elle se "réveille" uniquement lorsqu'elle est nécessaire. Mais qu'est-ce qui la réveille exactement ? C'est là que les déclencheurs entrent en jeu.

Les déclencheurs sont des événements qui disent à votre application Serverless, "Hé, il est temps de faire quelque chose !" Ces événements peuvent être toutes sortes de choses, comme :

* Un utilisateur visitant votre site web et cliquant sur un bouton.

* Quelqu'un téléchargeant un fichier vers votre stockage cloud (comme une image ou un document).

* Une nouvelle ligne ajoutée à une base de données.

* Une planification automatisée (comme un rappel qui s'exécute tous les jours à 8h).

Lorsque l'un de ces événements se produit, votre application se met instantanément en vie, exécute la tâche exacte que vous avez programmée, puis retourne "dormir" jusqu'au prochain déclencheur. C'est ainsi que Serverless maintient vos coûts cloud bas et vos ressources efficaces – pas de fonctionnement constant en arrière-plan, seulement de l'action lorsqu'il y a réellement quelque chose à faire !.⚡😊

Par exemple, si un utilisateur envoie une requête qui déclenche l'exécution de votre application pendant seulement 10 secondes et utilise 20 Mo de mémoire, c'est tout ce que vous payez – le temps exact et les ressources consommées.

Pas d'utilisateurs ? Pas de requêtes ? Pas de paiement. Maintenant, c'est une façon intelligente d'économiser de l'argent. 🤑💰

### 💡 Comparaison rapide : PaaS vs Serverless

| **Fonctionnalité** | **PaaS Traditionnel (exemple : AWS Fargate)** | **PaaS Serverless (exemple : AWS Lambda)** |
| --- | --- | --- |
| Configuration du serveur | Vous sélectionnez la taille et les limites de calcul. | Pas besoin – AWS gère tout. |
| Mise à l'échelle | Vous configurez les politiques de mise à l'échelle. | Mise à l'échelle automatique, basée sur les événements (en fonction du trafic entrant). Plus le trafic est élevé, plus de puissance de calcul est ajoutée à votre application, et vice versa. 😃 |
| Facturation | Facturé pour les instances en cours d'exécution 24h/24, même lorsqu'elles sont inactives. | Facturé uniquement lorsque votre code s'exécute. ⏳💰 |
| Déploiement | Déployer des applications complètes. | Déployer de petits morceaux de code (fonctions). Vous pouvez également déployer des microservices et des applications web à grande échelle |

---

## 🧑‍💻 Prérequis – Ce que vous devez savoir avant de suivre

Avant de plonger, voici la meilleure partie : j'ai écrit cet article pour qu'il soit super adapté aux débutants et détaillé, donc même si vous avez peu ou pas de connaissances en programmation, vous pourrez toujours suivre.

Que vous soyez un développeur, une startup curieuse de technologie, ou un chef d'entreprise essayant de comprendre les solutions cloud modernes, ce guide a été écrit pour vous.

Cela dit, avoir quelques connaissances légères dans ces domaines rendra le voyage encore plus fluide :

* 🧑‍💻 Concepts de programmation de base – comme le fonctionnement des applications Node.js et ce que fait un serveur.

* 💡 Familiarité avec les termes techniques courants – des mots comme "déployer", "application", "CPU" et "logiciel" apparaîtront, mais ne vous inquiétez pas : j'ai fait de mon mieux pour décomposer ces termes en explications simples et compréhensibles.

Aucune expérience préalable du cloud ? Pas de problème ! Ce guide vous tient la main tout au long du processus, de la configuration au déploiement – tout en langage clair, sans jargon.

Alors attachez votre ceinture, et procédons au déploiement de votre propre application sur AWS Lambda. 😁

## Comment configurer l'application en utilisant Git 🐙

Avant de nous lancer dans l'écriture de code ou le déploiement de quoi que ce soit, la toute première étape consiste à récupérer l'application avec laquelle nous allons travailler – et pour cela, nous allons utiliser Git.

Mais attendez... qu'est-ce que Git ? – C'est un système de contrôle de version (VCS) qui aide les développeurs à suivre les modifications de leur code, à collaborer avec leurs coéquipiers sans se marcher sur les pieds, et à stocker leur travail en toute sécurité dans un endroit central – comme GitHub.

### Cloner le dépôt de l'application 🧑‍💻

J'ai déjà créé un projet simple pour que nous l'utilisions dans ce tutoriel – il est joliment installé sur GitHub, en attendant que vous le récupériez.

Pour cloner le projet sur votre machine locale, ouvrez votre terminal et exécutez :

```bash
git clone https://github.com/onukwilip/lambda-tutorial.git
```

Cette commande téléchargera tout le code du dépôt `lambda-tutorial` dans un dossier sur votre ordinateur. 📁

Une fois le clonage terminé, naviguez dans le répertoire du projet comme ceci :

```bash
cd lambda-tutorial
```

Boum 💥 – juste comme ça, votre machine locale est maintenant configurée avec le même code que celui stocké dans le dépôt GitHub. 🏠

## Comprendre la base de code 🔍

### Ouvrir la base de code dans votre IDE préféré 🧑‍💻

Pour ce tutoriel, nous allons utiliser Visual Studio Code (VS Code), mais n'hésitez pas à utiliser l'éditeur avec lequel vous êtes à l'aise.

Une fois que vous avez ouvert le dossier du projet `lambda-tutorial`, vous remarquerez qu'il s'agit d'un serveur web Node.js simple. Rien de trop compliqué – juste un serveur capable de gérer les requêtes et de répondre avec des données.

Maintenant, il est important de comprendre ce qui se passe dans notre base de code, surtout si vous venez de déployer sur des plateformes comme Render, Vercel ou Google Cloud Run.

### **Déploiement sur Lambda vs autres plateformes Serverless ⚡**

Lorsque vous déployez sur des plateformes comme Vercel, Render ou Google Cloud Run, vous emballez généralement votre serveur web tel que vous l'avez écrit – qu'il s'agisse d'un serveur Node.js Express ou d'une application Next.js – et la plateforme le gère presque tel quel.

Ces plateformes exécutent votre serveur comme un mini-conteneur (ou microservice) qui est toujours prêt à gérer le trafic entrant, comme un serveur attendant à votre table, prêt à prendre votre commande.

Mais AWS Lambda fonctionne un peu différemment.

Lambda attend que votre code soit organisé autour de fonctions – et non de serveurs web complets. Considérez Lambda comme un chef qui n'apparaît que lorsqu'une commande est passée, prépare la nourriture et disparaît une fois le travail terminé. 👨‍🍳🍽️🍴

Ainsi, si vous avez un serveur Node.js Express complet, vous devrez effectuer une petite "traduction" pour répondre aux attentes de Lambda – et c'est là qu'intervient le fichier lambda.js.

#### Le fichier `lambda.js` – Votre traducteur Lambda 🔍

Voici à quoi ressemble le fichier :

```javascript
const serverless = require("serverless-http");
const app = require("./app");

const handler = serverless(app);
module.exports.handler = handler;
```

Décomposons cela :

* `const serverless = require("serverless-http");`: Cela importe une petite bibliothèque pratique appelée serverless-http. (La bibliothèque `serverless-http` est importante pour que notre plateforme fonctionne correctement sur AWS Lambda.) Elle agit comme un traducteur : elle prend votre application Express régulière et l'enveloppe de sorte qu'AWS Lambda puisse la comprendre.

* `const handler = serverless(app);`: Voici la magie. Cela enveloppe votre application Express dans une fonction compatible avec Lambda.

* `module.exports.handler = handler;`: Cela exporte votre fonction enveloppée afin qu'AWS Lambda puisse l'appeler lorsque l'application est déclenchée.

Ainsi, au lieu de démarrer votre serveur comme ceci :

```javascript
app.listen(5000, () => {
  console.log("Server running on port 5000");
});
```

Vous confiez votre application à Lambda et le laissez gérer les requêtes entrantes, la mise à l'échelle et l'exécution de l'application uniquement lorsqu'elle est nécessaire.

#### Le fichier `app.js` – Votre application Express classique 📂

Votre `app.js` est l'endroit où réside la logique principale de l'application. C'est généralement là que vous :

* Configurez Express.

* Définissez les routes (comme `/api`, `/users`, `/hello`).

* Appliquez des middlewares (comme l'analyse JSON, la journalisation, CORS, etc.).

* Gérez les requêtes HTTP et envoyez des réponses.

Dans un déploiement normal (Render, Google Cloud Run, DigitalOcean ou votre propre serveur), vous démarreriez le serveur en utilisant `app.listen(PORT)` en bas de ce fichier.

Mais puisque nous déployons sur Lambda, vous ne démarrez pas directement le serveur ici. Au lieu de cela, vous exportez l'`app` comme ceci :

```javascript
module.exports = app;
```

De cette façon, votre application reste "agnostique du serveur" – elle n'est pas codée en dur pour s'exécuter sur un serveur traditionnel. Lambda (via le fichier `lambda.js`) se charge de démarrer et d'arrêter votre application chaque fois qu'elle est déclenchée par un événement (comme une requête HTTP). Intelligent, n'est-ce pas ? 💡

Pourquoi cette configuration ? 🤔

Cette petite séparation vous donne de la flexibilité :

* Vous pouvez écrire votre application Node.js comme vous l'avez toujours fait (en utilisant `Express`) à l'intérieur de `app.js`.

* Et vous ne modifiez que le point d'entrée (via `lambda.js`) pour répondre aux attentes d'AWS Lambda.

## Comment créer une image Docker de l'application 🐳

Maintenant que nous avons bien examiné le code, emballons-le de manière intelligente – en utilisant Docker.

### Qu'est-ce que Docker ? 🐳

Vous vous demandez peut-être, *"Pourquoi utilisons-nous Docker ?"*

Docker est un logiciel permettant de créer des images de vos applications et d'exécuter ces images en tant que conteneurs. Tout comme les conteneurs de transport du monde réel contiennent des marchandises en toute sécurité, les conteneurs Docker contiennent votre application, regroupée avec tout ce dont elle a besoin pour fonctionner : son code, ses bibliothèques, ses dépendances et ses paramètres. Tout est bien emballé, de sorte que votre application fonctionne de la même manière partout, que ce soit sur votre ordinateur portable, AWS Lambda, ou même sur la machine de votre ami.

### Examinons le Dockerfile 📄

Dans votre dossier de projet, vous trouverez un fichier nommé `Dockerfile`. Il s'agit essentiellement de la recette que Docker utilise pour construire l'image du conteneur de votre application.

Voici à quoi il ressemble :

```dockerfile
FROM node:18-slim AS builder

WORKDIR /app

COPY package.json .

RUN npm i -f

COPY . .

USER root

FROM amazon/aws-lambda-nodejs

ENV PORT=5000

COPY --from=builder /app/ ${LAMBDA_TASK_ROOT}
COPY --from=builder /app/node_modules ${LAMBDA_TASK_ROOT}/node_modules
COPY --from=builder /app/package.json ${LAMBDA_TASK_ROOT}
COPY --from=builder /app/package-lock.json ${LAMBDA_TASK_ROOT}

EXPOSE 5000

CMD [ "lambda.handler" ]
```

Décomposons les étapes importantes – en anglais simple : 😊

* `FROM node:18-slim AS builder`: Nous commençons par utiliser une version légère de Node.js appelée `node:18-slim` et lui donnons une étiquette nommée `builder` (considérez cela comme l'étape 1). Cela nous donne les outils nécessaires pour construire une application Node.js, mais sans les éléments supplémentaires qui alourdissent l'image. L'étiquette `builder` nous permet de réutiliser le contenu de cette construction dans l'étape suivante.

* `WORKDIR /app`: Nous définissons le répertoire de travail à l'intérieur du conteneur sur `/app`. Considérez cela comme dire à Docker : *"Hé, c'est le dossier où je vais travailler !"*

* `COPY package.json .`: Cela copie le fichier `package.json` (qui liste les dépendances de votre application) dans le dossier `/app` à l'intérieur du conteneur.

* `RUN npm i -f`: Cela installe toutes les dépendances Node.js (les packages dont votre application a besoin pour fonctionner). Le drapeau `-f` force npm à résoudre les conflits s'ils apparaissent.

* `COPY . .`: Cela copie le reste de vos fichiers de projet depuis votre ordinateur dans le conteneur.

* `USER root`: Cela définit l'utilisateur sur root (niveau administrateur) à l'intérieur du conteneur. Utile lorsque des permissions supplémentaires sont nécessaires pour certaines tâches.

* `FROM amazon/aws-lambda-nodejs`: Maintenant, voici le changement : nous passons à l'image de base officielle AWS Lambda pour Node.js ! C'est-à-dire, l'étape 2. Cette image est conçue pour fonctionner en douceur lors du déploiement de conteneurs sur Lambda.

* `ENV PORT=5000`: Nous définissons une variable d'environnement pour le port du serveur. Notre application écoutera sur le port 5000.

* `COPY --from=builder /app/ ${LAMBDA_TASK_ROOT}`: Cela prend tous les fichiers de l'étape de construction et les copie dans le répertoire de travail spécial de Lambda (`${LAMBDA_TASK_ROOT}`).

* `COPY --from=builder /app/node_modules ${LAMBDA_TASK_ROOT}/node_modules`: Même chose, mais cela copie spécifiquement le dossier node_modules (toutes vos dépendances installées) dans le répertoire de travail de Lambda.

* `COPY --from=builder /app/package.json ${LAMBDA_TASK_ROOT}`: Copie le fichier `package.json` dans le répertoire de travail de Lambda.

* `COPY --from=builder /app/package-lock.json ${LAMBDA_TASK_ROOT}`: Copie le fichier de verrouillage pour vos dépendances – afin que Lambda sache exactement quelles versions des bibliothèques utiliser.

* `EXPOSE 5000`: Cela indique à Docker, *"Hé, mon application va écouter les requêtes sur le port 5000 !"* (Bien que Lambda n'utilise pas cela directement, c'est utile pour les tests locaux.)

* `CMD [ "lambda.handler" ]`: Cela indique à AWS Lambda quelle fonction exécuter lorsque le conteneur démarre. Dans ce cas, il recherche une fonction `handler` à l'intérieur de votre application – c'est le point d'entrée !

### Comment créer notre propre image Docker

Avant de continuer, vous devez avoir Docker en cours d'exécution sur votre machine. Si vous n'avez pas encore installé Docker, consultez le guide d'installation officiel ici : [Tutoriel d'installation de Docker](https://docs.docker.com/engine/install/). C'est une excellente ressource pour mettre Docker en route.

#### Assurez-vous que Docker est en cours d'exécution

Assurez-vous que Docker Desktop est installé et en cours d'exécution. Vous pouvez généralement le savoir grâce à l'icône Docker dans votre barre des tâches. Si ce n'est pas le cas, démarrez-le avant de continuer.

#### Construire l'image Docker

Maintenant, il est temps de créer une image Docker de notre application. Dans votre terminal, naviguez jusqu'au répertoire racine de votre projet (où se trouve votre Dockerfile). Ensuite, exécutez la commande suivante :

```bash
docker build -t demo-lambda-project:latest .
```

* La commande `docker build` indique à Docker de créer une image.

* Le drapeau `-t demo-lambda-project:latest` attribue une étiquette (ou un nom) à votre image (nous changerons cela plus tard pour la convention de nommage des images prise en charge par AWS Elastic Container Registry – ECR).

* Ici, `demo-lambda-project` est le nom, et `latest` est l'étiquette indiquant la construction la plus récente.

* Le `.` à la fin indique à Docker de rechercher le Dockerfile dans le répertoire actuel.

#### Ce que cela fait

Docker va maintenant suivre les instructions de votre Dockerfile étape par étape. Il commence par construire votre application Node.js (en utilisant l'image légère Node 18), installe les dépendances, puis copie tout dans une image prête pour AWS Lambda. Une fois terminé, vous avez une image bien rangée étiquetée `demo-lambda-project:latest` qui est prête pour le déploiement.

## Comment créer un registre de conteneurs sur AWS Elastic Container Registry (ECR) 📁

D'accord, plongeons dans la création d'un registre d'images sur AWS Elastic Container Registry (ECR). Suivez ces étapes de près pour configurer votre dépôt nommé lambda-practice :

### Étape 1 : Connectez-vous et accédez à AWS ECR

Connectez-vous à votre console de gestion AWS : [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home).

Dans la barre de recherche en haut, tapez "ECR". Vous devriez voir Amazon ECR apparaître dans les résultats du menu déroulant. Cliquez dessus pour accéder à la section Elastic Container Registry.

### Étape 2 : Commencez à créer votre dépôt

Une fois dans la section ECR, cherchez un bouton qui dit "Créer un dépôt". Cliquez sur ce bouton pour commencer à configurer votre nouveau registre de conteneurs.

![Créer un nouveau dépôt AWS ECR](https://cdn.hashnode.com/res/hashnode/image/upload/v1744649904087/615bbd21-c6ed-4243-9a18-10042eec9634.png align="center")

### Étape 3 : Configurer les détails du dépôt

Vous devrez ajouter des informations comme :

* **Nom du dépôt** : Dans le formulaire qui apparaît, entrez `lambda-practice` comme nom du dépôt. Ce nom sera utilisé pour référencer votre dépôt plus tard lors du téléchargement de votre image Docker.

* **Mutabilité des balises** : Vous verrez également une option pour la mutabilité des balises. Pour ce tutoriel, définissez-la sur Mutable. Cela signifie que si vous devez mettre à jour ou modifier une balise sur votre image plus tard, vous pouvez le faire. (Gardez à l'esprit que dans certains scénarios, vous pourriez vouloir des balises immuables pour les images utilisées dans les environnements de production – mais les balises mutables sont idéales pour les tests et le développement, surtout puisque nous voulons utiliser la balise `latest` pour nos images.)

Lorsque vous êtes satisfait des paramètres, cliquez sur le bouton "Créer un dépôt" en bas du formulaire.

![Configurer le dépôt AWS ECR](https://cdn.hashnode.com/res/hashnode/image/upload/v1744650070919/3010590f-f2e3-4d52-9631-8c5d4e1a5239.png align="center")

### Dépôt créé – Maintenant, jetons un coup d'œil

Après avoir créé le dépôt, AWS vous redirigera vers la page listant vos dépôts.

Trouvez le dépôt nommé `lambda-practice` dans la liste. Il s'agit de votre nouveau registre de conteneurs où vous pouvez pousser des images Docker.

Copiez l'URI du dépôt `lambda-practice`, dont nous aurons besoin plus tard lorsque nous pousserons notre image depuis notre machine locale. L'URI doit être dans un format similaire à celui-ci - `<aws_account_id>.dkr.ecr.<region>.amazonaws.com/lambda-practice`

![Création terminée du dépôt AWS ECR](https://cdn.hashnode.com/res/hashnode/image/upload/v1744650192129/67d724c7-15da-4ff1-8e38-638c3a8d1aa4.png align="center")

Et c'est tout ! Vous avez maintenant créé avec succès un registre de conteneurs sur AWS ECR et avez votre dépôt (`lambda-practice`) prêt à recevoir votre image Docker. 🚀

## IAM avec AWS : Comment créer un utilisateur sur AWS IAM pour permettre l'accès à votre AWS ECR 👨‍💻🔑

Maintenant que nous avons créé avec succès notre registre de conteneurs AWS ECR (le foyer pour notre image Docker), il est temps de s'assurer que notre machine locale dispose des autorisations nécessaires pour interagir avec ce registre. Sans une autorisation appropriée, nous ne pourrons pas télécharger notre image.

Pour cela, nous allons créer un utilisateur IAM avec les autorisations appropriées.

### Étape 1 : Accéder à la console IAM

Commencez par vous connecter à votre console de gestion AWS : [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home).

Dans la barre de recherche en haut, tapez "IAM" et sélectionnez le service IAM dans le menu déroulant. Cela vous amène au tableau de bord IAM où vous pouvez gérer les utilisateurs, les rôles, les politiques, etc.

### Étape 2 : Accéder à la section Utilisateurs

Dans la barre latérale gauche du tableau de bord IAM, cliquez sur "Utilisateurs". Vous verrez ici une liste des utilisateurs existants, et c'est là que vous en ajouterez un nouveau.

![Créer un utilisateur AWS IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1744651384601/085a25ca-82eb-447b-8106-46df32264a85.png align="center")

### Étape 3 : Créer un nouvel utilisateur

Cliquez sur le bouton "Ajouter des utilisateurs" en haut. Dans l'étape "Définir les détails de l'utilisateur", entrez le nom d'utilisateur comme `lambda-practice`.

### Étape 4 : Attacher des autorisations directement

Dans l'étape "Définir les autorisations", choisissez "Attacher des politiques directement". Dans la boîte de recherche, tapez `AmazonEC2ContainerRegistryPowerUser`. Sélectionnez la politique `AmazonEC2ContainerRegistryPowerUser` en cochant sa case. Cette politique accorde les autorisations nécessaires pour travailler avec AWS ECR, telles que pousser et tirer des images Docker.

Cliquez sur Suivant, et vérifiez que le nom d'utilisateur est `lambda-practice` et que la politique AmazonEC2ContainerRegistryPowerUser est attachée. Si tout semble bon, cliquez sur "Créer un utilisateur".

![Ajouter une politique à l'utilisateur AWS IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1744651476901/c6d91c8c-9757-4cc6-a00f-c23d3a72de59.png align="center")

### Étape 5 : Générer des clés d'accès pour l'utilisateur

Une fois l'utilisateur créé, vous serez redirigé vers la page listant tous les utilisateurs IAM. Localisez et cliquez sur l'utilisateur `lambda-practice`. Cette action vous amènera à la page de résumé de l'utilisateur.

* Accédez à l'onglet "Informations d'identification de sécurité".

* Sous "Clés d'accès", cliquez sur le bouton "Créer une clé d'accès".

* Une page apparaîtra pour configurer la nouvelle clé d'accès.

![Créer une clé d'accès pour l'utilisateur AWS IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652284582/f6a586e9-d09e-467f-ad12-81ccf538bc34.png align="center")

Dans l'étape "Meilleures pratiques pour les clés d'accès et alternatives", sélectionnez "Interface de ligne de commande (CLI)".

**Pourquoi devriez-vous sélectionner cette option ?** Choisir CLI garantit que la clé d'accès générée est optimisée pour une utilisation avec l'AWS CLI et d'autres outils en ligne de commande (comme les commandes Docker qui poussent des images vers ECR), ce qui est exactement ce dont nous avons besoin pour notre flux de travail.

Laissez les autres configurations avec leurs paramètres par défaut, puis cliquez sur "Créer une clé d'accès".

Une fois la clé créée, vous verrez la nouvelle ID de clé d'accès et la clé d'accès secrète. Assurez-vous de copier et de stocker ces informations d'identification en toute sécurité. Elles sont essentielles pour autoriser votre machine locale à accéder à AWS ECR et à effectuer des opérations avec les permissions attribuées à l'utilisateur `lambda-practice`.

![Création terminée de la clé d'accès pour l'utilisateur AWS IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652339772/c3d94e2a-f823-4d73-9a46-ab4d829289e9.png align="center")

### **Comment autoriser votre PC local à publier des images dans le dépôt AWS ECR**

Maintenant que nous avons configuré notre utilisateur IAM et que nous avons les clés d'accès en main, il est temps d'authentifier notre PC local afin que nous puissions pousser en toute sécurité nos images Docker vers AWS ECR en utilisant l'AWS CLI. Suivez ces étapes :

#### Étape 1 : Installer l'AWS CLI

Si vous n'avez pas encore installé l'AWS CLI sur votre machine, téléchargez-le et installez-le en utilisant le guide officiel ici : [Installer l'AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Cet outil vous permet d'interagir avec votre compte AWS directement depuis la ligne de commande, ce qui est essentiel pour pousser des images vers ECR.

#### Étape 2 : Configurer vos informations d'identification AWS CLI

Une fois installé, vous devez configurer votre AWS CLI pour utiliser les informations d'identification associées à l'utilisateur `lambda-practice`. Ouvrez votre terminal et exécutez la commande suivante pour configurer un nouveau profil nommé `lambda` :

```bash
aws configure --profile lambda
```

Vous serez invité à entrer les détails suivants :

* **ID de clé d'accès AWS** : Collez l'ID de clé d'accès que vous avez généré pour l'utilisateur `lambda-practice`.

* **Clé d'accès secrète AWS** : Collez la clé d'accès secrète correspondante.

* **Nom de la région par défaut** : Entrez votre région AWS préférée (par exemple, `us-east-1` ou votre région pertinente).

* **Format de sortie par défaut** : Vous pouvez laisser cela comme `json` ou choisir votre format préféré.

Cette commande configure un nouveau profil CLI appelé `lambda` avec les informations d'identification de notre utilisateur IAM.

![Authentifier et autoriser AWS CLI avec la clé d'accès de l'utilisateur AWS IAM](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652931837/650c93af-25f0-4d7b-a202-50d825a6b77a.png align="center")

#### Étape 3 : Vérifier la configuration

Pour vous assurer que tout est configuré correctement, exécutez :

```bash
aws sts get-caller-identity --profile lambda
```

Cette commande retournera des détails sur l'utilisateur IAM configuré pour le profil `lambda`, confirmant que votre PC local est maintenant authentifié correctement.

Vous êtes maintenant prêt ! Votre AWS CLI est configuré avec le profil `lambda`, ce qui signifie que votre machine locale dispose des bonnes informations d'identification pour interagir avec votre dépôt AWS ECR et pousser des images Docker en utilisant les permissions attribuées à votre utilisateur IAM `lambda-practice`.

## Comment télécharger votre image Docker vers le dépôt AWS ECR ⤶️

Le téléchargement de votre image Docker vers AWS ECR est le moment où votre travail acharné est envoyé à votre dépôt afin qu'AWS Lambda puisse ensuite récupérer et exécuter votre conteneur. Maintenant que votre PC est autorisé à communiquer avec ECR, voyons comment télécharger l'image.

### Étape 1 : Connectez-vous à ECR avec Docker

Avant de pouvoir pousser votre image, vous devez authentifier Docker auprès de votre compte AWS ECR. Vous faites cela en exécutant une commande qui obtient un jeton d'authentification auprès d'AWS et le transmet à Docker. Par exemple :

```bash
aws ecr get-login-password --region <YOUR_REGION> --profile lambda | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com
```

Décomposons cela :

* `aws ecr get-login-password --region <YOUR_REGION> --profile lambda` : Cette partie utilise l'AWS CLI pour obtenir un mot de passe de connexion temporaire pour ECR. Assurez-vous de remplacer `<YOUR_REGION>` par la région dans laquelle votre dépôt ECR a été créé (par exemple, `us-east-1`).

* `| docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.`[`amazonaws.com`](http://amazonaws.com) : Le pipe (`|`) prend le mot de passe de la commande AWS CLI et le transmet en entrée à `docker login`. La commande de connexion connecte ensuite Docker à ECR en utilisant le nom d'utilisateur fourni (`AWS`) et le mot de passe. Remplacez `<YOUR_AWS_ACCOUNT_ID>` par votre véritable ID de compte AWS.

### Étape 2 : Considérations environnementales

Cette commande fonctionne sur des environnements shell comme Powershell, zsh et bash.

**Utilisateurs Windows (CMD)** : 
Si vous utilisez l'invite de commande classique de Windows (CMD), la syntaxe de canalisation peut ne pas fonctionner de la même manière. Dans ce cas, vous pouvez envisager d'utiliser Windows PowerShell ou Git Bash. Alternativement, vous pouvez exécuter la commande dans un environnement comme Windows Subsystem for Linux (WSL).

#### Pourquoi utiliser la bonne région ?

Il est crucial d'utiliser exactement la région où votre dépôt ECR a été créé. La région fait partie de l'URI de votre dépôt. Si vous utilisez la mauvaise région, la connexion échouera car elle ne trouvera pas le point de terminaison du dépôt correct.

#### Comment vérifier la région :

Connectez-vous à votre console AWS, accédez à la section ECR et sélectionnez votre dépôt. L'URI ressemblera à ceci : `<YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice`. Ici, `<YOUR_REGION>` est la région que vous devez utiliser dans votre commande de connexion.

### Étape 3 : Construire votre image Docker avec la bonne étiquette

Avant de pousser l'image vers ECR, vous devez la construire sur votre machine locale et l'étiqueter avec le nom de votre dépôt. Dans votre terminal, naviguez jusqu'au dossier racine de votre projet (où se trouve votre Dockerfile), puis exécutez (remplacez les espaces réservés `<YOUR_AWS_ACCOUNT_ID>` et `<YOUR_REGION>` par votre ID de compte AWS et la région de votre dépôt AWS ECR) :

```bash
docker build -t <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice:latest
```

### Étape 4 : Pousser votre image Docker vers AWS ECR

Une fois votre image construite et étiquetée, il est temps de la pousser vers votre dépôt ECR distant. Exécutez la commande suivante :

```bash
docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice:latest
```

Cette commande indique à Docker de télécharger (ou "pousser") votre image vers le dépôt que vous avez créé précédemment.

* Assurez-vous que l'URI du dépôt et l'étiquette correspondent à ceux que vous avez utilisés dans la commande de construction.

* N'oubliez pas que si vous utilisez une région différente de celle de l'URI de votre dépôt, la poussée échouera car AWS ne reconnaîtra pas le point de terminaison du dépôt.

## Comment déployer le conteneur de l'application sur AWS Lambda à partir de l'image sur AWS ECR 🚀

Vous pouvez déployer votre fonction sur AWS Lambda de plusieurs manières, chacune répondant à différents cas d'utilisation. Voici un bref aperçu :

1. **Téléchargement de fichier ZIP** : Compressez simplement votre code et vos dépendances dans un fichier ZIP, puis téléchargez-le directement via la console AWS Lambda. Cette méthode traditionnelle est idéale pour les petites bases de code qui ne nécessitent pas de runtimes personnalisés.

2. **Édition directe dans la console** : Écrivez ou modifiez le code de votre fonction directement dans l'éditeur de code AWS Lambda. Pratique pour des ajustements rapides, mais pas idéal pour des projets plus importants.

3. **Image de conteneur** : Emballez votre application en tant qu'image de conteneur Docker et déployez-la. Cette approche est particulièrement utile si vous avez des dépendances complexes, avez besoin d'un runtime personnalisé ou souhaitez des environnements cohérents entre le développement et la production.

Dans ce tutoriel, nous adoptons la voie de l'image de conteneur car elle offre flexibilité, cohérence et évolutivité – tout en nous permettant de réutiliser notre configuration Docker existante. Voici les étapes pour déployer votre application conteneurisée sur AWS Lambda :

### Étape 1 : Accéder à la console AWS Lambda

Connectez-vous à votre console de gestion AWS. Dans la barre de recherche en haut, tapez "Lambda" et sélectionnez le service AWS Lambda dans les résultats du menu déroulant.

### Étape 2 : Créer une nouvelle fonction Lambda

Une fois sur la page Lambda, cliquez sur le bouton "Créer une fonction". Vous verrez plusieurs options de création de fonction. Pour nos besoins, sélectionnez l'option "Image de conteneur". Ce choix indique à AWS que vous allez déployer une application conteneurisée au lieu de télécharger un fichier ZIP.

### Étape 3 : Nommer votre fonction

Dans l'écran de configuration de la fonction, entrez `lambda-practice` comme nom de votre nouvelle fonction Lambda. Ce nom identifie votre fonction dans AWS.

### Étape 4 : Configurer l'image de conteneur

Sous les paramètres "Image de conteneur", cliquez sur le bouton "Parcourir les images". Une nouvelle fenêtre devrait apparaître, listant vos images disponibles depuis AWS Elastic Container Registry (ECR).

Sélectionnez le dépôt que vous avez précédemment créé (par exemple, celui nommé `lambda-practice`), et choisissez l'image étiquetée comme `latest`.

![Créer une fonction AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744655907615/df0e3576-5fe6-4387-8da5-d2964b36a2af.png align="center")

![Connecter l'image AWS ECR à la fonction AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744655978526/fafd6b35-579a-4439-b15e-dd5e3dba2acf.png align="center")

![Sélectionner l'image du dépôt AWS ECR](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656031049/3de3bcc1-2034-4518-acb6-84adb6136752.png align="center")

### Étape 5 : Finaliser et créer

Maintenant, vous voudrez passer en revue les paramètres de base. Dans cette étape, vous pourriez également configurer des options supplémentaires telles que l'allocation de mémoire, les limites de temps d'attente et les variables d'environnement, en fonction des besoins de votre application.

Une fois tout configuré, cliquez sur "Créer une fonction" pour finaliser le déploiement.

### Comment activer l'accès à votre fonction Lambda

Super – bravo, vous avez déployé avec succès votre image depuis AWS ECR vers AWS Lambda ! Maintenant, l'étape suivante consiste à vous assurer que votre fonction est opérationnelle et peut être déclenchée correctement. Mais vous vous demandez peut-être, "Comment accéder à ma fonction Lambda pour voir si elle fonctionne ?" Décomposons cela :

#### Comprendre les déclencheurs de fonction Lambda

Il existe plusieurs façons d'invoquer une fonction Lambda, et AWS prend en charge plusieurs options de déclenchement. En voici quelques-unes :

* **Mappage de source d'événement** : Déclenche automatiquement votre fonction en réponse aux changements dans des services comme DynamoDB, Kinesis ou S3.

* **Événements planifiés** : Configurez des invocations planifiées de type cron via Amazon CloudWatch Events.

* **API Gateway** : Créez des API RESTful qui appellent votre fonction.

* **AWS SDK/CLI** : Invoquez directement la fonction en utilisant l'AWS SDK ou les commandes CLI.

* **URL de fonction** : Une manière simple d'exposer votre fonction via HTTPS, vous donnant une URL publique que les utilisateurs ou les applications peuvent appeler directement.

Dans ce tutoriel, nous allons utiliser une URL de fonction pour déclencher notre fonction Lambda via un événement HTTP. Cette méthode vous permet d'invoquer votre fonction depuis l'internet public et est parfaite pour tester ou construire des API publiques.

### Comment créer une URL de fonction pour votre fonction Lambda

Maintenant que vous êtes sur la page des détails de votre fonction Lambda, voici comment créer une URL de fonction étape par étape :

Tout d'abord, sur la page de votre fonction Lambda, cliquez sur l'onglet "Configuration" en haut. Dans la section Configuration, trouvez et sélectionnez le sous-onglet "URL de fonction". C'est ici que vous gérez l'URL publique de votre fonction.

Cliquez sur le bouton "Créer une URL de fonction". Cela ouvrira un nouvel écran de configuration pour la configuration de votre URL de fonction.

![Créer une URL de fonction pour la fonction AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656877335/835422c5-8c88-418a-b1f2-3650360069c3.png align="center")

* **Type d'authentification** : Définissez le type d'authentification sur AUCUN. Ce paramètre permet un accès public et non authentifié à votre fonction depuis Internet, ce qui signifie que toute personne disposant de l'URL peut l'invoquer. (C'est idéal pour les tests ou la création de services publics, mais soyez prudent avec la sécurité dans les environnements de production !)

* **Paramètres supplémentaires** : Dans la section Paramètres supplémentaires, activez Configurer le partage des ressources cross-origin (CORS). Cela est utile si vous prévoyez d'appeler votre fonction depuis des applications côté client hébergées sur différents domaines. Considérez cela comme une fenêtre ouverte pour que votre application communique avec d'autres pages web ou services.

Après avoir configuré vos paramètres, cliquez sur le bouton approprié pour créer ou enregistrer l'URL de la fonction.

![Configurer l'URL de la fonction AWS pour la fonction AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656860868/cd98ce34-7fdf-4cb6-be85-a25d3718e2e6.png align="center")

#### Vérifier votre URL de fonction

Une fois configurée, vous verrez l'URL de la fonction affichée sur la même page. Vous pouvez maintenant copier cette URL.

Collez l'URL dans un navigateur ou utilisez des outils comme `curl` ou Postman pour envoyer une requête HTTP, déclenchant votre fonction Lambda et vérifiant qu'elle fonctionne comme prévu.

Vous devriez obtenir une réponse comme celle-ci sur votre navigateur :

![Application déployée sur AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656939019/fcda2621-8057-438b-8d5a-8ac8936b6322.png align="center")

Et c'est tout ! Vous avez réussi à configurer un point de terminaison HTTP public qui déclenche votre fonction AWS Lambda. Que vous testiez votre déploiement ou construisiez une API publique, l'URL de la fonction facilite l'interaction de quiconque avec votre fonction.

### **Félicitations – Vous l'avez fait !**

Vous venez de parcourir tout le chemin du déploiement d'un serveur web Node.js, conteneurisé avec Docker, jusqu'à AWS Lambda en utilisant AWS ECR comme votre dépôt d'images. 🚀

De l'écriture et de la conteneurisation de votre application Node.js, à la création d'un dépôt AWS ECR, en passant par la configuration des utilisateurs IAM et des clés d'accès, la poussée de votre image Docker vers ECR, jusqu'à son déploiement sur Lambda – vous avez tout couvert comme un pro. 💪

Non seulement cela, mais vous avez également configuré une URL de fonction publique afin que votre application serverless puisse désormais gérer les requêtes depuis n'importe où dans le monde 🌍.

Vous venez de combiner des flux de travail cloud natifs modernes avec un déploiement serverless – vous offrant flexibilité, évolutivité et des temps de réponse ultra-rapides sans le casse-tête de la gestion des serveurs 😁.

👏 Donnez-vous une tape dans le dos. Vous avez officiellement conteneurisé et déployé votre serveur web Node.js sur AWS Lambda !

## Avantages de l'adoption du modèle Serverless dans les entreprises 📜

En ce qui concerne le déploiement d'applications dans le cloud, le modèle serverless a vraiment bouleversé l'ancien manuel et a aidé les entreprises à économiser sur les coûts du cloud ! Décomposons cela en termes simples et concrets.

### **Efficacité des coûts 💰**

Pour la plupart des entreprises – en particulier les startups – le serverless offre un avantage financier majeur. Voici pourquoi :

Dans les modèles traditionnels comme l'IaaS (Infrastructure as a Service) et le PaaS (Platform as a Service), tels que l'utilisation d'AWS EC2 ou d'AWS Elastic Beanstalk, vous provisionnez des ressources à l'avance.

Par exemple : Vous lancez un serveur avec 4 Go de RAM et 4 vCPU, et AWS vous facture 100 $/mois (cela couvre 730 heures – le mois entier). Même si votre application ne fait presque rien – disons qu'elle ne traite que des requêtes réelles pendant 120 heures et n'utilise que 1 Go de mémoire – vous payez toujours les 100 $ complets, car les ressources étaient réservées et en attente de trafic 24h/24 et 7j/7.

Mais avec le Serverless :

* Vous n'allouez pas ou ne réservez pas de puissance de calcul à l'avance.

* Votre application ne fonctionne que lorsque quelqu'un en a réellement besoin (par exemple, lorsqu'un utilisateur effectue une requête HTTP).

* Vous ne payez que pour le temps d'exécution réel et les ressources utilisées.

Par exemple, si votre fonction ne fonctionne que pendant 50 heures dans un mois et utilise 1,5 Go de RAM, vous pourriez payer quelque chose comme 30 $, contre les 100 $ fixes que vous auriez payés sur EC2 ou Elastic Beanstalk.

### **Évolutivité sans stress 📈**

Les plateformes Serverless comme AWS Lambda gèrent automatiquement :

* La mise à l'échelle lors d'une forte demande.

* La réduction à zéro lorsqu'elles sont inactives.

Cela signifie que votre équipe n'aura pas besoin de prédire ou de provisionner des ressources pendant les pics de trafic. Que 1 ou 1 million d'utilisateurs visitent votre application, le fournisseur de cloud gère le reste.

### **Opérations simplifiées ⚙️**

Pour votre équipe logicielle :

* Plus besoin de surveiller les serveurs, d'appliquer des mises à jour de sécurité ou de s'inquiéter des équilibreurs de charge.

* Vous vous concentrez uniquement sur l'écriture de la logique métier et le déploiement du code.

* Le fournisseur de cloud gère l'infrastructure en arrière-plan.

Cela libère le temps de votre équipe, réduit les tâches de maintenance et accélère les temps de développement.

### **Meilleur retour sur investissement (ROI) 💹**

Parce que vous ne payez que ce que vous utilisez, le rapport coût-valeur s'améliore considérablement. Les startups et les entreprises peuvent :

* Lancer plus rapidement.

* Expérimenter sans risque financier.

* Mettre à l'échelle sans factures surprises.

* Éviter de trop payer pour des ressources inactives.

## Inconvénients du modèle Serverless 🚫

Aussi excitant et économique que semble le modèle serverless, la règle d'or de la technologie s'applique toujours : chaque solution a ses compromis.

Examinons quelques inconvénients importants que vous devriez considérer :

### **Pas de support intégré pour les tâches en arrière-plan ⏰**

Contrairement aux serveurs traditionnels où vous pouvez exécuter des processus en arrière-plan – comme envoyer des newsletters à minuit ou nettoyer des bases de données à des heures planifiées – les plateformes serverless telles qu'AWS Lambda ne prennent pas en charge nativement les tâches en arrière-plan ou les travaux récurrents.

Par exemple, supposons que vous souhaitiez que votre application génère automatiquement des rapports tous les jours à 3 heures du matin. Dans une configuration de serveur typique, vous écriviez simplement un cron job et c'était réglé.

Mais avec Lambda ou serverless, vous ne pouvez pas faire cela directement à l'intérieur de votre fonction déployée. Au lieu de cela, vous avez besoin d'outils externes comme :

* AWS EventBridge (pour la planification et le déclenchement de fonctions Lambda)

* Ou d'autres planificateurs natifs du cloud.

Cela ajoute un peu de configuration supplémentaire, de gestion et parfois des coûts supplémentaires.

### **Coûts cloud imprévisibles 💰**

L'un des principaux arguments de vente du serverless est le "pay-as-you-use" – mais cela peut aussi devenir un angle mort financier, car :

* Les coûts dépendent du volume de trafic et de l'utilisation des ressources.

* Si votre application devient soudainement virale ou connaît un pic de trafic, votre facture cloud pourrait s'envoler sans avertissement.

Par exemple, une application qui fonctionne de manière stable à 30 $/mois pour un trafic faible pourrait atteindre 1000 $ ou plus si une campagne marketing ou un événement externe attire un grand nombre d'utilisateurs vers votre service. Bien que cela signifie que votre application réussit, votre budget pourrait en prendre un coup.

En revanche, avec les modèles traditionnels comme AWS EC2 ou Elastic Beanstalk, vos coûts sont généralement prévisibles – même si votre serveur reste inactif tout le mois.

## Quand adopter le modèle Serverless 🤔

Alors, le Serverless est-il toujours le bon choix ? Pas nécessairement !

Si vous prévoyez :

* **Des charges de travail stables et prévisibles**, EC2 ou Elastic Beanstalk pourraient offrir plus de certitude en termes de coûts.

* **Des tâches en arrière-plan de longue durée**, le serverless n'est pas idéal sans services supplémentaires.

* **Un contrôle en temps réel sur les limites des ressources**, les serveurs traditionnels vous offrent plus de flexibilité.

Mais si votre application a un trafic par à-coups (les utilisateurs viennent et partent), une logique basée sur des événements (comme des API ou des webhooks), ou si vous voulez un minimum de frais généraux opérationnels, alors le Serverless peut vous faire gagner du temps, des efforts et de l'argent.

### **Quand le Serverless est le choix parfait : Une startup construisant une API basée sur des événements**

Imaginez que vous dirigez une petite startup technologique qui vient de lancer une application pour réserver des cours de fitness. Votre équipe est petite, les budgets sont serrés et le trafic est imprévisible – certains jours vous avez 50 utilisateurs, d'autres jours 5 000.

Dans ce cas :

* Votre backend gère principalement des requêtes HTTP : nouvelles inscriptions, réservations de cours, annulations et paiements.

* Le trafic augmente pendant les pauses déjeuner et les week-ends, mais est calme la nuit.

* Vous ne voulez pas embaucher un ingénieur DevOps à temps plein juste pour gérer les serveurs.

👉 **Pourquoi le Serverless est parfait dans ce cas :**

* Vous ne payez que lorsque les gens utilisent votre application.

* Pas besoin de gérer ou de provisionner des serveurs.

* AWS Lambda se met à l'échelle automatiquement en fonction de la demande.

* Rapide à déployer, facile à connecter à d'autres services AWS (comme DynamoDB pour votre base de données, S3 pour les images et SES pour les emails).

En utilisant le Serverless dans ce cas, vous pouvez économiser de l'argent, vous mettre à l'échelle automatiquement et rester concentré sur les fonctionnalités – pas sur l'infrastructure.

### **Quand le Serverless n'est pas une bonne idée : Une plateforme de streaming vidéo**

Maintenant, imaginez que vous construisez le prochain service de type YouTube pour un public de niche – disons, du contenu éducatif pour les universités.

Dans ce cas :

* Votre plateforme nécessite un traitement en arrière-plan continu : encodage de vidéos, génération de miniatures et leur envoi vers un CDN.

* Les utilisateurs diffusent du contenu 24h/24 et 7j/7, ce qui signifie que votre application est toujours sous charge.

* Les tâches en arrière-plan comme les mises à jour du moteur de recommandation ou les rapports nocturnes doivent s'exécuter fréquemment.

👉 **Pourquoi le Serverless pourrait être une mauvaise idée :**

* Les fonctions comme AWS Lambda ont une limite de temps d'exécution (par exemple, 15 minutes maximum par exécution).

* Le traitement continu ou le streaming ne correspondent pas à la nature à la demande et éphémère du serverless.

* Les coûts pourraient s'envoler puisque l'application fonctionne presque tout le temps, ce qui la rend plus chère qu'un cluster EC2 ou Kubernetes dédié.

**Alternative meilleure :** 
Pour ce type de cas d'utilisation, une configuration basée sur des serveurs traditionnels – comme EC2 ou l'orchestration de conteneurs via ECS ou Kubernetes – offrirait plus de contrôle, une tarification prévisible et un support pour les processus de longue durée.

✅ **En résumé :** 
Le Serverless est fantastique pour les applications modernes, mais comme tout outil, il est préférable utilisé lorsque ses forces correspondent aux besoins de votre projet.

## Conclusion 📝

Félicitations pour être arrivé à la fin de ce tutoriel ! 🚀

Dans cet article, nous avons exploré la puissance de l'informatique serverless en parcourant étape par étape le processus de déploiement d'un serveur web Node.js en utilisant Docker et AWS Lambda.

De la construction de votre image de conteneur, à son envoi vers AWS ECR, et enfin à son déploiement sur Lambda – vous avez maintenant vu à quel point il est facile de faire fonctionner une application sans le tracas de l'approvisionnement des serveurs.

Nous avons également discuté des avantages de l'adoption du modèle Serverless pour le déploiement de vos applications, de ses inconvénients et des cas d'utilisation réels dans lesquels vous devriez adopter l'approche serverless.

## **À propos de l'auteur 👨‍💻**

Bonjour, je suis Prince ! Je suis un ingénieur DevOps et architecte cloud passionné par la construction, le déploiement et la gestion d'applications évolutives et le partage de connaissances avec la communauté technologique.

Si vous avez apprécié cet article, vous pouvez en apprendre plus sur moi en explorant davantage mes blogs et projets sur mon [profil LinkedIn](https://www.linkedin.com/in/prince-onukwili-a82143233/). Vous pouvez trouver mes [articles LinkedIn ici](https://www.linkedin.com/in/prince-onukwili-a82143233/details/publications/). Vous pouvez également [visiter mon site web](https://prince-onuk.vercel.app/achievements#articles) pour lire plus de mes articles. Restons en contact et grandissons ensemble ! 😊