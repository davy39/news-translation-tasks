---
title: Comment créer un formulaire de recherche dans Google Sheets – Tutoriel Google
  Apps Script
subtitle: ''
author: Nibesh Khadka
co_authors: []
series: null
date: '2024-02-09T15:39:47.000Z'
originalURL: https://freecodecamp.org/news/create-search-form-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Search-Form-Thumbnail-3.png
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: JavaScript
  slug: javascript
seo_title: Comment créer un formulaire de recherche dans Google Sheets – Tutoriel
  Google Apps Script
seo_desc: "Have you ever struggled with navigating a massive spreadsheet? You can\
  \ do away with the endless scrolling and unlock the power of targeted data retrieval\
  \ with a custom search form using Google Apps Script. \nIn this hands-on guide,\
  \ we'll craft a searc..."
---

Avez-vous déjà eu du mal à naviguer dans une feuille de calcul massive ? Vous pouvez vous passer du défilement sans fin et débloquer la puissance de la récupération de données ciblées avec un formulaire de recherche personnalisé utilisant Google Apps Script. 

Dans ce guide pratique, nous allons créer un outil de recherche qui s'intègre parfaitement à votre feuille de calcul, vous permettant de :

* **Rechercher dans plusieurs onglets :** Interrogez facilement les données de différentes sections de votre feuille de calcul avec des champs de saisie dédiés.
* **Maîtriser les recherches ET & OU :** Trouvez exactement ce dont vous avez besoin avec les fonctionnalités de recherche **ET** et **OU**, assurant une correspondance précise ou flexible en fonction de vos exigences.
* **Augmenter votre productivité :** Gagnez un temps précieux en éliminant les recherches manuelles et en filtrant uniquement les points de données pertinents.

Prêt à transformer votre feuille de calcul en un hub de recherche dynamique ? Suivez-nous alors que nous explorons le monde de Google Apps Script et vous donnons les moyens de devenir un maître de la recherche dans les feuilles de calcul !

Vous pouvez trouver tout le code et les actifs associés dans [ce dépôt GitHub](https://github.com/nibukdk/Search-Form-In-Google-Sheets).

%[https://www.youtube.com/watch?v=FkYW2oEbEQk&t=886s]

<h2 id="toc">Table des matières</h2>
<ul>
  <li>
    <a href="#comprendre-la-structure-de-la-feuille-de-calcul"
      >Comprendre la structure de la feuille de calcul</a
    >
  </li>
  <li>
    <a href="#comment-construire-le-formulaire-de-recherche-listes-deroulantes-dynamiques-et-logique"
      >Comment construire le formulaire de recherche – Listes déroulantes dynamiques et logique</a
    >
  </li>
  <li><a href="#recherche-et-ou">Recherche ET ou OU</a></li>
  <li>
    <a href="#comment-creer-la-fonction-de-recherche-avec-google-apps-script"
      >Comment créer la fonction de recherche avec Google Apps Script</a
    >
  </li>
  <li>
    <a href="#comment-creer-la-fonction-etrecherche"
      >Comment créer la fonction etrecherche</a
    >
  </li>
  <li>
    <a href="#comment-correspondre-a-tous-les-criteres-avec-la-recherche-et"
      >Comment correspondre à tous les critères avec la recherche ET</a
    >
  </li>
  <li>
    <a href="#donner-vie-aux-resultats-de-recherche"
      >Donner vie aux résultats de recherche</a
    >
  </li>
  <li>
    <a href="#comment-supprimer-les-doublons-pour-assurer-la-precision"
      >Comment supprimer les doublons pour assurer la précision</a
    >
  </li>
  <li>
    <a href="#mettre-le-tout-ensemble-afficher-vos-resultats-de-recherche"
      >Mettre le tout ensemble – Afficher vos résultats de recherche</a
    >
  </li>
  <li>
    <a href="#comment-utiliser-la-recherche-ou-pour-trouver-des-donnees-qui-correspondent-a-un-terme-quelconque"
      >Comment utiliser la recherche OU pour trouver des données qui correspondent à un terme quelconque</a
    >
  </li>
  <li>
    <a href="#tenir-les-utilisateurs-informes-messages-toast-pour-une-recherche-sans-couture"
      >Tenir les utilisateurs informés – Messages toast pour une recherche sans couture</a
    >
  </li>
  <li>
    <a href="#mettre-le-tout-ensemble-tester-votre-formulaire-de-recherche"
      >Mettre le tout ensemble – Tester votre formulaire de recherche</a
    >
  </li>
  <li>
    <a
      href="#felicitations-vous-avez-construit-un-moteur-de-recherche-puissant-dans-google-sheets"
      >Félicitations ! Vous avez construit un moteur de recherche puissant dans Google Sheets !
    </a>
  </li>
  <li>
    <a href="#explorer-les-options-de-personnalisation"
      >Explorer les options de personnalisation</a
    >
  </li>
</ul>


## Comprendre la structure de la feuille de calcul

![Image](https://www.freecodecamp.org/news/content/images/2024/02/sheet_tab.png)
_Structure de la feuille de calcul_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/TABS.png)
_Différents onglets dans les feuilles de calcul_

Comme le montre l'image ci-dessus, il y a cinq onglets dans la feuille de calcul. Les données sont divisées en trois onglets par année : 2021, 2022 et 2023.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/header_row.png)
_Colonnes dans 2021, 2022 et 2023 dans la feuille de calcul_

Toutes les colonnes sont les mêmes dans ces trois onglets.

Examinons la structure de votre onglet de recherche dédié. Il est divisé en deux sections clés :

1. **Formulaire de recherche (lignes 1-7) :** C'est ici que vous interagissez avec vos données. Chaque champ de saisie correspond à une colonne spécifique dans vos autres onglets de feuille de calcul, vous permettant de personnaliser vos requêtes de recherche. Pensez à eux comme des filtres, vous aidant à cibler les informations dont vous avez besoin.
2. **Résultats de recherche (lignes 8+) :** C'est ici que vous trouverez les données que vous avez recherchées. Chaque résultat inclut les informations pertinentes que vous avez spécifiées dans votre recherche, ainsi qu'une colonne supplémentaire nommée "Nom de la feuille - Index de ligne". Cela agit comme une carte pratique, pointant l'onglet et la ligne exacts de la feuille de calcul d'où provient chaque résultat. Plus besoin de chercher à travers des lignes sans fin – vous serez concentré sur les données dont vous avez besoin.

En comprenant cette disposition organisée, vous pouvez naviguer efficacement dans votre expérience de recherche et récupérer rapidement les informations dont vous avez besoin.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/search_form_2.png)
_Formulaire de recherche_

### 

### Comment construire le formulaire de recherche – Listes déroulantes dynamiques et logique

Le formulaire de recherche a trois champs de saisie : Client, Quantité et Description. Chacun utilise un menu déroulant automatiquement rempli avec des valeurs uniques de l'onglet Config de la feuille de calcul. Mais comment cette magie se produit-elle ?

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1706803411374/7a8a5da4-b71a-4e35-b8d2-750cb611f23b.png)
_Validation des données des entrées déroulantes_

