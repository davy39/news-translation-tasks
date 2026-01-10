---
title: Pourquoi je n'utilise pas votre dépôt GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-17T16:25:39.000Z'
originalURL: https://freecodecamp.org/news/why-im-not-using-your-github-repository-2dff6c7ac7cf
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OqUuHr4YvJjeGWDn
tags:
- name: GitHub
  slug: github
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Pourquoi je n'utilise pas votre dépôt GitHub
seo_desc: 'By Sam Westreich, PhD

  As a bioinformatician, I reside in an interesting middle ground between developers
  and end users. My background training is in biology, not computer science.

  But in recent years, biology has moved closer to computer science. Man...'
---

Par Sam Westreich, PhD

En tant que bioinformaticien, je réside dans un terrain intermédiaire intéressant entre les développeurs et les utilisateurs finaux. Ma formation de base est en biologie, et non en informatique.

Mais ces dernières années, la biologie s'est rapprochée de l'informatique. De nombreux types de données biologiques sont trop volumineux pour être analysés manuellement et doivent être traités à l'aide d'ordinateurs. La diminution constante du coût du séquençage du génome a introduit d'énormes quantités de données de séquence. Toutes ces données doivent être assemblées, comparées, recherchées et annotées.

De plus en plus, les biologistes ont besoin d'ordinateurs.

Plus précisément, les biologistes ont besoin de programmes informatiques. Écoutez, si j'ai un tas de données de séquence d'un microbiome que je veux associer aux différentes espèces d'origine, je ne vais pas m'asseoir et construire mon propre outil d'alignement à partir de zéro. Je vais prendre un outil prêt à l'emploi qui a déjà été utilisé, prier pour qu'il soit assez simple à installer, et l'utiliser.

À l'école doctorale, j'ai fait une erreur. J'ai laissé le rythme rapide du monde informatique me séduire. « Plus d'expériences de plusieurs semaines au banc de laboratoire ! » me suis-je déclaré. « Je vais plonger tête la première dans le côté informatique de la biologie et devenir un pont entre les deux mondes — un _bioinformaticien_ ! »

En théorie, un bioinformaticien analyse les données recueillies par les biologistes, découvre de nouvelles conclusions et établit de nouvelles connexions.

En pratique, un bioinformaticien installe beaucoup de programmes et maudit les développeurs qui les ont créés.

J'ai abandonné de nombreux programmes — certains, je suppose, sont de très bons programmes — à cause d'instructions absurdes, de mauvais code ou d'une documentation horrible.

C'est arrivé au point où je peux jeter un coup d'œil à un dépôt GitHub et avoir une bonne idée de ce que je vais penser de votre outil.

Certains dépôts inspirent confiance. D'autres me remplissent de crainte.

