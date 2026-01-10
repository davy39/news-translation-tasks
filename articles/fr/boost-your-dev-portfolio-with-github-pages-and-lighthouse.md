---
title: Améliorez votre Portfolio de Développeur avec GitHub Pages et Lighthouse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-20T16:33:16.000Z'
originalURL: https://freecodecamp.org/news/boost-your-dev-portfolio-with-github-pages-and-lighthouse
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca42a740569d1a4ca609d.jpg
tags:
- name: GitHub
  slug: github
- name: Lighthouse
  slug: lighthouse
- name: portfolio
  slug: portfolio
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Améliorez votre Portfolio de Développeur avec GitHub Pages et Lighthouse
seo_desc: 'By Cam Barts

  For someone who is trying to break into software development, it doesn’t matter
  where you look — LinkedIn, career advice boards, youtube tutorials — the advice
  is always the same: you need a portfolio. freeCodeCamp knows this advise, and...'
---

Par Cam Barts

Pour quelqu'un qui essaie de se lancer dans le développement logiciel, peu importe où vous regardez — LinkedIn, forums de conseils de carrière, tutoriels YouTube — les conseils sont toujours les mêmes : vous avez besoin d'un portfolio. freeCodeCamp connaît ce conseil, et ils le rendent obligatoire pour créer un portfolio afin de terminer leur certification "Responsive Web Design".

Le portfolio est censé être un document vivant. Vous terminez un projet, vous ajoutez ce projet à votre portfolio pour le montrer au monde. Vous l'enrichissez constamment, affichant votre trajectoire de croissance personnelle. Vous le donnez à des recruteurs potentiels et à des responsables d'embauche pour ajouter une dimension à votre CV.

Parmi les cinq projets pour obtenir cette certification, j'ai sans conteste consacré le plus de travail à mon portfolio. Si c'était ma première impression numérique, je voulais m'assurer que ce soit la meilleure possible.

