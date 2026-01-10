---
title: Questions à se poser avant d'ajouter un package NPM à votre projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T18:09:22.000Z'
originalURL: https://freecodecamp.org/news/what-to-ask-yourself-before-adding-an-npm-package-to-your-project-6b92ba13070d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*40Etz3IOkChZ_RdoNcil3A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: open source
  slug: open-source
- name: software development
  slug: software-development
seo_title: Questions à se poser avant d'ajouter un package NPM à votre projet
seo_desc: 'By Jacob Worrel

  One of the greatest things about being a JavaScript developer today is the ability
  to leverage its incredibly rich ecosystem. With almost a million packages on the
  NPM registry, it’s not uncommon to reach for an off-the-shelf solution...'
---

Par Jacob Worrel

L'une des meilleures choses à propos d'être un développeur JavaScript aujourd'hui est la capacité à tirer parti de son écosystème incroyablement riche. Avec près d'un **million** de packages sur le registre NPM, il n'est pas rare de se tourner vers une solution clé en main lorsqu'on est confronté à un problème couramment résolu. Moins vous passez de temps à réinventer la roue, plus vous pouvez vous concentrer sur le problème plus large à résoudre.

Cela dit, tous les logiciels open source ne se valent pas et il est probablement bon de faire vos devoirs avant de sauter le pas et de dépendre du code de quelqu'un d'autre. Voici quelques questions de base que vous devriez vous poser avant d'ajouter un nouveau package NPM à votre projet, ainsi que les outils que vous pouvez utiliser pour y répondre.

### TL;DR

Les questions suivantes sont basées sur mon expérience en tant que développeur JavaScript et ne sont en aucun cas exhaustives. Si vous pensez que quelque chose manque, n'hésitez pas à me le faire savoir dans les commentaires !

**À quel point est-il populaire ?** Regardez les téléchargements hebdomadaires sur NPM et les étoiles sur Github.

**À quel point est-il mature ?** Regardez la date de la première version publiée sur NPM et le nombre de problèmes ouverts par rapport aux problèmes fermés sur Github.

**Est-il activement maintenu ?** Regardez l'historique des commits et les graphiques [Commits](https://github.com/expressjs/express/graphs/commit-activity) et [Fréquence du code](https://github.com/expressjs/express/graphs/code-frequency) (sous l'onglet Insights) sur Github. Vérifiez la date de "dernière publication" sur NPM.

