---
title: Tutoriel Microsoft Excel – Comment créer des formules et des fonctions
subtitle: ''
author: Benny Ifeanyi Iheagwara
co_authors: []
series: null
date: '2022-09-08T15:17:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-microsoft-excel-formulas-and-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Green-Orange-and-Brown-Collage-Math-Quiz-Presentation.png
tags:
- name: excel
  slug: excel
- name: spreadsheets
  slug: spreadsheets
seo_title: Tutoriel Microsoft Excel – Comment créer des formules et des fonctions
seo_desc: "Spreadsheets aren't merely for arranging data into rows and columns. Most\
  \ of the time, you use them for data analysis as well. \nMicrosoft Excel is one\
  \ of the most widely used spreadsheet applications, especially in finance and accounting.\
  \ This is par..."
---

Les feuilles de calcul ne servent pas uniquement à organiser des données en lignes et en colonnes. La plupart du temps, vous les utilisez également pour l'analyse de données.

Microsoft Excel est l'une des applications de feuille de calcul les plus largement utilisées, en particulier dans les domaines de la finance et de la comptabilité. Cela est en partie dû à son interface utilisateur facile à utiliser et à la profondeur inégalée de ses fonctions.

Dans cet article, vous apprendrez :

* Ce que sont les formules Excel
* Comment écrire une formule dans Excel
* Ce que sont les fonctions Excel
* Comment travailler avec une fonction Excel
* Enfin, nous examinerons les fonctions dynamiques d'Excel.

# Que dois-je installer sur mon ordinateur pour suivre cet article ?

Pour suivre cet article, vous devez avoir Microsoft Excel installé sur votre ordinateur. Nous utiliserons un ordinateur Windows pour cet article.

# Comment puis-je installer Microsoft Excel sur mon ordinateur ?

Suivez ces étapes pour installer Microsoft Excel sur votre ordinateur Windows :

