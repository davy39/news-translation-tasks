---
title: La manière la plus simple de mettre à niveau React Native vers la dernière
  version
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-21T10:15:15.000Z'
originalURL: https://freecodecamp.org/news/easiest-way-to-upgrade-react-native-to-the-latest-version-daecd284cb18
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ytrkryPcES23LiO1srdSvg.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La manière la plus simple de mettre à niveau React Native vers la dernière
  version
seo_desc: 'By Sam Johnson

  I’ve read many horror stories from people who have spent days trying to upgrade
  React-Native to the latest version. The official guideline as mentioned here do
  not work in most cases.

  Below is the way I found out after so many trials a...'
---

Par Sam Johnson

J'ai lu de nombreuses histoires d'horreur de personnes qui ont passé des jours à essayer de mettre à niveau React-Native vers la dernière version. Les directives officielles mentionnées [ici](https://facebook.github.io/react-native/docs/upgrading) ne fonctionnent pas dans la plupart des cas.

Voici la méthode que j'ai découverte après de nombreux essais et erreurs pour être la plus simple.

Il existe un outil merveilleux nommé [**_rn-diff-purge_**](https://github.com/pvinis/rn-diff-purge) (ne vous laissez pas tromper par le nom, il ne fera aucun type de purge ?). Ce que fait cet outil, c'est comparer différentes versions de react-native et vous montrer les différences au niveau du code source. En voyant les différences, vous pouvez apporter les modifications nécessaires à la construction. Cela dépend du nombre de bibliothèques que vous utilisez, mais la construction initiale pourrait réussir du premier coup ou montrer quelques erreurs. Ensuite, vous pouvez travailler sur ces erreurs une par une.

![Image](https://cdn-media-1.freecodecamp.org/images/1X3qYpeOtjUhf3F4Tt0lHZRtEZcF-RaTqfFm)

J'ai utilisé l'outil pour mettre à niveau react-native trois fois jusqu'à présent, et cela m'a pris de 30 minutes à 1 heure pour terminer la mise à niveau.

Voici les étapes que je suis à chaque fois que je décide de faire une mise à niveau :

* Assurez-vous que votre base de code est en bon état, ce qui signifie que vous avez résolu tous les problèmes connus.
* Assurez-vous d'avoir validé toutes vos modifications :

```
git add . git commit -m "Dernier commit avant la mise à niveau vers la version RN 0.59.0" git push
```

* Copiez et collez ceci dans votre navigateur : [https://github.com/pvinis/rn-diff-purge/compare/version/0.58.6..version/0.59.0](https://github.com/pvinis/rn-diff-purge/compare/version/0.58.6..version/0.59.0)
* Appliquez manuellement les modifications selon les différences affichées.
* Exécutez npm i pour mettre à jour les versions
* Construisez et déployez via Android Studio et Xcode

Si aucune erreur n'est affichée, commencez vos tests unitaires.

Si des erreurs sont affichées, elles sont plus susceptibles d'être dues aux bibliothèques que vous utilisez. Si c'est le cas, allez sur le dépôt github de la bibliothèque qui donne l'erreur.

Par exemple, lorsque j'ai mis à niveau React-Native de 0.58.6 à 0.59.0, une bibliothèque que j'utilisais ("lottie-react-native") m'a donné des erreurs de compilation sous Android Studio. Je suis donc allé sur leur site github et j'ai trouvé [ce problème](https://github.com/react-native-community/lottie-react-native/issues/453). Ensuite, j'ai suivi les instructions mentionnées là-bas pour résoudre le problème.

Vous rencontrerez certainement de nombreux problèmes, mais la plupart des problèmes (sinon tous) que j'ai rencontrés jusqu'à présent sont causés par les bibliothèques que j'ai utilisées, et non par React-Native lui-même.

Lorsque vous êtes satisfait de toutes les modifications, exécutez `git diff` pour voir les changements, puis `git add .` `git commit -m "Mise à niveau complète de React Native"` `git push`.

Félicitations ! Vous êtes prêt à utiliser les dernières fonctionnalités fournies par les dernières versions de React-Native.

Note : certains problèmes n'ont pas de solutions immédiates (ce qui peut nécessiter une nouvelle version des bibliothèques elles-mêmes). Mais la bonne nouvelle est que tous les problèmes auront une sorte de solution de contournement. ?