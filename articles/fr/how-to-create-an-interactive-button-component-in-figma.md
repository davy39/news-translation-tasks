---
title: Comment créer un composant de bouton interactif dans Figma
subtitle: ''
author: Faith Olohijere
co_authors: []
series: null
date: '2024-03-06T18:44:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-interactive-button-component-in-figma
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pexels-jess-bailey-designs-810079.jpg
tags:
- name: figma
  slug: figma
- name: Web Design
  slug: web-design
seo_title: Comment créer un composant de bouton interactif dans Figma
seo_desc: 'Designers are always searching for tools that help ease their workflow
  and create innovative solutions for their users. This ranges from components, style
  guides, and design systems, to plugins and extensions.

  In this article, we''re going to look at ...'
---

Les designers recherchent toujours des outils qui facilitent leur flux de travail et créent des solutions innovantes pour leurs utilisateurs. Cela va des composants, des guides de style et des systèmes de conception, aux plugins et extensions.

Dans cet article, nous allons examiner les composants comme des fonctionnalités qui peuvent aider à améliorer votre efficacité en tant que designer. Je vais vous montrer comment créer un composant de bouton interactif en utilisant Figma.

## Table des matières

1. [Prérequis](#prerequisites)
2. [Qu'est-ce que les composants ?](#heading-quest-ce-que-les-composants)
   - [Composants de bouton](#heading-composants-de-bouton)
3. [Comment créer un composant de bouton interactif dans Figma](#heading-comment-creer-un-composant-de-bouton-interactif-dans-figma)
   - [Construire le composant de bouton](#heading-construire-le-composant-de-bouton)
   - [Comment créer des variantes](#heading-comment-creer-des-variantes)
   - [Comment créer des états de survol et actifs](#heading-comment-creer-des-etats-de-survol-et-actifs)
   - [Comment créer d'autres états de bouton](#heading-comment-creer-dautres-etats-de-bouton)
   - [Comment regrouper les boutons par états](#heading-comment-regrouper-les-boutons-par-etats)
   - [Comment rendre les composants de bouton interactifs](#heading-comment-rendre-les-composants-de-bouton-interactifs)
4. [Conclusion](#heading-conclusion)

## Prérequis :

Pour tirer le meilleur parti de cet article, il sera utile d'avoir des connaissances de base sur l'utilisation de Figma et de ses fonctionnalités. Mais notez que cela n'est pas nécessaire, car j'ai écrit cet article pour tout le monde, indépendamment de leur niveau de connaissance individuel.

Cet article s'adresse à tous ceux qui s'intéressent à l'apprentissage des composants, des éléments réutilisables, de Figma et du design en général.

## Qu'est-ce que les composants ?

Les composants sont des éléments de design réutilisables que vous pouvez utiliser plusieurs fois dans un projet ou à travers différents projets.

> Les composants sont des blocs de construction interactifs pour créer une interface utilisateur. Ils peuvent être organisés en catégories basées sur leur objectif : Action, contenu, communication, navigation, sélection et saisie de texte. – Material Design 3

Les composants peuvent aller d'éléments simples comme des boutons ou des icônes à des structures plus complexes comme des barres de navigation ou des modules UI entiers. Ils aident à maintenir la cohérence et l'uniformité dans un design, ils sont évolutifs et très utiles pour la collaboration.

### Composants de bouton

Les boutons, parfois appelés CTAs, sont des éléments qui permettent à un utilisateur d'effectuer une action spécifique comme s'inscrire, acheter un produit, s'abonner à une newsletter, etc. Ils existent en différents formats et tailles, et sont des éléments très importants dans le design.

Les composants de bouton consistent généralement en des attributs visuels tels que la forme, la taille, la couleur et la typographie pour transmettre leur fonctionnalité et encourager l'interaction de l'utilisateur. Ils peuvent varier en style et en apparence en fonction du système de design, des directives de la marque ou du contexte de leur utilisation dans une application ou un site web.

## Comment créer un composant de bouton interactif dans Figma

Ensuite, nous allons créer un composant de bouton interactif dans Figma. Ce composant de bouton contiendra des boutons avec uniquement du texte, des boutons avec des icônes de chaque côté du texte, et des boutons avec uniquement des icônes.

Le composant de bouton contiendra différents états de bouton (par défaut, survol et actif), et sera interactif.

Cela est très utile lorsque vous concevez des interfaces avec différents cas d'utilisation. Par exemple, vous pourriez vouloir un bouton dans votre design qui contienne du texte et une icône accompagnatrice, pour un écran particulier. Dans un autre écran, vous pourriez vouloir utiliser un bouton avec uniquement une icône. Si vous avez déjà créé ces différents composants, vous gagnerez beaucoup de temps.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-30.png)
_Différents types de boutons (icône uniquement, icône et texte, texte uniquement). Image de [Telerik](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.telerik.com%2Fdesign-system%2Fdocs%2Fcomponents%2Fbutton%2F&psig=AOvVaw2RdR4WQVKTp_y542hJlwaB&ust=1709772173745000&source=images&cd=vfe&opi=89978449&ved=0CBYQ3YkBahcKEwjQnoXps96EAxUAAAAAHQAAAAAQBA)_

Commençons !

### Construire le composant de bouton

Ouvrez un nouveau fichier Figma. Si vous n'avez pas de compte Figma, allez-y et créez-en un sur [figma.com](https://www.freecodecamp.org/news/p/3c725afb-cd49-490c-b122-0115d9b1780a/figma.com).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-1.png)
_Ouverture d'un nouveau fichier Figma_

Ensuite, cliquez sur l'icône de texte dans le panneau de gauche et tapez _Bouton_.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-2.png)
_Taper "bouton" dans la barre de recherche._

Ensuite, ajoutez un auto-layout (Shift + A).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-3.png)
_Ajout d'un auto-layout_

Faites en sorte que le rembourrage horizontal du bouton soit de 36 px et le rembourrage vertical de 12 px.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-4.png)
_Ajout de rembourrage horizontal et vertical_

Donnez également au bouton un rayon de bordure de 8 px.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-5.png)
_Ajout d'un rayon de bordure._

Ajoutez un remplissage au bouton.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-6.png)
_Aller à la section "remplissage"._

Je vais choisir le code couleur #1C199, qui est une nuance de bleu.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Button-7.png)
_Choisir un code couleur._

Ensuite, je vais rendre le texte un peu plus gras. Pour cela, cliquez sur le texte et allez à la section de police dans le panneau de droite.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-8.png)
_Aller à la section de police._

Je vais donner au bouton une taille de police de 16 px et rendre le poids "moyen".

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-10.png)
_Changer la taille de la police à 16 px_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-11.png)
_Changer le poids de la police à moyen._

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-9.png)
_Montrer le texte édité_

Ensuite, j'ajouterai une icône de mon choix au cadre du bouton. Cela me permettra de créer facilement un composant de bouton avec des icônes, et pas seulement du texte lorsque le moment sera venu.

Pour ajouter une icône, j'utiliserai un plugin Figma appelé _Iconify_, qui est l'une des plus grandes collections d'icônes dans Figma. Pour cela, faites un clic droit sur votre canevas et un menu apparaîtra. Allez à l'onglet _Plugins_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-12.png)
_Ouvrir les plugins_

Une liste des plugins récents que vous avez utilisés apparaîtra. Vous verrez également tous les plugins _Enregistrés_ que vous avez. Le premier plugin de ma liste est Iconify (c'est parce que je l'utilise beaucoup, lol). Maintenant, je vais simplement cliquer sur Iconify et rechercher l'icône particulière que je veux utiliser.

Si vous n'avez jamais utilisé de plugin auparavant, et qu'il n'y a donc aucun plugin dans votre liste, vous pouvez utiliser la section des ressources pour rechercher le plugin de votre choix et l'enregistrer dans votre liste.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-65.png)
_Aller à la section des ressources_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-64.png)
_Rechercher des plugins_

