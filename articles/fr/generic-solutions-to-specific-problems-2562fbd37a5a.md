---
title: 'Solutions génériques à des problèmes spécifiques : quand écrire du code et
  quand simplement le faire'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T03:58:37.000Z'
originalURL: https://freecodecamp.org/news/generic-solutions-to-specific-problems-2562fbd37a5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0BIInBkbvWUbf2j1krD2Iw.jpeg
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: 'Solutions génériques à des problèmes spécifiques : quand écrire du code
  et quand simplement le faire'
seo_desc: 'By Rina Artstain

  There is a traditional story that tells of a rabbi who comes upon a guy sitting
  next to a fork in the road. The rabbi asks the guy which way is best to get to the
  city, and the guy answers: That one is a short road which is long, and...'
---

Par Rina Artstain

Il existe une histoire traditionnelle qui raconte qu'un rabbin tombe sur un homme assis à côté d'un embranchement. Le rabbin demande à l'homme quel est le meilleur chemin pour se rendre à la ville, et l'homme répond : Celui-ci est un chemin court qui est long, et l'autre est un chemin long qui est court. Le rabbin choisit le chemin court, mais arrive bientôt dans un champ rempli d'épines qu'il ne peut pas traverser et doit rebrousser chemin et prendre l'autre route, qui le mène finalement à la ville.

La morale de l'histoire, en plus de se demander si cet homme était le premier troll de l'histoire, est que parfois essayer de prendre un raccourci peut finir par être plus long que de simplement faire le détour.

### Coder le long chemin (qui est court)

Si vous écrivez spécifiquement une API ou une bibliothèque pour un usage interne ou externe, vous savez qu'elle doit être aussi générique que possible. Vous voulez qu'elle soit claire, concise et facile à utiliser, tout en offrant à vos utilisateurs beaucoup de flexibilité. Il y a des compromis entre ces objectifs, mais vous les trouverez.

Mais que se passe-t-il lorsque vous recevez une tâche spécifique à accomplir, et que vous pouvez soit simplement la faire, soit écrire une infrastructure qui rendra la tâche plus facile à l'avenir ?

Devez-vous accomplir la tâche le plus rapidement possible ou passer du temps à construire une infrastructure qui rendra les tâches futures plus faciles à accomplir ?

Devez-vous choisir le chemin court qui pourrait s'avérer long, ou le chemin long qui vous aidera en réalité à atteindre votre cible plus rapidement ?

### Un exemple (basé sur une histoire vraie)

(Certains détails ont été modifiés ou omis pour simplifier, et, eh bien, pour une meilleure narration. La réalité est beaucoup trop désordonnée.)

Un jour, mon patron vient me voir et me demande de récupérer rapidement des données de la base de données et de les lui envoyer sous forme de feuille Excel. Ce n'était pas trop compliqué, alors je l'ai fait tout de suite.

Le lendemain, il me demande les mêmes données, mais avec des dates différentes. Il réfléchit un peu et dit, eh bien — peut-être devrais-tu simplement mettre ce rapport en ligne. J'aimerais pouvoir accéder à ces données à tout moment et choisir les dates moi-même.

Pas de problème ! Voici, un peu de front-end, un peu de back-end, déploiement. Attendez. Attendez. Attendez. Déploiement terminé, et le rapport est en ligne.

Quelques jours passent, et on me demande un autre rapport rapide, et « fais-le avec cette belle interface et ces filtres de date que tu nous as donnés la dernière fois ». OK, bien sûr. Pas de problème. Front-end, back-end, déploiement, attendez, en ligne.

La fois suivante, j'ai reçu une demande similaire et j'ai dit : « Écoute, il me faudra une demi-journée pour écrire ce rapport, mais si tu me donnes deux jours, je peux construire une infrastructure qui me permettra de définir une requête dans la base de données, ajouter une configuration, et ton rapport sera en ligne sans avoir à attendre le déploiement ». Ma demande a été approuvée.

#### **Voici ce que j'ai fait avec mes deux jours :**

J'ai défini une convention pour une procédure stockée « rapport », qui devait recevoir les paramètres suivants :

* Date de début
* Date de fin
* Index de départ (pour la pagination)

Chaque procédure retournait un ensemble de résultats pour la requête, et le nombre total de résultats (pour la pagination).

En outre, j'ai ajouté une table Reports qui contenait :

* Nom de la procédure stockée (à exécuter)
* Titre (du rapport)
* Description (à afficher sur la page du rapport)

J'ai également ajouté un endpoint sur le serveur, une UI, et une logique pour :

