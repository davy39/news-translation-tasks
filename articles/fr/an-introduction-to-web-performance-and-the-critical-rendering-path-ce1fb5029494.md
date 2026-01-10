---
title: Une introduction à la performance Web et au Critical Rendering Path
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T22:27:47.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-web-performance-and-the-critical-rendering-path-ce1fb5029494
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wlMJbbRWAHesWIo-.
tags:
- name: Browsers
  slug: browsers
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: web performance
  slug: web-performance
seo_title: Une introduction à la performance Web et au Critical Rendering Path
seo_desc: 'By Sibylle Sehl

  Most of us work with the web every day. It’s become normal for us to get all the
  information we need delivered to us almost instantly. But how that web page is actually
  put together and delivered to us is a bit of a mystery.

  Sometimes...'
---

Par Sibylle Sehl

La plupart d'entre nous utilisons le web tous les jours. Il est devenu normal pour nous d'obtenir toutes les informations dont nous avons besoin presque instantanément. Mais la manière dont une page web est réellement assemblée et livrée reste un peu mystérieuse.

Parfois, les pages web sont incroyablement rapides, et parfois nous devons attendre longtemps pour voir le contenu — ce qui nous frustre souvent et nous pousse à abandonner la page. Dans l'article suivant, je vais essayer d'éclaircir un peu les choses.

_Avertissement_ : Toutes les informations que je partage dans cet article sont ce que j'ai appris grâce aux cours gratuits mentionnés à la fin et **résumés** ici pour toute personne intéressée.

### Le Critical Rendering Path

Tout d'abord, il serait utile de comprendre les étapes que le navigateur suit réellement. Il commence avec des fichiers HTML, CSS et JavaScript simples, passe par le rendu et la peinture d'une page, et arrive finalement à ce que l'utilisateur voit.

Ces étapes, depuis vos différents fichiers HTML, CSS et JS jusqu'à une page rendue, sont communément appelées le Critical Rendering Path (ou CRP pour faire court).

Le Critical Rendering Path se compose de cinq étapes différentes, qui sont mieux expliquées dans un graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/ecrsi9JGRA-uLZxs1ojHe4eJmyig79eJr3Dj)
_Les différentes étapes du Critical Rendering Path (DOM et CSSOM font référence respectivement au Document Object Model et au CSS Object Model)_

#### Construction du DOM et du CSSOM

La plupart des pages web sont composées de HTML, CSS et JavaScript, qui jouent tous un rôle critique dans le CRP. Pour lire et traiter votre HTML, le navigateur construit le Document Object Model (DOM). Le navigateur examine les balises HTML (<p>, </p>, <h1> et </h1>, etc.) dans votre balisage et les convertit en tokens, qui sont ensuite créés en nœuds en parallèle. En traitant ces tokens StartTag et EndTag dans l'ordre et en voyant lesquels viennent en premier, le navigateur peut établir leur hiérarchie et établir les parents et les enfants.

