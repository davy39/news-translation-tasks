---
title: Apprendre les bases de Google Apps Script en créant un jeu de Morpion
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-05-16T16:58:37.000Z'
originalURL: https://freecodecamp.org/news/learn-google-apps-script-basics-by-building-tic-tac-toe
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Tic-Tac-Toe-Google-Sheet2.png
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: Apprendre les bases de Google Apps Script en créant un jeu de Morpion
seo_desc: 'Google Sheets are powerful, and Apps Script makes them even more versatile
  and useful.

  Yes, you can use them for finance dashboards, personal budgets, and project management
  (and we''ll cover these as future topics). But in this article, I''ll go throu...'
---

Google Sheets est puissant, et Apps Script le rend encore plus polyvalent et utile.

Oui, vous pouvez les utiliser pour des tableaux de bord financiers, des budgets personnels et la gestion de projet (et nous aborderons ces sujets dans de futurs articles). Mais dans cet article, je vais passer en revue les bases d'Apps Script en créant un plateau de jeu de Morpion simple et jouable.

Voici le [lien vers la feuille de calcul](https://docs.google.com/spreadsheets/d/1I3mjQgfaZ9hFuUui6irpTdXg17TZXfK_jjtMvPrlGlM/edit?usp=sharing) que nous allons créer si vous souhaitez la consulter pendant que vous suivez les instructions :

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQF91mJiUd4F5w/article-inline_image-shrink_1500_2232/0/1684162312276?e=1689811200&v=beta&t=ue0QHmYwX0I7oqirS6GZx66YXl5y_-zSkA6iPdDGKBM)
_Allons-y gif_

### Vidéo de démonstration disponible

Si vous souhaitez consulter une vidéo de démonstration de la feuille Google, la voici :

%[https://youtu.be/LYN3Cvlsflg]

## Installation du projet

Créez une nouvelle feuille Google en allant dans votre Google Drive et en sélectionnant NOUVEAU -> Google Sheet ou en tapant simplement sheets.new dans la barre d'URL de votre navigateur.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQGtAhxBgZCiPQ/article-inline_image-shrink_1500_2232/0/1684161563448?e=1689811200&v=beta&t=5TuDNK0iSggXlKST3fzl-wv5JV04qwbYizc3ev8F51E)
_capture d'écran de Google Drive_

Puisque c'est un plateau de jeu, nous allons lui donner un peu de formatage pour qu'il soit beau, ajouter une validation des données et une mise en forme conditionnelle pour ajouter de la fonctionnalité au jeu, et créer des boutons utilisables pour notre tableau de scores.

Voici ce que nous allons obtenir :

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQFmLTdzhlehew/article-inline_image-shrink_1000_1488/0/1684161671894?e=1689811200&v=beta&t=2nJ0ZTnaCo2Dtq7u3zzSP7av2MHjtPtAyVp7dRQUwvY)
_capture d'écran de la feuille Google de Morpion_

Supprimons les lignes de grille, ajoutons des bordures au plateau de jeu et au tableau de scores, et définissons une police alternative pour le plateau.

Pour supprimer les lignes de grille, sélectionnez Affichage -> Afficher -> Lignes de grille pour décocher cette option.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQFsYtEPWEAxjA/article-inline_image-shrink_400_744/0/1684161946643?e=1689811200&v=beta&t=r6rUrzy6NSj-KQDb0o7Jx64N_u3CmTWQJxr_KaTAtII)
_capture d'écran des options d'affichage de Google Sheets_

Pour obtenir une grille carrée agréable avec de grands X et O, j'ai défini la hauteur des lignes et la largeur des colonnes des lignes 2 à 4 et des colonnes B à D en les surlignant, en cliquant avec le bouton droit et en sélectionnant les options de redimensionnement.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQGJGcSpYb2KyA/article-inline_image-shrink_1000_1488/0/1684162096408?e=1689811200&v=beta&t=uU37mbBSZBSMgi25ICD9r3hzAyCkepCmXAYx2ebCKsw)
_capture d'écran du redimensionnement des colonnes dans Google Sheets_

