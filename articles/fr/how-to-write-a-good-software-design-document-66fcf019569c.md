---
title: Comment rédiger un bon document de conception logicielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-13T15:06:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-good-software-design-document-66fcf019569c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vy3gDPKB1kyhzIqI8DNUvQ.png
tags:
- name: Design
  slug: design
- name: engineering
  slug: engineering
- name: project management
  slug: project-management
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment rédiger un bon document de conception logicielle
seo_desc: 'By Angela Zhang

  As a software engineer, I spend a lot of time reading and writing design documents.
  After having gone through hundreds of these docs, I’ve seen first hand a strong
  correlation between good design docs and the ultimate success of the p...'
---

Par Angela Zhang

En tant qu'ingénieure logicielle, je passe beaucoup de temps à lire et à écrire des documents de conception. Après avoir parcouru des centaines de ces documents, j'ai vu de première main une forte corrélation entre les bons documents de conception et le succès ultime du projet.

Cet article est ma tentative de décrire **ce qui rend un document de conception excellent**.

L'article est divisé en 4 sections :

* **Pourquoi** rédiger un document de conception
* **Que** inclure dans un document de conception
* **Comment** le rédiger
* Le **processus** qui l'entoure

### Pourquoi rédiger un document de conception ?

Un document de conception — également connu sous le nom de spécification technique — est une description de la manière dont vous prévoyez résoudre un problème.

