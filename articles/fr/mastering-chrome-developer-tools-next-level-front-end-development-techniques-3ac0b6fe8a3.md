---
title: 'Maîtriser les outils de développement Chrome : Techniques avancées de développement
  front-end'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-12T16:05:59.000Z'
originalURL: https://freecodecamp.org/news/mastering-chrome-developer-tools-next-level-front-end-development-techniques-3ac0b6fe8a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MO3U6DyiFUGfZrEaVfKUmw.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Maîtriser les outils de développement Chrome : Techniques avancées de
  développement front-end'
seo_desc: 'By Ben Edelstein

  You may already be familiar with the basic features of the Chrome Developer Tools:
  the DOM inspector, styles panel, and JavaScript console. But there are a number
  of lesser-known features that can dramatically improve your debugging ...'
---

Par Ben Edelstein

Vous êtes peut-être déjà familier avec les fonctionnalités de base des outils de développement Chrome : l'inspecteur DOM, le panneau des styles et la console JavaScript. Mais il existe un certain nombre de fonctionnalités moins connues qui peuvent considérablement améliorer vos flux de travail de débogage ou de création d'applications.

### Thème sombre

![Image](https://cdn-media-1.freecodecamp.org/images/kprZQTbB7uZgQnEF8XBqKrMnepTByHLI28Vq)

Chrome dispose d'un thème sombre intégré pour les outils de développement. Vous pouvez l'activer en cliquant sur l'icône des trois points dans le coin supérieur droit du panneau des outils de développement, en cliquant sur « paramètres », puis en basculant le thème.

Je trouve parfois cela plus reposant pour les yeux, et, évidemment, cela a l'air beaucoup plus cool :)

### Mode de sélection

![Image](https://cdn-media-1.freecodecamp.org/images/Z42xqdkYNVng5a89OPUQLkekPs-e-hbL-5L4)

Les outils de développement Chrome (DevTools) offrent plusieurs moyens de sélectionner des éléments — le plus pratique étant le mode de sélection.

Cet outil, activé en appuyant sur l'icône de la souris dans le coin supérieur gauche du panneau des outils de développement (ou avec cmd + shift + c), vous permet de sélectionner des éléments sur la page simplement en cliquant dessus.

Une fois activé, vous pouvez déplacer votre souris sur la page et prévisualiser la sélection, puis cliquer pour sélectionner un élément à inspecter.

Cet outil est idéal pour sélectionner rapidement un élément sur la page, car appuyer sur cmd + shift + c ouvrira les outils de développement et passera directement en mode de sélection.

### Stocker en tant que variable globale

![Image](https://cdn-media-1.freecodecamp.org/images/CYy2ePcPOjIXfjnbA0M6etgOIdECdtiVDada)

Inspecter des objets compliqués qui sont enregistrés dans la console peut parfois être délicat s'ils ont de nombreuses clés, ou contiennent des valeurs difficiles à analyser manuellement. Heureusement, Chrome facilite l'inspection de tels objets avec JavaScript.

Pour ce faire, faites un clic droit sur un objet dans la console et appuyez sur « stocker en tant que variable globale ». Cela stocke l'objet en tant que variable globale accessible dans la console appelée `temp1` avec laquelle vous pouvez ensuite travailler en utilisant JavaScript.

### Outils d'animation

![Image](https://cdn-media-1.freecodecamp.org/images/VtBXC64DheXLzxCQQJYqcR1N3zmDXnsSHKWD)

Récemment, l'équipe Chrome a ajouté un certain nombre de nouvelles fonctionnalités pour le débogage et la création d'animations.

En cliquant sur la liste déroulante dans le coin supérieur gauche de la console, un panneau « Animations » apparaît, vous permettant de limiter la vitesse de toutes les animations sur un site.

Vous pouvez également mettre en pause toutes les animations. Cela est particulièrement utile pour un site qui regorge de contenu animé.

![Image](https://cdn-media-1.freecodecamp.org/images/s2wpPRC4M5SzjB1LjdorbUvx4Z4tH5DQCKjg)
*Le visualiseur d'animations vous permet de contrôler individuellement la courbe de chaque propriété*

![Image](https://cdn-media-1.freecodecamp.org/images/QlDJcZSMNccentbE9d6fIjvmjAyiMo2rT4Ky)
*Contrôleur d'animation CSS*

En cliquant sur l'icône de courbe violette dans la propriété `transition` d'un élément, vous pouvez visualiser la courbe de mouvement d'une animation et ajuster ses propriétés. De plus, vous pouvez utiliser les icônes de flèches pour parcourir une liste d'animations prédéfinies à appliquer à votre élément.

### Simuler l'état pseudo d'un élément

![Image](https://cdn-media-1.freecodecamp.org/images/nuHLrpiy2g8VQ-imZtOK8eInzXGq6CfsJ04y)

Un autre outil pratique pour styliser les éléments est le simulateur d'état d'élément, accessible en cliquant sur l'icône `:hov` dans le coin supérieur droit du panneau Styles.

Cet outil vous permet de simuler les états pseudo des éléments tels que hover, active, focused et visited, et de visualiser les styles associés à ces sélecteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/slVF29-rY1EpnN9muudFJdrb2nP8CB4u50dq)

Pour ajouter des styles pour ces états pseudo, ajoutez un nouveau sélecteur (avec l'icône `+`) et ajoutez `:<etat>` à la fin de la chaîne de sélecteur.

Par exemple, pour ajouter une règle de survol à un `li` avec la classe `logo`, créez un nouveau sélecteur, `li.logo:hover`, et ajoutez des styles là.

Vous pouvez ensuite tester vos styles en cochant l'état de l'élément `:hover` pour simuler le survol de l'élément.

### Embellir le CSS et le JavaScript

![Image](https://cdn-media-1.freecodecamp.org/images/aCRgHPiMSdvKydcyBDeX6jbSxfqMe3NBlNej)

Déboguer ou visualiser du JavaScript et du CSS minifiés est très difficile. Mais heureusement, DevTools fournit un outil qui rend cela un peu plus facile.

Après avoir ouvert un fichier minifié dans l'onglet « Sources », vous pouvez cliquer sur le logo des crochets dans le coin inférieur gauche du fichier, et DevTools « embellira » le code.

Cela fonctionne assez bien avec les fichiers CSS, et fait un travail décent avec JavaScript, bien que certaines informations (comme les noms de variables) soient perdues dans le processus de minification.

### Alt + Haut / Alt + Bas

![Image](https://cdn-media-1.freecodecamp.org/images/qJhDKbGDSyA7e7X32za7oRcFiQLCg8zI1HnK)

Lors du débogage de CSS, vous pouvez sélectionner une propriété et utiliser les touches haut/bas pour ajuster sa valeur. Par défaut, les touches fléchées ajustent les valeurs de +/- `1`. Cependant, en maintenant la touche `alt`, vous pouvez utiliser les touches fléchées pour ajuster les valeurs finement par incréments de `0,1`, ce qui est particulièrement utile lorsque vous travaillez avec des valeurs fractionnaires.

Inversement, vous pouvez maintenir `shift` pour ajuster les valeurs par incréments de `10`.

### Conserver le journal

![Image](https://cdn-media-1.freecodecamp.org/images/Lz03uh4bgEx0y8B0Avxtcxke0m57KyNvzvdu)

Conserver le journal est une case à cocher qui vous permet de persister les journaux entre les actualisations de page. Cela est utile lors du débogage de problèmes de site Web qui nécessitent une actualisation de la page, car toutes les sorties de la console sont sinon effacées.

Lorsque cette option est activée, un nouveau type de journal « Navigation » apparaît dans la console pour montrer les actualisations de page ou les événements de navigation vers différentes pages.

### Filtres de réseau et de journal

![Image](https://cdn-media-1.freecodecamp.org/images/gvmb80U1el6fIFkYBNv50EPUXUsJXHVg5BEl)

Lors du débogage d'une application qui a beaucoup de requêtes réseau ou de journaux de console, il peut être utile de filtrer pour des types particuliers d'événements.

Chrome dispose d'un langage de filtrage qui prend en charge de nombreuses propriétés différentes, ainsi que des opérateurs comme `*` pour effectuer des correspondances avec des caractères génériques.

Si vous tapez « - », Chrome exposera une saisie semi-automatique qui montre les diverses propriétés que vous pouvez filtrer. Vous pouvez également activer le mode « regex » pour effectuer une correspondance regex sur les données affichées dans chaque ligne.

### Couverture de code

![Image](https://cdn-media-1.freecodecamp.org/images/ubyywvTQ-vMNXOCBm33ftRgQnQMUU64NPQ0a)

La couverture de code vous permet d'exécuter votre application Web, puis pour chaque fichier JavaScript et CSS, de voir quelles lignes de code ont été exécutées et lesquelles ne l'ont pas été. Cela est utile car, lors du travail sur un projet complexe ou à long terme, il est facile d'accumuler du code mort.

Pour l'utiliser, assurez-vous d'avoir Chrome 59 ou supérieur, et allez dans l'onglet « Couverture ». Appuyez sur « enregistrer » et commencez à utiliser votre application. Une fois terminé, Chrome vous montrera le code exact qui a été exécuté pendant votre session.

### Débogage des problèmes en production

DevTools ne fonctionne que si vous exécutez votre application sur votre propre machine. Si vous êtes intéressé par la compréhension des bugs et des problèmes de performance que les utilisateurs rencontrent en production, essayez [LogRocket](https://logrocket.com).

![Image](https://cdn-media-1.freecodecamp.org/images/-1GmSaj2CNCJ2MKwvXs6tOAzTvzkMx034BIN)

[LogRocket](https://logrocket.com) est un outil de journalisation front-end qui vous permet de rejouer les problèmes comme s'ils s'étaient produits dans votre propre navigateur. Au lieu de deviner pourquoi des erreurs se produisent, ou de demander aux utilisateurs des captures d'écran et des vidages de journal, LogRocket vous permet de rejouer la session pour comprendre rapidement ce qui s'est mal passé. Il fonctionne parfaitement avec n'importe quelle application, quel que soit le framework, et dispose de plugins pour journaliser un contexte supplémentaire à partir de React, Angular et Vue.js.

LogRocket instrument votre application pour enregistrer les journaux de la console, les requêtes/réponses réseau avec les en-têtes + corps, les métadonnées du navigateur, les actions/états Redux et les temps de performance. Il enregistre également le HTML et le CSS de la page, recréant des vidéos pixel-parfaites même des applications monopage les plus complexes.

Vous pouvez [découvrir LogRocket ici](https://logrocket.com/).

[**LogRocket | Journalisation et relecture de session pour les applications JavaScript**](https://logrocket.com)
[_LogRocket vous aide à comprendre les problèmes affectant vos utilisateurs, afin que vous puissiez revenir à la création de logiciels exceptionnels._logrocket.com](https://logrocket.com)

Merci d'avoir lu. J'espère que ces techniques avancées de DevTools vous aideront à créer de meilleures applications avec moins de stress.