J'ai choisi 150 pixels pour la hauteur et la largeur. Vous devrez faire cela séparément – vous ne pouvez pas changer à la fois la hauteur des lignes et la largeur des colonnes en même temps.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQHzgbT4rS6f6w/article-inline_image-shrink_1000_1488/0/1684162162590?e=1689811200&v=beta&t=J-yExtOPV3icc6-YhGUmWESA0FUMzaJQu6N4qemzCwU)
_capture d'écran du redimensionnement des colonnes dans Google Sheets_

Pour la taille de la police du plateau, sélectionnez 100, et pour la police, j'utilise Lexend. Vous pouvez ajouter des polices Google supplémentaires à partir du menu déroulant de la barre d'outils :

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQF6Ss_zEGVSug/article-inline_image-shrink_1500_2232/0/1684162246754?e=1689811200&v=beta&t=R548yqr57k0ffuORMeqbZ3fmhQEWYL_QCiJv1EOGNo4)
_capture d'écran des options de polices dans Google Sheets_

Ajoutez une bordure au plateau et aux zones du tableau de scores en surlignant les cellules, puis en sélectionnant les options de bordure dans la barre d'outils.

Cliquez et faites glisser sur les cellules pour sélectionner toute la plage, et maintenez le bouton CTRL enfoncé pour cliquer et faire glisser une deuxième zone. Vous pouvez styliser ces zones en même temps.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQHGcJin6dOdtw/article-inline_image-shrink_1000_1488/0/1684162477801?e=1689811200&v=beta&t=lfxyTUvqmv7KjhZ5B2X9eDeVw9bWVm5rNiCBmReF6OE)
_capture d'écran des options de bordure dans Google Sheets_

## Validation des données

Surlignez le plateau de jeu (B2:D4) et sélectionnez Données -> Validation des données dans le menu.

Cela nous permet de sélectionner Liste déroulante comme critère et d'ajouter X et O comme les deux options à sélectionner.

Ensuite, cliquez sur Options avancées et sélectionnez Rejeter la saisie si les données sont invalides, et texte brut pour le style d'affichage. Cela gardera les puces et les poignées de la liste déroulante de ne pas encombrer le plateau de jeu.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQGj3dQDQ4QGuQ/article-inline_image-shrink_1500_2232/0/1684162681967?e=1689811200&v=beta&t=_HfNZ0C9L7tWucbWMMpzKf9gItYhkMP3G1cRlVGioxQ)
_capture d'écran du menu de validation des données dans Google Sheets_

## Mise en forme conditionnelle

Nous utiliserons également la mise en forme conditionnelle pour notre plateau de jeu. Nous devons vérifier toutes les conditions de victoire, et si l'un des joueurs obtient trois cases alignées, nous mettrons en surbrillance ces cellules.

En gardant le plateau de jeu surligné, sélectionnez Format -> Mise en forme conditionnelle.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQFJwi61h00_3g/article-inline_image-shrink_1000_1488/0/1684162938075?e=1689811200&v=beta&t=rdKBw21dV6Q82CgxNfiOG8Zg9N3fKXA135SauhAAYhA)
_capture d'écran de la fenêtre de format dans Google Sheets_

Il y a huit conditions que nous vérifierons pour trois cases alignées : trois horizontalement, trois verticalement et deux en diagonale.

