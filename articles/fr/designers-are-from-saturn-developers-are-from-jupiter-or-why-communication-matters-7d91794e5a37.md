---
title: 'Les designers viennent de Saturne, les développeurs viennent de Jupiter :
  ou pourquoi la communication est importante'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-15T20:55:05.000Z'
originalURL: https://freecodecamp.org/news/designers-are-from-saturn-developers-are-from-jupiter-or-why-communication-matters-7d91794e5a37
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8fAGPEkr7UAqhNf0z3T5Zg.jpeg
tags:
- name: Design
  slug: design
- name: Front-end Development
  slug: front-end-development
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: 'Les designers viennent de Saturne, les développeurs viennent de Jupiter
  : ou pourquoi la communication est importante'
seo_desc: 'By Albino Tonnina

  About the ‘But it looks different on the Specs’ effect, UI Toolkits, and other stuff.


  Two different planets, but at least they’re in the same Solar System! And that’s
  the end of the analogy with planets.

  Allergy Advice

  This is an a...'
---

Par Albino Tonnina

#### À propos de l'effet « Mais ça a l'air différent sur les spécifications », des UI Toolkits et autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8fAGPEkr7UAqhNf0z3T5Zg.jpeg)

Deux planètes différentes, mais au moins elles sont dans le même système **Solaire** ! Et c'est la fin de l'analogie avec les planètes.

#### Avis d'allergie

Cet article parle des [Design Systems](https://www.uxpin.com/studio/blog/design-systems-vs-pattern-libraries-vs-style-guides-whats-difference/), en particulier sur le sujet des UI Toolkits et la dynamique de la communication entre les designers et les développeurs.

**Designers**, quelque chose me dit que vous connaissez les Design Systems et que vous les appréciez :) Si vous voulez en lire plus, Nathan Curtis a écrit beaucoup à ce sujet. J'aime et je respecte son [travail sur les Design Systems](https://medium.com/eightshapes-llc/tagged/design-systems).

**Développeurs**, je vais montrer un peu de code à la fin. Le terrain de jeu est une application React + CSS-in-JS (comme emotion ou styled-components).

### Un scénario typique