Il existe déjà [de nombreux écrits](https://www.joelonsoftware.com/2000/10/02/painless-functional-specifications-part-1-why-bother/) sur l'importance de rédiger un document de conception avant de se lancer dans le codage. Donc, tout ce que je dirai ici est :

**Un document de conception est l'outil le plus utile pour s'assurer que le bon travail est fait.**

L'objectif principal d'un document de conception est de vous rendre plus efficace en vous obligeant à réfléchir à la conception et à recueillir les commentaires des autres. Les gens pensent souvent que le but d'un document de conception est d'enseigner aux autres un système ou de servir de documentation plus tard. Bien que ces effets secondaires puissent être bénéfiques, ils ne sont **pas** le but en soi.

En règle générale, si vous travaillez sur un projet qui pourrait prendre 1 mois-ingénieur ou plus, vous devriez rédiger un document de conception. Mais ne vous arrêtez pas là — beaucoup de petits projets pourraient bénéficier d'un mini document de conception également.

Super ! Si vous lisez toujours, vous croyez en l'importance des documents de conception. Cependant, différentes équipes d'ingénierie, et même des ingénieurs au sein de la même équipe, rédigent souvent des documents de conception très différemment. Alors parlons du contenu, du style et du processus d'un bon document de conception.

![Image](https://cdn-media-1.freecodecamp.org/images/gj8fgseDg1J1gal9FQHJFTkKAMMGZN8XznjK)
_Photo par [Unsplash](https://unsplash.com/photos/x5SRhkFajrA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Todd Quackenbush</a> sur <a href="https://unsplash.com/search/photos/ingredients?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Que inclure dans un document de conception ?

Un document de conception décrit la solution à un problème. Puisque la nature de chaque problème est différente, vous voudrez naturellement structurer votre document de conception différemment.

Pour commencer, voici une liste de sections que vous devriez au moins **envisager** d'inclure dans votre prochain document de conception :

#### **Titre et Personnes**

Le titre de votre document de conception, les auteur(s) (devrait être la même liste que les personnes prévues pour travailler sur ce projet), les relecteur(s) du document (nous en parlerons plus dans la section Processus ci-dessous), et la date de la dernière mise à jour de ce document.

#### **Aperçu**

Un résumé de haut niveau que chaque ingénieur de l'entreprise devrait comprendre et utiliser pour décider s'il est utile pour eux de lire le reste du document. Il devrait faire 3 paragraphes maximum.

#### **Contexte**

Une description du problème en question, pourquoi ce projet est nécessaire, ce que les gens doivent savoir pour évaluer ce projet, et comment il s'intègre dans la stratégie technique, la stratégie produit, ou les objectifs trimestriels de l'équipe.

#### **Objectifs et Non-Objectifs**

La section Objectifs devrait :

* décrire l'impact piloté par l'utilisateur de votre projet — où votre utilisateur pourrait être une autre équipe d'ingénierie ou même un autre système technique
* spécifier comment mesurer le succès en utilisant des métriques — points bonus si vous pouvez lier à un tableau de bord qui suit ces métriques

Les Non-Objectifs sont tout aussi importants à décrire quels problèmes vous **ne** corrigerez **pas** afin que tout le monde soit sur la même longueur d'onde.

#### **Jalons**

Une liste de points de contrôle mesurables, afin que votre chef de produit et le manager de votre manager puissent le parcourir et savoir approximativement quand différentes parties du projet seront terminées. Je vous encourage à diviser le projet en jalons majeurs orientés utilisateur si le projet dure plus d'1 mois.

Utilisez des dates de calendrier afin de prendre en compte les retards sans rapport, les vacances, les réunions, etc. Cela devrait ressembler à quelque chose comme ceci :

`Date de début : 7 juin 2018`  
`Jalon 1 — Nouveau système MVP en mode sombre : 28 juin 2018`  
`Jalon 2 - Retrait de l'ancien système : 4 juillet 2018`  
`Date de fin : Ajout des fonctionnalités X, Y, Z au nouveau système : 14 juillet 2018`

Ajoutez une sous-section `[Mise à jour]` ici si l'ETA de certains de ces jalons change, afin que les parties prenantes puissent facilement voir les estimations les plus récentes.

#### **Solution Existante**

En plus de décrire l'implémentation actuelle, vous devriez également parcourir un exemple de flux de haut niveau pour illustrer comment les utilisateurs interagissent avec ce système et/ou comment les données circulent à travers lui.

Une **histoire d'utilisateur** est un excellent moyen de cadrer cela. Gardez à l'esprit que votre système peut avoir différents types d'utilisateurs avec différents cas d'utilisation.

#### **Solution Proposée**

Certaines personnes appellent cela la section **Architecture Technique**. Encore une fois, essayez de parcourir une histoire d'utilisateur pour concrétiser cela. N'hésitez pas à inclure de nombreuses sous-sections et diagrammes.

Fournissez d'abord une vue d'ensemble, puis remplissez **beaucoup** de détails. Visez un monde où vous pouvez écrire cela, puis prendre des vacances sur une île déserte, et un autre ingénieur de l'équipe peut simplement le lire et implémenter la solution comme vous l'avez décrite.

#### **Solutions Alternatives**

Quoi d'autre avez-vous considéré en élaborant la solution ci-dessus ? Quels sont les avantages et les inconvénients des alternatives ? Avez-vous considéré l'achat d'une solution tierce — ou l'utilisation d'une solution open source — qui résout ce problème plutôt que de construire la vôtre ?

#### **Testabilité, Surveillance et Alertes**

J'aime inclure cette section, car les gens traitent souvent cela comme une réflexion après coup ou l'ignorent complètement, et cela revient presque toujours les hanter plus tard lorsque les choses se cassent et qu'ils n'ont aucune idée de comment ou pourquoi.

#### **Impact Transverse**

Comment cela augmentera-t-il la charge de l'équipe de garde et des dev-ops ?   
Combien cela coûtera-t-il ?   
Cela cause-t-il une régression de latence dans le système ?   
Cela expose-t-il des vulnérabilités de sécurité ?   
Quelles sont certaines conséquences négatives et effets secondaires ?   
Comment l'équipe de support pourrait-elle communiquer cela aux clients ?

#### **Questions Ouvertes**

Toutes les questions ouvertes dont vous n'êtes pas sûr, les décisions contentieuses sur lesquelles vous aimeriez que les lecteurs se prononcent, les travaux futurs suggérés, etc. Un nom ironique pour cette section est les "inconnues connues".

#### **Planification Détaillée et Calendrier**

Cette section sera principalement lue par les ingénieurs travaillant sur ce projet, leurs responsables techniques et leurs managers. Par conséquent, cette section se trouve à la fin du document.

Essentiellement, il s'agit de la ventilation de la manière et du moment où vous prévoyez d'exécuter chaque partie du projet. Il y a beaucoup de choses qui entrent en jeu pour une planification précise, donc vous pouvez lire [cet article](https://medium.freecodecamp.org/how-to-effectively-scope-your-software-projects-from-planning-to-execution-e96cbcac54b9) pour en savoir plus sur la planification.

J'ai tendance à traiter également cette section du document de conception comme un suivi des tâches du projet en cours, donc je la mets à jour chaque fois que mon estimation de planification change. Mais c'est plus une préférence personnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/sGfVXpLpPjAP4aeejy0Sul3KviBKiX6kojUO)
_Photo par [Unsplash](https://unsplash.com/photos/EF8Jr-uPS2Y?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/writing?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Comment le rédiger

Maintenant que nous avons parlé de **ce** qui fait un bon document de conception, parlons du style de rédaction. Je promets que cela est différent de votre cours d'anglais au lycée.

#### **Écrivez aussi simplement que possible**

N'essayez pas d'écrire comme les articles académiques que vous avez lus. Ils sont écrits pour impressionner les relecteurs de revues. Votre document est écrit pour décrire votre solution et obtenir des commentaires de vos coéquipiers. Vous pouvez atteindre la clarté en utilisant :

* Des mots simples
* Des phrases courtes
* Des listes à puces et/ou des listes numérotées
* Des exemples concrets, comme "L'utilisateur Alice connecte son compte bancaire, puis…"

#### **Ajoutez beaucoup de graphiques et de diagrammes**

Les graphiques peuvent souvent être utiles pour comparer plusieurs options potentielles, et les diagrammes sont généralement plus faciles à analyser que le texte. J'ai eu de la chance avec Google Drawing pour créer des diagrammes.

**Astuce Pro :** n'oubliez pas d'ajouter un lien vers la version modifiable du diagramme sous la capture d'écran, afin de pouvoir le mettre à jour facilement plus tard lorsque les choses changeront inévitablement.

#### **Inclure des chiffres**

L'échelle du problème détermine souvent la solution. Pour aider les relecteurs à se faire une idée de l'état du monde, incluez des chiffres réels comme le nombre de lignes de la base de données, le nombre d'erreurs utilisateur, la latence — et comment ces éléments évoluent avec l'utilisation. Souvenez-vous de vos notations Big-O ?

#### **Essayez d'être drôle**

Une spécification n'est pas un article académique. De plus, les gens aiment lire des choses drôles, donc c'est un bon moyen de garder le lecteur engagé. Ne faites pas trop cela au point d'enlever l'idée principale.

Si vous, comme moi, avez du mal à être drôle, [Joel Spolsky](https://en.wikipedia.org/wiki/Joel_Spolsky) (_obviously_ connu pour ses talents comiques…) a ce conseil :

> L'une des façons les plus faciles d'être drôle est d'être **spécifique** lorsque ce n'est pas nécessaire [… Exemple :] Au lieu de dire « intérêts spéciaux », dites « agriculteurs gauchers d'avocats ».

#### Faites le **Test du Sceptique**

Avant d'envoyer votre document de conception à d'autres pour révision, passez-le en revue en faisant semblant d'être le relecteur. Quelles questions et doutes pourriez-vous avoir sur cette conception ? Ensuite, répondez-y de manière préventive.

#### Faites le **Test des Vacances**

Si vous partez en vacances prolongées maintenant sans accès à Internet, quelqu'un de votre équipe peut-il lire le document et l'implémenter comme vous l'aviez prévu ?

L'objectif principal d'un document de conception n'est pas le partage des connaissances, mais c'est un bon moyen d'évaluer la clarté afin que les autres puissent réellement vous donner des commentaires utiles.

![Image](https://cdn-media-1.freecodecamp.org/images/vqucQKHbe0zhgV9DZiEwWmogFhFzZTROdxAc)
_Photo par [Unsplash](https://unsplash.com/photos/IuE715vJo2I?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">SpaceX</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Processus

Ah oui, le redoutable _mot en P_. Les documents de conception vous aident à obtenir des commentaires avant de perdre beaucoup de temps à implémenter la mauvaise solution ou la solution au mauvais problème. Il y a beaucoup d'art pour obtenir de bons commentaires, mais ce sera pour un article ultérieur. Pour l'instant, parlons spécifiquement de la manière de rédiger le document de conception et d'obtenir des commentaires à ce sujet.

Tout d'abord, toutes les personnes travaillant sur le projet devraient faire partie du processus de conception. Il est acceptable que le responsable technique prenne beaucoup de décisions, mais tout le monde devrait être impliqué dans la discussion et adhérer à la conception. Donc le « vous » tout au long de cet article est un « vous » vraiment pluriel qui inclut toutes les personnes du projet.

Deuxièmement, le processus de conception ne signifie pas que vous restez devant le tableau blanc à théoriser des idées. N'hésitez pas à vous salir les mains et à prototyper des solutions potentielles. Ce n'est pas la même chose que de commencer à écrire du code de production pour le projet avant de rédiger un document de conception. Ne faites pas cela. Mais vous devriez absolument vous sentir libre d'écrire du code jetable et approximatif pour valider une idée. Pour vous assurer que vous n'écrivez que du code exploratoire, faites-en une règle selon laquelle **aucun de ce code prototype n'est fusionné dans master**.

Après cela, lorsque vous commencez à avoir une idée de la manière de procéder à votre projet, faites ce qui suit :

1. Demandez à un ingénieur expérimenté ou à un responsable technique de votre équipe d'être votre relecteur. Idéalement, ce serait quelqu'un qui est bien respecté et/ou familier avec les cas limites du problème. Corrompez-les avec du boba si nécessaire.
2. Allez dans une salle de conférence avec un tableau blanc.
3. Décrivez le **problème** que vous allez aborder à cet ingénieur (c'est une étape très importante, ne la sautez pas !).
4. Ensuite, expliquez l'**implémentation** que vous avez en tête, et convainquez-les que c'est la bonne chose à construire.

Faire tout cela **avant** même de commencer à écrire votre document de conception vous permet d'obtenir des commentaires dès que possible, avant d'investir plus de temps et de vous attacher à une solution spécifique. Souvent, même si l'implémentation reste la même, votre relecteur est en mesure de pointer les cas limites que vous devez couvrir, d'indiquer les zones potentielles de confusion et d'anticiper les difficultés que vous pourriez rencontrer plus tard.

Ensuite, après avoir écrit un brouillon de votre document de conception, faites relire le même relecteur, et faites-le approuver en ajoutant son nom en tant que relecteur dans la section **Titre et Personnes** du document de conception. Cela crée une incitation et une responsabilité supplémentaires pour le relecteur.

À ce sujet, envisagez d'ajouter des relecteurs spécialisés (comme des ingénieurs SRE et de sécurité) pour des aspects spécifiques de la conception.

Une fois que vous et le ou les relecteurs avez donné votre accord, n'hésitez pas à envoyer le document de conception à votre équipe pour des commentaires supplémentaires et le partage des connaissances. Je suggère de limiter ce processus de collecte de commentaires à environ 1 semaine pour éviter des retards prolongés. Engagez-vous à répondre à toutes les questions et commentaires que les gens laissent dans cette semaine. **Laisser des commentaires en suspens = mauvais karma.**

Enfin, s'il y a beaucoup de contentieux entre vous, votre relecteur et d'autres ingénieurs lisant le document, je vous recommande fortement de consolider tous les points de contentieux dans la section **Discussion** de votre document. Ensuite, organisez une réunion avec les différentes parties pour discuter de ces désaccords en personne.

Chaque fois qu'un fil de discussion dépasse 5 commentaires, passer à une discussion en personne tend à être beaucoup plus efficace. Gardez à l'esprit que vous êtes toujours responsable de prendre la décision finale, même si tout le monde ne peut pas parvenir à un consensus.

En parlant récemment avec [Shrey Banga](https://www.freecodecamp.org/news/how-to-write-a-good-software-design-document-66fcf019569c/undefined) à ce sujet, j'ai appris que Quip a un processus similaire, sauf qu'en plus d'avoir un ingénieur expérimenté ou un responsable technique de votre équipe comme relecteur, ils suggèrent également qu'un ingénieur d'une **autre** équipe révise le document. Je n'ai pas essayé cela, mais je peux certainement voir cela aider à obtenir des commentaires de personnes ayant des perspectives différentes et améliorer la lisibilité générale du document.

Une fois que vous avez fait tout ce qui précède, il est temps de passer à l'implémentation ! Pour des points bonus, **traitez ce document de conception comme un document vivant pendant que vous implémentez la conception**. Mettez à jour le document chaque fois que vous apprenez quelque chose qui vous amène à apporter des modifications à la solution originale ou à mettre à jour votre planification. Vous me remercierez plus tard lorsque vous n'aurez pas à expliquer les choses encore et encore à toutes vos parties prenantes.

Enfin, soyons **vraiment** méta pendant une seconde : Comment évaluons-nous le succès d'un document de conception ?

Mon collègue [Kent Rakip](https://www.linkedin.com/in/krakip/) a une bonne réponse à cela : **Un document de conception est réussi si le bon retour sur investissement du travail est réalisé.** Cela signifie qu'un document de conception réussi peut en fait conduire à un résultat comme celui-ci :

1. Vous passez 5 jours à écrire le document de conception, cela vous oblige à réfléchir à différentes parties de l'architecture technique
2. Vous obtenez des commentaires des relecteurs que `X` est la partie la plus risquée de l'architecture proposée
3. Vous décidez d'implémenter `X` en premier pour réduire les risques du projet
4. 3 jours plus tard, vous découvrez que `X` est soit impossible, soit beaucoup plus difficile que vous ne l'aviez prévu initialement
5. Vous décidez d'arrêter de travailler sur ce projet et de prioriser d'autres travaux à la place

Au début de cet article, nous avons dit que l'objectif d'un document de conception est de **s'assurer que le bon travail est fait.** Dans l'exemple ci-dessus, grâce à ce document de conception, au lieu de perdre potentiellement des mois pour abandonner ce projet plus tard, vous n'avez passé que 8 jours. Cela semble être un résultat assez réussi pour moi.

Veuillez laisser un commentaire ci-dessous si vous avez des questions ou des commentaires ! J'aimerais également entendre parler de la manière dont vous rédigez différemment les documents de conception dans votre équipe.

Rendant hommage là où c'est dû, j'ai appris beaucoup de ce qui précède en travaillant aux côtés de certains ingénieurs **incroyables** chez [Plaid](https://plaid.com/) ([nous recrutons !](https://jobs.lever.co/plaid?lever-via=fUydCnRbfC&commitment=Full-time&team=Engineering) Venez concevoir et construire des systèmes techniques avec nous) et [Quora](https://www.quora.com/careers).

Si vous aimez cet article, [suivez-moi sur Twitter](https://www.twitter.com/zhangelaz) pour plus d'articles sur l'ingénierie, les processus et les systèmes backend.