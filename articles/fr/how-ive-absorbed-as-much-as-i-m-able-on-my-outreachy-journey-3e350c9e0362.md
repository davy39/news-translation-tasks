---
title: Comment j'ai absorbé autant que possible lors de mon parcours Outreachy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-11T21:50:28.000Z'
originalURL: https://freecodecamp.org/news/how-ive-absorbed-as-much-as-i-m-able-on-my-outreachy-journey-3e350c9e0362
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l2XMmdd_4upTGH10T0kKPw.jpeg
tags:
- name: Health,
  slug: health
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment j'ai absorbé autant que possible lors de mon parcours Outreachy
seo_desc: 'By Toni Shortsleeve

  I can’t believe this will be the last month of my internship at LibreHealth! ?

  Just when it was starting to all come together. But I still have a few more weeks
  to finish my projects, and I’m thankful for the time to work on them....'
---

Par Toni Shortsleeve

Je n'arrive pas à croire que ce sera le dernier mois de mon stage chez LibreHealth ! 😮

Juste au moment où tout commençait à se mettre en place. Mais il me reste encore quelques semaines pour terminer mes projets, et je suis reconnaissante pour le temps qui m'est accordé pour travailler dessus.

Pour ceux qui me rejoignent dans mon parcours, je suis une [stagiaire Outreachy](https://www.outreachy.org/alums/) chez [LibreHealth](http://librehealth.io/) pour cet été. J'ai été acceptée le 23 avril de cette année pour commencer mon stage le 23 mai, jusqu'au 14 août. Vous pouvez en savoir plus sur le début de cette aventure [ici](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e).

Depuis mon dernier [article](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4), j'ai appris tellement de choses. Les deux documents sur lesquels je travaillais, les [LibreHealth EHR Provider Orders](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Provider_Orders) et les [LibreHealth EHR Encounters](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Encounters), ont été approuvés par mes mentors et sont maintenant sur le wiki de LibreHealth.

> **Note :** Les noms des patients et du personnel ou toute donnée que vous pourriez voir dans mes documents sont entièrement fictifs.

#### Mon stage Outreachy chez LibreHealth jusqu'à présent

Dans le document **Provider Orders**, nous avons couvert tout, depuis la visite du patient jusqu'à l'orientation du patient vers un laboratoire externe, puis la transcription de l'ordre.

La **transcription médicale** était un nouveau concept pour moi. Lorsque j'ai lu pour la première fois le mot « transcriptioniste », j'ai imaginé un rapporteur judiciaire à qui l'on demandait de relire les notes du témoin précédent. 🤔

En réalité, cela implique la comparaison de deux documents, puis le placement des informations de l'ordre du fournisseur dans le formulaire d'ordre de référence.

Parfois, les termes étaient similaires, comme **Referral Date**...

![Image](https://cdn-media-1.freecodecamp.org/images/yRVfSmYbUmqknbTBGEaYrs8B-oeCPBT3n6V0)

... et **Order Date**

![Image](https://cdn-media-1.freecodecamp.org/images/o5kWM-OFXaYmibY3QJE3549m1Wpmj7YdaFF6)

D'autres n'étaient pas si évidents.

Par exemple, le **Reason** sur le **Referral Form**

![Image](https://cdn-media-1.freecodecamp.org/images/JNeSmqHoLxAWzVr-4jzKQKFWUZzHO1gKdjyp)

... est le même que le **Clinical History** de la **Procedure Order**.

![Image](https://cdn-media-1.freecodecamp.org/images/dCosJ-mMlhn29T1vcr5UdHDGRV9hfcwmECCz)

Lorsque je conçois des pages web, je suis très gâtée avec mon codage. Avec HTML et CSS, j'ai la liberté de concevoir mes conteneurs, les bordures des images et les espacements comme nécessaire. Cependant, le format wiki ne le permet pas.

Un `<p>` ou `<br/>` n'avait aucun effet. Merci à mon [inter](http://king21.neowordpress.fr/focus-on-markdown/)n-mate Adele de m'avoir partagé que j'avais besoin de `<br>` sans la barre oblique initiale. Un concept totalement différent ! J'ai dû me rappeler sans cesse de rompre l'habitude d'ajouter cette barre oblique initiale.

Mon mentor m'a demandé de placer ces comparaisons côte à côte au lieu de les superposer, pour faciliter la lecture.

C'est à ce moment-là que j'ai appris que le wiki accepte certains éléments HTML dans la mise en forme. Imaginez ma joie lorsque j'ai découvert que je pouvais formater mon wiki avec du code comme ceci :

```
<div><blockquote>‘‘‘Referral Transaction’’’: ‘Referral Date’ = ‘‘‘Procedure Order’’’: ‘Order Date’<br><br><span>[[File:trans-refDate.jpg|500px]] [[File:trans-ordDate.jpg|500px]]</span><br><br></blockquote></div>
```

Et cela donne ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/mn0kSixpivfSzzsiqVG99Uq73Pxyuv-uCqO3)

Je pense que cela a l'air beaucoup mieux. Mon mentor était également d'accord. 😊

#### Relever de nouveaux défis

Mes deux domaines de défi dans les **Provider Orders** étaient le **Flow Board** et les **Fee Sheets**.

**Flow Board :** Le Flow Board suit le temps du patient dans chaque segment de la visite. Il se met à jour toutes les quelques secondes. Il conserve également tout ce qui s'est passé pendant la visite, y compris mes erreurs, et tente automatiquement de les corriger. On m'a finalement expliqué comment désactiver cela, mais il était trop tard. 😅

![Image](https://cdn-media-1.freecodecamp.org/images/s5y4Cs9lOfmNbfJ1tP-skr0CKPBkJYVUye1Z)

Remarquez comment l'**Appointment Time** ne correspondait pas à l'heure de **Start** ou **End**. Et le **Total Time** devait également être modifié. Non seulement cela, mais il ne devrait y avoir qu'un seul changement de statut.

Apparemment, le patient est arrivé trois fois. Elle est entrée dans la salle d'examen deux fois. Eh bien, vous voyez ce qui s'est passé. C'était un patient très occupé. 😅

De plus, le **Total Time** devait correspondre à la somme des temps de chaque section.

C'est là que mon expérience en développement et mon meilleur ami, l'Inspecteur Chrome, sont venus à ma rescousse. 😊

![Image](https://cdn-media-1.freecodecamp.org/images/gDJT-zwC9KSta-K65eoC8Fe8YsSEY6LotwUg)

J'ai pu modifier les détails, puis fermer l'Inspecteur et prendre une nouvelle capture. Bien sûr, chaque fois que j'oubliais une modification spécifique, je devais recommencer. Cette image a nécessité plusieurs essais pour être correcte :

![Image](https://cdn-media-1.freecodecamp.org/images/StI-STzGWCY-LqnEvgRtovndrzoeY2gJZOx-)

La **Fee Sheet** présentait des défis similaires car les codes devaient être ajoutés et justifiés.

Après avoir lutté avec les codes réels, je devais encore tout rendre esthétique dans tous les domaines.

![Image](https://cdn-media-1.freecodecamp.org/images/uIv2WkYDI8boVHFScxtwyJyM2kwoWmHPLeVI)

Et sur l'image finale, je devais supprimer les codes supplémentaires. Nous n'avons besoin que d'un seul code ICD10 pour une seule visite et une seule ordonnance.

![Image](https://cdn-media-1.freecodecamp.org/images/IAuCtqoHSYfliX13XzlYioMu-aH-le9gDfSp)

Dans la figure ci-dessus,

* CPT4 99203 est le code pour une visite de nouveau patient et le prix est de 25 $.
* CPT4 96372 est le code pour une injection. Il n'y a pas de coût car il est inclus dans le coût médical.
* HCPCS J2800 est le code pour le médicament injecté.

Chacun des codes ci-dessus a été justifié avec le code ICD10 M54.5.

Comme vous pouvez le voir, ICD10 M54.5 est le code de facturation médicale pour les douleurs lombaires.

Au début, cela m'a pris beaucoup de temps à comprendre, puis à tout rassembler. Je suis très reconnaissante envers mon mentor Harley Tuck pour sa patience.

Mais finalement, j'y suis parvenue et j'ai pu créer les **Billing Screens** et **Final Receipt**.

![Image](https://cdn-media-1.freecodecamp.org/images/-NvK2DUMv9PrWtvEbEtUTPx1GUtGN1HTkMrO)

#### La ligne d'arrivée

Ce sont mes missions **LibreHealth EHR**. Maintenant, je passe au segment **LibreHealth Radiology** et cela se déroulera un peu différemment.

Pendant mon stage, j'ai pu prendre un peu de temps pour me préparer à rencontrer d'autres membres de FreeCodeCamp à New York.

#### Prix du meilleur contributeur freeCodeCamp 2018

J'ai été totalement surprise de recevoir un email de [Quincy Larson](https://twitter.com/ossia) m'informant que j'avais été choisie pour être reconnue pour mes contributions à la publication Medium de [freeCodeCamp](https://www.freecodecamp.org/). Je ne pensais pas avoir fait quelque chose d'extraordinaire.

J'ai commencé à traîner dans les salons de discussion et les forums il y a un moment parce que je voulais connaître la réponse à une question ou apprendre une nouvelle solution à un problème. Ensuite, j'ai commencé à répondre à des questions dont je pensais connaître les réponses. Parfois, j'avais effectivement raison. 😊

J'aime coder. Cela me force à utiliser le côté logique de mon esprit pour résoudre des problèmes, et pourtant, mon côté créatif peut aussi rendre quelque chose de joli.

Mais j'aime aussi lire. Je fais partie d'un groupe de copies de révision avancées (ARC) pour quelques auteurs de fiction. J'aime leur travail et je peux parfois repérer une erreur avant qu'elle ne soit publiée.

Je lis les articles hebdomadaires envoyés par Quincy Larson, ainsi que le Digest Medium, depuis que j'ai rejoint freeCodeCamp. J'ai trouvé que ces articles m'ont beaucoup aidée, surtout si l'article était écrit en même temps que je travaillais sur un projet similaire ou que j'essayais de comprendre un concept similaire.

Alors, lorsque l'appel a été lancé pour des éditeurs bénévoles pour la publication Medium de freeCodeCamp, j'ai vu cela comme une grande opportunité d'étudier sous la direction de certains de mes auteurs préférés. Je peux lire les meilleurs articles en premier ! Et j'essaie d'aider à corriger les fautes de frappe ou les problèmes de grammaire qui surviennent.

Nous avons une grande équipe d'édition, et je suis fière d'en faire partie.

Lorsque j'ai postulé pour le stage de documentation avec LibreHealth, j'ai utilisé tout ce que j'avais appris en éditant ici sur Medium pour m'aider dans mon travail.

Et donc, lorsque j'ai reçu cet email de Quincy, j'ai mentionné l'événement du prix du meilleur contributeur 2018 à mon mentor. Il a suggéré que cela pourrait faire partie de mon stage. Il serait alors possible de recevoir une allocation pour aider à payer mon voyage à New York.

Ma coordinatrice Outreachy, [Sage Sharp](https://twitter.com/_sagesharp_), était d'accord avec mon mentor ! Je serai à New York le 18 août pour célébrer avec un groupe d'autres meilleurs contributeurs.

J'aurai également l'occasion de rencontrer l'un de mes autres mentors de LibreHealth à Manhattan dans la journée, avant l'événement freeCodeCamp de ce soir-là.

Et, bien sûr, j'ai également découvert que certains de mes héros préférés de freeCodeCamp seront présents à l'événement. Je suis excitée !

#### Derniers mots - Pour l'instant

Je voudrais rappeler aux femmes et aux autres membres sous-représentés dans l'industrie technologique :

La prochaine session de stages Outreachy commence en septembre 2018. Cela fait moins d'un mois. Si vous ne l'avez pas déjà fait et que vous êtes intéressé à postuler, [inscrivez-vous maintenant](https://lists.outreachy.org/cgi-bin/mailman/listinfo/announce) pour recevoir les annonces. Vous serez informé lorsque le processus commencera.

Et, les membres de freeCodeCamp sont également éligibles pour rejoindre ! 😊

Merci de rester avec moi dans ce voyage. J'aurai plus à partager à mon retour de New York.

#### **Articles précédents**

* [Comment j'ai battu les odds et suis devenue une stagiaire Outreachy](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e)
* [Mon stage Outreachy commence aujourd'hui ! Voici ce que j'ai fait et appris jusqu'à présent.](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619)
* [Les prochaines étapes de mon parcours Outreachy : Docker, grands défis et petites victoires](https://medium.freecodecamp.org/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a)
* [Chaque étape apporte quelque chose de nouveau dans mon parcours Outreachy](https://medium.freecodecamp.org/every-step-brings-something-new-on-my-outreachy-journey-e7c0f7adf2ea)
* [Moments spéciaux de mon parcours Outreachy](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4)