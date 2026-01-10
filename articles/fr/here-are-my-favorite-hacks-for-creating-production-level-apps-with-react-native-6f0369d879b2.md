---
title: Voici mes astuces préférées pour créer des applications de niveau production
  avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-18T21:57:29.000Z'
originalURL: https://freecodecamp.org/news/here-are-my-favorite-hacks-for-creating-production-level-apps-with-react-native-6f0369d879b2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VCJ_bcWjUGSK19znF1KMwg.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: technology
  slug: technology
- name: tips
  slug: tips
seo_title: Voici mes astuces préférées pour créer des applications de niveau production
  avec React Native
seo_desc: 'By Mehul Mohan

  Trust me when I say this, React Native is hard. And it’s not the usual hard of what
  we think hard is. It is hard in terms of working with in general. In this blog post,
  I’ll go over some tips and tricks and eventually the best practice...'
---

Par Mehul Mohan

Croyez-moi quand je dis cela, React Native est difficile. Et ce n'est pas le genre de difficulté auquel nous pensons habituellement. C'est difficile en termes de travail en général. Dans cet article de blog, je vais passer en revue quelques conseils et astuces, et finalement les meilleures pratiques que j'ai déployées pour l'une de mes applications codées en React Native : [codedamn Android](http://play.google.com/store/apps/details?id=com.codedamn) (ou [codedamn iOS](https://itunes.apple.com/us/app/codedamn/id1426709377)).

Salut ! Je m'appelle Mehul. Je suis étudiant, [youtuber](https://youtube.com/c/codedamn), [développeur fullstack](https://stackoverflow.com/users/2513722/mehulmpt), développeur d'applications et je peux également déployer des serveurs. Récemment, j'ai décidé de lancer une plateforme axée sur les développeurs (vous l'avez deviné, codedamn). Pour la lancer rapidement sur les appareils mobiles, j'ai choisi React Native. Partiellement parce que je ne suis pas un grand fan de Swift et Xcode pour l'instant. Mais je ne savais pas que j'interagirais plus avec le code natif que je ne le pensais. Dans tous les cas, commençons avec les informations que je veux mentionner.

_Note : Au moment de la rédaction de cet article, React Native était à la version v0.57-rc4. Vérifiez si certaines des choses sont déjà disponibles/corrigées dans la version récente de React Native !_

### #0 : Sachez ce que vous faites

Réalisez que le monde de React Native est un monde solitaire en ce moment. Vous pourriez vous retrouver avec un problème que personne n'a encore rencontré (ou vous n'êtes pas capable de le googler correctement). Gardez toujours votre VCS à jour avec votre projet natif et commitez régulièrement vos changements (tous les enfants cool appellent cela CI). Cela vous aide à revenir à la dernière copie fonctionnelle assez rapidement sans perdre beaucoup de code.

Il est tout aussi important de savoir ce que vous faites. Vous pourriez finir par casser complètement votre projet si vous n'êtes pas conscient. Si vous n'avez pas utilisé de VCS, alors vous êtes dans le pétrin.

### #1 : Mettez à niveau votre JSC

JSC (JavaScriptCore) est un moteur JavaScript basé sur webkit utilisé par React Native sur les plateformes Android pour évaluer votre code JavaScript. Ne me dites pas que vous pensiez que React Native convertit JavaScript en code natif. Ce n'est pas le cas ! ;-)

Tout JS que vous écrivez est toujours exécuté en tant que JavaScript uniquement par JSC sur Android. Le problème est que React Native est livré avec une version très ancienne de JSC. Cela signifie que vous devez utiliser des transformations babel de manière extensive. Parfois, il y a des bugs si méchants que vous vous arracherez les cheveux à chaque fois que vous vous asseyez pour coder, à cause d'une ancienne version de JSC.

Je l'ai appris à la dure après avoir gaspillé une journée de débogage. Il y avait une erreur fatale aléatoire inconnue pendant l'exécution de l'application. Après avoir étudié les logs pendant un certain temps, je suis arrivé à la conclusion que l'application plantait quelque part où [Symbol.iterator] est utilisé dans le code JS transpilé par babel.

Maintenant, les Symboles sont une chose ES6. Babel ne l'a pas transpilé plus loin, et JSC était si ancien qu'il n'était pas capable de supporter des choses simples comme celles-ci et a planté. J'ai gaspillé presque une journée à essayer de comprendre que la mise à niveau de JSC était une meilleure solution que d'autres hacks de fortune.