Voici ce qui se passe en coulisses : 

1. **Source de données :** Les valeurs pour les listes déroulantes sont soigneusement collectées à partir de trois onglets séparés : 2021, 2022 et 2023.
2. **Combinaison des forces :** Une formule astucieuse fusionne ces valeurs en une seule liste consolidée.
3. **Division :** Cette liste combinée est ensuite transformée en un tableau, permettant d'accéder aux valeurs individuelles.
4. **Réorganisation des données :** La magie de la transposition transforme la ligne de valeurs en une colonne, les rendant plus faciles à manipuler.
5. **Suppression des doublons :** La fonction `UNIQUE` élimine les valeurs répétées, assurant une liste concise et organisée.
6. **Tri :** Enfin, les valeurs restantes sont triées par ordre alphabétique pour votre commodité de navigation.

Voici la formule utilisée : `SORT(UNIQUE(TRANSPOSE(split(TEXTJOIN(",",TRUE,'2021'!A2:A1001)&","&TEXTJOIN(",",TRUE,'2022'!A2:A1001)&","&TEXTJOIN(",",TRUE,'2023'!A2:A1001),","))))`

![Image](https://www.freecodecamp.org/news/content/images/2024/02/config_tab.png)
_Feuilles de configuration_

### Recherche ET vs OU

Une case à cocher dédiée (située en G4:G5) sert de centre de contrôle pour votre logique de recherche. Lorsqu'elle est cochée, elle active la recherche **ET**, nécessitant que tous les critères spécifiés soient présents dans les résultats. 

La laisser décochée passe à la recherche **OU**, fournissant des résultats plus flexibles tant qu'un critère correspond.

Rappelons que la feuille de calcul téléchargeable conserve toutes les formules préconfigurées et les règles de validation des données, rendant la configuration un jeu d'enfant. Nous plongerons dans la création de la fonction de recherche magique à l'étape suivante !

## Comment créer la fonction de recherche avec Google Apps Script

Ouvrez l'éditeur de script à partir de **Extensions>Apps Script**

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1706803889387/4802b8d2-965f-4c14-8daa-efd0512a1c06.png)
_Ouvrir Apps Script depuis Sheets_

Pour ce projet, vous allez créer deux fichiers **search.gs** et **utils.gs** dans l'éditeur.

Dans le fichier **search.gs**, commençons par récupérer notre feuille de calcul et les termes de saisie.

```javascript
var ss = SpreadsheetApp.getActiveSpreadsheet();
var searchSheet = ss.getSheetByName("search");
var _2023Sheet = ss.getSheetByName("2023");
var _2022Sheet = ss.getSheetByName("2022");
var _2021Sheet = ss.getSheetByName("2021");
// plages pour les colonnes nom, description et quantité pour chaque onglet
var nameRangeNotation = 'A2:A'
var descriptionRangeNotation = 'F2:F'
var quantityRangeNotation = 'E2:E'
// valeur pour les boîtes de saisie
var clientName = searchSheet.getRange('B2:C2').getValue();
var quantity = searchSheet.getRange('E2').getValue();
var description = searchSheet.getRange('G2:H2').getValue();
var hasIncludeAllSelected = searchSheet.getRange('G4:G5').getValue();
```

Maintenant, en dessous de ce code, nous allons créer la fonction `search`, qui orchestrera tout depuis le haut.

```javascript
/**
 * La fonction principale assignée au bouton de recherche dans la feuille de calcul. Elle orchestrer l'opération de recherche.
 */
function search() {
  try {
     
    let status;

    if (hasIncludeAllSelected) {
      //effectuer une recherche ET
      const newData = andSearch(clientName, description, quantity);
    
    }
    else {
         }

   

  } catch (e) {
    console.log(e)

  }
}
```

Dans ce projet, nous allons construire nos fonctions étape par étape. Commençons par déterminer le type de recherche en fonction de la case à cocher en G4:G5.

Si la case est cochée, nous allons activer la fonctionnalité de recherche **ET**. Cela signifie que tous les critères spécifiés dans les champs de saisie doivent être présents dans les résultats. Pour gérer cela, nous allons appeler une fonction dédiée nommée `andSearch()`. 

Nous allons créer cette fonction ensuite, directement en dessous de la fonction `search` existante.

Cette approche garantit que notre script s'adapte au type de recherche choisi par l'utilisateur, fournissant des résultats précis et pertinents en fonction de leurs besoins.

### Comment créer la fonction `andSearch()`

