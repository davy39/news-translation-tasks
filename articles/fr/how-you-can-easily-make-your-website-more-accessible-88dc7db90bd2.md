---
title: Comment rendre votre site web plus accessible facilement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-18T09:51:24.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-easily-make-your-website-more-accessible-88dc7db90bd2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uCdCezP7OthCclgq_fDM7Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre site web plus accessible facilement
seo_desc: 'By Jaroslav Vaňkát

  As a designer, developer, or even product manager, you have thousands of responsibilities.
  Every project requires a lot of attention — desktop layout, mobile layout, iPhone
  X layout (thanks, Apple), IE support, Safari support…

  So w...'
---

Par Jaroslav Vaňkát

En tant que designer, développeur, ou même chef de produit, vous avez des milliers de responsabilités. Chaque projet nécessite beaucoup d'attention — mise en page desktop, mobile, iPhone X (merci, Apple), support IE, support Safari…

#### Pourquoi devriez-vous vous soucier de l'accessibilité ?

Voici quelques faits marquants :

* Environ 15 % de la population mondiale vit avec une forme de handicap, dont 2–4 % rencontrent des difficultés significatives dans leur fonctionnement. ([Organisation Mondiale de la Santé](http://www.who.int/disabilities/world_report/2011/report/en/))
* Tout le monde est parfois temporairement handicapé — dans un sens — que vous vous soyez coupé le doigt ou que vous essayiez de lire sur votre écran à faible contraste un jour ensoleillé.
* Dans certains cas, l'accessibilité peut être requise par la loi.

Et surtout :

> Tout le monde est un utilisateur de clavier lorsqu'il mange avec sa main sur la souris.

> — Adrian Roselli

En améliorant l'accessibilité de votre site web, vous ne soutenez pas seulement les personnes handicapées. Vous le rendez simplement plus utilisable pour tout le monde.

### Ne réinventez pas la roue

Chez [Site Search 360](https://sitesearch360.com/), nous avons développé un plugin qui permet à nos clients d'intégrer facilement notre solution de recherche dans un site web existant.

Alors que nous avons grandi, il était clair pour nous que nous devions effectuer un audit d'accessibilité. Oui, nous aurions dû considérer l'accessibilité dès le début du projet, mais il n'est jamais trop tard.

Vous n'activez pas simplement l'accessibilité.

Mais ne vous inquiétez pas. Même si vous n'avez jamais pensé à l'accessibilité dans votre projet actuel, il ne faudra pas longtemps pour apporter quelques améliorations. Je ne peux pas vous dire le temps exact que nous avons passé à rendre notre plugin plus accessible, mais ce n'était pas plus de quelques jours de travail (et environ 30 commits).

Je vais maintenant illustrer tout le processus (basé sur notre plugin JavaScript, pas un site web), afin que vous n'ayez pas à commencer depuis le très début. Mais d'abord :

### Qu'est-ce que l'accessibilité ?

Avant de vous mettre au travail, vous devez comprendre ce qu'est réellement l'accessibilité. Je ne vais pas vous ennuyer avec de longues définitions. Cette courte phrase résume l'accessibilité telle que je la conçois :

L'accessibilité est l'art de rendre votre produit utilisable par tout le monde.

Qui est tout le monde ? Quels types de handicaps devriez-vous considérer ?

* Cécité et daltonisme
* Handicaps cognitifs
* Handicaps physiques
* Handicaps auditifs (oui, vos vidéos ont besoin de sous-titres)
* Âge

### Quelques étapes faciles

Maintenant que vous savez pour qui vous améliorez votre site web, nous pouvons commencer à examiner les concepts de base d'un web accessible.

#### Écrivez un balisage sémantique

C'est probablement l'étape la plus importante. HTML5 est parmi nous depuis quelques années maintenant, donc il n'y a aucune raison (et aucune excuse) de ne pas en tirer parti. _Section, article, header, nav, banner_ et bien d'autres — toutes ces balises sont là pour être utilisées.

Vous avez probablement vu un balisage comme ceci (j'ai omis les classes et les ids car ils n'ont aucun but sémantique) :

```
<div>  <div>Recettes<span>98</span></div>  <div>Éléments de menu<span>1</span></div>  <div>Produits d'épicerie<span>1</span></div></div>
```

Croyez-le ou non, c'était notre navigation de groupe de contenu (vous pouviez cliquer sur un groupe de contenu et la page de résultats de recherche faisait défiler automatiquement vers les résultats de recherche pertinents). Vous ne l'auriez pas deviné, n'est-ce pas ?

Il y a quelques problèmes avec ce balisage. Comment quelqu'un qui dépend des technologies d'assistance peut-il savoir que c'est une navigation ? Ils ne peuvent pas. Un élément actif est-il représenté par _div_ ? Oui, c'est le cas.

Regardez maintenant le morceau de balisage suivant :

```
<nav role="navigation">  <ul role="menubar">    <li>      <button role="menuitem">Recettes<span>98</span></button>    </li>    <li>      <button role="menuitem">Éléments de menu<span>1</span></button>    </li>    <li>      <button role="menuitem">Produits d'épicerie        <span>1</span>      </button>    </li>  </ul></nav>
```

Beaucoup mieux, n'est-ce pas ? Passons en revue les concepts les plus importants du balisage sémantique :

* Utilisez des éléments sémantiques
* Utilisez toujours _<main role="main"> pour marquer le contenu principal
* Ajoutez l'attribut _role_ pour supporter les anciens navigateurs
* Utilisez des sections au lieu de divs lorsque c'est approprié
* _Span_ n'est pas un _button_ — ne détournez pas le sens des éléments (sauf si absolument nécessaire)
* Utilisez des _buttons_ pour les interactions dans la page
* Les en-têtes sont l'une des parties les plus importantes de chaque page web. Ayez toujours un seul en-tête _h1_ et ne sautez pas les niveaux d'en-tête

Je ne vais pas lister chaque changement que nous avons fait (et il y en a beaucoup), mais vous pouvez toujours demander dans les commentaires.

**Ce qu'il faut faire :** Passez en revue votre balisage actuel, vérifiez la structure du contenu et des en-têtes, assurez-vous que les éléments interactifs sont représentés par un _button_ ou des éléments, et utilisez les balises sémantiques HTML5.

#### Rendez toutes les fonctionnalités disponibles avec un clavier

C'est aussi un point important. Chaque interaction doit être possible avec un clavier.

Prenons un exemple similaire au précédent. Nous avions un bouton "Afficher plus de résultats" qui n'était pas réellement un bouton. Pouvez-vous deviner ? Oui, c'était un _div_ stylisé.

Pouvions-nous supporter les contrôles clavier pour un tel élément ? Oui, nous pouvions, en le rendant focusable et en gérant les événements _click_ et _keyup_ tout en testant si la touche _enter_ ou _space_ était pressée.

Néanmoins, c'est encore plus difficile que de simplement changer le balisage de _<div> à <button> — dans ce cas, vous devez simplement lier un événement de clic et ne pas avoir à forcer l'élément DOM à être focusable (et en bonus, vous n'avez pas à écrire autant de styles).

Points clés :

* Toutes les fonctionnalités doivent être accessibles par clavier
* Ne supprimez pas les contours des éléments focusés (si vous n'aimez pas ces contours, [vous pouvez toujours les styliser](https://css-tricks.com/almanac/properties/o/outline/))
* Les interactions dans la page doivent être représentées par un _button_
* Les interactions hors page (liens) doivent être représentées par une ancre (_<a>_)
* Les boutons sont destinés à être déclenchés par un clic, enter et space, les ancres par un clic et une pression sur enter

**Ce qu'il faut faire :** Assurez-vous que tous les éléments interactifs sont accessibles (et contrôlables) par clavier, que les éléments focusés sont mis en évidence, et que l'ordre de tabulation a réellement du sens.

#### Supportez les lecteurs d'écran

Jetez un œil à l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SK1QQ_SJ4N7LwQQkqLJ5NQ.jpeg)
_Couche Site Search 360 telle que vue par les personnes voyantes._

Il devrait être facile de deviner ce que fait le bouton dans le coin supérieur droit. Il ferme la couche. L'image suivante simule ce qu'une personne aveugle serait capable de "voir" en utilisant un logiciel de lecteur d'écran :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2MHSkfIy4KyJd7BC3bYxyw.jpeg)
_Couche Site Search 360 telle que vue par les personnes aveugles._

Vous avez déjà vu l'image complète, donc vous savez quelle action le même bouton est censé effectuer. Pourriez-vous le deviner en regardant la deuxième image ? Vous ne pourriez pas — la croix est rendue en utilisant une propriété CSS background-image et le bouton n'a aucun contenu interne.

C'est à cela que servent les attributs _aria-*_. En améliorant le balisage du bouton avec un simple attribut _aria-label_, vous n'avez pas à essayer de faire en sorte que le texte interne du bouton soit caché dans votre couche de présentation.

```
<!-- Mauvais balisage --><button></button>
```

```
<!-- Balisage accessible --><button aria-label="Fermer la couche"></button>
```

```
<!-- Balisage accessible alternatif --><button style="text-indent:100%;overflow:hidden;padding:0;white-space:nowrap;">Fermer la couche</button>
```

Avez-vous remarqué que j'ai également supprimé les images de la vue du lecteur d'écran ? Vous pouvez également les étiqueter en utilisant la même technique (où _aria-labeledby_ pourrait être plus approprié). J'ai supprimé ces images car dans notre cas, elles n'ont aucun but sémantique et sont marquées avec _role="presentation"_. Même si elles avaient un but sémantique, nous ne le savons généralement pas. La plupart de ces images seront illustratives, et les étiqueter serait redondant — l'en-tête porte déjà le même sens.

Attributs que vous devriez connaître :

* _role_ — utile pour marquer le but d'un élément
* _aria-hidden_ — indique aux technologies d'assistance d'ignorer un élément
* _aria-label, aria-labeledby_ — étiqueter l'élément
* _aria-describedby_ — utilisez ceci pour décrire les contrôles d'interface utilisateur non standard
* _aria-owns_ — marque une relation entre deux éléments

**Ce qu'il faut faire :** Cette étape peut être la plus difficile à mettre en œuvre correctement et à tester correctement. Assurez-vous que toutes les images ont un attribut _alt_, que toutes les sections et éléments interactifs sont étiquetés, et testez avec un logiciel de lecteur d'écran.

**Comment tester :** Utiliser un lecteur d'écran en tant que personne voyante peut ne pas sembler naturel, alors prenez d'abord un peu de temps et familiarisez-vous avec le logiciel de votre choix (et vous pourriez vouloir tester tous les plus courants — [VoiceOver](https://www.apple.com/accessibility/mac/vision/) sur Mac, [NVDA](https://webaim.org/articles/nvda/), et [Jaws](https://webaim.org/articles/jaws/) sur Windows et [TalkBack](https://play.google.com/store/apps/details?id=com.google.android.marvin.talkback&hl=cs) sur Android). Après cela, essayez de naviguer sur votre site web en utilisant uniquement le logiciel de lecteur d'écran (éteignez votre moniteur). Même un test court vous aidera à vous faire une idée de la performance de votre site web et révélera les problèmes les plus significatifs.

**Bonus :** Voici un exemple court (et un peu simplifié) de la façon dont nous avons amélioré nos autosuggestions. Les parties surlignées (et les deux _<span>_) ont été ajoutées dans le cadre de nos améliorations d'accessibilité.

```
<!-- Champ de recherche --><input type="text" placeholder="rechercher quelque chose"   autocomplete="off"   role="combobox"   aria-describedby="unibox-controls-description"   aria-owns="unibox-suggest-box"   aria-expanded="true"  aria-activedescendant="unibox-active">
```

```
<!-- Suggestions de recherche --><div id="unibox-suggest-box" role="listbox">;  <section aria-labelledby="unibox-suggest-cluster-heading-recettes">    <h3 id="unibox-suggest-cluster-heading-recettes">Recettes</h3>    <div aria-selected="false" role="option">      <img src=[...]         alt=""         aria-hidden="true"         role="presentation">      </div>      <a href=[..]>Poulet Curry</a>    </div>    <div aria-selected="true" role="option" id="unibox-active">      <img src=[...]         alt=""         aria-hidden="true"         role="presentation">      </div>      <a href=[..]>Poulet Curried</a>    </div>  </section>  </div>
```

```
<!-- Annoncer que les suggestions de recherche ont été modifiées --><span aria-live="polite" aria-atomic="true" role="status" class="ss360-sr-only">2 Suggestions de Recherche Affichées</span>
```

```
<!-- Contrôles de l'Interface Utilisateur de la Boîte de Suggestions --><span id="unibox-controls-description" class="ss360-sr-only">Utilisez les flèches haut et bas pour sélectionner le résultat disponible. Appuyez sur entrer pour aller au résultat de recherche sélectionné.</span>
```

#### Simplifiez la présentation

Accessibilité, Design UI, UX — toutes ces facettes sont les côtés d'une même pièce à trois faces.

Un faible contraste entre l'arrière-plan et le premier plan rendra votre texte difficile à lire.

Les animations sauvages rendent votre site web difficile pour les personnes en gueule de bois (vous ne vous en souciez pas ? Pensez plutôt à ceux qui souffrent de TDAH — ils peuvent trouver difficile de se concentrer). Saviez-vous qu'il existe une requête média _prefers-reduced-motion_ (même si elle n'est pas encore largement supportée) ? Vous pouvez simplement désactiver toutes vos animations si cette requête média est définie. Voici comment nous le faisons :

```
if(window.matchMedia &&   window.matchMedia("(prefers-reduced-motion: reduce)").matches){    animationSpeed = 0;}
```

> Vous ne pensez pas qu'un site web devrait être une sorte de spectacle de lumière stroboscopique folle, n'est-ce pas ?

Transmettre des informations uniquement par la couleur rendra les informations inaccessibles pour les personnes daltoniennes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dKxQL7ZYNIblkZNlXrgkmQ.jpeg)
_Exemple classique — les boutons bascule fonctionnent sans couleur._

Voici un exemple de la façon dont nous avons changé la mise en page par défaut de notre vue de superposition — des blocs de texte plus courts et des ratios de contraste plus élevés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y8GYLqsaPoRJ8iW3TzUeSw.jpeg)
_L'ancien look par défaut de notre superposition._

![Image](https://cdn-media-1.freecodecamp.org/images/1*p6cWlFXDWggkXPecyUHKHA.jpeg)
_Le nouveau look par défaut pour notre superposition._

L'un de nos points de douleur a toujours été les autosuggestions mobiles. Cela peut être moins un problème d'accessibilité, mais nous avons enfin ajouté une option pour passer aux autosuggestions en plein écran. Voici une comparaison :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFNLYS8lSNZZoYy487bfwQ.gif)
_Autosuggestions par défaut._

![Image](https://cdn-media-1.freecodecamp.org/images/1*0TvVZaH1RW0UeEG20NglEQ.gif)
_Nouvelles autosuggestions mobiles._

**Ce qu'il faut faire :**

* Vérifiez que les blocs de texte ne sont pas plus larges que 80 caractères et utilisez une _line-height_ environ 1,5 fois plus grande que la _font-size_ (qui doit également être suffisamment grande — optez pour 16 px et plus)
* Autorisez le zoom (au moins jusqu'à 200%)
* [Vérifiez vos ratios de contraste](https://webaim.org/resources/contrastchecker/)
* Assurez-vous que vos cibles tactiles sont suffisamment grandes (44 x 44 pixels est la règle générale)
* Lorsque la couleur transmet des informations, assurez-vous qu'il existe également une autre manière d'obtenir les mêmes informations
* Passez en revue vos animations et considérez si vous en avez vraiment besoin. Fournissez également un mécanisme pour les désactiver.
* Oubliez les captchas…

#### Évaluez, évoluez et intégrez votre flux de travail

Celui-ci n'est ici que parce que "5 étapes" sonne mieux que "4 étapes". Quoi qu'il en soit, concentrez-vous toujours sur l'accessibilité dans votre flux de travail quotidien (ou au moins hebdomadaire).

Vous n'aurez pas à dépenser de grandes sommes de votre budget pour faire cela correctement. Donc, lors de la planification d'une nouvelle fonctionnalité, pensez à tous les groupes que j'ai nommés dans la partie "Qu'est-ce que l'accessibilité ?" de cet article.

### Test

Il existe [beaucoup d'outils](https://www.w3.org/WAI/ER/tools/) qui vous aideront à évaluer l'accessibilité de votre site web. Je recommanderais [Tenon.io](https://tenon.io/), [FAE](https://fae.disability.illinois.edu/anonymous/), et Lighthouse pour Google Chrome (ouvrez les outils de développement, allez dans Audits, et cliquez sur 'Effectuer un audit…').

Cependant, certaines choses sont difficiles à évaluer avec des outils automatisés. Essayez d'utiliser votre site web en utilisant uniquement un clavier. Ensuite, essayez de l'utiliser avec un logiciel de lecteur d'écran.

### Sources supplémentaires

Il y a beaucoup plus à dire sur l'accessibilité que ce que cet article peut couvrir. Voici donc quelques ressources qui pourraient vous aider à approfondir le sujet :

* [**Comment répondre aux WCAG 2.0**](https://www.w3.org/WAI/WCAG20/quickref/)
* [Tutoriels WAI](https://www.w3.org/WAI/tutorials/)
* [Liste de contrôle pour le design inclusif](https://github.com/Heydon/inclusive-design-checklist)
* [Un bel article de l'équipe Freecodecamp](https://medium.freecodecamp.org/next-level-accessibility-freecodecamp-guide-7cbd6473eabd)

### TL;DR

Utilisez un balisage sémantique, supportez les lecteurs d'écran, rendez tous les éléments interactifs accessibles par clavier, simplifiez votre présentation, et lisez au moins tous les points dans "Quelques étapes faciles".

Ok, c'est tout. Si vous êtes intéressé par les changements exacts que nous avons apportés, demandez simplement dans les commentaires. Et si vous cherchez une solution de recherche de site qui se soucie de l'accessibilité (ou simplement une alternative à Google Site Search), [Site Search 360 est là pour vous](https://sitesearch360.com/).

**Et n'oubliez pas d'applaudir.**