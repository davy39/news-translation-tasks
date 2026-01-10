---
title: "Tableau de bord Unity\n\x14\nles leçons apprises en développant nos frontends,\
  \ notre culture de développement et nos processus"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T14:41:41.000Z'
originalURL: https://freecodecamp.org/news/unity-dashboard-lessons-learned-scaling-our-frontends-development-culture-and-processes-d28f429bd70e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rUtnJRnd_CvejLsYapq3-g.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: scaling
  slug: scaling
- name: 'tech '
  slug: tech
seo_title: "Tableau de bord Unity\n\x14\nles leçons apprises en développant nos frontends,\
  \ notre culture de développement et nos processus"
seo_desc: 'By Maciej Gurban

  At Unity, we’ve recently set out to improve our Dashboards — an undertaking which
  dramatically changed not only our frontend tech stack, but also the ways we work
  and collaborate.

  We’ve developed best practices and tooling to help us...'
---

Par Maciej Gurban

Chez Unity, nous avons récemment entrepris d'améliorer nos Tableaux de bord  une entreprise qui a non seulement radicalement changé notre stack technique frontend, mais aussi la façon dont nous travaillons et collaborons.

Nous avons développé des meilleures pratiques et des outils pour nous aider à développer notre architecture frontend, à construire des produits avec une excellente UX et performance, et à livrer de nouvelles fonctionnalités plus rapidement.

Cet article rassemble ces pratiques et vise à fournir autant de raisonnement que possible derrière chaque décision. Mais d'abord, un peu de contexte.

### L'Héritage

En regardant le nombre d'ingénieurs, Unity a plus que quadruplé ses effectifs au cours des 4 dernières années. Alors que l'entreprise a grandi à la fois organiquement et par le biais d'acquisitions, son offre de produits a également augmenté. Alors que les produits développés initialement chez Unity étaient largement uniformes en termes de technologie et de langage de design, les nouveaux acquis ne l'étaient naturellement pas.

En conséquence, nous avions plusieurs tableaux de bord visuellement distincts qui fonctionnaient et se comportaient différemment et qui ne partageaient aucun élément de navigation commun. Cela a entraîné une mauvaise expérience utilisateur et des utilisateurs frustrés. Au sens très littéral, l'état des frontends de nos produits nous coûtait des revenus.

Après avoir analysé le portefeuille de nos produits, nous avons identifié trois sections distinctes que le Tableau de bord Unity serait divisé en : Développer, Opérer et Acquérir, chacune satisfaisant un besoin commercial différent et destinée à différents groupes de clients, contenant ainsi des ensembles de fonctionnalités largement indépendants les uns des autres.

Cette nouvelle structure, et l'introduction d'éléments de navigation communs visaient à résoudre le premier problème majeur auquel nos utilisateurs étaient confrontés  où trouver les informations et les options de configuration qu'ils recherchent, et bien que tout cela semblait bon sur le papier, le chemin pour y parvenir était loin d'être évident.

#### Considérations

Beaucoup de nos développeurs étaient très enthousiastes à l'idée de passer à React et à sa stack technique plus moderne. Comme ces solutions avaient été testées en bataille dans de grandes applications, et que leurs meilleures pratiques et conventions étaient pour la plupart bien établies, les choses semblaient très prometteuses.

Néanmoins, ce que nos développeurs connaissaient le mieux et ce dans quoi la plupart de nos applications en développement actif étaient écrites était AngularJS. Décider de commencer à migrer tout en une seule fois aurait été une catastrophe en attente de se produire. Au lieu de cela, nous avons entrepris de tester nos hypothèses à une échelle beaucoup plus petite d'abord.

Peut-être le groupe de produits le plus disjoint que nous ayons eu étaient les **tableaux de bord de Monétisation**. Ces projets, qui finiraient par se retrouver sous l'égide du **tableau de bord Opérer**, étaient vastement différents à presque tous les égards possibles : technologies utilisées, approche de l'UI/UX, pratiques de développement, conventions de codage  vous l'appelez.

Voici à quoi la situation ressemblait approximativement :