```javascript

/**
 * Effectue une recherche "ET" pour les mots-clés donnés dans leurs colonnes respectives Nom, Description et Quantité pour 
 * les onglets 2021, 2022, 2023. Retourne de nouveaux tableaux imbriqués pour les résultats de recherche à remplir dans la feuille de calcul de recherche.
 * @param {String} name 
 * @param {String} description 
 * @param {String} quantity 
 * @returns {Array<Array<String>>?} - [[],[],[]]
 */
function andSearch(name = null, description = null, quantity = null) {

  // obtenir l'index correspondant pour chaque feuille.
  const _2021SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2021Sheet, nameRangeNotation, name);
  const _2021SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2021Sheet, quantityRangeNotation, quantity);
  const _2021SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2021Sheet, descriptionRangeNotation, description);


  const _2022SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2022Sheet, nameRangeNotation, name);
  const _2022SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2022Sheet, quantityRangeNotation, quantity);
  const _2022SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2022Sheet, descriptionRangeNotation, description);

  const _2023SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2023Sheet, nameRangeNotation, name);
  const _2023SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2023Sheet, quantityRangeNotation, quantity);
  const _2023SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2023Sheet, descriptionRangeNotation, description);


 //.... continue

}
```

Cette fonction prend trois paramètres, chacun correspondant à un terme de recherche défini par l'utilisateur : nom, description et quantité.

Si l'un de ces termes de recherche est vide, nous attribuons simplement un tableau vide comme résultat. Cela gère efficacement les scénarios où les utilisateurs laissent certains champs non remplis.

La logique principale repose sur la fonction `searchSheetByColumn`. Pensez à elle comme un détective de données qui vérifie des colonnes spécifiques dans les onglets de la feuille de calcul. Elle prend trois arguments cruciaux :

* **sheet** : L'onglet spécifique à rechercher (par exemple : "2021").
* **rangeNotation** : La plage de colonnes à cibler (par exemple : "A2:A").
* **searchVal** : La valeur à correspondre dans la colonne choisie (par exemple : "Khadka").

En utilisant ces informations, `searchSheetByColumn` scanne la colonne désignée et retourne un tableau contenant les index des lignes où `searchVal` est trouvé dans cette feuille.

#### Recherche de la valeur de saisie dans une colonne

Créons maintenant la fonction `searchSheetByColumn` dans le fichier **utils.gs**.

```javascript
/**
 * Recherche le mot-clé donné dans la colonne donnée à l'intérieur de l'onglet de la feuille de calcul donné.
 * Il retourne tous les index correspondants des données. Les index sont indexés à partir du tableau, pas de la ligne.
 * @param {Spreadsheet} sheet - feuille à rechercher
 * @param {String} rangeNotation - plage de la colonne dans la feuille de calcul donnée
 * @param {String} searchVal - mot-clé à rechercher
 * @returns {Array<number>} - [1,23,12,45,12] 
 */
function searchSheetByColumn(sheet, rangeNotation, searchVal) {
  const data = sheet.getRange(rangeNotation).getValues().flat().filter(String); // obtenir les données
  if (data.length < 1) return [];
  // filtrer uniquement les index des lignes correspondantes
  // obtenu de https://stackoverflow.com/a/58980987/6163929
  const allIndexes = data.map((val, index) => ({ val, index }))
    .filter(({ val, index }) => rangeNotation === quantityRangeNotation ? Number(val) === Number(searchVal) : val.toLowerCase().includes(searchVal.toLowerCase())
    )
    .map(({ val, index }) =>
      index + 1
    ) // +1 car nous extrayons les données à partir de la deuxième ligne dans la notation, plus tard nous devons correspondre avec le tableau de données complet
  return allIndexes;
}
```

Le code ci-dessus fait ce qui suit :

* Récupère les données de la plage et de la feuille spécifiées en utilisant `sheet.getRange(rangeNotation).getValues().flat()`.
* Supprime les valeurs vides en filtrant avec `filter(String)`.
* Parcourt les données et les index et applique `map` pour créer un tableau d'objets avec à la fois les valeurs et leurs index correspondants.
* Convertit à la fois le terme de recherche et les valeurs de données en nombres en utilisant `Number()`.
* Filtre les correspondances exactes en utilisant `rangeNotation === quantityRangeNotation ? Number(val) === Number(searchVal)`
* Convertit à la fois le terme de recherche et les valeurs de données en minuscules.
* Filtre les correspondances en utilisant `val.toLowerCase().includes(searchVal.toLowerCase())`
* Extrait les index correspondants en utilisant `map(({ val, index }) => index + 1)`.
* Ajoute 1 pour corriger le début de l'extraction à partir de la deuxième ligne.

### Comment correspondre à tous les critères avec la recherche ET

 Ajoutez le morceau de code suivant dans la fonction `andSearch`.

```javascript
function andSearch(name = null, description = null, quantity = null) {

// ..... continuation des codes précédents
  // index correspondants des lignes dans la recherche ET
  const _2021SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2021SheetNameSearchIndexes, _2021SheetQuantitySearchIndexes, _2021SheetDescriptionSearchIndexes);
  const _2022SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2022SheetNameSearchIndexes, _2022SheetQuantitySearchIndexes, _2022SheetDescriptionSearchIndexes);
  const _2023SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2023SheetNameSearchIndexes, _2023SheetQuantitySearchIndexes, _2023SheetDescriptionSearchIndexes);
//..........
}
```

Rappelons la recherche **ET** ? Son objectif est de découvrir des points de données qui cochent toutes les cases que vous avez spécifiées. Pour y parvenir, nous devons filtrer uniquement les lignes qui contiennent tous vos termes de recherche – nom, quantité et description – dans les trois feuilles de calcul.

Entrez la fonction `filterRowsIndexesWithAllSearchTerms`, à créer dans le fichier **utils.gs**. Cet outil pratique parcourt chaque ligne et s'assure qu'elle correspond à chaque critère que vous avez établi. Alors, comment fonctionne-t-il ? Nous explorerons le code ensuite !

