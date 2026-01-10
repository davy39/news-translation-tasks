---
title: Pourquoi vos notifications push ne voient jamais le jour
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-28T18:55:46.000Z'
originalURL: https://freecodecamp.org/news/why-your-push-notifications-never-see-the-light-of-day-3fa297520793
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1KfeXO-IedHQ9cUI83cV3g.jpeg
tags:
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: Firebase
  slug: firebase
- name: mobile app development
  slug: mobile-app-development
- name: push notification
  slug: push-notification
seo_title: Pourquoi vos notifications push ne voient jamais le jour
seo_desc: 'By Neil Mathew

  Push Notifications fail on specific Android phones. Here’s why.

  I recently added support for Push Notifications in the Kayako App. I tested and
  shipped it. And I thought I did pretty good job.

  But then one by one, my users start commen...'
---

Par Neil Mathew

#### Les notifications push échouent sur certains téléphones Android. Voici pourquoi.

J'ai récemment ajouté la prise en charge des [notifications push](https://firebase.google.com/docs/cloud-messaging/) dans l'[application Kayako](https://play.google.com/store/apps/details?id=com.kayako.android.k5). Je l'ai testée et déployée. Et je pensais avoir fait un bon travail.

Mais ensuite, un par un, mes utilisateurs ont commencé à commenter que l'application n'affichait aucune notification environ 95 % du temps. Au début, j'ai pensé que c'était une erreur car les notifications push fonctionnaient comme prévu sur mon émulateur et mes appareils. Mais en creusant plus profondément, il est devenu clair à quel point ce problème était sérieux et valide. Ce n'était que la partie émergée de l'iceberg. Près de 50 % de nos utilisateurs de l'application Android étaient affectés, mais seuls quelques-uns nous en ont informés.

### Alors, quel est le problème ?

Les notifications push ne fonctionnent **pas** correctement sur certains téléphones Android.

J'utilise le mot « correctement » car les utilisateurs reçoivent des notifications push lorsque l'application est ouverte, mais [pas lorsqu'elle est fermée](https://github.com/firebase/quickstart-android/issues/41), ce qui va à l'encontre du but des notifications push.

J'utilise les mots « certains téléphones Android » car ce problème est remarqué uniquement sur les téléphones de fabricants comme Xiaomi, Oppo, One Plus, Vivo, Lenovo, Huawei, Samsung, et quelques autres.

### Pourquoi cela se produit-il et comment le corriger ?

Pour comprendre le problème, comprenons d'abord l'interface utilisateur Android et le comportement attendu des notifications push.

Sur Android, nous avons trois boutons en bas faisant partie de la barre de navigation. Le bouton carré, lorsqu'on clique dessus, ouvre l'écran **Récent**. L'écran **Récent** liste toutes les tâches en cours ou les applications récemment ouvertes. Nous pouvons effacer ces applications à tout moment, comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/VMda4Y0jAqWe3uv5jqChb4HzarB7g2ffPjU0)
_Écran Récent_

Pourtant, sur certains [ROMs stock](https://www.xda-developers.com/what-is-custom-rom-android/) (système d'exploitation Android personnalisé par les fabricants de dispositifs), effacer une application tue cette application et ses services en arrière-plan. Cela est mauvais car nous avons besoin de services en arrière-plan pour afficher les notifications push.

Lorsque le serveur informe l'appareil Android d'une nouvelle notification push, il redémarrerait normalement les services en arrière-plan de l'application pour afficher la notification à l'utilisateur. C'est bien car les services en arrière-plan démarreront automatiquement pour afficher les notifications push.

L'image ci-dessous montre le comportement attendu, qui est le cas pour les ROMs vanilla. Il s'agit du firmware Android original qui n'est pas personnalisé par les fabricants.

![Image](https://cdn-media-1.freecodecamp.org/images/vsgpo013XZS9sWzJO4yXmsRyZ7O8TsP8QinG)
_Comportement attendu des notifications push_

Pourtant, malgré cela, certains téléphones Android utilisant l'application Kayako ne **reçoivent pas** de notifications push lorsque l'application est effacée de l'écran **Récent**. La raison est que les fabricants de téléphones comme Oppo, Xiaomi et One Plus utilisent un ROM stock qui désactive le redémarrage des services en arrière-plan pour la plupart des applications. Cela est mauvais car nous sommes revenus à la case départ sans moyen d'afficher les notifications push.

Heureusement, ces ROMs stock ont une page de paramètres pour activer le redémarrage des services en arrière-plan. Bien que le démarrage automatique des services en arrière-plan soit désactivé par défaut, les utilisateurs peuvent activer manuellement cette fonctionnalité en suivant certaines instructions. C'est bien car maintenant les services en arrière-plan peuvent être démarrés automatiquement pour afficher les notifications push. Mais c'est une solution peu élégante car elle implique un travail manuel que l'utilisateur doit effectuer.

Les intentions des fabricants sont de préserver la batterie et d'améliorer les performances. Les utilisateurs de l'application doivent maintenant ouvrir leur application de paramètres, naviguer jusqu'à la page correcte, faire défiler une liste d'applications, puis activer la fonctionnalité pour l'application Kayako.

#### Mais attendez, pourquoi des applications comme Gmail et Slack n'ont-elles pas ces problèmes ?

Les applications les plus populaires comme Gmail, Slack et Whatsapp sont sur liste blanche par ces ROMs stock. Cela signifie que ces applications ont le démarrage automatique activé par défaut pour elles.

Cependant, notre application, ainsi que beaucoup d'autres, ont le démarrage automatique désactivé par défaut.

![Image](https://cdn-media-1.freecodecamp.org/images/m-OlwUJt4m7rnaN84273MxOWR5viXIcDORZr)
_Page des paramètres 'Apps auto-launch' de One Plus_

#### Je ne trouve pas les paramètres pour activer le démarrage automatique. Où sont-ils situés ?

Les étapes pour activer le démarrage automatique pour une application sont différentes pour chaque fabricant. Cela est dû au fait que ce n'est pas une fonctionnalité native d'Android et est très spécifique aux ROMs stock.

Il convient également de noter que la terminologie utilisée par chaque fabricant est différente. La fonctionnalité de démarrage automatique peut être appelée démarrage automatique de l'application, gestionnaire de démarrage, gestionnaire de démarrage automatique, optimisation de l'application, applications protégées ou gestion des applications en arrière-plan.

Pour compliquer les choses, la page des paramètres de démarrage automatique n'est pas facile à trouver. Pour les appareils One Plus (utilisant [Nougat](https://www.android.com/versions/nougat-7-0/) ou une version antérieure), vous devez ouvrir les Paramètres, cliquer sur Apps, puis sur l'icône d'engrenage située sur la barre d'outils, puis sur Apps Auto-launch sous la sous-catégorie Avancé tout en bas.

### D'accord, quelle est la solution ?

En fin de compte, l'utilisateur devra effectuer les étapes manuellement. Cela ne peut pas être activé programmatiquement pour tous les appareils. Le mieux que nous puissions faire est de rendre cela aussi facile que possible pour les utilisateurs de l'application.

#### Créer un article de support

[Kelly O'Brien](https://www.freecodecamp.org/news/why-your-push-notifications-never-see-the-light-of-day-3fa297520793/undefined) et moi avons écrit un article qui tente d'identifier tous les fabricants de dispositifs ayant ce problème et explique les étapes pour activer les notifications push sur ces dispositifs. Vous pouvez le lire [ici](https://support.kayako.com/article/1461-why-aren-t-push-notifications-working-on-my-android-app).

#### Informer les utilisateurs dans l'application

Comme je l'ai mentionné précédemment, tout le monde ne prend pas le temps de se plaindre. Je ne peux pas m'attendre à ce que les utilisateurs contactent l'équipe de support ou recherchent l'article de support en ligne. En même temps, il n'y a pas de moyen facile d'identifier automatiquement si les notifications push ne fonctionnent pas lorsque l'application est fermée.

J'ai décidé d'afficher un petit pied de page sur la page des paramètres des notifications push où l'article est disponible pour l'utilisateur à tout moment.

![Image](https://cdn-media-1.freecodecamp.org/images/t1U0ZBIa3qJG1hvdU1lQT9GO4tJg3N0q5JUY)
_Page des paramètres des notifications push_

#### Ouvrir la page des paramètres concernée dans l'application

J'ai trouvé de nombreuses réponses sur Stack Overflow comme [celle-ci](https://stackoverflow.com/questions/34149198/how-to-enable-auto-start-for-my-app-in-xiaomi-programmatically) qui recommandent d'ouvrir programmatiquement la page des paramètres concernée en détectant le fabricant de votre appareil. Bien que j'aime l'idée, je ne l'ai pas implémentée. Je n'ai pas eu l'occasion de tester si le code spécifique à l'appareil fonctionne réellement, ce qui me met mal à l'aise.

Si vous avez d'autres suggestions ou idées, je les accueille avec plaisir.