---
title: Exploiter la puissance de React dans le prototypage de design
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T05:32:49.000Z'
originalURL: https://freecodecamp.org/news/harnessing-the-power-of-react-in-design-prototyping-4a74e70db5f5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vXbwcj_3ZK_oVij0DIFQtg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Exploiter la puissance de React dans le prototypage de design
seo_desc: 'By Linton Ye

  An interview with Jack Hallahan, a designer who uses React


  In today’s sea of design prototyping tools, React might be an unintuitive choice.

  The process of creating a prototype is supposed to be fast and visual. After all,
  the purpose o...'
---

Par Linton Ye

#### Une interview avec Jack Hallahan, un designer qui utilise React

![Image](https://cdn-media-1.freecodecamp.org/images/08Oq80eS4XQHZdq4MrbXpuqFtpHhsDzjNzFb)

Dans l'océan actuel d'outils de prototypage de design, React pourrait sembler un choix peu intuitif.

Le processus de création d'un prototype est censé être rapide et visuel. Après tout, le but de créer des prototypes est de passer le moins de temps possible à tester différentes options de design avant de prendre une décision. Conventionnellement, le codage (et donc React) est considéré comme lent et difficile en tant qu'outil de prototypage.

Jack Hallahan est un designer produit basé à Londres, au Royaume-Uni. Il fait partie des designers qui savent comment exploiter la puissance du code pour rationaliser leurs processus de design.

Intrigué par le post inspirant de Jack sur [Medium](https://medium.com/geckoboard-under-the-hood/react-js-for-design-prototyping-ec29cfa81b0f), je lui ai envoyé un e-mail pour en savoir plus. Jack a été assez gentil pour discuter avec moi, ce que je ne peux pas attendre de partager avec vous !

Voici ce dont nous avons parlé :

* Comment Jack a-t-il appris React en tant que designer ? Quels ont été ses plus grands défis ?
* Quand est-ce le bon moment pour utiliser React pour le prototypage de design ?
* Pourquoi React est-il le bon outil ? Comment se compare-t-il aux outils de prototypage visuel ?
* Quels outils liés à React utilise-t-il dans son processus de design ?
* Les suggestions de Jack aux designers sur la façon d'apprendre React

Intéressé par l'histoire d'un designer ? Continuez à lire ! Mes questions sont en *italique*. Les réponses de Jack suivent en texte normal.

### Sur l'utilisation de React comme outil de prototypage de design

#### Trouver le bon outil de prototypage

**_Linton :_** _Comment utilisez-vous React dans votre flux de travail ? Quelle est l'histoire derrière l'utilisation de React comme outil de prototypage ?_

**Jack :** Quelque chose avec lequel nous avons eu du mal pendant un certain temps dans notre entreprise est de trouver le bon outil de prototypage pour le type de travail que nous faisons.

De nombreuses expériences utilisateur sont plus ou moins un parcours utilisateur linéaire. Un exemple est un flux d'intégration, un processus de paiement ou un enregistrement de compte. Il peut y avoir de petites décisions en cours de route, mais elles peuvent être gérées en prototypant pour un « chemin heureux » puis en considérant les cas limites. Nous pouvons utiliser des outils comme Marvel pour le rendre assez fidèle et le tester avec les utilisateurs.

Cependant, ce dont j'avais besoin pour prototyper n'était pas un parcours utilisateur linéaire.

#### Prototypage d'un parcours utilisateur non linéaire

Notre produit est un outil métier qui permet aux clients d'obtenir leurs données de leur entreprise, par exemple les données de performance de leur équipe de vente. Il crée ensuite un tableau de bord visuel à afficher sur le téléviseur au bureau afin que tout le monde puisse voir les données en permanence.

Les gens l'utilisent pour concevoir des visualisations de données et des tableaux de bord. Il y a beaucoup d'options qu'un utilisateur pourrait avoir à parcourir pour obtenir les données dont il a besoin et les configurer de la bonne manière pour être visualisées. Il doit également gérer les données. Les données viennent sous différentes formes et tailles. Si nous concevons une nouvelle visualisation de données, elle doit être suffisamment robuste pour gérer différents types de données, différents schémas, différents nombres allant d'un chiffre à six chiffres.

**Configurer une visualisation de données est un exemple de chemin non linéaire.** Il y a de nombreuses options, toutes pouvant être choisies dans différentes combinaisons. Chaque combinaison aboutira à une visualisation différente. Voir l'aperçu du graphique changer est une confirmation visuelle que les décisions de l'utilisateur ont l'effet souhaité. Parce que le résultat est très visuel, une fidélité inférieure n'aurait pas permis de valider aussi complètement.

Il n'y avait pas vraiment d'outil qui nous permettait de prototyper **un parcours utilisateur complet**. J'ai également essayé de prototyper cela avec Axure RP par le passé, qui permet une certaine logique conditionnelle, mais cela est rapidement devenu ingérable.

J'ai mis de côté d'autres outils et j'ai investi mon temps dans la construction de quelque chose en React, et cela a vraiment porté ses fruits.

Pour moi, l'avantage de React est qu'il comble une lacune que nous avions dans notre boîte à outils de prototypage. **Cette lacune concernait les interfaces qui permettent de configurer quelque chose de manière non linéaire, et les interfaces qui gèrent les données**.

#### Exemples de prototypes

_Pouvez-vous nous donner des exemples de parcours utilisateur non linéaires ?_

Le premier prototype a été utilisé pour tester la conception de l'interaction avec les utilisateurs, ainsi que pour valider les options disponibles pour les utilisateurs : pouvaient-ils créer un thème qui correspondait à leur marque ?

Configurer un thème n'était pas un parcours linéaire. Il devait être assez visuel. Il est de haute fidélité car il introduisait de nouveaux modèles d'interaction dont nous devions être sûrs. Parce que le résultat est très visuel, une fidélité inférieure n'aurait pas permis de valider aussi complètement.

![Image](https://cdn-media-1.freecodecamp.org/images/BXVH-kAeHZ60dBkFoPlyklzSBFRZKEQzuw-E)

Un autre exemple est ce prototype de widget de tableau. Il est de haute fidélité uniquement dans la visualisation du tableau. Le formulaire à gauche est plus ou moins non stylisé. En fait, le tableau est très similaire au balisage et au style utilisés pour créer la même chose dans notre code de production. Le prototype a été créé pour déterminer ces détails — alignement, espacement, états de survol, tailles de police, troncature, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/Cf0pV3GmhGMaKzCSt2Co2gws1HwWuMETr95g)

#### Pourquoi React est-il le bon outil ?

**Gérer plusieurs chemins et manipuler les données sont les forces naturelles du code.**

Parce que React est JavaScript, si vous voulez apporter des modifications à la manière dont les données sont affichées, comme arrondir ou trier, vous pouvez le faire. Vous ne pouvez pas faire cela avec des outils visuels simples.

[Avec les outils visuels] Si vous voulez créer un prototype pour tester l'expérience de faire quelque chose comme trier le tableau, vous devez créer quelques écrans qui ressemblent au flux utilisateur et espérer que l'utilisateur va cliquer sur le bon bouton. Si ce n'est pas le cas, vous devrez dire, oops, désolé, nous n'avons pas conçu cette partie, revenons simplement au bon chemin.

En comparaison, React me permet de créer des prototypes plus robustes pour manipuler les données avec un parcours utilisateur complet. L'utilisateur pourrait explorer différentes options, plutôt que de simplement suivre un parcours où l'utilisateur doit cliquer sur le bon bouton à chaque fois.

L'une de ces choses est l'idée qu'un composant a un état. L'application connaît l'état actuel dans lequel elle se trouve, et vous pouvez faire quelque chose à l'interface pour mettre à jour l'état. Et cet état peut être transmis aux enfants. Vous pouvez mettre à jour un composant ici en cliquant sur quelque chose là-bas très facilement. Et ensuite vous pouvez revenir en arrière et annuler cela sans affecter les choses en aval.

**Prototypes de haute fidélité par défaut**

La fidélité est quelque chose que vous obtenez par défaut lorsque vous prototypage avec du code. Bien sûr, votre bouton peut ne pas être stylisé jusqu'à ce que vous ajoutiez du CSS, mais même un élément de bouton non stylisé ressemble et fonctionne comme un bouton dans le navigateur. Il semble réel et fonctionne comme prévu car il est réel. Vous obtenez des choses comme cursor: pointer, les états de survol et actifs, la capacité à surligner et copier du texte, de vrais éléments de formulaire comme des champs dans lesquels vous pouvez taper et des boutons radio que vous pouvez basculer, le tout sans avoir à les dessiner ou à les styliser de quelque manière que ce soit.

En fin de compte, nous avions quelque chose qui était proche d'une expérience finale. Nous avions toute la logique pour gérer quelqu'un changeant la couleur ou téléchargeant un logo. Et l'interface était capable d'être dans n'importe quel état à n'importe quel moment sans être cassée. Je pouvais donc le tester avec des utilisateurs sans m'inquiéter d'aller dans un état cassé et d'essayer de m'en remettre.

#### Comparaison avec les outils de prototypage visuel

_Utilisez-vous d'autres outils de prototypage ? Quand les utilisez-vous ?_

Oui, je crée des croquis statiques de faible fidélité avant de passer à React. Typiquement, je dessinerais sur papier et je ferais aussi quelques images rapides dans Sketch, peut-être même en utilisant un outil comme Marvel pour les assembler. Je peux explorer plus d'idées et apporter des modifications plus rapidement dans ces outils — ils sont meilleurs pour le design « divergent », et React est meilleur pour le design « convergent » — ne plus explorer mais plutôt décider, valider et itérer.

_Pouvez-vous commenter la vitesse de création de prototypes dans React par rapport aux outils de prototypage visuel ?_

React a une courbe d'apprentissage assez raide, mais une fois que vous avez compris, cela peut être surprenant. Cependant, c'est simplement excessif pour beaucoup de prototypes et je ne le recommanderais pas pour des choses que d'autres outils peuvent bien faire. Je trouve cela agréable de passer un après-midi à coder et à considérer la fidélité et la « robustesse » des prototypes comme ceux ci-dessus. Je pense que c'est assez rapide !

#### Flux de travail

_Comment se passe la transmission aux développeurs après l'approbation des prototypes que vous créez ?_

Nous n'avons pas de concept de transmission ici. Notre flux de travail est agile avec le design et le développement étroitement couplés. Nos ingénieurs sont habitués à traiter des concepts de design dans de nombreux formats différents, parfois des maquettes statiques, des prototypes détaillés, ou simplement des croquis. Cela dépend vraiment du travail. Nous décomposons le design en planification pour découvrir tout ce qui nécessite une exploration supplémentaire, et nous « pairons » souvent ensemble pour implémenter un design.

_Les développeurs utilisent-ils directement vos composants, ou écrivent-ils le code à partir de zéro, ou quelque chose entre les deux ?_

Non, aucun de mon code n'est utilisé dans notre application de production. Lorsque je construis un prototype, je n'ai pas besoin de me soucier de la maintenabilité, de la réutilisabilité ou de la scalabilité. Le code est mauvais, essentiellement, mais il fait le travail dont j'ai besoin. Notre application frontend est complexe avec Redux, des tests, des API de composants, etc. Cela ne vaut pas la peine d'essayer d'utiliser mon code pour ce travail.

#### Outils liés à React

_Quels outils liés à React utilisez-vous dans votre processus de design ?_

[**create-react-app**](https://github.com/facebook/create-react-app)

![Image](https://cdn-media-1.freecodecamp.org/images/yTsTuWbCFXr8VMloSZj02o-w5HkvWYWxRD5y)

Le premier outil qui m'a aidé à démarrer avec React est create-react-app de Facebook. L'application de démarrage boilerplate qui est prête à l'emploi, pré-configurée, et dispose de nombreuses fonctionnalités intégrées.

Avant cela, il était difficile de trouver un bon projet de modèle sur Github pour commencer. Je ne savais pas ce qui était bon, ce dont j'avais besoin, et ce dont je n'avais pas besoin. Des choses comme Webpack étaient un mystère complet pour moi, et le sont encore. Donc create-react-app était si facile. Il avait beaucoup de grandes choses intégrées et il n'a fait que s'améliorer avec le temps.

L'autre chose qui accompagne create-react-app est un moyen rapide de partager sur GitHub pages. Puisque tout est hébergé gratuitement, je peux très facilement obtenir une URL, l'envoyer à mes collègues, et ils peuvent y accéder ou l'envoyer à des utilisateurs qui pourraient être de l'autre côté du monde.

À part cela, j'ai installé des choses comme Lint et un prettier dans mon éditeur de code qui aident simplement à garder les choses propres et faciles à parcourir pour les erreurs, et l'outil d'extension Chrome React.

[**Tachyons**](http://tachyons.io/) **pour le style**

![Image](https://cdn-media-1.freecodecamp.org/images/lnPIMFd-L3UXldLwnSgdo-3qLh3XFOi3Fb0c)

Tachyons est une approche différente du CSS de ce à quoi la plupart des gens sont habitués. Il a été appelé CSS fonctionnel ou CSS atomique. En gros, c'est une bibliothèque de classes qui ont un but très spécifique comme appliquer un seul style.

Cela crée cette mentalité de design-au-fur-et-à-mesure. Vous écrivez plus ou moins des styles en ligne — en disant « Je veux que la police soit grande, et les coins arrondis. Je veux qu'il ait une ombre et que le fond soit vert. » Vous n'avez pas à aller lui donner un nom sémantique et ensuite aller écrire un tas de styles qui correspondent à cet élément. Si vous êtes à l'aise avec le fonctionnement du CSS, cela réduit simplement la quantité de jonglage que vous devez faire pour styliser quelque chose.

[**React Storybook**](https://github.com/storybooks/storybook)

![Image](https://cdn-media-1.freecodecamp.org/images/cSJ7nmA6QbfSPL7yqbiNUfexSKi3v-1DuhEH)

Nous utilisons React Storybook comme bibliothèque de composants. C'est une ressource partagée entre le design et le développement. Nous continuons à l'améliorer, mais je peux déjà voir comment Storybook peut être un excellent pont pour les designers et les développeurs frontend travaillant sur une application React.

Pour le moment, lorsque nous avons conçu un composant que nous voulons réutiliser, il sera ajouté à Storybook par un ingénieur. Nous pouvons ensuite nous référer à Storybook lors de la conception de nouvelles interfaces. Nous pouvons vérifier quels composants nous avons prêts à l'emploi, lesquels pourraient avoir besoin d'être modifiés, et découvrir si nous devons concevoir et construire quelque chose de nouveau.

À l'avenir, il serait formidable d'avoir Storybook comme source de vérité pour les designers et l'équipe frontend. Nous pourrions utiliser React-Sketchapp pour avoir une version de chaque composant qui peut être utilisée par les designers dans Sketch. Je n'ai pas encore eu l'occasion d'essayer correctement React-Sketchapp. L'équipe de design d'Airbnb fait un travail incroyable, mais nous ne sommes pas encore à l'échelle où cela devient crucial.

### Sur l'apprentissage de React en tant que designer

_Comment avez-vous appris React ? Aviez-vous une expérience préalable en programmation ?_

Je travaille dans le design numérique depuis un certain temps. Je suis évidemment devenu assez familier avec le HTML et le CSS. Je construis des sites web et des choses basiques depuis longtemps. JavaScript est quelque chose avec lequel j'ai souvent flirté, mais je n'avais jamais vraiment sauté dans le grand bain. J'ai utilisé un peu de jQuery, mais pour la plupart, c'était un mystère.

Nous avons un jour d'innovation toutes les deux semaines. Toute personne dans l'équipe produit et ingénierie peut utiliser ce temps pour travailler sur un projet personnel qui n'est pas le travail habituel de projet. C'est donc une excellente opportunité pour monter en niveau et élargir mes compétences.

J'ai commencé par faire quelques tutoriels JavaScript via Codecademy pour comprendre les bases. Et la raison pour laquelle j'ai regardé React était plus par curiosité que autre chose. Les ingénieurs l'utilisaient. J'avais appris quelques concepts de base, comme les composants et l'état. J'ai cherché quelques tutoriels et j'ai travaillé sur quelques petits projets, en suivant des articles de blog pour les instructions. Finalement, j'ai commencé à comprendre comment cela fonctionnait.

Une fois que j'avais compris ces concepts très basiques, j'ai essayé de les utiliser pour construire des projets réels. Cela m'a conduit à en apprendre davantage et à devenir un peu plus confiant avec cela.

_Quels ont été les plus grands défis lorsque vous appreniez React et comment les avez-vous surmontés ?_

L'écosystème React est notoirement complexe. Il peut être difficile pour un débutant de créer un espace sûr pour expérimenter sans lutter constamment avec les outils de construction. J'ai passé des âges à essayer de trouver le bon projet de démarrage, mais je ne savais pas vraiment ce que je cherchais. Un collègue m'a dirigé vers create-react-app lorsqu'il gagnait en traction, et à partir de ce moment-là, je m'en suis remis pour tous mes projets React.

Je pense que la plupart des gens trébucheront sur JSX de temps en temps, je le fais encore si je passe de React à html pour différents projets. Je n'ai pas trouvé de trucs ici — vous devez simplement mémoriser les différences, mais heureusement, il n'y en a pas trop.

Il m'a fallu un certain temps pour construire le bon modèle mental sur le fonctionnement de React et comment il s'assemble. Et le fait que j'étais presque un débutant complet avec JavaScript n'a pas aidé. C'était comme si de petits morceaux devenaient clairs, mais qu'il y avait encore trop de lacunes pour voir le tableau d'ensemble. Je me souviens avoir lutté pendant longtemps pour faire en sorte qu'un composant enfant mette à jour l'état de son parent.

Même maintenant, je me considérerais toujours comme un débutant — je devrais googler même des choses basiques. Mais je suis meilleur pour savoir quoi googler pour trouver les réponses, et comment la nouvelle connaissance s'intégrera avec les choses que je connais mieux.

_Lorsque l'on apprend une nouvelle technologie, une étape importante est de savoir quoi googler et quelles questions poser. À partir de ce moment-là, l'apprentissage tend à devenir auto-renforçant. Tout ce que vous apprenez dans le processus construira votre nouvelle fondation pour apprendre le prochain concept. Mais pour en arriver là, vous devrez apprendre suffisamment des bases pour vous débrouiller._

_C'est un peu comme apprendre une nouvelle langue (humaine), vous devrez connaître l'alphabet et construire suffisamment de vocabulaire. Ensuite, vous pouvez commencer à chercher des mots dans un dictionnaire, lire et parler avec des gens à partir desquels vous apprendrez de nouveaux mots et de nouvelles expressions._

_L'effort initial peut sembler fastidieux mais c'est une nécessité. La bonne nouvelle est que vous saurez quand vous y serez, comme Jack l'a fait. Vous aider à surmonter les obstacles initiaux est également mon objectif principal lors de la création du cours React pour les designers sur [learnreact.design](https://learnreact.design/?utm_source=medium&utm_campaign=jack-interview&utm_content=middle)._

_Avez-vous des suggestions pour les designers sur l'apprentissage de React ou l'apprentissage du code en général ?_

Vous pouvez lire autant de tutoriels que vous voulez. Vous pouvez suivre un cours ou regarder une vidéo, mais à moins d'essayer de construire quelque chose par vous-même, vous ne allez pas vraiment assembler les morceaux dans votre esprit. Donc cela a commencé à faire sens pour moi lorsque j'ai commencé à construire des choses qui allaient au-delà des tutoriels.

Prenez ce que vous avez fait dans un tutoriel ou un cours, ajoutez-y quelque chose. Ou pensez à quelque chose qui pourrait avoir des similitudes avec ce que vous venez d'apprendre. Si l'exemple était un profil de produit sur un site de commerce électronique, alors vous pouvez essayer de créer un profil utilisateur sur un réseau social. Vous pouvez le faire en React et réfléchir aux types de choses qui devraient aller dans cette interface. Commencez simplement à partir de zéro et construisez-le vous-même. Et c'est là que vous réalisez ce que vous savez et ce que vous ne savez pas.

À mesure que vous vous améliorez, à mesure que vous apprenez plus, vous apprendrez également à résoudre les problèmes que vous allez rencontrer plus facilement.

Donc lorsque vous commencez, vous verrez des erreurs de console et vous n'avez aucune idée de ce qu'elles signifient ou comment les corriger, c'est très effrayant et vous avez besoin de quelqu'un pour vous tenir la main. Mais à un moment donné, vous arrêtez d'avoir peur d'une erreur et vous pensez, « OK, je ne sais pas ce que c'est maintenant, mais je sais quoi googler pour comprendre comment le corriger ». Ou, « Je sais à peu près où cela se produit dans l'application, donc je vais essayer de le déboguer ».

Vous apprenez à corriger vos erreurs et si vous voulez faire quelque chose de nouveau, vous apprenez le chemin que vous pourriez prendre pour y parvenir. J'ai lutté au début. Mais en construisant des choses réelles, je suis arrivé à ce point où j'étais plus capable d'être autonome pour résoudre mes propres problèmes et apprendre la prochaine chose.

### Note finale (de moi, pas de Jack)

Je suis vraiment impressionné et inspiré par la détermination de Jack à explorer et utiliser tous les outils à sa disposition pour résoudre les problèmes de design qui se présentent. Avec cette mentalité, il n'a pas eu peur d'entrer dans de nouveaux territoires et d'adopter de nouveaux outils en cours de route.

Personnellement, je pense que chaque designer devrait avoir cette attitude envers les nouvelles technologies. Peu importe si c'est React, la blockchain ou les interfaces basées sur la voix. Nous devrions être ouverts à expérimenter avec elles et être prêts à les intégrer dans notre processus de design.

Qu'en pensez-vous ? Faites-le moi savoir dans les commentaires !

_Je tiens à remercier Jack pour le temps qu'il a passé à discuter avec moi, et pour avoir fourni des réponses de haute qualité à mes innombrables questions de suivi (afin que je puisse simplement copier et coller ?) !_

N'oubliez pas de consulter mon cours React spécialement conçu pour les designers : [learnreact.design](https://learnreact.design/?utm_source=medium&utm_campaign=jack-interview&utm_content=bottom). ?