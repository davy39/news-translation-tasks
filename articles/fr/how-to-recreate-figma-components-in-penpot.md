---
title: Comment déplacer les composants Figma vers Penpot
subtitle: ''
author: Fatuma Abdullahi
co_authors: []
series: null
date: '2025-03-26T23:20:33.197Z'
originalURL: https://freecodecamp.org/news/how-to-recreate-figma-components-in-penpot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743028701920/ef200f8f-888d-4658-a5b0-ffa483edbdcf.png
tags:
- name: Design Systems
  slug: design-systems
- name: Open Source
  slug: opensource
- name: Penpot
  slug: penpot
- name: figma
  slug: figma
- name: components
  slug: components
seo_title: Comment déplacer les composants Figma vers Penpot
seo_desc: Penpot is an open-source design tool for creating complete design systems.
  It is free, self-hostable, and allows multiple projects. Penpot supports reusable
  components and assets and allows files and libraries to be shared across projects.
  Penpot fil...
---

[Penpot](https://penpot.app/) est un outil de conception open-source pour créer des systèmes de design complets. Il est gratuit, auto-hébergeable et permet plusieurs projets. Penpot prend en charge les composants et les actifs réutilisables et permet de partager des fichiers et des bibliothèques entre les projets. Les fichiers Penpot peuvent être exportés dans divers formats pour améliorer la collaboration.

Les conceptions Penpot se traduisent directement en code conforme aux normes web, facilitant la collaboration et la transmission entre les designers et les développeurs.

Ce tutoriel vous guidera à travers la recréation ou le déplacement de composants [Figma](https://www.figma.com/) existants vers Penpot. Il inclura une présentation de l'outil Penpot et de son utilisation, une brève comparaison des deux outils et des ressources importantes.

## Table des matières

* [Comment recréer des fichiers Figma existants dans Penpot](#heading-comment-recreer-des-fichiers-figma-existants-dans-penpot)
  
* [Comprendre l'interface utilisateur de Penpot](#heading-comprendre-linterface-utilisateur-de-penpot)
  
* [Comprendre les mises en page de Penpot](#heading-comprendre-les-mises-en-page-de-penpot)
  
* [Comment créer et utiliser des composants Penpot](#heading-comment-creer-et-utiliser-des-composants-penpot)
  
* [Comment créer des actifs réutilisables dans Penpot](#heading-comment-creer-des-actifs-reutilisables-dans-penpot)
  
* [Comment ajouter et utiliser des icônes dans Penpot](#heading-comment-ajouter-et-utiliser-des-icones-dans-penpot)
  
* [Figma vs Penpot - Mon expérience](#heading-figma-vs-penpot-mon-experience)
  
* [Ressources et notes](#heading-ressources-et-notes)
  

## Comment recréer des fichiers Figma existants dans Penpot

Il existe deux façons de déplacer ou de recréer des composants Codex existants de Figma vers Penpot : en utilisant l'outil de migration soutenu par la communauté ou en recréant manuellement les composants et les fichiers.

### Utilisation du plugin de migration soutenu par la communauté

Vous pouvez utiliser [ce plugin](https://www.figma.com/community/plugin/1219369440655168734/penpot-exporter) pour déplacer vos conceptions Figma vers Penpot. C'est une manière simple de migrer depuis Figma, surtout si vous avez de nombreux composants.

Pour ce faire, ajoutez-le en tant que plugin Figma et trouvez l'option dans le menu contextuel. Ensuite, cliquez sur l'option "Penpot Exporter" pour activer le plugin. Le plugin créera alors un fichier zip pour votre composant et le téléchargera.

![Une capture d'écran illustrant comment ajouter et utiliser le plugin "Penpot Exporter".](https://cdn.hashnode.com/res/hashnode/image/upload/v1742571496007/da97ad1b-6939-4bb9-9000-6c367a711797.gif align="center")

Dans Penpot, dans votre tableau de bord des projets, cliquez sur le menu contextuel des trois points et sélectionnez "Importer des fichiers Penpot" pour ouvrir une fenêtre de sélection de fichiers. Cliquez sur le fichier zip téléchargé depuis Figma, et Penpot créera un nouveau projet avec le même nom que le fichier zip. Ce nouveau projet contiendra votre composant Figma traduit dans l'environnement Penpot.

![Une illustration de la manière d'importer des fichiers dans Penpot](https://cdn.hashnode.com/res/hashnode/image/upload/v1742571779644/1ebeb54d-ce27-4987-b630-f101a60ee8d3.gif align="center")

En regardant le nouveau composant, vous remarquerez que le plugin de migration récupère correctement tous les composants enfants et les variables de typographie tout en gardant les choses assez organisées. Mais il ne récupère pas les variables de couleur.

### Recréation manuelle des composants Figma

Une autre façon de déplacer les composants Figma vers Penpot est de les recréer manuellement. Bien que cette option soit plus fastidieuse que la précédente, elle vous donne un contrôle précis sur l'apparence du composant, l'organisation des fichiers et la gestion des actifs.

C'est une excellente occasion de rafraîchir les composants existants, surtout s'il y en a peu. C'est aussi un bon exercice pour les nouveaux utilisateurs pour comprendre Penpot.

Pour déplacer efficacement les composants en utilisant cette méthode, vous devrez comprendre comment Penpot fonctionne. Les concepts suivants vous aideront à rendre ce processus plus efficace.

## Comprendre l'interface utilisateur de Penpot

L'interface utilisateur de Penpot est assez similaire à celle de Figma, sauf que Penpot utilise par défaut le mode sombre. Vous avez vos contrôles à droite et vos fichiers, actifs et calques à gauche, avec une toile au milieu.

![Alt: Capture d'écran d'une interface utilisateur Penpot avec un panneau de gauche étiqueté "Calques" montrant la structure du fichier, une toile centrale étiquetée "Toile", et un panneau de droite avec divers outils et paramètres de conception.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742811019699/ea5336e3-50a7-4771-bfa6-07a225390320.png align="center")

Les deux ont une barre d'outils qui vous permet d'interagir avec la toile. Les barres d'outils ont des icônes et des noms légèrement différents mais ont la même fonctionnalité. Notamment, dans Penpot, l'outil Frame est appelé Board.

Penpot prend en charge la plupart des fonctionnalités de Figma, à l'exception des Design Tokens, qui seront ajoutés bientôt.

## Comprendre les mises en page de Penpot

Penpot prend en charge les mises en page Flex et Grid. Ces mises en page vous permettent de positionner les éléments avec précision et simplifient la création de designs fluides. Pour ceux qui sont familiers avec CSS Grid et Flex, ils fonctionnent de la même manière.

La mise en page Flex vous permet d'organiser les éléments dans un conteneur parent, comme un tableau ou une forme englobante, sur une dimension, largeur ou hauteur. Elle vous permet de déterminer l'espacement et le positionnement des éléments enfants via des contrôles visuels avec des étiquettes sur le panneau latéral droit.

![Une illustration sur la manière d'utiliser la mise en page Flex de Penpot](https://cdn.hashnode.com/res/hashnode/image/upload/v1742571904634/c8bf8fc0-79a7-415f-916b-42da7c881ed8.gif align="center")

Les mises en page Grid permettent les mêmes contrôles que les mises en page Flex mais avec la flexibilité supplémentaire de faire s'étendre un élément enfant sur les deux dimensions simultanément. Cela rend les mises en page Grid très utiles pour créer des designs complexes et nuancés.

## Comment créer et utiliser des composants Penpot

Créer un composant dans Penpot est relativement simple. Vous sélectionnez les éléments qui composeront le composant, puis faites un clic droit et cliquez sur "Créer un composant", transformant votre sélection en un composant.

Votre nouveau composant sera disponible sous l'onglet "Actifs" du panneau latéral gauche. Pour l'utiliser, faites-le glisser sur la toile.

Vous pouvez également créer des copies du composant. Par défaut, les copies sont liées au composant principal, et toute modification du principal sera reflétée dans toutes les copies. Vous pouvez annuler cela en détachant les copies du menu contextuel.

![Un speedrun de la manière de créer un composant Penpot](https://cdn.hashnode.com/res/hashnode/image/upload/v1742571991986/6dd4820b-0f3a-4d41-895d-cb9f5e7d4f52.gif align="center")

## Comment créer des actifs réutilisables dans Penpot

Penpot a trois types d'actifs : Typographie, Couleurs et Composants, avec les [jetons de design Penpot](https://penpot.app/collaboration/design-tokens) arrivant très bientôt. La typographie fait référence aux informations sur les types et les poids de police qui composent les styles de texte. Les couleurs vous permettent de créer et de trier vos couleurs répétées. Les composants font référence aux pièces de design réutilisables et, dans ce contexte, incluent des éléments graphiques comme les icônes et les images.

Pour créer un actif de couleur ou de typographie, cliquez sur l'onglet "Actifs" et sur l'icône plus de l'élément d'accordéon pertinent. Pour la couleur, cela ouvrira un sélecteur de couleur. Collez la valeur hexadécimale à l'endroit approprié, puis enregistrez-la. La couleur apparaîtra dans le menu déroulant de l'accordéon. Vous pouvez cliquer dessus pour lui donner un nom sémantique si vous le souhaitez.

![Capture d'écran d'une interface utilisateur Penpot montrant une palette de couleurs avec des codes hexadécimaux, un sélecteur de couleur et des actifs de bibliothèque locale.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742809861347/9ae3b0fb-798b-4363-ab90-873c18a16793.png align="center")

Pour la typographie, cliquez sur l'icône plus de l'accordéon pertinent. Cela ouvrira un panneau où vous pourrez spécifier la police, le poids de la police, l'espacement des lettres et la hauteur de ligne. Vous pouvez également changer le nom de l'actif après l'avoir enregistré.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1742810318737/daf0e24f-7c4a-4c00-bb73-ccca7575bcf5.png align="center")

## Comment ajouter et utiliser des icônes dans Penpot

Vous pouvez ajouter des packs et des bibliothèques d'icônes dans Penpot depuis le tableau de bord du projet. En bas de la page, une bannière contenant une liste de bibliothèques couramment utilisées est affichée. Ces bibliothèques incluent généralement quelques packs d'icônes. Vous pouvez faire défiler pour en choisir un ou cliquer sur l'option explorer plus à la fin du curseur pour ouvrir la page dédiée aux modèles Penpot.

![Capture d'écran de l'interface utilisateur de Penpot montrant en bas "Penpot - Design System v2.0", "New Project 1", "Avataaars", "UX Notes", "Whiteboarding Kit", "Open Color Scheme", et "Flex Layout Playground". Une barre latérale étiquetée "Libraries & Templates" est visible à droite.](https://cdn.hashnode.com/res/hashnode/image/upload/v1742810534992/83b2eb72-4877-49b3-9d2e-02c37e0cb894.png align="center")

Si vous trouvez une bibliothèque pertinente dans la bannière du bas, cliquez sur l'icône de téléchargement. Penpot vous demandera d'ajouter la bibliothèque sélectionnée. Une fois que vous l'acceptez, elle sera ajoutée à l'élément de menu "Bibliothèques" du panneau latéral gauche.

Si vous cliquez sur la page dédiée aux modèles, cliquer sur l'icône de téléchargement téléchargera un fichier Penpot. Vous pouvez ensuite le faire glisser vers la page des projets, et il sera également disponible dans la section "Bibliothèques" de la page des projets.

Pour utiliser les bibliothèques dans votre fichier de projet, cliquez sur l'onglet "Actifs" du panneau latéral gauche, puis cliquez sur le bouton "Bibliothèques" en dessous. Cela ouvrira une modale avec toutes vos bibliothèques listées sous "Bibliothèques partagées".

Cliquez sur l'icône plus de celles que vous souhaitez utiliser dans votre projet. Cela liera cette bibliothèque à votre projet et elle sera disponible dans le panneau latéral gauche. Vous pouvez ensuite rechercher une icône particulière depuis la barre de recherche et la faire glisser sur la toile.

![Un gif illustrant comment lier et délier des bibliothèques dans l'interface utilisateur de Penpot](https://cdn.hashnode.com/res/hashnode/image/upload/v1742571300138/3dbbc937-f727-4c03-987b-43ddb71b1608.gif align="center")

Pour supprimer une bibliothèque de votre projet, cliquez sur le bouton des bibliothèques. Dans la modale, sous "bibliothèques dans ce fichier", toutes les bibliothèques utilisées sont listées. Cliquez sur l'icône de lien à côté de la bibliothèque que vous souhaitez supprimer. Cela la déliera et la supprimera du panneau latéral.

## Figma vs Penpot – Mon expérience

En tant que premier utilisateur de Penpot et utilisateur occasionnel de longue date de Figma, j'ai remarqué quelques différences et rencontré quelques problèmes de démarrage.

### Remplacement des icônes

Vous pouvez [remplacer des composants](https://help.penpot.app/user-guide/components/#component-swap) dans Penpot ! C'est dommage que je l'aie découvert après avoir terminé ma première migration de composants.

### Renommage des fichiers et dossiers

J'ai eu du mal à trouver comment renommer les fichiers et dossiers dans Penpot. Je cherchais sans cesse le raccourci ou un élément de menu dans le menu contextuel. Il s'avère que vous devez double-cliquer sur le titre pour le changer. Vous pouvez renommer les fichiers de la même manière dans Figma, mais je ne l'ai jamais fait comme ça.

### Adhérence aux normes web

J'ai été agréablement surpris par la qualité du code que Penpot fournit, ainsi que vos conceptions. Il répond aux [normes w3c](https://www.w3.org/standards/), mais le HTML pourrait être plus [sémantique](https://web.dev/learn/html/semantic-html).

### Système de design Penpot

Penpot met à disposition son [système de design](https://community.penpot.app/t/pencil-the-penpot-design-system/7152) ainsi que de nombreuses petites bibliothèques qui vous aident à comprendre comment l'outil fonctionne. C'est très bien car cela vous permet de bien comprendre le langage de design et comment organiser les systèmes de design.

### Options de forme limitées dans la barre d'outils

La barre d'outils de Penpot manque de formes essentielles telles que le stylo, la flèche et le triangle. Bien que vous puissiez recréer cela avec l'outil de chemin ou utiliser une bibliothèque pour les importer, c'est définitivement quelque chose qui me manquait et qui était facilement disponible dans Figma.

Il m'a fallu quelques essais pour me familiariser avec Penpot et, au final, j'ai vraiment aimé. De plus, sa nature open-source le rend encore plus attachant.

## Ressources et notes

L'utilisation de Penpot a une courbe d'apprentissage, même si vous êtes familier avec d'autres outils de conception comme Figma. Ces ressources peuvent vous aider à vous mettre à niveau plus rapidement et à être plus efficace avec Penpot.

* [Vidéo Penpot sur les mises en page](https://www.youtube.com/live/64O8qi51Jqc?si=A6AVp1m8se3gl1ut)
  
* [Penpot en direct sur les jetons de design](https://www.youtube.com/live/aW0LNHLEI_Y?si=HATAWee8tH29Sgrq&t=1604)
  
* [Documentation Penpot](https://help.penpot.app/user-guide/)
  
* [Plugin de migration Penpot](https://www.figma.com/community/plugin/1219369440655168734/penpot-exporter)
  
* [Modèles et bibliothèques Penpot](https://penpot.app/libraries-templates)
  
* [Systèmes de design Penpot](https://penpot.app/blog/penpot-for-design-systems-101/)