---
title: Comment utiliser un système de design – une étude de cas
subtitle: ''
author: Faith Olohijere
co_authors: []
series: null
date: '2023-10-17T14:37:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-a-design-system
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/pexels-toa-heftiba-s-inca-1194420.jpg
tags:
- name: Design Systems
  slug: design-systems
- name: Web Design
  slug: web-design
seo_title: Comment utiliser un système de design – une étude de cas
seo_desc: 'You may have heard of, studied, or used a design system at some point in
  your coding career. But what role do design systems actually play in our projects?
  Why should we even bother to create or use them?

  In this guide, you''ll be learning what design...'
---

Vous avez peut-être entendu parler, étudié ou utilisé un système de design à un moment donné de votre carrière de codeur. Mais quel rôle jouent réellement les systèmes de design dans nos projets ? Pourquoi devrions-nous même nous donner la peine de les créer ou de les utiliser ?

Dans ce guide, vous apprendrez ce que sont les systèmes de design, pourquoi ils sont importants, les éléments typiques d'un système de design, et un exemple pratique de la manière d'implémenter un système de design en tant que designer. Plongeons-nous dans le sujet !

## Qu'est-ce qu'un système de design ?

Les systèmes de design sont des collections structurées de composants et d'éléments de design réutilisables. Nous les utilisons pour créer une expérience utilisateur cohérente et homogène sur une gamme de produits ou de services.

Un système de design est comme un ensemble de blocs de construction et de règles pour créer des produits numériques comme des sites web et des applications. Les systèmes de design sont composés d'éléments clés comme la typographie, la palette de couleurs, les icônes, l'espacement et la mise en page, et ainsi de suite.

### Importance et objectif d'un système de design

Les systèmes de design sont importants pour de nombreuses raisons.

#### Efficacité

Les systèmes de design vous aident à devenir plus efficace. Parce que c'est une collection de composants réutilisables, cela économise le temps de production de nouveaux éléments, et aide les designers à produire rapidement de nouvelles fonctionnalités dans les projets. Cela sert également de booster de productivité.

#### Collaboration

Une équipe essayant de construire un produit peut être composée de designers, de développeurs, de chefs de produit, et d'autres. Le système de design aide tous les membres de l'équipe à se référer aux directives de la marque, peu importe ce sur quoi ils travaillent. Cela aide également à s'assurer que tout le monde, y compris les parties prenantes, est impliqué dans le processus de design, et facilite la collaboration.

#### Cohérence

Les systèmes de design assurent la cohérence de l'interface utilisateur et de l'expérience utilisateur sur divers produits et plateformes.

Nous ne voudrions pas d'un scénario où le design d'un bouton est incohérent sur différents écrans, n'est-ce pas ? C'est là que le système de design intervient. Il aide nos actifs et éléments de design à rester cohérents, et peut toujours servir de point de référence.

#### Évolutivité

L'évolutivité ici fait référence à la capacité du système de design à croître et à s'adapter aux besoins changeants d'un projet ou d'une organisation.

Un élément crucial de tout système de design est l'évolutivité. Les systèmes de design aident dans les situations où le projet pourrait avoir besoin de s'étendre pour accommoder différents appareils et plateformes ou lorsque l'équipe s'agrandit ou lorsque l'on essaie d'accommoder de nouvelles tendances et pratiques.

### Comment fonctionnent les systèmes de design

Pour comprendre comment fonctionne un système de design, vous devez simplement connaître les types d'actifs ou de composants qui constituent le système et leurs rôles.

Un système de design typique comprend les parties suivantes :

#### Couleurs

Lorsque vous ouvrez un système de design, l'une des premières choses que vous verrez est une section de palette de couleurs. C'est l'un des éléments les plus courants dans un système de design.

Les systèmes de design définissent un ensemble de couleurs primaires et secondaires, ainsi que leurs diverses utilisations. Cela inclut les couleurs de fond, les couleurs de texte, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-46.png)
_Section de palette de couleurs du système de design Rayna UI_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-47.png)
_Section de palette de couleurs du système de design Atlassian_

