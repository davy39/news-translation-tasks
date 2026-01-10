---
title: Comment supprimer les doublons dans Excel – Supprimer les lignes en double
  en quelques clics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T20:47:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-duplicates-in-excel-delete-duplicate-rows-with-a-few-clicks
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/excel-1-1.jpg
tags:
- name: efficiency
  slug: efficiency
- name: excel
  slug: excel
- name: Productivity
  slug: productivity
seo_title: Comment supprimer les doublons dans Excel – Supprimer les lignes en double
  en quelques clics
seo_desc: "By James Murphy\nExcel has many applications, like keeping track of inventory,\
  \ maintaining a mailing list, making sales reports, and many others. \nAs the database\
  \ grows, one main issue many users encounter is getting duplicate values and rows.\
  \ This ca..."
---

Par James Murphy

[Excel](https://www.freecodecamp.org/news/how-to-create-read-update-and-search-through-excel-files-using-python-c70680d811d4/) a de nombreuses applications, comme le suivi des stocks, la gestion d'une liste de diffusion, la création de rapports de ventes, et bien d'autres.

À mesure que la base de données grandit, un problème majeur auquel de nombreux utilisateurs sont confrontés est l'apparition de valeurs et de lignes en double. Cela peut rendre vos calculs inexacts et faire douter de votre compétence.

Vous pourriez finir par donner un rapport récapitulatif avec des valeurs en double ou même envoyer une lettre à la même personne deux fois. Vous devrez donc trouver et supprimer les doublons pour éviter ces petites erreurs qui pourraient avoir des implications sérieuses.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/excel-1-1-1.jpg)
_Supprimer les doublons_

## Option 1 : Utiliser l'outil de suppression des doublons

Puisque ce problème se pose souvent, il existe une commande dédiée dans le ruban qui facilite la gestion des doublons. C'est le cas avec les versions récentes de la suite Microsoft Office, comme Excel 2007 jusqu'à 2016.

### Sélectionnez le tableau sur lequel vous allez travailler

Tout d'abord, vous devez sélectionner les cellules ciblées, car l'outil peut être utilisé pour supprimer les doublons dans des lignes entières ou des enregistrements partiellement correspondants.

Vous pouvez le faire en sélectionnant le tableau, puis en appuyant sur Ctrl + A. Vous devez vous assurer que le fichier original est enregistré, car le processus supprime les doublons de manière permanente.

### Cliquez sur l'onglet Données en haut de l'écran

Une fois que vous avez sélectionné la plage, vérifiez en haut de l'écran et cliquez sur l'onglet Données. Les différentes commandes seront affichées, et vous devriez alors chercher « supprimer les doublons » et cliquer dessus.

Une petite boîte de dialogue apparaîtra à l'écran. La première ligne est automatiquement sélectionnée car « mes données ont un en-tête » est coché. Si il n'y a pas d'en-tête et que les données commencent à la 1<sup>ère</sup> ligne, désélectionnez cette option.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-165.png)

### Appuyez sur le bouton OK pour supprimer les doublons

Le tableau entier est maintenant sélectionné, et vous devriez donc appuyer sur le bouton OK. Cela supprimera tous les doublons. Les détails de la suppression apparaissent à l'écran avec les valeurs uniques restantes et le nombre d'entrées en double supprimées affiché.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-166.png)

Cependant, si vous souhaitez supprimer des **doublons partiels** basés sur des colonnes spécifiques, vous devriez les sélectionner, en laissant le reste. Si le tableau contient de nombreuses colonnes, il est préférable de tout désélectionner et de ne sélectionner que celles qui nécessitent la suppression des doublons.

Une fois terminé, vous devriez cliquer sur OK. Les informations en double seront alors supprimées, et les détails seront affichés à l'écran.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/EXCEL-1.png)

## Option 2 : Utiliser les filtres avancés dans Excel

L'icône de filtre avancé vous aide à identifier et supprimer les doublons dans Excel. Cela peut être utilisé dans la dernière suite Microsoft Office et la version 2003. Vous devez ouvrir votre feuille de calcul Excel et tout sélectionner en cliquant sur Ctrl + A.

### Cliquez sur l'onglet Données puis sur le bouton Avancé sous la section Trier et filtrer

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-167.png)

Vous devriez ensuite cliquer sur l'onglet Données en haut de l'écran où différentes sections apparaissent en dessous. Cherchez la section Trier et filtrer et cliquez sur le bouton Avancé.

