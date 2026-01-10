---
title: Ce que j'ai appris en analysant plus de 80 refus d'emploi avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T17:49:55.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-analyzing-more-than-80-job-rejections-with-python-11044ee6927b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ux_ov2BCOxHApB3e1DBt2Q.png
tags:
- name: Data Science
  slug: data-science
- name: jobs
  slug: jobs
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Ce que j'ai appris en analysant plus de 80 refus d'emploi avec Python
seo_desc: 'By Conor Dewey

  We’ve all gotten those emails at one point or another. You know, the ones that start
  with “Thank you for your interest” and end with shattered dreams and self-doubt.
  Okay, maybe that’s a bit extreme. Nonetheless, getting job rejections...'
---

Par Conor Dewey

Nous avons tous reçu ces e-mails à un moment ou à un autre. Vous savez, ceux qui commencent par « Merci pour votre intérêt » et se terminent par des rêves brisés et des doutes sur soi-même. D'accord, peut-être que c'est un peu exagéré. Néanmoins, recevoir des refus d'emploi peut être difficile.

Croyez-moi, je sais. J'ai reçu plus de 80 e-mails de refus d'emploi explicites au cours de l'année dernière en postulant pour des stages. Examinons [mon expérience](https://github.com/conordewey3/DS-Career-Resources) en chiffres pour fournir un peu de contexte avant de plonger dans les données.

* Candidatures : 234
* Réponses : 93
* Refus : 90
* Offres : 3

Il est utile de souligner que, au moins pour les stages, ne recevoir aucune réponse du tout n'est pas rare. En fait, plus de 60 % des candidatures que j'ai remplies n'ont vu aucune réponse. À bien des égards, cela peut causer encore plus d'anxiété que de recevoir un « non » clair et net. Au moins dans ce cas, vous pouvez continuer votre recherche au lieu de vous concentrer sur une cause perdue.

Comme vous pouvez l'imaginer, après avoir entendu « non » 80 fois, vous développez une sorte de résistance à cela. Cette résistance, couplée à un peu de curiosité, est ce qui a finalement déclenché l'idée de ce projet. En bref, je voulais enquêter sur ce qui faisait fonctionner ces e-mails de refus automatisés et comment ils différaient entre les entreprises. Si vous voulez passer directement au code lui-même, n'hésitez pas à vous rendre sur le [dépôt GitHub](https://github.com/conordewey3/Job-Rejection-Analysis) et à vous y atteler.

**Tout au long du reste de cet article, je vais expliquer comment j'ai extrait les e-mails de refus. Ensuite, je répondrai à quelques questions intéressantes concernant le timing et le contenu de ces e-mails.**