#### Typographie

Un autre élément typique d'un système de design est la typographie. Chaque système de design inclut généralement des directives pour la typographie, spécifiant les polices, les tailles de police, la hauteur de ligne, et ainsi de suite.

Il peut également définir comment la typographie est utilisée pour différents types de contenu comme les titres et le texte de corps, en s'assurant qu'ils sont accessibles et lisibles pour une utilisation en design.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-48.png)
_Section de typographie du Material Design de Google_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-49.png)
_Section de typographie du Polaris de Shopify_

#### Icônes

Les icônes sont très importantes lorsque l'on essaie de donner des indices visuels à vos utilisateurs. Les systèmes de design fournissent un ensemble d'icônes standard et des directives pour leur utilisation, en s'assurant qu'elles sont reconnaissables et cohérentes.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-50.png)
_Section d'iconographie du système de design Atlassian_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-57.png)
_Section d'iconographie du Material Design de Google_

#### Grilles et styles d'espacement

Un système de grille aide à établir une structure cohérente pour différents composants ou pages.

Les systèmes de design fournissent des directives d'espacement spécifiant les marges, le remplissage, et d'autres règles liées à la mise en page pour maintenir l'alignement afin de créer un design visuellement agréable et organisé.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-51.png)
_Section des grilles et styles d'espacement du système de design Rayna UI_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-53.png)
_Section d'espacement du système de design Atassian_

#### Documentation

Tout système de design bien structuré possède une forme de documentation qui explique généralement comment utiliser les éléments et les directives de manière efficace. La documentation aide également les designers et les développeurs à comprendre comment utiliser et implémenter le système de design.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-54.png)
_Documentation pour les styles de boutons dans le système de design Rayna UI_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-58.png)
_Documentation pour les icônes d'applications sur les directives d'interface humaine d'Apple_

#### Modèles et composants d'interface utilisateur

Les modèles et composants d'interface utilisateur sont les blocs de construction d'une interface utilisateur. Les systèmes de design définissent des modèles et composants d'interface utilisateur tels que des boutons, des formulaires, des modales, des accordéons, des barres de navigation, et ainsi de suite, ainsi que des directives sur la manière et le moment de les utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-59.png)
_Section des composants d'interface utilisateur du Polaris de Shopify_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-60.png)
_Section des modèles d'interface utilisateur des directives d'interface humaine d'Apple_

#### Directives de contenu

Celles-ci couvrent la manière dont le texte et les images sont utilisés dans l'interface utilisateur. Elles peuvent spécifier le ton, l'utilisation des images, et la hiérarchie du contenu, en s'assurant que le contenu est cohérent et aligné avec les directives de la marque.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-61.png)
_Section des directives de contenu du Polaris de Shopify_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-62.png)
_Section des directives de contenu du Material Design de Google_

#### Directives d'accessibilité

La plupart des systèmes de design contiennent des directives d'accessibilité afin d'augmenter l'utilisabilité des produits pour les personnes de toutes capacités. Ces directives garantissent que le design est inclusif et conforme aux normes d'accessibilité comme les WCAG (Web Content Accessibility Guidelines). Cela inclut le contraste des couleurs, la navigation au clavier et d'autres fonctionnalités d'accessibilité.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-55.png)
_Directives d'accessibilité du Material Design de Google_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-56.png)
_Directives d'accessibilité du système de design Atlassian_

#### Exemples et cas d'utilisation

La plupart des systèmes de design contiennent également des exemples et des cas d'utilisation du système de design en action pour aider les designers et les développeurs à comprendre comment l'implémenter efficacement.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-52.png)
_Cas d'utilisation du tableau de bord Fintech du système de design Rayna UI_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-63.png)
_Application du cas d'utilisation de la typographie du Material Design de Google_

## Différences entre un système de design et un guide de style

Les guides de style et les systèmes de design sont très similaires et peuvent souvent être confondus, mais ils sont différents.

Quelques différences entre les systèmes de design et les guides de style sont :

### Portée