Parfois, j'en trouve un si mauvais que je refuse même d'essayer d'installer l'outil (sauf si mon patron l'exige).

Voici les plus gros problèmes que je vois, et comment les éviter.

### Raison 1 : Aucune documentation

![Image](https://cdn-media-1.freecodecamp.org/images/1zjiS85MIpXdcMtpIlG0S-y71a8qsl74iaFH)
_Personne ne sait comment utiliser votre programme à moins que vous ne l'écriviez pour eux. Photo par [Beatriz Pérez Moya](https://unsplash.com/@beatriz_perez?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

J'ai vu toutes les variations de documentation :

* Documentation écrite dans le Readme.
* Un « guide rapide » dans le Readme, avec des informations détaillées dans un PDF ou un document Word séparé.
* Un lien vers un wiki GitHub.
* Un lien vers un site externe, avec la documentation écrite là-bas.
* Un lien vers un site externe, où il y a un autre lien pour télécharger un PDF. (Pourquoi ne pas simplement mettre le PDF dans le dépôt ?)
* Le pire de tout… **aucune documentation.**

Oui, je sais que écrire de la documentation est horrible. J'ai construit des pipelines et des outils, et je me suis forcé à écrire de la documentation. J'ai oublié des cas particuliers et les détails des commandes, et j'ai parfois reçu des rappels embarrassants de la part des utilisateurs.

Si vous construisez un outil et le rendez public, votre documentation doit inclure, au minimum :

1. Les exigences et dépendances pour utiliser votre outil. Cela inclut à la fois les exigences matérielles (RAM et taille du disque) et les exigences logicielles (système d'exploitation, autres programmes).
2. Comment installer votre outil.
3. Ce que fait votre outil.
4. Comment faire fonctionner votre outil, avec des exemples de commandes.

Je recommande également fortement d'inclure :

1. Une section « questions fréquemment posées ».
2. Des tests — cela inclut des données de test et les commandes exactes qui doivent être utilisées sur ces données de test (au niveau où les commandes doivent être copiées/collées sur la ligne de commande).
3. Des exemples de sortie.
4. Une licence.
5. Des captures d'écran, si applicable.
6. Des remerciements, si vous êtes ouvert aux pull requests, et des informations de contact, afin que les utilisateurs puissent signaler des problèmes.

Une mauvaise ou incomplète documentation est la raison numéro un pour laquelle j'arrête d'utiliser un outil. Vous savez comment fonctionne votre outil, mais personne d'autre ne le sait — ne forcez pas les gens à le découvrir. Donnez des instructions claires et faciles.

### Raison 2 : L'enfer des dépendances

![Image](https://cdn-media-1.freecodecamp.org/images/FDURQPsceanAj4o0NmU9zlxk3jSqxqlwirie)
« Chacun de ceux-ci est une dépendance. Assurez-vous de les déballer tous dans le bon ordre ! » Photo par [chuttersnap](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

J'ai déjà trouvé un outil (un pipeline pour l'annotation de séquences d'ADN) qui avait six dépendances.

« Ce n'est pas le pire », me suis-je dit. « Je peux gérer l'installation de six dépendances pour utiliser cet outil. »

Malheureusement, la plupart de ces dépendances avaient d'autres dépendances. Et celles-ci en avaient encore plus, y compris certaines qui refusaient de bien fonctionner ensemble.

Au moment où j'ai abandonné cet outil d'origine, j'avais rencontré dix-neuf dépendances différentes que je devrais installer, spécifiquement pour utiliser ce seul pipeline. _Dix-neuf !_

C'est génial qu'il y ait beaucoup d'outils utiles qui peuvent servir de blocs de construction pour des programmes plus complexes. Il est beaucoup mieux d'utiliser une dépendance déjà existante et reconnue que de réinventer la roue et de tout faire soi-même.

Mais si vous prenez cette voie, trouvez un moyen plus facile pour moi d'installer les dépendances de votre outil.

Donnez-moi un script d'installation que je peux exécuter pour obtenir toutes les dépendances — cela fonctionne particulièrement bien si j'ai besoin d'une demi-douzaine de packages Python ou R. Si possible, donnez-moi une archive de la dépendance, afin que je n'aie pas à aller la chercher (en supposant que la licence de la dépendance permette ce niveau de redistribution).

Ne me piégez pas dans l'enfer des dépendances — ou si vous le faites, soyez prêt à voir de nombreux utilisateurs abandonner l'utilisation de votre programme. Personne ne veut passer du temps en enfer.

### Raison 3 : Problèmes d'abandon

![Image](https://cdn-media-1.freecodecamp.org/images/KhyADvIhU0dygAeG6bMFeH4ECrYEia3ciQ8v)
« Personne n'a fait de mises à jour sur ce dépôt depuis longtemps. » Photo par [Nathan Wright](https://unsplash.com/@cozmicphotos?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")._

Quand un projet GitHub est nouveau et frais, il n'y a pas de problèmes. Il est nouveau, il est propre, et personne n'a encore rencontré de bugs.

Au cours des semaines ou mois suivants, alors que les utilisateurs découvrent le programme et le testent, ils signaleront des problèmes. Heureusement, GitHub dispose d'une page sur chaque dépôt dédiée à la journalisation de ces problèmes. Elle s'appelle « Issues ».

Ici, sur cette page, les utilisateurs commentent qu'ils obtiennent un message d'erreur lorsqu'ils tentent diverses tâches. Parfois, il s'agit d'une dépendance obsolète. Parfois, il s'agit d'une faute de frappe dans le code. Parfois, il s'agit d'une erreur de l'utilisateur — ils ont la mauvaise version d'un autre outil, leurs entrées sont dans le mauvais format, ou ils utilisent des options illégales et ne lisent pas les messages d'aide.

En surface, c'est une fonctionnalité géniale. Mais cette page Issues peut aussi être un avertissement — ou un élément dissuasif.

Une page Issues peut lever l'un des deux drapeaux rouges — ou un drapeau vert :

* Drapeau rouge 1 : Il n'y a pas de problèmes. Il n'y a jamais eu de problèmes. **Personne n'a jamais utilisé cet outil, et il est abandonné et prend la poussière.**
* Drapeau rouge 2 : Il y a plusieurs problèmes ouverts, principalement sur des erreurs, sans résolution de la part du propriétaire du dépôt. **Cet outil est abandonné et cassé et le propriétaire s'en moque.**
* Drapeau vert : Il y a très peu de problèmes ouverts, dont la plupart sont étiquetés comme des améliorations — mais beaucoup de problèmes fermés. **Le propriétaire corrige activement les erreurs, aide les utilisateurs et prévoit d'ajouter plus de fonctionnalités.**

Parce que j'ai publié des programmes sur GitHub, je sais que les maintenir n'est pas amusant. C'est amusant de créer quelque chose de nouveau. Ce n'est pas amusant de dépanner des messages d'erreur étranges et des cas d'utilisation obscurs. Ce n'est pas amusant de revenir sur des pages de vieux code et de comprendre pourquoi une condition super-spécifique conduit à un échec.

Mais les meilleurs programmes (et les dépôts GitHub les plus fiables) proviennent de créateurs qui sont prêts à faire le travail ennuyeux et fastidieux. Cela inclut la correction des problèmes et la fourniture de support aux utilisateurs.

Et si d'autres questions sont répondues, je me sens plus confiant que mes propres problèmes seront abordés, et je pourrai utiliser l'outil en toute confiance pour mes propres besoins.

### Vendez-moi votre programme

![Image](https://cdn-media-1.freecodecamp.org/images/8EDMTIs25bBgemnT6mDTYz25kR-hn81Wk3yP)

Que cela vous plaise ou non, votre dépôt GitHub est souvent la « vitrine » de votre programme. Votre dépôt doit vendre votre programme comme facile à installer, facile à exécuter et facile à comprendre.

Un excellent dépôt GitHub est une belle chose. En tant qu'utilisateur semi-qualifié, j'adore quand un fichier readme me dit exactement quelles commandes installer l'outil, comment l'utiliser et comment dépanner les problèmes les plus courants. Un manuel détaillé et simple met un sourire sur mon visage. Un script d'installation des dépendances en une seule étape me fait soupirer de soulagement. Les indications que vous supportez votre outil et corrigez les bugs remplissent ma poitrine de confiance.

Laissez-moi utiliser votre outil.

Laissez-moi citer votre travail et chanter vos louanges à mes collègues.

Laissez-moi vous respecter et le grand programme que vous avez construit.

Évitez ces problèmes — et évitez ces erreurs dans votre prochain dépôt GitHub public.

_Sam Westreich est un scientifique du microbiome travaillant dans la Silicon Valley, et a passé des années à s'immerger dans la science et les poursuites les plus nerds. Il blogue sur la science, la biologie, les microbes et les microbiomes, et ses réflexions sur l'école doctorale et la recherche du succès._