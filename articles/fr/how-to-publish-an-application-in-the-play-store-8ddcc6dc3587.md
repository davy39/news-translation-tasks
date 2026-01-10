---
title: Comment publier une application dans le Play Store
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-01-08T01:08:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-an-application-in-the-play-store-8ddcc6dc3587
coverImage: https://cdn-media-1.freecodecamp.org/images/0*SzdQbUV7zp0_5_fC
tags:
- name: Apps
  slug: apps-tag
- name: Android
  slug: android
- name: coding
  slug: coding
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment publier une application dans le Play Store
seo_desc: If you have been following my articles, you may have noticed that I have
  been writing about developing and publishing a Chrome extension. Now, I want to
  take you on a different journey. What one must undergo to publish an application
  in the Play stor...
---

Si vous avez suivi mes articles, vous avez peut-être remarqué que j'ai écrit sur le développement et la publication d'une extension Chrome. Maintenant, je veux vous emmener dans un voyage différent. Ce que l'on doit faire pour publier une application dans le Play Store. **Allons-y, jouons.**

#### Avant de trop nous exciter

Il y a quelques choses que nous devons vérifier avant de nous rendre dans le Play Store :

* [Signer numériquement votre APK](https://developer.android.com/studio/publish/app-signing) - Cela est requis par Google afin qu'ils puissent vérifier qui est l'auteur de l'application.
* [Construire votre APK](https://developer.android.com/studio/run/) - Vous devez construire une version **_release_** de votre application
* [Créer un compte développeur](https://play.google.com/apps/publish/) - Vous devez avoir un compte développeur dans la Google Play Console. **_Bien que la création soit gratuite, vous devez payer 25 $ pour pouvoir publier des applications._**

![Image](https://cdn-media-1.freecodecamp.org/images/fINt0mz9aAydAocUVQCBsRmuS0F4YFh79-Mn)
_Photo par [Unsplash](https://unsplash.com/@spaceboy?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Henrik Dønnestad</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Passer par les étapes

Maintenant que nous avons terminé toutes les formalités, nous pouvons commencer le processus de publication de l'application.

> ⚠️ Avertissement : Vous ne pourrez PAS publier votre application si vous ne complétez pas toutes les étapes ci-dessous

1. Connectez-vous à la Google Play Console
2. Lorsque vous êtes sur l'onglet **_Toutes les applications_**, dans le coin supérieur droit, vous verrez un bouton **_Créer une application_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/3FO0tqmLtPe684x773I281WKSDIKsA2WrOfN)
_Cliquez dessus_

3. Ensuite, donnez un titre à votre application et la langue par défaut

4. Vous serez maintenant redirigé vers l'écran **_Fiche de l'application_**

![Image](https://cdn-media-1.freecodecamp.org/images/mtdATBsQ-ScG91neilPm0ntsYTShZp5hT9Hg)
_Fiche de l'application - Tout ce qui concerne l'apparence de votre application dans le store_

Ici, vous devrez fournir les éléments **_obligatoires_** suivants (ils sont obligatoires car ils ont un ⭐ à côté) :

* Une courte description de votre application
* Une description complète
* Des captures d'écran (au moins 2)
* Une icône haute résolution
* Un graphique de fonctionnalité
* Le type de l'application et sa catégorie
* Votre email
* Votre politique de confidentialité (si vous n'en avez pas, cochez la case "Ne pas soumettre de politique de confidentialité")

5. Allez maintenant à la fenêtre **_Versions de l'application_**

![Image](https://cdn-media-1.freecodecamp.org/images/ZGoBMntMJIXJsORd1l47A6CDvVh-gtroqH8f)
_Versions de l'application - Choisissez une voie pour publier votre application_

Ici, vous devrez choisir une voie pour publier votre application. Une voie est essentiellement le processus de publication de votre application. Vous pouvez choisir de la publier directement en production, ou en phase bêta ou pour un test interne. La plupart des voies sont similaires dans ce que vous devez faire, à part les différences évidentes, donc je vais me concentrer sur la publication d'une application en **_Production_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/Y6nze58diPwB0Vi3rqCqYJAwday9v-Lva-vu)
_Cliquez sur Créer une version_

6. Ici, vous devrez soit signer votre application en utilisant Google Play, soit choisir de ne pas le faire. Ensuite, vous devrez télécharger l'APK que vous avez construit.

![Image](https://cdn-media-1.freecodecamp.org/images/QJwr6tTkpsoAvmgctnTQ3ntIKlauFFhMmKaA)
_Téléchargez votre APK_

Ici, vous pouvez également donner un nom à la version et spécifier ce qui est nouveau dans cette version. **_Faites particulièrement attention à ce que vous tapez dans "ce qui est nouveau dans cette version" car cela apparaîtra dans le Play Store sous la section "Nouveautés"_**. Une fois que vous avez terminé, vous pouvez appuyer sur le bouton **_Revoir_** dans le coin inférieur droit de la page.

7. Ensuite, **_Classification du contenu_**

![Image](https://cdn-media-1.freecodecamp.org/images/1t1lVM2li7KQrcEe5kyPQguaUznjvB-cODoI)
_Le bouton Continuer ne sera pas grisé si vous avez complété toutes les choses nécessaires_

Après avoir appuyé sur le bouton Continuer, qui ne sera pas grisé si vous avez fait toutes les étapes ci-dessus, vous serez invité à répondre à plusieurs questions concernant le contenu de votre application. Suivez-les simplement dans l'ordre, en les remplissant une par une.

8. Enfin, mais non des moindres, **_Prix et distribution_**

![Image](https://cdn-media-1.freecodecamp.org/images/0BEO1RTaMOhJgLNIJ1ibCUtxCkzfgIybbMSY)
_Décidez des questions monétaires de votre application_

Dans cette dernière page, vous pouvez décider :

* Si votre application sera gratuite ou non
* Dans quels pays votre application sera disponible
* Si elle contient des publicités
* Programmes utilisateurs
* Consentement

Assurez-vous de remplir tous les champs obligatoires (marqués d'un ⭐)

![Image](https://cdn-media-1.freecodecamp.org/images/fdrB6t7r3L2yMo16Z4x-Wcv16cteqSRvcxor)
_Photo par [Unsplash](https://unsplash.com/@dre0316?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Andre Hunter</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

C'est tout ! Après tout ce travail acharné, vous pouvez maintenant publier votre application. Retournez à la fenêtre des versions de l'application et procédez à la publication de votre application.

N'oubliez pas de me faire savoir ce que vous pensez dans les commentaires ci-dessous.

_Si vous avez aimé cet article, applaudissez pour que d'autres puissent en profiter également ! ?_