Les guides de style sont relativement limités en portée et peuvent ne pas inclure de composants d'interface utilisateur détaillés ou des interactions.

Les systèmes de design, en revanche, sont plus complets et englobent une gamme plus large d'éléments, y compris des composants interactifs, des directives d'interface utilisateur, parmi d'autres.

#### Cohérence

Les guides de style se concentrent généralement sur la cohérence de la marque, aidant à maintenir un look et une sensation uniformes sur divers matériaux et plateformes.

Les systèmes de design visent à établir à la fois la cohérence de la marque et de l'interface utilisateur, en fournissant des composants réutilisables et des modèles d'interaction.

#### Évolution et évolutivité

Les guides de style tendent à évoluer plus lentement et peuvent ne pas être aussi évolutifs que les systèmes de design. Les systèmes de design sont plus adaptables et évoluent avec le produit ou le service.

#### Collaboration

Les guides de style sont principalement utilisés par les designers pour assurer la cohérence visuelle d'une marque. Ils jouent un rôle limité dans la facilitation de la collaboration entre designers et développeurs.

Les systèmes de design, en revanche, favorisent la collaboration en fournissant un langage commun et des ressources partagées entre designers et développeurs.

### Exemples concrets de systèmes de design

De nombreuses entreprises logicielles ont créé leurs propres systèmes de design pour faciliter le travail de leurs designers et rendre l'expérience de construction de produits plus fluide.

Google, par exemple, dispose d'un système de design qu'ils utilisent pour leurs produits – vous pouvez voir des styles et des éléments similaires dans la plupart de leurs produits.

La plupart de ces systèmes de design sont gratuits et disponibles pour le public. Voici quelques exemples de systèmes de design concrets :

* [Google Material Design](https://m3.material.io/) par Google
* [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) par Apple
* [Atlassian Design System](https://atlassian.design/) par Atlassian
* [Polaris](https://polaris.shopify.com/) par Shopify
* [Carbon Design System](https://carbondesignsystem.com/) par IBM

## Comment utiliser un système de design pour vos designs – Exemple du système de design Rayna UI

Pour cet article, nous utiliserons le système de design Rayna UI pour illustrer comment utiliser un système de design pour vos designs.

C'est un système de design plus récent que j'ai récemment découvert, alors j'ai pensé partager mon expérience en l'utilisant pour un défi.

### Étape 1 – Télécharger le système de design

La première étape sera de télécharger le système de design que vous essayez d'utiliser. Dans ce cas, nous téléchargerons le système de design Rayna UI. Allez sur leur page d'accueil @[Rayna UI](https://www.raynaui.com/) et récupérez-le depuis là-bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-1.png)
_Page d'accueil de Rayna UI_

Ensuite, cliquez sur "Get Rayna UI" pour télécharger le système de design.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-2.png)
_Page d'accueil de Rayna UI_

Ensuite, tapez votre email afin de recevoir le système de design à votre adresse email.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/rayna-3.png)
_Fournir votre adresse email_

Le lien vers le fichier Figma sera partagé à votre email, et vous pourrez l'ouvrir.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-4.png)
_Vérification de votre email_

Faites défiler vers le bas dans l'email pour trouver le lien permettant de visualiser le fichier Figma de Rayna UI.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-5.png)
_Vérification de votre email_

Cliquez sur le lien envoyé à votre email pour ouvrir le système de design. Le lien ouvrira le système de design Rayna UI sur la communauté Figma.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-1.1.png)
_Ouverture du fichier Rayna UI dans la communauté Figma_

Ensuite, cliquez sur le bouton "Open in Figma" du côté droit de votre écran. Cela ouvrira un fichier Figma contenant tous les actifs et composants du système de design Rayna UI.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-6.png)
_Ouverture du fichier Rayna UI dans Figma_

### Étape 2 – Publier le système de design Rayna UI dans vos bibliothèques.

L'étape suivante consiste à publier le système de design Rayna UI dans vos bibliothèques, afin de pouvoir l'utiliser pour n'importe quel design.

La troisième page du fichier Figma (Get Started) contient un guide pour commencer avec le système de design. Ce guide inclut des ressources pour les débutants afin que vous puissiez acquérir une solide compréhension des bases, ainsi que les étapes à suivre pour publier et activer la bibliothèque dans d'autres projets.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-7.png)
_Commencer avec le système de design Rayna UI_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-8.png)
_Exploration de la section de démarrage_

