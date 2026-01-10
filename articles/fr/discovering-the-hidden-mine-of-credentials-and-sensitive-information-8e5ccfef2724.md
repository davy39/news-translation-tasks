---
title: Comment j'ai utilisé une simple requête Google pour extraire des mots de passe
  de dizaines de tableaux Trello publics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T16:41:34.000Z'
originalURL: https://freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6PO4cITaemxEBISjKuRimg.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Life lessons
  slug: life-lessons
- name: privacy
  slug: privacy
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment j'ai utilisé une simple requête Google pour extraire des mots de
  passe de dizaines de tableaux Trello publics
seo_desc: 'By Kushagra Pathak

  A few days ago on 25th April, while researching, I found that a lot of individuals
  and companies are putting their sensitive information on their public Trello boards.
  Information like unfixed bugs and security vulnerabilities, the...'
---

Par Kushagra Pathak

Il y a quelques jours, le 25 avril, alors que je faisais des recherches, j'ai découvert que de nombreux particuliers et entreprises publient leurs informations sensibles sur leurs tableaux Trello publics. Des informations comme des **bugs non corrigés et des vulnérabilités de sécurité**, **les identifiants de leurs comptes de réseaux sociaux**, **comptes email**, **serveurs** et **tableaux de bord admin** — vous l'avez compris, tout est disponible sur leurs tableaux Trello publics qui sont indexés par tous les moteurs de recherche et n'importe qui peut facilement les trouver.

### Comment ai-je découvert cela ?

