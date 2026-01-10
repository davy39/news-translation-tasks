---
title: Le Guide du Programmeur pour Organiser un Concert
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-20T15:29:00.000Z'
originalURL: https://freecodecamp.org/news/the-programmers-guide-to-booking-a-concert-e048a580735f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nf8zqZaL0U2EaVmiGupPew.png
tags:
- name: Data Science
  slug: data-science
- name: music
  slug: music
- name: san francisco
  slug: san-francisco
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Le Guide du Programmeur pour Organiser un Concert
seo_desc: 'By Sina Habibian

  About two months ago, a friend and I decided to organize a concert in San Francisco.
  We had no prior experience promoting shows, but we both loved live music and felt
  up to the challenge. Plus, 2016 had been a crappy year, and it see...'
---

Par Sina Habibian

Il y a environ deux mois, un ami et moi avons décidé d'organiser un concert à San Francisco. Nous n'avions aucune expérience préalable dans la promotion de spectacles, mais nous aimions tous les deux la musique live et nous sentions prêts à relever le défi. De plus, 2016 avait été une année pourrie, et il semblait que ce serait une bonne façon de rassembler la communauté et de terminer l'année sur une note positive.

Nous avons commencé par contacter des artistes locaux que nous connaissions personnellement dans l'espoir de les réserver pour un concert en décembre. Une semaine plus tard, nous avions épuisé notre liste de contacts et n'avions toujours pas de succès. J'ai commencé à réfléchir à la possibilité d'analyser les réseaux sociaux pour repérer des musiciens locaux.

J'ai décidé de me pencher sur Soundcloud, le lieu de rencontre en ligne de facto pour les musiciens. Ayant rencontré quelques musiciens grâce à un autre projet, je savais qu'ils utilisaient régulièrement la plateforme pour distribuer de la musique et se connecter avec les fans. Peu importait qui ou où quelqu'un était — un DJ de chambre à SoMa, un groupe de garage à Mountain View, ou un auteur-compositeur-interprète à Oakland — ils postaient tous de la musique sur Soundcloud. Et tant qu'ils avaient posté une seule piste, je savais que je pourrais les trouver.

### Explorer le Graphe Soundcloud

Un rapide coup d'œil à l'API de Recherche de Soundcloud a révélé qu'elle ne serait pas adéquate. La simple recherche par mot-clé ne me permettrait pas d'écrire une requête comme « retourner tout utilisateur basé à San Francisco ou Oakland qui a moins de 10k abonnés et a posté au moins une piste ».

À la recherche d'une solution, j'ai réalisé que l'exploration du graphe social pourrait être une approche efficace. Je pourrais écrire un algorithme qui, lorsqu'il est initialisé avec un utilisateur Soundcloud, récupérerait tous ses abonnés et abonnements, puis à son tour récupérerait tous les abonnés et abonnements pour chacun de ces utilisateurs. Cet algorithme récursif simple s'étendrait pour couvrir des milliers d'utilisateurs après quelques itérations. J'aurais ensuite le luxe d'analyser les connexions sociales de n'importe quelle manière, la plus simple étant d'écrire une requête SQL.

J'ai choisi Afrolicious, Mark Slee, EARMILK et quelques autres comme comptes de départ. Ces utilisateurs sont profondément intégrés dans les scènes hip hop, électronique et indie de San Francisco. J'étais convaincu que leur graphe social combiné fournirait une représentation diverse et complète de la musique de la région de la Baie.

Alors que je commençais à expérimenter avec l'algorithme, j'ai réalisé qu'il était peu pratique de récupérer les abonnés d'un utilisateur. Les musiciens ont régulièrement des dizaines ou des centaines de milliers d'abonnés (Calvin Harris, à l'extrémité extrême du spectre, a 7,08 millions d'abonnés). Récupérer tous les abonnés pour tous les utilisateurs était évidemment une approche sous-optimale. Je n'avais pas non plus l'intention de payer mille dollars par mois en coûts de base de données.

