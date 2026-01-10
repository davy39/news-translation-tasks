---
title: Un guide pratique pour les tests de charge
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-09T10:48:05.000Z'
originalURL: https://freecodecamp.org/news/practical-guide-to-load-testing
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a6a740569d1a4ca257c.jpg
tags:
- name: performance
  slug: performance
- name: Testing
  slug: testing
seo_title: Un guide pratique pour les tests de charge
seo_desc: 'By Dipto Karmakar

  If you want to be sure that your site works well regardless of the level of traffic
  it has, then you should do load testing.

  In simple terms, load testing is a subset of performance testing. It is used to
  recognize the upper limit o...'
---

Par Dipto Karmakar

Si vous voulez être sûr que votre site fonctionne bien, quel que soit le niveau de trafic, alors vous devriez effectuer des tests de charge.

En termes simples, le test de charge est un sous-ensemble des tests de performance. Il est utilisé pour reconnaître la limite supérieure d'une application web et vérifier comment le système peut gérer une charge lourde.

Si vous vous êtes déjà demandé : _Comment ce site web se comportera-t-il en termes de performance sous une charge extrême si trop d'utilisateurs y accèdent simultanément ?_ alors lisez la suite, car c'est exactement la question à laquelle nous répondrons dans cet article.

Ci-dessous, nous vous montrerons trois outils différents avec lesquels ce type de test peut être effectué.

Mais avant de commencer à utiliser ces outils, voyons d'abord quelles données nous devons collecter.

En matière de tests de performance, voici les indicateurs qui décrivent le mieux notre application :

* **Temps de réponse** - la durée entre une requête et une réponse.
* **Temps de chargement moyen** - le temps de réponse moyen.
* **Temps de réponse maximal** - le temps de réponse le plus long.
* **Débit / Requêtes par seconde (rps)** - nombre de requêtes traitées par seconde.
* **Utilisation de la mémoire / CPU** - la quantité de mémoire/CPU consommée par la machine hôte.
* **Taux d'erreur** - ratio erreurs/requêtes.
* **Utilisateurs simultanés** - nombre d'utilisateurs/sessions actifs dans l'application.
* **Percentiles (50% et 95%)** - le pourcentage de requêtes qui ont eu un temps meilleur qu'une certaine valeur.

## LoadTest

