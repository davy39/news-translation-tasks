---
title: Comment concevoir les états d'interface utilisateur et communiquer avec les
  développeurs à l'aide d'un tableau FSM
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T16:46:50.000Z'
originalURL: https://freecodecamp.org/news/designing-ui-states-and-communicate-with-developers-effectively-by-fsm-fb420ca53215
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QO0sTki4wLIb9eUw-lCSZg.png
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: Comment concevoir les états d'interface utilisateur et communiquer avec
  les développeurs à l'aide d'un tableau FSM
seo_desc: 'By Vince MingPu Shao

  Life can be tough sometimes for UI designers. While they get to create great designs,
  they also get to deal with pressure from clients or PMs. They’re required to consider
  user experience and user flow. And they often struggle to...'
---

Par Vince MingPu Shao

La vie peut parfois être difficile pour les designers d'interface utilisateur (UI). Bien qu'ils créent de superbes designs, ils doivent également gérer la pression des clients ou des chefs de projet (PM). On leur demande de prendre en compte l'expérience utilisateur et le flux utilisateur. Et ils ont souvent du mal à trouver un moyen efficace de communiquer avec les développeurs.

Pour soulager une partie de la pression de mes collègues designers, je souhaite aider en introduisant une meilleure façon de gérer les composants UI avec des variations d'état. Je pense que c'est l'un des plus grands défis auxquels les designers sont confrontés.

Gérer les variations d'état des composants UI est pénible. Au début, je pensais que c'était si difficile parce qu'il faut créer différentes vues, ce qui peut être ennuyeux. Mais j'ai réalisé ensuite que le design n'est pas la partie terrifiante. Ce sont plutôt les états manquants et le fait de dire exactement aux développeurs ce que l'on veut qui le sont. Cet article abordera donc ces deux problèmes.

### État et organigramme

Pour éviter que l'équipe de design ne manque de préparer les états nécessaires, [ces](https://medium.com/@mikehlee/designing-for-various-states-823816e49c8d) [cinq](http://scotthurff.com/posts/why-your-user-interface-is-awkward-youre-ignoring-the-ui-stack) [états](https://uxdesign.cc/a-cup-of-coffee-and-states-of-ui-screens-1873f522901e) ont été proposés comme norme à suivre pour les designers. Mais par souci de précision, j'aimerais d'abord souligner la différence entre un état et une vue correspondante.

L'état est en fait le résultat d'un composant UI après avoir reçu une entrée. Un état peut nécessiter ou non une vue correspondante pour interagir avec les utilisateurs.