Suivez les étapes données dans le guide pour publier la bibliothèque. Tout d'abord, allez dans le panneau des actifs dans la zone en haut à gauche de votre écran, et appuyez sur l'icône de livre.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-9.png)
_Cliquer sur le panneau "Assets"_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-10.png)
_Cliquer sur l'icône "book"_

Lorsque vous cliquez sur l'icône de livre, une modale s'ouvrira pour que vous puissiez publier la bibliothèque.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-1.2.png)
_Publication de la bibliothèque_

Cliquez sur le bouton de publication à côté du fichier dans la modale.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-12.png)
_Déplacement de la bibliothèque vers une équipe professionnelle_

On m'a demandé de déplacer la bibliothèque vers une équipe professionnelle, afin que je puisse la publier là-bas. Cliquez sur le bouton "Move to team" pour déplacer le fichier.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-14.png)
_Sélection d'une équipe._

Ensuite, sélectionnez le fichier d'équipe auquel vous souhaitez publier la bibliothèque.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-15.png)
_Sélection d'une équipe_

Après avoir sélectionné une équipe, vous devrez publier le système de design dans les fichiers de l'équipe.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-16.png)
_Publication du système de design_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-17.png)
_Publication du système de design_

Vous recevrez une notification indiquant que votre bibliothèque a été publiée.

## Comment utiliser le système de design dans vos projets

Ensuite, nous allons apprendre comment implémenter le système de design dans un design. Je vais concevoir un écran d'inscription pour un site web fintech pour illustrer cela.

Avant de commencer votre design, vous pouvez copier certaines icônes dont vous pourriez avoir besoin depuis le système de design vers votre fichier de design. J'ai tendance à copier les styles de boutons et de champs de saisie dont j'aurai besoin, si je veux adhérer strictement au système de design.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-24-1.png)
_Éléments copiés depuis la page du système de design._

Pour la page d'inscription que je vais concevoir, les détails dont j'ai besoin sont le nom du site web, les champs de saisie (nom complet, nom de famille, adresse email, mot de passe, confirmer le mot de passe), et les boutons ou CTA (s'inscrire et s'inscrire avec Google).

## Comment concevoir un écran web d'inscription

### Étape 1 – Sélectionner un cadre

Tout d'abord, j'ouvrirai le cadre que je vais utiliser. Pour ce design, j'utiliserai le cadre de bureau (1440 x 1024).

Pour ouvrir un cadre, allez dans le panneau d'outils dans le coin supérieur gauche de votre écran. Un panneau avec différents types et tailles de cadres apparaîtra.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-25-1.png)
_Panneau d'outils-Cadre_

Ouvrez la section Bureau et choisissez "Desktop" (1440 x 1024). Le cadre apparaîtra sur votre écran, et vous pourrez commencer à concevoir.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-26.1.png)
_Choix d'un cadre_

### Étape 2 – Ajouter des styles de grille

J'aime utiliser des grilles pour l'arrangement et la cohérence dans mes designs, donc j'ajouterai une mise en page de grille au cadre.

Dans le système de design Rayna UI, il existe déjà des styles de grille, donc je peux simplement en choisir un. Pour ajouter un style de grille, allez dans le panneau de droite, et cliquez sur le menu à 4 blocs dans la section _layout grid_.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-26-1.png)
_Panneau de style de grille_

Une liste de différents styles de grille du système de design apparaîtra, et vous pourrez choisir celui qui correspond au type d'écran que vous concevez.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-27-1.png)
_Choix d'un style de grille_

Puisque je conçois avec un cadre de bureau, je choisirai _Large_.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-28-1.png)
_Choix d'un style de grille pour un cadre_