![Image](https://cdn-media-1.freecodecamp.org/images/M-8Rbct9m1hh-Nzbknh2DsLBsRerT9yr2sOv)
_État de nos tableaux de bord en avril 2018. Projets utilisant Angular vs ceux utilisant React._

Après quelques séances de brainstorming, nous avons identifié les principaux domaines sur lesquels nous devions travailler pour rassembler tous les produits :

#### 1. Un seul produit

Nous avions besoin que ces tableaux de bord (répartis sur plusieurs applications, domaines et stacks techniques) :

* Donnent l'impression d'être un seul produit (pas de redirections de page complète lorsque l'utilisateur navigue à travers les pages de toutes les différentes applications)
* Aient une apparence et une sensation cohérentes
* Incluent des éléments de navigation communs toujours visibles et identiques, peu importe quelle partie du tableau de bord l'utilisateur visite

#### 2. Support de l'héritage

Bien que nous ayons eu une ardoise propre en ce qui concerne le choix technologique de notre nouvelle solution frontend, nous devions accommoder les projets hérités qui devaient être intégrés dans le nouveau système. Une solution qui n'impliquait pas de gros efforts de refactorisation, et qui n'arrêterait pas le développement de fonctionnalités, ou ne traînerait pas pendant des mois sans fin en vue.

#### 3. Pratiques et outils

Bien que presque toutes les équipes utilisaient AngularJS, différents outils étaient utilisés pour répondre au même ensemble de défis. Différents runners de test et bibliothèques d'assertion, solutions de gestion d'état ou leur absence, jQuery vs sélecteurs natifs du navigateur, SASS vs LESS, bibliothèques de graphiques, etc.

#### 4. Productivité des développeurs

Puisque chaque équipe avait sa propre solution pour développer, tester et construire son application, l'environnement de développement était souvent truffé de bugs, d'étapes manuelles et d'inefficacités.

De plus, beaucoup de nos équipes travaillent dans des lieux séparés par une différence de 10 heures (Helsinki, Finlande et San Francisco), ce qui rend la prise de décision efficace sur toute pièce partagée un vrai défi.

### Le Nouveau

Nos principaux domaines de concentration étaient :

1. Encourager et préserver les méthodes de travail agiles dans nos équipes, et laisser les équipes être largement indépendantes les unes des autres
2. Tirer parti et développer des outils et conventions communs autant que possible, les documenter, et les rendre facilement accessibles et utilisables

Nous croyions que la réalisation de ces objectifs améliorerait significativement notre temps de mise sur le marché et la productivité des développeurs. Pour que cela se produise, nous avions besoin d'une solution qui :

* **Construise des fonctionnalités de produit avec une meilleure expérience utilisateur**
* **Améliore la qualité du code**
* **Permette une meilleure collaboration** sans bloquer le progrès du travail de quiconque dans le processus.

Nous voulions également encourager et faciliter le passage à une stack technique moderne pour rendre nos développeurs plus satisfaits de leur travail, et pour, avec le temps, nous éloigner de nos frameworks et outils antiqués.

Le résultat en constante évolution de notre travail est une SPA basée sur React construite à l'intérieur d'un monodépôt où toutes les pages et les fonctionnalités plus importantes sont construites en bundles de code largement indépendants chargés à la demande, et qui peuvent être développés et déployés par plusieurs équipes en même temps.

Comme moyen de sandboxer toutes les applications héritées tout en les affichant dans le contexte de la même nouvelle application, nous les chargeons à l'intérieur d'un iframe depuis lequel elles peuvent communiquer avec la SPA principale en utilisant un bus de messages implémenté avec l'API `[postMessage()](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)`.

### Le monodépôt

Voici la structure de répertoire avec laquelle nous avons commencé :

```
/src   /components  /scenes    /foo      /components      package.json      foo.js    /bar      /components      package.json      bar.js package.json index.js
```

Le `package.json` dans le répertoire racine contient un ensemble de `devDependencies` responsables de l'environnement de développement, de test et de construction de l'application entière, mais contient également les `dependencies` du cœur de l'application (plus à ce sujet un peu plus tard).

Toutes les parties plus grandes de l'UI sont appelées _scènes_. Chaque _scène_ contient un `package.json` où les `dependencies` utilisées par les composants de cette scène sont définies. Cela rend deux choses possibles :

1. **Les mises à jour de déploiement ne concernent que les fichiers qui ont changé**  
L'étape de construction compile des bundles séparés pour chaque scène, nommant chacun en utilisant un hash qui changera uniquement lorsque le contenu du fichier aura changé. Cela signifie que nos utilisateurs ne téléchargent que les fichiers qui ont changé depuis leur dernière visite, et rien de plus.
2. **Les scènes sont chargées uniquement lorsque nécessaire**  
Nous chargeons toutes les scènes de manière asynchrone et à la demande, ce qui améliore considérablement les temps de chargement de l'application entière. Le « à la demande » ici signifie généralement visiter une route spécifique, ou effectuer une action UI qui effectue un [import de module dynamique](https://github.com/tc39/proposal-dynamic-import).

Voici à quoi ressemble une telle configuration en pratique (simplifiée pour la lisibilité) :

```
// Dans src/routes.jsconst FooLoader = AsyncLoadComponent( () => import('src/scenes/foo/foo'), GenericPagePreloader,);
```

```
<Route path="/foo" component={FooLoader) />
```

```
// Dans src/scenes/foo/foo.js<React.Suspense fallback={GenericPagePreloader}> <Component /></React.Suspense>
```

`AsyncLoadComponent` est un wrapper léger autour de `[React.lazy()](https://reactjs.org/docs/code-splitting.html#reactlazy)`, acceptant en plus un composant de préchargement, le même que celui passé en fallback à `[React.Suspense()](https://reactjs.org/docs/code-splitting.html#suspense)`, et un délai après lequel le préchargement doit être rendu si la scène n'a pas fini de charger.

Cela est utile pour s'assurer que nos utilisateurs voient le même préchargement sans aucune interruption ou flash de contenu du moment où une scène est demandée au moment où tous ses fichiers ont été téléchargés, toutes les requêtes API critiques ont été complétées, et le composant a fini de rendre.

### Niveaux de composants

À mesure que chaque application grandit, sa structure de répertoire et ses abstractions évoluent avec elle. Après environ six mois de construction et de déplacement de fonctionnalités vers la nouvelle base de code, avoir un seul répertoire _composants_ s'est avéré insuffisant.  
Nous avions besoin que notre structure de répertoire nous informe sur :

* Les composants ont-ils été développés pour être génériques, ou sont-ils destinés à un cas d'utilisation spécifique ?
* Sont-ils suffisamment génériques pour être utilisés dans toute l'application, ou doivent-ils être utilisés uniquement dans certains contextes ?
* Qui est responsable et le plus connaisseur du code ?

Sur cette base, nous avons défini les **Niveaux de Composants** suivants :

#### 1. Spécifique à l'application (src/app)

Composants à usage unique qui répondent à des cas d'utilisation spécifiques au sein de cette application, et qui ne sont pas destinés à être réutilisés ou extraits dans la bibliothèque de composants (routes, pied de page, en-tête de page, etc.).

#### 2. Générique (src/components)

Composants multi-usage génériques à utiliser dans toute l'application et ses scènes. Une fois que nous avons atteint une API stable pour ces composants, ils pourraient être déplacés dans la bibliothèque de composants commune (plus à ce sujet ci-dessous)

#### 3. Composants d'une seule scène (src/scenes/my-scene/components)

Composants développés avec un cas d'utilisation spécifique en tête ; non destinés à être utilisés dans d'autres scènes. Pour les cas où un composant d'une scène doit être utilisé dans une autre, nous utiliserions :

#### 4. Composants multi-scènes (src/scenes/components/my-feature)

Composants utilisés dans plusieurs scènes, mais non destinés à être suffisamment génériques pour être utilisés ailleurs. Pour illustrer pourquoi les déplacer simplement dans `src/components` n'est pas suffisant :

Imaginez que jusqu'à présent vous aviez une seule scène qui contenait des composants utilisés pour construire des graphiques de données plutôt spécifiques. Votre équipe construit maintenant une deuxième scène qui utilisera différentes données pour les graphiques, mais visuellement les deux seront presque identiques.

Importer des composants d'une scène dans une autre briserait l'encapsulation de la scène et signifierait que nous ne pouvons plus être certains que les changements apportés aux composants d'une seule scène n'affectent que cette scène.

À cette fin, tout composant ou groupe de composants, grossièrement appelé une fonctionnalité, serait placé dans `src/scenes/components` d'où il peut être importé et utilisé par toute autre équipe, cependant :

Chaque fois qu'une équipe souhaite commencer à utiliser des composants de scène développés par une autre équipe, la meilleure pratique serait de contacter cette équipe en premier pour déterminer si le cas d'utilisation que vous prévoyez pour ces composants peut être pris en charge en toute sécurité à l'avenir. Donner un avertissement à l'équipe qui a initialement développé le code empêchera la livraison de fonctionnalités cassées à l'avenir lorsque le code que vous avez pris en utilisation change inévitablement de manière inattendue (parce que, bien sûr, comment pourriez-vous le savoir !), et qui ne sont pas toujours détectées par les tests unitaires.

#### 5. Bibliothèque commune

Composants que nous avons testés en production et que nous souhaitons extraire dans notre bibliothèque de composants partagée, utilisée par d'autres équipes de tableau de bord chez Unity.

### Ode aux dépendances partagées

Bien qu'il serait très pratique de pouvoir construire et déployer chaque partie de notre application dans un environnement entièrement isolé, certaines dépendances  à la fois des bibliothèques externes et du code interne de l'application  seront simplement utilisées dans toute la base de code. Des choses comme React lui-même, Redux et toute la logique liée à Redux, les composants de navigation communs, etc.

#### Déploiement des changements

À l'heure actuelle, l'encapsulation complète des scènes n'est pas pratique et dans de nombreux cas simplement impossible. Cela nécessiterait soit l'envoi de nombreuses dépendances à plusieurs reprises et en ralentissant les chargements de pages, soit la construction d'abstractions destinées à faire fonctionner certaines bibliothèques de manière à laquelle elles n'ont pas été conçues.

Cependant, à mesure que le développement web et son écosystème évoluent, les bibliothèques semblent devenir de plus en plus autonomes et encapsulées, ce qui, nous l'espérons, signifiera à l'avenir peu ou pas de dépendances partagées, et une véritable isolation entre tous les modules.

> Peut-être le plus grand inconvénient de la création d'applications à grande échelle est d'effectuer des changements de code et des mises à jour de dépendances sans casser quelque chose dans le processus

L'utilisation d'un monodépôt rend possible (bien que non obligatoire) le déploiement de changements et de mises à jour du code de manière plus progressive et sûre  si un changement cause des problèmes, ces problèmes n'affecteront qu'une petite partie de l'application, et non l'ensemble du système.

Et bien que pour certains, la capacité d'effectuer des mises à jour sur plusieurs zones non liées de la base de code en même temps pourrait sembler un avantage, la réalité d'avoir plusieurs équipes travaillant sur la même base de code et ne connaissant pas toutes les fonctionnalités des autres équipes en profondeur signifie qu'une grande prudence est nécessaire lors de la construction de l'échafaudage de l'application et de la prise de mesures pour minimiser le risque de casse.

#### Comment éviter de casser les choses

Peut-être la stratégie la plus fondamentale qui nous aide à le faire, autre que l'isolation des scènes, est d'avoir une **couverture de tests unitaires élevée**.

1. **Tests**

Les tests unitaires ne sont bien sûr pas tout  de nombreux produits matures, même à une échelle modérée, investissent après tout dans des suites de tests d'intégration et e2e qui font un meilleur travail de vérification si l'application fonctionne comme prévu dans l'ensemble. Cependant, à mesure que le nombre de fonctionnalités augmente, le coût de maintenance et le temps nécessaire pour les exécuter augmentent également  un coût qui ne peut pas toujours être justifié pour des fonctionnalités moins cruciales mais toujours importantes.

**Quelques leçons que nous avons apprises de diverses stratégies de test :**

* Essayez de tester unitairement autant de code que possible, surtout : la logique conditionnelle, les transformations de données et les appels de fonction
* Investissez et tirez parti des tests d'intégration à leur plein potentiel avant de décider d'écrire des tests e2e. Le coût initial des tests d'intégration est beaucoup plus élevé, mais pâlit en comparaison du prix de l'entretien d'une suite e2e
* Essayez de ne pas surréagir en commençant à écrire des tests e2e pour des choses qui n'ont pas été détectées par les tests unitaires ou d'intégration. Parfois, les processus ou les outils sont en faute
* Laissez les cas de test expliquer le comportement de l'UI plutôt que les détails d'implémentation
* Les tests automatisés ne peuvent pas remplacer entièrement les tests manuels

**2. Minimiser la surface du code partagé**

Outre les tests, le code réutilisé dans toute l'application est maintenu à un minimum raisonnable. L'une des stratégies les plus utiles jusqu'à présent a été de déplacer les composants et le code les plus couramment utilisés vers une bibliothèque de composants partagée, d'où ils sont utilisés comme dépendances dans les scènes qui en ont besoin. Cela nous permet de déployer la plupart des changements de manière progressive, sur une base par équipe ou par page.

**3. Responsabilité**

Enfin, mais non des moindres, un énorme facteur permettant à plusieurs équipes de collaborer au sein de la même base de code vient de l'encouragement et de la prise de **responsabilité personnelle et de responsabilité des développeurs pour le produit**, au lieu de déleser la responsabilité de tester correctement que tout fonctionne à l'assurance qualité, aux testeurs ou à l'automatisation.

Cela se répercute également sur les revues de code. S'assurer que chaque changement est soigneusement examiné est plus difficile qu'il n'y paraît en surface. Comme les équipes travaillent en étroite collaboration, un degré de confiance sain se développe entre ses membres. Cette confiance, cependant, peut parfois se traduire par le fait que les gens sont moins diligents quant aux changements apportés par les développeurs plus expérimentés ou autrement dignes de confiance.

Pour encourager la diligence, nous soulignons que **l'auteur de la PR et le relecteur sont également responsables de s'assurer que tout fonctionne**.

### Bibliothèque de composants

Pour obtenir la même apparence et la même sensation sur toutes les pages de nos tableaux de bord, nous avons développé une bibliothèque de composants. Ce qui distingue notre approche, c'est que de nouveaux composants sont presque jamais développés au sein de cette bibliothèque.

Chaque composant, après avoir été développé dans la base de code du tableau de bord, est d'abord utilisé dans un ensemble de fonctionnalités au sein de cette base de code. Habituellement, après quelques semaines, nous commençons à nous sentir plus confiants que le composant pourrait être déplacé, à condition que :

* L'API soit suffisamment flexible pour supporter les cas d'utilisation prévisibles
* Le composant ait été testé dans une variété de contextes
* La performance, la réactivité et l'UX soient toutes prises en compte

Ce processus suit la [Règle des Trois](https://blog.codinghorror.com/rule-of-three/) et vise à nous aider à **publier uniquement des composants qui sont véritablement réutilisables** et qui ont été utilisés dans une variété de contextes avant d'être déplacés dans notre bibliothèque commune.

Certains des exemples de composants que nous déplacerions incluent : pied de page, en-tête de page, éléments de navigation latéraux et supérieurs, blocs de construction de mise en page, bannières, versions améliorées de boutons, éléments de typographie, etc.

Dans les premiers jours, la bibliothèque de composants était située dans la même base de code que l'application elle-même. Nous l'avons depuis extraite dans un dépôt séparé pour rendre le processus de développement plus démocratisé pour les autres équipes chez Unity  important pour en favoriser l'adoption.

#### Conception modulaire des composants

Pendant très longtemps, la construction de composants réutilisables signifiait traiter avec plusieurs défis, dont beaucoup n'avaient souvent pas de bonnes solutions :

* Comment importer facilement le composant avec ses styles, et seulement cela
* Comment remplacer les styles par défaut sans guerres de spécificité de sélecteur
* Dans les composants plus grands composés de plusieurs plus petits, comment remplacer le style du plus petit composant

Notre tableau de bord, ainsi que notre bibliothèque de composants, dépendent fortement et utilisent [Material UI](https://material-ui.com/). Ce qui est particulièrement convaincant dans la solution de style de Material UI est le potentiel apporté par [JSS](https://cssinjs.org) et leur [Langage de Style Unifié](https://medium.com/seek-blog/a-unified-styling-language-d0c208de2660) (qui vaut vraiment la peine d'être lu), qui rendent possible le développement d'UI _encapsulées par conception_ comme dans le cas de [CSS Modules](https://github.com/css-modules/css-modules), et résolvent les problèmes mentionnés ci-dessus d'un seul coup.

Cela diffère significativement des approches comme [BEM](http://getbem.com/) qui fournissent une _encapsulation par convention_ qui tend à être moins extensible et moins encapsulée.

### Guide de style vivant

Une bibliothèque de composants ne serait pas complète sans un moyen de présenter les composants qu'elle contient et de pouvoir voir les composants au fur et à mesure qu'ils changent tout au long des versions.

Nous avons eu une assez bonne expérience avec [Storybook](https://storybook.js.org/) qui était ridiculement facile à configurer et à démarrer, mais après un certain temps, nous avons réalisé qu'une solution plus robuste et de bout en bout était nécessaire. Très proche de ce que [Styleguidist](https://react-styleguidist.js.org/) offre, mais plus adapté à nos besoins.

#### Documentation de design existante

La documentation servant de source principale d'information sur les dernières spécifications de design était située dans Confluence, où les designers maintenaient une spécification à jour pour chaque composant en utilisant des captures d'écran illustrant les cas d'utilisation autorisés, les états et les variations dans lesquels le composant pouvait se trouver, listant les meilleures pratiques, ainsi que des détails comme les dimensions, les couleurs utilisées, etc. En suivant cette approche, nous avons été confrontés à un certain nombre de défis :

* **La spécification du design matériel continue d'évoluer** et, pour cette raison, nous nous retrouvions souvent soit à passer du temps à mettre à jour toutes les captures d'écran et les directives, soit à laisser nos directives de design devenir obsolètes
* **Déterminer ce qui est le plus correct : l'implémentation ou la spécification** n'était pas toujours une tâche facile. Parce que nous avons publié des démos Storybook de chaque composant et pour chaque version de la bibliothèque, nous pouvions voir ce qui avait changé et comment. Nous ne pouvions pas faire de même pour la spécification de design.
* **Les captures d'écran et les vidéos ne peuvent communiquer que tant de choses**. Pour fournir des composants de haute qualité et qui peuvent être utilisés par plusieurs équipes, il est nécessaire de vérifier si chaque composant fonctionne dans toutes les résolutions, est exempt de bugs et a une bonne UX  cela était difficile sans avoir le designer assis littéralement à côté de vous pour voir la démonstration de l'implémentation affichée à l'écran

### Application de documentation des composants

Notre application de documentation vise à fournir les moyens d'une collaboration efficace entre les designers et les ingénieurs pour simplifier et rendre moins chronophage pour les deux parties la documentation, la révision et le développement des composants. Plus précisément, nous avions besoin de :

* **Avoir un point de référence unique présentant les composants**, comment ils doivent apparaître, se comporter et être utilisés  fourni pour chaque version  en remplaçant les descriptions détaillées par des démos en direct
* **Rendre la collaboration entre designers et développeurs aussi facile que possible** sur les composants et leur documentation et ce avant que les composants ne soient publiés  sans avoir besoin de partager des vidéos, des captures d'écran, ou d'être physiquement au même endroit
* **Séparer les designs en ce que nous prévoyons de faire vs ce qui a été fait**

De manière similaire à avant, chaque version de la bibliothèque de composants entraîne la publication d'une nouvelle version du guide de style vivant. Cette fois-ci, cependant, il y a quelques différences :

1. **Les designers contribuent directement à la documentation des composants** en éditant les fichiers de documentation via l'interface utilisateur de Github, en validant les changements pour la dernière version.
2. **Démos de composants en WYSIWYG**  le même code que vous voyez comme exemple de la façon d'implémenter le composant est utilisé pour rendre la démonstration, y compris toutes les importations de fichiers intermédiaires, déclarations de variables, etc. En bonus, les composants enveloppés dans `withStyles()` sont affichés correctement ([problème](https://github.com/storybooks/storybook/issues/3851) présent dans Storybook à l'heure actuelle).
3. **Les changements apportés à la documentation et au code sont presque instantanément visibles** sans avoir besoin de vérifier la branche localement et de démarrer l'application de documentation  l'application est reconstruite et publiée pour chaque commit.

![Image](https://cdn-media-1.freecodecamp.org/images/QPddvKiDlGWgFTSYYHzPqWd5znUsU1BcHJ10)

### Expérience de développement

L'un des principaux objectifs des revues de code est de s'assurer que chaque changement est soigneusement examiné, considéré et testé avant d'être fusionné et déployé.

Pour rendre cette tâche aussi fluide que possible, nous avons développé un **Serveur de Prévisualisation** capable de créer une nouvelle version de notre application chaque fois qu'une PR est créée ou mise à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/NDRV4o2ldxNzhA2UKhGJzKoWhieO4xfioA0k)
_Un commentaire contenant des liens de version est ajouté à chaque PR et est mis à jour à chaque changement poussé_

Nos designers, chefs de produit et ingénieurs peuvent tester chaque changement avant de le fusionner, dans les environnements de staging et de production et dans les minutes suivant la modification.

![Image](https://cdn-media-1.freecodecamp.org/images/YT6YyLFIVEkURWwR0bNvMlnnf1v1-A43bff5)
_Navigation dans la version de production de l'application avant de fusionner la PR_

### Mots de la fin

Cela fait près d'un an que nous avons entrepris de consolider nos tableaux de bord. Nous avons passé ce temps à apprendre comment faire croître un grand mais sain projet logiciel, comment mieux collaborer et communiquer, et comment élever la barre de la qualité pour nous-mêmes.

Nous avons développé un projet frontend non seulement en termes de lignes de code, mais aussi en termes de nombre d'ingénieurs qui travaillent dans sa base de code  un nombre qui a quadruplé depuis le début.

![Image](https://cdn-media-1.freecodecamp.org/images/qP03wrJ8qgRo6ewiwac2oQDZCai50SmXiG6a)
_Fréquence du code depuis le début de l'existence du projet jusqu'à maintenant_

Nous avons fait un changement à 180 degrés dans la gestion des différences horaires entre nos équipes, passant d'un modèle où nos équipes travaillaient en pleine isolation à un modèle où la collaboration et la communication étroites sont une occurrence quotidienne.

Bien que nous ayons encore un long chemin à parcourir pour nous assurer que nous pouvons développer notre approche à plus d'équipes et à des défis plus grands, nous avons déjà remarqué un certain nombre d'améliorations :

* **Visibilité de la feuille de route et du travail**  
Grâce à un seul endroit où tout le travail se déroule, les progrès sont suivis et tous les problèmes sont rassemblés
* **Vitesse de développement et temps de mise sur le marché**  
De nouvelles fonctionnalités peuvent être créées en grande partie à partir de composants existants et bien testés  facilement trouvés via notre application de documentation
* **Qualité du code et couverture des tests**  
Lors de la construction de nouvelles choses, une solution à un problème similaire existe généralement déjà et est à portée de main, avec des exemples sur la façon de le tester
* **Qualité globale et UX**  
Tester les fonctionnalités et garantir leur qualité est maintenant plus facile que jamais, car les designers, les chefs de produit et les autres parties prenantes peuvent tester chaque changement sur leur propre machine, avec leurs propres comptes et ensembles de données

Naturellement, en cours de route, nous avons rencontré un certain nombre de défis que nous devons résoudre, ou qui devront être résolus à l'avenir :

* **Performance de construction et CI**  
À mesure que le nombre de dépendances, de bundles de construction et de tests augmente, le temps nécessaire pour effectuer un déploiement augmente également. À l'avenir, nous devrons développer des outils pour nous aider à ne construire, tester et déployer que les parties qui ont changé.
* **Culture de développement**  
Pour construire des logiciels sains, nous devons travailler en continu sur des moyens sains de communiquer et d'échanger des idées, et les communications basées sur le texte rendent cette tâche plus difficile. Nous travaillons à résoudre ce problème par le biais d'une série de sessions de formation régulières pour les dirigeants et en adoptant des méthodes de travail plus open-source, ainsi qu'en organisant quelques sessions de rencontre par an pour que les équipes se rencontrent en face à face.
* **Isolation des pannes et mises à jour**  
À mesure que le nombre de fonctionnalités et de pages augmente, nous aurons besoin d'une méthode plus robuste pour isoler nos modules d'application afin d'empêcher les dommages de se propager lorsque les choses tournent mal. Cela pourrait être réalisé en versionnant tout le code partagé (logique redux, src/components), ou dans des cas extrêmes en produisant des builds autonomes de certaines fonctionnalités.

#### État alors, maintenant et dans le futur

La migration a impliqué le passage d'AngularJS à React. Voici comment la situation a changé au cours de l'année écoulée :

![Image](https://cdn-media-1.freecodecamp.org/images/hrtCCbYM4vq2Pcm8YXGwJj9ZxT9Cc9zxk7QL)
_Avril 2018_

![Image](https://cdn-media-1.freecodecamp.org/images/vCd4c0YHkqK3HQT7PBM1ZiHbGQyXTBTVcKIp)
_Février 2019_

![Image](https://cdn-media-1.freecodecamp.org/images/Ak8ZHR-gW1rx70m7nKLZV6szLNZxtpLjVDrA)
_Où nous espérons que nos tableaux de bord seront d'ici la fin de 2019_

C'est tout ! Merci d'avoir lu ! Vous pouvez me trouver sur LinkedIn [ici](https://www.linkedin.com/in/maciejgurban/).

Si travailler sur des défis similaires vous intéresse, nous recherchons toujours des ingénieurs talentueux pour rejoindre nos équipes [partout dans le monde](https://careers.unity.com/).