```javascript
/**
 * Fonction qui filtre uniquement les lignes qui contiennent les trois mots-clés fournis par l'utilisateur
 * @param {Array<String>} arr1 
 * @param {Array<String>} arr2 
 * @param {Array<String>} arr3 
 * @returns {Array<String>?} 
 */
function filterRowsIndexesWithAllSearchTerms(arr1, arr2, arr3) {
  // créer un tableau imbriqué
  const arr = [arr1.length > 0 ? [...arr1] : "", arr2.length > 0 ? [...arr2] : "", arr3.length > 0 ? [...arr3] : ""].filter(String);

  // retourner vide si la longueur des tableaux maîtres est inférieure au nombre de termes de recherche
  if (arr.length < 1 || arr.length < numberOfInputFieldEntered) return [];

  const matchingIndexes = [];

  if (arr.length === 3) {

    arr[0].forEach((val) => {
      if (arr[1].includes(val) && arr[2].includes(val)) {
        matchingIndexes.push(val)
      }

    });

  }
  else if (arr.length === 2) {
    arr[0].forEach((val) => {
      if (arr[1].includes(val)) {
        matchingIndexes.push(val)
      }

    });


  }
  else {

    matchingIndexes.push(arr[0]) //juste pousser le tableau qui n'est pas vide
  }
  return matchingIndexes.flat();

}
```

Voici ce que fait le code :

La fonction prend trois tableaux en entrée, chacun représentant des index correspondants d'une feuille de calcul basée sur vos termes de recherche. Cependant, nous comprenons que les utilisateurs peuvent ne pas remplir tous les champs de recherche.

Pour gérer cela, la fonction crée d'abord un "tableau maître" contenant uniquement les tableaux non vides parmi les trois entrées. Pensez à cela comme à un filtrage de tous les résultats de recherche vides. `const arr = [arr1.length > 0 ? [...arr1] : "", arr2.length > 0 ? [...arr2] : "", arr3.length > 0 ? [...arr3] : ""].filter(String);`

Si le tableau maître se retrouve vide, cela signifie qu'aucune ligne ne correspond à aucun de vos termes de recherche – la fonction retourne simplement un tableau vide, indiquant qu'aucun résultat n'a été trouvé.

De même, si le tableau maître a moins d'éléments que le nombre total de termes de recherche que vous avez saisis, cela signifie une recherche **ET** incomplète. Dans ce cas, la fonction retourne un tableau vide, vous informant qu'aucun résultat ne correspond à tous les critères. `arr.length < numberOfInputFieldEntered`

Mais lorsque les trois tableaux ont des correspondances, la fonction commence son travail, elle parcourt le premier tableau, vérifiant méticuleusement si chaque valeur d'index existe dans les deuxième et troisième tableaux. Si c'est le cas, cet index est considéré comme une correspondance et ajouté à un tableau "matchingIndexes" séparé. Cela garantit que seules les lignes contenant tous vos termes de recherche sont incluses : `arr[0].forEach((val) => { if (arr[1].includes(val) && arr[2].includes(val)) { matchingIndexes.push(val)}`

Si seulement deux tableaux ont des correspondances, la fonction effectue une vérification plus simple, vérifiant si chaque valeur du premier tableau existe dans le deuxième. Toute correspondance est ajoutée à "matchingIndexes." `arr[0].forEach((val) => if (arr[1].includes(val)) { matchingIndexes.push(val)}`.

Sinon, si un seul tableau est présent, la fonction utilise simplement ce tableau directement.

En résumé, la fonction garantit que seules les lignes contenant tous vos termes de recherche choisis survivent – un outil puissant pour une récupération précise des données !

Ensuite, dans votre fichier **search.gs** juste après avoir déclaré la variable `hasIncludeAllSelected` pour la case à cocher, créez un compteur de valeurs de saisie.

```javascript
var numberOfInputFieldEntered = [clientName, description, quantity].filter(String).length;
```

Avec cela, nous avons maintenant des index pour les lignes de la recherche **ET**. Maintenant, continuez avec votre fonction `andSearch` et obtenez les données de ces index.

### Donner vie aux résultats de recherche

```javascript
function andSearch(name = null, description = null, quantity = null) {
//.... continuation de ci-dessus
  // obtenir les données des index des lignes
  const _2021SheetMatchingRows = fetchDataByRowIndexes(_2021Sheet, _2021SheetMatchingRowsIndexes)
  const _2022SheetMatchingRows = fetchDataByRowIndexes(_2022Sheet, _2022SheetMatchingRowsIndexes)
  const _2023SheetMatchingRows = fetchDataByRowIndexes(_2023Sheet, _2023SheetMatchingRowsIndexes)
}
```

Maintenant que nous avons les index des lignes correspondantes, il est temps de récupérer les données réelles. Entrez la fonction `fetchDataByRowIndexes`, résidant dans le fichier **utils**. Cet outil pratique sert de récupérateur de données, récupérant les informations basées sur les index fournis.

```javascript
/**
 * Fonction extrait les lignes des index+1 fournis, de l'onglet de la feuille de calcul donné.
 * @param {Spreadsheet} sheet - feuille à rechercher
 * @param {Array<number>} indexes - index des lignes à extraire les valeurs.
 * @returns {Array<Array<Srting>>} - Tableaux de lignes imbriquées dans les index de la feuille donnée.
 */
function fetchDataByRowIndexes(sheet = _2021Sheet, indexes = []) {
  // console.log("Inside fetchDataByRowIndexes() provided indexes are:" + indexes)

  if (indexes.length < 1) return [];

  const data = sheet.getDataRange().getValues();
  const newData = [];

  for (let i = 0; i < indexes.length; i++) {
    newData.push([...data[indexes[i]], `${sheet.getName()} - ${indexes[i] + 1}`])
  }
  // console.log("Inside fetchDataByRowIndexes() data from procvided indexes:" + newData)
  return newData;
}
```

Les données récupérées ne sont pas simplement déversées dans la feuille de recherche – elles reçoivent une touche spéciale. La fonction ajoute une valeur supplémentaire pour la colonne nommée `Sprd Name - Row Indexes` avec ``${sheet.getName()} - ${indexes[i] + 1}`` . 

Cette colonne agit comme une carte routière, affichant à la fois le nom de la feuille de calcul d'origine et l'index de ligne correspondant pour chaque résultat. Ainsi, d'un coup d'œil, vous savez exactement d'où provient chaque morceau de données.

Rappelons que cette information supplémentaire est ajoutée comme dernière colonne dans la feuille de recherche. Avec ce contexte précieux, les résultats de recherche deviennent encore plus informatifs et plus faciles à naviguer.