**Quelle est sa taille ?** Vérifiez la taille du bundle sur [Bundlephobia](https://bundlephobia.com/).

**A-t-il une couverture de test ?** Recherchez les badges de couverture sur NPM/Github. Ouvrez les fichiers de test.

### À quel point est-il populaire ?

![Image](https://cdn-media-1.freecodecamp.org/images/ipdckGNlq1pIHne7aM65st7F3LI9A1XVazOr)
_Popularité des bibliothèques CSS-in-JS par téléchargements NPM, courtesy of [npmcharts](https://npmcharts.com/" rel="noopener" target="_blank" title=")._

La popularité est probablement la première chose que la plupart des gens veulent savoir lorsqu'ils cherchent un package open source pour résoudre leur problème — plus spécifiquement, combien d'étoiles il a sur Github et combien de téléchargements hebdomadaires il obtient sur NPM.

Et bien que ces deux métriques puissent vous donner une idée de la traction d'un projet au sein de la communauté, vous devriez définitivement prendre ces chiffres avec des pincettes. Gardez à l'esprit qu'une étoile Github est essentiellement l'équivalent d'un "like" sur les sites de réseaux sociaux et que beaucoup de développeurs les distribuent comme des bonbons. Je suis moi-même coupable de cela, et le fait que j'aie mis une étoile à un dépôt ne signifie pas que j'ai vérifié la qualité du code et que je l'ai pleinement approuvé.

En ce qui concerne les téléchargements, même NPM admet que leurs statistiques sont "[naïves par conception](https://blog.npmjs.org/post/92574016600/numeric-precision-matters-how-npm-download-counts)" puisqu'elles incluent les téléchargements par des serveurs de construction automatisés, des miroirs et des bots. Néanmoins, il faut bien commencer quelque part, alors vous pouvez aussi bien régler cette question. Soyez simplement conscient que c'est probablement le facteur le moins important (et souvent le plus trompeur !), alors assurez-vous de faire votre diligence raisonnable et ne vous arrêtez pas là.

### À quel point est-il mature ?

![Image](https://cdn-media-1.freecodecamp.org/images/tZzWTv2iChpcSd3AgNunYVE6cezc9a4kRIvc)
_Un nombre sain de problèmes ouverts par rapport aux problèmes fermés est un bon indicateur de la maturité d'un projet._

Si vous avez entendu parler de la [règle 80/20](https://swreflections.blogspot.com/2013/11/applying-8020-rule-in-software.html), vous êtes probablement familier avec le concept selon lequel les 80 % premiers du code sont généralement réalisés en 20 % du temps, et les 20 % restants prennent les 80 % restants du temps. Cela est dû au fait qu'il est généralement facile de faire fonctionner quelque chose, mais la gestion de tous les cas limites, la correction des bugs imprévus et le traitement des performances et de l'échelle sont souvent les parties les plus difficiles de l'écriture de logiciels stables. C'est pourquoi vous ne voulez idéalement utiliser que des logiciels open source qui ont été testés en conditions réelles et qui ont résisté à l'épreuve du temps.

La première chose à vérifier est la date à laquelle un package a été publié pour la première fois. Allez sur la page NPM du projet, cliquez sur l'onglet Versions pour obtenir l'historique complet de chaque version et faites défiler jusqu'en bas. Un long historique avec de nombreuses versions est généralement un bon signe, car cela signifie que le projet a été itéré au fil du temps.

Le prochain et probablement meilleur indicateur d'un projet mature est le nombre de problèmes ouverts et fermés sur Github. Il est généralement bon de regarder ces deux chiffres ensemble, car l'un ne signifie pas grand-chose sans l'autre. Un nombre élevé de problèmes ouverts n'est pas nécessairement une mauvaise chose si le nombre de problèmes fermés est encore plus élevé. Pour vous donner un cadre de référence, au moment de la rédaction de cet article, [React](https://github.com/facebook/react/issues) a environ 400 problèmes ouverts mais plus de 6500 fermés. [Node.js](https://github.com/nodejs/node/issues) a environ 600 problèmes ouverts et près de 9000 fermés.

Il n'y a pas de ratio magique, mais méfiez-vous de tout projet avec un nombre élevé de problèmes ouverts par rapport au nombre de problèmes fermés. En revanche, un faible nombre de problèmes ouverts n'est pas nécessairement une bonne chose si le nombre de problèmes fermés est également faible. Cela signifie probablement qu'il n'a pas été beaucoup utilisé et qu'il est encore à un stade précoce de développement.

### Est-il activement maintenu ?

![Image](https://cdn-media-1.freecodecamp.org/images/0lyma8THIp-zVYm3kAZmyxbnzHh7gX3ojNkf)
_L'onglet Insights sur Github_

Sauf si un projet est déjà très mature et n'ajoute pas de nouvelles fonctionnalités, ou fait quelque chose de relativement petit en termes de portée, il est important qu'il soit activement maintenu. Souvenez-vous de la règle 80/20 ? La seule façon pour que le logiciel passe de nouveau et expérimental à stable et mature est par une maintenance active, ce qui signifie des corrections de bugs régulières et des améliorations ajoutées.

D'après mon expérience, la meilleure façon de vérifier cela est de regarder l'historique des commits sur la branche principale du projet. Tout d'abord, cliquez sur le nombre de commits sur la page Github du projet et vérifiez quand le dernier commit a été fusionné dans la branche principale. Cette date ne signifie pas grand-chose par elle-même, mais c'est une pièce importante du puzzle global.

Si vous êtes comme moi et que vous préférez voir ce type de données visualisées, cliquez sur l'onglet Insights, où vous pouvez glaner toutes sortes d'informations sur le dépôt. Je pourrais probablement écrire un article de blog entier sur cette fonctionnalité seule, alors tout ce que je vais dire, c'est que si vous ne l'avez pas encore utilisée, arrêtez de lire, allez sur la page Github de votre projet open source préféré et commencez à jouer avec.

J'aime particulièrement les graphiques [Commits](https://github.com/expressjs/express/graphs/commit-activity) et [Fréquence du code](https://github.com/expressjs/express/graphs/code-frequency) car ils me donnent en un coup d'œil une idée de la quantité de travail effectuée sur le projet. Souvenez-vous cependant que le fait qu'il n'y ait pas beaucoup de commits récents ne signifie pas que le code ne peut pas être fiable. Au contraire, cela peut parfois être un signe de maturité — dans la capture d'écran ci-dessus, le graphique de fréquence du code pour Express est une excellente visualisation de ce à quoi ressemble un projet mature.

Enfin, mais non des moindres, je trouve utile de savoir quand une nouvelle version a été publiée pour la dernière fois sur NPM, ce qui est inclus dans les statistiques principales sur la page NPM d'un projet. Cela me donne une idée générale de la fréquence à laquelle les mainteneurs planifient réellement les versions, par opposition à la simple validation du code.

### Quelle est sa taille ?

![Image](https://cdn-media-1.freecodecamp.org/images/rG7TrFGwBkJWXUwo--WIqZCV1FYfVh70KaqN)
_Une ventilation du module NPM de d3 sur [Bundlephobia](https://bundlephobia.com/" rel="noopener" target="_blank" title=")._

Personne n'aime un bundle gonflé. Et bien qu'il soit facile de continuer à ajouter des modules node à un projet, cela peut avoir un [coût](https://medium.com/@addyosmani/the-cost-of-javascript-in-2018-7d8950fbb5d4). La minification, la compression et le fractionnement de code aident beaucoup, mais à la fin de la journée, tout se résume à la quantité de JavaScript que vous envoyez au client.

Ma ressource de référence pour cela est [Bundlephobia](https://bundlephobia.com/), un site merveilleux qui non seulement vous montre la taille du bundle d'un package NPM, mais aussi toutes sortes d'autres choses fantastiques. Comme illustré ci-dessus, vous pouvez voir le temps de téléchargement estimé sur les réseaux lents, l'évolution de la taille du bundle au cours des différentes versions, et la composition des dépendances. Il vous indiquera également si le package est optimisé pour tirer parti du tree-shaking avec des bundlers modernes comme Webpack, et suggère même des modules similaires, avec des statistiques comparant leur taille respective !

Idéalement, vous voulez utiliser des modules de petite taille et avec un faible nombre de dépendances, voire aucune. Bien sûr, la taille est relative, alors assurez-vous de comparer des pommes avec des pommes — si vous regardez une bibliothèque de graphiques, par exemple, assurez-vous de la comparer à d'autres bibliothèques de graphiques (qui tendent à être du côté plus grand du spectre).

### A-t-il une couverture de test ?

![Image](https://cdn-media-1.freecodecamp.org/images/RLyKPuibGV878fVuLCqackTNSNIwShpczNJb)
_Une bibliothèque de test sans couverture de test… ?_

Cela peut sembler évident, mais vérifiez toujours, toujours, toujours la couverture de test. Le code que vous ne pouvez pas tester est un code que vous ne pouvez pas faire confiance.

De nos jours, il est beaucoup plus facile d'obtenir une vue d'ensemble de la couverture grâce à des outils comme [Coveralls](https://coveralls.io/) et [Codecov](https://codecov.io/) — qui suivent la couverture au fil du temps et fournissent aux auteurs des badges brillants qu'ils peuvent afficher fièrement sur leurs pages Github et NPM. Gardez à l'esprit cependant que les outils de couverture de test ne vérifient que la quantité de code exécutée pendant les tests et peuvent être [trompeurs](http://www.developintelligence.com/blog/2017/11/why-test-coverage-shouldnt-trust/) par moments. Si vous voulez vraiment entrer dans les détails, il n'y a pas de substitut à l'ouverture des fichiers de test et à la lecture des spécifications de test.

### Et bien sûr…

#### Suit-il la version sémantique ?

La version sémantique est un moyen pour les auteurs de logiciels open source de communiquer — via le numéro de version — avec les utilisateurs de leur logiciel sur le type de changements qu'une nouvelle version inclut. Elle garantit que vous savez quand des changements majeurs sont introduits et donc que vous restez en contrôle de votre code malgré la dépendance à d'autres modules. Plus d'informations sur la version sémantique [ici](https://semver.org/).

#### Quelle est la licence ?

Si vous étiez présent pendant toute l'affaire de la [licence React](https://medium.freecodecamp.org/facebook-just-changed-the-license-on-react-heres-a-2-minute-explanation-why-5878478913b2), vous avez probablement appris qu'il est bon de vérifier la licence avant de commencer à utiliser un logiciel open source, de peur qu'une organisation apparemment bienveillante ne tente de vous jouer un mauvais tour. Vous pouvez les trouver dans le code source, généralement dans le répertoire racine du projet. Recherchez des licences permissives comme la [licence MIT](https://en.wikipedia.org/wiki/MIT_License), qui vous permet essentiellement de faire ce que vous voulez sauf poursuivre l'auteur. Plus d'informations sur les licences [ici](https://medium.com/shakuro/software-licenses-explained-77f4f18ebeb1).

### C'est ça, lisez le code source !

Bien que les questions discutées ci-dessus soient un bon moyen d'avoir un aperçu de la santé globale d'un package NPM, la meilleure façon de déterminer la qualité du code sur n'importe quel projet est de jeter un coup d'œil au code source. Bien sûr, cela prend considérablement plus de temps que de parcourir les pages NPM/Github/Bundlephobia d'un projet, donc il est peu probable que vous fassiez cela pour chaque dépendance. Cependant, cela pourrait bien payer si le module est critique pour votre application. Cela pourrait même vous éviter un gros mal de tête plus tard si vous découvrez un problème majeur qui aurait autrement pu passer inaperçu.

### Note sur les composants UI tiers

Si vous utilisez un framework front-end basé sur des composants comme React, Vue ou Angular, il est probable que vous ayez quelques composants UI tiers dans vos dépendances `package.json`. Et bien que toutes les questions soulevées dans cet article s'appliquent toujours, les composants UI nécessitent un examen supplémentaire, que je prévois d'aborder dans un futur article, alors restez à l'écoute !