* Vérifier la base de données pour les rapports et les ajouter à la navigation du site.
* Lorsque qu'un rapport était consulté, exécuter la procédure stockée correspondante et retourner le résultat à l'UI.
* Afficher deux sélecteurs de date pour choisir la Date de début et la Date de fin et exécuter la requête.
* Un tableau générique pour afficher les résultats formatés selon le type de données de chaque colonne. (J'avais déjà un composant UI générique pour la pagination, youpi !)

Lorsque j'ai terminé, je pouvais ajouter une procédure stockée et une entrée dans la base de données et le rapport apparaissait automatiquement sur notre site.

### La seule constante est le changement

Tout le monde était heureux et super excité par ma fonctionnalité de rapport économisant du temps, mais… Qu'en est-il du tri ? Et pourrait-on avoir la première colonne liée au profil du client ? Et pourrait-on peut-être ajouter un filtrage par le représentant commercial responsable de ce client ?

Oui ! Bien sûr. Cela a beaucoup de sens. J'ai donc ajouté :

* Des paramètres facultatifs Tri par et Direction de tri aux procédures stockées.
* Un indicateur pour spécifier si la première colonne doit être liée au profil du client.
* Un autre indicateur pour spécifier si la requête incluait un filtrage par représentant commercial.
* Et quelques modifications de l'UI/logique pour prendre en charge l'affichage/l'exécution de ces nouvelles exigences.

Heureux, heureux, joie, joie. Mais… Comment regrouper les résultats ? Et lorsque vous cliquez sur la ligne, pourrait-on envoyer un e-mail à un groupe d'utilisateurs prédéfinis ? Et lorsque qu'un représentant commercial entre dans le rapport, pourrait-on afficher le rapport dans sa couleur préférée ? (OK, j'ai inventé ce dernier.)

#### Retenez vos chevaux

À ce stade, j'ai dû m'arrêter et réfléchir aux fonctionnalités qui devaient être implémentées dans le cadre de ma solution générique, et à celles qui devaient être développées comme une solution autonome.

Il était évident pour moi que des actions personnalisées spécifiques qui ne dépendent pas des données réelles retournées par la requête (comme l'envoi d'un e-mail à certains utilisateurs prédéfinis) étaient hors de question.

Je pensais également que des actions peu courantes qui dépendent des données retournées par la requête ne devaient pas être ajoutées à l'infrastructure de rapport générique. Donc, filtrer par représentant commercial — bien sûr, pourquoi pas. Lien vers le client — OK, scénario courant. Mais d'autres actions très spécifiques à un seul rapport — non.

L'exigence de regroupement posait un défi plus important : le regroupement est un scénario courant et extrêmement utile. Devais-je l'ajouter à mon infrastructure ou non ?

Eh bien, que nécessiterait le regroupement des résultats ?

* Ajouter un indicateur Group By à l'entrée de la base de données du rapport, pour informer la logique de s'attendre à deux ensembles de résultats distincts — en-tête de groupe et détails du groupe.
* La logique devrait également savoir comment associer le groupe aux détails, et cela devrait être fait par convention. Extrêmement risqué.
* Trouver comment trier génériquement les résultats avec un en-tête de groupe. Je ne peux même pas.
* Et probablement quelques autres problèmes auxquels je n'ai pas pensé.

### Le code non écrit

Je n'ai pas ajouté le regroupement.

En rétrospective, avoir mis environ une semaine d'effort au total dans cette fonctionnalité de rapports m'a fait économiser des centaines d'heures de développement de rapports plus tard. J'ai également réussi à éviter le piège d'essayer d'être trop générique et de supporter trop de **choses** superflues, ce qui aurait nui à la stabilité du système à long terme.

Mais vraiment, je n'aurais pas dû écrire une seule ligne de code. J'aurais dû chercher un outil de reporting.

Cependant, il existe d'autres systèmes d'assistance génériques que j'ai écrits et qui étaient un bon investissement et **auraient dû** être écrits. Par exemple, une bibliothèque d'assistants qui créent des éléments HTML avec des identifiants et des classes prévisibles adaptés à nos modèles de données et aux exigences de l'UI.

### Et maintenant ?

Alors, comment décider si vous devez écrire une infrastructure ou simplement le faire ? Voici comment je décide :

* Est-ce une tâche routinière ? Si c'est ennuyeux et récurrent, si vous vous surprenez à copier-coller beaucoup de code souvent — vérifiez si vous pouvez généraliser ce que vous faites et construire du code pour le faire pour vous.
* Combien de temps prendra la construction de l'infrastructure ? Si vous pouvez construire l'infrastructure en 5 minutes et que chaque tâche aurait pris 5 jours, la réponse est facile. Si la construction de l'infrastructure prendrait un an et que chaque tâche prendrait 5 minutes — ne la construisez pas. Mais ce n'est généralement pas aussi clair. Essayez d'estimer au mieux, essayez de garder cela simple, et soyez prêt à couper vos pertes si cela prend trop de temps.
* N'ajoutez pas d'implémentations spécifiques à votre solution générique. Si cela ne convient pas, n'essayez pas de forcer. Vous finirez par ruiner votre infrastructure et obtiendrez un résultat médiocre pour la tâche que vous essayiez réellement d'accomplir.
* Mais d'abord, **s'il vous plaît** vérifiez s'il existe une solution prête à l'emploi pour votre problème.

Vous avez aimé ce que vous avez lu ? Partagez l'amour en applaudissant. Vous avez une question ou un commentaire ? Faites-le moi savoir dans la section des commentaires.