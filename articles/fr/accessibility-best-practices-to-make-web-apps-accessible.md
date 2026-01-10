---
title: Meilleures pratiques d'accessibilité – À retenir lors de la création d'applications
  web accessibles
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2022-12-16T21:01:26.000Z'
originalURL: https://freecodecamp.org/news/accessibility-best-practices-to-make-web-apps-accessible
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/ben-kolde-bs2Ba7t69mM-unsplash-1.jpg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
- name: best practices
  slug: best-practices
- name: Web Applications
  slug: web-applications
seo_title: Meilleures pratiques d'accessibilité – À retenir lors de la création d'applications
  web accessibles
seo_desc: 'Anyone should be able to use your websites and apps - both people with
  disabilities and those without. This will make your website accessible.

  Think about the last site you built, or your favorite site. Are you confident that
  anyone can use your site...'
---

Tout le monde devrait pouvoir utiliser vos sites web et applications - tant les personnes handicapées que celles qui ne le sont pas. Cela rendra votre site web accessible.

Pensez au dernier site que vous avez construit, ou à votre site préféré. Êtes-vous sûr que n'importe qui peut utiliser votre site et effectuer les actions critiques qu'il nécessite ? Avez-vous pensé aux personnes souffrant de handicaps moteurs, visuels, cognitifs et auditifs ?

L'accessibilité est souvent laissée de côté. Lorsque vient le moment de livrer une fonctionnalité, nous effectuons un test d'accessibilité et découvrons que notre site n'était pas accessible, puis nous appliquons une solution rapide et peu élégante.

Rendre un site accessible est une tâche énorme. Mais si nous gardons l'accessibilité à l'esprit dès le départ, cela facilite grandement la création d'une application web accessible.

Dans cet article, je vais passer en revue 5 choses à garder à l'esprit PENDANT la construction de votre application, afin de ne pas avoir à bricoler une solution à la fin.

## 5 choses à retenir pour une bonne accessibilité

1. HTML sémantique
2. Tabindex
3. Attributs Aria
4. Rôle
5. Navigation au clavier et lecteurs d'écran

En bref, S.T.A.R.K.

Si vous avez besoin d'aide pour vous en souvenir, pensez à Tony Stark.