Ne laissez pas cette terminologie vous effrayer, cependant. Imaginez le DOM comme un grand arbre avec des branches qui représentent les nœuds parents, et qui contiennent à leur tour des feuilles, les nœuds enfants. Cet arbre représentera les dépendances des nœuds dans notre HTML et ressemble quelque peu à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/N9bQMLisw9BAWK3bzjrrSILJx0rtabPFKKVg)
_Tiré de W3 Schools ([https://www.w3schools.com/js/js_htmldom.asp](https://www.w3schools.com/js/js_htmldom.asp" rel="noopener" target="_blank" title=")) — L'arbre DOM des objets_

Dans l'image ci-dessus, nous pouvons voir l'élément racine qui englobe tous ses enfants, qui sont à leur tour des parents contenant des enfants. Retournez cela à l'envers et cela ressemblera presque à un arbre !

Le DOM représente ainsi notre balisage HTML complet. Comme vous l'avez vu, il est construit de manière incrémentielle en traitant les tokens et en les convertissant en nœuds. En fait, nous pouvons utiliser cela à notre avantage en retournant un HTML partiel et en donnant à notre utilisateur l'indication que quelque chose se passe et se rend sur la page.

Après avoir construit le DOM, votre navigateur traitera le CSS et construira le CSS Object Model (CSSOM). Ce processus est très similaire à la construction du DOM. Mais dans ce processus, contrairement à avant, les nœuds enfants héritent des règles de style de leurs nœuds parents — d'où le nom Cascading Style Sheets (CSS).

Malheureusement, nous ne pouvons pas traiter le CSS partiel de manière incrémentielle comme nous avons pu le faire avec le DOM, car cela pourrait facilement conduire à appliquer les mauvais styles si un style de remplacement arrive plus tard dans le processus. C'est la raison pour laquelle le CSS est bloquant pour le rendu, car le navigateur doit arrêter le rendu jusqu'à ce qu'il reçoive et traite tout le CSS.

Notre arbre DOM et CSSOM contiendra tous les nœuds et dépendances que nous avons dans notre page.

#### Rassembler tout le contenu visible — L'arbre de rendu

Le navigateur doit savoir quels nœuds représenter visuellement sur la page. L'arbre de rendu réalise exactement cela et est une représentation du contenu **visible** du DOM et du CSSOM.

Nous commençons à construire l'arbre de rendu en identifiant le nœud racine, puis en copiant toutes les informations **visibles** du DOM et du CSSOM. Pour cela, nous vérifions également que nous recherchons des balises ayant le même sélecteur. Les métadonnées, les liens, etc., ne sont **pas** copiés dans l'arbre de rendu. Il en va de même pour le CSS contenant "display: none;" car il s'agit également d'un élément non visible.

Une fois ce processus terminé, nous obtenons quelque chose de similaire à ce qui suit (remarquez comment "web performance" n'est pas copié).

![Image](https://cdn-media-1.freecodecamp.org/images/xTIwe6nvSWmROHLXZzTuOgOoS3Unzt8ccFGS)
_Le droit d'auteur de l'image appartient à Google et Ilya Grigorik — tiré de [https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/render-tree-construction" rel="noopener" target="_blank" title=")_

L'arbre de rendu est une description assez précise de ce qui est réellement affiché à l'écran, capturant à la fois le contenu et les styles associés. Bien sûr, cela serait beaucoup plus complexe dans des exemples réels.

#### Faire en sorte que cela s'adapte correctement — La mise en page

Bien que nous sachions maintenant **ce** que nous devons afficher et rendre sur la page, il est important de savoir **comment** cela est rendu. Pour que la mise en page ait l'air correcte, nous devons connaître la taille du navigateur. Notre mise en page en dépend pour calculer les positions et dimensions correctes pour tous nos éléments sur la page.

Tout cela se passe pendant l'étape de mise en page. Prendre en compte l'étape de mise en page est particulièrement important pour les mobiles, où notre point de vue peut changer lorsque nous passons du mode paysage au mode portrait lorsque nous tournons nos téléphones. Cela signifie que le navigateur devrait avoir besoin de relancer l'étape de mise en page chaque fois que nous tournons notre téléphone, ce qui pourrait être un goulot d'étranglement pour les performances.

#### Peindre les pixels

Cette étape consiste à peindre réellement les pixels à l'écran, spécifiés par ce qui (arbre de rendu) et comment (mise en page). L'étape de peinture inclut la peinture réelle des pixels (par exemple, lors du redimensionnement d'une image) par opposition à simplement la positionner. C'est ce que vous voyez finalement sur votre écran par la suite.

![Image](https://cdn-media-1.freecodecamp.org/images/KB1AjGRrtg1jv-2wn5Xz2sThlNBZt0vokPXt)
_Exécuter toutes les étapes du CRP dans l'ordre. (Photo par [Unsplash](https://unsplash.com/@the_alp_photography?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">ALP STUDIO</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="))_

#### Résumons

Maintenant, rassemblons toutes ces informations pour voir si nous avons saisi toutes les étapes que nous devons suivre dans le Critical Rendering Path (CRP).

1. Le navigateur commence par construire le DOM en analysant tout le HTML pertinent.
2. Il procède ensuite à l'examen des ressources CSS et JavaScript et les demande, ce qui se produit généralement dans l'en-tête où nous plaçons couramment nos liens externes.
3. Le navigateur analyse ensuite le CSS et construit le CSSOM, suivi de l'exécution du JavaScript.
4. Ensuite, le DOM et le CSSOM sont fusionnés dans l'arbre de rendu.
5. Nous exécutons ensuite les étapes de mise en page et de peinture pour présenter la page à l'utilisateur.

### D'accord, c'est bien à savoir — mais pourquoi est-ce important ?

Maintenant, tout cela est bien à savoir, et nous avons une meilleure compréhension de ce que le navigateur fait réellement en arrière-plan. Mais pourquoi est-ce exactement important ? Avons-nous tous besoin de savoir ce qui se passe sous le capot ?

**Oui, nous en avons besoin !**

Si nous continuons à augmenter la taille de nos fichiers et ne faisons pas attention à ce que nous demandons au navigateur de rendre et de peindre sur la page, le navigateur aura besoin de plus de temps pour traiter toutes les ressources. Cela se traduit généralement par une expérience utilisateur plus lente et moins agréable, ce qui signifie que les pages ne seront pas utilisables et rendues correctement, entraînant de la frustration du côté de l'utilisateur.

Cela est particulièrement vrai si vous demandez une page depuis une zone rurale où le haut débit rapide n'est pas nécessairement le meilleur.

Mais heureusement, il existe quelques moyens de contourner cela et nous pouvons rendre nos pages plus rapides !

![Image](https://cdn-media-1.freecodecamp.org/images/4enXiRx7lUm5Rn7vJjC23ZDoQAaxMeFvdtDZ)
_Photo par [Unsplash](https://unsplash.com/@pietsgallery?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Peter Finger</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Optimisation des performances

Il existe un certain nombre de stratégies que nous pouvons utiliser pour rendre nos pages plus rapides et meilleures à utiliser pour nos utilisateurs. Cela est particulièrement important pour les utilisateurs qui pourraient se trouver dans des endroits plus éloignés où un internet plus rapide n'est pas la norme ou où les pages sont couramment accessibles via l'internet mobile.

Lorsque nous parlons de stratégies d'optimisation, nous avons grossièrement trois techniques à notre disposition.

#### Minification, compression et mise en cache

Ces techniques peuvent toutes être appliquées à notre HTML, CSS et JS. Ensuite, grâce à leur taille réduite, elles réduiront la quantité de données que nous envoyons entre le client et le serveur. Moins nous avons de bytes à envoyer, plus le navigateur recevra rapidement les données et commencera à traiter et à rendre la page.

#### Minimiser l'utilisation des ressources bloquant le rendu (CSS)

Le CSS lui-même est bloquant pour le rendu comme nous l'avons discuté ci-dessus, ce qui signifie que le navigateur arrêtera de rendre la page jusqu'à ce que le CSS soit complètement chargé et traité.

Nous pouvons atténuer les effets des grands fichiers CSS, cependant, en débloquant le rendu pour certains styles et viewports. Nous faisons cela en utilisant des règles d'impression dans nos requêtes média, analytiques et orientation de l'appareil (si vous voulez savoir comment, je vous suggère de consulter les ressources ci-dessous). Nous pouvons également réduire le nombre de ressources devant être chargées en intégrant certains de notre CSS dans certaines circonstances.

#### Minimiser l'utilisation des ressources bloquant l'analyseur (JS document parser)

Nous pouvons également différer l'exécution de notre JavaScript et utiliser des attributs async sur notre script pour y parvenir. Cela signifie que le reste de la page peut être traité, et entre-temps, l'utilisateur voit une indication que quelque chose se passe sur la page. Cela signifie également que nous n'avons pas besoin d'attendre que le JavaScript se charge.

#### Donc, en termes généraux, cela nous laisse avec 3 modèles d'optimisation :

1. Minimiser le nombre d'octets que vous envoyez
2. Réduire le nombre de ressources critiques dans le chemin de rendu critique (les analytiques n'ont peut-être pas besoin d'être chargées dès le début lorsque la page est construite)
3. Raccourcir la longueur du chemin de rendu critique (ce qui signifie réduire le nombre d'allers-retours entre votre navigateur et le serveur nécessaires pour rendre la page)

### Essayez par vous-même

Si vous êtes impatient d'essayer cela et de commencer à optimiser, vous pouvez mesurer la performance de votre site web ou d'autres avec un certain nombre d'outils. Les plus faciles sont probablement les produits Google comme [PageSpeedInsights](https://developers.google.com/speed/pagespeed/insights/) ou [Google Lighthouse](https://developers.google.com/web/tools/lighthouse/), une petite extension Google Chrome pratique que vous pouvez facilement installer via le Chrome App Store.

Il suffit de cliquer sur l'extension, puis de générer un rapport et vous obtenez un rapport qui inclut les éléments suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/lyyGO2zINP098lQZ3h12kXIs4rR44zIjVhxt)
_Exemple d'un audit de performance dans Google Lighthouse sur mon site personnel — Le CSS bloquant le rendu pour deux ensembles d'icônes différents signifie que mon site subit un impact sur les performances (je réfléchis définitivement à la manière de réduire cela à l'avenir)_

Vous pouvez ensuite comparer vos performances à un certain nombre de métriques, telles que le premier pixel peint à l'écran, le premier interactif, la complétude visuelle de votre site, et bien d'autres.

Les outils de développement de votre navigateur préféré sont également un excellent endroit pour examiner les temps de chargement et les goulots d'étranglement de performance. Garder les temps de chargement globaux bas augmentera définitivement la vitesse globale à laquelle votre site est servi à vos utilisateurs finaux.

### Conclusion

Espérons que cela a jeté un peu de lumière sur le fonctionnement interne de la manière dont votre navigateur affiche une page et le travail intensif qu'il doit accomplir en arrière-plan pour s'assurer que votre HTML, CSS et JavaScript sont transformés correctement.

Être conscient de ces étapes nous aide à rendre les pages existantes plus performantes. Mais cela nous permet également d'être conscients de la manière dont nous développons des applications et des sites web et de considérer comment nos pages apparaissent pour les humains dans d'autres régions du monde.

#### Ressources

La plupart de mes connaissances que j'ai partagées ici, je les ai acquises grâce aux éléments suivants :

1. _Website Performance Optimisation_ sur [Udacity](https://eu.udacity.com/course/website-performance-optimization--ud884)
2. _Why Performance Matters_ sur [Google Developers](https://developers.google.com/web/fundamentals/performance/why-performance-matters/)
3. _High Performance Browser Networking_ par Ilya Grigorik ([https://hpbn.co/](https://hpbn.co/))
4. _High Performance Websites: Essential Knowledge for Front-end Engineers_ par Steve Souders