Vous pouvez détacher l'instance pour voir les spécifications du style de grille que vous avez choisi. Pour détacher l'instance, cliquez sur l'icône de détachement à côté de l'icône de l'œil dans la section de la grille de mise en page.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-29-1.png)
_Détachement du style_

Vous pouvez maintenant voir les spécifications du style de grille que vous avez choisi. Puisque j'ai choisi _Large_, les spécifications de la grille sont :

* Compte – 12, utilisant des colonnes
* Couleur – F4BBAE, avec une opacité réglée à 20%
* Type – Stretch
* Largeur – Auto
* Marge – 112
* Gouttière – 32

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-30.png)
_Spécifications du style de grille_

### Étape 3 – Ajouter du contenu

Je vais commencer à ajouter du contenu à l'écran. J'utiliserai un texte pour représenter mon logo – Ketusha.

Vous pouvez également contrôler les styles et les tailles de texte dans le système de design. Pour ce faire, allez dans le panneau Texte du côté gauche de votre écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-31.png)
_Édition de la taille du texte_

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-32.png)
_Confirmation de la taille du texte_

En suivant le même format, j'ai tapé un titre pour le formulaire appelé "Sign Up".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-33.png)
_Titre du formulaire d'inscription_

Plus tôt, j'ai suggéré que vous copiiez les icônes, les boutons et les exemples de champs de saisie depuis le fichier du système de design, afin de pouvoir les utiliser facilement pendant la conception. Maintenant, je vais coller l'exemple de champ de saisie que j'ai copié dans mon cadre.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-35.png)
_Collage de l'exemple de champ de saisie dans le cadre_

Puisque je veux que le champ de saisie soit plus long, je vais l'allonger légèrement à 400 de largeur. Il était précédemment à 375 de largeur.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-36.png)
_Allongement de la largeur du champ de saisie_

Ensuite, je vais structurer le champ de saisie pour qu'il ressemble à ce que je veux – sans icônes.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-37.png)
_Champ de saisie sans icônes_

Ensuite, je vais modifier l'étiquette pour l'étiquette que je veux pour mon design.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-38.png)
_Édition de l'étiquette_

Ensuite, je vais simplement dupliquer le champ de saisie jusqu'à ce que je sois satisfait, et aussi modifier toutes les étiquettes.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-39.png)
_Ajout d'autres champs de saisie_

Ensuite, je vais ajouter les boutons à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-40.png)
_Ajout des CTA_

Je vais ajouter le bouton "Sign up with Google", afin que l'utilisateur ait différentes options pour s'inscrire sur la plateforme.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-41.png)
_Ajout d'autres options d'inscription_

Ensuite, je vais essayer de coller l'icône Google à l'intérieur du cadre "Sign up with Google", mais cela pourrait ne pas être possible.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-42.png)
_Collage de l'icône Google_

Pour pouvoir coller et remplacer un élément à l'intérieur de la sélection, je vais devoir détacher l'instance. Pour ce faire, faites un clic droit sur l'élément que vous essayez de remplacer. Une liste d'options apparaîtra. Cliquez sur "detach instance".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-43.png)
_Détacher l'instance_

Après cela, faites un clic droit sur l'icône à nouveau, et "paste to replace".

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-44.png)
_Coller pour remplacer_

L'icône sera remplacée instantanément.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/Rayna-45.png)
_Formulaire d'inscription web_

Nous venons de créer une page d'inscription en utilisant le système de design Rayna UI !

Gardez à l'esprit que l'utilisation d'un système de design ne signifie pas que vous ne pouvez pas être créatif et ajouter votre propre touche. Vous pouvez ajouter votre propre style et créativité autant que vous le souhaitez au fur et à mesure.

## Conclusion

L'utilisation des systèmes de design est une compétence nécessaire que chaque designer et développeur devrait cultiver.

Les systèmes de design sont un composant critique du design et du développement de produits modernes, favorisant la collaboration, l'efficacité et l'innovation.

Merci d'avoir lu !