1. Connectez-vous à [www.office.com](https://www.office.com/) si vous n'êtes pas déjà connecté.
2. Connectez-vous avec le compte associé à votre abonnement [Microsoft 365](https://www.microsoft.com/en/microsoft-365?ocid=oo_support_mix_marvel_ups_support_railbanner_1000852&rtc=1). Vous pouvez également essayer [Office gratuitement](https://signup.live.com/signup?mkt=en-US&uiflavor=web&lw=1&fl=easi2&client_id=4345a7b9-9a63-4910-a426-35363201d503&wreply=https%3A%2F%2Fwww.office.com%2F%3Fauth%3D1%26from%3DOdotComFreeSignup).
3. Une fois connecté, sélectionnez « Installer Office » depuis la page d'accueil d'Office. Cela téléchargera automatiquement Microsoft Office sur votre ordinateur Windows.
4. Exécutez l'installateur pour configurer Microsoft Office et sélectionnez "Fermer" une fois terminé.
5. Une fois terminé, sélectionnez le bouton "Démarrer" (situé dans le coin inférieur gauche de votre écran) et tapez "Microsoft Excel".
6. Cliquez sur Microsoft Excel pour l'ouvrir.
7. Acceptez le contrat de licence, et commençons.

# Que sont les formules Excel ?

Une formule Excel est une expression qui effectue une opération basée sur la valeur d'une cellule ou d'une plage de cellules. Vous pouvez utiliser une formule Excel pour :

* Effectuer des opérations mathématiques simples telles que l'addition ou la soustraction.
* Effectuer une opération simple comme la concaténation de données catégorielles.

Il est important de comprendre deux choses : les formules Excel commencent toujours par le signe égal "=" et elles peuvent retourner une erreur si elles ne sont pas correctement exécutées.

# Quels opérateurs sont utilisés dans les formules Excel ?

Il existe quatre types différents d'opérateurs dans Excel : arithmétiques, de comparaison, de concaténation de texte et de référence. Mais pour la plupart des formules, vous utiliserez généralement ces trois-là :

### Opérateurs arithmétiques

<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">+</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Addition</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">-</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Soustraction</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">/</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Division</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">*</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Multiplication</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">^</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Exponentiation</span></p></td></tr></tbody></table>

### Opérateurs de comparaison

<table style="border:none;border-collapse:collapse;table-layout:fixed;width:468pt"><colgroup><col><col></colgroup><tbody><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Égal à</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&gt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Supérieur à</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Inférieur à</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&gt;=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Supérieur ou égal à</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;=</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Inférieur ou égal à</span></p></td></tr><tr style="height:0pt"><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">&lt;&gt;</span></p></td><td style="border-left:solid #000000 1pt;border-right:solid #000000 1pt;border-bottom:solid #000000 1pt;border-top:solid #000000 1pt;vertical-align:top;padding:5pt 5pt 5pt 5pt;overflow:hidden;overflow-wrap:break-word;"><p dir="ltr" style="line-height:1.2;margin-top:0pt;margin-bottom:0pt;"><span style="font-size:11pt;font-family:Arial;color:#000000;background-color:transparent;font-weight:400;font-style:normal;font-variant:normal;text-decoration:none;vertical-align:baseline;white-space:pre;white-space:pre-wrap;">Différent de</span></p></td></tr></tbody></table>

### Concaténation de texte

Ici, vous avez simplement le signe esperluette "&" pour joindre du texte.

# Comment puis-je créer une formule Excel ?

Prenons un scénario simple en utilisant l'un des opérateurs arithmétiques.

En mathématiques, pour additionner deux nombres, disons 20 et 30, vous calculerez cela en écrivant : 20 + 30 = 

Et cela vous donnera 50.

Dans Excel, voici comment cela se passe :

1. Tout d'abord, ouvrez une feuille de calcul Excel vierge.
2. Dans la cellule A1, tapez 20.
3. Dans la cellule A2, tapez 30.
4. Pour les additionner, tapez = 20 + 30 dans la cellule A3.

![Image](https://lh5.googleusercontent.com/ahFv4-tCq-5p6B9wWJwrfv-0glehpnu9gMnAw34pwCUh9hUVyw3p5aOu5ejIAnCPBDtw6g_CTOOWaEtap1ph2XP5nL9TkxVb2E5iV80tp6Tm73968jE3kyCPKaMkrVYpw1Mn4rYBxXMSrU5CzEkSlxNhBp-KiZLfEtDAOagAzGHa6RWO5yLaZsyevQ)
_Comment puis-je créer une formule Excel ?_

5. Ensuite, appuyez sur ENTRÉE sur votre clavier. Excel calculera instantanément cela et retournera 50.

![Image](https://lh6.googleusercontent.com/XGXatK9hD_imhCrF3wQ-NuzlOzCgW0TCysQ0vwtk-Xz8Wu-W5ZxIKf65DBbc0i5H2_ubVC4rBoiyVauMcOWdapOwqGwhANyNKhwS_us0CTFMBP76q2wP3HGksmsWvb8ebB6cLG_3RzWSp2vie7woGbTZTuMmaPsnwa5oFoP8gFNf6RwbJa4O-hnVzQ)
_Comment puis-je créer une formule Excel ? Addition de nombres dans Excel_

J'ai mentionné précédemment que chaque formule commence par le signe égal "=". C'est ce que je voulais dire. Pour écrire une formule, vous tapez le signe égal suivi des valeurs numériques. Cela s'applique également aux cas de soustraction, de division, de multiplication et d'exponentiation. 

Prenons un autre scénario simple en utilisant l'un des opérateurs de comparaison. Supposons que nous voulons savoir si 30 est supérieur à 40.

Dans Excel, voici comment nous le ferions :

1. Tapez =30>40
2. Appuyez sur ENTRÉE.

![Image](https://lh6.googleusercontent.com/j7NqF7FlQbtnSWU_QiE2pHtmsadofCUgJHkXKTEEp2miFXV24QjJMMyZrP-sVibNuM__jgW1szMEQjuFtz4gb9ZbOm6n5UtWtGNktWd3iOEcnbTFH4_4GftYs_FLySTkeWhA51MujOKvZGAkdYN96hzyGb86Na_dKhawPQFXRNtP7jI87Azo1FZ1qA)
_Comment puis-je créer une formule Excel ? Opérateurs de comparaison_

  
3.  Cela retournera FAUX car 30 n'est pas supérieur à 40. Excel utilise VRAI et FAUX pour les déclarations logiques, de la même manière que nous, humains, disons oui et non.

![Image](https://lh5.googleusercontent.com/rmJNrTzMCS3Qg0nIk-1DqURQuqfO2qF-0eqiF4RyAsM9lPDGtVyDpzsJryzN-7BXrv3qGbIhRjw2NGNKHiMVaHlWwnqVWigvlu35dqTUgHaxGshud8n3bdsnwrJ9cXPMLASLQDMKoAJqRjivuqgA_WQpYZaUMDq4T41LMJzgivLeqd5LN2_zrsmTrA)
_Comment puis-je créer une formule Excel ? Opérateurs de comparaison_

Enfin, prenons un autre scénario simple en utilisant l'opérateur de concaténation de texte – le signe esperluette "& ". Cela fonctionne avec vos types de données de chaîne et vous l'utilisez pour joindre du texte.

Supposons que nous avons "Bienvenue", "À", et "FreeCodeCamp" tous dans différentes cellules—A1, A2, et A3—de votre feuille de calcul. Nous taperions =A1&" "&A2&" "&A3 pour les joindre.

L'espace entre guillemets " " représente le fait que nous voulons un espace entre nos mots.

![Image](https://lh6.googleusercontent.com/_NuH8HoSTLRA4zTSGaCkcCwLKhjZVYy885wThXg_NgwYsyIDEk_6APoloy2wujJUNZUkXsBTFDr-dmO_x3B_4WU0XQUaBJGiNz6gTlPC3lqR2U5utRsK9S3R9yxoRi4U9N1zvH92LMW-F97cn5hx1_k09du0tYxFERxtg5w5Zl8M4Bw_HSyF8maq6w)
_Comment puis-je créer une formule Excel en utilisant le signe esperluette "&"_

Un autre conseil : la barre de formule montre la formule utilisée pour générer une valeur.

# Que sont les fonctions Excel ?

Les fonctions Excel sont des formules préétablies qui effectuent des calculs et des opérations mathématiques, statistiques et logiques en utilisant vos valeurs et arguments.

Pour les fonctions Excel, vous devez savoir que :

* Ce sont des formules, donc oui, elles commencent également par le signe égal "=".
* L'ordre est très important.

Il existe plus de 500 fonctions disponibles. Vous pouvez trouver toutes les fonctions Excel disponibles dans l'onglet Formules du Ruban.

![Image](https://lh5.googleusercontent.com/GL6J_F_ao0U-lmLQs8CCZHrjxGZz5l_zF9b7EAn6lirKVRx9YZ86PCw6UTrCFBFhPDaiEUBSpLA8fOZcj43CW7oDWYlcxjEHXMXe5cSphegI2HpdfjrJxoXaWcP8wCEK9gAV30rqE89Gd08y1pj5vI5JGSCfDgdUg8lxu2MT9S-KgnFahn5o-H2x7A)
_Toutes les formules et fonctions Excel disponibles_

Mais pourquoi utiliser une fonction lorsque vous pouvez simplement écrire une formule ?

Voici quelques avantages des fonctions Excel.

* Pour améliorer la productivité et l'efficacité.
* Pour simplifier les calculs complexes.
* Pour automatiser votre travail.
* Pour visualiser rapidement les données.

## De quoi sont composées les fonctions Excel ?

Contrairement aux formules, les fonctions Excel sont composées d'une structure avec des arguments que vous devez passer.

Chaque fonction :

* Commence par le signe égal "="
* A un nom. Certains exemples sont RECHERCHEV, SOMME, UNIQUE, et RECHERCHEX.
* Nécessite des arguments qui sont séparés par des virgules. Vous devez savoir que les points-virgules sont utilisés comme séparateurs dans des pays comme l'Espagne, la France, l'Italie, les Pays-Bas et l'Allemagne. Vous pouvez, cependant, changer cela via les paramètres d'Excel.
* Les arguments entre crochets [] sont optionnels
* A une parenthèse ouvrante et fermante.
* A une info-bulle d'argument qui vous montre ce que vous devez passer.

Il existe quelques exceptions. Par exemple,

* La fonction DATEDIF ne s'affiche pas dans Excel car ce n'est pas une fonction standard et donne des résultats incorrects dans quelques circonstances. Cependant, voici la syntaxe :

`DATEDIF(date_de_naissance, AUJOURDHUI(), "y")`

* Les fonctions comme PI(), ALEA(), MAINTENANT(), AUJOURDHUI() ne nécessitent aucun argument.

# Comment utiliser les fonctions Excel

Examinons quelques fonctions :

### Comment utiliser la fonction `SOMME()` dans Excel

Selon la documentation, la fonction SOMME additionne les valeurs. Voici la syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-315.png)
_Syntaxe de la somme Excel_

Supposons que nous avons une ligne de nombres de 1 à 10 et que nous voulons les additionner. Pour y parvenir, nous taperons simplement =SOMME(A1:A10). Le A1:A10 retourne simplement un tableau de nombres situés dans les cellules A1 à A10, c'est-à-dire A1, A2, et A3 jusqu'à A10.

![Image](https://lh3.googleusercontent.com/oj-2CwOiYRuzMhsH6oyy8zMFUCw9EpTPQWtLhkUbsbigzk-U6RG_dDG_aVeazYkgIQmuil80wG0N6_t3yk9oqF3EKjdSoREj8c-PqACBgOkZX763fMyM4oLKnGVharikQAFt0SNEvkxO1bnN67LQs3LLfQ-LW2R37IFVJGXz7KvJ1Wu_S7imz-0YsA)
_Comment utiliser la somme dans Excel_

Puisque le deuxième argument est optionnel, cela signifie qu'une somme(A10) retournera une valeur. Dans notre cas, elle retournera simplement 10 puisque A10 contient la valeur 10. Essayez-le.

Si vous écriviez cela en utilisant l'opérateur d'addition, vous auriez écrit :

=1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 

ou 

=A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 

Cela ne semble pas très productif ou efficace.

### Comment utiliser la fonction `AUJOURDHUI()` dans Excel

Selon la documentation, la fonction AUJOURDHUI affiche la date actuelle sur votre feuille de calcul. Elle ne nécessite également aucun argument. Voici la syntaxe :

![Image](https://lh3.googleusercontent.com/o0zz_IZW5soeg7kcBLmaruiuCHlVhyR4C3_-D0lDhtXV0xDZU4JnapR9q_QbyXOdsSN_n8Ko0owSMITVXWbOjZml2GATMUBx4h9QcNpQsbz6B1BsDbxvoK2N-cuyw5I7OcwyyAJI8BbnPXiU2pVAYmQ26SnXHrWQt2DFsiWi5l6oo_U4dEo6cruImA)
_Comment utiliser Aujourd'hui() dans Excel_

Excel affiche automatiquement la date actuelle selon les paramètres de date et d'heure de votre ordinateur. Il en va de même pour la fonction MAINTENANT(), qui affiche la date et l'heure actuelles.

### Comment utiliser la fonction `CONCATENER()` dans Excel

Examinons une fonction de texte. Vous utilisez CONCATENER pour joindre deux ou plusieurs chaînes de texte en une seule chaîne.

Voici la syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-316.png)
_Syntaxe CONCATENER() d'Excel_

Supposons que nous voulons joindre "Ceci est" avec "freeCodeCamp" – mais dans votre cellule, vous avez simplement "freeCodeCamp".

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-320.png)
_freeCodeCamp Excel_

Si vous allez écrire une chaîne à l'intérieur d'une formule, vous devez l'écrire entre guillemets comme ceci " ". 

Pourquoi ?

De cette manière, Excel ne pensera pas que vous essayez d'écrire une autre fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-319.png)
_Comment utiliser la fonction CONCATENER d'Excel_

Cela retournera la phrase "Ceci est freeCodeCamp"

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-321.png)
_Comment utiliser CONCATENER() dans Excel_

### Comment utiliser la fonction `RECHERCHEV()` dans Excel

C'est l'une des formules ou fonctions les plus intéressantes et les plus couramment utilisées d'Excel. Vous l'utilisez pour trouver une valeur dans un tableau ou une plage par ligne.

Voici un scénario :

Nous avons un tableau simple qui montre divers films avec leur genre, studio principal, score du public %, rentabilité, pourcentage de tomates pourries, recettes mondiales et année. J'utiliserai simplement les 10 premières lignes des données d'exemple de ce [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea).

![Image](https://lh5.googleusercontent.com/T12acvhR4WeGpmxjG8Ye9-nif_k8r-trYb3Zacz9PZjxRDZJOQd1weeIx06Soa-QRsriVCuaGrJ2B_-6klJcxyuRKh7cmoIPre-cbHecnxvooo6AEYd5pgc_Dz2keINjCm-yF3Vw1HtcQTfzMK938gUK5Ybks72moTZEGuPmnHVHS2-yHv38hRvArg)
_Ensemble de données de films_

Je veux que, chaque fois que je tape un film dans la cellule jaune, l'année s'affiche dans la cellule verte. Utilisons RECHERCHEV pour le trouver.

Voici la syntaxe de RECHERCHEV :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-317.png)
_Syntaxe Vlookup d'Excel_

Outre l'écriture de vos formules dans la cellule, vous pouvez également les écrire en utilisant le bouton Insérer une fonction (fx) d'Excel, qui se trouve près de la barre de formule.

Essayons cela.

1. Écrivez `=Vlookup(` dans la cellule verte.
2. Cliquez sur fx. Une boîte de dialogue s'ouvrira montrant tous les arguments dont cette formule a besoin.
3. Saisissez la valeur pour chaque argument.
4. Lookup_value (argument requis) : C'est ce que vous voulez trouver. Dans notre cas, il s'agit du film "Youth in Revolt" qui se trouve dans la cellule B1.
5. Table_array (argument requis) : Il vous demande simplement le tableau contenant les données. Vous lui donnez le tableau entier, qui dans notre cas est A4:H13
6. Col_index_num (argument requis) : Il vous demande le numéro de colonne du tableau que vous avez donné. Dans notre cas, nous voulons l'année. Cela se trouve dans la colonne 8.
7. Range_lookup (argument optionnel) : Enfin, nous choisissons si nous voulons une correspondance approximative (VRAI) ou une correspondance exacte (FAUX). 

	- VRAI signifie correspondance approximative, donc il retourne la valeur la plus proche ou une estimation.

	- FAUX signifie correspondance exacte, donc il retourne une erreur si elle n'est pas trouvée.

8. Nous opterons pour FAUX car nous voulons la correspondance exacte.

![Image](https://lh6.googleusercontent.com/T-VtgAKve9lXEP8VA5FATji23YJveuZJfqWEnde330eLDw0gJj2hn1Qol5R1fVqs9aFYPoxFZ9Y5XLwth6MHWgYH55i0Llz-gS8m2_r7aEViaDD_3_Gpow5rWATdGtCBVlPTolM-9zZ2hono6lsBiN-l_DM7pVjLzk7oOZ-GYO8unxTQF7unpzA5MA)
_Comment utiliser RECHERCHEV() dans Excel_

9. Cliquez sur "OK." Excel retournera 2010. 

Cependant, vous pouvez écrire cela dans la cellule en tapant `=RECHERCHEV(B1,A4:H13,8,FAUX)` dans votre cellule.

![Image](https://lh3.googleusercontent.com/fhQrWy2DvFXRtscCz_H-DbZE73claukadh-KwtU5XGuxmZWDwtDlo60aM7cqBS3iPpayxfB3DH6NeFFH2j19l2M3QXM7RCUlYrGHRUlxcFAmEUylwj4g1b8k00lYx_8FWrEQl4cJyxmhoUPLlxJuALoUtO5F06SQl1_0nWusaza0nWFwZmO4T-3qGA)
_Comment utiliser RECHERCHEV() dans Excel_

# Conseils et règles lors de l'écriture de fonctions Excel

Lors de l'écriture de notre fonction, Excel fournit quelques conseils de formule.

1. L'info-bulle d'argument ne disparaît pas tant que vous n'avez pas fermé la dernière parenthèse.
2. La barre de formule montre votre formule.
3. L'argument que vous êtes en train d'écrire est toujours en surbrillance. Jetez un œil à la valeur de recherche dans l'image ci-dessous.
4. Les crochets [] vous indiquent qu'il est optionnel.
5. Enfin, le code couleur – notre B1 est en bleu, et la cellule B1 est en bleu pour nous guider sur la cellule ou le tableau qui a été sélectionné. La même chose se produira pour A4:H13 lorsque nous le sélectionnerons comme argument table_array.  


![Image](https://lh4.googleusercontent.com/DVOp6zoa3z8cC01iE0iW01CcMv3ceE3WId7qu-2peocY8HkJf3ltmXHfAgHjj9Sj-7w-NS0DugruBR8FTCTRW77AFLRmdwM_UY83pXcFv3M6FHZBHFpWXy6B02ocko1NtC15GpHenEzBjU2w13i5SorlHU_6FdfA12iycyevjQhgnu6Mr78_CwkRSw)
_Recherchev et barre de formule Excel_

# Comment travailler avec des fonctions imbriquées dans Excel

Une fonction imbriquée est lorsque vous écrivez une fonction dans une autre fonction. Par exemple, trouver la moyenne de la somme des valeurs.

Le premier conseil lors de l'écriture d'une fonction imbriquée sera de traiter chaque fonction individuellement. Donc, adressez la première fonction avant d'adresser la deuxième. Un conseil pro serait de regarder l'info-bulle d'argument lors de l'écriture.

Prenons un scénario simple.

Nous avons deux tableaux de nombres. Chacun contient les scores des étudiants de la classe. Je veux additionner les deux tableaux avant d'obtenir la moyenne. 

Commençons.

1. Tapez votre = suivi de la moyenne.
2. Le premier nombre sera la somme des scores de la première classe.
3. Le deuxième nombre sera la somme des scores de la deuxième classe. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-318.png)
_Fonction imbriquée : Syntaxe MOYENNE et SOMME d'Excel_

![Image](https://lh3.googleusercontent.com/SBV3QpbGiSsXkDoXBpRaRfbjVUjJckLV0crBJ2u5iptUb0C10poCJZIZltv0b13tTTXpABVQ9CvHoAC2S5gwCNMxhaTFX3Y1oyRgNehxFEHPRf_Sm9--HQmVh8ZsVWKsWs2EfQBAEdv6sSTqTP2tmr0JXPb44UmLOO82OzM3oERfntfhPyHQaf1b_w)
_Syntaxe MOYENNE d'Excel_

Enfin, n'oubliez pas la parenthèse fermante. 

Ainsi, la formule sera `=MOYENNE(SOMME(B3:B8),SOMME(D3:D8))`.

# Comment travailler avec les fonctions de tableau dynamique dans Excel

Les fonctions de tableau dynamique sont des formules associées au comportement de déversement de tableau. 

Auparavant, vous écriviez une fonction et elle retournait une seule entrée. Nous appelons ces types de fonctions des formules de tableau héritées. 

Les fonctions de tableau dynamique, en revanche, retourneront des valeurs qui entreront dans les cellules voisines. Voici quelques exemples de fonctions de tableau dynamique :

* UNIQUE
* TEXTE.DECALER
* FILTER
* SEQUENCE
* TRIER
* TRIERPAR
* ALEA.MATRICE

Examinons la formule UNIQUE.

### Comment utiliser la formule UNIQUE() dans Excel

La formule unique fonctionne en retournant la valeur unique d'un tableau ou d'une liste. Utilisons les données d'exemple de film de ce [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea). Ce tableau contient 77 lignes de films, à l'exclusion de l'en-tête.

![Image](https://lh5.googleusercontent.com/cgULd4fUAfw1b4J5Q2utiNG_bPSaicGK6vEtuNKS6zCL2IFgoq8ivfZL_UMTTUcRUNc-nVDRxx8O6gQUCba1Eoko6U588n18CsiuBigsVS83V8W8bLZjtltBOqIkWUJRDhhamJzGzqz3FWn_sgVAB3oLJx5L7JOEike_iawhMd7fQHinqfSb_MoaxA)
_Données de films GitHub_

Essayons d'obtenir les années uniques de notre ensemble de données – c'est-à-dire les années sans doublons. 

Pour ce faire :

1. Tapez `=UNIQUE(`
2. Sélectionnez l'ensemble du tableau de valeurs de la colonne année : =UNIQUE(H2:H78)

![Image](https://lh6.googleusercontent.com/mdX9zeClRBtGuzdHukis2gU-2RcH1K2rJvLrUHbSXN2ECokzYTn6SWSLuE2UOACXx3J2DrJQTauzLIb2u5Eqgq1LGvUJXVhpYAZD29CKZnWMBaId2O_6AFHtPJLFbz1FsG7dSIq8zMeRivRwG-qdpw74JG_Qglu4yrlgWIH-8ycQRMQ4cqp1ZNbSgQ)
_Comment utiliser la formule UNIQUE d'Excel_

3. Fermez la parenthèse et appuyez sur Entrée.

Bien que la formule ait été écrite dans une seule cellule, la valeur retournée s'est déversée dans les cellules en dessous. C'est le comportement de déversement de tableau.

![Image](https://lh4.googleusercontent.com/BM4eUSa5hvjSJF4Md2eizx-N97bc2dOdV0LwGYKLErjP4acTf0oCYnjYLhuxs3JHcF7YHyONMWTbXH24Epmc0AT6kvmyL_cg6d0shcKjEmvVL9wN_YQXMpTIGKoh-1dgmfyqUg102K67JsjUGycCMogiCzsIK7E53e7rZ5qd_buCQfylmIH4jHPtaQ)
_Formule de tableau dynamique Excel_

# Comment créer vos propres fonctions dans Excel

Microsoft Excel a publié un ensemble de nouvelles fonctions pour rendre les utilisateurs plus productifs. L'une de ces fonctions était la fonction LAMBDA.

La fonction LAMBDA vous permet de créer des fonctions personnalisées sans macros, VBA ou JavaScript, et de les réutiliser dans un classeur. 

Le meilleur ? vous pouvez la nommer.

### Comment utiliser la fonction `LAMBDA()` dans Excel

Cette fonction LAMBDA augmentera la productivité en éliminant le besoin de copier et coller cette formule, ce qui peut être sujet à des erreurs.

Voici la syntaxe LAMBDA :

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-322.png)
_Fonction LAMBDA d'Excel_

Commençons par un cas d'utilisation simple en utilisant les données d'exemple de film de ce [GitHub Gist](https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea). 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-323.png)
_L'ensemble de données de films_

Nous avions une colonne appelée "Recettes mondiales", essayons de trouver la valeur en Naira.

1. Créez une nouvelle colonne et appelez-la "Recettes mondiales en Naira".
2. Juste en dessous du nom de notre colonne, Cellule I2, tapez `=lAMBDA(`
3. LAMBDA nécessite un paramètre et/ou un calcul. 

Le paramètre signifie la valeur que vous voulez passer, dans notre cas d'utilisation, nous voulons changer la valeur brute. Appelons cela brut.

Le calcul signifie la formule ou la fonction que vous voulez exécuter. Pour nous, ce sera de le multiplier par le taux de change. Pour le moment, c'est 670. Donc écrivons brut * 670. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-328.png)
_Comment utiliser la fonction LAMBDA dans Excel_

4. Appuyez sur Entrée. Cela retournera une erreur car brut n'existe pas et vous devez faire savoir à Excel ces noms.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-329.png)
_Utilisation de LAMBDA d'Excel_

5. Pour utiliser la fonction nouvellement créée, vous devez copier la syntaxe écrite.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-330.png)
_Écriture de fonction avec LAMBDA d'Excel_

6. Allez dans le ruban de formule et ouvrez le gestionnaire de noms. 

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-332.png)
_Gestionnaire de noms d'Excel utilisant la fonction LAMBDA_

7. Définissez les paramètres du gestionnaire de noms :

* Le nom est simplement ce que vous voulez appeler cette fonction. Je vais avec NairaConvert.
* La portée doit être le classeur car vous voulez utiliser cette fonction dans le classeur.
* Les commentaires expliquent ce que fait votre fonction. Cela agit comme une documentation.
* Dans **référer à**, vous devez coller la syntaxe de la fonction copiée.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-333.png)
_Gestionnaire de noms d'Excel_

8. Appuyez sur Ok.

9. Pour utiliser cette nouvelle fonction, vous l'appelez avec le nom que vous lui avez donné—NairaConvert—et vous lui donnez le brut qui est notre recette mondiale sur G2.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-334.png)
_Fonction personnalisée avec LAMBDA_

10. Fermez la parenthèse et appuyez sur Ok

![Image](https://www.freecodecamp.org/news/content/images/2022/09/image-336.png)
_Calcul avec LAMBDA d'Excel_

# Où puis-je en apprendre davantage sur Excel ?

Il existe une multitude de ressources pour apprendre Microsoft Excel de nos jours. Tellement qu'il est difficile de déterminer lesquelles sont à jour et utiles.

La meilleure chose que vous puissiez faire est de trouver un tutoriel utile et de le suivre jusqu'à la fin, plutôt que d'essayer d'en suivre plusieurs à la fois. Je vous conseille de commencer par le [Tutoriel Microsoft Excel pour débutants - Cours complet](https://www.youtube.com/watch?v=Vl0H-qTclOg) de freeCodeCamp, disponible sur YouTube. 

Vous devriez également rejoindre des communautés comme la [Communauté d'apprentissage Microsoft Excel et d'analyse de données](https://www.meetup.com/Microsoft-Excel-and-Data-Analysis-Learning-Community/). Cependant, si vous cherchez une compilation de ressources, consultez les [tags Excel de la publication freeCodeCamp](https://www.freecodecamp.org/news/tag/excel/).

Si vous avez aimé lire cet article et/ou si vous avez des questions et souhaitez entrer en contact, vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/ifeanyi-iheagwara/) ou [Twitter](https://twitter.com/Bennykillua).