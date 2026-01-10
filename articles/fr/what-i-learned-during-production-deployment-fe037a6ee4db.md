---
title: Ce que j'ai appris lors du déploiement en production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-27T16:01:34.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-during-production-deployment-fe037a6ee4db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9tVtNJqSGjIiLwuA1_oelw.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: deployment
  slug: deployment
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Ce que j'ai appris lors du déploiement en production
seo_desc: 'By Shruti Tanwar

  Production deployment. The final stage of every project. When all the hard work
  you’ve put in over the course of time goes live to be used by the target audience.
  It sure is an exciting time, especially when you’re part of the infras...'
---

Par Shruti Tanwar

Déploiement en production. La dernière étape de chaque projet. Lorsque tout le travail acharné que vous avez accompli au fil du temps est mis en ligne pour être utilisé par le public cible. C'est certainement un moment passionnant, surtout lorsque vous faites partie du processus de configuration de l'infrastructure !

J'avais déjà participé à des processus de déploiement par le passé. Mais cette fois, j'ai eu l'occasion de travailler sur un système énorme en termes de volume, de pile technologique et d'infrastructure, ce qui a été une aventure passionnante ! J'ai pu vivre tout le processus de première main et j'ai appris pas mal de choses.

Voici la liste de mes apprentissages que je vais me rappeler et appliquer tout au long de ma carrière en tant que développeur.

### Les deux piliers : Préparation & Planification 🏛️

Il va sans dire que la préparation et la planification doivent faire partie de tout ce que vous faites. Mais lorsqu'il s'agit du déploiement en production, cela devient une règle. C'est une évidence, **une nécessité absolue**. Vous devez connaître les intrications des technologies sur lesquelles vous avez travaillé dans votre projet. Vous devrez également réfléchir au type d'infrastructure qui conviendrait le mieux pour exécuter différents types de systèmes.

Le système que nous avons construit se composait de _nodejs, MongoDB, InfluxDB, redis, [asp.net](http://asp.net/), et rabbitMQ_ comme partie de sa pile technologique. L'une des exigences principales du système était de gérer un énorme volume de données au quotidien. Ainsi, le système devait être mis en ligne avec une carte de déploiement appropriée en tête, qui indiquait clairement des éléments comme :

* Quel type de système/technologie devait fonctionner sur quel type de machine
* Les spécifications concernant le clustering des systèmes
* Comment toutes ces boîtes autonomes allaient communiquer entre elles de manière infaillible.

### Pensez local, agissez global ?

Eh bien, c'était un conseil de mon architecte de projet/ami. Moi et quelques autres jeunes développeurs de l'équipe n'avions aucune expérience préalable dans le déploiement d'un système aussi énorme dans nos carrières. Ainsi, notre architecte nous a conseillé de créer un système identique à la production localement.

Cela signifiait que nous devions avoir une expérience pratique de tout. D'un environnement _NodeJS_ en cluster (composé de 8 clusters) et d'une configuration multi-serveurs _MongoDB_ avec une installation _Redis_ prête pour la production, à des configurations _pm2_ prêtes pour la production et des variables d'environnement !

Et nous avons documenté tout. Nous avons mis en place toutes les configurations de production sur nos machines locales, puis nous les avons testées de bout en bout. Plus tard, nous avons noté toutes les étapes nécessaires pour atteindre l'infrastructure de travail finale localement sur nos machines. Cette pratique nous a aidé à trouver les problèmes typiques rencontrés lors de la configuration de l'infrastructure, et comment nous pouvions les surmonter.

Nous avons noté tous les points, les leçons et les ajustements particuliers que nous avons effectués pour faire fonctionner le système. Cela a boosté ma confiance de plusieurs crans, et je me suis senti prêt à déployer l'environnement de production pour notre application.

### Documenter, Documenter, & Documenter !!?

Je sais, je sais. Cela a été dit beaucoup de fois. En tant que développeur, vous l'avez assez entendu. Vous ne voulez probablement pas une autre leçon sur l'importance de la documentation. Alors je vais garder cela court en mettant simplement en évidence les points principaux :

* La configuration de production doit être documentée dans les moindres détails. Elle doit être claire, infaillible et compréhensible.
* Elle doit contenir toutes les configurations du système, les adresses IP, les spécifications du système et les instructions d'installation. Et aussi tout ce que vous considérez comme suffisamment important pour que vous ou un autre développeur devriez savoir.
* Elle doit être mise à jour dès qu'un changement est apporté à l'environnement de production du système.

En tant qu'être humain, il est assez courant de penser : « Oh ! Je vais m'en souvenir ! » Faites-moi confiance, **vous ne vous en souviendrez pas**. Personne dans l'histoire du développement logiciel ne l'a jamais fait (D'accord, cela peut être un peu exagéré, mais vous voyez l'idée. ?) !

Documentez toutes les données et métadonnées autour de votre configuration de production. Vous vous remercierez plus tard. Les futurs développeurs qui rejoindront votre projet vous remercieront ensuite !

### Surveillance & Journalisation ?

Pendant la période de développement d'un projet, il est relativement plus facile de gérer les bugs et les erreurs. Quelque chose ne fonctionne pas ? Laissez-moi simplement me connecter rapidement à la boîte de développement et vérifier. Eh bien, cela ne se produit pas en production. Vous ne pouvez pas vous connecter à un système en direct et commencer à fouiller simplement parce que vous ne comprenez pas d'où vient le problème.

La mise en place d'un système de surveillance et de journalisation approprié est essentielle pour maintenir un contrôle de santé sur le système en direct. Des systèmes de surveillance intelligents sont disponibles sur le marché aujourd'hui qui peuvent vous fournir des rapports de fréquence d'erreurs, des e-mails de contrôle de santé planifiés, et plus encore.

Nous avons choisi [**_Sumologic_**](https://www.sumologic.com/) et [**_DataDog_**](https://www.datadoghq.com/) comme nos compagnons pour mettre en place le système de journalisation et de surveillance de notre application. C'était presque passionnant lorsque je pouvais identifier le problème dans le système sans faire un "ssh".

**Une configuration décente d'un système de surveillance est un long chemin pour poser une base solide pour votre produit en direct**. Ne manquez pas cela !

Ouf ! Eh bien, c'est tout ! Quelles sont vos découvertes ? N'hésitez pas à partager vos apprentissages, conseils ou points dans les commentaires ci-dessous !