### Comment supprimer les doublons pour assurer la précision

L'étape suivante consiste à s'assurer que nos résultats de recherche sont exempts de doublons, peu importe la feuille dont ils proviennent. Après tout, qui veut voir le même élément deux fois ? Ajoutez donc ce code dans la fonction `andSearch` :

```javascript
//.. continue à l'intérieur de la fonction andSearch
 // filtrer les lignes en double
  const _2021SheetMatchingUniqueRows = filterDuplicateRows(_2021SheetMatchingRows);
  const _2022SheetMatchingUniqueRows = filterDuplicateRows(_2022SheetMatchingRows);
  const _2023SheetMatchingUniqueRows = filterDuplicateRows(_2023SheetMatchingRows);
```

Pour créer cette fonction, retournons au fichier **utils.gs**.

```javascript
/**
 * Prend les données en double qui peuvent avoir résulté de différentes recherches de colonnes individuelles et ne retourne que les lignes uniques 
 * dans chaque colonne des résultats de recherche.
 * @param {Array<String>} arr 
 * @returns {Array<String>}- [[],[]]
 */
function filterDuplicateRows(arr) {
  if (arr.length < 1) return [];
  const delimiter = "*---*--*";
  // console.log("Inside filterDuplicateRows() arr to check:" + arr)

  const strArr = arr.map(row => row.join(delimiter)).flat();
  // console.log("Inside filterDuplicateRows() strArr:" + strArr)

  const uniqueArrays = [...new Set(strArr)].map(str => str.split(delimiter))
  // console.log("Inside filterDuplicateRows() uniqueArrays:" + uniqueArrays)

  return uniqueArrays;

}
```

Voici ce que nous avons fait :

* **Création d'une empreinte unique :** Nous avons commencé par créer un "délimiteur" spécial, une combinaison de caractères très improbable d'apparaître dans vos données réelles. Pensez à cela comme une étiquette unique pour chaque ligne.`const delimiter = "*---*--*";`
* **Joindre les forces :** Ensuite, nous avons mappé chaque ligne, joignant ses éléments avec ce délimiteur pour créer une seule chaîne. Cela nous permet de comparer les chaînes pour l'unicité au lieu des points de données individuels.`const strArr = arr.map(row => row.join(delimiter)).flat();`
* **Détective de doublons :** Nous avons exploité la puissance de l'objet [Set](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) de JavaScript, renommé pour sa capacité à contenir uniquement des valeurs uniques. En convertissant notre tableau de chaînes en un Set, nous supprimons efficacement toute entrée identique : `[...new Set(strArr)]`
* **Retour à nos racines :** Enfin, nous avons converti les chaînes uniques en un tableau de tableaux, en les divisant à l'aide du même délimiteur que nous avons utilisé précédemment. Cela nous donne un ensemble propre et sans doublons de résultats. `map(str => str.split(delimiter))`

**Note :** Cette unicité est basée sur la valeur combinée "`Sprd Name - Row Indexes`", assurant une véritable unicité à travers les feuilles de calcul. Sans cela, des doublons peuvent exister naturellement.

Avec cette étape finale, nous avons obtenu des résultats de recherche précis et rationalisés, prêts à être combinés et présentés à partir de la fonction `andSearch`.

```javascript
// à l'intérieur de la fonction andSearch, ajoutez à la fin

  const andSearchResult = [..._2023SheetMatchingUniqueRows, ..._2022SheetMatchingUniqueRows, ..._2021SheetMatchingUniqueRows]

  if (andSearchResult.length < 0) return;
  return andSearchResult;
}
```

Trouvez la fonction `andSearch` complète ci-dessous.

```javascript
/**
 * Effectue une recherche "ET" pour les mots-clés donnés dans leurs colonnes respectives Nom, Description et Quantité pour 
 * les onglets 2021, 2022, 2023. Retourne de nouveaux tableaux imbriqués pour les résultats de recherche à remplir dans la feuille de calcul de recherche.
 * @param {String} name 
 * @param {String} description 
 * @param {String} quantity 
 * @returns {Array<Array<String>>?} - [[],[],[]]
 */
function andSearch(name = null, description = null, quantity = null) {

  // obtenir l'index correspondant pour chaque feuille.
  const _2021SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2021Sheet, nameRangeNotation, name);
  const _2021SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2021Sheet, quantityRangeNotation, quantity);
  const _2021SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2021Sheet, descriptionRangeNotation, description);


  const _2022SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2022Sheet, nameRangeNotation, name);
  const _2022SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2022Sheet, quantityRangeNotation, quantity);
  const _2022SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2022Sheet, descriptionRangeNotation, description);

  const _2023SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2023Sheet, nameRangeNotation, name);
  const _2023SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2023Sheet, quantityRangeNotation, quantity);
  const _2023SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2023Sheet, descriptionRangeNotation, description);


  // index correspondants des lignes dans la recherche ET
  const _2021SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2021SheetNameSearchIndexes, _2021SheetQuantitySearchIndexes, _2021SheetDescriptionSearchIndexes);
  const _2022SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2022SheetNameSearchIndexes, _2022SheetQuantitySearchIndexes, _2022SheetDescriptionSearchIndexes);
  const _2023SheetMatchingRowsIndexes = filterRowsIndexesWithAllSearchTerms(_2023SheetNameSearchIndexes, _2023SheetQuantitySearchIndexes, _2023SheetDescriptionSearchIndexes);

  // obtenir les données des index des lignes
  const _2021SheetMatchingRows = fetchDataByRowIndexes(_2021Sheet, _2021SheetMatchingRowsIndexes)
  const _2022SheetMatchingRows = fetchDataByRowIndexes(_2022Sheet, _2022SheetMatchingRowsIndexes)
  const _2023SheetMatchingRows = fetchDataByRowIndexes(_2023Sheet, _2023SheetMatchingRowsIndexes)

  // filtrer les lignes en double
  const _2021SheetMatchingUniqueRows = filterDuplicateRows(_2021SheetMatchingRows);
  const _2022SheetMatchingUniqueRows = filterDuplicateRows(_2022SheetMatchingRows);
  const _2023SheetMatchingUniqueRows = filterDuplicateRows(_2023SheetMatchingRows);


  const andSearchResult = [..._2023SheetMatchingUniqueRows, ..._2022SheetMatchingUniqueRows, ..._2021SheetMatchingUniqueRows]

  if (andSearchResult.length < 0) return;

  return andSearchResult;

}
```

