---
title: L'art aléatoire et le sapin de Noël cryptographique
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-11-29T18:12:35.000Z'
originalURL: https://freecodecamp.org/news/the-geekiest-ugly-sweater-ever-34a2e591483f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3J45l0AZ0VANlUsoXzZKYg.jpeg
tags:
- name: Design
  slug: design
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: L'art aléatoire et le sapin de Noël cryptographique
seo_desc: 'When I first learned how to code, one of my first tasks was setting up
  an SSH key so I could use encryption to securely connect to my friend’s Linux server.

  I ran the command:

  ssh-keygen -t rsa

  Then my computer created my SSH keys and spat out this “...'
---

Lorsque j'ai appris à coder pour la première fois, l'une de mes premières tâches était de configurer une clé SSH afin de pouvoir utiliser le chiffrement pour me connecter en toute sécurité au serveur Linux de mon ami.

J'ai exécuté la commande :

```
ssh-keygen -t rsa
```

Ensuite, mon ordinateur a créé mes clés SSH et a généré cet "art aléatoire" :

![Image](https://cdn-media-1.freecodecamp.org/images/p6XU-k6WwG2hCyGbXXJHq2CGVUM0sK6sa2g2)

« Qu'est-ce que c'est ? » ai-je demandé, en plissant les yeux devant l'art aléatoire et en essayant de trouver un ordre dans le chaos.

Mon ami s'est penché par-dessus mon épaule et a dit : « Oh, c'est un art aléatoire. On dirait que tu as obtenu un petit sapin de Noël cryptographique mignon. »

J'ai un peu plissé les yeux et tourné la tête. En effet, cela ressemblait à un sapin de Noël !

Il s'avère que ces arts aléatoires sont assez utiles. Aussi désordonnés qu'ils puissent paraître, ils sont [beaucoup plus faciles pour les humains à différencier](http://unix.stackexchange.com/a/144727) que de longues chaînes de code hexadécimal.

Comparez ces deux arts aléatoires :

```
+--[ RSA 2048]----+|        .        ||       + .       ||      . B .      ||     o * +       ||    X * S        ||   + O o . .     ||    .   E . o    ||       . . o     ||        . .      |+-----------------+
```

```
Versus :
```

```
+--[ RSA 2048]----+|       .o o..    ||       o +Eo     ||        + .      ||         . + o   ||        S o = * o||           . o @.||            . = o||           . o   ||            o.   |+-----------------+
```

Maintenant, essayez de comparer ces deux chaînes de code hexadécimal :

```
2048 1b:b8:c2:f4:7b:b5:44:be:fa:64:d6:eb:e6:2f:b8:fa 192.168.1.84 (RSA)
```

```
Versus :
```

```
2048 1b:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48 192.168.1.84 (RSA)
```

Vous voyez ce que je veux dire ? Donc, l'art aléatoire. CQFD.

### Une étrange tradition de vacances

Avance rapide jusqu'à la semaine dernière. Je pensais à concevoir un pull moche pour les fêtes.

Je n'avais jamais possédé de pull moche sauf un que ma tante avait tricoté pour moi. Et je ne me suis même pas rendu compte que c'était un pull moche jusqu'à des années plus tard, lorsque je feuilletais l'album de ma grand-mère et que je suis tombé sur une photo horrifiante de moi en train de le porter.

Pourtant, je me suis convaincu que les pulls moches [étaient effectivement une chose](http://newsfeed.time.com/2011/12/22/a-brief-history-of-the-ugly-christmas-sweater/).

« Les gens organisent des fêtes de pulls moches ! » m'a-t-il dit. « Tu mets le pull de Noël le plus moche que tu peux trouver, puis tu vas boire de l'[eggnog](https://en.wikipedia.org/wiki/Eggnog) ensemble ! »

Une rapide recherche sur Google a confirmé qu'il avait raison. J'avais vécu dans une bulle toutes ces années et j'avais manqué la splendeur des fêtes de pulls moches.

### Conception du pull moche

J'ai donc réfléchis pendant un moment. Quelle était la chose la plus moche que je pouvais imaginer en relation avec la programmation ? Du CSS minifié ? Une trace de pile C++ ?

C'est alors que je me suis souvenu de mon premier art aléatoire de clé SSH et du commentaire de mon ami sur le fait qu'il ressemblait à un sapin de Noël.

J'ai appelé [Wesley Searan](https://dribbble.com/Searan), un designer graphique à Austin, au Texas. Wesley et moi avons échangé des idées de design pendant quelques jours.

J'ai fait la chose agile et [tweeté](https://twitter.com/ossia/status/803266288009129984) un brouillon de notre design pour obtenir des commentaires de notre communauté.

Les gens voulaient que nous retirions le XMAS 2016 (que j'avais utilisé à la place du RSA 2048) afin qu'ils puissent porter le pull lors des fêtes suivantes. Et ils voulaient aussi des T-shirts et des hoodies. Nous avons donc rendu ceux-ci disponibles.

Comme toujours, nous avons rendu ces actifs sous licence creative-commons et les avons mis à disposition sur le [dépôt d'actifs](https://www.github.com/freecodecamp/assets) de Free Code Camp pour que tout le monde puisse s'amuser avec.

Voici à quoi ressemble [le pull terminé](https://www.freecodecamp.com/shop), avec un fond kitsch :

![Image](https://cdn-media-1.freecodecamp.org/images/bI6NMfF5HolzcqqAsa2yvieUAw7v8dnBQitX)

Ainsi, vous pouvez maintenant organiser votre fête de pulls de Noël moches ou simplement en porter un lors des rassemblements familiaux. Vous serez la personne la plus geek de l'assistance (ce qui est une bonne chose !) dans votre pull moche génial avec un art aléatoire de clé SSH.

Ceux-ci seront disponibles dans [la boutique de notre communauté](https://freecodecamp.com/shop) pendant les prochains jours, alors procurez-vous-en un.

Bon chiffrement !