![TonyStark](https://cdn.vox-cdn.com/uploads/chorus_image/image/55400215/ktokatitmir0.0.jpg)

Passons en revue chacun de ces points pour comprendre comment les utiliser dans vos applications web.

### Qu'est-ce que le HTML sémantique ?

L'utilisation du HTML sémantique est importante pour l'accessibilité. En effet, les technologies d'assistance telles que les lecteurs d'écran sont capables d'interpréter ce qui se trouve sur la page en analysant le HTML de la page. Elles permettent aux utilisateurs d'effectuer des actions en fonction des éléments.

Par exemple, si un lecteur d'écran rencontre un `button`, il signale à l'utilisateur qu'il doit cliquer dessus.

Examinons quelques cas d'utilisation de ce qui peut se passer lorsque vous n'utilisez pas de HTML sémantique :

#### Création de boutons en utilisant `div` au lieu de `button` :

Les `div` sont des éléments conteneurs, donc lorsqu'un lecteur d'écran rencontre une div, il pense automatiquement qu'il s'agit d'un élément de présentation.

Lorsque l'utilisateur d'un lecteur d'écran rencontre une `div` qui contient du contenu ou des enfants, le lecteur d'écran annonce `role="group"` et l'utilisateur manquera complètement que la `div` est interactive. Assurez-vous donc d'utiliser l'élément sémantique approprié pour son usage. Vous obtenez l'accessibilité gratuitement.

#### Utilisation de CSS pour simuler des titres au lieu d'utiliser les balises `h1-6` :

Les balises de titre telles que `<h1>` et `<h2>` permettent à une technologie d'assistance de savoir qu'il s'agit d'un texte important, et le lecteur d'écran annoncerait "Titre".

Lorsque vous utilisez CSS pour créer un titre au lieu d'utiliser une sémantique correcte, la signification du texte est perdue pour un lecteur d'écran.

Assurez-vous simplement d'utiliser le HTML sémantique chaque fois que possible.

### Qu'est-ce que Tabindex ?

L'ajout d'un `tabindex` rend les éléments interactifs navigables au clavier. Lorsque vous ajoutez `tabindex` à un élément, un utilisateur peut naviguer vers celui-ci en utilisant uniquement son clavier et/ou des technologies d'assistance.

1. Vous utilisez un tabindex de `0` pour définir le focus sur un élément dans l'ordre de tabulation par défaut,
2. Vous utilisez un tabindex de `-1` pour focaliser programmatiquement un élément en utilisant JavaScript.
3. N'attribuez pas une valeur > 1 à tabindex.

Un mot d'avertissement cependant - vous ne devriez ajouter `tabindex` qu'aux éléments interactifs. Ce n'est pas une bonne pratique d'ajouter `tabindex` à des éléments tels que `div`.

Au lieu d'ajouter tabindex dans ce cas, utilisez un élément sémantique, tel qu'un `button` puisque les éléments sémantiques sont déjà tabulables et n'ont pas besoin d'une valeur `tabindex` supplémentaire.

### Qu'est-ce que les attributs ARIA ?

Les attributs Aria tels que `aria-checked`, `aria-label` donnent des informations supplémentaires aux technologies d'assistance.

Les attributs Aria sont un ensemble d'attributs HTML que vous utilisez pour fournir des informations supplémentaires sur le but et l'état des éléments sur une page web. Ces attributs sont particulièrement bénéfiques pour les technologies d'assistance afin de fournir plus de contexte et une meilleure navigation pour les utilisateurs.

Certains attributs aria courants incluent :

1. `aria-label` : utilisé pour fournir une étiquette ou un nom pour un élément.
1. `aria-hidden` : utilisé pour indiquer qu'un élément doit être caché des technologies d'assistance. Cela peut être utile pour les éléments qui sont utilisés à des fins de mise en page mais qui ne sont pas pertinents pour le contenu de la page.
1. `aria-describedby` : utilisé pour associer un élément à une description, ce qui aide à fournir le contexte d'un élément.
1. `aria-liv`e : utilisé pour indiquer que le contenu d'un élément peut changer dynamiquement, et que les technologies d'assistance doivent prêter attention aux changements dans le contenu de l'élément.

Vous pouvez utiliser ces attributs en combinaison les uns avec les autres et avec des attributs HTML standard pour créer un contenu web plus accessible et convivial.

### Qu'est-ce que l'attribut `aria-role` ?

Vous utilisez l'attribut `aria-role` pour définir le but d'un élément HTML et fournir sa signification sémantique.

Par exemple, si vous construisez un composant de grille à l'aide de CSS et de divs, vous pouvez utiliser `role="grid"` pour informer les technologies d'assistance sur la sémantique du composant.

Certains `aria-role` courants incluent :

1. `button` : utilisé pour indiquer qu'un élément doit être traité comme un bouton.
2. `alert` : utilisé pour indiquer qu'un élément est une boîte d'alerte.
3. `presentation` : utilisé pour indiquer qu'un élément n'est que présentationnel.

Il est important de faire preuve de prudence avec `aria-role`. N'en abusez pas.

### Comment gérer la navigation au clavier et les lecteurs d'écran

De nombreux utilisateurs souffrant de handicaps moteurs dépendent de leur clavier et des technologies d'assistance pour naviguer sur le web. Il est donc crucial que chaque composant soit navigable à l'aide d'un clavier et d'un lecteur d'écran.

Vous pouvez tester l'accessibilité au clavier en naviguant sur un site en utilisant uniquement votre clavier. Voici quelques touches courantes :

1. La touche `tab` pour naviguer vers différentes sections du site.
2. La `barre d'espace` pour sélectionner des éléments, tels qu'une case à cocher.
3. `entrée` pour appuyer sur les boutons.

Lors du test de la navigation au clavier, assurez-vous de penser aux points suivants :

1. Le focus reste visible : Assurez-vous de pouvoir voir clairement quel élément est mis en focus sur la page. Le focus doit toujours rester visible.
2. Ordre de tabulation : Lorsque vous naviguez entre les sections, l'ordre de tabulation doit suivre le flux naturel et la structure logique du site web. Il ne doit pas sauter d'une section à l'autre.
3. Pièges au clavier : Assurez-vous que lors de la navigation avec le clavier, le focus ne reste pas bloqué sur un élément. Par exemple, cela pourrait se produire lorsqu'une modale est ouverte, ou que le focus est navigué vers un widget, tel qu'un calendrier ou un sélecteur d'emoji. Assurez-vous que lorsque vous sélectionnez un élément dans le widget, vous pouvez revenir à la navigation sur le site.

## Conclusion

Dans l'ensemble, tester l'accessibilité pendant le développement est une partie importante du processus qui peut aider à créer des logiciels plus utilisables et accessibles pour tous les utilisateurs. Tester l'accessibilité tôt aide à fournir une excellente expérience utilisateur pour tout le monde.

Dans le prochain article, je parlerai des différents outils d'accessibilité et de la manière de déboguer un problème d'accessibilité. Vous pouvez [vous inscrire pour le recevoir dans votre boîte de réception ici.](http://tinyletter.com/shrutikapoor)

En attendant, profitez de vos vacances !

Feliz Navidad.