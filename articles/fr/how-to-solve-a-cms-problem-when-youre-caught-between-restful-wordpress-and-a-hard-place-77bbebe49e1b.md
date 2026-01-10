---
title: Comment résoudre un problème de CMS lorsque vous êtes coincé entre RESTful,
  WordPress et une situation difficile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-19T02:34:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-solve-a-cms-problem-when-youre-caught-between-restful-wordpress-and-a-hard-place-77bbebe49e1b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IQ9QA3Sy1kX7XdmZmFwlYg.jpeg
tags:
- name: cms
  slug: cms
- name: General Programming
  slug: programming
- name: storytelling
  slug: storytelling
- name: technology
  slug: technology
- name: WordPress
  slug: wordpress
seo_title: Comment résoudre un problème de CMS lorsque vous êtes coincé entre RESTful,
  WordPress et une situation difficile
seo_desc: 'By Jessica Duffin Wolfe

  Last fall I was trying to decide on how to host and manage a small storytelling
  project built by around 40 users — my students. I wanted them to have a clean and
  easy experience uploading their content (images and audio files,...'
---

Par Jessica Duffin Wolfe

L'automne dernier, je tentais de décider comment héberger et gérer un petit [projet de narration](http://36to.ca/#/) construit par environ 40 utilisateurs — mes étudiants. Je voulais qu'ils aient une expérience propre et facile pour télécharger leur contenu (images et fichiers audio, ainsi que du texte). Je voulais également que celui-ci soit stocké à long terme dans un format que mon petite application Vue.js pourrait facilement récupérer et afficher sans trop de configuration ni de surcharge de ma part.

J'ai compté très heureusement sur WordPress comme système de gestion de contenu (CMS) principal pendant des années, mais il commence à sembler un peu vieillot ces derniers temps, et il n'est pas tout à fait conçu pour un projet aussi axé sur l'audiovisuel et multi-utilisateurs, j'ai donc décidé de chercher d'autres options plus récentes.

### **Option 1 : Google Sheets**

Le chemin le plus simple semblait être de configurer une feuille Google Sheets que les étudiants pourraient remplir avec des liens vers leurs propres médias auto-hébergés. J'ai eu de bonnes expériences en construisant de petits sites comme celui-ci en important les données via JSON.

Dans ce cas, cependant, avec environ quinze éléments de contenu différents pour chaque contribution d'utilisateur, si j'utilisais une feuille de calcul, ce serait un monstre, et la remplir ne serait pas une bonne expérience utilisateur pour les étudiants.

Les liens vers les médias auto-hébergés des étudiants risquaient également de devenir invalides avec le temps, à mesure que les comptes expirent et que les services disparaissent. Je ne voulais pas que le projet devienne incomplet, et je ne voulais pas avoir à faire trop de maintenance chaque année pour le garder solide.

Donc, non à Google Sheets.

### **Option 2 : Contentful**

[Contentful](https://www.contentful.com/) est un CMS headless, ce qui signifie qu'il fournit une infrastructure pour stocker, éditer et servir du contenu sans offrir aucun type d'affichage frontal. WordPress traditionnel, en revanche, est conçu pour faire les deux — stocker votre contenu et offrir tout le code qui le récupère et l'affiche. Cette grande pile de fonctionnalités le rend assez encombrant, et de plus en plus, il ne semble pas aussi agile qu'un outil web devrait l'être.

J'étais vraiment enthousiaste à propos de Contentful. Il est si joli et élégant ! Et si intelligent — il permet le géotagging direct du contenu ! Ahhh. Et je pourrais configurer un modèle de contenu personnalisé qui correspondrait exactement au projet en cours, et c'était amusant ! Youpi.

Après avoir passé du temps à configurer Contentful, je voulais désespérément l'utiliser, mais j'ai commencé à perdre mon intérêt plus je réfléchissais à la façon dont les étudiants téléchargeraient leur travail.

Le niveau gratuit est limité à cinq utilisateurs. Bien que j'aurais pu faire en sorte que les étudiants téléchargent leur contenu via un compte utilisateur générique, cela n'aurait pas été une bonne expérience, car ils auraient dû naviguer dans le back-end et les fichiers des autres pour soumettre leur travail.

Je n'étais également pas convaincu que le niveau gratuit couvrirait les besoins d'hébergement de ce projet. Cela aurait probablement été suffisant — mais j'aurais dû surveiller la bande passante, les requêtes API et le statut à long terme du contenu.

Avec le premier niveau payant commençant à 249 $ par mois, passer à un niveau supérieur était trop cher à considérer. Ce prix m'a dissuadé même d'utiliser un compte gratuit, car je savais que je ne mettrais jamais à niveau à ce prix. Il y avait donc un risque que je doive migrer tout si je commençais à construire le projet sur ce service.

Il était clair que Contentful ne voulait pas vraiment s'occuper des travaux expérimentaux à petite échelle — ce qui est compréhensible — et de toute façon, cela devenait trop ennuyeux de s'attarder sur ces détails pour un petit projet.

### **Option 3 : WordPress RESTful**

Alors que j'essayais de faire fonctionner Contentful, je continuais à revenir à une installation WordPress pour jouer avec. Encombrant que le vieux WP peut être, face à l'approche de Contentful qui facture pour les "enregistrements" de contenu, je commençais à ressentir une grande nostalgie pour la facilité et la liberté d'ajouter du contenu dans WordPress.

Je me suis dit — bien, hey — pourquoi ne pas utiliser WordPress comme un CMS headless avec sa nouvelle fonctionnalité d'API REST ? Cela me permettrait de contourner l'encombrement de servir du contenu via PHP, tout en me permettant d'utiliser WordPress comme un CMS, une interface que mes étudiants connaissent bien.

Pour permettre aux étudiants d'ajouter toutes les images et l'audio pour leurs projets, je devrais ajouter un type de publication personnalisé. Pour cela, je devrais ajouter un plugin. Pour utiliser le plugin, je devrais comprendre comment le configurer, puis créer un type de publication personnalisé approprié qui fournirait une interface facile à utiliser dans le système WP. Pour cela, je devrais réécrire WordPress de fond en comble, car, malgré ses bonnes intentions, il n'est pas conçu pour faire autre chose que ressembler et fonctionner comme WordPress. Il gère les articles de blog vraiment, vraiment, vraiment bien, et peut être bricolé pour faire d'autres choses, mais pas bien. L'odeur de l'article de blog ne s'estompe jamais vraiment.

J'ai abandonné tout cela avant même d'essayer de comprendre comment j'utiliserais l'API REST dans mon projet. Je suis toujours enthousiaste à ce sujet, cependant. C'est probablement une option incroyable pour servir du contenu à partir de sites plus grands utilisant des frameworks JS.

### **Option 4 : WordPress + Formulaires = CMS Sugar**

La solution sur laquelle j'ai finalement arrêté mon choix semblait ridiculement simple et un drôle d'amalgame de tous mes efforts précédents.

En utilisant Gravity Forms, un plugin WordPress que je connais bien grâce à d'autres projets, j'ai construit un formulaire de base à travers lequel les étudiants pouvaient télécharger leurs quinze fichiers et coller leurs composants textuels.

J'ai exporté les entrées sous forme de feuille de calcul avec des liens vers le contenu téléchargé stocké dans le site WordPress, et j'ai transformé ce fichier en JSON pour l'utiliser comme je l'aurais fait avec une feuille Google Sheets.

Ainsi, mes étudiants ont eu une expérience propre, familière et accessible pour télécharger leur contenu, et je pourrai le stocker à long terme sans tracas dans un format avec lequel mon application web statique fonctionnera bien. Problème résolu.

Ta da ! Pourquoi cette solution n'était-elle pas plus évidente lorsque j'ai commencé ?

Pour moi, une morale de cette histoire est que même à cette ère d'options de déploiement de plus en plus sophistiquées et bien reposées, il est toujours utile de bien connaître WordPress — malgré son âge, son faible coût et son écosystème riche en fonctionnalités continuent de réduire les barrières à la créativité numérique.