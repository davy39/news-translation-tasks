---
title: Comment créer des règles de validation de données dans Excel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-26T00:07:47.000Z'
originalURL: https://freecodecamp.org/news/create-data-validation-rules-excel
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-pixabay-262438.jpg
tags:
- name: data
  slug: data
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Comment créer des règles de validation de données dans Excel
seo_desc: 'By Faith Oyama

  Data validation is a feature in Excel used in restricting data entry in specific
  cells. It can also prompt the user to enter valid data into the cells based on the
  rules and restrictions provided by the creator of the Excel worksheet. ...'
---

Par Faith Oyama

La validation des données est une fonctionnalité d'Excel utilisée pour restreindre la saisie de données dans des cellules spécifiques. Elle peut également inviter l'utilisateur à entrer des données valides dans les cellules en fonction des règles et restrictions fournies par le créateur de la feuille de calcul Excel. 

Lors de la configuration d'un classeur, vous pouvez vouloir vous assurer que les utilisateurs saisissent un type spécifique de données. Par exemple, vous pouvez vouloir autoriser uniquement des dates, des nombres ou des lettres dans une plage spécifique à être imputés dans une cellule. Cela est crucial si vous souhaitez éliminer autant d'erreurs que possible dans vos données.

## Types de règles de validation de données dans Excel

Voici quelques règles de validation de données que vous pouvez configurer dans Excel :

* Autoriser uniquement des valeurs textuelles ou numériques dans une cellule.
* Autoriser uniquement des nombres dans une plage spécifique.
* Afficher un message d'avertissement lorsque l'utilisateur saisit des données incorrectes.
* Autoriser uniquement des dates et heures en dehors d'une plage donnée.
* Règle de validation basée sur des critères d'une autre cellule.

## Étapes pour créer des règles de validation de données dans Excel.

Pour créer une règle de validation de données dans Excel, procédez comme suit :

Tout d'abord, sélectionnez la ligne, la colonne ou la cellule spécifique à laquelle vous souhaitez appliquer une règle de validation de données.

Ensuite, ouvrez le volet de données et cliquez sur la validation des données. Alternativement, vous pouvez accéder directement à la boîte de dialogue de validation des données en appuyant sur les touches suivantes de votre clavier séparément. ALT > D > L. Ne maintenez pas les touches enfoncées ensemble, appuyez sur les touches séparément et vous serez dirigé vers la boîte de dialogue également.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/data-menu.png)

Créez la validation des données en fonction des données que vous souhaitez voir fournies dans la cellule ou la ligne.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/data-validation.png)

Vous pouvez fournir les critères de validation suivants :

**Autoriser** : Créez une règle basée sur le type de données que vous souhaitez autoriser. Vous pouvez en choisir une dans le menu déroulant. Vous pouvez décocher le bouton "Ignorer les blancs" si vous ne voulez pas d'espaces vides.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/select-whole-number.png)

**Données** : Dans le menu déroulant, vous pouvez choisir les critères et également saisir les valeurs minimales et maximales que vous souhaitez que l'utilisateur saisisse. 

Avec les critères de validation définis, cliquez sur OK pour fermer la fenêtre ou cliquez sur l'onglet Message d'entrée ou Alerte d'erreur pour donner plus d'informations à l'utilisateur sur la règle de validation des données.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/select-between.png)

**Message d'entrée** : Bien que cela soit facultatif, vous pouvez saisir un message à afficher lorsque l'utilisateur clique sur une cellule qui a une règle de validation de données définie.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/input-message.png)

Ensuite, donnez un titre à votre message d'entrée, et sous le message d'entrée, assurez-vous que le message que vous fournissez est clair pour l'utilisateur. Cliquez sur OK pour fermer la boîte de dialogue ou accédez à l'onglet Alerte d'erreur.

Ensuite, affichez un message d'erreur. Cela est facultatif, mais il est bon de pratique d'afficher un message d'erreur aux utilisateurs lorsqu'ils saisissent des données qui ne respectent pas la règle de validation que vous avez définie.

Il existe trois types d'alertes d'erreur :

1. **Arrêt** : Il s'agit du type par défaut et il est très strict, car il empêche les utilisateurs de saisir des données invalides. Vous ne pouvez cliquer que sur "Réessayer" ou "Annuler".

![Image](https://www.freecodecamp.org/news/content/images/2024/04/enter-a-valid-number-popup.png)

2. **Avertissement** : Cela avertira uniquement l'utilisateur, mais n'est pas aussi strict que l'avertissement d'arrêt. Un utilisateur peut ignorer le message en cliquant sur "OUI" et les données invalides seront saisies.

Voici un exemple du message d'avertissement qu'un utilisateur recevra :

![Image](https://www.freecodecamp.org/news/content/images/2024/04/continue-no.png)

3. **Information** : Il s'agit d'un type d'alerte d'erreur permissif, car il informe uniquement l'utilisateur des données invalides saisies.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/continue-yes.png)

Si l'utilisateur clique sur OK, les données invalides sont insérées dans la feuille de calcul. Si l'utilisateur clique sur Annuler, les données sont supprimées.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/error-alert-stop.png)

Donnez un titre à l'alerte d'erreur et fournissez également un message pour que vos utilisateurs le voient. Lorsque vous avez terminé, cliquez sur OK et votre règle de validation de données est définie.

# Conclusion

La validation des données dans Excel est une fonctionnalité puissante que vous devriez utiliser lors de la création d'une feuille de calcul Excel.

Vous pouvez utiliser la fonctionnalité de validation des données dans Excel pour créer des règles qui garantiront que les données saisies répondent à certains critères ou suivent des règles prédéfinies. La définition d'une règle de validation des données aide à maintenir l'exactitude, la cohérence et l'intégrité des données dans votre feuille de calcul Excel.