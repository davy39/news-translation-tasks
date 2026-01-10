---
title: iPhone sans bouton Home
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-11T11:20:23.000Z'
originalURL: https://freecodecamp.org/news/homeless-iphone-20c154fabbf7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3MUpCSujRh6EJa321FpCJw.gif
tags:
- name: Apple
  slug: apple
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: iPhone sans bouton Home
seo_desc: 'By Fabrice Dubois

  So, apparently the next iPhone won’t have a physical Home button. There’s been much
  speculation already about what that means for the user. The bottom area of the device,
  for some, will be used to host the navigation bar items, as w...'
---

Par Fabrice Dubois

Donc, apparemment, le prochain iPhone n'aura pas de bouton Home physique. Il y a déjà eu beaucoup de spéculations sur ce que cela signifie pour l'utilisateur. La partie inférieure de l'appareil, [pour certains](http://www.allenpike.com/2017/developing-for-iphone-pro/), sera utilisée pour héberger les éléments de la barre de navigation, ainsi qu'un bouton Home virtuel.

Cet article décrit une autre possibilité.

Certaines découvertes récentes dans du code divulgué peuvent invalider ce que je m'apprête à écrire ci-dessous, mais peu importe.

> **Mise à jour du 28 août** : [Partie 2](https://medium.com/@fab.dubois/homeless-iphone-part-2-1f7b3acc8a6c) de cette histoire est maintenant en ligne.

### Pourquoi un bouton Home ?

Pour résoudre un problème de conception, il est bon de commencer par les bonnes questions. Nous semblons utiliser le bouton Home pour deux raisons dominantes :

* Pour aller à un endroit où nous pouvons choisir une autre application
* Pour "fermer" l'application actuelle parce que nous avons fini avec elle

Bien sûr, plusieurs autres fonctions dépendent également du bouton Home actuel (utilisateurs de Siri, tirez-moi dessus !) mais pour l'instant, permettez-moi de simplifier un peu et de supposer qu'une alternative peut être trouvée pour chaque cas particulier.

Lorsque j'ai essayé la première bêta d'iOS 11 sur iPad, ce qui m'a le plus frappé était le nouveau sélecteur d'applications. Balayer depuis le bord inférieur ne révèle pas seulement le centre de contrôle comme dans les versions précédentes d'iOS ; maintenant, il vient avec le dock des applications favorites et le sélecteur d'applications aussi, tout sur le même écran.

![Image](https://cdn-media-1.freecodecamp.org/images/H6By7-z70NwKo0kES8JxSYHHFf0ZtDyC-VQI)
_Le nouveau sélecteur d'applications sur iPad (à partir d'iOS 11 Beta 5)_

À partir de là, il est intéressant de noter que **taper n'importe où sur l'arrière-plan flou vous ramène instantanément à l'écran d'accueil.** Après un certain temps, j'ai réalisé que je n'appuyais plus autant sur le bouton Home. Le dock avec mes applications favorites, ainsi que la liste des applications récentes, semblaient suffisants pour que je puisse continuer mon flux de travail — au moins la plupart du temps. Et mon besoin subconscient de "fermer" l'application actuelle semblait également comblé.

J'ai commencé à me demander si cette nouvelle interface, déclenchée par un simple balayage, pourrait être l'arme secrète d'Apple pour remplacer définitivement le bouton Home.

Qu'est-ce que cela prendrait pour l'adapter à l'iPhone ? C'est ce que j'ai essayé de faire.

### Le concept

![Image](https://cdn-media-1.freecodecamp.org/images/PoNhJt0KXPx2MSBHZrJoJLasTMfm95DF8-xE)
_Comment le nouveau sélecteur d'applications iPad pourrait fonctionner sur iPhone_

C'est ça. Décomposons le film en clips séparés pour discuter des différents états.

#### **État du dock**

![Image](https://cdn-media-1.freecodecamp.org/images/VKnMdkyuba2ES7TygM8-QHGPNP6DuFbODoNE)
_Le dock est votre cache de niveau 1_

La barre des applications favorites, comme sur iPad et sur macOS, s'appelle Dock et peut être révélée (seule, sans transition vers le sélecteur d'applications complet) par-dessus n'importe quelle application. Il peut même y avoir de la place pour inclure une suggestion supplémentaire dans la partie droite. C'est votre cache de niveau 1 pour passer à votre prochaine application.

#### **État du sélecteur d'applications**

![Image](https://cdn-media-1.freecodecamp.org/images/KkcyVEzydhqHbeTxBlhkn8YMxfo9VwfjaXrf)
_Le sélecteur d'applications est votre cache de niveau 2, plus les contrôles système_

Le cache de niveau 2, auquel vous accédez si vous continuez à balayer vers le haut. Je le surnomme cache de niveau 2 parce qu'il propose plus d'applications que le dock, mais toujours moins que l'écran d'accueil. Ici, l'application actuelle a été "garée" temporairement. Et c'est la clé. C'est essentiellement ce que nous avons en tête lorsque (nous pensons que) nous fermons une application. Je suppose que la plupart des gens sont maintenant conscients que l'application n'est pas tuée, elle est simplement garée. Le concept est cohérent avec celui de l'iPad (je n'ai vraiment rien inventé ici), sauf que la version iPhone utiliserait deux rangées séparées en raison du ratio d'affichage allongé.

#### **Fermer le sélecteur d'applications**

![Image](https://cdn-media-1.freecodecamp.org/images/-9aSL8TXH1u6--oJvoKEMNTe-qytJX1ro0So)
_Fermer le sélecteur d'applications en tapant sur les zones vides (par exemple le bas, ici)_

Ici, la conception repose sur un réflexe commun : si nous ne trouvons pas ce que nous cherchons dans une vue, nous avons tendance à chercher un moyen de sortir de la vue. Et si nous ne trouvons aucune affordance concrète pour sortir, alors nous avons tendance à taper où nous pouvons ! Je simplifie peut-être trop, je l'admets. Mais la sur-simplification est souvent plus gérable que la sur-complication.

Encore une fois, c'est ce que fait l'implémentation iPad de toute façon. Afin de garantir une zone de fermeture confortable en bas, cependant, le dock ne persiste pas dans l'état du sélecteur d'applications (sur iPad, il le fait parce qu'il y a assez de place pour lui). Je ne suis pas trop heureux avec cet aspect, il mériterait d'être affiné.

#### **Ouvrir une application**

![Image](https://cdn-media-1.freecodecamp.org/images/GwZuG4VXdoNecV2Ooj8Ea-Rnlxr0dFCqdKXg)

Une fois l'application ouverte, le dock disparaît afin que l'application puisse tirer le meilleur parti de l'espace disponible, qui est apparemment massif sur le prochain iPhone ; mais comme vous pouvez le voir, il est retiré avec un léger délai. Cela est fait pour améliorer la découvrabilité du sélecteur d'applications. Peut-être excessif, peut-être pas.

Maintenant, discutons des problèmes et des avantages.

### _Problèmes_

La découvrabilité, ainsi que les deux étapes pour aller à l'écran d'accueil, peuvent encore poser problème aux yeux de beaucoup. Personnellement, je trouve cela surprenant de fluidité à utiliser, ayant essayé et ajusté le proto sur un appareil réel, mais j'apprécie que cela puisse ne pas être convaincant au premier abord.

Comment accéder aux autres fonctions dépendant du bouton Home ? Touch ID est fortement attendu pour être remplacé par une méthode d'authentification meilleure, telle que la reconnaissance faciale avancée. Je n'ai pas réfléchi à toutes les solutions de contournement nécessaires — c'est un travail à temps plein — et en effet, c'est problématique. Accessibilité, Siri, capture d'écran : des idées, quelqu'un ?

Le carrousel des applications récentes n'est pas aussi bon que celui existant : il est plus petit. Et le Centre de contrôle n'est pas aussi bon que celui existant non plus : il doit facilement être défilé. C'est le coût de la simplification.

L'approche proposée peut décevoir ceux qui s'attendent à une sorte de barre de fonctions riche en bas, éventuellement sur le modèle de la Touch Bar du Macbook, ou d'autres fonctions profondes qu'Apple voudrait mettre juste sous notre pouce. Mais l'iPhone n'est-il pas déjà une Touch Bar ? Les applications ont toujours pu utiliser le bas de l'écran pour fournir des fonctionnalités contextuelles. Quant aux fonctions système, il y a un endroit raisonnable pour elles : le Centre de contrôle. Donc oui, la solution proposée ici concerne la simplification (au moins en termes de modèle mental), pas l'ajout de fonctions.

### _Avantages_

Tout d'abord, l'élégance de ne pas avoir de bouton Home du tout. C'est plus frappant, plus pur, que de le virtualiser. Supprimer complètement le bouton serait le raffinement ultime.

Les solutions basées sur des superpositions telles qu'un bouton virtuel ont leurs propres problèmes : comment s'assurer que le bouton contrastera bien avec la vue de l'application derrière lui ? Comment gérer les conflits de toucher avec l'application ? Peut-on le déplacer ? etc. S'en débarrasser complètement élimine ces préoccupations.

La métaphore utilisée ici est plus cohérente avec ce qui se passe réellement dans le téléphone : lorsque vous "fermez" une application, ce qui se passe réellement, c'est que vous la poussez en arrière-plan. C'est précisément ce que montre l'interface utilisateur du nouveau sélecteur d'applications. Littéralement : Vous pouvez voir et sentir que vous poussez l'application en arrière-plan.

Aucun impact sur le niveau de l'interface utilisateur de l'application. Les applications restent ignorantes de tout bouton ou de toute barre de fonctions supposée et ne devraient donc pas avoir besoin d'adapter leur comportement ou leur disposition de quelque manière que ce soit. Lorsque qu'une application est mise au premier plan, tout l'espace lui appartient.

La complexité logicielle est maintenue à un niveau bas. Encore une fois, mon expérience réutilise simplement ce qu'ils ont déjà construit pour l'iPad. Nous ne parlons pas d'un autre mécanisme fait uniquement pour le nouvel iPhone. Pour l'utilisateur, cela garantit également un certain niveau de familiarité.

Le design pourrait fonctionner surprenamment bien en mode paysage. La disposition ne tournerait pas ou ne se reconfigurerait pas. Seuls chaque élément individuel tournerait de 90 degrés. Pensez à l'interface utilisateur de la caméra, ce qui tourne et ce qui ne tourne pas, et vous verrez immédiatement ce que je veux dire. La nouvelle grille du Centre de contrôle semble suffisamment flexible pour les rotations d'éléments requises. Et puisque nous balayerions toujours vers le haut depuis le bas, le dock apparaîtrait toujours en bas, mais avec une telle largeur massive, j'imagine qu'il pourrait offrir beaucoup de suggestions d'applications supplémentaires.

![Image](https://cdn-media-1.freecodecamp.org/images/8gJh9e7cJdn1Ih56Nvc1uT8rU7nmKoY7EoR4)
_En mode paysage, tout défilerait verticalement. Et vous profiterez d'une zone de fermeture confortable juste sous votre pouce droit._

### Résumé

Le point à retenir est que le nouveau sélecteur d'applications dans iOS 11 pour iPad peut être encore plus intelligent que nous le pensons. Il est possible qu'ils ne l'aient pas conçu spécifiquement pour l'iPad, après tout. S'il est parfaitement réglé, il offre un moyen convaincant de changer de contexte et peut être vu comme un cache efficace entre l'application actuelle et l'écran d'accueil.

Et, quelle coïncidence, il ne dépend pas d'un bouton Home.

Mon propos avec cet article n'est pas de spéculer ; je ne me soucie pas vraiment de la manière dont Apple aborde la suppression du bouton Home physique, je fais confiance à ce que ce sera bien. Et certaines spéculations autour ont aussi de bons points, à leur manière. J'ai simplement vu ici un exercice de design très intéressant et irrésistible.

Pour les prototypes, réalisés avec Principle, j'ai utilisé des proportions réalistes, tant pour l'affichage ([résolution attendue de 375 * 812 pt](https://daringfireball.net/2017/08/d22_display_conjecture)) que pour les composants connus tels que les éléments du Centre de contrôle.

Cet article est également disponible [en chinois](https://medium.com/@rocketcafeonline/28880c4fd9d5), grâce à [Fred Jame](https://www.freecodecamp.org/news/homeless-iphone-20c154fabbf7/undefined).

Vous pourriez également vouloir lire [Partie 2](https://medium.com/@fab.dubois/homeless-iphone-part-2-1f7b3acc8a6c), sur le processus de design.