![Image](https://www.freecodecamp.org/news/content/images/2020/06/yx9YuUnS-2.png)
_loadtest_

Le premier outil est un package **npm** appelé [loadtest](https://www.npmjs.com/package/loadtest).

Pour utiliser cet outil, vous devez avoir [NodeJS](https://nodejs.org/en/) installé sur votre machine, puis vous devez exécuter cette commande :

```shell
npm install -g loadtest
```

LoadTest est de loin l'outil le plus simple et le plus facile de cette liste à configurer et à utiliser. Tout ce que vous avez à faire est d'ouvrir une ligne de commande et d'exécuter :

```shell
loadtest [-n requests] [-c concurrency] URL
```

À des fins de démonstration, nous utiliserons mon site web préféré [blank.org](https://blank.org), qui est une page web vide principalement utilisée à des fins de test.

La commande suivante enverra un maximum de 60 requêtes à partir de 30 clients simultanés différents :

```shell
loadtest -n 60 -c 30 https://blank.org
```

!**Remarque : le nombre d'utilisateurs simultanés ne signifie pas le nombre de requêtes simultanées.**

Les utilisateurs/sessions simultanés représentent le nombre d'utilisateurs connectés à l'application qui effectuent des requêtes à intervalles réguliers mais simultanément.

Le résultat de la commande précédente sera le suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/yKedbwzw-1.png)

Cet outil nous fournit des informations sur :

* **percentiles** (50, 90, 95, 99 et 100%)
* **latence moyenne**
* **taux d'erreur**

Nous pouvons voir que pour blank.org, le temps en millisecondes pour 50% de nos requêtes (30 requêtes) est inférieur à 581 ms et la réponse pour la requête la plus longue a pris 649 ms.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/2aqkM2yA-1.gif)

## Loadmill

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Gjaq1JQ4-1.png)
_Loadmill_

Un autre outil que nous pouvons utiliser est Loadmill, un outil gratuit basé sur le web pour les tests. Il est également disponible sous forme de package [npm](https://www.npmjs.com/package/loadmill) si nous voulons écrire le code nous-mêmes, mais à des fins de démonstration, nous utiliserons l'outil en ligne.

Pour effectuer un test de charge avec Loadmill, tout ce que nous avons à faire est de créer une requête dans le panneau correspondant et de fournir l'URL de notre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/KNvBJyiW.png)

L'étape suivante consiste à cliquer sur le bouton **Run Test** et à configurer le nombre de sessions simultanées et la durée du test.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/dCE9UX0f.png)

Vous remarquerez que le domaine **blank.org** apparaît dans un bouton rouge. C'est parce que c'est un domaine non vérifié. Après tout, je ne possède pas le site web **blank.org**. Pour cette raison, il existe un certain seuil de charge maximale que nous pouvons envoyer à ce site.

Avec cette configuration, nous verrons comment blank.org se comporte lorsque 5 sessions simultanées tentent d'utiliser l'application dans un laps de temps de 2 minutes.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/e0nj_7mp.png)

En sortie, nous pouvons voir la performance au fil du temps :

* toutes les requêtes avaient un temps de réponse moyen de 55 ms,
* nous avons eu un pic au début où 95% des requêtes avaient un temps de réponse inférieur à 1 059 ms et 50% des requêtes avaient un temps de réponse inférieur à 51 ms.

Cela signifie que le temps le plus long pour une réponse a pris plus d'une seconde.

En même temps, nous pouvons voir le **taux d'erreur** et le débit en **rps** (requêtes par seconde) de nos sessions. C'est le nombre de requêtes envoyées par nos utilisateurs simultanés dans un laps de temps d'une seconde.

Maintenant, vous pourriez vous demander pourquoi cette grande disparité entre les résultats du premier outil et ceux-ci ?

Voici une chose extrêmement importante à laquelle il faut prêter attention, à savoir la pertinence et l'exactitude des données.

Vous devez être réaliste et essayer de faire en sorte que vos tests reflètent la réalité autant que possible.

Il existe plus d'une stratégie en matière de tests de performance. Certains outils et fournisseurs utilisent uniquement l'environnement local et d'autres créent des machines virtuelles pour chaque utilisateur simultané.

**Loadmill** se distingue des autres services en raison de son utilisation du trafic web réel pour générer la charge sur le serveur testé. En d'autres termes, le trafic qui va vers le site web ciblé provient de _vrais navigateurs_.

Le package **Loadtest** est fortement lié à la machine locale sur laquelle vous exécutez les tests et vous pouvez aller aussi loin que votre CPU vous le permet.

Comme vous l'avez vu, j'ai exécuté les tests en utilisant **loadtest** sur ma machine en utilisant la ligne de commande. Le temps de réponse était 10 fois plus grand que le temps de réponse en utilisant **Loadmill**. Trouvons pourquoi.

Si nous ouvrons les outils de développement sur blank.org, nous pouvons trouver son IP, qui est **18.217.80.105**. En utilisant cette valeur, nous pouvons effectuer une recherche d'IP et voir que le serveur est situé en **Ohio, USA**.

Nous savons que le temps de réponse est le temps mesuré entre une requête et une réponse. Donc la requête va au serveur et du serveur revient à l'agent (navigateur).

Avec le premier outil, nous avons obtenu environ 500 ms, car j'envoie les requêtes depuis ma machine. Donc les requêtes doivent parcourir environ 11 000 miles aller-retour.

Si nous allons dans le deuxième panneau de nos résultats de test **PERFORMANCE / COUNTRY**, nous voyons que toutes les requêtes ont été envoyées depuis les USA. C'est pourquoi le temps de réponse est significativement plus petit.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/VT_lB9s9.png)

Rappelez-vous, lors des tests, qu'il est préférable de simuler des conditions aussi proches de la réalité que possible afin que les données soient aussi précises que possible.

Avant de passer à l'outil suivant, je veux mentionner une autre chose à propos de Loadmill, et c'est le fait qu'il peut être configuré pour faire beaucoup plus que cela.

Nous pouvons créer des scénarios de test de charge complexes avec plusieurs requêtes contenant des paramètres et des données, y compris l'authentification de base et les notifications par e-mail.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/05LYVjqb.png)

## Apache JMeter

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vXGvTN3q.png)
_Apache JMeter_