Mais nous n'avons besoin d'écrire que quatre formules (deux pour les diagonales, une pour l'horizontale et une pour la verticale) puisque nous pouvons utiliser des signes dollar ($) pour faire glisser la formule vers le bas et vers la droite pour celles-ci.

Pour les trois cases alignées verticalement :

```javascript
//Appliquer à la plage B2:D2 
=ET($B2=$C2,$B2=$D2,ESTTEXTE($B2))
```

Pour les trois cases alignées horizontalement :

```javascript
//Appliquer à la plage B2:D2
=ET(B$2=B$3,B$2=B$4,ESTTEXTE(B$3))
```

Pour les diagonales, nous devons les définir séparément :

```javascript
//Appliquer à la plage B2, C3, D4 
=ET($B$2=$C$3,$B$2=$D$4,ESTTEXTE($B$2))

//Appliquer à la plage B4, C3, D2 
=ET($B$4=$C$3,$B$4=$D$2,ESTTEXTE($B$4))
```

Nous testons l'égalité de chaque cellule et si il y a quelque chose dans la cellule avec la fonction `=ESTTEXTE()`. En enveloppant chaque élément dans une fonction `=ET()`, nous n'appliquerons le formatage que si toutes les conditions sont remplies.

J'ai sélectionné un fond vert pour la mise en forme conditionnelle.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQERGL76FWm8nA/article-inline_image-shrink_1500_2232/0/1684163627050?e=1689811200&v=beta&t=9C0IASvwa_KE1wm68iez-FxJ2YjmuwDRB42-ASak_5s)
_capture d'écran de la fenêtre de mise en forme conditionnelle_

## Apps Script

Maintenant, pour la logique du tableau de scores. Ouvrons Apps Script en sélectionnant Extensions -> Apps Script dans le menu :

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQHtQjZ3mujfUQ/article-inline_image-shrink_1500_2232/0/1684178999142?e=1689811200&v=beta&t=N5Wvx0y2md14-2Ih_PGj1_lHbKpW2mcEIPRNnRsvUAI)
_capture d'écran du menu Apps Script_

Nous allons écrire quatre fonctions pour gérer notre logique :

1. `xScore()` incrémentera le score de X dans le tableau de scores
2. `oScore()` incrémentera le score de O dans le tableau de scores
3. `clearBoard()` effacera le plateau mais gardera les scores
4. `reset()` effacera le plateau et remettra les scores à zéro

Pour rendre les choses plus lisibles, définissons quelques plages nommées.

Surlignez à nouveau le plateau de jeu et sélectionnez Données -> Plages nommées. Donnez à cette plage le nom **Board**. Faites de même pour les cellules G4 et H4 pour **xScore** et **oScore**, respectivement.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQHS7_YVdCFbog/article-inline_image-shrink_1500_2232/0/1684163925497?e=1689811200&v=beta&t=8-jk-X5iea045w1ZBkCqiExObkF6c4A572zR4dqIrI0)

Pour les scores, nous aurons exactement la même fonction pour chacun en utilisant seulement les deux plages différentes : xScore pour X et oScore pour O. Voici à quoi elles ressembleront en utilisant xScore comme exemple :

**`xScore()` & `oScore()`:**

```javascript
function xScore() {
    var sheet = SpreadsheetApp.getActive(); 
    var xScore = sheet.getRangeByName('xScore').getValue();
    sheet.getRangeByName('xScore').setValue(xScore+1); clearBoard();
}
```

* Ligne 1 : Cela définit une variable (nous ferons cela dans chaque fonction) pour la feuille de calcul active.
* Ligne 2 : Cela définit une variable pour xScore comme la valeur dans la plage nommée xScore (cellule G4)
* Ligne 3 : Cela définit une nouvelle valeur pour la cellule xScore comme celle qu'elle était plus 1.
* Ligne 4 : Cela exécute la fonction clearBoard() que nous allons écrire ensuite...

**`clearBoard()`:**

Cela effacera simplement le plateau de jeu mais laissera le tableau de scores intact.

```javascript
function clearBoard() {
    let sheet = SpreadsheetApp.getActive();
    let board = sheet.getRangeByName('Board');
    board.clearContent(); 
}
```

* Ligne 1 : Notre variable sheet à nouveau.
* Ligne 2 : Notre variable board. Cela récupère la plage B2:D4 que nous avons nommée 'Board'
* Ligne 3 : Cette méthode intégrée `clearContent()` efface simplement tout dans ces cellules. Très simple.

**`reset()`:**

Maintenant, nous avons besoin d'une fonction pour remettre le tableau de scores et le plateau de jeu à leur état initial.

```javascript
function reset() {
    let sheet = SpreadsheetApp.getActive(); 
    sheet.getRangeByName('xScore').setValue(0);
    sheet.getRangeByName('oScore').setValue(0); clearBoard(); 
}
```

