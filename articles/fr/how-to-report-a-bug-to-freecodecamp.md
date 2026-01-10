---
title: Comment signaler un bug à freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-03T21:07:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-report-a-bug-to-freecodecamp
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-pixabay-144243.jpg
tags:
- name: bugs
  slug: bugs
- name: debugging
  slug: debugging
- name: freeCodeCamp.org
  slug: freecodecamp
- name: GitHub
  slug: github
- name: learn to code
  slug: learn-to-code
seo_title: Comment signaler un bug à freeCodeCamp
seo_desc: 'Thank you for taking the time to report an issue with freeCodeCamp.

  If you think you’ve found a bug on freeCodeCamp, please follow these steps to resolve
  your problem:

  Reset the Code in the Editor

  Try resetting the code in the editor using the reset ...'
---

Merci d'avoir pris le temps de signaler un problème avec freeCodeCamp.

Si vous pensez avoir trouvé un bug sur freeCodeCamp, veuillez suivre ces étapes pour résoudre votre problème :

## Réinitialiser le code dans l'éditeur

Essayez de réinitialiser le code dans l'éditeur en utilisant le bouton de réinitialisation sur la page. Cela résoudra la plupart des problèmes si vous avez modifié du code qui affecte le défi d'une manière ou d'une autre.

La réinitialisation efface le code pour le ramener à son état d'origine tel qu'il était lorsque le défi vous a été présenté pour la première fois.

## Utiliser un clavier de codage ou l'application sur mobile

