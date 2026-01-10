---
title: Comment Fuzzer les Répertoires et Fichiers Cachés avec Ffuf
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2023-01-19T14:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-fuzz-hidden-directories-files-with-ffuf
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-13-at-7.47.41-PM.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: penetration testing
  slug: penetration-testing
seo_title: Comment Fuzzer les Répertoires et Fichiers Cachés avec Ffuf
seo_desc: 'Fuzzing is a technique used to test the security of a web application.
  It helps you find vulnerabilities you may not have discovered through other testing
  methods. Fuzzing also improves the overall quality and stability of a web application.

  In this ...'
---

Le fuzzing est une technique utilisée pour tester la sécurité d'une application web. Elle aide à trouver des vulnérabilités que vous n'auriez peut-être pas découvertes par d'autres méthodes de test. Le fuzzing améliore également la qualité et la stabilité globales d'une application web.

Dans cet article, nous allons examiner en détail ce qu'est le fuzzing. Vous en apprendrez également davantage sur un outil de fuzzing populaire appelé FFUF, et nous passerons par un guide étape par étape sur la façon de l'utiliser pour tester une application web.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-34.png)

Que vous soyez un pentester expérimenté ou que vous débutiez, cet article vous fournira les informations nécessaires pour commencer à utiliser le fuzzing afin d'améliorer vos compétences en pentesting d'applications web.

## Qu'est-ce que le Fuzzing ?

Tout d'abord, définissons ce qu'est le fuzzing. Le fuzzing, en général, est une technique pour trouver des vulnérabilités dans un logiciel. Nous le faisons en fournissant des entrées inattendues ou modifiées au programme.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-35.png)
_Comment fonctionne le Fuzzing_

Un exemple simple serait de générer une liste de noms de fichiers aléatoires et d'utiliser le fuzzing pour voir s'ils existent sur le site web. Un autre exemple serait de fuzzer un formulaire de connexion avec des entrées aléatoires pour voir si nous pouvons faire planter l'application web.

Lors d'un test de fuzzing, nous bombardons le logiciel avec un grand nombre d'entrées générées aléatoirement. Nous observons ensuite le logiciel pour voir comment il gère ces entrées.

S'il y a des comportements ou des erreurs inhabituels, cela signifie qu'il y a une vulnérabilité dans le logiciel. Nous pouvons utiliser le fuzzing pour tester une grande variété de vulnérabilités, y compris les problèmes de validation des entrées, les problèmes de contrôle d'accès et d'autres types de faiblesses de sécurité.

## Qu'est-ce que Ffuf ?

FFUF (Fuzz Faster U Fool) est un outil qui automatise le processus de fuzzing. Ffuf est conçu pour les professionnels de la sécurité afin de trouver des vulnérabilités dans les applications web.

Ffuf le fait en envoyant un grand nombre de requêtes à une cible avec diverses charges utiles. Ffuf analyse ensuite les réponses et nous indique ce qui a fonctionné et ce qui n'a pas fonctionné.

Nous pouvons utiliser Ffuf pour tester une grande variété de vulnérabilités, y compris les problèmes de validation des entrées, les problèmes de contrôle d'accès et d'autres types de faiblesses de sécurité.

FFUF est également rapide et flexible, nous permettant de spécifier les entrées à utiliser pour le fuzzing et les paramètres des requêtes envoyées à l'application web cible.

Ffuf est également largement utilisé dans la chasse aux primes de bogues, donc si vous prévoyez de devenir un chasseur de primes de bogues, vous utiliserez Ffuf au quotidien.

## Comment Installer Ffuf

Maintenant que vous savez ce qu'est Ffuf, voyons comment l'installer et travailler avec.

Si vous utilisez Kali ou Parrot, Ffuf est préinstallé. Comme Ffuf est écrit dans le langage de programmation Go, vous devez d'abord installer Go avant d'installer Ffuf.

[Voici le lien pour installer Go](https://go.dev/doc/install) si vous ne l'avez pas installé.

Une fois que vous avez installé Go, vous pouvez installer FFuf en exécutant la commande :

```
go install github.com/ffuf/ffuf@latest
```

Une fois que vous avez installé Ffuf, vous pouvez vérifier l'installation en utilisant la commande d'aide. Vous pouvez également utiliser la commande d'aide comme référence lors de l'utilisation de Ffuf.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-36.png)
_Options de FFUF_

