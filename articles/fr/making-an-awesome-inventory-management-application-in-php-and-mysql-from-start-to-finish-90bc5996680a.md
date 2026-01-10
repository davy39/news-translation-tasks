---
title: Comment créer une application de gestion de stock géniale en PHP et MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T02:35:39.000Z'
originalURL: https://freecodecamp.org/news/making-an-awesome-inventory-management-application-in-php-and-mysql-from-start-to-finish-90bc5996680a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D8DAUz3T2nustjr2Pnn6QQ.jpeg
tags:
- name: business
  slug: business
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer une application de gestion de stock géniale en PHP et MySQL
seo_desc: 'By Richard

  You do not need bloated enterprise software to effectively track your inventory.
  This tutorial will help you develop your own custom inventory tracking application
  so you can make smart inventory decisions based on timely and accurate inve...'
---

Par Richard

Vous n'avez pas besoin de logiciels d'entreprise encombrants pour suivre efficacement votre inventaire. Ce tutoriel vous aidera à développer votre propre application de suivi d'inventaire personnalisée afin que vous puissiez prendre des décisions intelligentes en matière d'inventaire basées sur des données d'inventaire opportunes et précises.

### Configuration requise du système

Notre système d'inventaire nécessite la licence standard commerciale phpGrid et phpChart. Il nécessite quelques fonctionnalités avancées des deux composants.

* PHP 5.6+ (**PHP 7.x est maintenant fortement recommandé !**)
* MySQL / MariaDB
* phpGrid Lite (sous-grille) -ou- phpGrid Enterprise (Maître détail, Groupement)
* phpChart (pour les rapports)

### Qu'est-ce qu'un système de gestion de stock

Un système de gestion de stock comporte plusieurs composants critiques. À sa base, le contrôle des stocks fonctionne en suivant les deux fonctions principales d'un entrepôt : la réception (entrante) et l'expédition (sortante). D'autres activités telles que le mouvement ou la relocalisation des stocks ont également lieu. Les matières premières sont décrémentées et les produits finis sont incrémentés.

* Expéditions entrantes
* Commandes sortantes
* Inventaire
* Fournisseurs
* [Scanneur de code-barres](https://medium.com/@chensformers/inventory-management-system-with-barcode-scanner-in-php-a-definitive-guide-d18fdc165511) (Nouveau 1/2019 !)

### Conception de la base de données du système d'inventaire

Typiquement, un système d'inventaire a quatre éléments de base : les produits, les achats, les commandes et les fournisseurs. Chaque élément doit être suivi en fonction de son emplacement, de son SKU et de sa quantité. L'inventaire actuel, ou les produits en stock, est mis à jour en suivant les expéditions entrantes et les commandes sortantes. Des alertes de commande peuvent être définies pour se déclencher lorsque les niveaux de stock tombent en dessous des niveaux minimaux définis par l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/ZH5FJWHyUxVNeNFNMqOKPwde7lqBS5Lwvtkp)

### Configuration de la base de données Inventory Manager

