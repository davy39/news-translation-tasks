---
title: 'Les prochaines étapes de mon parcours Outreachy : Docker, grands défis et
  petites victoires'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T19:03:44.000Z'
originalURL: https://freecodecamp.org/news/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2-_OdNIVPbRBjJKb7OiNgw.jpeg
tags:
- name: Docker
  slug: docker
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Les prochaines étapes de mon parcours Outreachy : Docker, grands défis
  et petites victoires'
seo_desc: 'By Toni Shortsleeve

  This has been an interesting couple of weeks for me. As a result, I was slightly
  delayed in getting this article out.

  I was recently selected to intern at Outreachy. Outreachy is a program that organizes
  three-month paid internshi...'
---

Par Toni Shortsleeve

Ces dernières semaines ont été intéressantes pour moi. En conséquence, j'ai été légèrement retardée dans la publication de cet article.

J'ai récemment été sélectionnée pour un stage chez Outreachy. Outreachy est un programme qui organise des stages rémunérés de trois mois avec des projets de logiciels libres et open source pour les personnes généralement sous-représentées dans le domaine technologique.

En tant que stagiaire Outreachy, j'ai pour mission d'écrire sur mon expérience toutes les deux semaines. C'est une première pour moi, car je suis habituée à éditer plutôt qu'à écrire.

Dans mon premier [article](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e), je venais d'être acceptée en tant que stagiaire [Outreachy](https://www.outreachy.org/) travaillant avec [LibreHealth](http://librehealth.io/). Le deuxième [article](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619) discutait de ma préparation pour commencer le stage proprement dit après mon acceptation. Aujourd'hui, je vais partager où j'en suis depuis le début du stage.

### Vouloir en savoir plus

J'ai récemment soumis ma dernière révision de la documentation sur laquelle je travaille, et j'attends des retours. Entre-temps, je me suis rendu compte que je n'avais toujours pas assez d'informations sur le module de radiologie et le LibreHealth Toolkit qui le fait fonctionner.

Ma collègue stagiaire [@adele](https://medium.com/@nguimatiobest) m'a orientée vers un excellent [blog](https://ivange94blog.wordpress.com/). Ivange Larry Ndumbe est un stagiaire GSOC 2017 qui a travaillé sur le module de radiologie de LibreHealth.

Quelques-uns de ses articles m'ont mise sur la bonne voie pour aider à configurer le Toolkit. Il s'est avéré que je devais télécharger Docker. Mais il y avait un problème : je n'avais aucune idée de ce qu'était Docker ou de ce qu'il faisait.

### Quelques détours

Mais parfois, le timing est tout. Juste à ce moment-là, j'ai eu la chance d'éditer [Let me guide you through your first date with Docker](https://medium.freecodecamp.org/let-me-guide-you-through-your-first-date-with-docker-f03f35567d95) pour la publication Medium de freeCodeCamp. Cela m'a donné une bonne introduction aux téléchargements de Docker. Sauf que le téléchargement de Docker pour Windows n'est disponible que pour Windows 10.

Vous vous souvenez de Windows 95, Vista et XP ? Mon ordinateur, oui. Ils étaient meilleurs amis à travers chaque nouvelle mise à jour jusqu'à Windows 8. Je suis parfaitement heureuse avec la plupart de mes mises à jour logicielles au fil des ans. Mais j'ai trouvé que certains de mes favoris n'étaient plus disponibles après la mise à jour. Et personnellement, je ne suis pas assez impressionnée par Windows 10 pour abandonner mes suites préférées. Cela a été la source de mon angoisse lors de cette dernière session.

Plus de recherches m'ont menée à la [Toolbox](https://docs.docker.com/toolbox/overview/) de Docker. Mais d'abord, la documentation de Docker disait :

> Assurez-vous que votre système Windows prend en charge la technologie de virtualisation matérielle et que la virtualisation est activée.

**C'était effrayant.**

![Image](https://cdn-media-1.freecodecamp.org/images/pa-0s9ghXHuagCoD9VBrxNUSX2wLk2X9SlEv)

Retour à la recherche. J'ai (en quelque sorte) trouvé une stratégie pour activer la virtualisation [ici](https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html).

J'ai dû accéder au BIOS de mon ordinateur pendant son démarrage et changer un code avant qu'il ne charge complètement.

Cela a pris beaucoup de redémarrages. J'ai dû essayer les touches `F` suggérées tout en étant assez rapide pour les attraper avant que le système ne passe complètement à la phase de démarrage. Ensuite, j'ai répété le redémarrage avec une touche `F` différente jusqu'à ce que je trouve la bonne au bon moment. Après avoir essayé toutes ces touches `F`, j'ai essayé la touche `Suppr`. Succès !

Bien sûr, mon interrupteur était caché dans la section avancée, et j'ai dû chercher pour trouver les bonnes commandes. Mais au redémarrage suivant, la virtualisation était activée !

### Une victoire à la fois

Il était maintenant temps de télécharger la Docker Toolbox. Cela a pris quelques essais, mais j'étais prête à exécuter la commande `docker-compose`. Mais j'ai oublié de lancer la commande en tant qu'administrateur, et mon accès a été refusé.

Je l'ai donc relancée, cette fois en tant qu'administrateur. Et j'ai reçu une erreur `Fichier introuvable`.

Retour à la recherche. Le salon de discussion [freeCodeCamp](https://www.freecodecamp.org/) [PairProgrammingWomen](https://gitter.im/FreeCodeCamp/PairProgrammingWomen) a été formidable pour me connecter via des messages privés et m'envoyer des liens utiles. Et mon mentor technique a été génial en fournissant encore plus de liens et d'informations utiles.

J'ai finalement réussi à faire fonctionner Docker Compose ! Mais maintenant, je ne peux pas accéder à mon localhost. Mon mentor continue de travailler avec moi sur ce problème. C'est un processus.

### Avancer

Je vais continuer à suivre la suggestion que j'ai reçue du salon de discussion freeCodeCamp d'utiliser la méthode Read-Search-Ask. Je vais également parcourir tous ces liens et continuer à créer une installation de radiologie gérable.

Ce sera un excellent guide utilisateur d'ici la fin. Merci de m'accompagner dans la suite de mon parcours de stage avec Outreachy et LibreHealth. À la prochaine !