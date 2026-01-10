---
title: Réflexions finales sur mon parcours estival avec Outreachy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T22:49:12.000Z'
originalURL: https://freecodecamp.org/news/final-reflections-on-my-summer-journey-with-outreachy-3d38375f8b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mw4SmCZV23tSDsDsV8xuXg.jpeg
tags:
- name: coding
  slug: coding
- name: healthcare
  slug: healthcare
- name: Life lessons
  slug: life-lessons
- name: outreachy
  slug: outreachy
- name: 'tech '
  slug: tech
seo_title: Réflexions finales sur mon parcours estival avec Outreachy
seo_desc: 'By Toni Shortsleeve

  Working as an Outreachy intern with LibreHealth this summer has been a great experience!
  Needless to say, I had mixed emotions when it was time to hand in my final project.
  I am proud of what I’ve contributed, thankful to have wor...'
---

Par Toni Shortsleeve

Travailler en tant que stagiaire [Outreachy](https://www.outreachy.org/) avec [LibreHealth](https://librehealth.io/) cet été a été une expérience formidable ! Inutile de dire que j'avais des émotions mitigées lorsque le moment est venu de remettre mon projet final. Je suis fière de ce que j'ai contribué, reconnaissante d'avoir travaillé avec de grands mentors et une collègue stagiaire fabuleuse, et attristée que cela se termine.

Pour ceux qui doivent rattraper leur retard, vous pouvez lire le [début](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e) de mon expérience. Les autres liens de mon parcours seront à la fin de cet article. Pour ceux d'entre vous qui m'ont suivie tout au long de cet été, je vais directement entrer dans le vif du sujet.

### Projets

En tant que stagiaire en documentation, j'ai fourni une partie de la documentation sur le système de dossiers de santé électroniques de LibreHealth en anglais. [Adele](https://medium.freecodecamp.org/@nguimatiobest) était ma collègue stagiaire. Elle a traduit toute la documentation en français. Vous pouvez suivre son parcours [ici](http://king21.neowordpress.fr/my-internship-is-coming-to-an-end/).

Du 23 mai au 31 août, j'ai contribué à quatre documents sur le wiki de LibreHealth.

#### Guide de l'utilisateur

Mon premier document était le [Guide de l'utilisateur de LibreHealth EHR](https://wiki.ehr.librehealth.io/LibreHealth_EHR_User_Guide). Il s'agissait d'un aperçu de l'apparence de base et des fonctionnalités du système LibreHealth EHR. Nous avons parcouru les différents écrans et nous nous sommes concentrés sur les différentes fonctionnalités du système. L'objectif était d'aider l'utilisateur à faire fonctionner le système de dossiers de santé électroniques de manière fluide et efficace. Nous avons exploré les sections Connexion, Préférences de l'utilisateur et Navigation dans le menu.

![Image](https://cdn-media-1.freecodecamp.org/images/oKxVj35LEJL651obqtONNBxpz67nzf6JgiTp)
_user-login-1_

J'ai suivi une vidéo de mon mentor EHR, Harley Tuck, intitulée [LibreHealth EHR Introduction To Libre](https://www.youtube.com/watch?v=Fh0_NUVUn7k&t=62s). Bien qu'elle n'ait que quelques mois, certaines choses avaient changé. J'ai utilisé la démo du site pour capturer le flux et les images non couvertes dans la vidéo. J'aime la façon dont Harley parle — claire, articulée et précise. J'ai essayé de garder le ton des guides de l'utilisateur conversationnel, comme il l'a fait.

Un médecin, également appelé prestataire, était déjà répertorié dans la démo. J'ai créé une nouvelle installation — également appelée pratique — pour montrer les différentes méthodes de calendriers et de préférences de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/B5kDyiFrn1qdc-G5lkkJ11LjVU-cZIuSJArI)
_nav-cal-two-day.jpeg_

#### Ordres des prestataires

Le deuxième document était le guide [LibreHealth EHR Provider Orders](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Provider_Orders). J'ai créé un patient qui avait besoin d'une référence pour une radiographie. Ensuite, j'ai créé le laboratoire qui effectuerait la radiographie afin que nous puissions envoyer les ordres.

J'ai utilisé le même médecin et la même installation que ceux que j'avais utilisés pour le guide de l'utilisateur précédent. J'ai également créé trois utilisateurs. Il s'agissait du réceptionniste de l'accueil, de l'IPL et du transcripteur.

![Image](https://cdn-media-1.freecodecamp.org/images/BaPJ8TafBpasJLSkDtxYOoyxMChhOqpFJbIB)

#### Rencontres ou visites

Le troisième document était le guide [LibreHealth EHR Encounters](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Encounters). Il était similaire aux ordres des prestataires. Cependant, au lieu d'envoyer le patient à un autre prestataire, nous avons administré des médicaments sur place.

![Image](https://cdn-media-1.freecodecamp.org/images/2xdc3Vp3NimMwy2Lt6fymIJfkeiSgzfuWpGh)
_encounter-soap-med.jpeg_

C'est là que j'ai beaucoup appris sur les codes de santé. Comprendre comment les services, les procédures et la justification — pour la facturation de l'assurance — fonctionnaient ensemble pour créer les frais à payer.

![Image](https://cdn-media-1.freecodecamp.org/images/4urStQjQ0u9LAooMVzozXyYcW4WmLznWD5SD)

Remarquez les deux codes CTP4 :
99203 est la première visite du patient à 25 $.
96372 est l'injection sans frais. Les frais pour l'injection étaient couverts par le médicament — code HCPCS.

HCPCS J28000 est le médicament sous forme de solution à 27 $.

Ils se sont tous combinés avec le code de diagnostic ICD10 de M54.5 comme douleur lombaire.

#### Feuilles de frais

Le document final était [COMMENT : Créer des catégories de liste de feuilles de frais](https://wiki.ehr.librehealth.io/HOW_TO:_Create_Fee_Sheet_List_Categories). Ce guide pratique montrait comment l'administrateur ajouterait un médicament et le code approprié à une liste de feuilles de frais. Les informations sur la liste de feuilles de frais seront utilisées pour la facturation de la visite sur la feuille de frais.

![Image](https://cdn-media-1.freecodecamp.org/images/4W1Ph3qzQsyIq3Mzb93kHHPH0SeTB7MY7YIX)

### Leçons apprises

#### Wiki

Wiki est largement ouvert aux contributeurs. Cela signifie que nous devions être très prudents quant à la manière dont nous nommions nos fichiers et images. Sinon, vous pourriez finir par utiliser les images de quelqu'un d'autre.

J'ai résolu ce problème en préfixant l'image par le surnom du document ou de la section, puis par le nom réel de l'image. Par exemple : `orders-vapgar.jpg`.

![Image](https://cdn-media-1.freecodecamp.org/images/Foe2ug4u0mLkAVecnJaZZgxeWBxzGMm7SRKN)
_orders-vapgar.jpg_

Le markdown de Wiki n'est pas le même que les fichiers ReadME.md de GitHub. Et ce n'est pas du HTML. J'ai dû faire un ajustement d'attitude de code, car je ne pouvais pas tout à fait styliser comme je le faisais normalement.

La balise `<p>` ne fonctionnait pas du tout pour moi. J'ai donc essayé une balise `<br/>`. Non, cela ne fonctionnait pas non plus. Cependant, la balise `<br>` fonctionnait.

Je ne pouvais pas diviser les colonnes — comme on le ferait sur une grille. Cependant, `<div>`, `<span>` et `<blockquote>` ont résolu mon problème.

Je ne pouvais pas utiliser la balise `<img src="section-image.jpg" />`. Les images sont appelées fichiers. J'ai donc dû appeler `[[Files:section-image.jpg]]`.

Mon code pour créer une section d'image à deux lignes et deux colonnes ressemblait à ceci :

```html
<div>
  <blockquote>
    'Referral Transaction': 'Referral Date' = 'Procedure Order': 'Order Date'
    <br><br>
    <span>
      [[File:trans-refDate.jpg|500px]] [[File:trans-ordDate.jpg|500px]]
    </span>
    <br><br>
  </blockquote>
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/-DEKVfggg2VUUFFjwBlc2IcjVYaZG2f2o9Ta)
_Cela a fonctionné !_

C'était différent pour moi et cela a pris un certain temps pour m'adapter.

#### Santé

Les notes SOAP ne concernent pas le savon pour se laver. Ce sont les notes du médecin et de l'infirmière qui reflètent les déclarations du patient, les observations objectives du médecin, l'évaluation de la situation et le plan de traitement pour le patient.

![Image](https://cdn-media-1.freecodecamp.org/images/VUCQxSEpi1gaLb49gn-8oJVksdq3knLoAKnH)

De plus, si ce n'est pas dans le plan des notes SOAP, ne le faites pas...

Le flux de travail est très spécifique. De nombreux membres du personnel ont un accès restreint à diverses zones des informations sur les patients.

![Image](https://cdn-media-1.freecodecamp.org/images/I6f774Vry4gNZFGKCjeYtun89EeMtNELqncZ)
_order-access.jpg_

La facturation, les médicaments, les frais et les codes de justification sont très stricts. J'ai beaucoup vérifié avec mon mentor pour m'assurer que mon travail était correct.

#### Styles de documentation

Mes trois premiers documents avaient un ton conversationnel. Cependant, le dernier document était un guide d'instructions étape par étape.

Ce n'était pas facile pour moi de placer des flèches et des numéros dans celui-ci. Bien qu'il s'agisse du plus petit document, il a nécessité plus de concentration pour le réaliser comme le voulait mon mentor.

![Image](https://cdn-media-1.freecodecamp.org/images/HPO2TSowp3t4y5XxfSSEJDaWH3ws82FjazmN)

### Réalisations

Cet été a été rempli de nombreuses bénédictions et de sentiments d'accomplissement positif pour moi.

J'ai beaucoup appris sur les pratiques de santé, les codes et les flux de travail. J'ai également appris beaucoup sur la documentation technique et utilisateur.

Et j'ai appris plus d'une façon de créer des documents markdown.

#### Outreachy

Cet été n'aurait pas pris cette direction si je n'avais pas d'abord été acceptée au stage Outreachy. Cela signifiait beaucoup pour moi que parmi 45 candidats, j'étais considérée comme quelqu'un qui pouvait aider avec leur projet LibreHealth.

Le fait qu'ils soient prêts à me payer pendant que j'apprenais était encore plus génial.

Ensuite, ils ont fourni une allocation de voyage pour le [New York Minute](https://medium.freecodecamp.org/how-i-escaped-to-nyc-and-celebrated-with-freecodecamp-on-my-outreachy-journey-22946d5af21e) de mon voyage.

Je recommande à chaque étudiante en technologie de postuler pour le stage Outreachy lorsque les sessions s'ouvrent.

#### freeCodeCamp

L'une de mes tâches en tant que stagiaire Outreachy était d'écrire toutes les deux semaines sur mes expériences. Je ne me considère vraiment pas comme une écrivaine, donc cela semblait être une tâche ardue.

En tant que campeuse de freeCodeCamp et éditrice pour freeCodeCamp sur Medium, j'avais la plateforme de publication parfaite. Heureusement, notre fondateur [Quincy Larson](https://twitter.com/ossia) a accepté.

Notre rédactrice en chef, [Abigail Rennemeyer](https://twitter.com/abbeyrenn), a été la première à voir mes brouillons — après mon mari, [Alex Shortsleeve](https://twitter.com/alxsleeve). Elle m'a encouragée à écrire plus et à arrêter de faire des articles d'une minute.

Et nous avons une équipe d'édition géniale qui fait en sorte que mon travail final soit beau. Mais les images sont toutes de moi...

#### Prix du meilleur contributeur

J'ai été l'une des deux cents campeuses à recevoir le badge de meilleur contributeur de [freeCodeCamp](https://www.freecodecamp.org/konikodes). Ce fut un grand honneur, mais je n'étais pas sûre de pouvoir me permettre de voyager de l'autre côté du continent.

C'est alors que mon mentor de LibreHealth m'a fait contacter mon organisateur d'Outreachy. J'ai été approuvée pour l'allocation de voyage ! Je suis arrivée tard vendredi soir et je suis partie tôt dimanche matin. Mais mon samedi était génial !

J'ai pu rencontrer certains de mes héros et auteurs, quelques-uns de mes modérateurs préférés et les grandes personnes qui dirigent des groupes d'étude du monde entier. C'était incroyable. Vous pouvez voir le flux en direct [ici](https://www.youtube.com/watch?v=u_4ZhwZmtes).

Honnêtement, je ne pense pas avoir fait grand-chose pour mériter cela. J'ai simplement aimé éditer certains des articles de mes auteurs préférés et répondre aux questions dont je pensais connaître les réponses sur le Forum. Mais je suis contente qu'ils n'aient pas réalisé que je n'étais qu'une curieuse...

### Regrets et espoirs

J'avais l'espoir d'en apprendre davantage sur le système d'information radiologique de LibreHealth. J'ai commencé à travailler sur deux documents différents, le guide de l'utilisateur et le guide technique.

Je n'ai pas pu le terminer en raison de difficultés techniques. J'espère que le prochain stagiaire pourra le créer correctement.

### Conseils pour les futurs stagiaires

À partir du 19 septembre, les candidatures pour les stages Outreachy de décembre 2018 à mars 2019 sont maintenant ouvertes. Vous pouvez postuler [ici](https://www.outreachy.org/apply/).

Trouvez quelque chose qui vous intéresse. Quelque chose que vous pouvez aimer apprendre et à laquelle vous pouvez contribuer.

Suivez les directives d'Outreachy. Votre projet aura également des directives en place pour vous. Vous pouvez les faire fonctionner ensemble. En cas de doute — comme les dates limites — demandez à votre organisateur Outreachy.

Soyez patient. Tout le monde n'est pas dans votre fuseau horaire. Et tout le monde a un emploi du temps différent. Posez donc votre question, mais sachez qu'il peut falloir quelques jours pour obtenir une réponse.

N'oubliez pas les jours fériés. En Amérique, nous avons beaucoup de jours fériés nationaux. Et chaque État a ses propres jours de célébration. La famille passe généralement en premier. Si vous avez un jour férié à venir — où le travail, les services et les banques sont fermés — informez votre équipe à l'avance.

Soyez transparent. Vous travaillerez dans un environnement open source. N'envoyez pas de message direct à votre mentor sauf si c'est une question sur votre charge de travail personnelle. Le reste de l'équipe et les mentors doivent voir ce que tout le monde fait.

Soyez amical et jouez bien. Oui, c'est une compétition. Mais gardez-la amicale.

### Remerciements

Un remerciement spécial à mes mentors, Harley Tuck et Robby O'Connor. Vous m'avez tous les deux gardée sur la bonne voie, encouragée à me dépasser et applaudie lorsque j'ai réussi.

Et merci à vous, mes lecteurs. Vos retours ont été inestimables. Et le fait que vous m'ayez suivie tout au long de mon parcours a vraiment contribué à rendre mon été une saison spéciale.

#### Et maintenant ?

La saison d'automne commence avec la fin d'un projet d'édition spécial et le début du travail avec un autre campeur sur une nouvelle bibliothèque intéressante.

Je retournerai également à mon programme [freeCodeCamp](https://learn.freecodecamp.org/) et verrai si je peux faire des progrès réels sur mes défis React-Redux. Et, espérons-le, créer quelque chose de spécial à partager avec le monde.

#### Articles précédents

* [Comment j'ai battu les probabilités et suis devenue une stagiaire Outreachy](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e)
* [Mon stage Outreachy commence aujourd'hui ! Voici ce que j'ai fait et appris jusqu'à présent.](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619)
* [Les prochaines étapes de mon parcours Outreachy : Docker, grands défis et petites victoires](https://medium.freecodecamp.org/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a)
* [Chaque étape apporte quelque chose de nouveau dans mon parcours Outreachy](https://medium.freecodecamp.org/every-step-brings-something-new-on-my-outreachy-journey-e7c0f7adf2ea)
* [Moments spéciaux de mon parcours Outreachy](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4)
* [Comment j'ai absorbé autant que possible lors de mon parcours Outreachy](https://medium.freecodecamp.org/how-ive-absorbed-as-much-as-i-m-able-on-my-outreachy-journey-3e350c9e0362)
* [Je suis arrivée à NYC et j'ai célébré avec freeCodeCamp lors de mon parcours Outreachy](https://medium.freecodecamp.org/how-i-escaped-to-nyc-and-celebrated-with-freecodecamp-on-my-outreachy-journey-22946d5af21e)
* [Partager l'esprit Aloha avec le Cloud](https://medium.freecodecamp.org/sharing-the-aloha-spirit-with-the-cloud-1c62e1a93cfb)

Vous pouvez me retrouver sur [GitHub](https://github.com/KoniKodes) ou me rejoindre sur [Twitter](https://twitter.com/konikodes). Vous pouvez également visiter mon [site web](https://www.konikodes.com).