Notre designer a produit une série de beaux designs, y compris la mise en page de notre page _Documents_ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*k0iI0xz1Qls-w1vT-PwWLw.png)
_[https://www.sketchappsources.com/free-source/2576-ooto-productivity-dashboards-sketch-freebie-resource.html](https://www.sketchappsources.com/free-source/2576-ooto-productivity-dashboards-sketch-freebie-resource.html" rel="noopener" target="_blank" title=")_

C'est propre, c'est équilibré, c'est plutôt agréable à l'œil. Pour les designers, c'est le point culminant d'un **long processus**, une série entière de tâches impliquant des recherches, des entretiens, des réflexions, des révisions, des repensées, des sessions de whiteboard, des prototypages et des wireframings. Un processus long et fastidieux auquel les développeurs ne sont souvent pas exposés.

Comment les designers ont-ils produit cette image, au fait ? Ils ont probablement utilisé un **design toolkit**. Un très populaire est [Sketch](https://www.sketchapp.com/).

**Hélas**, la façon dont ce logiciel fonctionne est diamétralement opposée à la façon dont les développeurs travaillent. **Et je dis que c'est le cœur de notre problème**.

Les designers ont besoin d'outils qui leur permettent de réitérer rapidement, en révisant et en mettant à jour, feedback après feedback, une réunion de parties prenantes après l'autre. **Les designers ont besoin d'outils comme Sketch.**

#### Les développeurs, en revanche, travaillent différemment.

Ils travaillent sur des **codebases en constante évolution** qui, à tout moment, doivent produire une version fonctionnelle d'une application. Il faut des efforts pour implémenter une mise en page comme celle de notre exemple, en concevant, en abstraisant, en implémentant, en refactorant, en testant, en révisant, en refactorant, en corrigeant des bugs, en refactorant. Les développeurs doivent s'assurer qu'ils ne cassent rien d'autre ou ne polluent pas la codebase avec du **mauvais code dupliqué**.

Pour moi, être designer ressemble plus à sauter en arrière et en avant, tandis que les développeurs travaillent dans une boucle continue de développement.

#### Le fichier de spécifications visuelles

Maintenant, il est temps pour les designers de communiquer avec les développeurs, de _passer le relais_.

Il y a des mises en page, des espaces et des couleurs (et ainsi de suite) à documenter. Sketch ou tout autre outil ne connaît pas beaucoup votre codebase actuelle, votre structure de fichiers ou votre abstraction, alors que peut faire Sketch ? Mesurer les choses. Et c'est ce qui sera produit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*t8K0NcmFdWBkCTalH92aVw.png)

### Quelques jours passent...

Les choses sont prêtes et les designers voient le résultat pour la première fois :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Op-Fmt6HD_onew7zktxn9Q.png)

### Designers frustrés, développeurs frustrés.

C'est le moment où l'enchantement est vraiment rompu. **Le fichier de spécifications**. Petits problèmes avec la couleur, l'espacement, la typographie, la mise en page, des détails mal communiqués, des comportements manquants.

Les développeurs devront interpréter et adapter les spécifications à leur propre système dans la codebase à la volée alors qu'ils devraient simplement se soucier de l'implémentation de la logique métier de la nouvelle fonctionnalité. Les designers ne sont pas à blâmer, cependant — ils ne connaissent peut-être tout simplement pas un tel système.

Mon grand-père avait l'habitude de dire :

> Lorsque les designers et les développeurs ne communiquent pas bien, obtenez un Design System avec un ensemble d'outils, d'abstractions et de contraintes bien partagés et communiqués.

### Vous avez besoin d'un bon UI Toolkit

C'est à travers un système partagé que les designers et les développeurs peuvent vraiment **communiquer efficacement** sans stress. Un UI Toolkit vise à **renforcer** les principes documentés dans un Design System. Il est gouverné par un ensemble **hautement partagé et documenté** de conventions, de motifs UI, de comportements, et il est conçu, testé et approuvé par tous. _C'est là que les efforts des designers et des développeurs se rencontrent._

#### Pourquoi vous avez vraiment besoin d'un bon UI Toolkit

* Votre application devient-elle de plus en plus complexe ?
* Les designers parlent-ils beaucoup des incohérences dans l'application ?
* CI/CD ? Allez-vous vite vite vite ?
* Des équipes à distance ?
* Les fichiers CSS deviennent-ils un peu désordonnés ?
* Commencez-vous à vous soucier de la taille de l'application ?
* L'expérience utilisateur est-elle au cœur de votre modèle économique ?

Vous n'avez pas besoin de cocher toutes ces cases — même une seule peut suffire :)

#### Pourquoi vous avez besoin de votre propre UI Toolkit

Un Design System est tout au sujet du **Langage**. Langage visuel, langage de conception UI, etc. **Cela demande beaucoup d'efforts pour définir le vôtre** : Produit, Design, Ingénierie, tous ces départements seront fortement impliqués.

Beaucoup de fois, ce n'est tout simplement **pas une option viable**. Il existe des frameworks incroyables, [semantic-ui](https://react.semantic-ui.com/), [ant-design](https://ant.design/), [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/), [Material-UI](https://material-ui.com/). Ils viennent tous avec une sorte de **Langage pré-fait** et un **UI Toolkit testé en bataille**, prêt à être utilisé.

**Le piège ?** À mon avis honnête, ils ne vous conviendront plus assez tôt. **Vous voudrez les éviter.** De plus, les UI toolkits sont probablement si conçus qu'ils sont difficiles à contrôler. N'oubliez pas que ces frameworks sont faits pour passer d'innombrables cas, peut-être plus que ce dont vous avez besoin. De plus, cette **complexité supplémentaire est payée en kb** également.

#### Voler comme un artiste

N'adoptez pas un UI Toolkit. Copiez plutôt les autres, et par là, je veux dire prenez les morceaux qui vous conviennent le mieux et implémentez-les **à partir de zéro**. Il est maintenant courant pour les entreprises très centrées sur l'utilisateur d'avoir leur propre Design System, et beaucoup d'entre eux sont open-source !

Regardez cette liste de Design Systems : [https://adele.uxpin.com](https://adele.uxpin.com/) :

* BBC : [Gel](http://www.bbc.co.uk/gel)
* Trello : [Nachos](https://design.trello.com/)
* Salesforce : [Lightning](https://www.lightningdesignsystem.com/)

Et des dizaines d'autres. Et en fin de compte, tout est une question de concevoir et de livrer cela **ensemble**. Il s'agit de **construire quelque chose de spécifique pour votre domaine**, également **unique** et représentatif de votre **marque**. C'est gratifiant, et vous pouvez lui donner un joli nom aussi :)

### Faisons-en un

Je vais vous montrer à quel point il est facile de démarrer votre propre Design System.

> Je vais l'appeler **Larry**.

Prenons une petite partie de notre mise en page et essayons de la construire à partir de zéro :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ctk5K5_2twIWj8JBx2KrGw.png)

#### Résultat final d'abord

Le CodeSandbox suivant est la seule application au monde qui implémente **Larry** :

Vous pouvez trouver **Larry** sur **GitHub** : [https://github.com/albinotonnina/larry](https://github.com/albinotonnina/larry)

#### La documentation

Cette partie est la plus importante. Qui est responsable de cela, peut-être les designers ? Eh bien, typiquement oui, mais faites-moi confiance sur ce point : vous devriez tous les deux être également impliqués dans la documentation de votre langage. **Vous devriez tous les deux être d'accord sur littéralement tout ici.**

Commençons par définir quelques conventions vraiment basiques :

#### Couleurs

Générons une palette pour notre mise en page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KqcQkVqdJBKSuS7loVd7Yw.png)

Je suggère que vous définissiez une série de noms sémantiques à partir de ces couleurs, comme ceci :

**headerText** = JapaneseIndigo  
**paragraphText** = JapaneseIndigo  
**elementBackgroundDefault** = Snow  
**elementBackgroundHover** = BrilliantAzure  
**elementButton** = LightGray — alpha 60%

Ce sont les noms **que vous allez tous les deux utiliser lorsque vous spécifiez** (qui est un mot).

#### Espacement

**Portez une attention particulière à l'espacement.** Sans une stratégie claire pour l'espacement, les choses peuvent vraiment mal tourner.

Définissez et convenez d'un système d'espacement, par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*8vWeubT5wjJs-cOQHf7cNQ.png)

**Un fichier de spécifications ressemblerait à ceci :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*wopFDrMRdrdLlPv-XMO6Zw.png)

#### Typographie

Assurez-vous que les tailles de police, les poids de police, les hauteurs de ligne, les marges, les couleurs dans vos titres, vos paragraphes et ainsi de suite correspondent simplement. Appelez-les avec des noms que vous aimez, par exemple HeaderHuge, HeaderLarge, HeaderTiny ou utilisez des balises sémantiques (h1, h2, h3) correctement. Assurez-vous simplement que vous êtes alignés sur cela.

#### Motifs

Qu'est-ce qui rime avec UI Toolkit ? **Bibliothèque de motifs** ! Vous devez commencer à peupler votre bibliothèque de motifs. Ce que vous voulez, c'est avoir les composants dont vous avez besoin qui se comportent de la manière dont vous avez convenu afin que vous puissiez les composer comme vous le souhaitez, à tout moment.

Commencez par les **particules** et les **primitives**, comme un composant Box, pour lorsque vous devez définir des espacements et des bordures autour de quelque chose d'autre.

Ajoutez **de nouvelles particules plus spécialisées**, comme un composant Text ou un composant Flex, que vous pourriez imaginer comme un composant Box + quelques utilitaires flex.

Voyez-les comme des particules qui vivent en isolation, sans connaître le contexte dans lequel elles seront utilisées et l'espace qui devrait exister autour d'elles.

Continuez avec des composants UI plus complexes, des compositions d'autres plus petits composants et ainsi de suite.

Ce qui est important ici, ce n'est pas la technologie ou le type d'abstractions dans votre documentation. Ce qui est important, c'est que vous fassiez cela **ensemble**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YYrdHo0lKQrNkVZQ9W7D_g.png)
_Exemple d'un composant UI plus complexe_

#### Vous avez compris l'idée ?

Vous avez défini des constantes et vous avez quelques particules à construire.

Vous allez réitérer sur ces particules et étendre la bibliothèque assez rapidement, alors acceptez et préparez-vous à l'élasticité. Développeurs, vous ne voulez pas que les designers **finissent** de documenter l'ensemble du système avant de commencer à implémenter le code. **Vous devez faire cette chose ensemble ou cela ne décollera tout simplement pas.**

Alors, designers et développeurs, juste après l'article, **allez créer votre propre Larry** si vous n'en avez pas un !

### Code

Vous avez [une copie de Larry](https://github.com/albinotonnina/larry), vous pouvez la cloner et jouer avec. Votre Larry peut être différent ou vous pouvez utiliser des frameworks différents, alors je vais passer par les points clés de cette approche.

#### Thème, définir les constantes

C'est un objet avec nos constantes de thème, donc les définitions d'espaces, les couleurs, les polices, la typographie, les points de rupture, tout. Voici [le thème de Larry](https://github.com/albinotonnina/larry/blob/master/src/design-system/constants/index.js), et voici une version d'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ctftgBakeNeruWAQdJArfw.png)

Il n'y a pas de limite à la complexité/complétude que vous pouvez atteindre ici, après tout, il s'agit de générer un objet JavaScript, imaginez simplement ce que vous pourriez faire !

![Image](https://cdn-media-1.freecodecamp.org/images/1*RjRcYjLRD5haC8DDgQYKrw.png)

C'est un fichier central. **Toute couleur, marge ou remplissage, taille de police ou poids de police ou point de rupture doit provenir d'ici et uniquement d'ici.**

Les bibliothèques CSS-in-JS sont des outils incroyables, et [styled-system](https://github.com/jxnblk/styled-system) les rend encore meilleurs. C'est un ensemble d'utilitaires pour les Design Systems et se compose de fonctions qui prennent `props` comme argument et retournent des objets de style, tout en simplifiant l'utilisation des valeurs d'un thème et en appliquant des styles de manière réactive à travers les points de rupture.

Cette approche tire parti de ces utilitaires, alors n'hésitez pas à l'évaluer.

#### Intégrez le thème dans votre application

[Fournissez ces constantes à votre application](https://www.npmjs.com/package/emotion-theming) : chaque composant de l'application aura accès à nos constantes de thème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6M6Q9zuKzNlcWPphfUI9ww.png)

#### Créez des composants UI de base

![Image](https://cdn-media-1.freecodecamp.org/images/1*1eIZb7yNcdppncpoj5fCLw.png)
_un composant UI primitif Box_

#### Composants UI plus spécialisés

Voici un composant Flex.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kd_s4cbWxxqcJTlC2N04fw.png)

#### Implémentez des composants UI dans vos fichiers de fonctionnalités

![Image](https://cdn-media-1.freecodecamp.org/images/1*qSxzGojmAS-vfB3LTkZctw.png)

#### Il est temps de rendre quelque chose

C'est là que vous implémentez votre composant UI et votre logique métier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5vObQKvSpUX9engeMaNX6A.png)

### La structure des fichiers

Voici la structure des fichiers de Larry. Je n'ai pas d'opinions fortes sur les structures de fichiers, en fait, je crois en quelque chose de différent : déplacez vos fichiers jusqu'à ce que vous vous sentiez à l'aise avec eux.

Larry est entièrement dans un dossier « **design-system** ». C'est là que vous pouvez trouver ses constantes et ses composants UI génériques et réutilisables.

Remarquez également le dossier UI dans le dossier de mise en page des documents — c'est là que je définis et exporte les composants UI spécifiques à notre fonctionnalité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eN6vUZcqCJfmHMdVmKu5EQ.png)

### Conclusion

Avec des applications grandes et complexes, il n'est jamais facile de garder l'UI cohérente et cohésive. Les Design Systems aident. Les Design Systems personnalisés et les UI Toolkits sur mesure aident vraiment.

Les designers et les développeurs peuvent avoir des approches très différentes du même problème, mais cela ne signifie pas qu'ils ne peuvent pas communiquer efficacement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LRjLAzWqaLiYl4N5DZH8Kg.gif)
_[https://dribbble.com/shots/2712522-Designer-vs-Developer](https://dribbble.com/shots/2712522-Designer-vs-Developer" rel="noopener" target="_blank" title=")_

### Merci d'avoir lu

Avez-vous des expériences positives à partager ? Faites-le dans les commentaires.

Bonjour, je m'appelle Albino Tonnina, je suis un ingénieur logiciel qui travaille à Londres, vous pouvez me trouver sur [Twitter](https://twitter.com/albinotonnina) ou [Github](https://github.com/albinotonnina) ou [Instagram](https://www.instagram.com/albino_tonnina/) ou dans la ville.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ndz2zpAwq7qvQhhQI0ieLQ.png)

#### Mes derniers articles

[Comment perdre un emploi en informatique en 10 minutes](https://hackernoon.com/how-to-lose-an-it-job-in-10-minutes-3d63213c8370)  
[En parlant de mises en page web... présentation de la technique Magic Hat ?✨](https://medium.com/@albinotonnina/magic-hat-technique-408a3fa590bb)

Suivez-moi sur [Twitter](https://twitter.com/albinotonnina) !