Je veux utiliser l'icône de _flèche avant_, donc je vais simplement rechercher cela en utilisant le champ de recherche sur le plugin.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-13.png)
_Rechercher l'icône de flèche avant._

Beaucoup d'icônes de flèche avant de différentes collections apparaîtront, donc je vais simplement choisir une en particulier qui fonctionne le mieux pour moi, dans ce cas, une icône de flèche avant de _IonIcons_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-14.png)
_Sélectionner une icône de flèche avant particulière_

Je vais sélectionner l'icône et cliquer sur le bouton _Importer l'icône_ pour qu'elle apparaisse dans mon fichier Figma.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-15.png)
_Importer l'icône dans votre fichier_

Ensuite, nous allons réduire la taille de l'icône à la hauteur et à la largeur que nous voulons. Elle est actuellement à 48 x 48 et je veux qu'elle soit à 24 x 24.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-16.png)
_Taille de l'icône actuellement 48x48_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-17.png)
_Changer la taille de l'icône à 24x24_

Nous allons également changer la couleur de l'icône pour qu'elle corresponde à la couleur du texte (blanc). Pour cela, assurez-vous que l'icône est sélectionnée, puis faites défiler vers le bas jusqu'à _Couleurs de sélection_ pour entrer le code couleur, qui dans ce cas est #FFFFFF.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-18.png)
_Changer la couleur de l'icône en blanc (#FFFFFF)_

