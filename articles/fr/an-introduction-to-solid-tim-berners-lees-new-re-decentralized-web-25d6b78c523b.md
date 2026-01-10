---
title: Une introduction à SOLID, le nouveau Web re-décentralisé de Tim Berners-Lee
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-29T15:20:48.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-solid-tim-berners-lees-new-re-decentralized-web-25d6b78c523b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*P4F0K6HR2L0VfQZmMvYt0g.png
tags:
- name: decentralization
  slug: decentralization
- name: internet
  slug: internet
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Une introduction à SOLID, le nouveau Web re-décentralisé de Tim Berners-Lee
seo_desc: 'By Arnav Bansal

  Recently, Prof. Tim Berners-Lee lifted the veil off a project called Solid. I decided
  to check it out. In this article, I describe what Solid aims to do, and also how
  you can get started with it.

  What is Solid?

  Solid is an attempt to ...'
---

Par Arnav Bansal

Récemment, [Prof. Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee) a levé le voile sur un projet appelé Solid. J'ai décidé de le vérifier. Dans cet article, je décris ce que Solid vise à faire, et aussi comment vous pouvez commencer avec lui.

### Qu'est-ce que Solid ?

Solid est une tentative de re-décentraliser le web.

_Re**-**_décentraliser ?

À l'époque, la vision du web était un espace de lecture-écriture décentralisé et collaboratif. Le premier navigateur (appelé WorldWideWeb) était [aussi un éditeur](https://www.w3.org/People/Berners-Lee/WorldWideWeb.html).

Cependant, au fur et à mesure de son évolution, la conception des applications web a commencé à se centraliser pour diverses raisons. Les données des utilisateurs sont devenues la source de pouvoir et de revenus pour les entreprises Internet.

Solid est une solution à cela.

Solid est un nouveau paradigme pour les applications web, compatible avec le web existant.

Solid est une pile technologique, un groupe de protocoles, d'implémentations et une communauté grandissante. Un peu comme le web.

### La séparation de l'application et des données

Dans l'informatique pré-internet, votre ordinateur personnel stockait vos données.

Alors que les gens ont commencé à utiliser plusieurs ordinateurs et ont ajouté des smartphones à leur vie, le modèle "vos données restent avec vous" a été remplacé par "Vos données sont dans un ou plusieurs centres de données massifs dans le monde, gérés par le développeur de l'application".

Et ainsi, les applications étaient profondément couplées à leurs données. Créer une application sur le web implique de gérer les données des gens à grande échelle.

Les applications et leur capacité à gagner de l'argent sont mesurées par leur _silo de données_. Vos données sont difficiles à migrer, car différentes applications stockent vos données de manière très différente.

Le résultat ? Presque toutes les applications ont des caractéristiques de jardin clos. Cela réduit les incitations pour les développeurs à innover au niveau de l'application. Les plateformes existantes sont protégées contre les perturbations, car le verrouillage des données rend difficile le déplacement des utilisateurs.

### Règlementations sur la protection des données

Certains pays ont promulgué des lois sur la protection des données. Les entreprises doivent rendre vos données disponibles, et vous pouvez choisir de les télécharger ou de les supprimer.

Cela tente de rendre le contrôle des données aux utilisateurs. Mais c'est une prescription légale, et non la réalité technique. Les données des utilisateurs restent entre les mains des développeurs d'applications, et la capacité à télécharger vos données n'est pas très utile si vous ne pouvez pas migrer vers une alternative.

### Pods : Apportez vos propres données

Solid remédie à cela sur le plan technique. Il permet de construire des applications de manière à ce qu'elles lisent et écrivent des données stockées sur votre _pod_.

Vous avez un pod. Vos amis ont un pod. Les pods stockent vos données. Vous autorisez les applications à accéder à votre pod.

Peut-être avez-vous plusieurs pods. Peut-être des pods séparés pour la maison et le travail. Votre pod peut vivre sur votre ordinateur ou être distribué sur vos appareils. Ou il pourrait être hébergé pour vous.

Et les pods stockent des _données liées_. Votre pod peut lier quelque chose sur mon pod, ou n'importe où sur le web.

Nous voulons des applications qui fonctionnent sur nos appareils. Mais nous voulons aussi l'autonomie de nos données. Et nous voulons la capacité pour différentes applications d'utiliser les mêmes données et d'y écrire.

### Les idées derrière Solid

Se lancer dans Solid m'a rappelé mes débuts dans le développement web. Je me souviens avoir appris HTML, CSS, JavaScript et les frameworks de l'époque, tout en même temps.

La seule différence : Solid est nouveau, et l'aide est plus difficile à trouver.

