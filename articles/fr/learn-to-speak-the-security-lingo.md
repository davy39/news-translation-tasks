---
title: Apprendre à parler le jargon de la sécurité – Préparation aux entretiens pour
  les emplois en cybersécurité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-01T16:01:00.000Z'
originalURL: https://freecodecamp.org/news/learn-to-speak-the-security-lingo
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9692740569d1a4ca11bd.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: Security
  slug: security
seo_title: Apprendre à parler le jargon de la sécurité – Préparation aux entretiens
  pour les emplois en cybersécurité
seo_desc: 'By Megan Kaczanowski

  This article will serve as a quick and dirty guide to some of the most commonly
  asked interview questions for entry-level security jobs.

  What''s the difference between an allowlist and a denylist?

  With an Allowlist, everything is ...'
---

Par Megan Kaczanowski

Cet article servira de guide rapide et concis pour certaines des questions d'entretien les plus fréquemment posées pour les emplois de sécurité de niveau débutant.

## Quelle est la différence entre une liste autorisée et une liste bloquée ?

**Avec une liste autorisée**, tout est refusé par défaut, sauf les éléments qui sont sur la liste. 

Par exemple, une entreprise peut compiler une liste de toutes les applications autorisées de l'entreprise et bloquer toutes les applications non présentes sur cette liste.

C'est un moyen très efficace d'empêcher les logiciels problématiques de s'exécuter dans votre environnement, car il bloque par défaut.

**Avec une liste bloquée**, seuls les éléments sur la liste sont refusés.

Par exemple, une entreprise peut bloquer certains sites web ou catégories (comme le porno, les jeux, etc.).

C'est quelque peu efficace, cependant, étant donné que les catégories sont parfois incorrectes et que les logiciels malveillants changent extrêmement rapidement, ce n'est pas aussi efficace que les listes autorisées et est souvent plus réactif.

## Quelle est la différence entre un test d'intrusion et un bug bounty ? Lequel est le meilleur ?

**Un test d'intrusion (ou Penetration Test)** est une simulation où une entreprise engage un testeur ou une firme (avec des accords de non-divulgation, ou NDA) pour simuler un attaquant. Ils opèrent dans un périmètre prédéfini pendant une période limitée, rédigent un rapport sur leurs découvertes et incluent des étapes de remédiation recommandées. 

Les testeurs d'intrusion ne sont pas conçus pour trouver chaque faiblesse dans un système (bien qu'ils essaieront d'identifier autant de vulnérabilités que possible). Ceux-ci sont généralement utilisés par des organisations matures (car pour que le test soit efficace, une organisation doit être capable de remédier à toute vulnérabilité identifiée).

**Les Bug Bounties**, en revanche, ouvrent le processus de recherche de vulnérabilités dans le système d'une entreprise à tous les participants de la plateforme de bug bounty. 

