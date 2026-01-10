---
title: Qu'est-ce qu'une bibliothèque de composants ? Quand construire la vôtre et
  quand utiliser celle de quelqu'un d'autre
date: '2024-08-13T14:58:56.725Z'
author: Andrico Karoulla
authorURL: https://www.freecodecamp.org/news/author/andrico1234/
originalURL: https://freecodecamp.org/news/what-is-a-component-library-when-to-build-your-own
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723543483889/400c638b-4a6f-430a-92c3-4d8a7b750464.png
tags:
- name: Web Development
  slug: web-development
- name: JavaScript
  slug: javascript
- name: Beginner Developers
  slug: beginners
- name: component libraries
  slug: component-libraries
seo_desc: 'If you''ve built a frontend project in the last five years, you will have
  likely written some components, and maybe even used a component library.

  Components and libraries have been an important part of the web development landscape
  for multiple decad...'
---


Si vous avez construit un projet frontend au cours des cinq dernières années, vous avez probablement écrit des composants, et peut-être même utilisé une bibliothèque de composants.

<!-- more -->

Les composants et les bibliothèques sont des éléments essentiels du paysage du développement web depuis plusieurs décennies maintenant, et ils sont plus utiles et importants que jamais.

Il y aura des moments où vous devrez construire votre propre bibliothèque de composants, et d'autres où il sera préférable d'utiliser une option tierce. À la fin de cet article, vous connaîtrez les avantages et les inconvénients de chaque approche, et vous pourrez prendre la bonne décision pour votre prochain projet.

### Table des matières :

