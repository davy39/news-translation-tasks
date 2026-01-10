---
title: Android Studio 4.0 – les mises à jour les plus excitantes expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-19T22:28:00.000Z'
originalURL: https://freecodecamp.org/news/android-studio-4-updates
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/android.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: mobile app development
  slug: mobile-app-development
seo_title: Android Studio 4.0 – les mises à jour les plus excitantes expliquées
seo_desc: "By Roger James\nIn the midst of a pandemic, Google finally released its\
  \ stable version of Android Studio 4.0 on May 28, 2020. \nEvery release brings its\
  \ own interesting updates and bug fixes that help developers code smarter and develop\
  \ apps faster tha..."
---

Par Roger James

Au milieu d'une pandémie, Google a enfin publié sa version stable d'**Android Studio 4.0 le 28 mai 2020**.

Chaque version apporte ses propres mises à jour intéressantes et corrections de bugs qui aident les développeurs à coder plus intelligemment et à développer des applications plus rapidement que jamais. Et Android Studio 4.0 ne fait pas exception.

Dans cet article, nous allons découvrir certaines des fonctionnalités passionnantes qu'Android Studio 4.0 apporte, ce qui aidera beaucoup les développeurs.

Vous pouvez obtenir un lien direct pour télécharger Android Studio 4.0 en [cliquant ici](http://studio) pour vos machines Windows, Mac et Linux.

Voici quelques points forts des notes de version :

![Image](https://lh4.googleusercontent.com/L6l7K-eujulsvFgFa-c-Z8Uw5vf8G2g-P_3lLVWFm5Ijt7KEFZRw6OLenSHrCZxOHoRLQaWVfONUAnxSRoqqQGwZqh4ipYZYrJqoOPaKnnn1GhD8yOzrIr2eJprSl4p_ievJswEa)

Android Studio 4.0 introduit une pléthore de fonctionnalités intéressantes, notamment :

* Fenêtre de vitesse de construction
* Aperçu multi-disposition
* Éditeur de mouvement
* Inspecteur de disposition en direct
* Éditeur intelligent pour les règles R8
* Fichiers de script Kotlin DSL

Examinons en profondeur les nouvelles fonctionnalités amusantes d'Android Studio 4.0.

## Quelles sont les nouvelles fonctionnalités d'Android Studio 4.0 ?

Voici une liste des nouvelles fonctionnalités avec quelques informations sur leur fonctionnement et pourquoi elles sont géniales.

### 1. Éditeur de mouvement

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-101.png)

L'Éditeur de mouvement améliore l'éditeur de conception visuelle pour la disposition de mouvement et génère également du XML. MotionLayout est une sous-partie de _ConstraintLayout_ qui aide les développeurs à gérer l'animation des widgets et des mouvements dans les [applications mobiles](https://www.freecodecamp.org/news/how-to-secure-mobile-apps/).

Il dispose d'un éditeur de conception visuelle qui vous aide à créer, modifier et prévisualiser vos animations sans développer l'application. Il vous permet également de lire/mettre en pause les animations pour le débogage.

Motion Layout remplace l'ancienne disposition de contrainte et l'améliore. Il aide les développeurs d'applications Android à animer entre les états de disposition et à gérer les animations critiques facilement.

Vous pouvez maintenant déployer l'_API Motion Layout_ avec l'_Éditeur de mouvement_ avancé pour développer ou modifier une animation tandis que tout est stocké dans un fichier XML.

La seule différence est que vous n'avez pas besoin de l'écrire manuellement car tout est maintenant géré par l'Éditeur de mouvement. Vous pouvez facilement prévisualiser vos animations et apporter des modifications.

### 2. Inspecteur de disposition en direct

![Image](https://lh6.googleusercontent.com/CY3Ej_RuhXaxqK9wYYAqDXcoNL_3pJR1nxZUO4_eypEC1ChBZjD4Je_IFKNRal-L4xIQznl8aGW0fefhj0tbkyno6yEm3ooBUynqUaSdTGhwpt08EKFQd3ErFIZPAsz7pdKiy_a-)
_[**Source de l'image**](https://medium.com/androiddevelopers/layout-inspector-1f8d446d048)_

Android Studio 4.0 permet désormais aux développeurs d'avoir des informations en temps réel sur l'interface utilisateur de leurs applications mobiles. Cela signifie que vous pouvez maintenant visualiser comment votre application sera disposée à l'écran avec diverses fonctionnalités.

Il dispose également d'une hiérarchie de disposition dynamique qui est mise à jour à chaque actualisation, et d'attributs de vue détaillés qui vous aident à déterminer les valeurs des ressources.

Vous pouvez déployer la fonctionnalité en sélectionnant **Affichage > Fenêtres d'outils > Inspecteur de disposition** dans le menu principal.

Si vous déployez une application sur un appareil fonctionnant avec le niveau d'API 29 ou supérieur, vous pouvez accéder à des fonctionnalités supplémentaires comme une disposition dynamique. Il y a beaucoup d'informations détaillées sur l'Inspecteur de disposition à consulter également.

Sa fonctionnalité de résolution des valeurs de propriété vous permet de connaître l'origine de la propriété dans le code source. Elle vous guide également vers son emplacement en utilisant le lien hypertexte. Vous pouvez tirer parti de la représentation 3D si votre application ou votre appareil fonctionne avec **Android API 29** ou plus.

Les développeurs peuvent maintenant déployer une représentation 3D de l'animation à l'écran et inspecter les autres attributs. Ainsi, lorsque vous engagez un développeur pour moderniser l'interface de votre application ou ajouter de nouvelles fonctionnalités, vous n'avez pas à vous soucier de l'apparence de l'application avec la typographie moderne de conception UX/UI, car vous pouvez vérifier simultanément pendant le codage.

### 3. Validation de disposition

![Image](https://lh6.googleusercontent.com/mNaXO7Uhmu5DFI2ctSeWhqGeEz1zOgVjp82W6wJ4CaKV0SVPNK7Lb3DfU8UsRTNXYT4-DqHeuFYFj5hhuO-ZchoNm4TpriRLhvGf2dYSS_uXY5oJwQOfsK0DPgPAv_TOpUaf5i9b)
_[**Source de l'image GIF**](https://developer.android.com/studio/debug/layout-inspector)_

Vous pouvez maintenant produire des dispositions sur divers appareils et les configurer en même temps sans interruption. La _Validation de disposition_ ou l'_Aperçu multi-disposition_ sont des outils visuels.

Auparavant, lors de la création d'une disposition dans Android Studio, le passage entre différentes tailles et résolutions d'écran en mode aperçu était difficile. Mais avec ces dernières mises à jour, c'est beaucoup plus simple.

Comment ? Eh bien, vous devez simplement choisir les appareils en pixels, puis vous pouvez facilement vérifier ou prévisualiser les changements dans l'environnement de développement intégré.

Vous pouvez également utiliser cet outil pour identifier les problèmes potentiels dans l'interface utilisateur, car vous concevez souvent une interface utilisateur pour une configuration particulière ou une taille d'écran visible.

Vous pouvez accéder à cet outil en cliquant sur l'onglet **Validation de disposition** dans le **coin supérieur droit** de la **fenêtre de l'IDE**.

### 4. Analyseur de construction

![Image](https://lh3.googleusercontent.com/QHwWxAxkZUKTSzxmElJXcV6U8TL88Cg-aRYU_9C-H_x0lJUbCaIq-YHHdCYEShM5pIJVb6_2eW9cQpXZeVsDkRqNHn2TJdlAOFiAs6hBzIEpLRd_kVW_2tc9xq99BsidcgC9HU51)
_[**Source de l'image**](https://developer.android.com/studio/build/apk-analyzer)_

Android Studio 4.0 a introduit un outil d'analyse de construction qui aide les développeurs à analyser et à gérer les problèmes liés à la construction. Le temps de développement des applications a toujours représenté beaucoup de travail supplémentaire pour les développeurs Android.

Cette nouvelle fonctionnalité atténue rapidement le temps perdu et la productivité en reconnaissant les travaux obsolètes et mal configurés. L'outil d'analyse de construction montre vos travaux et plugins et suggère des moyens de réduire les régressions.

Cela aide également à résoudre un autre problème : auparavant, les développeurs ne savaient pas exactement quelle partie du système de construction prenait plus de temps. Ce n'est plus le cas maintenant.

Ainsi, le nouveau plugin Gradle 4.0 aide les développeurs à analyser et à trouver le problème, tel que des tâches mal configurées, dans le processus de construction. Vous pouvez facilement spécifier les paramètres par défaut en incluant une ou plusieurs des lignes ci-dessous dans chaque fichier build.gradle des modules.

![Image](https://lh4.googleusercontent.com/IfEkdNyS602D0FbzFoVDUj_vkXeqIyNdAJI4FzbZW6WhxG3ik3MBx0fGRoIAfaWxJE32d6VK_T-WJfuWGf6d_ktladRlmQRBV_I-lYSQJA_iqwi40sxdVpfJTsjMpK1MaBfT9ntl)

L'analyseur de construction vous aide également à identifier et à comprendre les goulots d'étranglement dans votre construction en mettant en évidence les plugins et les tâches qui sont les plus importants pour le temps de construction global de l'application. Il vous donne ensuite quelques étapes pour atténuer les régressions.

### 5. Désucriage de la bibliothèque de langage Java 8 pour toutes les API

![Image](https://lh5.googleusercontent.com/eBFuPz0PDehdRa28ZEMxNTd3Ya2cZH48-bNlO_COUAG6ZPLfY9Wd-uflU4Cp4le12aFmv0cGD1-OuLopJ-48oThRNszytUiOtVsl69lWyFdy9N4gQ6aiKEhdNQ1qJIaR34r-j36u)
_[**Source de l'image**](https://developer.android.com/studio/write/java8-support?hl=el)_

Une autre partie super ennuyeuse du développement d'applications Android a été d'essayer de déployer les fonctionnalités de Java 8. Vous pouvez trouver du code qui utilise un **Stream** ou vouloir implémenter une **fonction lambda**, ou il peut même y avoir une API Java 8 dont vous avez besoin et qui n'est pas pratique à contourner.

Mais avec le plugin **Android Gradle**, vous pouvez compiler certaines fonctionnalités de Java 8 avec vos anciennes API.

Et Android Studio 4.0 active le moteur de désucriage pour fournir un support aux langages Java.

### 6. Fonctionnalités de construction

![Image](https://lh6.googleusercontent.com/uLTDonznC4iK9bVZR3aCBh3RYjfKe4t5JeumdJw3gGs_XawiJ02o4Cujzg8LixhSVtmtFToeJ62rgeNfIC57DgewvVcZdE43SreMHunupZbW-kGved-0_9hTVjrkBl9HcQCgm-L9)
_[**Source de l'image**](https://developer.android.com/studio/releases)_

Les développeurs utilisant Android Studio 4.0 peuvent activer et désactiver les fonctionnalités de construction, telles que la liaison de vue, la liaison de données ou les classes BuildConfig générées automatiquement.

De plus, vous n'avez peut-être pas besoin de ces plugins et bibliothèques pour chaque projet, vous pouvez donc désactiver les bibliothèques/plugins et augmenter la scalabilité pour les grands projets.

Kotlin est l'une des technologies les plus utilisées parmi les [programmeurs Android en Inde](https://www.valuecoders.com/hire-developers/hire-android-developers?utm_source=freecodecamp&utm_medium=hire%2Bandroid%2Bdeveloper_rg&utm_campaign=website), et cette fonctionnalité encouragera probablement son adoption pour un développement d'applications plus rapide à l'avenir.

### 7. Dernier éditeur pour les règles R8

R8 a été introduit dans le plugin Android Gradle 3.4.0 pour combiner la réduction, le désucriage, la dexing et l'obfuscation en une seule étape. Cela a permis d'améliorer les performances de construction.

Auparavant, il n'y avait pas de support pour un éditeur intelligent qui offrait des suggestions automatiques lors de l'écriture des règles R8. Mais avec Android Studio 4.0, un éditeur intelligent peut écrire les règles pour la réduction de code.

Lors du développement de fichiers de règles pour R8, Android Studio offre désormais diverses fonctionnalités, y compris la complétion, la coloration syntaxique et la vérification des erreurs.

Cet éditeur fonctionne en douceur avec votre projet pour offrir une complétion complète des symboles pour tous les modèles, classes et champs, et inclut également le refactoring et la navigation.

![Image](https://lh6.googleusercontent.com/6GkRn5PchI3-pblXj1xTrVive131J_4A1-CWlNlNLa0nCOhb9ZmmXiJdWmBKgHSdaGK3JfUApKFelO8wbEGdcl_u_4gyOi64VwrZZbFdKdWKJf7U5do2VhDBmD86ukOng6_Yu_oV)
_[**Source de l'image**](https://miro.medium.com/max/711/1*fzTTnrKnVuVpO0H_eWnWmQ.png)_

### 8. Assistants de fragment

![Image](https://lh3.googleusercontent.com/82lsSjJI0AJhHUjW0UDWg9vEp4b4grDfh4Xfrsei4OrT9eEloifBFvCni_OpH4qhoh77aXpc23STWWpGog4LtpFgdglKJyOGyUzNSpb1PS3PGLebdWYw7tkPnrw-L9qQM56IvI5t)
_[**Source de l'image**](https://stackoverflow.com/questions/37432212/android-wizard-with-multiple-fragments-back-button-behavior)_

De nouveaux modèles de fragments et des assistants de fragments sont désormais disponibles dans l'éditeur de navigation.

Ces modèles permettent aux développeurs de naviguer rapidement dans le contenu de l'assistant de fragment pour créer des diaporamas en utilisant **ViewPager** (qui est disponible dans la bibliothèque de support). Cet outil vous permet de configurer facilement l'animation de diapositive et améliore l'apparence et la convivialité de l'application.

Ces mises à jour ont facilité l'implémentation par les développeurs d'un diaporama d'écran par défaut animé grâce à des modèles simples de glisser-déposer disponibles dans l'éditeur de navigation. Et il y a moins de codage impliqué également.

En gros, Fragment est une classe dans Android qui permet l'intégration d'une interface utilisateur adaptable à différentes orientations d'écran de l'appareil. Il combine différents types de segments en un seul élément d'écran.

L'introduction de modèles dans l'Assistant de fragment rend l'utilisation de ces différentes fonctionnalités assez sans effort. Et c'est définitivement un bonus lorsque l'interface utilisateur de votre application mobile s'adapte à différentes tailles et orientations d'écran.

### 9. Modèles en direct Kotlin Android

![Image](https://lh3.googleusercontent.com/Fp4myIQSWXL9PR8S706CmBWUwc7w2un7Yp3fPL6LUYQp2pmiFdYYeMgXf4fTn_TOfNHqrQxRk4SnBf-k3-R9xC5VBKvl1EZLe0hw2SpIOGmTXu8skKiNdpSH3V0uMeCPFOFQwPU5)
_[**Source de l'image**](https://stackoverflow.com/questions/51473637/how-to-create-a-kotlin-live-template-for-newinstance-fragments-using-android-stu)_

La dernière version d'Android Studio prend en charge les fichiers de script **Kotlin DSL**. Vous pouvez facilement utiliser la suite complète de corrections rapides prises en charge par la boîte de dialogue de structure de projet. Android Studio dispose désormais de modèles en direct spécifiques à Android pour le code Kotlin.

Par exemple, tapez simplement **« toast »** et appuyez sur la **touche Tab** pour insérer rapidement le code standard pour un Toast.

Pour une liste complète des modèles en direct, accédez à **Éditeur > Modèles en direct** dans la boîte de dialogue des paramètres (ou préférences).

### 10. Mises à niveau de l'interface utilisateur du profileur CPU

![Image](https://lh6.googleusercontent.com/L3ENpbiZj0xq8XtsuSe_3yi91WXYvkxmkO4O7XtADPvDmmTuebvFqKO7Su5-_CT09MiNk8f703tCIDpmwrKUqETbE1TS7C-rLai7g0LZNi1p9NfyT2dCkKTBQrJVzilB5Clkdw8h)
_[**Source de l'image**](https://developer.android.com/studio/profile/cpu-profiler.html?hl=lt)_

Les profileurs CPU sont l'une des meilleures nouvelles fonctionnalités d'Android Studio, surtout en matière de performance. Le profileur CPU est conçu pour vous donner des informations liées à l'enregistrement des traces et à l'activité des threads de votre application.

Auparavant, toutes les données des profileurs étaient affichées sous une seule section :

![Image](https://lh3.googleusercontent.com/7BAmmJFUBcUgNEc4RNpg6iEEdZHg3P9svGM-EqwT8cb1tcBOIpMlI5eL_aksD0aSlRIKKxbt8MbeWuetlFukOJxus9WAlCHXEu2JfxHGwkw604lmlHXUFF1mzQqNhFMmL4r3QC7O)
_[**Source de l'image**](https://miro.medium.com/max/788/1*4IDJaeUhsraqzeqc9Mynrg.png)_

Avec Android Studio 4.0, les enregistrements CPU peuvent être mis de côté par rapport à la timeline principale du profileur et gérés en groupes pour permettre une analyse plus facile. Les développeurs peuvent facilement glisser-déposer et déplacer des groupes vers le haut et vers le bas des éléments individuels au sein d'un groupe pour une personnalisation supplémentaire.

De plus, pour une analyse côte à côte fluide, vous pouvez inspecter toute l'activité des threads dans la timeline d'activité des threads (y compris les fonctions, méthodes et événements) et essayer les derniers raccourcis de navigation pour vous déplacer dans les données.

L'interface utilisateur de la trace système a également été mise à niveau afin que les événements puissent être colorés de manière unique pour des distinctions visuelles améliorées. Les threads peuvent également être triés pour faire ressortir les plus occupés en fonction de la priorité, et vous pouvez vous concentrer davantage sur la visualisation des données pour uniquement les threads que vous avez sélectionnés plutôt que sur toutes les données combinées.

Pour une description détaillée du profileur CPU, [cliquez ici](https://developer.android.com/studio/releases#cpu-profiler-upgrades).

### 11. Dépendances de fonctionnalité sur fonctionnalité

![Image](https://lh6.googleusercontent.com/BHSx1Ets1xQMFDaqXAop0cfNXOZ9_iQVOlXHGOurDGDTHcuzg_YFHEzAX-FgPmxaZIC2vAVl3q2y0-q4AU5ZUFZwkyRHqS7-QPwK-p_SxI_pTuqRk1kDi13RDS7PzDONG3KhGYeb)
_[**Source de l'image**](https://android-developers.googleblog.com/2020/05/android-studio-4.html)_

Android Studio 4.0 permet aux développeurs de désigner quel module de fonctionnalité dynamique dépend d'un autre module de fonctionnalité. En déployant cela, vous pouvez vérifier si l'application dispose de modules suffisants pour améliorer la fonctionnalité de vos applications.

Par exemple, si un utilisateur enregistre une vidéo, le module informatique est automatiquement téléchargé. Cela est dû au fait que le module vidéo dépend du module caméra.

## Conclusion

Ce sont les fonctionnalités d'Android Studio 4.0 qui aideront vraiment à améliorer les performances de vos applications Android. Elles aideront également les développeurs d'applications Android à coder plus rapidement et plus efficacement.

Actuellement, la création d'applications Android est un intérêt d'investissement majeur parmi les entrepreneurs et les entreprises.

Ainsi, il y a une énorme concurrence parmi les entreprises pour choisir une [société de développement d'applications Android](https://www.pixelcrayons.com/mobile-app-development/android-development?utm_source=freecodecamp&utm_medium=android%2Bapp%2Bdevelopment_sk&utm_campaign=website) qui est à jour sur les verticales technologiques modernes et qui peut créer des produits précieux.

Le lancement d'Android 4.0 rendra les choses beaucoup plus faciles et plus intéressantes pour tout le monde.