Ensuite, nous allons ajouter l'icône à l'intérieur du cadre du bouton. Pour cela, il suffit de faire glisser votre icône à l'intérieur du cadre.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-19.png)
_Faire glisser l'icône de flèche dans le cadre du bouton_

Vous remarquerez que la taille du cadre augmente pour accueillir l'icône ajoutée.

Ensuite, dupliquez l'icône et déplacez-la de l'autre côté du texte. Dupliquer l'icône nous aidera à créer facilement des composants de bouton avec des icônes de chaque côté du texte plus tard.

Pour cela, utilisez simplement Ctrl + D, et déplacez l'icône dupliquée de l'autre côté.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-20.png)
_Utiliser Ctrl + D pour dupliquer une icône_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-21.png)
_Déplacer l'icône dupliquée de l'autre côté du cadre._

Ensuite, je vais masquer les deux icônes car je veux créer mon premier composant de bouton (bouton avec texte uniquement). Je vais renommer le cadre en Bouton.

Pour masquer les deux icônes, allez dans le panneau des calques à gauche et cliquez sur l'icône de l'œil à côté des éléments que vous voulez masquer.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-22.png)
_Aller au panneau des calques pour masquer les icônes_

Vous remarquerez que le cadre se redimensionne automatiquement une fois que les deux icônes sont masquées.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-23.png)
_Cadre de bouton avec les icônes masquées_

Je vais ensuite renommer le cadre en _Bouton_. Pour cela, double-cliquez sur l'en-tête du cadre et renommez.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-24.png)
_Double-cliquer sur le cadre_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-25.png)
_Cadre de bouton renommé_

### Comment créer des variantes

Ensuite, nous allons faire du cadre du bouton une variante.

Les variantes vous aident à créer plusieurs versions ou états d'un composant. Elles sont très utiles lors de la conception d'interfaces qui ont différents états ou variations, comme des boutons de différentes tailles ou designs, comme nous en créons ici.

Pour faire du cadre du bouton une variante, double-cliquez sur l'icône du composant en haut de votre écran.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-26.png)
_Aller à l'icône du composant en haut de l'écran et double-cliquer_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-27.png)
_Variante du composant de bouton_

Ensuite, j'ajouterai une autre variante car je veux avoir trois états pour le bouton (Par défaut, Survol et Actif). Pour ajouter une autre variante, cliquez sur l'icône plus sur l'une des variantes déjà existantes.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-28.png)
_Cliquer sur l'icône plus sur une variante pour ajouter une autre variante_

Automatiquement, une nouvelle variante sera ajoutée.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-29.png)
_Ajout d'une troisième variante_

Ensuite, j'augmenterai la taille du cadre du composant pour qu'il puisse accueillir d'autres variantes qui seront ajoutées. Pour cela, sélectionnez simplement le composant entier et faites glisser pour obtenir la taille souhaitée.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-30.png)
_Sélectionner le cadre du composant_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-31.png)
_Augmenter la largeur du cadre du composant._

### Comment créer des états de survol et actifs

Ensuite, je vais ajuster les deux derniers boutons (états de survol et actifs), afin que la différence entre les trois états de bouton soit évidente. Pour cela, je vais rendre l'état de survol plus clair et l'état actif plus foncé.

Pour l'état de survol, je vais changer le code couleur en #392AE7, qui est une nuance plus claire de bleu. Assurez-vous que le bouton particulier est sélectionné pour que les changements prennent effet :

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-32.png)
_Changer le code couleur pour l'état de survol_

Pour l'état actif, je vais changer le code couleur en #19107A qui est une nuance légèrement plus foncée de bleu.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-33.png)
_Changer le code couleur de l'état actif_

### Comment créer d'autres états de bouton

Ensuite, nous voulons créer d'autres états de bouton (boutons avec des icônes de chaque côté du texte, et avec des icônes uniquement).

Pour commencer, je vais dupliquer les trois boutons. Pour cela, sélectionnez les trois boutons et dupliquez-les en utilisant Ctrl + D.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-34.png)
_Dupliquer les trois boutons_

Ensuite, nous voulons créer des composants de bouton avec du texte et une icône à gauche. Pour cela, cliquez sur l'œil des icônes de gauche sur chacune des icônes pour les révéler.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-35.png)
_Révéler les icônes du côté gauche des boutons_

