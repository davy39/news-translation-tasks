---
title: Comment créer un bot alimenté par IA capable de publier sur Twitter/X
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2025-04-23T18:27:44.353Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-ai-powered-bot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745416845372/5eb9963d-e092-4844-99d9-01fa70032169.png
tags:
- name: automation
  slug: automation
- name: AI
  slug: ai
- name: bot
  slug: bot
- name: Twitter
  slug: twitter
- name: gemini
  slug: gemini
seo_title: Comment créer un bot alimenté par IA capable de publier sur Twitter/X
seo_desc: 'These days, everyone wants to be a content creator. But it can be hard
  to find time to create and curate content, post on social media, build engagement,
  and grow your brand.

  And I’m not an exception to this. I wanted to create more content, and had ...'
---

De nos jours, tout le monde veut devenir créateur de contenu. Mais il peut être difficile de trouver le temps de créer et de curater du contenu, de publier sur les réseaux sociaux, de construire un engagement et de développer sa marque.

Et je ne fais pas exception à cette règle. Je voulais créer plus de contenu et j'ai eu une idée basée sur quelque chose que j'ai observé. Je suis abonné à quelques newsletters technologiques et je lis beaucoup de mises à jour chaque jour sur l'écosystème technologique. Mais j'ai remarqué que beaucoup de mes pairs ne semblent souvent pas être au courant de ces nouvelles. J'ai donc décidé de publier mes trois principales histoires d'actualité (surtout sur l'IA) sur mon compte Twitter/X chaque jour.

J'ai fait cela pendant quelques semaines, mais après cela, je n'ai plus trouvé le temps de continuer. J'ai donc fait quelques recherches sur la façon dont je pourrais automatiser le processus, et j'ai trouvé une solution. Dans ce guide, je vais expliquer le processus afin que vous puissiez l'utiliser également.

À la fin de ce tutoriel, vous aurez créé votre propre bot IA qui :

* Récupère des données à partir d'une API ou parcourt une page web
  
* Traite les données en utilisant l'IA
  
* Publie les résultats sur Twitter/X
  

Et le plus intéressant : ce processus entier est automatisé.

## Table des matières

* [Prérequis](#heading-prerequisites)
  
* [Comment construire le bot](#heading-comment-construire-le-bot)
  
  * [Étape 1 : Générer la clé API Twitter](#heading-etape-1-generer-la-cle-api-twitter)
    
  * [Étape 2 : Générer le jeton d'accès et le secret](#heading-etape-2-generer-le-jeton-dacces-et-le-secret)
    
  * [Étape 3 : Générer une clé API dans Google Gemini](#heading-etape-3-generer-une-cle-api-dans-google-gemini)
    
* [Configuration du projet Node.js](#heading-configuration-du-projet-nodejs)
  
  * [Étape 1 : Récupérer les données de l'API](#heading-etape-1-recuperer-les-donnees-de-lapi)
    
  * [Étape 2 : Télécharger les données sous forme de fichier vers l'API Gemini](#heading-etape-2-telecharger-les-donnees-sous-forme-de-fichier-vers-lapi-gemini)
    
  * [Étape 3 : Inviter Gemini à obtenir les dernières nouvelles sur l'IA](#heading-etape-3-inviter-gemini-a-obtenir-les-dernieres-nouvelles-sur-lia)
    
  * [Étape 4 : Publier en utilisant l'API Twitter/X](#heading-etape-4-publier-en-utilisant-lapi-twitterx)
    
  * [Étape 5 : Supprimer le fichier téléchargé dans l'API Gemini](#heading-etape-5-supprimer-le-fichier-telecharge-dans-lapi-gemini)
    
  * [Le résultat](#heading-le-resultat)
    
* [Conclusion](#heading-conclusion)
  

## Prérequis

Avant de commencer à créer un bot, vous devrez avoir les éléments suivants configurés et prêts à l'emploi :

* [NodeJS](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) - Une application NodeJS simple pour coder le bot
  

Vous aurez également besoin de certaines clés API, secrets et jetons. Vous devrez donc avoir créé les comptes suivants :

* [Twitter Developer](https://developer.x.com/) - Pour générer les clés, secrets et jetons de l'API Twitter/X
  
* [Google AI Studio](https://aistudio.google.com/) - Pour générer la clé API Gemini
  

## Comment construire le bot

Il y a plusieurs étapes que je vais vous guider pour construire votre bot.

Nous commencerons par générer une clé API et un secret afin de pouvoir utiliser l'API Twitter/X. Ensuite, nous générerons un jeton d'accès et un secret de jeton d'accès avec des permissions "Lecture et Écriture" qui pourront publier sur votre compte. Après cela, nous générerons une clé API dans Google Gemini (nous utiliserons l'API Gemini pour traiter les données).

Une fois tout cela pris en charge, nous commencerons à travailler sur l'application Node.js. L'application sera capable de récupérer des données à partir d'une API, de traiter les données en utilisant l'IA, puis de publier ces données sous forme de tweets sur Twitter/X.

Enfin, nous automatiserons l'ensemble du processus et le planifierons pour qu'il s'exécute quotidiennement.

### Étape 1 : Générer la clé API Twitter

1. Accédez au [site web des développeurs Twitter](https://developer.x.com/).
  
2. Cliquez sur le "Portail des développeurs" en haut à droite :
  
  ![Image montrant le portail des développeurs mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1745152618491/214fe6d6-b699-40bb-8ac0-533b0c72b927.png align="center")
  
3. Inscrivez-vous en utilisant votre compte.
  
4. On vous demandera de remplir un formulaire demandant comment vous utiliserez l'API Twitter, et quelques détails de base. Cela peut prendre jusqu'à 24 heures pour être approuvé. Mais, pour moi, c'est approuvé instantanément.
  
  ![Formulaire demandant comment vous utiliserez l'API Twitter](https://cdn.hashnode.com/res/hashnode/image/upload/v1745152170917/d2c2ba21-f3f5-4bc6-bdd5-58d222e203e6.png align="center")
  
5. Après la connexion, accédez à "Projets et applications" et sous "Aperçu", cliquez sur "Créer une application" :
  
  ![Écran de création d'application](https://cdn.hashnode.com/res/hashnode/image/upload/v1745153184830/1a731639-0df2-47e3-baf2-3633e1735a69.png align="center")
  
6. Entrez un nom pour votre application et cliquez sur "Suivant" pour procéder à la création de votre application. À la fin, on vous montrera votre clé API et votre secret. Ne les copiez pas maintenant.
  
7. Cliquez sur le projet que vous avez créé dans le tiroir de gauche et cliquez sur l'option "Modifier" dans la section "Paramètres d'authentification de l'utilisateur".
  
  ![Modification de la section des paramètres d'authentification de l'utilisateur](https://cdn.hashnode.com/res/hashnode/image/upload/v1745153746932/002f3b38-5aaf-43ef-8d7c-0368f141524f.png align="center")
  
8. Sélectionnez "Lecture et Écriture" dans la section des permissions de l'application, "Application Web, Application Automatisée ou Bot" dans la section Type d'application, et entrez l'URL de votre site web (cela peut être n'importe quelle URL, y compris http://localhost) dans les champs "URI de rappel" et "URL du site web". Ensuite, cliquez sur "Enregistrer".
  
9. Allez dans l'onglet "Clés et jetons".
  
10. Cliquez sur le bouton "Régénérer" dans la section "Clé API et Secret".
  
11. Copiez et enregistrez la clé API et le secret quelque part en sécurité.
  

### Étape 2 : Générer le jeton d'accès et le secret

1. Allez dans l'onglet "Clés et jetons".
  
2. Cliquez sur le bouton "Générer" ou "Régénérer" dans la section "Jeton d'accès et Secret".
  
3. Copiez et enregistrez le jeton d'accès et le secret quelque part en sécurité.
  
  ![Génération ou régénération des clés et jetons](https://cdn.hashnode.com/res/hashnode/image/upload/v1745154373207/4309dbcc-1081-46b7-be71-5babf950eae0.png align="center")
  

### Étape 3 : Générer une clé API dans Google Gemini

1. Accédez à [Google AI Studio](https://aistudio.google.com/).
  
2. Connectez-vous à votre compte.
  
3. Cliquez sur le bouton "Obtenir une clé API" en haut à droite.
  
4. Cliquez sur le bouton "Créer une clé API".
  
  ![Écran de création de l'API](https://cdn.hashnode.com/res/hashnode/image/upload/v1745154646809/54c4fa1a-097e-4bf6-8a5f-229c01845d28.png align="center")
  
5. Copiez et enregistrez la clé API quelque part en sécurité.
  

D'accord, nous avons terminé la création des clés API et des secrets nécessaires pour notre projet. Enfilons nos chaussures de codage.

## Configuration du projet Node.js

Il y a 5 étapes majeures pour cette partie du projet. Elles sont :

1. Récupérer les données de l'API
  
2. Télécharger les données sous forme de fichier vers l'API Gemini
  
3. Inviter Gemini avec le fichier téléchargé pour obtenir les dernières nouvelles sur l'IA
  
4. Publier les nouvelles sur Twitter/X en utilisant leur API
  
5. Supprimer le fichier téléchargé dans l'API Gemini
  

Ce ne sont que des extraits de code qui peuvent être assemblés ensemble pour exécuter ce projet.

### Étape 1 : Récupérer les données de l'API

Dans mon cas, j'utiliserai `techmeme.com` pour obtenir les dernières nouvelles. Mais ce site ne propose pas d'API. Je vais donc télécharger le HTML de ce site.

%[https://gist.github.com/arunachalam-b/b204531fbfda5e805202b5f5ab5aa55d] 

Dans l'en-tête `User-Agent`, nous passons la valeur qui imite un agent utilisateur de navigateur pour éviter les blocs potentiels.

### Étape 2 : Télécharger les données sous forme de fichier vers l'API Gemini

Maintenant, nous devons stocker ce HTML dans un fichier séparé. Nous ne pouvons pas passer directement le code HTML dans l'invite à l'API Gemini, car cela entraînerait une erreur. Cela est dû au fait que Gemini n'accepte qu'un nombre limité de jetons dans cette API. Le code HTML de n'importe quel site web entraînera toujours un grand nombre de jetons. Nous allons donc créer un fichier séparé.

Téléchargez le fichier vers l'API Gemini. Référez-vous à l'ID du fichier dans l'invite à Gemini.

%[https://gist.github.com/arunachalam-b/5ebfed570c79a0f0faa8c4e42559c673] 

### Étape 3 : Inviter Gemini à obtenir les dernières nouvelles sur l'IA

Écrivons une invite à Gemini lui demandant de générer les principales nouvelles en se référant au fichier HTML fourni. Nous lui demanderons de fournir un titre, une courte description, une URL et trois hashtags pertinents pour chaque tweet. Nous lui donnerons également quelques exemples de données pour qu'il sache à quoi cela doit ressembler. Nous lui demanderons de générer une réponse structurée en fournissant le format du JSON que nous voulons pour la sortie.

Vous pouvez utiliser n'importe quel modèle que vous souhaitez, mais j'utiliserai le modèle `gemini-2.5-pro-exp-03-25` pour ce cas d'utilisation. J'utilise ce modèle car nous avons besoin d'un modèle de réflexion qui réfléchit et choisit les bonnes principales nouvelles - pas seulement un modèle qui prédit le prochain jeton/mot. Le modèle Gemini 2.5 Pro est le mieux qualifié pour cela.

%[https://gist.github.com/arunachalam-b/466449de313bcbc4241eaf3b6e1646a7] 

### Étape 4 : Publier en utilisant l'API Twitter/X

Voici le cœur de notre application. Nous devons publier tous les tweets que nous avons reçus de Gemini. Nous publierons le tweet sous forme de fil. Cela signifie que le premier tweet sera le tweet racine et que les tweets suivants seront dans les commentaires du tweet précédent. Cela en fait un fil.

Pour ce faire, nous prendrons l'ID de chaque tweet après sa publication et le passerons au tweet suivant comme référence. Une chose supplémentaire à noter ici est qu'après chaque tweet réussi, nous donnerons une pause de 5 secondes avant de publier le tweet suivant. Il y a quelques raisons de procéder ainsi.

1. Lorsqu'un script s'exécute, il s'exécute généralement à une vitesse beaucoup plus élevée (généralement en millisecondes). Ainsi, le deuxième tweet peut être publié avant que le premier tweet ne soit publié (peut-être en raison d'une mauvaise connexion Internet). De plus, je crois que Twitter met en œuvre un système de file d'attente qui peut traiter rapidement le deuxième tweet avant le premier. Il est donc toujours préférable de laisser un petit intervalle - si ce n'est 5 secondes, alors au moins 1 seconde.
  
2. Twitter peut avoir mis en œuvre un mécanisme de limitation de débit. Ainsi, si plusieurs requêtes sont reçues d'une même IP dans un court laps de temps, ils peuvent bloquer l'IP et considérer votre compte comme du spam.
  
3. Puisque nous utilisons une API de niveau gratuit, nous sommes limités à 1500 tweets par mois. Si vous avez payé pour cette API, vous n'aurez pas à vous en soucier (puisque vous aurez une limite plus élevée et que le mécanisme de limitation de débit - référez-vous au point #2 - peut ne pas être applicable). Tout cela dépend de leur [tarification](https://docs.x.com/x-api/introduction#access-levels), alors référez-vous simplement à cela et prenez votre décision en conséquence.
  

J'utilise le niveau gratuit, et puisque c'est un projet de loisir, avoir un temps d'attente de 5 secondes a du sens. Je n'ai pas rencontré de problèmes jusqu'à présent avec cela.

%[https://gist.github.com/arunachalam-b/b049fda9e567bc68c7fb33de0ce67cd3] 

### Étape 5 : Supprimer le fichier téléchargé dans l'API Gemini

Après avoir publié tous les tweets, il est temps de nettoyer le système. La seule chose que nous devons faire comme nettoyage est de supprimer le fichier téléchargé. Il est toujours une bonne pratique de supprimer un fichier inutilisé qui n'est plus nécessaire. Et puisque nous avons déjà publié les tweets, nous n'avons plus besoin de ce fichier. Nous allons donc le supprimer dans cette étape.

%[https://gist.github.com/arunachalam-b/741c5b13603187c76905f7b349661293] 

C'est tout. Nous avons terminé. Vous devez simplement copier ces blocs de code dans un fichier `index.js` et installer quelques dépendances dans le projet, et vous devriez être prêt à partir.

Pour rendre cela encore plus simple, j'ai créé un dépôt et l'ai rendu public. Voici l'[URL du dépôt Github](https://github.com/arunachalam-b/existential-crisis-alert-bot). Vous devez simplement cloner le dépôt, installer les dépendances et exécuter la commande `post`.

```plaintext
git clone https://github.com/arunachalam-b/existential-crisis-alert-bot.git
cd existential-crisis-alert-bot
npm i
```

Créez un fichier .env et mettez à jour vos clés API et secrets dans ce fichier :

```plaintext
GEMINI_API_KEY=
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
```

Exécutez la commande suivante pour publier les dernières nouvelles sur l'IA sur votre compte :

```plaintext
npm run post
```

### Le résultat

Voici un exemple de sortie de cette commande :

![Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1745169397786/14e08ef8-dba5-45e0-a5d5-f3c6135c6347.png align="center")

Vous pouvez modifier le code/invite pour récupérer des données à partir d'une API différente et publier les meilleurs résultats sur votre compte Twitter.

## Conclusion

J'espère que vous comprenez maintenant comment vous pouvez automatiser un processus légèrement complexe en utilisant l'IA et quelques API. Notez simplement que cet exemple n'est pas complètement automatisé. Vous devez toujours exécuter manuellement la commande chaque jour pour publier les tweets.

Mais vous pouvez également automatiser ce processus. Envoyez-moi simplement un message si vous souhaitez en savoir plus à ce sujet. Ce sujet mérite à lui seul d'être un tutoriel séparé. De plus, je vous demanderais de donner une étoile à mon projet si vous avez apprécié ce tutoriel.

En attendant, vous pouvez suivre mon [compte Twitter/X](https://x.com/AI_Techie_Arun) pour recevoir les principales nouvelles sur l'IA chaque jour. Si vous souhaitez en savoir plus sur l'automatisation, abonnez-vous à ma newsletter par e-mail ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_automated_tweet)) et suivez-moi sur les réseaux sociaux.