J'ai recherché des instances [Jira](https://www.atlassian.com/software/jira) d'entreprises exécutant des [Programmes de Bug Bounty](https://en.wikipedia.org/wiki/Bug_bounty_program) avec la requête de recherche suivante :

```
inurl:jira AND intitle:login AND inurl:[company_name]
```

> _Note : J'ai utilisé une requête Google dork, parfois appelée dork. Il s'agit d'une chaîne de recherche qui utilise des [opérateurs de recherche](https://whatis.techtarget.com/definition/search-operator) avancés pour trouver des informations qui ne sont pas facilement disponibles sur un site web. — [WhatIs.com](https://whatis.techtarget.com/definition/Google-dork-query)_

J'ai entré `Trello` à la place de `[company name]`. Google a présenté quelques résultats sur des tableaux Trello. Leur visibilité était définie sur Public, et ils affichaient les détails de connexion à certaines instances Jira. Il était environ 8h19, UTC.

**J'étais si choqué et émerveillé ?**

Alors pourquoi était-ce un problème ? Eh bien, [Trello](https://trello.com/tour) est un outil en ligne pour gérer des projets et des tâches personnelles. Et il dispose de tableaux qui sont utilisés pour gérer ces projets et tâches. L'utilisateur peut définir la visibilité de ses tableaux sur Privé ou Public.

Après avoir découvert cette faille, je me suis dit — pourquoi ne pas vérifier d'autres problèmes de sécurité comme les identifiants de comptes email ?

J'ai modifié ma requête de recherche pour me concentrer sur les tableaux Trello contenant les mots de passe des comptes Gmail.

```
inurl:https://trello.com AND intext:@gmail.com AND intext:password
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZTQwW7EGpyypN0rJ09BMXUnzOEoLNx7vATRi)

Et qu'en est-il de SSH et FTP ?

```
inurl:https://trello.com AND intext:ftp AND intext:password
```

```
inurl:https://trello.com AND intext:ssh AND intext:password
```

![Image](https://cdn-media-1.freecodecamp.org/images/5sbSgGKEZQ4dCjahS1A20HGRvjJ0NJozV942)

### ? Ce que j'ai trouvé d'autre

Après avoir passé quelques heures à utiliser cette technique, j'ai fait d'autres découvertes étonnantes. Tout en continuant à modifier ma requête de recherche.

Certaines entreprises utilisent des tableaux Trello `Public` pour gérer les bugs et les vulnérabilités de sécurité trouvés dans leurs applications et sites web.

![Image](https://cdn-media-1.freecodecamp.org/images/rcT--o5vH-ohrAqIOxSzzbLRAWcvfZOYONUP)

Les gens utilisent également des tableaux Trello publics comme un **fancy** gestionnaire de mots de passe public pour les identifiants de leur organisation.

Certains exemples incluaient le serveur, [CMS](https://en.wikipedia.org/wiki/Content_management_system), [CRM](https://en.wikipedia.org/wiki/Customer_relationship_management), emails professionnels, comptes de réseaux sociaux, analytiques de sites web, Stripe, comptes AdWords, et bien plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/jqPEJQruX8MPqIZor6NIR3wxoH9lhpgfAH84)
_Exemples de tableaux Trello publics contenant des identifiants sensibles_

Voici un autre exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/M0IhGrqZYJgqwUZsLeZpyUummXbonwDEzD6l)
_Une ONG partageant les détails de connexion à leur logiciel de gestion des donateurs (base de données) qui contenait beaucoup d'informations personnelles identifiables ([personally identifiable information](https://en.wikipedia.org/wiki/Personally_identifiable_information" rel="noopener" target="_blank" title=")), et des détails comme les dossiers des donateurs et les enregistrements financiers_

Jusqu'alors, je ne me concentrais pas sur une entreprise ou un programme de bug bounty spécifique.

Mais neuf heures après avoir découvert cette faille, j'avais trouvé les coordonnées de presque **25 entreprises** qui fuitaient des informations très sensibles. Je les ai donc signalées. Trouver les coordonnées de certaines d'entre elles était une tâche fastidieuse et difficile.

J'ai posté à ce sujet dans un Slack privé de chasseurs de bug bounty et sur un serveur Discord infosec. J'ai également [tweeté à ce sujet](https://twitter.com/xKushagra/status/989074112411824129) juste après avoir découvert cette technique Trello. Les gens là-bas étaient aussi émerveillés et stupéfaits que moi.

Ensuite, les gens ont commencé à me dire qu'ils trouvaient des choses intéressantes comme des emails professionnels, des identifiants Jira et des informations internes sensibles de programmes de bug bounty grâce à la technique Trello que j'avais partagée.

![Image](https://cdn-media-1.freecodecamp.org/images/23G9wAjLnJmsDCY5tN8ZQhSncOwYbcbsRM9r)

Presque 10 heures après avoir découvert cette technique Trello, j'ai commencé à tester spécifiquement des entreprises exécutant des programmes de bug bounty. J'ai alors commencé par vérifier une entreprise bien connue de covoiturage en utilisant la requête de recherche.

```
inurl:https://trello.com AND intext:[company_name]
```

J'ai immédiatement trouvé un tableau Trello qui contenait les détails de connexion d'un compte email professionnel d'un employé, et un autre qui contenait certaines informations internes.

Pour vérifier cela, j'ai contacté quelqu'un de leur équipe de sécurité. Ils ont dit qu'ils avaient reçu un rapport sur le tableau contenant les identifiants de connexion d'un employé juste avant le mien et sur l'autre tableau contenant certaines informations internes. L'équipe de sécurité m'a demandé de leur soumettre un rapport complet car il s'agit d'une nouvelle découverte.

Malheureusement, mon rapport a été fermé comme étant un `Duplicata`. L'entreprise de covoiturage a ensuite découvert qu'elle avait déjà reçu un rapport sur le tableau Trello que j'avais trouvé.

Dans les jours qui ont suivi, **j'ai signalé des problèmes à 15 autres entreprises** concernant leurs tableaux Trello qui fuitaient des informations très sensibles sur leurs organisations. Certaines étaient de grandes entreprises, mais beaucoup ne disposent pas d'un programme de bug bounty.

L'une des 15 entreprises exécutait un programme de bug bounty, donc je leur ai signalé via celui-ci. Malheureusement, ils ne m'ont pas récompensé car il s'agissait d'un problème pour lequel ils ne paient actuellement pas. ?

#### Mise à jour — 18 mai 2018 :

Et il y a quelques jours, j'ai trouvé un ensemble de **tableaux Trello publics** contenant des informations vraiment sensibles (y compris des détails de connexion !) **d'un gouvernement**. Incroyable !

[The Next Web](https://thenextweb.com/security/2018/05/10/psa-saving-passwords-in-public-trello-boards-is-a-really-really-bad-idea/) et [Security Affairs](https://securityaffairs.co/wordpress/72380/data-breach/trello-data-leak.html) ont également rapporté cela.

#### Mise à jour — 17 août 2018 :

Au cours des derniers mois, j'ai découvert un total de **50 tableaux Trello des gouvernements britannique et canadien** contenant des informations confidentielles internes et des identifiants. [The Intercept](https://www.freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724/undefined) a écrit un article détaillé à ce sujet [ici](https://theintercept.com/2018/08/16/trello-board-uk-canada/).

[**Les gouvernements britannique et canadien ont accidentellement exposé des mots de passe et des plans de sécurité à l'ensemble...**](https://theintercept.com/2018/08/16/trello-board-uk-canada/)  
[_En mal configurant des pages sur Trello, un site populaire de gestion de projets, les gouvernements du Royaume-Uni et..._theintercept.com](https://theintercept.com/2018/08/16/trello-board-uk-canada/)

#### Mise à jour — 24 septembre 2018 :

En août, **j'ai trouvé 60 tableaux Trello publics**, un Jira public et un ensemble de Google Docs des **Nations Unies** qui contenaient des identifiants pour plusieurs serveurs FTP, des comptes de réseaux sociaux et emails, beaucoup de communications internes et des documents. [The Intercept](https://www.freecodecamp.org/news/discovering-the-hidden-mine-of-credentials-and-sensitive-information-8e5ccfef2724/undefined) a écrit un article détaillé à ce sujet [ici](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords).

[**Les Nations Unies ont accidentellement exposé des mots de passe et des informations sensibles à l'ensemble d'Internet**](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords)  
[_Les Nations Unies ont accidentellement publié des mots de passe, des documents internes et des détails techniques sur des sites web lorsqu'elles..._theintercept.com](https://theintercept.com/2018/09/24/united-nations-trello-jira-google-docs-passwords)

Merci d'avoir lu mon histoire.

Si vous avez aimé cet article, donnez-moi quelques applaudissements ?

Et vous pouvez [me suivre sur Twitter](https://twitter.com/xKushagra/) ✍️

[**Kushagra Pathak (@xKushagra) | Twitter**](https://twitter.com/xKushagra)  
[_Les derniers Tweets de Kushagra Pathak (@xKushagra). Chercheur en sécurité ?‍? | À la recherche d'un emploi. ?twi_tter.com](https://twitter.com/xKushagra)

_Je tiens à remercier_ [CyberSecStu](https://twitter.com/cybersecstu/), [Toffee](https://twitter.com/PolarToffee) _et l'équipe éditoriale de freeCodeCamp pour m'avoir aidé à relire et éditer cet article._