La solution était d'explorer uniquement les _abonnements_ et non les abonnés. Les musiciens suivent d'autres musiciens. Intéressamment, il existe même des articles qui ont analysé ce comportement et les « scènes virtuelles » qui émergent ([Allington et al., 2015](http://dx.doi.org/10.1080/09548963.2015.1066073)). En explorant le graphe des abonnements, je pourrais cartographier efficacement la scène musicale locale. De plus, en gardant une trace de qui suit qui, je pourrais ensuite utiliser un algorithme comme PageRank pour trouver des talents émergents qui n'ont pas encore beaucoup d'abonnés mais qui ont néanmoins un vote de confiance de la communauté.

J'ai construit une application Sinatra pour explorer le graphe social de Soundcloud et j'ai sauvegardé tous les utilisateurs et leurs relations dans une base de données Postgres. Après quelques itérations, il y avait plus de 200k utilisateurs et 500k relations. Il était temps de donner un sens aux données.

### Analyser le Réseau

J'ai écrit un script Python pour interroger la base de données pour tout utilisateur Soundcloud avec au moins 500 abonnés, au moins une piste, et basé à San Francisco ou Oakland. J'ai ensuite cartographié ces utilisateurs et leurs relations sur un graphe dirigé [Networkx](https://networkx.github.io/). Il était alors simple d'exporter un fichier de graphe .gexf qui pourrait être consommé par [Gephi](https://gephi.org/) pour une analyse visuelle.

Gephi s'est avéré être un outil incroyable pour visualiser les réseaux sociaux et m'a donné plus qu'assez à explorer.

![Image](https://cdn-media-1.freecodecamp.org/images/AWLLpA9AOHqudPcnIpntMuuSnKm0DcsCQhr0)
_Le réseau Soundcloud à San Francisco et Oakland. La taille correspond au PageRank et la couleur correspond à la communauté._

Ce qui précède est un graphe dirigé du réseau Soundcloud. J'ai d'abord utilisé PageRank pour exploiter les relations existantes entre abonnés et abonnements et déterminer quels sont les nœuds les plus importants. Cela est représenté par la taille d'un nœud. J'ai ensuite superposé un algorithme d'optimisation de modularité intégré pour détecter les communautés. La communauté est représentée par la couleur d'un nœud.

Ce graphe offre un point de vue intéressant sur la scène musicale de San Francisco. Le plus grand nœud, Anthony Mansfield, est un DJ de House vétéran de la région de la Baie qui est également profondément impliqué dans le camp Disco Knights de Burning Man. Un autre grand nœud est Honey Sound System, un collectif de DJ qui appelle San Francisco leur maison. Le coin inférieur gauche du graphe est un groupe Hip Hop incluant des artistes de San Francisco comme Telli Prego et Show Banga.

Notre objectif était de trouver des musiciens pour notre prochain concert. Ironiquement, cela était maintenant difficile étant donné la quantité d'options disponibles. Nous avions identifié plus d'un millier de comptes Soundcloud comme musiciens dans la région de la Baie. Nous n'avions pas un bon moyen d'écouter cette quantité de musique sans copier chaque URL Soundcloud dans le navigateur. De plus, nous voulions des avis de nos amis et de notre communauté sur les artistes qu'ils aimeraient voir en live.

### Repérer les Talents

Pour résoudre ces problèmes, j'ai ajouté une couche d'interface utilisateur à l'application Sinatra afin que nous puissions rationaliser nos efforts de repérage. Elle affichait une liste de musiciens classés selon les résultats de l'analyse de réseau précédente. Il y avait un widget Soundcloud intégré afin que nous puissions écouter la musique d'un artiste sans quitter la page. J'ai également ajouté un système de notation afin que nous puissions évaluer chaque artiste et commenter si nous voulions les voir en live.

![Image](https://cdn-media-1.freecodecamp.org/images/0I0zLpDW6C0oSgcROpgtmAAfHEgrYxZrSSBU)
_Interface pour évaluer un artiste._

J'ai ensuite ajouté un schéma d'authentification utilisateur afin que plusieurs personnes puissent utiliser le système en même temps. Nous avons sollicité l'aide de quelques amis vivant dans la ville qui apprécient également la musique. Avec leur aide et notre nouveau système de repérage de talents, nous avons collectivement écouté et voté pour 400 artistes. J'ai ensuite construit une page d'administration afin que je puisse voir les musiciens les mieux notés sur la plateforme.

![Image](https://cdn-media-1.freecodecamp.org/images/OemmvmzPBF24CqG4YLoyiDx-9O5wukMVpEBD)
_Interface d'administration avec les notations des repérages agrégées._

Nous avions externalisé nos efforts de repérage et commencions à trouver quelques pépites. Plus important encore, nous avions validé la demande concernant les artistes locaux que nos amis et notre communauté voulaient voir en live.

### Réserver le Spectacle

Avec les choses qui se mettaient en place, nous nous sommes donné un nom : les Gremlins. Les Gremlins sont mignons, espiègles et sont toujours en train de s'amuser et de casser des choses. Cela semblait approprié étant donné nos progrès jusqu'à présent.

Nous avons contacté quelques-uns de nos nouveaux artistes préférés et réservé deux talents locaux funky : Foxtails Brigade et Baby's Day Out. Nous parlions avec des lieux en parallèle et avons obtenu une soirée à The Lost Church, un théâtre chaleureux dans The Mission avec une capacité de 75 personnes. L'intérieur en bois et les œuvres d'art éclectiques éparpillées dans l'endroit étaient en accord avec l'atmosphère que nous essayions de créer.

### Les Gremlins Présentent

Un mois plus tard, nous sommes entrés dans The Lost Church le soir du concert. J'ai ressenti un sentiment d'accomplissement alors que nous accueillions des amis et des futurs amis dans le théâtre. Le spectacle était complet.

Laura de Foxtails Brigade et Meggy et Mel de Baby's Day Out ont partagé leur musique avec un public animé. Nous les avons suivis à travers des moments joyeux et mélancoliques. Ce fut une soirée mémorable.

![Image](https://cdn-media-1.freecodecamp.org/images/PS21N1tC1buRspcVXwVQoDvhSrwmxWtj8AaB)
_Les Gremlins !_

![Image](https://cdn-media-1.freecodecamp.org/images/qHoROWic974rFY6nT92i9uGG0S8LxGBDange)
_Les Gremlins présentent : Baby's Day Out !_

![Image](https://cdn-media-1.freecodecamp.org/images/i4A4-kTZSLdDk52YXfveubDfePbpIdCxVmEq)
_Les Gremlins présentent : Laura Weinbach !_

En coordonnant ce concert, j'ai vécu deux perspectives étrangement différentes sur la vision d'un « musicien ». D'abord, en tant que nœud dont l'importance relative et le degré de connectivité peuvent être calculés dans un réseau connecté. Ensuite, en tant qu'être humain talentueux et plein d'âme qui peut émouvoir un public à travers l'expression de son art.

Cette dichotomie est un fait de la vie dans le monde d'aujourd'hui. Nous sommes chacun fortement connectés dans les graphes sociaux de Facebook, Instagram et Twitter. Il est fascinant de nous imaginer comme des nœuds dans cette perspective. Je me demande quelles perspectives les bricoleurs de ces entreprises ont glanées sur nos vies intérieures.

[_Abonnez-vous_](https://sinahab.com/subscribe/) pour suivre mes écrits, ou contactez-moi sur [Twitter](https://twitter.com/sinahab).