Le dernier outil de notre liste est [Apache JMeter](https://jmeter.apache.org/), qui est une application open-source basée sur Java pour les tests de performance. Cette application nécessite une installation et est un peu plus difficile à configurer. Par conséquent, les informations suivantes sont séparées en étapes.

### Étape 1 - Télécharger et Installer

[Téléchargez](https://jmeter.apache.org/download_jmeter.cgi) l'archive des binaires sur votre ordinateur et décompressez le contenu.

Ensuite, allez dans le dossier **bin** et exécutez le fichier **jmeter.bat** deux fois. Une fois pour configurer l'outil et la deuxième fois pour le démarrer.

### Étape 2 - Ajouter un Groupe de Threads

![Image](https://www.freecodecamp.org/news/content/images/2020/06/YCAk5QOE.png)

Le **Groupe de Threads** a trois propriétés particulièrement importantes qui influencent le test de charge :

* **Nombre de Threads (utilisateurs)** : Le nombre de sessions simultanées que JMeter créera.
* **Période de Montée en Charge (en secondes)** : La durée du test.
* **Compteur de Boucle** : Le nombre de fois où le test doit être exécuté.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/1EWOCdBA.png)

### Étape 3 - Ajouter un Échantillonneur de Requête HTTP

![Image](https://www.freecodecamp.org/news/content/images/2020/06/yQp6pIQk.png)

Dans **HTTP Request Sample**, sous la section HTTP Request, remplissez le **Nom du Serveur, le Protocole** et le **Chemin** de l'application que vous souhaitez tester.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/3SQWGdiU.png)

### Étape 4 - Ajouter une Vue

Dans JMeter, vous utiliserez des écouteurs pour afficher les résultats d'un test de performance. Il existe une variété d'écouteurs disponibles, et vous pouvez en ajouter d'autres en installant des plugins. Utilisons le Tableau dans ce cas.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/iSn4m0co.png)

### Étape 5 - Exécuter le test

Exécutez le test en cliquant sur le triangle vert.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/lV6zm1C8.png)

Maintenant, nous pouvons analyser notre test.

Tout d'abord, nous pouvons voir dans le coin supérieur droit que le test s'exécute pendant 10 secondes, exactement comme nous l'avons spécifié dans les options auparavant.

Ensuite, les colonnes qui nous intéressent le plus sont **Status** et **Latency**.

* **Latency** : Le nombre de millisecondes qui se sont écoulées entre la requête et la réception d'une réponse initiale.
* **Status** : Représente le statut de la requête, si elle a réussi ou non. Il est utilisé pour calculer le taux d'erreur.

_En tant que note supplémentaire, nous pouvons observer que les valeurs sont similaires à celles obtenues en utilisant_ **_loadtest._** _C'est parce qu'ils fonctionnent de la même manière._

## Indicateurs Restants

Avec ces outils, nous avons acquis des informations sur la plupart des indicateurs dont nous avons parlé au début.

Enfin, si nous voulons obtenir des informations sur l'**Utilisation de la Mémoire / CPU** également, alors nous devons nous connecter à notre machine où l'application est hébergée et exécuter les commandes suivantes :

```
$ top
```

Cette commande vous montrera à la fois l'utilisation du CPU en pourcentage et l'utilisation de la mémoire.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/nvBNDJxk.png)

ou

```
$ free -h
```

Cette commande ne vous montrera que les données sur la mémoire mais est plus facile à lire.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/tHD3HjhA.png)

## Conclusion

Il existe de nombreux outils qui peuvent être utilisés pour effectuer des tests de performance. Ce qui est important, c'est d'en trouver un qui soit simple à utiliser, mais qui vous montre également les données les plus précises pour votre cas. Et rappelez-vous, faites toujours en sorte que vos tests simulent des conditions aussi proches de la réalité que possible.