Une boîte de dialogue apparaîtra à l'écran où vous pouvez soit sélectionner « copier vers un autre emplacement » ou « filtrer la liste en place ». Ce dernier masque toutes les lignes avec des doublons tandis que le premier génère une copie des enregistrements.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-168.png)

### Ajustez la plage de données sous le champ "Plage de liste"

Dans la boîte de dialogue, il y a un champ de plage de liste avec des données remplies par Excel. Si vous souhaitez changer la plage, vous pouvez le faire en l'ajustant sous « Plage de liste ».

Laisser le champ de plage de critères vide et copier vers le champ n'est utile que si vous avez choisi de copier vers un autre emplacement. Sinon, laissez-le vide pour l'option « filtrer la liste en place ».

### Cochez la case "Enregistrements uniques uniquement"

Sous la même boîte de dialogue, il y a un champ intitulé "Enregistrements uniques uniquement" - cochez cette case. Cela indique à Excel de filtrer les doublons tout en conservant les entrées uniques.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-169.png)

### Cliquez sur OK pour supprimer les doublons

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-170.png)

Après avoir suivi ce processus, vous pouvez cliquer sur le bouton OK pour vous débarrasser des doublons. Le document contient alors des données en double à l'exception de celles qui ont été supprimées.

Comme le processus suppose qu'il y a des en-têtes dans le document, si la 1<sup>ère</sup> ligne contient un doublon, il ne sera pas supprimé. Supprimez-le manuellement s'il ne s'agit pas d'un en-tête.

Lorsque vous utilisez le processus de filtre avancé, vous ne pouvez supprimer les doublons que dans le tableau entier, car il n'y a pas de choix pour le faire partiellement. Cependant, vous pouvez supprimer les doublons et, en même temps, créer une copie des données.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/excel-2.jpg)

## Option 3 : Utiliser un outil de suppression des doublons avec 2 clics de souris

En plus des outils de suppression des doublons intégrés, vous pouvez utiliser des modules complémentaires tels que [Ablebits duplicate](https://www.ablebits.com/excel-remove-duplicates/index.php) remover pour vous débarrasser des doublons. L'outil est polyvalent et peut effectuer d'autres fonctions également. Il fonctionne sur tous les systèmes d'exploitation et toutes les versions d'Excel. Ici, nous allons nous concentrer sur une façon d'utiliser l'outil qui ne prend que 2 clics de souris.

### Sélectionnez la cellule dans le tableau d'intérêt

Vérifiez le tableau où vous devez supprimer les doublons, et dans les données Ablebits, cliquez sur "supprimer les doublons du tableau". Cela sélectionne le tableau entier, et la boîte de dialogue s'ouvrira avec toutes les colonnes choisies automatiquement.

### Sélectionnez supprimer les doublons dans la liste déroulante sous le champ "sélectionner l'action"

En bas à droite, il y a une liste déroulante sous le champ sélectionner l'action. Choisissez l'option supprimer les doublons et appuyez sur OK. Les valeurs en double seront supprimées à l'exception des 1<sup>ères</sup> occurrences.

### Suppression des doublons dans les colonnes clés

Le processus en 2 clics de souris peut être utilisé pour supprimer les doublons sur des lignes spécifiques sous des colonnes cruciales. Pour ce faire, décochez les autres colonnes en laissant celles que vous souhaitez supprimer cochées. Suivez les deux points ci-dessus, et les doublons seront supprimés.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-171.png)

L'action de sélection peut être utilisée pour d'autres opérations telles que la copie des doublons vers un autre emplacement sans les supprimer. Utilisez le menu déroulant pour sélectionner en conséquence afin que votre feuille Excel soit propre et sans erreurs.

## Mot de la fin

Supprimer les doublons sur Excel est simple en utilisant les trois options mises en évidence ci-dessus. Le processus est facile, et avec ce guide, vous pouvez le faire avec quelques clics pour obtenir l'aide ultime pour les [devoirs](https://my-assignment.help/) et l'assistance de travail d'Excel.

Lorsque vous travaillez dans Excel, vous devez toujours nettoyer votre ensemble de données, en éliminant toute erreur non professionnelle. Si vous rencontrez des défis, vérifiez que les données traitées ne sont pas sous-totalisées ou esquissées.

Dans de tels cas, vous devez supprimer les sous-totaux et l'esquisse, puis utiliser l'une des méthodes ci-dessus. Les données seront alors nettoyées, ce qui les rendra beaucoup plus faciles à travailler.