## Comment Utiliser Ffuf pour Trouver des Fichiers et Répertoires Cachés

Tout d'abord, voyons comment trouver certains fichiers cachés sur un site web. Nous allons fournir deux entrées à Ffuf, l'une est l'URL et l'autre est une liste de mots.

```
ffuf -u <http://target.com/FUZZ> -w <wordlist>
```

Si vous ne savez pas ce qu'est une liste de mots, [vous pouvez trouver une vidéo ici](https://www.youtube.com/watch?v=3gXu3rdH7jw&t=18s&ab_channel=StealthSecurity). Une liste de mots est simplement une liste de mots, dans ce cas, une liste de noms de fichiers que nous recherchons sur le site web.

Voici une simple liste de mots que nous pouvons utiliser.

```
index.html
root.html
admin.html
admin
root
upload
assets
favicon.ico
style.css
public
```

Vous pouvez voir que l'URL cible contient le placeholder FUZZ. Ce placeholder sera remplacé par les mots de la liste de mots.

Par exemple, si nous avons index.html dans la liste de mots, l'URL deviendra [target.com/index.html](http://target.com/index.html). Ffuf frappera ensuite cette URL et nous dira si le fichier existe ou non en fonction de la réponse du site web.

Voici un exemple de réponse de Ffuf lors de son exécution sur une cible :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-37.png)
_Fuzzing pour les fichiers et répertoires cachés_

C'est ainsi que fonctionne Ffuf : il prend une liste de mots et essaie d'énumérer la cible pour les mots de la liste de mots. Voyons quelques autres façons d'utiliser Ffuf.

## Comment Fuzzer les Requêtes POST avec Ffuf

FFuf permet également de spécifier différentes méthodes de requête et de personnaliser les en-têtes. Cela est utile lorsque vous fuzzez des API et des endpoints d'applications web individuelles.

Par exemple, vous pouvez envoyer une requête POST avec un en-tête personnalisé et une charge utile JSON.

```
ffuf -X POST
-H "Content-Type: application/json"
-d '{"key": "FUZZ"}' -w wordlist.txt
-u <http://target.com/endpoint>
```

## Comment Utiliser les Filtres et Enregistrer les Résultats avec Ffuf

Lors de l'analyse de grandes applications web, les résultats peuvent être accablants. Avec Ffuf, vous pouvez également utiliser divers filtres et options pour affiner les résultats.

Par exemple, pour n'afficher que les réponses avec un code d'état de 200, vous pouvez utiliser le drapeau `-sc`.

```
ffuf -w wordlist.txt -u <http://target.com/FUZZ> -sc 200
```

Vous pouvez également enregistrer les résultats de l'analyse dans un fichier texte. Cela peut ensuite être importé dans d'autres outils comme Metasploit ou Burpsuite. Vous pouvez utiliser le drapeau `-of` pour enregistrer les résultats dans un fichier texte.

```
ffuf -w wordlist.txt -u <http://target.com/FUZZ> -of results.txt
```

## Documentation de Ffuf

Voici quelques autres choses que Ffuf peut faire :

* Capacité à scanner les répertoires de manière récursive
* Filtrage avancé des réponses
* Prise en charge des méthodes GET, POST et autres méthodes HTTP
* Prise en charge des connexions TLS/SSL
* Optimisation des performances pour accélérer les analyses
* Formatage de la sortie pour un parsing facile
* Intégration avec d'autres outils tels que Burp Suite

Ce ne sont que quelques exemples d'utilisation de FFuf, mais il existe de nombreuses autres options et fonctionnalités disponibles. Je vous encourage à consulter la [documentation formidable](https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html) mise en place par Codingo.

## Résumé

Le fuzzing est une technique de test de logiciels en leur fournissant des données d'entrée invalides, inattendues ou aléatoires. Cela vise à faire en sorte que le logiciel se comporte de manière inattendue ou non sécurisée.

Ffuf est un outil populaire utilisé pour effectuer le fuzzing des applications web. Que vous soyez un pentester ou que vous cherchiez simplement à améliorer la sécurité de vos applications web, cet article vous fournira les connaissances nécessaires pour commencer avec le fuzzing en utilisant ffuf.

J'espère que vous avez apprécié cet article. Vous pouvez trouver plus d'informations sur mes articles et vidéos sur [mon site web](https://www.manishmshiva.com/).