Ensuite, nous voulons créer des composants de bouton avec du texte et une icône à droite.

Pour cela, dupliquez à nouveau les boutons et faites de même pour les icônes de droite.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-36.png)
_Dupliquer les boutons une deuxième fois_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-37.png)
_Révéler les icônes du côté droit_

Enfin, nous voulons créer des composants de bouton avec des icônes uniquement.

Pour cela, nous allons dupliquer les boutons une dernière fois pour masquer le texte.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-38.png)
_Dupliquer les boutons une troisième fois_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-39.png)
_Masquer le texte_

Je vais rendre les cadres _icône uniquement_ de forme carrée. Pour cela, sélectionnez les trois cadres et faites glisser pour redimensionner.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-40.png)
_Sélectionner les cadres 'icônes uniquement'_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-41.png)
_Redimensionner les cadres_

Je vais maintenant redimensionner le cadre du composant pour qu'il s'adapte à son contenu.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-42.png)
_Redimensionner le cadre du composant._

Ensuite, nous allons renommer les différents états de bouton pour qu'il soit facile de les identifier. Tout d'abord, sélectionnez le cadre du composant entier. Ensuite, allez dans la section intitulée _Propriétés_ et changez _Propriété 1_ en _Bouton_ pour montrer que ceci est un composant de bouton.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-43.png)
_Aller à la section des propriétés_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-44.png)
_Renommer le cadre du composant_

Ensuite, nous allons renommer les cadres de bouton par icônes. Sélectionnez les trois premiers cadres horizontalement et allez dans la section _Variante actuelle_. Renommez-les _Pas d'icônes_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-46.png)
_Sélectionner les trois premiers boutons et les renommer_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-47.png)
_Boutons sans icônes renommés_

Nous allons faire de même pour les trois boutons suivants et les nommer _Icônes à gauche_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-48.png)
_Boutons avec icônes à gauche renommés_

Nous allons faire la même chose pour le prochain ensemble, en les renommant _Icônes à droite_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-49.png)
_Boutons avec icônes à droite renommés_

Enfin, pour le dernier ensemble, nous allons renommer les boutons _Icônes uniquement_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-50.png)
_Boutons avec icônes uniquement renommés_

### Comment regrouper les boutons par états

Ensuite, nous allons regrouper les boutons par états et les nommer. Nous allons commencer par le premier état : _Par défaut_. Sélectionnez tous les cadres de bouton sous défaut et allez dans la section _Variante actuelle_ dans le panneau de droite. Cliquez sur l'icône de configuration pour éditer la configuration du composant.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-51.png)
_Cliquer sur l'icône de configuration_

Cliquez sur la boîte de description pour ajouter une description. Dans ce cas, je vais simplement taper _État par défaut_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-55.png)
_Ajouter une description_

Faites de même pour les deux autres états – survol et actif.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-53.png)
_Ajouter une description pour l'état de survol_

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-54.png)
_Ajouter une description pour l'état actif_

### Comment rendre les composants de bouton interactifs

Pour commencer, basculez vers l'onglet Prototype, situé en haut de votre écran, dans le panneau de droite.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-56.png)
_Passer en mode prototype_

Ensuite, ajoutez une interaction du premier au deuxième cadre de bouton _sans icône_. Pour cela, cliquez sur le premier cadre de bouton et faites glisser l'icône plus vers le deuxième cadre.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-57.png)
_Ajouter une interaction_

Cela fera apparaître une liste d'options et de paramètres d'interaction pour l'animation.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-58.png)
_Faire apparaître les paramètres d'interaction_

Changez _Au clic_ en _Lors du survol_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-60.png)
_Changer le type d'interaction en "lors du survol"_

Faites de même pour le cadre de bouton suivant, mais au lieu de _Lors du survol_, changez en _Lors de la pression_.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-61.png)
_Animer le troisième cadre de bouton_

Maintenant, répétez les mêmes étapes pour les autres ensembles.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Button-62.png)
_Répéter les étapes d'animation pour les autres ensembles de boutons._

Voilà, vous venez de créer un composant de bouton interactif.

## Conclusion

Les composants aident à améliorer vos designs et à les rendre plus efficaces. Ils vous aident également à gagner du temps et améliorent la cohérence de vos designs. Mais ils ne peuvent aider que s'ils sont créés de la bonne manière.

Pratiquer souvent vous aidera à améliorer votre capacité à créer des composants réutilisables utiles. N'oubliez pas, prenez chaque décision en gardant vos utilisateurs à l'esprit.