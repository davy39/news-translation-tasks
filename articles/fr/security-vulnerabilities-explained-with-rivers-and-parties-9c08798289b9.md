---
title: Vulnérabilités de sécurité expliquées avec des rivières et des fêtes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T18:02:39.000Z'
originalURL: https://freecodecamp.org/news/security-vulnerabilities-explained-with-rivers-and-parties-9c08798289b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9d26Q5AQW9j1rsCPaqzh-Q.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Vulnérabilités de sécurité expliquées avec des rivières et des fêtes
seo_desc: 'By Andrea Zanin

  Security vulnerabilities can be boring to learn. But you still need to learn them,
  unless you want some hacker to delete all your production databases. To make it
  a bit more entertaining, I tried to explain 3 major vulnerabilities in ...'
---

Par Andrea Zanin

Les vulnérabilités de sécurité peuvent être ennuyeuses à apprendre. Mais vous devez quand même les apprendre, à moins de vouloir qu'un hacker supprime toutes vos bases de données de production. Pour rendre cela un peu plus divertissant, j'ai essayé d'expliquer 3 vulnérabilités majeures en termes de vie quotidienne. Alors sans plus tarder, commençons.

### Attaque de l'homme du milieu

Lorsque vous ouvrez un site web, vous vous connectez à un serveur. Vous pouvez imaginer cette connexion comme une rivière et les données (par exemple, les Tweets sur Twitter) sont des messages dans des bouteilles qui flottent le long de la rivière.

Si Alex (le serveur) veut vous envoyer une invitation à dîner, il doit la mettre dans une bouteille et l'envoyer dans le courant. Mais que se passe-t-il si John (l'attaquant) prend la bouteille hors de la rivière et change le message en une insulte, puis la remet dans la rivière ? Vous n'aurez aucun moyen de reconnaître que le message que vous avez reçu n'a pas été envoyé par Alex !

Cela s'appelle une **attaque de l'homme du milieu**.

Pour résoudre ce problème, vous et Alex pouvez décider d'écrire vos messages en inversant l'ordre des caractères. Par exemple, **secret message** devient **egassem terces**.

John ne connaît pas la **méthode** que vous avez utilisée pour générer le code secret, donc il ne peut pas comprendre ce que dit le message ni changer ce qui est écrit dessus sans que vous le remarquiez.

C'est ce que fait le protocole **HTTPS**, mais avec une méthode plus sophistiquée.

### DoS et DDoS

Une autre façon de voir un serveur est comme la boîte aux lettres de votre maison. Vous recevez du courrier, vous les lisez et vous répondez.

Que se passe-t-il si John commence à vous écrire une tonne de courrier ? Vous ne pourriez pas répondre à l'invitation à dîner d'Alex à temps, parce que vous seriez trop occupé à répondre à tous les autres messages de spam envoyés par John.

Cela s'appelle une **attaque par déni de service**, DoS en abrégé.

Une façon de mitiger cela est de lire l'expéditeur en haut du courrier avant de l'ouvrir. Si c'est John, ne vous donnez pas la peine d'ouvrir le courrier. De cette façon, vous n'avez pas besoin de répondre à John et pouvez vous concentrer sur la gestion des choses sérieuses, comme l'invitation à dîner d'Alex.

C'est le **blacklisting IP** en un mot, seulement avec des adresses de protocole internet numériques de l'expéditeur.

Malheureusement, John a convaincu beaucoup d'autres personnes malveillantes de vous envoyer des courriers indésirables. Donc maintenant vous ne pouvez pas simplement jeter les courriers de John, parce qu'il y a beaucoup de gens qui vous écrivent.

C'est une **attaque par déni de service distribuée (DDoS)** et c'est très difficile à gérer.

Une façon de gérer cela est de recevoir du courrier uniquement d'Alex. C'est dommage que vos autres amis ne puissent pas vous écrire, parce que vous jetterez aussi leurs emails. Mais les temps désespérés appellent des mesures désespérées. Mais progressivement, vous pouvez augmenter le nombre de personnes légitimes dont vous souhaitez recevoir du courrier.

Cela s'appelle le **whitelisting IP** et peut être utilisé pour atténuer l'impact d'une attaque DDoS, mais ce n'est pas une solution parfaite.

Les attaques DDoS sont difficiles à gérer, heureusement, elles sont aussi difficiles à organiser, car vous avez besoin de beaucoup de personnes pour vous aider. Mais avec les attaquants utilisant des appareils IoT vulnérables, des serveurs mal configurés et des services DDoS à la demande pour lancer des attaques DDoS, il devient très facile de lancer de telles attaques.

### Injection

Supposons qu'Alex ait décidé d'organiser une fête avec quelques amis. Il a préparé un modèle d'invitation :

> Samedi prochain, j'organise une fête, tu veux venir ? Si possible, apporte quelques [espace laissé pour un aliment ici].  
> Tom

Il a également décidé de prendre des suggestions pour la nourriture, alors il a laissé une boîte à suggestions dans la cafétéria de l'école. Ensuite, il a copié sans réfléchir une suggestion de la boîte dans l'espace laissé sur chaque invitation.

Voici les suggestions :

* coca
* chips
* pâtes
* oranges. Je voulais aussi te dire que Rick est stupide

Vous voyez ce qui se passe ici ? Un ami de Tom recevra ce message

> Samedi prochain, j'organise une fête, tu veux venir ? Si possible, apporte quelques oranges. Je voulais aussi te dire que Rick est stupide.  
> Tom

L'ami de Tom pensera que tout le message a été écrit par Tom, y compris la partie concernant Rick ! Le gars qui a laissé la suggestion de nourriture (je pense que nous connaissons son nom) a simplement **injecté** un message dans l'invitation d'Alex.

Pour éviter l'**injection**, validez simplement (en langage technique **échappez**) ce que vous acceptez d'un utilisateur lorsqu'il ne provient pas d'une source de confiance.

### Avant de partir

Si votre nom est John, je vous dois des excuses, mais restez, je promets que dans le prochain article, vous serez le bon.

J'espère que vous avez apprécié l'article. N'oubliez pas que vous pouvez ? jusqu'à 50 fois !