* Ligne 1 : notre feuille active
* Ligne 2 : nous récupérons notre plage xScore et définissons sa valeur à 0.
* Ligne 3 : nous faisons de même pour notre oScore
* Ligne 4 : nous exécutons la fonction reset pour gérer le plateau de jeu.

Et c'est tout ! Maintenant, nous pouvons exécuter l'une de ces fonctions depuis l'éditeur Apps Script et voir qu'elles fonctionnent.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQFUTfyjYKeECQ/article-inline_image-shrink_1000_1488/0/1684178952423?e=1689811200&v=beta&t=ek0cIfi0cCqZfWKM7q7ygA7n18pKwMD5wdqUVizCQjU)
_capture d'écran de l'exécution de code dans l'éditeur Apps Script_

## Comment créer des boutons

Il serait beaucoup plus agréable d'avoir des boutons dans notre feuille de calcul réelle pour pouvoir exécuter les fonctions.

Pour ce faire, nous allons dessiner un bouton puis lui assigner un script.

Sélectionnez Insertion -> Dessin dans le menu.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQEmlXrm9lNOjw/article-inline_image-shrink_1500_2232/0/1684179236609?e=1689811200&v=beta&t=wSn2IgbM2H6_flsNE0CecTzLqKj9K2ILIgCDL9N5x9w)
_Capture d'écran du menu Insertion dans Google Sheets_

Vous pouvez dessiner ce que vous voulez, mais j'ai choisi le rectangle arrondi de base.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQFbc8Vp8xMAEw/article-inline_image-shrink_400_744/0/1684179297444?e=1689811200&v=beta&t=M7QO7ZdcylQ6W4grOmguGY3aI_S-G-cpAVWiJOiyMcc)
_Capture d'écran des formes dans le menu de dessins de Google Sheets_

Double-cliquez dans la forme pour ajouter du texte, et redimensionnez, recolorez, restylez selon vos besoins.

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQHSkIBOsRvNdg/article-inline_image-shrink_1000_1488/0/1684179429349?e=1689811200&v=beta&t=9G87KKPY_efHEOTU_K2POBbUzeSfFlbs5nG282Oo4Gc)
_Capture d'écran du bouton dans Google Sheets_

Une fois que vous avez créé votre bouton, cliquez sur Enregistrer et Fermer. Ensuite, redimensionnez et positionnez-le où vous le souhaitez dans la feuille Google. J'ai mis le mien juste sous le tableau de scores, et j'en ai fait un pour chaque score ainsi qu'un bouton de réinitialisation.

Enfin, pour faire fonctionner le bouton, cliquez sur les trois petits points en haut à droite du bouton et sélectionnez **assigner un script**. Ensuite, tapez le nom du script (sans les parenthèses).

![Aucun texte alternatif fourni pour cette image](https://media.licdn.com/dms/image/D5612AQGCHPMJ8FW-hw/article-inline_image-shrink_1500_2232/0/1684179559428?e=1689811200&v=beta&t=41p0tXKvG3Moj8bTJAI45nUhcZAUjhzPNoSbD_IP57I)
_Capture d'écran de l'assignation d'un script à un bouton dans Google Sheets_

Maintenant, tout ce que vous avez à faire est de cliquer sur l'un des boutons et le script assigné s'exécutera 🔥.

Deux notes :

1. La première fois que vous exécutez un script, une boîte de dialogue contextuelle apparaîtra vous demandant d'accepter les autorisations de sécurité. C'est un filet de sécurité pour vous assurer que vous savez que vous exécutez le code qui est écrit dans Apps Script, et pour l'examiner si vous ne l'avez pas écrit. Vous devrez cliquer à travers celles-ci et accepter le risque pour permettre son exécution.
2. Si vous devez déplacer un bouton après avoir assigné le script, vous pourriez être frustré lorsque le clic ne fait pas apparaître les trois points pour le menu et exécute uniquement le script. Pour contourner cela et permettre le déplacement et le menu à trois points, cliquez avec le bouton droit sur le bouton.

## Conclusion

J'espère que cela a été utile pour vous !

Veuillez vous abonner à [ma chaîne YouTube ici](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) pour plus de contenu comme celui-ci.

Passez une excellente journée !