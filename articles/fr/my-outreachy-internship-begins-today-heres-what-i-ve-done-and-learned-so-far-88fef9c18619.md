---
title: Mon stage Outreachy commence aujourd'hui ! Voici ce que j'ai fait et appris
  jusqu'à présent.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T01:24:58.000Z'
originalURL: https://freecodecamp.org/news/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VLRQmKC6ipGiZS3il-wQWw.jpeg
tags:
- name: healthcare
  slug: healthcare
- name: internships
  slug: internships
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: technology
  slug: technology
seo_title: Mon stage Outreachy commence aujourd'hui ! Voici ce que j'ai fait et appris
  jusqu'à présent.
seo_desc: 'By Toni Shortsleeve

  Today marks the first day of my official full-time Outreachy Internship with LibreHealth.
  If you missed my first story about how I got this wonderful internship, check it
  out here. It’s been quite a journey!

  I’m thankful for the b...'
---

Par Toni Shortsleeve

Aujourd'hui marque le premier jour de mon stage officiel à temps plein avec Outreachy chez LibreHealth. Si vous avez manqué mon premier récit sur la façon dont j'ai obtenu ce merveilleux stage, consultez-le [ici](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e). Cela a été un sacré parcours !

Je suis reconnaissante pour la pause entre l'acceptation et le début effectif du stage. Cela m'a permis de finaliser certains de mes projets précédents, et j'ai passé une partie de mon temps à me préparer pour aujourd'hui. Dans cet article, je vais donner un bref aperçu de ce que j'ai fait — et appris — jusqu'à présent.

### Installation

J'ai fait des recherches sur le flux de travail et les procédures de la pratique clinique grâce aux vidéos YouTube de [LibreHealth](https://www.youtube.com/channel/UC4bKSiSB7196D5W3xGGKxqQ/featured). Comme il y avait deux vidéos qui n'avaient pas encore été transcrites — et qu'elles traitaient des sujets dont je devais mieux comprendre — c'est par là que j'ai commencé.

J'ai travaillé avec le système de dossier médical électronique (DME) de LibreHealth. J'ai créé un patient qui avait besoin d'une orientation pour une radiographie. Ensuite, j'ai créé le laboratoire qui effectuerait la radiographie.

J'ai également créé trois utilisateurs. Il s'agissait de la réceptionniste de l'accueil, de l'infirmière auxiliaire autorisée (IAA) et du transcripteur. Je ne savais même pas qu'il y avait un transcripteur dans le domaine médical, mais maintenant cela a un peu plus de sens.

### Qui peut faire quoi

La réceptionniste de l'accueil, Tina, n'est autorisée à voir que certaines données démographiques des patients. Elle accueille le patient et attribue les salles d'examen disponibles. Dans ce contexte, Tina accompagne le patient à la station de l'infirmière.

À la station de l'infirmière, Dana, l'IAA, prend les constantes vitales du patient. Cela nécessite un formulaire spécifique qui doit être rempli correctement. Ce formulaire est intimidant. Il demandait à la fois des mesures impériales et métriques. Ce fut une agréable surprise de constater que le système calculait automatiquement les mesures métriques pour moi.

Une fois que Dana a terminé le processus de saisie des informations vitales du patient, elle accompagne le patient dans la salle d'examen.

Le médecin était déjà dans le système en tant que fournisseur de soins, donc je n'ai pas eu besoin de créer un profil pour elle.

### Notes et codes

Mais le médecin devait rédiger une note Subjective, Objective, Assessment Plan (SOAP). C'était complexe. Elle devait indiquer ce que le patient a dit, ce que le médecin a observé, ce que le médecin suggère comme problème, et ensuite comment le patient devrait être traité.

Au début, je pensais que « Objective » aurait plus de sens s'il était étiqueté « Observation ». Mais ensuite, j'ai réalisé que cela pourrait signifier que le médecin devrait être un observateur objectif.

Selon mon mentor, ma première tentative était proche — mais j'avais inversé quelques éléments. Une fois que j'allais dans la bonne direction, ma note SOAP mise à jour avait aussi du sens. Une erreur que j'ai faite : je l'ai signée trop tôt. Ensuite, j'ai dû recommencer, car la signature électronique d'une note SOAP la verrouille et je n'étais pas encore prête pour cela.

Ensuite, le médecin devait créer un ordre de procédure — également connu sous le nom d'ordre du fournisseur. Ce formulaire d'ordre indique au personnel ce qui doit être fait pour le patient, comme l'envoi d'échantillons à un laboratoire ou l'orientation vers un spécialiste. Il nécessite également un code de diagnostic.

La [Classification internationale des maladies](https://searchhealthit.techtarget.com/definition/ICD-10) (CIM) 10e révision est le système de catalogage clinique le plus actuel. Je suis retournée sur Google et j'ai trouvé le code CIM10 pour une radiographie d'une entorse au poignet. Il y a beaucoup de sous-codes ! Quelle partie de la main ? S'agit-il de la radiographie initiale ou d'une vue séquentielle ?

J'ai vérifié avec mon mentor à nouveau, et j'ai eu le bon code ! Cela était beaucoup plus difficile que de trouver une simple erreur JavaScript ou de résoudre pourquoi mon code ne s'affichait pas à l'écran. J'apprends quelque chose de nouveau chaque jour !

### Transmission

Marc est le clinicien chargé de transcrire l'ordre de procédure et de l'envoyer au laboratoire.

Son travail est intéressant. Il crée un formulaire de référence basé sur les informations de l'ordre de procédure.

La [Terminologie actuelle des procédures](https://searchhealthit.techtarget.com/definition/Current-Procedural-Terminology-CPT) (CPT) 4e édition est l'ensemble de codes médicaux le plus actuel utilisé pour déclarer les procédures et services médicaux, chirurgicaux et diagnostiques à des fins de facturation médicale.

Marc a ajouté des codes CPT4 basés sur le code CIM10.

Et c'est là que j'ai été bloquée pendant un moment. Une fois de plus, mon mentor est venu à la rescousse pour que je puisse continuer.

Une fois que Marc a soumis et signé électroniquement le formulaire de référence, le patient a pu payer et partir — et espérons-le, programmer cette radiographie.

### Ma documentation

Mon document a été soumis pour révision le 22 mai, la veille du début officiel de mon nouveau stage Outreachy. On m'a donné beaucoup de points à réviser.

J'ai du pain sur la planche. Je vais réviser le document actuel et transcrire l'autre vidéo en fonction des commentaires de ce document.

J'espère qu'en quelques semaines, je pourrai suivre le flux de travail en radiologie. Cela fait partie du système LibreHealth, mais c'est un style et un flux de travail totalement différents de tout ce avec quoi j'ai travaillé auparavant.

### À venir

Je suis si heureuse d'avoir eu le temps d'accomplir autant de choses en préparation pour ce stage. Bien que je n'aie pas tout compris immédiatement, j'apprends beaucoup et j'ai hâte d'en apprendre davantage.

Merci de m'accompagner dans mon parcours Outreachy.