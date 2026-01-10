---
title: iPhone sans bouton Home (Partie 2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T12:30:13.000Z'
originalURL: https://freecodecamp.org/news/homeless-iphone-part-2-1f7b3acc8a6c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Mvw-7X4soi0LMJnQyPbtg.png
tags:
- name: Apple
  slug: apple
- name: Design
  slug: design
- name: iphone
  slug: iphone
- name: prototyping
  slug: prototyping
- name: user experience
  slug: user-experience
seo_title: iPhone sans bouton Home (Partie 2)
seo_desc: 'By Fabrice Dubois

  Pause. Rewind. Deep dive in the design process.

  Two weeks ago I posted about the possibility of an iPhone that has no Home button
  at all.

  With iOS 11 on an iPad you enjoy a whole new app switcher. As a little design challenge,
  I stu...'
---

Par Fabrice Dubois

_Pause. Retour en arrière. Plongée profonde dans le processus de design._

Il y a deux semaines, j'ai [publié un article sur la possibilité d'un iPhone sans bouton Home](https://medium.freecodecamp.org/homeless-iphone-20c154fabbf7).

Avec iOS 11 sur un iPad, vous profitez d'un tout nouveau sélecteur d'applications. En tant que petit défi de design, j'étudie comment cette interface pourrait fonctionner sur l'imminent 'iPhone 8', et si elle pourrait s'adapter à l'absence de bouton Home.

Aujourd'hui, j'ai mis en pause l'exploration et je vous guide à travers le processus de design. Nous examinerons mes croquis en détail, verrons ce qu'ils révèlent sur le fil de la pensée (_aïe !_), et regarderons quelques variantes de prototypes que vous pourrez télécharger et essayer.

> Être orienté processus, et non produit, est la compétence la plus importante et difficile pour un designer à développer.

> Matthew Frederick

Les croquis et prototypes ci-dessous sont fournis _tels quels_, ils n'ont pas été modifiés pour les besoins de cet article. J'inclus des scans bruts de mes grandes planches de croquis, donc l'article est probablement mieux vu sur un ordinateur de bureau ou une tablette.

### Croquis

Je garde toujours mes croquis et notes. Ils sont utiles pour revoir au ralenti ce qui s'est passé dans l'esprit, évaluer le raisonnement, et jeter un regard neuf sur les idées en germination qui ont été oubliées en chemin.

Pour ce projet, j'ai utilisé deux feuilles A3. Commentons les écrans clés :

> **_1._** **_Essayer de forcer l'adaptation du design de l'iPad._** _Dans cette première tentative, tout est sur une seule vue de défilement horizontal. Et il y a un bouton Home ! Faux départ._

> **_2._** **_Essayer à nouveau._** _Mais m'arrêter rapidement car clairement, cela ne va pas fonctionner. Mes proportions sont complètement irréalistes. Manque de discipline._

> **_3. Un ratio plus réaliste._** _Je reconnais enfin que le téléphone avec lequel je travaille est très long (ratio 6/13). Je vais avoir besoin de mon imagination. La vue entière défile maintenant verticalement, avec les applications sur 2 colonnes. Un accident se produit ici : mon attention s'est maintenant déplacée vers le Centre de contrôle de l'iPhone (que j'examine probablement sur mon téléphone iOS 11, comme modèle pour le croquis). Je suis mal orienté et ajoute le petit chevron en haut, signifiant « balayez vers le bas pour fermer »._

![Image](https://cdn-media-1.freecodecamp.org/images/KFPEoJsGeyiPVN4Dyv4UAYIV8mMH5Cxz4hp5)
_Feuille 1 sur 2_

> **_4._ _Un conflit potentiel._** _Parce que j'assume maintenant à tort que l'interface peut être balayée vers le bas, je m'inquiète que cela va interférer avec mon défilement vertical. Je capture cela dans une note latérale : « KO puisque le balayage est nécessaire pour fermer le calque ». J'échange les choses, déplace les applications vers le haut, comme si cela pouvait aider, mais finis par planter la graine d'une idée alternative : « Applications récentes @ haut mais en carrousel horizontal »._

> **_5._ _Une dernière tentative avec le défilement vertical._** _Ici, je suppose que je cherche une confirmation que l'approche verticale est défectueuse... Mais mon esprit bifurque à nouveau alors que je remarque un nouveau problème ! Les contrôles et les applications récentes sont en compétition pour la visibilité : faites défiler pour voir l'un et l'autre est poussé hors des limites. Ils font partie de la même sangle. À ce moment-là, je décide d'essayer de les découpler._

![Image](https://cdn-media-1.freecodecamp.org/images/bEdIEtTi3RKTZgHoeJwAVRerrDO18vy1pGKE)
_Feuille 2 sur 2_

> **_6. Applications récentes en carrousel horizontal._** _Cela semble plus familier pour un sélecteur d'applications. Les contrôles défilent toujours verticalement, bien que — alors comment cela fonctionne-t-il dans l'ensemble ? Cela ne semble pas correct. Je semble à nouveau distrait entre 6 et 7 mais passons cela._

> **_7. Deux vues de défilement parallèles._** _Le groupe de contrôle et le carrousel d'applications sont maintenant libres de se déplacer sans se heurter. L'espace est partagé équitablement. J'annote certains éléments avec « Taille ? » : Puis-je me permettre cette disposition sur le véritable appareil ? Une seule façon de le savoir : augmenter la fidélité. Mais dans l'ensemble, je sens que j'ai une solution candidate avec laquelle je peux travailler._

### Observations

**Je ne précise pas mon objectif**. C'est dommage car quelque chose d'aussi simple que « Adapter le nouveau sélecteur d'iPad à l'iPhone 8 » (même si évident) m'aurait concentré plus tôt sur les véritables problèmes.

**Je n'ai pas une logique très claire en tête**. Preuve de confusion : l'idée fausse que l'interface est un calque qui peut être balayé vers le bas, et le bouton Home que je retire puis, pour une raison quelconque, fais revenir (ne demandez pas !).

**Je semble principalement préoccupé par un problème de disposition**. Apparemment, je ne m'inquiète pas beaucoup de la façon d'accéder à l'écran d'accueil. Pourtant, c'est très clé dans mon expérience ! Je laisse une trace timide à l'étape 3 : « Manque de moyen évident pour aller à l'écran d'accueil », puis place un bouton Home partout. C'est embarrassant (étant donné que l'expérience est tout à fait sans bouton !) — je suis probablement conscient qu'à un moment donné je dois trouver un espace vide pour que l'arrière-plan puisse être touché, comme sur le sélecteur d'iPad, mais je ne le jurerais pas. Le bouton Home ressemble davantage à une étiquette FIX-ME appliquée mécaniquement, quelque chose que je ne veux pas traiter pour l'instant.

> Être orienté processus signifie : [Longue liste qui inclut :] Travailler fluidement entre l'échelle du concept et l'échelle du détail pour voir comment chacun informe l'autre.

> Matthew Frederick

**Mon dessin et mon écriture sont affreux**. Mais d'une certaine manière, c'est positif. Dans le processus de réalisation de ces croquis, il ne m'est jamais venu à l'esprit que je les partagerais plus tard ; sur le moment, l'absence d'exigences esthétiques a effectivement renforcé la concentration.

**Les notes latérales aident à informer mes prochaines étapes**. Croquis, évaluation, notation des problèmes, et tentative de les résoudre dans une itération future. Tout changement peut apporter de nouveaux problèmes, et plus je les capture tôt, mieux c'est. Il est si facile de les repérer et de les oublier. Je prendrai des notes latérales de manière plus systématique à l'avenir.

### Prototypage

Vous pouvez essayer les prototypes ci-dessous si vous utilisez [Principle](http://principleformac.com/index.html), sur un Mac ou un iPhone directement. Cliquez sur les légendes des films pour télécharger les fichiers .prd de Principle. Pour en savoir plus, consultez [la documentation de Principle](http://principleformac.com/docs.html#running-on-device), et mes conseils à la fin de l'article.

![Image](https://cdn-media-1.freecodecamp.org/images/Iw0SnOEAmZH3CKrbMefFowTxKp9bYkcgUi8q)
_[Télécharger v8](https://www.dropbox.com/s/i8lsat5mq5w9x8i/homeless%20v8.prd?dl=1" rel="noopener" target="_blank" title=")_

Une version précoce (v8 ci-dessus) présente le chevron en haut et un discret bouton Home en bas. Appuyer sur le chevron rouvre l'application actuelle (que pourrait-il faire d'autre ?) mais un appui sur la miniature de l'application le fait déjà.

Ainsi, cette interaction basée sur le chevron semble stupide, avec le recul. Faites attention à l'animation qu'elle déclenche : bien qu'elle fasse la bonne chose (zoomer sur l'application correctement représente l'action de la ramener au premier plan), elle est déconnectée de l'objet chevron lui-même. Le chevron, d'une part, fait ce que vous voulez (fermer le sélecteur et revenir à l'application) mais d'autre part, il ne se comporte pas comme vous vous y attendez (glisser vers le bas). Le prototypage a instantanément piégé la contradiction ici. J'aurais dû attraper le défaut beaucoup plus tôt, mais c'est bon — il y a beaucoup de choses dans ma vie que j'aurais dû faire plus tôt.

![Image](https://cdn-media-1.freecodecamp.org/images/LH5LZRNSFe0foAcKRCUVBBjXcRzwIg8yo-r4)
_[Télécharger v11](https://www.dropbox.com/s/6dsveqoqusqam8g/homeless%20v11.prd?dl=1" rel="noopener" target="_blank" title=")_

Le chevron a disparu (v11 ci-dessus) mais j'expérimente maintenant avec une miniature de l'écran d'accueil (comme dans le sélecteur d'iOS 10). Cela est efficace pour le cas d'utilisation de l'écran d'accueil, mais cela pousse l'application précédente (verte) trop à gauche pour un droitier. Et il y a à nouveau une duplication : le bouton Home devient redondant, mais si je le retire, alors l'utilisateur ne peut compter que sur la miniature pour aller à l'écran d'accueil, ce qui est trop à droite pour les gauchers ! Ils pourraient faire défiler mais dans ce cas particulier, je ne veux certainement pas qu'ils aient à le faire.

Il y a un autre aspect : ce modèle est incohérent avec mon modèle cible, selon lequel seul un appui sur l'arrière-plan devrait vous ramener à l'accueil. Cela est clé pour la cohérence de l'ensemble, et central à la beauté du nouveau sélecteur iOS 11. Pourquoi ? Parce que **l'arrière-plan flou derrière le sélecteur _est_ l'écran d'accueil.** Toute affordance spécifique pour accéder à l'écran d'accueil (comme un bouton Home ou ma miniature) est superflue (pour ne pas dire incohérente) lorsque vous pouvez interagir avec l'écran d'accueil _directement_. La profondeur est l'un des principes de design fondamentaux dans iOS — avec la Clarté et la Déférence — et Apple s'appuie magnifiquement dessus ici.

![Image](https://cdn-media-1.freecodecamp.org/images/fKt156S1jrG3GdSdduTaIh-g9ECryaj-W0zy)
_Couches principales du modèle mental dans iOS 11_

![Image](https://cdn-media-1.freecodecamp.org/images/XGPDJ5m0tQYmMDZS9qFFbE9GP3h3q-j1pcJE)
_[Télécharger v14](https://www.dropbox.com/s/9p5zon3u8kfkjru/homeless%20v14.prd?dl=1" rel="noopener" target="_blank" title=")_

Dans la dernière itération v14 ci-dessus, je nettoie et aligne plus strictement avec le sélecteur d'iPad. C'est la version que je présente dans [la partie 1](https://medium.freecodecamp.org/homeless-iphone-20c154fabbf7). Une amélioration supplémentaire pourrait être d'agrandir la zone vide en bas, par exemple en limitant la grille du Centre de contrôle à 3 rangées.

Une dernière citation de l'excellent [101 Things I Learned in Architecture School](https://mitpress.mit.edu/books/101-things-i-learned-architecture-school) de Matthew Frederick :

> Prendre correctement le contrôle du processus de design tend à donner l'impression de *perdre* le contrôle du processus de design [...] Acceptez l'incertitude. Reconnaissez comme normal le sentiment de perte qui accompagne une grande partie du processus.

Au cours de mon voyage, je me suis éloigné de mon objectif initial à plusieurs reprises et j'ai entrevu par accident différentes possibilités. Certaines peuvent valoir la peine d'être revisitées plus tard, d'autres m'ont ouvert les yeux sur de nouveaux pièges. L'errance n'est pas une perte, c'est l'essence de l'exploration. En même temps, on ne peut pas continuer à ouvrir des boîtes et à ajouter des todos indéfiniment ; il est également important de livrer des solutions raisonnablement stables et présentables au fur et à mesure. Le défi est de trouver un équilibre entre largeur et profondeur.

#### **Conseils – si vous essayez les prototypes**

* Les interactions sont limitées à : balayer vers le haut, faire défiler horizontalement, appuyer sur la miniature de l'application bleue, appuyer sur l'arrière-plan du sélecteur. Dans l'écran d'accueil, appuyer uniquement sur l'icône bleue.
* L'état intermédiaire du Dock que je décris dans le précédent article n'est pas pris en charge par les prototypes que je partage ici. Afin de créer le film de l'état du Dock, j'ai apporté une modification temporaire.
* Les prototypes sont conçus pour l'« iPhone 8 » lui-même, à 375 * 812 points (145 pt plus grand qu'un iPhone 6/7). Donc, si votre appareil de test, comme le mien, est un modèle 6/7, Principle réduit légèrement l'interface pour qu'elle s'adapte à votre écran : tout semble un peu plus petit que cela ne devrait être. Et positionné un peu plus haut aussi, en raison de la zone inférieure sur le 6/7 (pas un tel menton sur l'écran bord à bord futur).
* Cependant, si vous [ouvrez cette image sur un 6/](https://www.dropbox.com/s/2cykf04u1vzpzc3/Simulated%20iPhone%208%20rendering%20%28view%20on%20a%204.7%20inch%29.png?dl=1)7, vous obtenez une bien meilleure idée de la sensation attendue de l'« iPhone 8 ». Imaginez simplement que le téléphone est plus grand et que vous pouvez appuyer n'importe où dans la zone inférieure. Vous devrez peut-être d'abord enregistrer l'image dans votre bibliothèque de photos. Elle est censée remplir tout l'écran et ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/iCC1SBV7SoerqKjrzZ7IF1BhaewkpYhW2636)