Cela utilise la foule (et peut donc trouver plus de vulnérabilités), mais le nombre de vulnérabilités trouvées dépend probablement de l'intérêt de la foule (une couverture continue n'est pas garantie). De plus, cela ne garantit pas le même niveau de reporting qu'un test d'intrusion (vous n'aurez peut-être pas assez de hackers ayant les compétences spécifiques nécessaires pour tester votre outil/application/site web). 

De plus, un programme de bug bounty ne doit pas être entrepris sans un plan en place pour la remédiation des vulnérabilités (la posture de sécurité de l'entreprise doit être relativement mature).

**Lecture complémentaire :** Qu'est-ce que les [Bug Bounties](https://www.freecodecamp.org/news/whats-a-bug-bounty-program/), comment fonctionnent-ils et qui devrait les utiliser ?

## Quelle est la différence entre menace, vulnérabilité et risque ? Comment décidez-vous sur quoi vous concentrer ?

Une **menace** est un événement négatif qui conduit à un résultat indésirable. Cela inclut un employé qui clique sur un lien de phishing, un développeur qui configure incorrectement une instance de base de données, ou un tremblement de terre qui détruit votre centre de données.

Un **acteur de menace** est la personne, le groupe ou l'entité responsable de l'événement.

Une **vulnérabilité** est une faiblesse dans un système (comme le manque de contrôle d'accès physique à un centre de données, l'injection SQL, etc.) qu'un acteur de menace peut exploiter.

Un **risque** est la probabilité d'un événement négatif (à quel point il est probable que la mauvaise chose se produise) et l'impact de cet événement (à quel point la mauvaise chose est grave). Un risque est généralement calculé en multipliant la probabilité x l'impact.

La **modélisation des menaces** est un processus d'identification des menaces pour une cible particulière, de compréhension et de priorisation de celles-ci. Ce processus est conçu pour répondre aux questions : « quel type d'acteur est susceptible de me cibler ? », « où suis-je le plus vulnérable ? », « quels sont mes actifs de grande valeur ? ».

**Lecture complémentaire :** [Une introduction à la modélisation des menaces](https://redcanary.com/blog/threat-modeling/).

## Quelle est la différence entre les équipes rouge, bleue et violette ?

**Équipe Rouge :** Les équipes rouges sont à l'offensive (elles pénètrent dans les systèmes).

**Équipe Bleue :** Les équipes bleues sont à la défense (elles défendent les systèmes).

**Équipe Violette :** Idéalement, une équipe qui intègre les équipes rouge et bleue de manière à faciliter leur apprentissage mutuel et à améliorer la sécurité de l'organisation dans son ensemble.

## Quelle est la différence entre un événement, une alerte et un incident ?

Un **événement** est une aberration par rapport au comportement normal du système.

Une **alerte** est une notification envoyée lorsqu'un événement spécifique ou une série d'événements se produit.

Un **incident** est un événement ayant un impact négatif sur l'organisation (exemples : un utilisateur télécharge un logiciel malveillant sur le réseau et il se propage, des identifiants sont publiés en ligne par un attaquant, etc.). Tous les événements ne deviennent pas des incidents.

## Quelle est la différence entre l'encodage, le chiffrement et le hachage ?

**L'encodage** est un moyen de convertir des données d'un format à un autre (par exemple, du texte en ASCII). Ce n'est pas une fonction de sécurité en soi. 

**Le chiffrement** est un moyen de cacher un message dans le but de permettre uniquement au destinataire prévu de comprendre le sens du message. 

C'est une fonction à double sens (vous devez pouvoir annuler le brouillage que vous avez appliqué au message). Cela est conçu pour protéger les données en transit.

**Le hachage** est une fonction à sens unique (elle ne peut pas être inversée) qui convertit un message de longueur variable en une chaîne de longueur fixe unique pour chaque message. 

Les hachages sont utilisés comme moyen efficace d'espace pour stocker des données et comme moyen sécurisé de stocker des mots de passe. Si un mot de passe est stocké sous forme de hachage, même si l'ordinateur est compromis, les données restent sécurisées (car la fonction ne peut pas être inversée). Lorsque l'utilisateur entre un mot de passe, l'ordinateur peut simplement utiliser la même fonction de hachage pour convertir le mot de passe en hachage, qu'il peut comparer au hachage stocké pour voir s'ils correspondent. 

Les fonctions de hachage sont également utilisées pour créer des condensés de message afin de vérifier qu'un message n'a pas été modifié en transit.

**Lecture complémentaire :** En savoir plus sur ce qu'est le [hachage ici](https://www.freecodecamp.org/news/an-intro-to-password-cracking/) et comment fonctionne le [chiffrement ici](https://www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords/).

## Doit-on chiffrer ou compresser les données en premier ? 

Compresser, puis chiffrer. Si vous chiffrez en premier, vous n'aurez que des données aléatoires à traiter, ce qui supprime les avantages de la compression.

## Qu'est-ce que le salage ?

**Le salage** est le processus d'ajout de valeurs aléatoires à la fin des données, comme un mot de passe, puis de hachage de la valeur. 

Cela protège contre les attaques par force brute (quand un attaquant essaie toutes les combinaisons possibles de lettres et de chiffres jusqu'à ce que le mot de passe soit trouvé) car cela rend plus difficile pour un attaquant de deviner.

**Lecture complémentaire :** En savoir plus sur le [salage ici](https://www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords/).

## TLS, SSL ou HTTPS, lequel est le plus sécurisé ?

**TLS (Transport Layer Security)** est un protocole cryptographique qui aide à sécuriser les communications sur un réseau.

**SSL (Secure Sockets Layer)** est le prédécesseur de TLS et est largement obsolète.

**HTTPS (Hypertext Transfer Protocol Secure)** est simplement HTTP chiffré avec SSL ou TLS (généralement TLS, puisque celui-ci a largement remplacé SSL). Comme vous ne pouvez pas avoir HTTPS sans SSL ou TLS, c'est une question piège.

## Sur quel port fonctionne ping ?

Encore une fois, une question piège, car ping est un protocole de couche 3 qui utilise ICMP et ne fonctionne pas sur un port du tout.

## Quel protocole utilise DNS ?

**UDP** est utilisé pour les requêtes de nom et les requêtes régulières ou inverses, ainsi que pour toute information inférieure à 512 octets.

**TCP** est utilisé pour le transfert de zone et les informations de plus de 512 octets. De plus, si un client ne reçoit pas de réponse, il retransmettra les données en utilisant TCP.

### Vous cherchez plus de ressources pour la préparation aux entretiens ? 

* [60 questions d'entretien en cybersécurité](https://danielmiessler.com/study/infosec_interview_questions/)
* [Conseils de carrière en infosec de Lesley Carhart](https://tisiphone.net/category/security-education/)
* [Conseils de carrière de Troy Hunt](https://www.troyhunt.com/careers-in-security-ethical-hacking-and-advice-on-where-to-get-started/)
* [Événements locaux BSides](http://www.securitybsides.com/w/page/12194156/FrontPage)
* [Ressources de carrière WiCyS](https://www.wicys.org/career-central)