### Mettre le tout ensemble – Afficher vos résultats de recherche

Maintenant que nous pouvons récupérer les résultats de recherche basés sur vos critères "ET", il est temps de les intégrer dans votre fonction `search`. 

Nous allons continuer là où nous nous sommes arrêtés. Dans le bloc `if`, ajoutez le code suivant.

```javascript
 if (hasIncludeAllSelected) {
      //effectuer une recherche ET
      const newData = andSearch(clientName, description, quantity);
      // ..........................
      // nouveau morceau de code 
       status = fillSearchWithResults(searchSheet.getDataRange().getValues(), newData)
       // ................................................
}
```

Créons une nouvelle fonction, `fillSearchWithResults`, résidant dans le fichier **utils.gs** :

```javascript
/**
 * Pour remplir la feuille de recherche avec des valeurs
 * @param {Array<Array<Srting>>}  oldData - données précédentes des résultats de recherche
 * @param {Array<Array<Srting>>}  newData - nouveaux résultats de recherche à remplir
 */
function fillSearchWithResults(oldData, newData) {
  // console.log("Inside fillSearchWithResults() old data:", oldData.length);
  if (oldData.length >= 8) {
    searchSheet.getRange(8, 1, oldData.length - 7, 9).clear(); // effacer jusqu'aux dernières données remplies
  }
  SpreadsheetApp.flush();
  Utilities.sleep(1000);
  // console.log("Inside fillSearchWithResults() new Data:", newData);
  if (newData.length < 1) return 400;
  searchSheet.getRange(8, 1, newData.length, 9).setValues(newData);
  return 200;
}
```

La fonction prend deux entrées clés :

* **Données actuelles de la feuille de recherche :** Cela représente les informations existantes affichées dans votre feuille de recherche.
* **Nouveaux résultats de recherche :** Ce sont les nouvelles données récupérées en utilisant les fonctions expliquées précédemment.

Voici ce qui se passe étape par étape :

1. **Nettoyer le pont :** Si un résultat de recherche précédent existe (à partir de la ligne 8), la fonction le supprime pour faire de la place aux nouvelles découvertes.  `if (oldData.length >= 8) { searchSheet.getRange(8, 1, oldData.length - 7, 9).clear(); }`
2. **Résultats vides ? Pas de problème :** Si les résultats de recherche nouvellement récupérés sont vides, la fonction retourne un code spécial : 400. Ce code, que nous utiliserons plus tard, indique à l'utilisateur qu'aucune donnée correspondante n'a été trouvée. `if (newData.length < 1) return 400`
3. **Temps d'affichage des données ! :** S'il y a effectivement des résultats, la fonction les enregistre dans la feuille de recherche, à partir de la ligne 8. De plus, elle retourne un code différent : 200. Ce code signifie une opération réussie, et nous l'utiliserons pour montrer des messages de succès à l'utilisateur.

Avec cette dernière pièce en place, vos recherches "ET" apporteront facilement les données pertinentes à portée de main, présentées proprement dans votre feuille de recherche. 

### Comment utiliser la recherche OU pour trouver des données qui correspondent à un terme quelconque

Notre voyage continue ! Après avoir configuré la recherche "ET", nous pouvons maintenant maîtriser la recherche "OU", vous permettant de trouver des données contenant l'un de vos termes spécifiés.

Dans le bloc `else` de la fonction `search`, nous avons la fonction `orSearch`. Son but est de parcourir vos données et d'identifier les lignes contenant au moins l'un de vos termes de recherche. 

Pensez à cela comme à lancer un filet plus large, capturant des correspondances qui répondent à l'un de vos critères.

```javascript
  else {
      //effectuer une recherche OU
      let newData = orSearch(clientName, description, quantity);

      status = fillSearchWithResults(searchSheet.getDataRange().getValues(), newData)
}
```

Créez la fonction `orSearch` en dessous de `andSearch` dans le fichier de recherche.