La méthode de facto pour compléter les projets sur freeCodeCamp est d'utiliser codepen.io. La version gratuite vous permet de coder dans des panneaux HTML, CSS et JavaScript, et de voir vos modifications au fur et à mesure que vous les tapez dans une fenêtre. Vous pouvez ouvrir la page en vue complète, ce qui élimine les panneaux HTML, CSS et JavaScript, mais laisse une bannière noire en haut. L'URL est un hash, quelque chose comme [https://codepen.io/cam-barts/full/ZPWpqo](https://codepen.io/cam-barts/full/ZPWpqo), qui n'est pas mémorable, ne donne aucune indication sur le contenu du site, et à mon avis ne fait pas grande impression sur un CV. De plus, à moins de payer pour un abonnement avec codepen, vous ne pouvez pas le changer.

Vers la fin de mon projet, les étoiles se sont alignées et j'ai découvert deux technologies qui aideraient mon portfolio à se démarquer : GitHub Pages et Google Lighthouse.

[GitHub Pages](https://pages.github.com/) vous permet d'héberger un site web directement depuis un dépôt GitHub. Il offre une URL github.io plutôt élégante, ce qui a attiré mon attention pour quelque chose à mettre sur un CV. Cela me donnerait un contrôle total sur ce que mes utilisateurs verraient lorsqu'ils navigueraient sur le site (adieu, bannière noire), et je n'aurais pas à gérer l'auto-hébergement ou à payer pour un autre service d'hébergement.

J'ai entendu parler de [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/) dans le [CodeNewbie Podcast avec Frances Coronel](https://www.codenewbie.org/podcast/what-are-progressive-web-apps). Il audite votre site web directement depuis les outils de développement Chrome pour cinq domaines : Performance, Progressive Web App, Accessibilité, Bonnes Pratiques et SEO. Le SEO, ou Search Engine Optimization, est ce qui aide votre site à remonter en haut des moteurs de recherche comme Google, ce qui vous aide à être trouvé. De plus, maintenant que j'allais héberger mon site sur Pages, je voulais prendre la responsabilité de la performance de mon site, et pour le faire efficacement, je devais au moins avoir un point de référence.

Mon objectif en écrivant cet article est de vous aider à créer un site portfolio professionnel et ultra-rapide, sans aucun coût pour vous. Je veux que ce soit quelque chose dont vous soyez fier de parler sur LinkedIn et d'afficher en haut de votre CV, et je veux utiliser GitHub Pages et Google Lighthouse pour y parvenir.

Pour aller plus loin, j'ai fait quelques hypothèses. La première est que vous avez un compte GitHub. Si vous n'en avez pas déjà un, [en créer un est facile](https://github.com/join). La seconde est que vous avez une compréhension de base de git. Si vous êtes tout nouveau, il y a beaucoup d'excellents [articles](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) pour commencer. Cet article suppose que vous avez terminé votre portfolio sur codepen. Enfin, vous devriez avoir Google Chrome installé.

Cet article suit mon portfolio personnel. Vous pouvez trouver le pen [ici](https://codepen.io/cam-barts/pen/ZPWpqo), le code [ici](https://github.com/cam-barts/cam-barts.github.io), et le produit final est à [cam-barts.github.io](https://cam-barts.github.io/).

### Commencer

La configuration de votre site GitHub Pages est assez simple. La version TL;DR est :

* Créer un dépôt suivant la convention de nom [Nom d'utilisateur GitHub].github.io
* Cloner localement
* Créer les fichiers _index.html_, _style.css_, _script.js_ dans le dépôt
* Ajouter du code à ces fichiers
* Valider et pousser vers GitHub
* Profitez !

Vous créez un dépôt avec un titre qui suit la convention [Votre nom d'utilisateur GitHub].github.io. Voici le mien : cam-barts.github.io. Tout code poussé vers ce dépôt est affiché lorsque vous naviguez vers ce site.

Alors, une fois que vous avez cloné le dépôt localement, que mettez-vous exactement dedans ?

Vous devriez commencer avec trois fichiers, un fichier _index.html_, un fichier _style.css_, et un fichier _script.js_. Dans l'éditeur de votre choix (j'utilise [Atom](https://atom.io/)), vous devriez commencer avec le snippet de code suivant dans votre _index.html_ :

Il y a beaucoup de choses ici qui peuvent être inconnues si vous n'avez travaillé qu'avec codepen.io.

L'attribut _dir_ dans la balise html indique que le document doit être lu de **G**auche **à** **D**roite. Cela garantit simplement que lorsque votre page s'affiche, tous les éléments sont justifiés à gauche, ce qui est la façon dont les anglophones lisent.

Les balises meta dans le head indiquent des métadonnées sur la page, ce qui aide les moteurs de recherche comme Google à indexer votre site.

À ce stade, vous devriez remplir les balises meta et la balise title. Notez que le contenu de la balise meta _keywords_ doit être séparé par des virgules et doit inclure des termes que vous souhaiteriez que les gens utilisent dans Google pour trouver votre portfolio. Voici à quoi ressemble le mien :

L'étape suivante consiste à copier la section HTML de votre portfolio pen dans la section body de votre snippet. Une fois cela terminé, si vous avez lié un CSS ou JS externe dans les paramètres de votre pen, comme [Bootstrap](https://getbootstrap.com/) ou [Font Awesome](https://fontawesome.com/?from=io), vous devez lier ceux-ci dans votre _index.html_.

Créez plus de balises link pour le CSS et de balises script pour le JavaScript et ajoutez les liens qui se trouvent dans les paramètres aux attributs _href_ et _src_, respectivement. Pour vous assurer que vos styles et scripts apparaissent, assurez-vous de les placer avant les balises link et script existantes dans le snippet. Par exemple, lier Bootstrap et JQuery ressemblerait à ceci :

Ensuite, vous devez ajouter votre propre CSS dans votre _style.css_, et si vous avez du JavaScript, ajoutez-le à votre _script.js_.

Après avoir fait cela, vous êtes prêt à valider tout votre travail et à le pousser vers GitHub. Immédiatement après avoir fait cela, vous pouvez naviguer vers [Votre nom d'utilisateur GitHub].github.io et consulter votre site web !

### Optimiser votre site portfolio

Félicitations pour la publication de votre portfolio !

Les prochaines étapes consistent à optimiser votre site. Pour cela, nous utiliserons [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/). Il est préférable de le faire dans une fenêtre de navigateur InPrivate afin que le cache ou les extensions Chrome que vous pourriez avoir n'affectent pas les résultats. Lorsque vous naviguez vers votre site, ouvrez les outils de développement Chrome (Ctrl + Maj + i) et cliquez sur l'onglet _Audits_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7v572NCjU_EmmpcSfIzHdQ.png)
_Volet Google Lighthouse_

Les Progressive Web Apps sont hors du cadre de ce tutoriel, mais il n'y a aucun mal à exécuter tous les audits. Lorsque vous les exécutez, vous devriez obtenir une page qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YJ54LEN5nN3AuoJ5VEVHYg.png)

Le meilleur aspect de ces rapports est qu'ils vous donnent des "Opportunités" pour améliorer vos scores.

Dans la section performance, il vous indique de servir des formats de fichiers de nouvelle génération tels que WebP au lieu des images .PNG traditionnelles, et suggère le chargement paresseux des images.

Dans la section SEO, il suggère des améliorations SEO telles que l'ajout d'une balise meta description et l'utilisation de tailles de police lisibles. Non seulement il fait ces suggestions, mais il fournit également des liens vers des articles avec des exemples pratiques de choses à changer dans votre code pour optimiser ces domaines.

Pour moi, il n'a fallu qu'une heure pour obtenir des scores dans les années 90 pour la Performance, l'Accessibilité, les Bonnes Pratiques et le SEO. Vous pouvez voir toutes les modifications que j'ai apportées [ici](https://githistory.xyz/cam-barts/cam-barts.github.io/blob/master/index.html).

### Aller plus loin

Les prochaines étapes pour votre site dépendent de vous. Vous pourriez le lier à [Google Analytics](https://analytics.google.com/analytics/web/) pour voir combien de visiteurs votre Portfolio reçoit. Vous pourriez ajouter des sections pour vos récompenses afin de montrer vos certifications freeCodeCamp au fur et à mesure que vous les obtenez. L'évolution de votre site est entièrement entre vos mains ! Commentez les liens vers votre portfolio ci-dessous.