-   [Une analogie : et si les albums de musique pré-enregistrés n'existaient pas ?][1]
    
-   [Pourquoi j'écris ce guide][2]
    
-   [Qu'est-ce qu'un composant ?][3]
    
-   [Qu'est-ce qu'une bibliothèque de composants ?][4]
    
-   [Quelle est la différence entre une bibliothèque de composants et un design system ?][5]
    
    -   [Design Systems][6]
        
    -   [Bibliothèques de composants][7]
        
-   [Une brève histoire des bibliothèques de composants][8]
    
-   [Qu'est-ce qui fait une bonne bibliothèque de composants ?][9]
    
-   [Quels sont les avantages d'utiliser une bibliothèque de composants ?][10]
    
-   [Quels sont les inconvénients d'utiliser une bibliothèque de composants tierce ?][11]
    
-   [Les différentes formes que peut prendre une bibliothèque de composants][12]
    
    -   [Bibliothèques de classes utilitaires / Guides de styles CSS][13]
        
    -   [Bibliothèques de composants prête à l'emploi][14]
        
    -   [Composants non stylisés][15]
        
    -   [Bibliothèques de composants par copier-coller][16]
        
-   [Pourquoi n'y a-t-il pas une bibliothèque de composants unique pour les gouverner toutes ?][17]
    
-   [Devriez-vous construire votre propre bibliothèque de composants ?][18]
    
-   [Quand (et pourquoi) il est utile de construire sa propre bibliothèque de composants][19]
    

## Une analogie : et si les albums de musique pré-enregistrés n'existaient pas ?

Je suis un grand fan de musique. L'un de mes passe-temps favoris est de mettre un disque et de l'écouter du début à la fin. Un album de musique est simple dans son concept : c'est une suite de pistes enregistrées par un artiste et considérée comme un ensemble de chansons complet et cohérent.

Mais que se passerait-il si la musique enregistrée n'existait pas ? Au lieu de graver des chansons sur bande, CD ou mp3 (ou FLAC si vous êtes de ce genre-là), vous ne pourriez écouter un album que si l'artiste le jouait en direct pour vous. Vous devriez aller voir le groupe, leur demander d'installer leur équipement et les faire jouer l'album de bout en bout. Ils devraient le jouer de la même manière à chaque fois pour s'assurer que tout le monde vive exactement la même expérience.

Les fissures commenceraient à apparaître. Ce n'est pas un moyen efficace de s'assurer que toute personne intéressée par la musique du groupe puisse l'écouter. Si Taylor Swift devait jouer sa chanson Fortnight personnellement pour chaque personne qui l'écoute sur Spotify, cela lui prendrait 3 179 ans. Et cela ne tient pas compte des [voyages en avion][20]. Les artistes s'ennuieraient, deviendraient peut-être même négligents, ce qui entraînerait une expérience médiocre pour leurs auditeurs.

Alors, quel est le rapport avec le développement web ? Chaque fois que vous construisez un contrôle UI, vous devez vous assurer qu'il est fonctionnel, robuste et accessible. Vous finirez par vous ennuyer si vous réécrivez sans cesse la même interface utilisateur. Des erreurs se glisseront, entraînant une mauvaise expérience pour vos utilisateurs finaux.

## Pourquoi j'écris ce guide

Je suis développeur web depuis près de 10 ans, et j'ai écrit des centaines de composants, souvent le même pattern UI à de nombreuses reprises. J'ai utilisé des dizaines de bibliothèques de composants et j'ai construit des tableaux de bord d'administration, des bibliothèques de composants, des applications mobiles, des blogs, des plugins Figma, des extensions VSCode, et plus encore.

Dans cet article, je discuterai du rôle des composants et des bibliothèques dans le développement web, et de la pertinence pour les développeurs d'écrire les leurs.

Je suis également le créateur de [Component Odyssey][21], un cours qui vous apprendra à construire votre propre bibliothèque de composants fonctionnant dans n'importe quel framework frontend.

## Qu'est-ce qu'un composant ?

Lors de la construction d'interfaces utilisateur, nous n'écrivons pas tout le balisage HTML à partir de zéro à chaque fois. Nous écrivons nos interfaces en utilisant des composants – des blocs de construction réutilisables qui encapsulent des patterns UI communs. Écrire un composant vous permet de l'utiliser plusieurs fois dans un seul projet ou même dans des projets indépendants.

Ici, j'ai écrit un composant de compteur. Je l'ai écrit une fois et je l'ai utilisé à plusieurs endroits sur la page.

```
<body>
  <div class="wrapper">
    <counter-button></counter-button>
    <counter-button></counter-button>
    <counter-button></counter-button>
  </div>

  <script type="module">
    import { LitElement, html } from 'lit';

    class CounterButton extends LitElement {
      constructor() {
        super();
        this.count = 0;
      }

      static properties = {
        count: { type: Number }
      };

      _increment() {
        this.count++;
      }

      render() {
        return html`
          <button @click=${this._increment}>Count: ${this.count}</button>
        `;
      }
    }

    customElements.define('counter-button', CounterButton);
  </script>
</body>
```

Nous, les créateurs de tutoriels, aimons faire des démos de compteurs comme s'ils allaient disparaître – mais une application réelle contiendra des dizaines de patterns UI différents écrits sous forme de composants.

Dans cet article, je regrouperai les règles CSS qui fournissent le style pour certains patterns UI sous l'ombrelle des composants. La définition peut devenir floue selon la personne à qui vous demandez.

## Qu'est-ce qu'une bibliothèque de composants ?

Tous les composants ne sont pas autonomes. Il est logique que de nombreux composants soient regroupés au sein d'un seul paquet, appelé bibliothèque de composants.

Si vous voulez que votre site ait un aspect ou une sensation spécifique, vous pouvez utiliser une _bibliothèque de composants_. Il existe des bibliothèques de composants qui :

-   proposent des composants conformes à une spécification de design.
    
-   proposent plusieurs solutions pour un pattern UI spécifique.
    
-   fonctionnent avec une toolchain spécifique.
    

Mais elles se présentent sous différentes formes et tailles. La définition que j'en suis venu à utiliser pour définir une bibliothèque de composants est la suivante :

_Une bibliothèque de composants est un ensemble de composants réutilisables qui sont cohérents dans leur utilité, ou leur apparence (ou les deux). Une excellente bibliothèque de composants aidera les développeurs à répondre efficacement à leurs besoins d'interface utilisateur, tout en offrant une expérience exemplaire pour l'utilisateur final._

## Quelle est la différence entre une bibliothèque de composants et un design system ?

Je parlerai des directives et des design systems plus loin dans cet article, je vais donc prendre un moment pour les lever toute ambiguïté. Il peut être difficile de voir où l'un s'arrête, où l'autre commence, ou si l'un englobe l'autre.

### **Design Systems**

Je vois un design system comme une spécification de la façon dont les choses doivent paraître, être ressenties et se comporter. Un design system peut englober un produit, une marque ou une entreprise pour assurer la cohérence à travers l'ensemble des expériences. Un design system complet dictera tout, des familles de polices, tailles de polices et espacements, aux patterns UI et directives de rédaction.

Quelques-uns des design systems les plus connus incluent :

-   [Material Design][22] (Google)
    
-   [Base Design][23] (Uber)
    
-   [Lightning Design System][24] (Salesforce)
    

Bien que de nombreux design systems soient spécifiques à des entreprises, il existe des design systems, comme Material Design, que des équipes du monde entier utilisent pour créer rapidement des produits familiers. Vous avez probablement utilisé une poignée de produits qui utilisent les principes de Material Design, mais ils ne sont [certainement pas exempts de problèmes d'utilisabilité de base][25].

### **Bibliothèques de composants**

Quant aux bibliothèques de composants, elles peuvent être ou non l'implémentation logicielle d'un design system. Si vous travaillez pour une entreprise disposant d'un design system, il est probable que la bibliothèque de composants correspondante (si elle existe) y soit étroitement intégrée.

Par exemple, [Material Web][26] de Google est une implémentation web component de Material Design. [Base Web][27] et [Lightning Web Components][28] sont également open source.

## Une brève histoire des bibliothèques de composants

Le concept de composants UI (ou widgets) existe depuis longtemps. Si vous voulez voir une collection de musée d'interfaces utilisateur rétro, prenez du pop-corn et regardez cette [vidéo de plus de 2 heures de "tous les widgets" de 1974 à 1990][29].

Dès le début des années 2000, nous avons commencé à voir apparaître des bibliothèques de composants conçues pour aider les développeurs à construire pour le web.

Le paysage des navigateurs web à l'époque était méconnaissable par rapport à ce que nous voyons aujourd'hui. Les versions d'Internet Explorer déviaient entièrement de la spécification, ce qui était particulièrement problématique étant donné l'[énorme part de marché qu'IE détenait à l'époque][30]. [Internet Explorer 6 était célèbre pour être un calvaire à développer][31]. C'était principalement dû à son implémentation incorrecte du [modèle de boîte (box model)][32] et à l'absence de support CSS2.

> 💡 Le saviez-vous : Internet Explorer supportait un « [quirks mode][33] » qui permettait aux développeurs d'écrire du HTML et du CSS non standard pour satisfaire les anciens navigateurs qui ne supportaient pas les standards.

Heureusement, quand j'ai commencé sérieusement le développement web, beaucoup de ces problèmes étaient résolus. À ce stade, il existait encore quelques bibliothèques qui facilitaient l'écriture d'interfaces complexes avec un support multi-navigateur.

[jQuery UI][34], la première bibliothèque de composants que j'ai utilisée, supportait les accordéons et d'autres widgets. Mais le navigateur évolue constamment, et nous avons maintenant un moyen natif d'implémenter ce pattern d'accordéon en utilisant les éléments `details` et `summary`, disponibles dans tous les navigateurs depuis 2020.

Avec ces éléments, vous pouvez aller assez loin dans la création d'accordéons interactifs sans JavaScript.

Comparez cela avec 2009, avant que ces éléments ne soient implémentés dans aucun navigateur. Cela nécessitait pas mal de JS pour fonctionner. Jetez un œil au [code source de jQuery UI v1.7][35], et faites CTRL+F « accordion » si vous voulez voir comment les développeurs web implémentaient les accordéons il y a 15 ans.

Au cours des deux décennies suivantes, les capacités du web ont grandi. Des appareils plus puissants signifiaient des navigateurs plus puissants. Des navigateurs plus puissants signifiaient que les applications web devenaient plus ambitieuses.

Les développeurs ont répondu en créant des outils pour nous aider à construire ces applications en nous permettant de créer des interfaces utilisateur à l'aide de _blocs de construction_ – c'est-à-dire un modèle de composants. Nous avons vu une prolifération de ces frameworks basés sur les composants. Je parle d'Angular, React et Vue. Et chacun possède son propre écosystème riche de bibliothèques de composants.

On peut raisonnablement soutenir qu'il y a eu une sur-correction et que le paysage frontend est maintenant sursaturé d'outils trop puissants pour les besoins de la plupart des gens... mais n'entrons pas là-dedans.

## Qu'est-ce qui fait une bonne bibliothèque de composants ?

Le défi avec la construction d'une bibliothèque de composants est qu'il ne s'agit pas d'une solution _unique et définitive_. Beaucoup des bibliothèques les plus populaires existent depuis des années et ont bénéficié de tonnes de recherche, de retours d'utilisation et de contributions pour en arriver là où elles sont aujourd'hui.

J'ai trouvé qu'une bonne bibliothèque de composants possède souvent les traits suivants :

-   Elle comprend les problèmes de ses développeurs cibles et résout bien ces problèmes.
    
-   Elle possède une excellente documentation.
    
-   Elle garantit une bonne expérience pour l'utilisateur final.
    
-   Elle est robuste et s'adapte aux modes de saisie et aux appareils appropriés.
    

À l'inverse, une façon de discerner si une bibliothèque de composants _n'est pas bonne_ est si elle ne prend pas en compte l'accessibilité, possède une API incohérente, n'a que peu ou pas de pilotage (stewardship) de projet, ou n'a pas de documentation claire et cohérente.

## Quels sont les avantages d'utiliser une bibliothèque de composants ?

Nous savons à quoi ressemble une bonne bibliothèque de composants – voyons maintenant comment elle peut rendre votre vie, et celle de vos utilisateurs, un peu meilleure.

### Les bibliothèques de composants vous font gagner du temps

Si vous êtes sur un projet avec un délai serré, il est important d'être efficace. Mais l'efficacité ne doit pas se faire au détriment de la création d'une expérience web robuste. Utiliser une bibliothèque de composants vous permet de passer moins de temps à réinventer la roue et plus de temps à vous concentrer sur les détails les plus fins.

### Les bibliothèques de composants vous rendent, vous et vos utilisateurs, plus heureux

Nous ne sommes pas motivés par le travail répétitif. Nous aimons les défis techniques, et écrire les mêmes composants encore et encore n'est pas un défi amusant. Nous avons déjà parlé de ce qui se passe quand nous nous ennuyons et que nous laissons passer des erreurs.

Si vous vouliez implémenter un composant de dialogue à partir de zéro, vous devriez :

-   Gérer correctement le piégeage du focus (focus trapping).
    
-   Rendre le reste de la page inerte.
    
-   Positionner le dialogue correctement.
    
-   S'assurer qu'il fonctionne avec les technologies d'assistance.
    

Il faut du travail pour se souvenir et implémenter ce qui précède, mais la conséquence d'une erreur peut rendre votre interface littéralement inutilisable. C'est le cas si vous [gérez mal le focus][36].

En utilisant une bibliothèque de composants conçue en pensant aux utilisateurs finaux, vous pouvez prévenir le risque d'introduire des expériences défectueuses, tout en passant moins de temps à reconstruire les mêmes composants.

### Les bibliothèques de composants mènent à des expériences cohérentes

Si vous travaillez pour une entreprise possédant plusieurs applications web différentes, elles suivront généralement un ensemble de directives. Ces directives peuvent dicter la palette de couleurs à utiliser, la taille de votre typographie ou l'apparence et le comportement des éléments de l'interface utilisateur.

Mais vous augmentez la probabilité que votre application dévie du guide de style si vous réécrivez les composants. En ayant une bibliothèque de composants, vous pouvez plus facilement auditer l'interface utilisateur de votre composant par rapport aux directives de la marque afin qu'ils soient parfaits, quel que soit l'endroit où ils sont utilisés.

Uber possède plusieurs applications différentes qui partagent les mêmes éléments d'interface utilisateur. Je suis presque certain qu'ils utilisent la même bibliothèque de composants à travers ces applications. De cette façon, chaque nouvelle application est virtuellement garantie de respecter les directives de la marque.

![Différentes applications Uber côte à côte, montrant leur similitude en termes d'apparence](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4lh0etdq7yhk4zhmiac8.png)

## Quels sont les inconvénients d'utiliser une bibliothèque de composants tierce ?

Les avantages que j'ai mentionnés ci-dessus s'appliquent que vous utilisiez votre propre bibliothèque de composants ou une tierce. Si vous ou votre équipe avez décidé de ne pas construire de bibliothèque et de vous appuyer sur une solution tierce, il vaut la peine de considérer ce qui suit.

### Verrouillage fournisseur (Vendor Lock-in)

En choisissant une bibliothèque de composants, vous choisissez un partenaire qui aura un impact considérable sur la façon dont vous écrivez votre code frontend et sur l'apparence et le comportement de vos interfaces.

Le premier point aura un impact important sur vous, et le second sur vos utilisateurs finaux. Utiliser une bibliothèque de composants vous enferme dans les standards de cette bibliothèque.

La bibliothèque pourrait introduire des changements majeurs (breaking changes) massifs dans une version majeure qui pourraient nécessiter un temps de développement dédié et beaucoup de tests pour s'assurer qu'aucune régression sérieuse n'a été introduite.

Il y a quelques années, j'ai utilisé React Admin pour construire un tableau de bord d'administration complexe pour une division interne. La bibliothèque offrait une suite de composants spécifiquement dédiés à la récupération et à l'affichage de données complexes.

Parce que notre application à l'époque reposait lourdement sur React Admin, la mise à niveau entre les versions majeures était difficile, d'autant plus que de nombreux outils internes utilisés par React Admin avaient été remplacés par d'autres. La surface de changement était énorme, et nous avons passé beaucoup de temps à mettre à jour et à signaler les problèmes que nous repérions.

Je ne pense pas que construire notre propre solution nous aurait fait gagner du temps à long terme, mais ce genre de verrouillage fournisseur (vendor lock-in) mérite d'être pris en considération, surtout avant de s'engager pleinement dans un outil.

### Gonflement du code (Code Bloat)

Aussi choquant que cela puisse paraître, les bibliothèques comportant beaucoup de composants ont tendance à être écrites avec beaucoup de code. Du code que vous téléchargez lors de l'installation des dépendances, et du code que vous envoyez à vos utilisateurs finaux.

L'outillage moderne facilite les optimisations de bundle comme le tree-shaking pour supprimer le code inutilisé, mais il n'y a aucune garantie que vous supprimiez tout le code dont vos utilisateurs n'auront pas besoin.

À moins de plonger profondément dans les bibliothèques que vous utilisez, vous ne serez peut-être pas conscient de tous les paquets séparés qu'elles importent. Vous pourriez vous retrouver avec des centaines de dépendances inutiles. Les membres de la communauté [e18e][37] travaillent dur pour mettre ce problème en lumière, [tout en le corrigeant également][38].

Beaucoup de ces problèmes pourraient également être soulevés lors du déploiement de votre propre bibliothèque de composants. La plus grande différence est que vous avez la gérance (stewardship) de votre bibliothèque de composants. Vous êtes en mesure de définir comment elle résout vos problèmes spécifiques, et vous avez le contrôle sur l'amélioration de ses lacunes.

## Les différentes formes que peut prendre une bibliothèque de composants

La [proposition initiale][39] pour le World Wide Web était un outil pour améliorer la communication entre les chercheurs du CERN. La proposition décrivait comment les documents pouvaient être partagés et liés les uns aux autres grâce à l'utilisation de l'hypertexte.

C'est la pierre angulaire fondamentale du web, et nous utilisons toujours la modeste balise `<a>` pour créer des liens entre d'autres documents HTML à travers le web.

Mais la portée du web s'est étendue au cours des dernières décennies, et les navigateurs que nous utilisons pour naviguer sur le web sont devenus des monstres à part entière. Les navigateurs d'aujourd'hui permettent de [puissantes formes d'expression créative][40] et l'[exécution de logiciels de type natif][41].

Il existe des centaines de solutions différentes, certaines polyvalentes, d'autres hyper-niche, mais trouver le bon outil pour votre prochain projet nécessite un processus de décision complexe qui pourrait ressembler à ceci :

![Les différents types de bibliothèques de composants et quand les utiliser. Le contexte du diagramme est exploré ci-dessous](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bn80olo3e0h8v4h4v311.png)

Ceci n'est pas une liste exhaustive de TOUS les cas d'utilisation ou types de bibliothèques de composants, mais elle illustre comment les bibliothèques de composants diffèrent en termes de :

-   technologies impliquées.
    
-   niveaux d'abstraction qu'elles offrent.
    
-   problèmes qu'elles résolvent.
    

Jetons un coup d'œil à certains des types de bibliothèques de composants les plus courants.

💡 Une petite note : Si vous êtes intéressé par la construction de votre propre bibliothèque de web components, alors considérez mon cours [Component Odyssey][42]. Vous apprendrez à construire et à publier une bibliothèque de composants qui fonctionne dans n'importe quel framework frontend.

### Bibliothèques de classes utilitaires / Guides de styles CSS

Pour moi, [Bootstrap][43] est le premier qui vient à l'esprit. À l'époque, si vous vouliez donner un coup de frais rapide à votre site, vous ajoutiez le lien CDN vers le fichier CSS de Bootstrap et obteniez immédiatement le look Bootstrap. C'était partout au milieu des années 2010.

![Un exemple de démo d'un site web Bootstrap, vers 2013](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7zl86ek2nhsoxc043pnt.png)

La portée technique de ce genre d'outils s'étend de :

-   Un seul fichier CSS ([Pico][44])

à

-   Une toolchain pour générer des classes CSS basées sur votre configuration ([Tailwind][45])

Des dizaines d'autres outils, comme [Open Props][46], se situent quelque part entre les deux.

### Bibliothèques de composants prête à l'emploi

Si vous construisez une application web interactive, vous pourriez simplement vouloir récupérer une suite de composants qui ont fière allure et fonctionnent bien. Il existe de nombreuses bibliothèques de composants prêtes à l'emploi qui vous donnent tout ce dont vous avez besoin et plus encore.

Quel que soit le framework avec lequel vous écrivez votre application, il est probable qu'il existe un ensemble de composants esthétiques à votre disposition.

Une autre excellente bibliothèque de composants est [Shoelace][47], qui fournit des dizaines de composants entièrement interactifs et stylisés.

Ce qui rend les bibliothèques comme Shoelace particulièrement intéressantes, c'est qu'elles sont construites à l'aide de web components, la méthode intégrée au navigateur pour écrire des composants. Construire vos interfaces avec des outils comme Shoelace vous donne l'avantage supplémentaire de pouvoir les utiliser à travers différents frameworks frontend. [C'est quelque chose dont j'ai un peu parlé par le passé.][48]

Voici le même composant Shoelace utilisé dans Vue et React :

![Boutons Shoelace dans Vue et React](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/anphi6seqnbqvjd0q7ty.gif)

### Composants non stylisés (Headless)

Selon les spécifications de votre projet, vous n'aurez peut-être pas le luxe d'utiliser un outil prêt à l'emploi. Vos spécifications de design peuvent être très précises.

J'ai vu des équipes créer leurs propres composants au premier signe de friction. Et dans un cas de sélecteur de date fait maison, cela a conduit à une expérience utilisateur bien pire. Rétrospectivement, l'utilisation d'une bibliothèque de composants non stylisés aurait donné à l'équipe de la flexibilité sur l'apparence, tout en garantissant que le comportement lié au temps, notoirement délicat, soit correct.

C'est pourquoi vous pouvez vous tourner vers une bibliothèque qui propose des composants complètement non stylisés avec des hooks de stylisation flexibles. S'il s'agit d'une bonne bibliothèque, elle s'occupera également de toutes ces interactions complexes. C'est une situation gagnant-gagnant.

Il est facile de rater une case à cocher si vous voulez aller au-delà des hooks de stylisation fournis par le navigateur, à moins de tester avec une large gamme d'appareils et de modes de saisie.

<iframe width="640" height="360" src="https://player.vimeo.com/video/995085532" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="Vimeo embed" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen="" loading="lazy"></iframe>

[Radix][49] est un exemple populaire de bibliothèque, mais elle est construite avec React.

D'autres exemples de bibliothèques de composants de ce type sont [Lion][50] et [HeadlessUI][51].

### Bibliothèques de composants par copier-coller

Certains développeurs veulent le meilleur des deux mondes. Ils peuvent vouloir un composant construit par une bibliothèque tierce de confiance, tout en ayant un contrôle total sur le balisage, les styles et les fonctionnalités.

Des bibliothèques comme [ShadCN][52] permettent ce genre de flux de travail en permettant aux développeurs de copier et coller la définition du composant dans leurs propres projets, leur permettant ainsi de _posséder_ le composant.

## Pourquoi n'y a-t-il pas une bibliothèque de composants unique pour les gouverner toutes ?

À ce stade, il est probablement clair pourquoi une telle bibliothèque de composants unique n'existe pas. Nous avons jeté un coup d'œil non exhaustif à différents groupes de bibliothèques de composants.

Il existe cependant un mouvement pour introduire un « [Global Design System][53] », un concept mené par Brad Frost.

Dans l'annonce, Brad souligne que dans les centaines de projets auxquels il a participé, de nombreux contrôles UI se comportent (ou devraient se comporter) de manière similaire à travers ces divers projets – mais les développeurs réimplémentent la même chose dans chaque projet.

Cela a conduit à beaucoup de temps et d'efforts perdus, et à des incohérences entre les projets. Cela s'étend également aux bibliothèques de composants existantes. Vous verrez que le comportement du clavier pour une combobox dans React Aria est différent de celui de la combobox dans ShadCN.

<iframe width="640" height="360" src="https://player.vimeo.com/video/995085659" style="aspect-ratio: 16 / 9; width: 100%; height: auto;" title="Vimeo embed" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen="" loading="lazy"></iframe>

Brad Frost propose un Global Design System sous la forme d'un ensemble de web components qui devraient être adoptables par presque n'importe quel projet frontend pour assurer une base de fonctionnalités pour les contrôles qui ne sont pas encore disponibles en HTML.

Des [discussions sont en cours au sein d'Open UI][54] pour voir comment cela pourrait commencer à prendre forme dans les prochaines années.

## Devriez-vous construire votre propre bibliothèque de composants ?

Cet article a approfondi le sujet des bibliothèques de composants. Et avec tout ce contexte, vous finirez inévitablement par vous demander, devant la page HTML vide de votre prochain grand projet, si vous devez construire votre propre bibliothèque de composants ou en utiliser une existante.

Ma première pensée est : _Je ne pense pas que vous devriez construire votre propre bibliothèque._

Je privilégie généralement le choix d'une bibliothèque éprouvée. Particulièrement une qui a :

-   Été utilisée dans des milliers de projets.
    
-   Une communauté forte, sur Discord ou GitHub.
    
-   Une excellente documentation.
    
-   Un fort accent sur l'accessibilité.
    
-   Travaillé avec les forces du framework choisi.
    

Le plus important de tous ces points est d'utiliser une bibliothèque de composants qui apporte un soin particulier à la construction de composants accessibles.

Prenez une combobox, par exemple. C'est un mélange d'un champ de recherche et d'un menu de sélection. Si vous avez construit la vôtre, vous pouvez réussir à la rendre esthétique et fonctionnelle avec votre souris. Mais vous devrez également considérer :

-   Le support multi-navigateur.
    
-   Le comportement de tabulation et de focus.
    
-   Le support des lecteurs d'écran.
    
-   La gestion des états pour le chargement asynchrone des résultats de recherche.
    

Konnor Rogers, qui fait un excellent travail dans l'espace web + web component, a partagé d'innombrables frustrations liées à ses expériences de construction d'une combobox accessible. Voici l'un de ces [tweets qu'il a partagés][55].

Le support des lecteurs d'écran est particulièrement complexe et mérite sa propre liste de points. Pour supporter les lecteurs d'écran, vous devrez également gérer :

-   les régions en direct (live regions).
    
-   les contrôles interactifs.
    
-   les éléments sélectionnés.
    
-   le support entre différents lecteurs d'écran.
    

En note latérale, je n'ai accès qu'à Voiceover, ce qui signifie qu'il m'est difficile de tester ces patterns UI complexes avec différents lecteurs d'écran. Comme les navigateurs, il existe des différences entre les lecteurs d'écran. Dans cet article, [Are We Live?][56], Scott O’Hara décrit comment il existe des variations dans la façon dont ils traitent les régions en direct.

Cela signifie qu'il vous appartient également, en tant que développeur, de choisir une bibliothèque de composants en laquelle vous pouvez avoir confiance quant à son développement axé sur l'accessibilité. C'est pourquoi il est également important de choisir une bibliothèque de composants qui possède une communauté forte.

Vous devriez être en mesure de :

-   Voir les bugs et les problèmes que d'autres ont signalés pour une bibliothèque donnée.
    
-   Suggérer (ou même contribuer à) des améliorations et des changements à la bibliothèque.
    
-   Discuter d'idées avec les membres de la communauté et établir des relations de travail avec des membres actifs ou même les mainteneurs eux-mêmes.
    

Enfin, et ce n'est pas le moins important, une excellente bibliothèque de composants considérera bien plus que l'esthétique de ses composants. Pour une bibliothèque de composants conçue pour le web, elle devrait faire de son mieux pour :

-   respecter les [Directives d'accessibilité aux contenus web (WCAG)][57].
    
-   s'assurer que les composants fonctionnent sur différentes modalités de saisie (tactile, clavier, lecteur d'écran).
    
-   s'assurer que les composants sont utilisables pour les personnes ayant des besoins supplémentaires, comme celles vivant avec des troubles vestibulaires, des déficiences visuelles ou une main cassée.
    

## Quand (et pourquoi) il est utile de construire sa propre bibliothèque de composants

Si je ne vous ai pas découragé de construire une bibliothèque de composants, laissez-moi me contredire et expliquer pourquoi cela peut être une très bonne chose de construire la vôtre.

Si vous prenez le temps d'apporter soin et attention à la construction d'une bibliothèque de composants, vous deviendrez un développeur qui comprend mieux la plateforme du navigateur, les meilleures pratiques d'accessibilité, les pratiques de test, et plus encore.

Mais cela ne s'arrête pas là : il existe d'excellentes raisons de construire votre propre bibliothèque.

Pour commencer, vous pouvez construire quelque chose de adapté à vos besoins et éviter une partie du gonflement (bloat) que vous pourriez obtenir d'une bibliothèque de composants prête à l'emploi. C'est à vous et à votre équipe de comprendre vos utilisateurs finaux, et vous pouvez construire quelque chose spécifiquement pour eux.

Vous avez également l'opportunité d'expérimenter des approches novatrices. Si vous avez un problème hyper-niche, il se peut qu'il n'y ait pas de bibliothèque de composants capable de résoudre ce besoin. Il pourrait s'agir d'une bibliothèque de composants qui :

-   Visualise les données d'une manière spécifique.
    
-   Possède une identité visuelle distincte et unique.
    
-   Est construite sur un nouveau framework.
    

Cela vous donne l'opportunité de construire quelque chose sur mesure. Vous avez ensuite la possibilité de changer et de corriger les choses à mesure que vos besoins évoluent ou que vous comprenez mieux l'espace du problème.

Surtout, vous en apprendrez davantage sur le web en le faisant. Si c'est la première fois que vous construisez une bibliothèque de composants, cela peut être l'occasion de plonger plus profondément dans les [spécifications HTML du navigateur][58], ou de parfaire vos [connaissances en accessibilité web][59]. Cela améliorera vos capacités en tant que développeur web, ce qui vous servira dans n'importe quel projet frontend à l'avenir. Cela pourrait même vous aider à décrocher votre prochain emploi.

Ainsi, la décision de construire une bibliothèque de composants dépend de vos objectifs finaux. Considérez des questions comme :

-   Est-ce que je veux mieux comprendre le navigateur ?
    
-   Est-ce que je veux construire quelque chose rapidement ?
    
-   Est-ce que je veux le rendre utilisable pour le plus grand nombre d'utilisateurs possible ?
    
-   Existe-t-il des bibliothèques qui résolvent mon problème actuel ?
    

Selon vos réponses, vous pourrez prendre la bonne décision pour votre projet.

## Merci de m'avoir lu !

Merci d'avoir exploré les bibliothèques de composants avec moi. Si vous êtes intéressé par la construction de votre propre bibliothèque de web components, alors considérez mon cours [Component Odyssey][60]. Vous apprendrez à construire et à publier une bibliothèque de composants qui fonctionne dans n'importe quel framework frontend.

💡 Je tiens à remercier tout particulièrement stephband ([Mastodon][61], [Bluesky][62]) pour la relecture et les commentaires.

---

![Andrico Karoulla](https://cdn.hashnode.com/res/hashnode/image/upload/v1663007071410/4i8XhoHghu.png)

Lire [plus d'articles][63].

---

Si cet article vous a été utile, partagez-le.

Apprenez à coder gratuitement. Le programme open source de freeCodeCamp a aidé plus de 40 000 personnes à trouver un emploi de développeur. [Commencer][64]

[1]: #heading-une-analogie-et-si-les-albums-de-musique-pre-enregistres-n-existaient-pas
[2]: #heading-pourquoi-j-ecris-ce-guide
[3]: #heading-qu-est-ce-qu-un-composant
[4]: #heading-qu-est-ce-qu-une-bibliotheque-de-composants
[5]: #heading-quelle-est-la-difference-entre-une-bibliotheque-de-composants-et-un-design-system
[6]: #heading-design-systems
[7]: #heading-bibliotheques-de-composants
[8]: #heading-une-breve-histoire-des-bibliotheques-de-composants
[9]: #heading-qu-est-ce-qui-fait-une-bonne-bibliotheque-de-composants
[10]: #heading-quels-sont-les-avantages-d-utiliser-une-bibliotheque-de-composants
[11]: #heading-quels-sont-les-inconvenients-d-utiliser-une-bibliotheque-de-composants-tierce
[12]: #heading-les-differentes-formes-que-peut-prendre-une-bibliotheque-de-composants
[13]: #heading-bibliotheques-de-classes-utilitaires-guides-de-styles-css
[14]: #heading-bibliotheques-de-composants-prete-a-l-emploi
[15]: #heading-composants-non-stylises
[16]: #heading-bibliotheques-de-composants-par-copier-coller
[17]: #heading-pourquoi-n-y-a-t-il-pas-une-bibliotheque-de-composants-unique-pour-les-gouverner-toutes
[18]: #heading-devriez-vous-construire-votre-propre-bibliotheque-de-composants
[19]: #heading-quand-et-pourquoi-il-est-utile-de-construire-sa-propre-bibliotheque-de-composants
[20]: https://www.threads.net/@adhd.international/post/C6ugTXAPt71?hl=en-gb
[21]: https://component-odyssey.com/
[22]: https://m3.material.io/foundations/layout/understanding-layout/overview
[23]: https://base.uber.com/6d2425e9f/p/294ab4-base-design-system
[24]: https://www.lightningdesignsystem.com/getting-started/
[25]: https://www.smashingmagazine.com/2021/02/material-design-text-fields/
[26]: https://material-web.dev/
[27]: https://baseweb.design/components/button/
[28]: https://lwc.dev/guide/introduction
[29]: https://vimeo.com/61556918
[30]: https://en.wikipedia.org/wiki/Usage_share_of_web_browsers#TheCounter.com_(2000_to_2009)
[31]: https://www.quora.com/Why-do-people-hate-IE6-so-much-and-want-it-to-die#:~:text=IE6%20doesn't%20support%20web,PNGs%20to%20natively%20support%20IE6
[32]: https://www.webfx.com/blog/web-design/definitive-guide-to-taming-the-ie6-beast/#616723179a361-3
[33]: https://www.notion.so/Complete-written-content-806882f918204715a6e45df68f492bdd?pvs=21
[34]: https://jqueryui.com/
[35]: https://code.jquery.com/ui/1.7.0/jquery-ui.js
[36]: https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap.html
[37]: https://e18e.dev/
[38]: https://x.com/DanaWoodman/status/1819084012729798833
[39]: https://cds.cern.ch/record/369245/files/dd-89-001.pdf
[40]: https://plumegame.com/
[41]: https://medium.com/@addyosmani/photoshop-is-now-on-the-web-38d70954365a
[42]: https://component-odyssey.com/
[43]: https://getbootstrap.com/
[44]: https://picocss.com/
[45]: https://tailwindcss.com/
[46]: https://open-props.style/
[47]: https://shoelace.style/
[48]: https://component-odyssey.com/articles/01-writing-components-that-work-in-any-framework
[49]: https://www.radix-ui.com/
[50]: https://lion-web.netlify.app/
[51]: https://headlessui.com/
[52]: https://ui.shadcn.com/
[53]: https://bradfrost.com/blog/post/a-global-design-system/
[54]: https://github.com/openui/open-ui/issues/1066
[55]: https://x.com/RogersKonnor/status/1797529313279140294
[56]: https://www.scottohara.me/blog/2022/02/05/are-we-live.html
[57]: https://www.w3.org/TR/WCAG21/
[58]: https://html.spec.whatwg.org/multipage/
[59]: https://www.w3.org/TR/WCAG21/
[60]: https://component-odyssey.com/
[61]: https://front-end.social/@stephband
[62]: https://bsky.app/profile/stephen.band
[63]: /news/author/andrico1234/
[64]: https://www.freecodecamp.org/learn/