```javascript
/**
 * Effectue une recherche "OU" pour les mots-clés donnés dans leurs colonnes respectives Nom, Description et Quantité pour 
 * les onglets 2021, 2022, 2023. Retourne de nouveaux tableaux imbriqués pour les résultats de recherche à remplir dans la feuille de calcul de recherche.
 * @param {String} name 
 * @param {String} description 
 * @param {String} quantity 
 * @returns {Array<Array<String>>?} - [[],[],[]]
 */
function orSearch(name = null, description = null, quantity = null) {
  // obtenir l'index correspondant pour chaque feuille.
  const _2021SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2021Sheet, nameRangeNotation, name);
  const _2021SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2021Sheet, quantityRangeNotation, quantity);
  const _2021SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2021Sheet, descriptionRangeNotation, description);

  const _2022SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2022Sheet, nameRangeNotation, name);
  const _2022SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2022Sheet, quantityRangeNotation, quantity);
  const _2022SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2022Sheet, descriptionRangeNotation, description);

  const _2023SheetNameSearchIndexes = name === "" ? [] : searchSheetByColumn(_2023Sheet, nameRangeNotation, name);
  const _2023SheetQuantitySearchIndexes = quantity === "" ? [] : searchSheetByColumn(_2023Sheet, quantityRangeNotation, quantity);
  const _2023SheetDescriptionSearchIndexes = description === "" ? [] : searchSheetByColumn(_2023Sheet, descriptionRangeNotation, description);

  // obtenir les valeurs de ces index
  const _2021SheetNameSearch = fetchDataByRowIndexes(_2021Sheet, _2021SheetNameSearchIndexes);
  const _2021SheetQuantitySearch = fetchDataByRowIndexes(_2021Sheet, _2021SheetQuantitySearchIndexes);
  const _2021SheetDescriptionSearch = fetchDataByRowIndexes(_2021Sheet, _2021SheetDescriptionSearchIndexes);

  const _2022SheetNameSearch = fetchDataByRowIndexes(_2022Sheet, _2022SheetNameSearchIndexes);
  const _2022SheetQuantitySearch = fetchDataByRowIndexes(_2022Sheet, _2022SheetQuantitySearchIndexes);
  const _2022SheetDescriptionSearch = fetchDataByRowIndexes(_2022Sheet, _2022SheetDescriptionSearchIndexes);

  const _2023SheetNameSearch = fetchDataByRowIndexes(_2023Sheet, _2023SheetNameSearchIndexes);
  const _2023SheetQuantitySearch = fetchDataByRowIndexes(_2023Sheet, _2023SheetQuantitySearchIndexes);
  const _2023SheetDescriptionSearch = fetchDataByRowIndexes(_2023Sheet, _2023SheetDescriptionSearchIndexes);



  // filtrer les lignes en double
  const _2021SheetMatchingUniqueRows = filterDuplicateRows([..._2021SheetNameSearch, ..._2021SheetQuantitySearch, ..._2021SheetDescriptionSearch]);
  const _2022SheetMatchingUniqueRows = filterDuplicateRows([..._2022SheetNameSearch, ..._2022SheetQuantitySearch, ..._2022SheetDescriptionSearch]);
  const _2023SheetMatchingUniqueRows = filterDuplicateRows([..._2023SheetNameSearch, ..._2023SheetQuantitySearch, ..._2023SheetDescriptionSearch]);

  const orSearchResult = [..._2021SheetMatchingUniqueRows, ..._2022SheetMatchingUniqueRows, ..._2023SheetMatchingUniqueRows]

  if (orSearchResult.length < 0) return;

  return orSearchResult;

}
```

Maintenant, ne soyez pas surpris si certaines choses semblent familières ! La structure globale de la fonction `orSearch` ressemble à son homologue "ET". Cependant, une différence clé les distingue :

Puisqu'une recherche "OU" nécessite seulement un terme correspondant, nous pouvons nous débarrasser de la fonction `filterRowsIndexesWithAllSearchTerms`. Rappelez-vous que cette fonction garantissait que tous les termes étaient présents, ce qui n'est pas le cas ici.

En essence, la fonction `orSearch` fonctionne en parcourant chaque terme de recherche et ses index correspondants. Pour chaque terme, elle récupère les données de la feuille de calcul en utilisant la fonction familière `fetchDataByRowIndexes`. 

Enfin, elle fusionne les données récupérées pour tous les termes, créant un ensemble unifié de résultats, même s'ils proviennent de différentes feuilles de calcul.

Avec cet outil puissant dans votre arsenal, vous pouvez découvrir des points de données qui n'auraient peut-être pas surfacé avec une recherche "ET", élargissant vos capacités de recherche et enrichissant votre expérience d'exploration de données.

### Tenir les utilisateurs informés – Messages toast pour une recherche sans couture

Maintenant que nos fonctions de recherche sont complètes, ajoutons un élément crucial : le retour d'information utilisateur ! Après tout, tenir les utilisateurs informés tout au long du processus de recherche conduit à une expérience plus fluide.

Pour éviter toute confusion, remplacez la fonction de recherche par celle-ci :

```javascript
/**
 * La fonction principale assignée au bouton de recherche dans la feuille de calcul. Elle orchestrer l'opération de recherche.
 */
function search() {
  try {
    SpreadsheetApp.getActiveSpreadsheet().toast("Recherche dans votre base de données...", 'Recherche');
   
    let status;

    if (hasIncludeAllSelected) {
      //effectuer une recherche ET
      const newData = andSearch(clientName, description, quantity);



      status = fillSearchWithResults(searchSheet.getDataRange().getValues(), newData)
      // console.log(status);
      if (status === 400) { throw new Error(SEARCH_STATUS.SEARCH_FAILURE); }
    }
    else {
      //effectuer une recherche OU
      let newData = orSearch(clientName, description, quantity);

      status = fillSearchWithResults(searchSheet.getDataRange().getValues(), newData)
      // console.log(status);

      if (status === 400) { throw new Error(SEARCH_STATUS.SEARCH_FAILURE); }
    }

    if (status === 200) {
      SpreadsheetApp.getActiveSpreadsheet().toast(SEARCH_STATUS.SEARCH_SUCCESFULL, 'Succès');
    }

  } catch (e) {
    // console.log(e)
    if (e.Error === SEARCH_STATUS.SEARCH_FAILURE) {
      SpreadsheetApp.getActiveSpreadsheet().toast(SEARCH_STATUS.SEARCH_FAILURE, 'Non trouvé !');

    } else {
      SpreadsheetApp.getActiveSpreadsheet().toast(e, 'Erreur !');

    }

  }
}
```

