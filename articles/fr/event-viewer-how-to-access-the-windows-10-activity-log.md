---
title: Visionneuse d'événements – Comment accéder au journal d'activité de Windows
  10
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-10-19T16:33:26.000Z'
originalURL: https://freecodecamp.org/news/event-viewer-how-to-access-the-windows-10-activity-log
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/eventViewer-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Windows 10
  slug: windows-10
seo_title: Visionneuse d'événements – Comment accéder au journal d'activité de Windows
  10
seo_desc: 'The Windows 10 Event Viewer is an app that shows a log detailing information
  about significant events on your computer. This information includes automatically
  downloaded updates, errors, and warnings.

  In this article, you''ll learn what the event vie...'
---

La Visionneuse d'événements de Windows 10 est une application qui affiche un journal détaillant les informations sur les événements significatifs de votre ordinateur. Ces informations incluent les mises à jour téléchargées automatiquement, les erreurs et les avertissements.

Dans cet article, vous apprendrez ce qu'est la visionneuse d'événements, les différents journaux qu'elle contient et, surtout, comment y accéder sur un ordinateur Windows 10.

## Qu'est-ce que la Visionneuse d'événements ?

Chaque programme que vous ouvrez sur votre ordinateur Windows 10 envoie une notification à un journal d'activité particulier dans la Visionneuse d'événements.

Toutes les autres activités telles que les changements du système d'exploitation, les mises à jour de sécurité, les anomalies des pilotes, les défaillances matérielles, etc., sont également enregistrées dans un journal particulier. Vous pouvez donc considérer la visionneuse d'événements comme une base de données qui enregistre chaque activité de votre ordinateur.

Avec la visionneuse d'événements, vous pouvez résoudre différents problèmes de Windows et d'applications.

Si vous explorez la visionneuse d'événements en profondeur, vous verrez différentes informations, avertissements et de nombreuses erreurs. Ne paniquez pas – c'est normal. Même les ordinateurs les mieux entretenus montrent de nombreuses erreurs et avertissements.

## Comment accéder au journal d'activité de Windows 10

Il existe 3 principales façons d'accéder à la visionneuse d'événements sur Windows 10 – via le menu Démarrer, la boîte de dialogue Exécuter et la ligne de commande.

### Comment accéder au journal d'activité de Windows 10 via le menu Démarrer

**Étape 1** : Cliquez sur Démarrer ou appuyez sur la touche WIN (Windows) de votre clavier
**Étape 2** : Recherchez « Visionneuse d'événements »
**Étape 3** : Cliquez sur le premier résultat de recherche ou appuyez sur `ENTRÉE`
![ss-1-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-1-5.jpg)

Vous serez accueilli avec cette page :
![ss-2-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-2-1.png)

### Comment accéder au journal d'activité de Windows 10 via la boîte de dialogue Exécuter

**Étape 1** : Cliquez avec le bouton droit sur Démarrer (logo Windows) et sélectionnez « Exécuter », ou appuyez sur `WIN` (touche Windows) + `R` sur votre clavier
![ss-3-4](https://www.freecodecamp.org/news/content/images/2021/10/ss-3-4.jpg)

**Étape 2** : Tapez « eventvwr » dans l'éditeur et cliquez sur « OK » ou appuyez sur `ENTRÉE`
![ss-4-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-4-5.jpg)
![ss-5-5](https://www.freecodecamp.org/news/content/images/2021/10/ss-5-5.png)

### Comment accéder au journal d'activité de Windows 10 via l'invite de commande

**Étape 1** : Cliquez sur Démarrer (logo Windows) et recherchez « cmd »
**Étape 2** : Appuyez sur Entrée ou cliquez sur le premier résultat de recherche (devrait être l'invite de commande) pour lancer l'invite de commande
![ss-6-3](https://www.freecodecamp.org/news/content/images/2021/10/ss-6-3.jpg)

**Étape 3** : Tapez « eventvwr » et appuyez sur `ENTRÉE`
![ss-7-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-7-2.png)
![ss-8-2](https://www.freecodecamp.org/news/content/images/2021/10/ss-8-2.png)

## Journaux d'activité de la Visionneuse d'événements

Lorsque vous ouvrez la visionneuse d'événements pour voir les journaux d'activité de votre ordinateur, vous êtes automatiquement dirigé vers l'onglet Visionneuse d'événements (Local). Mais cela peut ne pas contenir les détails dont vous avez besoin, car ce n'est qu'une page d'accueil lorsque vous ouvrez la Visionneuse d'événements.

Il y a beaucoup plus à découvrir dans la Visionneuse d'événements.

### Le journal des événements administratifs

Vous pouvez développer l'onglet Vues personnalisées pour voir les événements administratifs de votre ordinateur, comme ceci :
![ss-9](https://www.freecodecamp.org/news/content/images/2021/10/ss-9.png)

### Les journaux d'activité de Windows

Vous pouvez également développer les journaux Windows pour afficher diverses activités telles que :
- Événements d'application : Informations, erreurs et rapports d'avertissement des activités des programmes
![ss-10](https://www.freecodecamp.org/news/content/images/2021/10/ss-10.png)

- Événements de sécurité : Cela montre les résultats de diverses actions de sécurité. Ils sont appelés audits et chacun d'eux peut être un succès ou un échec
![ss-11](https://www.freecodecamp.org/news/content/images/2021/10/ss-11.png)

- Événement d'installation : cela concerne les contrôleurs de domaine, qui sont des serveurs vérifiant les utilisateurs sur les réseaux informatiques. Vous ne devriez pas vous en soucier au quotidien.
![ss-12](https://www.freecodecamp.org/news/content/images/2021/10/ss-12.png)

- Événements système : ce sont des rapports des fichiers système détaillant les erreurs qu'ils ont rencontrées
![ss-13-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-13-1.png)

- Événements transférés : ceux-ci sont envoyés à votre ordinateur depuis d'autres ordinateurs du même réseau. Ils vous aident à suivre les journaux d'événements des autres ordinateurs du même réseau.
![ss-14-1](https://www.freecodecamp.org/news/content/images/2021/10/ss-14-1.png)

De plus, il y a les journaux d'application et de service, qui montrent les activités matérielles et d'Internet Explorer, ainsi que les activités des applications Microsoft Office.

Vous pouvez double-cliquer sur une erreur pour vérifier ses propriétés et rechercher l'ID de l'événement de l'erreur en ligne. Cela peut vous aider à découvrir plus d'informations sur l'erreur afin que vous puissiez la corriger si nécessaire.
![ss-15](https://www.freecodecamp.org/news/content/images/2021/10/ss-15.png)

## Conclusion

Dans cet article, vous avez appris à connaître la Visionneuse d'événements de Windows 10, qui est un outil très puissant que les utilisateurs de Windows devraient savoir utiliser.

Outre la visualisation de divers journaux d'activité, elle vous aide également à être conscient de ce qui se passe sur votre ordinateur.

Merci d'avoir lu. Si vous trouvez cet article utile, veuillez le partager avec vos amis et votre famille.