![Image](https://cdn-media-1.freecodecamp.org/images/yL8CxM6pQ7p8Rll7JNTycja8mhNwLJk4dZwb)

![Image](https://cdn-media-1.freecodecamp.org/images/HPr5bUL5vWLq9g6rYNEWbI3b4fvr0nKTxl3s)
_Tout arrive pour une raison, n'est-ce pas ?_

### Collecte de données

D'abord, obtenons les données. Après avoir interrogé ma boîte de réception Gmail, j'ai trouvé plus de 1 000 e-mails contenant les mots « stage » et « candidature ». Cela a rendu les choses un peu délicates du point de vue de l'automatisation.

J'ai trié les refus d'emploi par entreprise. J'ai fourni à chacun une étiquette « Refus d'emploi » dans Gmail. Une fois cela fait, il était temps de tirer parti de la puissance de Python. J'ai pu me connecter avec `imaplib` et extraire des parties spécifiques des e-mails avec le package `email`. Pour l'analyse de contenu, j'ai dû tokeniser le texte avec `nltk`, et supprimer toute ponctuation et mots vides pour l'analyse.

### Mots et phrases courants

Vous êtes-vous déjà dit que ces e-mails semblent tous utiliser le même langage général ? Personnellement, j'ai remarqué beaucoup des mêmes phrases et lignes utilisées d'une entreprise à l'autre. Cela ne signifie pas qu'il n'y a pas quelques tentatives créatives pour adoucir le coup, mais elles sont définitivement rares.

![Image](https://cdn-media-1.freecodecamp.org/images/NmdkH6IZPYQxSha-hss4eFo19KGwZJCqRtmh)
_Un peu d'optimisme va loin, merci AT&T_

Examinons les mots et phrases les plus courants utilisés dans les lignes d'objet de ces e-mails. Vous savez, pour que vous puissiez, au moins, voir cela venir.

![Image](https://cdn-media-1.freecodecamp.org/images/omf6WkUYUdKXfYoxSfLONbJoAEoK9j4v1oPn)

Comme vous pouvez le voir ci-dessus, les choix de mots populaires incluent « candidature » et « votre » parmi d'autres. En jetant un coup d'œil à cela, vous pouvez probablement reconstituer les en-têtes de sujet les plus probables sans trop d'effort :

* Merci pour votre intérêt.
* Mise à jour de votre candidature [Insérer le rôle].

Il semble y avoir de petites variations de ces mêmes lignes d'objet éprouvées, mais ces mots servent souvent de premiers messagers de mauvaises nouvelles.

### Modèles temporels

Allons plus loin et regardons comment le timing de ces e-mails se décompose. Cela m'a rappelé le vieux conseil de ne jamais licencier quelqu'un un vendredi, puisque ils ne peuvent pas vraiment prendre de mesures vers un nouvel emploi pendant le week-end. Bien que ce ne soit pas aussi grave que de laisser quelqu'un partir, il est toujours fascinant de penser aux processus de réflexion utilisés lorsque les entreprises choisissent de délivrer les mauvaises nouvelles.

Suivons cette idée et regardons la répartition des jours de la semaine pour les e-mails de refus. Je vais plonger dans la répartition de l'heure de la journée ensuite.

![Image](https://cdn-media-1.freecodecamp.org/images/zPiBcFgH9gvbudyO0cNq4p291TkUkktPzP69)

Il semble que le « jour du pigeon » soit le clair vainqueur ici. Jeudi arrive en deuxième position, avec le reste des jours de la semaine semblant assez cohérents. Les week-ends semblent être une navigation tranquille pour la plupart, à part quelques anomalies notables qui ont été envoyées le samedi. Dommage...

![Image](https://cdn-media-1.freecodecamp.org/images/KqWxUcKLONzjcRC65edwX4Qj5eSXhMw77MNu)

Pour l'heure de la journée, cela ressemble à la distribution normale à laquelle nous nous attendrions. Il semble y avoir des pics dans les comptes de refus à 9h et à midi. Ces heures signalent le début de la journée de travail pour les fuseaux horaires EST et PST, respectivement. Un seul refus est arrivé après 17h PST (heure 20). Je vous regarde, P&G.

Cela conclut la partie analyse de l'article. Une fois de plus, vous pouvez consulter le code et l'analyse originale sur [GitHub](https://github.com/conordewey3/Job-Rejection-Analysis) ou dans le gist lié ci-dessous.

### Mots de la fin

J'ai trouvé ce projet être une exploration amusante des e-mails de refus d'emploi. Plus que cela, je l'ai trouvé être une réflexion utile sur [ma recherche d'emploi](https://github.com/conordewey3/DS-Career-Resources) et sur la gestion du refus en général. Pas assez de gens valorisent la capacité à gérer l'échec comme une compétence pratique ou même une [super puissance](https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection) à certains égards.

> « J'ai échoué encore et encore dans ma vie... et c'est pourquoi je réussis » — Michael Jordan

Après 80 refus explicites, vous commencez à vous habituer à la notion d'échec. J'ai trouvé que je devenais de moins en moins hésitant à postuler pour des postes dans des entreprises prestigieuses ou à envoyer des e-mails à froid aux recruteurs. Cela m'a permis d'obtenir des opportunités que je ne pensais pas initialement à ma portée.

Si vous lisez ceci, prenez ces chances, allez un peu plus loin, sortez et échouez. Relevez-vous. Ensuite, échouez encore. C'est seulement à travers ce processus que l'amélioration et, finalement, le succès peuvent être atteints. Et lorsque vous atteignez ce prochain succès, n'oubliez pas de regarder en arrière tous les échecs qui vous ont mené là et de dire une chose :

> _Merci pour votre intérêt._

Merci d'avoir lu ! Si vous avez aimé l'article, n'hésitez pas à montrer un peu d'amour au bouton d'applaudissements et à consulter quelques-uns de mes articles connexes ci-dessous :

* [Déconstruire les métriques sur Medium](https://towardsdatascience.com/deconstructing-metrics-on-medium-bf5b4863bf96?source=friends_link&sk=8bd7eb3ae6d762eccb2111788c7a8933)
* [La grande liste des ressources d'entretien DS/ML](https://towardsdatascience.com/the-big-list-of-ds-ml-interview-resources-2db4f651bd63?source=friends_link&sk=e229d4fc3452514bd8d560ae898809cc)
* [Python pour la Data Science : 8 concepts que vous avez peut-être oubliés](https://towardsdatascience.com/python-for-data-science-8-concepts-you-may-have-forgotten-i-did-825966908393?source=friends_link&sk=f8daac7acb936a5a7eaa65e80cfda01f)

Si vous êtes intéressé par plus d'articles à venir, assurez-vous de [me suivre](https://medium.com/@conordewey3) et de vous abonner à [ma newsletter](https://www.conordewey.com/newsletter/) ci-dessous pour recevoir tout nouveau contenu. Pour en savoir plus sur moi et ce que je fais, consultez [mon site web](https://www.conordewey.com/).