Téléchargez le script SQL `**InventoryManager.sql**` depuis le [dépôt GitHub](https://github.com/phpcontrols/inventory-manager) de ce tutoriel, puis exécutez le script à l'aide d'un outil MySQL tel que [MySQL Workbench](https://www.mysql.com/products/workbench/). Cela créera une nouvelle base de données nommée `**InventoryManager**` ainsi que les tables nécessaires pour ce tutoriel.

### Une note sur ZenBase

```
Le système de gestion de stock est également l'un des nombreux modèles d'application prêts à l'emploi disponibles sur ZenBase (construit sur phpGrid) pour que chacun — avec ou sans compétences en codage — puisse utiliser et personnaliser selon ses propres besoins.
```

### Configuration de phpGrid

Passons à la suite.

Nous utiliserons un composant de grille de données de [phpGrid](https://phpgrid.com) pour gérer toutes les opérations internes de la base de données **CRUD (Create, Remove, Update, and Delete)**.

Assurez-vous de [télécharger une copie de phpGrid](https://phpgrid.com/download/) avant de continuer.

Pour installer phpGrid, suivez ces étapes :

1. Décompressez le fichier téléchargé de phpGrid.
2. Téléchargez le dossier `**phpGrid**` vers le dossier phpGrid.
3. Terminez l'installation en configurant le fichier `**conf.php**`.

Avant de commencer à coder, nous devons inclure les informations suivantes dans `**conf.php**`, le fichier de configuration de phpGrid.

### Création de l'interface utilisateur (UI)

Notre système d'inventaire se compose de quatre pages :

* Inventaire actuel
* Achats entrants
* Commandes à expédier
* Rapports

![Image](https://cdn-media-1.freecodecamp.org/images/5AWVXClN4dV5xDNjuSOuNyHn2iJWDJ3Xu4PL)

### Menus

Le fichier d'inclusion pour le menu est stocké dans un dossier `**inc**` nommé `**menu.php**`. Le code pour le menu est simple. Pour des raisons de concentration, nous n'entrerons pas dans les détails. N'hésitez pas à regarder le code à l'intérieur du dossier `[**inc**](https://github.com/phpcontrols/inventory-manager/tree/master/inc)`.

Nous avons également ajouté un élément de menu nommé `Rapports`.

![Image](https://cdn-media-1.freecodecamp.org/images/nL2WOBl0IY3-KmkHLxyWenxsQ5CmYZcKTC-k)

### Pages

Nous utiliserons le même modèle de page que nous avons utilisé pour les tutoriels [CRM](https://phpgrid.com/example/build-first-simple-crm-scratch/) et [Gestion de projet](https://phpgrid.com/example/build-project-management-application-scratch/).

#### Inventaire actuel

![Image](https://cdn-media-1.freecodecamp.org/images/AVz5Mdch-aEydKuRqCNgKCUz24E7XCreeaIM)

Commençons par la page Inventaire actuel.

Les achats entrants augmentent l'inventaire tandis que les commandes sortantes le diminuent. D'un point de vue maître-détail, l'Inventaire actuel n'a pas une, mais deux grilles de détails — les **Achats** (achats entrants) et les **Commandes** (commandes sortantes).

Ainsi, la page Inventaire actuel est composée d'une grille maître (l'Inventaire actuel en stock) et de deux grilles de détails (Achats entrants et Commandes sortantes). Nous pouvons facilement présenter ces relations en utilisant la fonction de phpGrid une grille maître et plusieurs grilles de détails.

### phpGrid Lite vs. Professional et Enterprise

> **Les fonctionnalités Master detail et Grouping nécessitent l'édition Professional ou Enterprise de phpGrid. Si vous utilisez la version Lite gratuite, vous pouvez toujours utiliser [subgrid](https://phpgrid.com/documentation/set_subgrid/) à la place de Master detail bien que moins avancé. Les versions Professional ou Enterprise sont fortement recommandées.**

Si vous avez lu le dernier tutoriel [Building a Donation Manager from Scratch](https://medium.com/@chensformers/a-step-by-step-guide-to-building-a-donation-manager-from-scratch-in-php-part-i-514a7d34ee82), vous n'aurez aucun problème à suivre le code ci-dessous.

Notez l'utilisation de la fonction [set_col_format()](https://phpgrid.com/documentation/set_col_format/) utilisée pour formater les entiers.

C'est tout pour la grille de données Inventaire actuel. Voici à quoi elle ressemble pour l'instant :

![Image](https://cdn-media-1.freecodecamp.org/images/z4aLzzcqepAfvKzy8SgY-hpYfAkRjh6NAbDE)

Maintenant, apportons quelques modifications pour améliorer notre grille de données **Produit**.

Tout d'abord, nous allons ajouter un formatage conditionnel : chaque fois que **InventoryOnHand** est défini à zéro ou à une valeur négative, il est affiché avec une couleur de fond différente. Nous utiliserons la fonction [set_conditional_format()](https://phpgrid.com/documentation/set_conditional_format/) à cet effet.

Le code ci-dessus ajoute une condition d'affichage de sorte que chaque fois que le champ `InventoryOnHand` a une valeur inférieure (`lt`) à un, la couleur du texte passe à `red` et la couleur de fond à gris foncé (`#DCDCDC`).

Deuxièmement, chaque fois que `InventoryOnHand` est inférieur à la valeur affichée dans `MinimumRequired`, nous souhaitons alerter l'utilisateur en l'affichant avec une couleur de fond proéminente telle que l'or. Pour comparer les valeurs entre deux champs, nous devons passer à Javascript car la fonction [set_conditional_format()](https://phpgrid.com/documentation/set_conditional_format/) ne fonctionne qu'avec un seul champ.

Le code ci-dessous utilise une boucle `for` pour parcourir chaque ligne de la grille de données **Produits**. Il compare `inventoryOnHand` avec `minimumRequired` et, lorsque la condition est remplie, il utilisera la fonction `setCell` pour changer la couleur de fond.

Vous pouvez en savoir plus sur la [comparaison de plusieurs valeurs de cellules](https://phpgrid.uservoice.com/knowledgebase/articles/909546-conditional-format-compare-two-cells) sur le site de support de phpGrid.

Ensuite, sur la même page, nous devons voir les achats entrants (**Incoming**) et les commandes sortantes (**Outgoing**) pour un produit spécifique.

#### Grille de détails des achats (Incoming)

#### Grille de détails des commandes (Outgoing)

Les deux grilles de détails utilisent la même clé étrangère `ProductId` pour se lier à la grille de données maître (**Produits**).

Enfin, notre code complet pour gérer la page **Inventaire actuel** est :

Voici un aperçu de la page d'inventaire :

![Image](https://cdn-media-1.freecodecamp.org/images/Spe5wb7oEkaVAikkKBEJrPzQExFzFj70EZTf)

### Achats entrants

![Image](https://cdn-media-1.freecodecamp.org/images/luyVRlrvSLQ10tITWdwYUHJ4A5flLdxEtuaZ)

La page suivante est la page **Achats entrants**. Elle est similaire à la **Grille de détails des achats** que nous avons vue lors de la configuration de la page **Inventaire actuel**. Nous regroupons les achats par `ProductId` et affichons la somme dans `NumberReceived`. Tout achat entrant augmentera l'inventaire.

> **Note : La fonctionnalité de regroupement n'est disponible que dans l'édition Professional et Enterprise de phpGrid. Pour filtrer sans le regroupement, utilisez la [recherche intégrée](https://phpgrid.com/example/integrated-search/).**

Le code complet :

Voici une capture d'écran de notre page **Achats entrants** avec le regroupement activé :

![Image](https://cdn-media-1.freecodecamp.org/images/8sDg-Tnhm0s1ZH5td-xdCWokJ3oO3ulAzf-T)

### Commandes sortantes

![Image](https://cdn-media-1.freecodecamp.org/images/9ymBPuuoXXvfEoCntXG-WPBxpUqIiGOpUACw)

La page suivante est la page **Commandes sortantes**. Elle est similaire à la **Grille de détails des commandes** de la page **Inventaire actuel**. Ici, nous introduirons une fonction avancée appelée [set_grid_method()](https://phpgrid.com/documentation/set_grid_method/).

### Résumé

Ce tutoriel construit un système d'inventaire simple et extensible en moins de 50 lignes de code. Le style progressif de ces tutoriels aide également le lecteur à devenir finalement plus familier et à l'aise avec phpGrid en introduisant un nombre limité de nouvelles fonctionnalités de phpGrid dans chacun d'eux.

### Ce qui arrive

Cela marque la fin du code nécessaire pour créer les grilles de données requises pour ce tutoriel. Cependant, nous n'avons pas encore terminé. Il reste encore une page à créer — Rapports. Nous couvrirons cela après le saut.

À quoi sert un système d'inventaire sans aucun type de rapport ? Dans cette section, vous apprendrez à utiliser [phpChart](http://phpchart.com/) — qui s'intègre parfaitement avec phpGrid — pour créer des rapports visuellement agréables et utiles pour votre application Inventory Manager.

Voici à quoi ressemblera notre page une fois terminée :

![Image](https://cdn-media-1.freecodecamp.org/images/rLTmQ3BPx8zS1nbHXhPPaTDHB81SDxBrWqDE)

Avant de commencer, nous devons installer phpChart. Il est recommandé d'obtenir la [version complète de phpChart](https://phpchart.com/download/) puisque la version gratuite (phpChart Lite) ne supporte que le graphique en ligne.

### Configuration de phpChart

Il est important de garder phpGrid et phpChart dans des dossiers séparés. Voici la hiérarchie des dossiers **recommandée**.

```
www    +-- Donation_Manager    |   |-- phpGrid    |   |   +-- conf.php    |   |-- phpChart    |   |   +-- conf.php    |   +-- ...
```

### Conception du rapport

Nous placerons un graphique en secteurs à côté d'une grille de résumé d'inventaire. La grille de données fournit les données de la série pour tracer le graphique en secteurs.

![Image](https://cdn-media-1.freecodecamp.org/images/oBEgm5-eYi2TXN1Ay5YQ-wgwGZveIgLFZpAp)

### Intégration de phpGrid et phpChart

Tout d'abord, incluez les appels aux deux fichiers `**conf.php**` au début du code.

```
require_once("phpGrid/conf.php"); require_once("phpChart/conf.php");
```

### Graphique en secteurs

Voici le code complet pour créer notre graphique en secteurs :

Passons en revue le code.

La première ligne est le constructeur. Nous passons `array(null)` comme données de la série car nous ne souhaitons pas avoir de données affichées dans le graphique en secteurs initialement. Les données d'inventaire utilisées pour tracer le graphique ne sont pas encore disponibles lorsqu'il est initialisé pour la première fois. Les données sont fournies par la grille de données plus tard en JSON.

Nous donnons également à notre graphique un nom unique, `PieChart`.

Ensuite, nous lui donnons un titre. Rien de compliqué ici.

Une fois que nous avons le titre, nous appelons la fonction [series default](https://phpchart.com/phpChart/docs/output/C_PhpChartX_set_series_default@.html) pour définir le `renderer` sur `PieRenderer`. Contrairement à un graphique en barres, un graphique en secteurs n'a pas d'axe Y.

Nous pouvons également définir la propriété `rendererOptions`. Nous n'entrerons pas dans les détails de chaque option ici, mais vous pouvez trouver plus d'informations dans la [documentation en ligne](https://phpchart.com/documentation/).

Nous voulons également afficher une légende. La commande set_legend ci-dessous affiche la légende à l'ouest (noté par `w`) ou à gauche du graphique en secteurs.

Nous supprimerons également la bordure et l'arrière-plan.

Enfin, nous dessinons notre graphique en lui donnant une hauteur et une largeur en pixels.

Cependant, si vous exécutez le code maintenant, vous ne verrez pas le graphique car les données utilisées pour le rendre ne sont pas encore disponibles.

### Grille de résumé d'inventaire

Ici, nous utiliserons la même grille de données d'inventaire que celle que nous avons utilisée dans la page **Produits**. Nous devons simplement ajouter une chose de plus — un gestionnaire d'événements.

Dans phpGrid, nous pouvons ajouter un gestionnaire d'événements avec la fonction [add_event()](https://phpgrid.com/documentation/add_event/). add_event() lie un gestionnaire d'événements, qui est essentiellement une fonction JavaScript, à un événement phpGrid spécifique. Une liste des événements possibles peut être trouvée [ici](https://phpgrid.com/documentation/add_event/).

Puisque nous devons attendre que la grille de données ait fini de charger **avant** qu'elle ne puisse envoyer les données pour tracer le graphique, nous utilisons l'événement `jqGridLoadComplete`.

**phpGrid 101 — Événement jqGridLoadComplete**

jqGridLoadComplete est le dernier événement qui se produit une fois que tout le corps de la grille de données a fini de charger. Notez que le corps de la grille sera rechargé si l'utilisateur change l'ordre de tri d'une colonne ou définit un filtre.

#### Envoi de données avec Javascript

Ce qui suit est le gestionnaire d'événements Javascript pour `jqGridLoadComplete`.

Le code complet :

Maintenant, vous y êtes. Vous venez de construire votre tout premier système de gestion d'inventaire à partir de zéro en utilisant PHP et MySQL !

Merci d'avoir lu ! Si vous avez aimé cet article, veuillez m'applaudir afin que plus de personnes le voient.

### Nouveau en programmation ? N'ayez pas peur !

Si vous êtes nouveau en programmation et que vous n'êtes pas encore à l'aise avec le codage, vous pouvez consulter [ZenBase](https://getzenbase.com/) qui est construit sur phpGrid. Le système de gestion de stock n'est qu'un des [nombreux modèles d'application](https://getzenbase.com/templates/) prêts à l'emploi disponibles sur ZenBase pour que chacun — _avec ou sans_ compétences en codage — puisse utiliser et personnaliser selon ses propres besoins.

### Démo en ligne

* [Inventaire actuel](https://phpdatagrid.com/apps/inventory-manager/products.php)
* [Achats entrants](https://phpdatagrid.com/apps/inventory-manager/incoming-purchases.php)
* [Commandes sortantes](https://phpdatagrid.com/apps/inventory-manager/outgoing-order.php)
* [Rapports](https://phpdatagrid.com/apps/inventory-manager/reports.php) (avec grille de données côte à côte)

### Prochaine étape : Ajouter le scanneur de code-barres

[Ajouter le scanneur de code-barres à notre système de gestion de stock](https://medium.com/@chensformers/inventory-management-system-with-barcode-scanner-in-php-a-definitive-guide-d18fdc165511)

![Image](https://cdn-media-1.freecodecamp.org/images/VqWE2ltTZhdjoJld8PcEnfrTL4g645hyQJTv)

### Télécharger le code source sur Github

[**phpcontrols/inventory-manager**](https://github.com/phpcontrols/inventory-manager)  
[_Code source de l'application de gestion de stock géniale en PHP et MySQL de A à Z_github.com](https://github.com/phpcontrols/inventory-manager)

### **Problème courant :**

**Erreur fatale** : Erreur non capturée : Classe 'phpGrid\C_DataGrid' introuvable

**Comment corriger :**  
Si vous utilisez la version Lite gratuite, vous pouvez soit commenter la première ligne

```
// use phpGrid\C_DataGrid;
```

— OU —

Ajoutez un symbole d'espace de noms global — une barre oblique inverse unique — AVANT le constructeur

```
$dg = new \C_DataGrid("SELECT * FROM orders", "orderNumber", "orders");
```

### Vous pourriez également être intéressé par ces tutoriels :

[**Créer une application de gestion de projet à partir de zéro**](https://phpgrid.com/example/build-project-management-application-scratch/)  
[_Qu'est-ce qu'une application de gestion de projet ?_](https://phpgrid.com/example/build-project-management-application-scratch/)[**Créer un CRM simple de A à Z**](https://phpgrid.com/example/build-first-simple-crm-scratch/)   
[_La gestion de la relation client (CRM) est un système qui gère les interactions et les données des clients tout au long du parcours client..._](https://phpgrid.com/example/build-first-simple-crm-scratch/)[**Créer un gestionnaire de dons à partir de zéro en PHP**](https://medium.com/@chensformers/a-step-by-step-guide-to-building-a-donation-manager-from-scratch-in-php-part-i-514a7d34ee82)

### Merci d'avoir lu. Si vous avez aimé cet article, veuillez cliquer sur ce bouton d'applaudissements ? pour aider les autres à le trouver et [me suivre sur Twitter](https://twitter.com/midlifesaas).

![Image](https://cdn-media-1.freecodecamp.org/images/vOBVYAx4FtRWyDloyXcnKPsRfAh4OMvCI9zC)

### **Souhaitez-vous voir plus de tutoriels comme celui-ci ? Envoyez une demande à mon [Twitter](https://twitter.com/midlifesaas) ou laissez un commentaire ci-dessous !**