Essayez de lire cet article sur [Comment utiliser freeCodeCamp sur un téléphone mobile](https://www.freecodecamp.org/news/freecodecamp-mobile/). Ou si vous utilisez un appareil Android, vérifiez si l'[application freeCodeCamp](https://play.google.com/store/apps/details?id=org.freecodecamp&gl=US) possède la fonctionnalité que vous souhaitez utiliser.

## Faire un rafraîchissement forcé

Si la page semble endommagée d'une manière ou d'une autre, essayez de faire un rafraîchissement forcé de la page. Cela mettra à jour tout ancien code qui aurait pu être mis en cache dans votre navigateur.

Si le site web de freeCodeCamp a été récemment déployé et que les problèmes proviennent de cela, cela suffira à le corriger.

### Comment faire un rafraîchissement forcé

Tout en étant sur la page problématique, utilisez la combinaison de touches ci-dessous pour déclencher un rafraîchissement forcé en fonction de votre système d'exploitation :

* Windows : `CTRL + F5`
* Mac/Apple : `Apple + Shift + R ou Command + Shift + R`
* Linux : `F5`

Pour en savoir plus à ce sujet, lisez : [http://refreshyourcache.com/en/cache/](http://refreshyourcache.com/en/cache/)

## Essayez de vider le stockage local de votre navigateur

Supprimer tous vos défis stockés localement résoudra de nombreux problèmes liés au plantage du navigateur sur freeCodeCamp.

### Dans Chrome :

* Sur freecodecamp.org, ouvrez votre console
* Windows : `Ctrl` + `Shift` + `J`
* Mac OS : `Cmd` + `Opt` + `J`
* Allez dans l'onglet ressources (Chrome).
* Là, cliquez sur le lien "Local Storage" dans la barre de navigation à droite.
* Supprimez toutes les entrées du côté droit, ou exécutez cette commande dans la console de votre navigateur pour effacer toutes les entrées de votre localStorage : `localStorage.clear();`
* Voyez si cela résout votre problème.

### Comment supprimer un seul défi du stockage local

Peut-être que vous ne voulez pas perdre le code des autres défis ou quelque chose comme ça. Cette méthode supprimera uniquement le défi problématique du stockage local de votre navigateur.

#### Dans Chrome :

* Sur **freecodecamp.org**, ouvrez vos outils de développement.
* Plus d'outils > Outils de développement (ou `Ctrl` + `Shift` + `I` (Windows), `Cmd` + `Opt` + `I` (Mac))
* Naviguez vers l'onglet `Ressources`
* Développez l'élément `Local Storage` dans le volet de gauche
* Sélectionnez `http://www.freecodecamp.org`
* Trouvez le défi pour lequel vous souhaitez supprimer les données dans le volet de droite
* Cliquez avec le bouton droit sur le défi souhaité et sélectionnez `Supprimer`

#### Dans Firefox :

* Sur **freecodecamp.org**, ouvrez votre console web avec
* `Ctrl` + `Shift` + `K`
* À partir de là, en utilisant directement la console :
* Tapez `console.log(localStorage);` et appuyez sur `Entrée`.
* Cliquez sur le lien `Storage`.
* Le panneau **Storage** apparaîtra à droite.
* Filtrez les résultats pour trouver l'algorithme, le projet Front End ou le défi causant le problème.
* Une fois localisé, passez la souris dessus et cliquez sur le `x` à droite.
* Une fois supprimé, vérifiez si le problème était résolu. Rafraîchissez ou fermez et ouvrez le navigateur si nécessaire.

**Note :** Cela peut également être fait avec le [Storage Inspector](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector), mais il semble que Firefox se fige lorsqu'il y a tant de valeurs.

## Vérifiez si le problème est causé par l'une de vos extensions de navigateur

Essayez de désactiver vos extensions de navigateur, ou essayez d'ouvrir la page dans le mode privé de votre navigateur.

Si de cette manière le problème est résolu, vous devrez mettre une exception pour freeCodeCamp dans l'extension coupable, ou la garder désactivée pendant que vous utilisez le site web de freeCodeCamp.

## Lisez les FAQ de support

Les [FAQ de support](https://www.freecodecamp.org/news/support) offrent des solutions pour de nombreux problèmes courants. Essayez de lire cet article si les étapes ci-dessus n'ont pas fonctionné ou n'étaient pas liées à votre problème.

## Demandez de l'aide sur le Forum

Vous êtes peut-être arrivé ici et avez toujours votre problème. Il est maintenant temps de demander de l'aide à d'autres humains.

[Ouvrez un sujet sur le forum décrivant votre problème](http://forum.freecodecamp.com/). Essayez de donner autant d'informations que possible, y compris votre code et le lien du défi, ou le lien vers la page affectée, et votre système d'exploitation (si vous êtes sur un défi, vous pouvez utiliser le bouton "Demander de l'aide" pour créer un post précompilé avec ces problèmes déjà inclus, auquel vous pouvez ajouter votre description du problème et d'éventuelles captures d'écran).

Il peut y avoir quelque chose qui ne va pas avec votre code, ou il peut y avoir un problème de courte durée avec freeCodeCamp en général.

### Comment formater le code sur le Forum

Lorsque vous entrez un bloc de code dans un post sur le forum, précédez-le d'une ligne séparée de trois backticks et suivez-le d'une ligne séparée de trois backticks pour le rendre plus facile à lire.

Vous pouvez également utiliser l'outil "texte préformaté" dans l'éditeur (`</>`) pour ajouter des backticks autour du texte.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Pre-formatted-text.gif)

## Créer un problème sur GitHub

Le forum peut être en mesure de vous aider, ou peut vous envoyer sur GitHub.

Avant de créer un nouveau problème sur GitHub, essayez de rechercher parmi les problèmes existants pour voir si quelqu'un a déjà signalé quelque chose de similaire.

### Comment rechercher un problème sur GitHub

1. Allez sur la page des [problèmes GitHub](https://github.com/FreeCodeCamp/FreeCodeCamp/issues) de freeCodeCamp.
2. Utilisez la barre de recherche pour rechercher des problèmes déjà signalés qui peuvent être liés à votre problème.
3. Si vous en trouvez un, lisez-le ! Vous pouvez vous abonner pour recevoir des mises à jour sur ce problème spécifique en cliquant sur `S'abonner` dans la barre latérale. Vous pouvez ajouter une réaction aux posts qui décrivent le mieux votre problème, ou vous pouvez également commenter le problème si vous avez quelque chose à ajouter.
4. Si vous ne pouvez pas trouver de problèmes pertinents, vous devriez créer un nouveau problème GitHub.

### Comment créer un nouveau problème sur GitHub

**IMPORTANT :**
Avant de signaler un nouveau problème, obtenez toujours une confirmation tierce de quelqu'un dans les salles de chat ou le forum. N'oubliez pas que le suivi des problèmes est strictement réservé à la déclaration de bugs ou d'améliorations, ce n'est pas un endroit pour demander de l'aide pour résoudre les défis.

Rédiger un bon problème facilitera grandement la tâche de l'équipe de développement pour reproduire et résoudre votre problème. Suivez ces étapes pour bien le faire :

* Allez sur la page des [problèmes GitHub](https://github.com/FreeCodeCamp/FreeCodeCamp/issues) de freeCodeCamp et cliquez sur `Nouveau problème`.
* Sélectionnez le type de problème correct dans la liste

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-19.png)

* **Ayez un titre utile.** Rédigez un titre significatif qui décrit le problème. Voici quelques bons exemples : `La connexion depuis les pages News et Field Guide ne redirige pas correctement (en utilisant l'e-mail)` et `Faute de frappe : "for" au lieu de "while" loop` ; les mauvais exemples incluent `Un bug, AIDE!!!11` et `J'ai trouvé ce bug dans un défi`.
* Gardez le titre relativement court, car la description est destinée à des informations supplémentaires. Un exemple est de raccourcir les noms longs des défis, donc au lieu d'écrire `Bug de cas de test dans 'Défis : Vérifier les boutons radio et les cases à cocher par défaut'`, vous pourriez vouloir écrire `Bug de cas de test dans le défi 'Boutons radio'`.
* Dans le corps, **fournissez un lien** vers la page sur laquelle vous avez rencontré ce problème.
* **Décrivez le problème** et **fournissez des étapes** afin qu'un développeur puisse essayer de reproduire le problème. Incluez votre système d'exploitation et la version du navigateur. Lorsque vous référencez d'autres problèmes ou demandes de tirage, écrivez simplement #numéro-du-problème/pr.
* Collez tout code pertinent en utilisant un formatage de code approprié
* **Prenez une capture d'écran** du problème et incluez-la dans le post.
* Cliquez sur `Soumettre un nouveau problème` et vous avez terminé ! Vous serez automatiquement abonné aux notifications pour toute mise à jour ou commentaire futur.

### Comment formater le code sur GitHub

Vous devez utiliser trois backticks ``` avant votre bloc de code, et trois backticks ``` après votre bloc de code.

Vous pouvez également sélectionner votre bloc de code et utiliser le bouton "Ajouter du code" dans l'éditeur GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-11.png)

De cette manière, votre code sera formaté et plus lisible.

Ressources compilées et éditées par Ilenia Magoni, auteure de freeCodeCamp et responsable de la localisation et de la communauté italiennes.