Voici une collection de concepts de premier jour que vous voudrez connaître pour commencer à développer pour Solid :

(PS : si vous voulez simplement vous lancer, passez directement à "Premiers pas")

#### **Données liées**

La puissance de Solid, et du web en général, vient de la manière dont les données sont hyperliées ensemble.

Dans Solid, vous stockez les données que vous produisez où vous voulez. Vos données personnelles résident probablement sur votre pod. Pour faire référence à ces données, vous utilisez des URL, comme sur le web.

C'est aussi un bon moment pour introduire la forme complète de Solid : **SO**cial **LI**nked **D**ata.

Lisez à propos des [Données Liées dans le contexte de Solid](https://solid.inrupt.com/docs/intro-to-linked-data)

#### **Resource Description Framework**

RDF est un moyen de représenter des données liées avec des déclarations de la forme `sujet-prédicat-objet`. Ce sont aussi appelés des triples.

RDF est un modèle abstrait. Vous pourriez même représenter RDF en phrases anglaises. Voici une tâche sur une liste de choses à faire :

```
T1 est une tâcheT1 est étiquetée "Écrire un article sur Solid"T1 est due le 5 octobre 2018T1 est assignée à @itsarnavbT1 est incomplète
```

#### **Turtle**

Turtle est une manière compacte de représenter les données RDF, en utilisant des URL pour représenter `sujet`, `prédicat` et `objet`.

C'est répétitif et difficile à lire, donc turtle a un système de préfixe et d'abréviation. Cela devient particulièrement important avec des documents plus longs.

Vous pouvez en lire plus sur [turtle](https://solid.inrupt.com/docs/expressing-ld-with-turtle). Ou vous pourriez consulter un document turtle complet [ici](https://ruben.verborgh.org/profile/#me). C'est un profil public détaillé du Prof. Ruben Verborgh, qui fait partie de l'équipe Solid.

#### Web sémantique

Tim Berners-Lee explique cela le mieux :

> J'ai un rêve pour le Web [dans lequel les ordinateurs] deviennent capables d'analyser toutes les données sur le Web - le contenu, les liens et les transactions entre les personnes et les ordinateurs. Un "Web Sémantique", qui rend cela possible, reste à émerger, mais quand il le fera, les mécanismes quotidiens du commerce, de la bureaucratie et de notre vie quotidienne seront gérés par des machines qui parlent à des machines. Les "[agents intelligents](https://en.wikipedia.org/wiki/Intelligent_agent)" que les gens ont vantés depuis des âges finiront par se matérialiser.

### Premiers pas

Faites ces étapes, dans l'ordre qui vous convient.

* [Obtenez un pod](https://solid.inrupt.com/get-a-solid-pod) : Inscrivez-vous avec un fournisseur de pod gratuit ou exécutez votre propre serveur (si c'est votre truc).
* [Créez une application Solid avec ce tutoriel](https://solid.inrupt.com/docs/app-on-your-lunch-break)
* [Lisez à propos de ces hacks réalisés avec Solid](https://solid.gitbook.io/solid-hacks/)
* [Lisez la documentation Solid](https://solid.inrupt.com/docs)

### Allez Solid

Vous pouvez aider l'écosystème Solid en

* contribuant au développement de Solid lui-même et de l'infrastructure connexe.
* développant des applications utilisant Solid.

![Image](https://cdn-media-1.freecodecamp.org/images/0*tapHw7Osr5LbkuUh)

Mais attention, pour le moment, apprendre et développer pour Solid nécessite beaucoup d'essais et d'erreurs, et poser des questions potentiellement stupides. Il n'y a pas de Stack Overflow à consulter. Le débogage de certaines erreurs peut nécessiter de plonger dans le code source.

Voici les communautés où vous pouvez obtenir de l'aide :

* [r/solid](https://reddit.com/r/solid) (Je suis l'un des modérateurs)
* [gitter.im/solid](https://gitter.im/solid/home)

Et enfin, mes DM sont ouverts : [@itsarnavb](https://twitter.com/itsarnavb). J'essaierai de répondre à toutes les questions que je reçois, ou de trouver quelqu'un qui peut le faire.

Et je garderai cet article à jour avec les meilleures ressources pour apprendre Solid.

### Lectures complémentaires

* [Site web de Solid - solid.mit.edu](https://solid.mit.edu)
* [Changements de paradigme pour le web décentralisé - Ruben Verborgh](https://ruben.verborgh.org/blog/2017/12/20/paradigm-shifts-for-the-decentralized-web/)
* [Un petit pas pour le Web - Tim Berners-Lee](https://medium.com/@timberners_lee/one-small-step-for-the-web-87f92217d085)