La mise à niveau de votre JSC est assez simple. Suivez ce [dépôt github](https://github.com/react-community/jsc-android-buildscripts) et vous devriez être opérationnel en un rien de temps.

### #2 : Configurez Redux correctement

Redux peut être un casse-tête à configurer correctement. Et par le configurer correctement, je veux dire l'intégrer profondément avec votre application. Qu'il s'agisse de vos propres reducers ou de la navigation React. Configurer la navigation react avec Redux est une excellente décision pour le long terme même si la page de navigation React donne un avertissement à ce sujet :

![Image](https://cdn-media-1.freecodecamp.org/images/ItiPqHDhW9zo-NBMXZkcy0CW2UvMXmrAyw18)

Pas du tout. Nous parlons d'applications de niveau entreprise et de production ici. Allez-y et stockez votre état de navigation dans Redux et obtenez un contrôle très fin sur votre état.

Mais rappelez-vous, avec un grand pouvoir vient une grande responsabilité. Avec un tel contrôle fin sur votre navigation, assurez-vous de la configurer correctement. Sinon, votre application plantera aléatoirement. Ce sera un casse-tête à configurer initialement, mais croyez-moi, cela en vaut la peine.

Lisez à propos de Redux et de son intégration avec [react navigation ici](https://reactnavigation.org/docs/en/redux-integration.html).

### #3 : Utilisez les outils d'automatisation disponibles comme fastlane

Fastlane est un excellent utilitaire en ligne de commande pour automatiser de nombreuses tâches courantes que vous rencontrerez. C'est plus une optimisation du temps qu'une optimisation du code. Je pense qu'il mérite une place ici parce qu'il économise beaucoup de temps une fois configuré correctement.

Découvrez fastlane ici : [https://fastlane.tools/](https://fastlane.tools/)

### #4 : Faites la gestion des erreurs correctement

N'attendez pas de vos utilisateurs qu'ils vous pingent avec exactement comment l'application plante. Avec des applications plus complexes, il est difficile de trouver des étapes spécifiques qui mènent au plantage de l'application. J'utilise sentry.io pour la gestion des erreurs sur mes applications, et je l'aime personnellement beaucoup. Il peut s'intégrer dans vos étapes de construction et même télécharger la sourcemap sur leurs serveurs afin que vous puissiez voir le code réel, et non des déchets aléatoires dans vos traces de plantage.

Sentry est disponible à l'adresse [https://sentry.io/](https://sentry.io/)

### #5 : Faites le débogage de la bonne manière !

Utilisez-vous toujours cette console d'inspection chrome fantaisiste pour déboguer vos applications React Native ? Et qu'en est-il de Redux ? Un autre onglet ? Que faire si vous voulez effacer le stockage asynchrone de votre application ? Forcer l'arrêt de l'application et effacer les données ? Cela semble trop fastidieux, surtout lorsque vous développez activement l'application. Au lieu de cela, utilisez un débogueur dédié autonome pour react native. La meilleure partie ? C'est gratuit !

Voici votre débogueur React Native : [https://github.com/jhen0409/react-native-debugger](https://github.com/jhen0409/react-native-debugger)

### 5 conseils rapides :

* Gardez votre structure de fichiers organisée. C'est très important pour mettre à l'échelle votre application.
* Évitez d'utiliser expo pour vos applications. S'IL VOUS PLAÎT NON. Même si vous l'utilisez, vous réaliserez que vous DEVEZ éjecter à un moment donné, et ensuite bonne chance pour comprendre tout le bordel. Ce n'est pas impossible, cela prendra beaucoup de votre temps plus tard. Rappelez-vous, expo est bien mais nous parlons d'applications liées à des entreprises/démarrages à long terme et non d'une application d'âge de chat (pour laquelle expo serait bien).
* ASSUREZ-VOUS de créer un fichier package-lock.json (si vous utilisez npm). Vous le regretterez grandement plus tard lorsque vous supprimerez accidentellement votre dossier node_modules et réaliserez qu'aucun package sur npm ne se soucie de la version sémantique.
* N'utilisez pas de bibliothèques UI très lourdes avec React Native. Cela ralentit les performances même en production. Je ne recommande pas [NativeBase](https://nativebase.io/) pour l'instant, même si cela semble très fantaisiste en termes d'UI. C'est coûteux en performances. Il existe de bien meilleures options disponibles comme [react native paper](https://github.com/callstack/react-native-paper).
Merci à [Andre Biel](https://www.freecodecamp.org/news/here-are-my-favorite-hacks-for-creating-production-level-apps-with-react-native-6f0369d879b2/undefined) pour le commentaire, assurez-vous de passer en revue cette page de documentation en profondeur si vous en avez assez des applications RN lentes et/ou de leur profilage. C'est une mine d'or : [https://facebook.github.io/react-native/docs/performance.html](https://facebook.github.io/react-native/docs/performance.html)
* Tirez parti du remplacement du bundle JS de React Native à la volée sans avoir à resoumettre l'application aux magasins d'applications en utilisant des technologies comme [CodePush](https://microsoft.github.io/code-push/).
* Familiarisez-vous avec au moins les bases du code natif sur les deux plateformes. Surtout les fichiers de construction sur Android et les fichiers pod sur iOS. Ce sont des fichiers sur lesquels vous passerez la plupart de votre temps à travailler sur le natif.

Je continuerai à écrire des articles de blog sur React Native dans une série de posts, peut-être, voyons voir !

### Questions ?

Posez-les dans les commentaires ci-dessous ! Je serai heureux de vous aider.

**_Petite publicité éhontée :_** _Si vous commencez avec React Native, voici mon cours à 95 % de réduction sur la façon de commencer avec : [React Native — Les Premières Étapes](http://bit.ly/rn-basics-medium)_