Par conséquent, un composant UI ne peut avoir que [cinq états](https://medium.com/@mikehlee/designing-for-various-states-823816e49c8d), mais chaque état peut en fait avoir plusieurs versions de vues. Confus ? Jetons un coup d'œil à un exemple quotidien d'un bouton de validation, et je pense que vous comprendrez immédiatement.

![Image](https://cdn-media-1.freecodecamp.org/images/Glwjmys2mj0QPze10MNSwkpvIzuVDmynrCN9)
_Un bouton de validation comprend généralement les états par défaut, de chargement, de succès et d'erreur, et chaque état peut avoir différentes vues_

Mais comment savoir qu'il existe trois autres états en plus de l'état initial ? Et comment ces états basculent-ils entre eux ? Il est plus facile de comprendre cette question en regardant un organigramme.

![Image](https://cdn-media-1.freecodecamp.org/images/qFmzHj0yphxyH6wahzjbg2RlVvYME4jhD7bC)
_L'organigramme ne suffit pas à exprimer les détails de conception_

La méthode qui nous aide à gérer les états de l'interface utilisateur est cruciale. Elle doit transmettre le message de l'état vers lequel le composant doit basculer après avoir reçu une certaine entrée. Mais même si cet organigramme est un outil puissant dans la plupart des cas, il n'est pas idéal pour les variations d'état détaillées, en raison de ces inconvénients :

1. **Inconvénient**. Il nécessite l'aide de logiciels ou de plugins (autres que les logiciels de bureau ou de design classiques) pour dessiner, modifier ou maintenir le graphique. Et il est immense.
2. **Imprécision**. Il est difficile de dire quels états nécessitent une vue, et quelles entrées font basculer les états.
3. **Complexité**. Il nécessite une attention particulière lors du choix des symboles et des couleurs appropriés.

En résumé, il est inefficace et imprécis de gérer les états des composants UI à l'aide d'un organigramme. Je pense que la plupart des designers seraient d'accord. Je vais donc proposer ici une meilleure solution.

### Tableau de Machine à États Finis (FSM)

![Image](https://cdn-media-1.freecodecamp.org/images/Pbsf05o4zxVtaE2UutUvfBIwvI-Dq9vfKSZ8)
_Tableau FSM inspiré par [l'introduction à la FSM de Krasimir](http://krasimirtsonev.com/blog/article/managing-state-in-javascript-with-state-machines-stent" rel="noopener" target="_blank" title=")_

Designers, ne soyez pas effrayés par ce nom à consonance technique ! Laissez-moi vous expliquer.

#### Qu'est-ce qu'une machine à états finis ?

Une machine à états finis (FSM) est une machine abstraite qui organise tous les états et entrées possibles. Cette méthodologie est couramment appliquée en programmation et dans toutes sortes d'appareils. Jetez un coup d'œil à l'exemple de machine à états finis d'un tourniquet illustré sur [Wikipedia](https://en.wikipedia.org/wiki/Finite-state_machine), et vous aurez tout de suite une meilleure idée.

Encore une fois, la FSM n'est qu'une collection d'états et d'entrées. C'est aussi simple que cela. Examinons de plus près l'utilisation de ce tableau et découvrons sa puissance.

#### Comment utiliser le tableau FSM

Il y a trois colonnes dans le tableau : **État d'origine (From State)**, **Entrée (Input)**, et **État de destination (To State)**.

Dans la colonne **État d'origine**, chaque cellule représente un état possible du composant.

La colonne **Entrée** contient les informations les plus importantes du tableau : quelles actions limitées peuvent être exécutées ou quelles entrées peuvent être reçues dans chaque état.

Enfin, la colonne **État de destination** est en fait l'état de sortie correspondant à l'entrée reçue.

#### Pourquoi est-ce mieux ?

Le tableau liste clairement trois choses :

* tous les états possibles
* quand chaque action peut être effectuée
* le résultat de l'exécution d'une certaine action

En comparant cela à l'organigramme, aux notes textuelles ou au prototype interactif, je pense que la plupart des développeurs seraient ravis de recevoir ce tableau. Il couvre presque toutes les informations dont un développeur a besoin !

En plus de réduire les coûts de communication, le tableau FSM encourage également un certain état d'esprit. Il aide à établir un lien clair entre la cause et l'effet, vous empêchant de prendre des décisions sans le support d'une logique solide.

### Une meilleure communication d'équipe

Maintenant, après cette brève introduction au tableau FSM, considérons un exemple plus pratique et complexe pour en voir vraiment la puissance. Regardons une page de connexion.

![Image](https://cdn-media-1.freecodecamp.org/images/NxE8X6HX88T6hIGzH7J1K-1J4HjGxwbiVLAo)
_Organigramme et wireframe de la page d'authentification_

La page contient un en-tête, un titre principal, un groupe de formulaires avec deux champs de saisie et un bouton de validation. Pour avoir une vue d'ensemble des fonctions d'authentification, nous avons toujours besoin d'un organigramme clair. Mais il ne peut pas exprimer les variations détaillées des composants, en raison des inconvénients mentionnés ci-dessus.

Par exemple, si un utilisateur clique sur le bouton de validation et que la validation échoue, nous obtenons un message d'erreur — et nous obtenons cette information de l'organigramme. Mais qu'en est-il des messages de validation de saisie spécifiques lorsque l'utilisateur essaie de mettre le focus, de quitter le champ (blur) ou de cliquer sur chaque champ de saisie ? Quand la fonction de validation de saisie doit-elle s'initialiser ? Le bouton de validation doit-il être verrouillé jusqu'à ce que la saisie de l'utilisateur dans le formulaire soit validée ?

![Image](https://cdn-media-1.freecodecamp.org/images/h-sYwcWIhReXKwP2gUJWfi3YoD6Wt7zWPMnj)
_Il y a beaucoup de conditions à prendre en compte_

Ce sont toutes des décisions détaillées qui pourraient affecter l'expérience utilisateur, et elles ne devraient pas être ignorées. Mais comment, en tant que designer, dire exactement au développeur ce que vous pensez ? Les prototypes interactifs, les listes de notes et les réunions en face à face peuvent tous être inefficaces.

Mais en préparant un tableau FSM, les choses deviennent instantanément limpides. Vous pouvez même préparer rapidement de nombreuses versions selon différentes préoccupations d'expérience utilisateur.

Si vous voulez que le bouton de validation soit désactivé avant que tous les champs de saisie ne soient correctement remplis, le tableau ressemblerait à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/vV8ZulIty18DZSRqnH0LouRWxUUFaY4YcgiD)
_FSM du formulaire d'authentification — version désactivée_

Or si vous suivez le [guide Material Design de Google](https://material.io/design/components/text-fields.html#usage), le tableau ressemble alors à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/hzim041f5AbrGtYsiIFgN2iUoGbZEWCN3TBQ)
_FSM du formulaire d'authentification — version Material Design_

N'est-ce pas facile, rapide et clair ? Je pense que c'est bien mieux que d'autres méthodes !

De plus, un tableau FSM peut également s'occuper de composants qui ne sont pas liés au traitement des données. Supposons que le designer veuille que l'en-tête se comporte comme [ce magnifique site](https://legramme.com/). Le tableau FSM peut aider à fournir des seuils et des vues de chaque état.

![Image](https://cdn-media-1.freecodecamp.org/images/6WLZESiLFLgUt-jqOMugKe4UcwjbLeEqSY0j)
_Tableau FSM de l'en-tête_

Et voilà ! Félicitations pour avoir réalisé un document simple mais compréhensible pour votre page d'authentification, en combinant un wireframe, un organigramme et un tableau FSM !

#### Une dernière note

Dans une grande entreprise avec des équipes spécialisées qui collaborent étroitement sur un produit, les designers pourraient ne pas être tenus de réfléchir aux problèmes de gestion d'état. Je n'ai tout simplement jamais fait partie de ce genre d'équipe auparavant. En général, je pense que la plupart des designers UI ont encore besoin de communiquer avec les développeurs, les managers ou d'autres designers sur la transition d'état dans leur carrière.

I sincèrement j'espère que le tableau FSM aidera les designers à réduire les précieuses ressources de temps consacrées aux obstacles de communication, et les aidera même à découvrir une nouvelle façon de penser.

Enfin, n'hésitez pas à me faire part de vos réflexions à ce sujet !

---

[Version chinoise](https://medium.com/@mingpushao/better-way-of-designing-ui-states-chinese-a5c43e46d391) ([中文版連結)](https://medium.com/@mingpushao/better-way-of-designing-ui-states-chinese-a5c43e46d391) / Lisez plus de mes travaux sur [vinceshao.com](https://www.vinceshao.com/blog/how-to-design-ui-states-and-communicate-with-developers-using-fsm-table/)