Nous allons utiliser la méthode [toast](https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet#toastmsg,-title) fournie par SpreadsheetApp pour afficher des messages brefs et non intrusifs directement dans l'interface de la feuille de calcul. Voici ce que nous allons accomplir :

**Recherche initiée :** Dès que l'utilisateur clique sur le bouton de recherche, un message toast apparaît : "Recherche dans votre base de données..." Cela leur indique que la recherche est en cours, évitant toute confusion ou attente inutile. `SpreadsheetApp.getActiveSpreadsheet().toast("Recherche dans votre base de données...", 'Recherche');`

**Histoires de succès :** Si la recherche retourne un résultat (indiqué par un code de statut de 200), un message toast positif apparaît : "La recherche a réussi !" Cela confirme l'achèvement de l'opération et rassure l'utilisateur que des données pertinentes ont été trouvées.  `if (status === 200) { SpreadsheetApp.getActiveSpreadsheet().toast(SEARCH_STATUS.SEARCH_SUCCESFULL, 'Succès'); }`

**Trouvailles vides :** Bien que ce ne soit pas techniquement une erreur, un résultat de recherche vide (code de statut de 400) déclenche un message légèrement différent : "Aucun élément trouvé avec les critères donnés." Cela informe l'utilisateur du résultat sans causer d'alarme. `if (status === 400) { throw new Error(SEARCH_STATUS.SEARCH_FAILURE); }`

Voici ce qui se passe en coulisses :

```javascript
const SEARCH_STATUS = {
  SEARCH_SUCCESFULL: "La recherche a réussi !",
  SEARCH_FAILURE: "Aucun élément trouvé avec les critères donnés.",
}
```

* Un "enum" appelé `SEARCH_STATUS` dans le fichier **utils.gs** stocke ces chaînes de messages pour un accès et une maintenance faciles.
* Un "bloc catch" gère toute erreur inattendue, garantissant que l'utilisateur reçoit un retour d'information approprié même dans des situations inhabituelles.

Avec ces messages toast en place, votre fonctionnalité de recherche devient plus conviviale et transparente. N'oubliez pas, une communication claire conduit à une expérience utilisateur agréable !

### Mettre le tout ensemble – Tester votre formulaire de recherche

Maintenant que vous avez construit vos puissantes fonctions de recherche, il est temps de les voir en action ! Suivez ces étapes pour tester votre formulaire de recherche directement dans votre feuille de calcul :

1. **Enregistrer vos scripts :** Assurez-vous d'avoir enregistré tous vos fichiers de code (**utils.gs** et **search.gs**) avant de continuer.
2. **Assigner la fonction de recherche :** Faites un clic droit sur le bouton Rechercher dans votre formulaire et sélectionnez "Assigner un script". Dans la fenêtre contextuelle, tapez le nom de la fonction `search` et cliquez sur "OK". Cela lie le bouton à votre code.
3. **Prêt, à vos marques, cherchez :** Dans votre feuille de calcul, expérimentez différentes combinaisons de recherche. Essayez d'entrer des termes dans diverses combinaisons pour voir comment les recherches ET et OU produisent différents résultats.

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1707047218515/d6e37765-ad85-4b08-ac8f-b62f80148a1e.png)
_Assigner une fonction à un bouton dans Google Sheets_

### Félicitations ! Vous avez construit un moteur de recherche puissant dans Google Sheets !

Vous avez réussi à accomplir un exploit impressionnant : créer un moteur de recherche personnalisé dans vos feuilles de calcul Google. Faisons un récapitulatif de vos réalisations :

* **Formulaire de recherche fluide :** Vous avez créé un formulaire de recherche convivial directement dans votre feuille de calcul, simplifiant l'exploration des données.
* **Puissance scriptable :** Vous avez exploité la puissance d'Apps Script pour développer des fonctions qui gèrent diverses opérations de recherche en coulisses.
* **Maîtrise de ET & OU :** Vous avez implémenté les fonctionnalités de recherche ET et OU, offrant aux utilisateurs une flexibilité pour trouver des données pertinentes.
* **Correspondance précise :** Vous avez conçu une fonction qui sélectionne les lignes contenant tous les termes de recherche spécifiés, garantissant des résultats précis.
* **Suppression des doublons :** Vous avez mis en place un mécanisme pour éliminer les entrées en double, gardant vos résultats de recherche propres et concis.
* **Retour d'information informatif :** Vous avez intégré des messages toast conviviaux pour informer les utilisateurs sur l'avancement et les résultats de la recherche.

### Explorer les options de personnalisation

Vous avez construit un moteur de recherche fantastique, mais rappelez-vous, le voyage ne s'arrête pas ici ! Avec quelques ajustements, vous pouvez adapter cet outil pour qu'il corresponde parfaitement à vos besoins et flux de travail spécifiques. Voici quelques possibilités passionnantes à considérer :

**Diversifier vos données :** Libérez-vous des contraintes d'une seule feuille de calcul ! Explorez l'intégration avec diverses sources de données comme les systèmes de gestion des stocks, les bases de données fiscales, ou même les avis de restaurants. Avec quelques ajustements à votre code, vous pouvez débloquer une richesse d'informations à travers différentes plateformes.

**Entrées de recherche dynamiques :** Besoin de plus de flexibilité dans vos critères de recherche ? Envisagez d'ajouter ou de supprimer des champs de saisie en fonction de vos besoins évolutifs. Cela permet des recherches plus personnalisées et rationalise votre processus d'exploration de données.

**Journaux de recherche détaillés :** Gardez une trace de votre historique de recherche ! Implémentez une boîte de journal pour enregistrer automatiquement vos derniers termes de recherche et le nombre de résultats trouvés. Cela peut être inestimable pour revisiter les recherches passées et analyser les tendances.

**L'apparence visuelle compte :** Améliorez l'expérience utilisateur en donnant à votre formulaire de recherche un lifting visuel. Jouez avec les couleurs, les polices et la mise en page pour créer une interface plus engageante et intuitive.

**Optimisations de vitesse :** Chaque seconde compte ! Explorez des moyens d'optimiser vos fonctions de recherche pour des temps de réponse plus rapides. Cela peut impliquer l'affinement du code, l'indexation des données ou l'utilisation de stratégies de mise en cache.

**Dompter les grands ensembles de données :** Travailler avec des bases de données massives ? Ne vous inquiétez pas, vous avez des options ! Implémentez une logique pour surmonter la limite de temps d'exécution de 6 minutes des fonctions Google Apps Script. 

En explorant ces avenues, vous pouvez transformer votre fonction de recherche de base en un outil puissant et personnalisé d'exploration de données. N'oubliez pas, les possibilités sont infinies !

PS : À quel point serez-vous plus productif (ou procrastinant) avec cette nouvelle capacité ?

Je suis Nibesh Khadka. Partagez ce blog et aimez la vidéo si cela a été utile ! Trouvez plus de mes contenus sur [Script-Portal](https://medium.com/script-portal) (Medium) et sur ma chaîne YouTube : [CodingWithNibesh](https://youtube.com/@codingWithNibesh).