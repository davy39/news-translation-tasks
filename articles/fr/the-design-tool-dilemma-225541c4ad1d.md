---
title: Le dilemme des outils de design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-11T16:58:04.000Z'
originalURL: https://freecodecamp.org/news/the-design-tool-dilemma-225541c4ad1d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2eX5pLryqNXCm1HOmY0c6Q.png
tags:
- name: Collaboration
  slug: collaboration
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: Le dilemme des outils de design
seo_desc: 'By Colm Tuite

  A detailed look at two opposing narratives emerging in the design tool space.


  A diagram illustrating the two opposing narratives emerging in the design tool space.

  There are two opposing narratives in the design tool space which have b...'
---

Par Colm Tuite

#### Une analyse détaillée de deux récits opposés émergent dans le domaine des outils de design.

![Image](https://cdn-media-1.freecodecamp.org/images/Mh4jZ86dool1TsiEQQGUUPpjU6SQ72pIrBjo)
_Un diagramme illustrant les deux récits opposés émergent dans le domaine des outils de design._

Il existe deux récits opposés dans le domaine des outils de design qui évoluent depuis de nombreuses années. Ces récits reflètent deux écoles de pensée très différentes en ce qui concerne la compréhension de la valeur spécifique que nos outils fournissent et la direction qu'ils devraient prendre.

Le premier récit vend l'idée que les artefacts de design peuvent et doivent être la Source Unique de Vérité™ pour le produit. Dans ce récit, le code est secondaire—son travail est de reproduire les artefacts de design aussi précisément que possible. Les contraintes de la plateforme sont largement ignorées au profit de la vitesse et de la créativité sans limites.

Appelons cela le récit de la "réduction de l'écart".

Le second récit est centré autour de l'idée que toutes les personnes collaborant sur un produit peuvent et doivent contribuer à ce même produit. Dans ce récit, le code est tout—il **est** le produit. Les contraintes de la plateforme sont respectées et comprises. Les décisions sont prises en contexte et les outils embrassent leurs médias cibles.

Nous appellerons cela le récit "collaboratif".

Alors, d'où viennent ces récits ? Dans quelle mesure chacun a-t-il du sens ? Examinons de plus près.

### Récit #1 : Réduire l'écart

Depuis aussi longtemps que les designers numériques utilisent des outils de design, nous avons toujours eu un désir brûlant de voir nos idées réalisées en production. Posséder le processus de design de l'idée au déploiement a toujours été le saint graal. Si vous regardez la chronologie évolutive de nos outils de design, vous pouvez voir ce désir se manifester.

Vers 2005, lorsque ma carrière de designer numérique a commencé, la plupart d'entre nous utilisions soit Illustrator soit Photoshop pour créer des illustrations vectorielles de tout produit que nous concevions. Cela est resté le statu quo pendant de nombreuses années—avec la plupart des offres d'emploi en design exigeant la maîtrise de la suite Creative d'Adobe.

Jusqu'au jour, en 2010, où Sketch est arrivé et a secoué le cocotier. Sketch était plus simple, moins cher et **beaucoup** plus ciblé. Bien sûr, les designers l'ont d'abord combattu, mais ont finalement trouvé son interface propre et son ensemble de fonctionnalités raffiné rafraîchissant.

Plus récemment, Figma est arrivé. Figma a étendu la révolution que Sketch avait lancée. L'ensemble des fonctionnalités est très similaire, mais en termes d'exécution, je ne pense pas que ce soit comparable. Presque toutes les fonctionnalités ont été surprenamment bien implémentées. Étonnamment bien, même.

Les outils de prototypage ont ajouté une couche supplémentaire de réalisme—prenant les images statiques exportées par nos outils de design et les assemblant, simulant des événements tactiles et des transitions d'écran.

Mais il y avait encore un écart observable à combler entre les flux de travail de design et de développement. Comment pourrions-nous franchir l'étape suivante ?

La controversée "transmission aux développeurs", bien sûr. [InVision](https://www.invisionapp.com/feature/inspect) et [Abstract](https://www.goabstract.com/blog/introducing-inspect-where-the-file-is-the-design-spec/) ont lancé "Inspect". [Avocode](https://avocode.com), [Marvel](https://marvelapp.com/features/handoff/) et [Zeplin](https://zeplin.io/) ont sorti "Handoff". Figma et Sketch ont tenté d'exporter du CSS. L'idée étant que lorsque les designers avaient quelque chose à partager, ils pouvaient transmettre leur travail aux développeurs dans un format que les développeurs comprenaient.

La dernière avancée sur cette chronologie a été une nouvelle génération d'outils promettant de convertir des images statiques en code de production. [Supernova Studio](https://supernova.studio/), [Rapid UI](https://rapidui.io/), [PageDraw](https://pagedraw.io/), [Teleport](https://teleporthq.io/), [Sketch2React](https://sketch2react.io/) et [Anima Launchpad](https://launchpad.animaapp.com/) ne sont que quelques-unes des startups menant cette charge.

À première vue, vous ne remarquerez peut-être rien d'inhabituel dans cette chronologie. Nos outils se sont simplement améliorés de manière exponentielle, comme on pourrait s'y attendre. Ils deviennent plus performants, plus robustes et plus riches en fonctionnalités. Si vous limitez votre perspective aux dix dernières années, tout cela semble être une progression naturelle.

Mais remontez un peu plus loin et vous remarquerez quelque chose de **très** particulier.

Retournons, pour un moment, à une époque où l'impression était la principale forme de communication marketing. C'était une époque plus simple. Les débats sans fin sur les outils ou les frameworks étaient réduits au minimum. Occasionnellement, quelque nouveau venu mentionnait QuarkXPress, mais la rébellion ne durait jamais longtemps. La plupart des professionnels du design utilisaient Illustrator, Photoshop et InDesign. Adobe régnait en maître et c'était tout.

Mais surtout, les designers concevaient le produit final, et non des imitations de celui-ci—le produit final étant du papier à lettres, des affiches, des livres, des identités de marque, des brochures et autres supports imprimés. Les designers avaient une influence directe sur le produit qu'ils concevaient.

Cela était possible parce que les designers imprimés avaient (et ont toujours) une bonne maîtrise du média pour lequel ils concevaient. Il y avait une corrélation étroite entre les contraintes d'entrée et de sortie.

Par exemple, les designers imprimés savaient qu'il y aurait de légères différences dans la façon dont les couleurs pourraient être reproduites sur un carton épais par rapport à un papier à lettres plus léger de 120 gsm. Les designers étaient responsables de l'ajout de 3 mm de fond perdu et de marques de coupe pour accommoder les imprécisions de l'alignement de l'imprimante. Les designers étaient conscients des délais de traitement—ils savaient que les effets fantaisistes comme le gaufrage ou le marquage à chaud étaient plus coûteux à reproduire.

Surtout lorsque la révolution de l'impression numérique est arrivée, de nombreux designers ont commencé à investir du temps et de l'argent pour apprendre autant que possible sur le média imprimé. Les logiciels de design imprimé ont embrassé le média et y ont été adaptés.

Puis, à un moment donné, le design web est devenu le focus principal et des millions de designers imprimés sont devenus des designers web du jour au lendemain.

Je ne critique pas ce changement de focus. J'ai moi-même fait la transition de l'impression au numérique. Beaucoup des compétences étudiées par les designers graphiques sont transférables à d'autres industries, et j'aime voir les gens élargir leurs horizons.

Le problème était que nous avions maintenant très peu de connaissances sur le nouveau média pour lequel nous concevions. Plutôt que de passer du temps à comprendre ce nouveau média, nous avons essayé de le dompter. Cela est devenu évident alors que nous luttions pour tout faire tenir dans un conteneur de 960px, que nous faisions référence aux interfaces comme des "pages" et que nous inventions des termes comme "site web brochure".

La plupart des designers ne pouvaient pas écrire de code, alors nous avons fait ce que nous pouvions : dessiner des images. Pour le faire, nous avons utilisé ce qui nous avait bien servi pendant des décennies auparavant : notre logiciel de design graphique.

Les designers ne concevaient plus le produit final, mais des imitations de celui-ci.

Ce changement de paradigme est resté non adressé pendant longtemps, car le design basé sur les images était encore très largement une partie cruciale de la conception pour le web. Beaucoup d'entre vous se souviendront avec nostalgie de la création d'énormes feuilles de sprites pour pirater des effets comme les dégradés et les coins arrondis. Des boutons de survol, quelqu'un ?

Aujourd'hui, les astuces basées sur les images ont été complètement remplacées par le CSS. Même l'utilisation d'images raster comme forme de communication est en déclin au profit d'actifs plus performants et/ou plus immersifs comme les animations CSS, les illustrations SVG et la vidéo.

Aujourd'hui, la corrélation entre le web et l'impression est à peu près aussi proche que la corrélation entre le web et l'architecture.

Malheureusement, nos outils n'ont pas évolué assez rapidement. Notre génération actuelle d'outils de design numérique est très largement une extension des outils de design d'impression. Les jeunes designers apprennent avec enthousiasme le design numérique à travers le prisme des outils de dessin statiques.

Bien sûr, il y a eu quelques avancées impressionnantes, mais pour la plupart, ils sont encore juste des outils de dessin vectoriel optimisés pour l'illustration. À cause de cela, nos outils manquent du contexte et de la nuance nécessaires pour prendre des décisions de design éclairées.

### Récit #2 : Collaboration

Plutôt que d'encourager le dessin d'imitations du produit final, ce récit préconise de prendre le code et de le rendre plus facile à digérer afin que toute l'équipe puisse collaborer dessus.

Étrangement, l'origine des deux récits peut être retracée à peu près à la même époque. Adobe Dreamweaver, l'infâme éditeur de code visuel WYSIWYG, est arrivé sur la scène en 1997. Softpress Freeway est arrivé un an plus tôt en 1996, et Microsoft Frontpage encore plus tôt en 1995, seulement 5 ans après Photoshop et plus d'une décennie avant Sketch.

Malheureusement, ces outils étaient souvent plus un obstacle qu'une aide. Ils étaient optimisés pour l'exportation vers la production, les rendant trop encombrants pour le processus de design.

Graduellement, une vague de designers, y compris moi-même, a abandonné les éditeurs WYSIWYG au profit d'un outil de design moins restrictif : l'éditeur de texte.

Pendant longtemps, taper du code était assez désagréable. Mais avec le temps, un écosystème sain d'outils a commencé à émerger autour du code, réduisant considérablement la barrière à l'entrée. Aujourd'hui, nous avons des outils de design basés sur le code qui ne nécessitent aucune connaissance en codage.

Examinons de plus près l'évolution des outils de design basés sur le code jusqu'à présent.

**La mise en forme du code et la coloration syntaxique** étaient parmi les premiers "outils" axés sur la rendre le code plus digeste. L'application de couleur et de structure a amélioré la lisibilité et la scannabilité. Récemmment, des outils comme [Prettier](https://prettier.io/) ont automatisé cela.

**Les préprocesseurs et les langages de templating** sont arrivés vers 2006. Des outils comme Haml, Sass, LESS, CoffeeScript et autres ont encore amélioré la gestion du code en encourageant la brièveté, en abstraisant une partie de la complexité visuelle et en automatisant certaines des tâches les plus courantes.

**JSX** est une extension de syntaxe JavaScript développée par Facebook qui ne ressemble pas trop aux langages de templating qui l'ont précédée. L'API de composants de React aide également à promouvoir la réutilisation et à abstraire la complexité visuelle, aidant ainsi notre cause de rendre le code plus digeste et accessible.

Plus récemment, nous voyons des outils supprimer les barrières à l'entrée comme la nécessité de configurer des environnements de développement et de bidouiller avec la ligne de commande, etc. [Compositor ISO](https://compositor.io/iso/) et [SEEK's Style Guide Sandbox](http://seek-oss.github.io/seek-style-guide/sandbox/) font un travail incroyable ici.

![Image](https://cdn-media-1.freecodecamp.org/images/Ev0t3TfC8YQOoDlzbPjbk5mdmwG0HAT6A7Dd)

![Image](https://cdn-media-1.freecodecamp.org/images/n9xq3W-cBeAavWG-0xPHFprR3MXQ8a0bGmSb)
_Compositor ISO et SEEK Style Guide Sandbox, où vous pouvez prototyper en utilisant JSX sans configuration de build requise._

[Modulz](https://twitter.com/colmtuite/status/909792399924318209) (un outil de design que je construis) et [UXPin](https://twitter.com/marcintreder/status/1011369055817588736) rendent également le code plus accessible en supprimant les barrières à l'entrée. Ces outils visualisent JSX, utilisant des calques familiers pour le représenter et une interface graphique pour manipuler les props des composants.

![Image](https://cdn-media-1.freecodecamp.org/images/RisINJWLfOC0nAIZDTa6pn6uaxQEUA1Z-yZ7)
_[Modulz](https://www.modulz.co/" rel="noopener" target="_blank" title=") — un outil de design basé sur le code pour composer des UI visuellement._

[Polypane](https://polypane.rocks/) construit un environnement de design intelligent où vous pouvez prévisualiser vos designs sur une multitude de navigateurs, appareils et viewports. Un autre exemple de flux de travail qui considère le contexte complet du média cible.

![Image](https://cdn-media-1.freecodecamp.org/images/bzf4etJ84-4GUDSHBjH7udomDz8uz2RPqVmM)
_[Polypane](https://polypane.rocks/" rel="noopener" target="_blank" title=")—un navigateur web intelligent pour le design et le développement réactifs._

Ces éditeurs de code visuels sont simplement l'étape suivante dans la progression de la facilitation de l'écriture de code. Toutes ces innovations ont du sens et sont possibles parce qu'une grande partie du développement front-end est intrinsèquement visuelle.

Alerte spoiler : Je suis d'accord avec la prédiction de Jason. Les outils de développement des navigateurs ont déjà commencé à aller dans cette direction, offrant des interfaces graphiques pour manipuler visuellement les styles CSS comme les transitions, les ombres et les couleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/YzzIidMbM7WKIpwVpaVKEkXg8KIViXcKz5BZ)
_Un ensemble d'interfaces graphiques pour manipuler le code visuellement à l'intérieur des outils de développement de Google Chrome._

Bien sûr, les outils de développement des navigateurs fonctionnent sur du code compilé, mais ces mêmes outils visuels peuvent s'appliquer au code précompilé également. [Compositor Lab](https://compositor.io/lab/) et [Modulz Editor](https://twitter.com/colmtuite/status/965146829716324352) facilitent l'édition visuelle des composants React.

![Image](https://cdn-media-1.freecodecamp.org/images/fc47Z5wnWlZ2Gl5U7umC0jAJ13JIyHY9tvVE)
_[Modulz Editor](https://twitter.com/colmtuite/status/954715289517805568" rel="noopener" target="_blank" title=")—un outil pour concevoir des composants React visuellement._

[Xcode](https://developer.apple.com/xcode/) est un outil largement sous-estimé—permettant aux équipes de concevoir, développer, tester et déboguer leurs produits à travers une combinaison d'édition de code et de manipulation directe.

Le [Lona](https://github.com/airbnb/Lona) d'Airbnb est l'un des éditeurs de code visuel les plus prometteurs que j'aie vus. Lona Studio fournit une interface graphique pour construire des systèmes de composants, maquetter de nouveaux écrans à partir de composants existants, prévisualiser des designs avec des données réelles, expérimenter avec plusieurs tailles d'écran, et **beaucoup** plus.

Cette même progression peut également être observée dans d'autres industries comme le design de jeux, la production musicale, l'architecture, le montage vidéo, etc. Parmi d'autres, [Maya](https://www.autodesk.eu/products/maya-lt/overview), [Unity](https://unity3d.com/), [Cubase](https://www.steinberg.net/en/products/cubase/cubase_pro.html), [Logic Pro](https://www.apple.com/lae/logic-pro/) et [Final Cut](https://www.apple.com/lae/final-cut-pro/) fournissent tous des outils pour la manipulation directe afin que des équipes entières puissent collaborer sur le même produit.

Bien que chacun de ces outils fonctionne à un niveau d'abstraction différent, ils partagent tous le même objectif : rendre le code plus digeste, plus gérable, plus visuel et plus accessible à un public plus large.

Bien que ces outils puissent sembler très différents, le concept sous-jacent reste constant. Il n'y a pas de changement de paradigme fondamental. Il n'y a pas de duplication de travail. Pas d'effort gaspillé. Il n'y a pas de fausses simulations ou de rendus inexacts. Il n'y a pas de manque de contexte. Il y a juste du code, sous de nombreuses formes.

En continuant avec ce récit, nous pouvons exposer les designers d'interface utilisateur à la réalité des médias pour lesquels nous concevons, tout en cachant toute la complexité irrélevante, nous permettant de prendre des décisions de design bien informées.

### Le dilemme

Les équipes de design, les entreprises et les investisseurs ont investi d'énormes quantités de temps et d'argent dans le soutien d'un processus de design brisé : le flux de travail traditionnel basé sur les images.

Une industrie entière a été construite sur cette fondation instable : des outils pour dessiner des images, des outils pour ajouter des interactions aux images, des outils pour versionner les images, des outils pour stocker les images, des outils pour extraire des données des images. Chacun d'eux tentant de faire en sorte que ces imitations statiques ressemblent davantage au vrai produit—comme si, en superposant des simulations sur des simulations, nous pouvions somehow combler l'impossible distance entre les graphiques vectoriels et les logiciels interactifs.

Aujourd'hui, nos produits numériques embrassent des technologies de plus en plus complexes : micro-interactions, animations, AR, VR, entrée vocale, sortie audio, vidéo, multiples densités de pixels, dimensions de viewport infinies, détection de luminosité, etc. Alors que les designers continuent d'explorer ces nouveaux territoires, les outils de dessin vectoriel continueront d'être exposés pour leurs lacunes.

Considérez comment le paysage du design pourrait changer au cours des cinq prochaines années. Comment chacun de ces récits va-t-il se dérouler ? Pour avoir une idée précise, je pense qu'il est préférable de revenir aux bases et de nous poser quelques questions difficiles.

Que signifie concevoir des produits numériques aujourd'hui ? Quels aspects du design un outil de design devrait-il accélérer, automatiser ou simplifier ?

Je me souviens encore comment Rebekah Cox, l'une de mes designers préférées de tous les temps, a défini [ce que le design de produit signifiait chez Quora](http://www.artypapers.com/ap.log/thread.php?346) dans les premiers jours.

> "Une interface utilisateur est le produit d'un design. Un design est un ensemble de décisions concernant un produit particulier." — Rebekah Cox

Cela fait presque une décennie que j'ai lu pour la première fois cette définition du design, mais elle est restée avec moi toutes ces années. C'était la première fois que je comprenais qu'une interface est le résultat du design, et non le design lui-même. Le design est l'ensemble des décisions qui ont conduit au produit.

Donc, si le design est un ensemble de décisions, quelles décisions entrent dans la conception des produits numériques d'aujourd'hui ? Voici un petit échantillon qui me vient à l'esprit :

* Comment un bouton devrait-il se comporter lorsqu'il est survolé, pressé, focalisé ou désactivé ?
* Comment cette interface devrait-elle se comporter lorsqu'il n'y a pas de données pour la remplir ?
* Comment cette interface va-t-elle gérer les chaînes de données inhabituellement longues ?
* Dans quel ordre les éléments doivent-ils recevoir le focus lors de la tabulation ?
* Des raccourcis clavier doivent-ils être disponibles pour interagir avec cette interface ?
* Des commandes vocales doivent-elles être disponibles pour interagir avec cette interface ?
* Des sons doivent-ils être joués lors de l'interaction avec cette interface ?
* Comment cette couleur ou cette police va-t-elle s'afficher sur toutes les permutations les plus courantes de navigateurs, versions de navigateurs et systèmes d'exploitation ?
* Comment le petit changement que j'apporte à ce composant de bouton va-t-il impacter d'autres zones du produit ?
* Comment le composant x devrait-il se comporter lorsque ses données ne sont pas encore chargées ?
* Comment le composant x devrait-il se comporter pendant le chargement de ses données ?
* Comment cette mise en page devrait-elle s'adapter à l'infinie variété de dimensions de viewport, de ratios d'aspect et de densités de pixels possibles sur le web ?

Ce sont les types de décisions que les designers de produits numériques réfléchissent quotidiennement. Non seulement nous devons prendre ces décisions, mais nous devons également les tester, les examiner, les communiquer et les vendre.

Mais de telles décisions nuancées de produit ne peuvent pas être capturées dans une collection de vecteurs, même avec des interactions superposées.

Plus tôt, j'ai fait référence à la "transmission aux développeurs" comme étant controversée. Ce que je voulais dire, c'est ceci : le flux de travail fortement promu allant des maquettes statiques au code a peu de sens compte tenu des vastes différences entre les deux médias.

Le problème avec la "transmission aux développeurs" n'est pas dans le nom. Ni dans la mise en œuvre. Même la notion de designers passant leur travail le long de la chaîne de production est conceptuellement solide.

Le problème est qu'il n'y a rien d'utile à "transmettre". Extraire les informations des vecteurs n'est pas la partie difficile. Honnêtement, la plupart de ces informations sont inutiles de toute façon. C'est obtenir les informations nécessaires **dans** le vecteur qui est le défi. C'est la raison pour laquelle les outils de dessin vectoriel ne sont pas bien adaptés au design d'interface utilisateur. Les graphiques vectoriels sont physiquement incapables de contenir le type d'informations nécessaires pour informer adéquatement la conception d'un produit numérique.

Mais même si nous pouvions somehow emballer ces décisions dans des graphiques vectoriels, les outils d'illustration ne fournissent pas un environnement propice à la prise de décisions clés concernant un produit numérique. Vous ne pouvez pas prendre de décisions de design de produit bien informées dans un environnement qui manque de tout contexte du média pour lequel vous concevez.

Ce sont les décisions qui font ou défont les produits numériques. Si vous voulez être celui qui prend ces décisions, vous devez vous familiariser avec les nombreux environnements dans lesquels votre produit existera.

> "Le code de production est un substitut au pouvoir de décision. Le code de production est la source de vérité. Il est la somme en temps réel de toutes les conversations, de toutes les décisions, de toute la politique... c'est tout. Celui qui pousse le code en production dirige le produit. Tout le monde n'a que de l'influence." — Rebekah Cox

Rebekah propose que les personnes ayant le plus de pouvoir de décision sont celles qui sont les plus proches du code.

Si nos outils de design doivent nous fournir le même niveau d'influence sur le produit que les développeurs ont exclusivement apprécié pendant des décennies, ils doivent abandonner les flux de travail brisés du passé et continuer à embrasser les médias interactifs de l'avenir.

_Si vous êtes intéressé par [Modulz](https://www.modulz.co/), le nouvel outil de design sur lequel je travaille, nous publions régulièrement des mises à jour sur [Twitter](https://twitter.com/Modulz). Si vous voulez discuter des outils ou des systèmes, n'hésitez pas à me contacter par email ou sur [Twitter](https://twitter.com/colmtuite)._

_Merci à Dave Feldman, Adam Morse, Scott Raymond, Patrick Smith, Michael Le, Kilian Valkhof, David Tuite et autres pour leur aide à l'édition._