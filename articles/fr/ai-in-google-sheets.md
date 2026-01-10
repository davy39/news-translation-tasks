---
title: L'IA dans Google Sheets – Comment utiliser GPT Copilot
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-06-12T22:10:01.000Z'
originalURL: https://freecodecamp.org/news/ai-in-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/ai-in-google-sheets-thumb.jpg
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: L'IA dans Google Sheets – Comment utiliser GPT Copilot
seo_desc: 'It seems to be the year of AI. And my favorite tool, Google Sheets, is
  not to be left out of the fun. 🎉


  Coefficient produced a Google sheets extension with the ability to use OpenAI''s
  GPT models from within a spreadsheet. It’s called GPT Copilot an...'
---

Il semble que ce soit l'année de l'IA. Et mon outil préféré, Google Sheets, n'est pas en reste. 🎉

![Image](https://www.freecodecamp.org/news/content/images/2023/06/giphy.gif)

[Coefficient](https://coefficient.io/gpt-google-sheets) a produit une extension pour Google Sheets permettant d'utiliser les modèles GPT d'OpenAI directement depuis une feuille de calcul. Elle s'appelle GPT Copilot et est disponible pour un essai gratuit. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.00.44-PM.png)
_capture d'écran de la page GPT dans Sheets de Coefficient_

J'ai repoussé l'exploration de cet outil pendant assez longtemps, bien que je suive le travail de Coefficient sur Google Sheets depuis un moment.

Pour être honnête, j'en avais un peu assez de tout ce battage autour de l'IA et j'étais méfiant face à un nouvel effort dans ce domaine. Ai-je vraiment besoin d'utiliser l'IA dans des feuilles de calcul ? 

🤷Oui et non.

## Exemple vidéo

J'ai réalisé une courte vidéo présentant quelques-unes des fonctions GPTx, et je vais détailler chacune d'entre elles dans l'article ci-dessous. Si vous avez une minute, regardez la vidéo de 2,5 minutes et donnez-lui un 👍.

%[https://youtu.be/HaKYyPLaOFA]

L'extension est plutôt cool.

L'IA n'est pas quelque chose qui va faire tout mon travail à ma place. Mais c'est un outil assez puissant avec lequel je peux travailler plus rapidement, plus efficacement, et dans certains cas, obtenir une inspiration unique.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/potential.gif)
_gif de Ted Lasso disant, ça sent le potentiel_

## Fonctions de GPT Copilot

Dans l'extension GPT Copilot sur Google Sheets, nous avons une liste de plusieurs fonctions intégrées `GPTX` que nous pouvons maintenant utiliser directement dans la feuille elle-même. 

[Voici](https://docs.google.com/spreadsheets/d/1CaLdC22IS_9K42ycwkyYlnsCSGsEpyJtedPWXxn5poI/edit#rangeid=903106705) un document avec toutes les fonctions listées, et nous allons passer en revue chacune d'entre elles ci-dessous.

Et [voici la feuille de calcul](https://docs.google.com/spreadsheets/d/10suhdcRdi5NI_PCGO0VK1TXiLIGdy44T8R3zL9938So/edit?usp=sharing) que j'ai utilisée pour tous mes exemples et la vidéo. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.12.07-PM.png)

La première fonction, `=GPTX(prompt)` nous permet simplement de générer du texte en utilisant le modèle GPT d'Open AI.

Je l'ai utilisée pour générer un objet de mail ci-dessous. Cette fonction générique `GPTX` peut être utilisée pour interroger le modèle ChatAI pour tout ce à quoi vous pouvez penser : 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-113.png)
_Capture d'écran de la fonction GPTX()_

Ensuite, nous avons `**=GPTX_LIST(prompt)**` qui nous permet de générer une liste de valeurs de la même manière. 

Cela ressemble au premier exemple, mais la liste des éléments apparaîtra dans des cellules séparées, ce qui est pratique si vous voulez... disons, les 10 jeux vidéo les plus vendus en Corée :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-114.png)
_Capture d'écran de la fonction GPTX_LIST()_

`**=GPTX_EDIT(text,[task])**` était utile lorsque j'ai créé des messages de corps d'email basés sur une invite que j'ai alimentée dans la fonction. Elle nous permet donc d'effectuer une tâche ou une transformation sur un texte d'entrée.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.14.09-PM.png)
_capture d'écran de la fonction GPTX_EDIT_

`**GPTX_MAP(search_keys, inputs)**` effectue une recherche floue, étant donné une liste de clés de recherche dans la liste des valeurs d'entrée, puis sortie la recherche la plus similaire pour chaque valeur d'entrée.

Si nous avons une liste de jeux et de sociétés de plateformes, elle peut mapper les valeurs des sociétés aux jeux corrects :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-124.png)
_Capture d'écran de GPTX_MAP()_

`**GPTX_FILL(text, [task])**` remplit les informations manquantes dans le tableau en fonction des lignes d'exemple.

Cela vous permettra de lui fournir quelques données d'exemple et de faire remplir le reste par GPTX :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-115.png)
_Capture d'écran de GPTX_FILL_

`**GPTX_TABLE(prompt, [header_row])**` génère un tableau de valeurs. Celle-ci était particulièrement cool car vous pouvez lui donner une requête réelle pour obtenir des données, ou lui faire remplir un tableau avec des données fictives.

Ici, nous pouvons obtenir quelques informations sur la population des 5 premières villes du Tennessee : 😀

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-116.png)
_Capture d'écran de GPTX_TABLE()_

`**GPTX_FORMAT(text, language)**` convertit les valeurs d'entrée dans le format spécifié. 

`**GPTX_TAG(text, tags)**` fait ce à quoi on pourrait s'attendre : il applique une ou plusieurs balises correspondant à un texte.

Si vous avez une liste de films et une liste de genres, vous pouvez les baliser ici. Intéressamment :

1. GPT ne semble pas avoir le sens de l'humour puisqu'il n'a pas classé Waterworld comme un flop.
2. Il ne remplira pas non plus aveuglément les genres manquants dans la liste (Goldeneye et Seven)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/flop.png)
_Capture d'écran de GPTX_TAG()_

Une autre histoire édifiante, cependant... lorsque j'ai ajouté "crime" pour voir s'il remplirait le vide de Seven, il est revenu avec des réponses différentes sur certains des autres... et a omis Casper et Jumanji cette fois-ci. Donc, bien que rien ne soit vraiment mal balisé, il donne des résultats variables. 

Dans ce cas, il se comporte un peu comme un humain. Vous obtiendrez différentes personnes répondant à ce type de question de balisage de différentes manières aussi. 🤷🏻

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2.png)

`**GPTX_CLASSIFY(text, labels)**`, de la même manière, classe le texte donné un ensemble de libellés ou de catégories.

`**GPTX_EXTRACT(text, info_to_extract)**` extrait les informations souhaitées du texte d'entrée. Donc, si vous avez une adresse dans une cellule, il peut extraire le nom de la ville de l'adresse.

> Attention cependant ; j'ai rencontré plusieurs instances lors de l'écriture de ces fonctions GPTX où j'ai obtenu des #ERROR! et j'ai dû rafraîchir la page, la fermer et la rouvrir, ou simplement attendre un moment...

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-118.png)

`**GPTX_SUMMARIZE(text, language)**` résume le texte d'entrée selon le format donné.

J'ai essayé d'être malin ici. J'ai collé le premier chapitre de The Great Gatsby dans une cellule. J'ai rapidement obtenu une erreur "trop grand" 😂)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-119.png)
_capture d'écran de l'erreur GPTX_Summarize_

Mais ! Réduire à 726 mots a suffi pour qu'il résume réellement le début de ce formidable roman :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-121.png)
_Capture d'écran de GPTX_SUMMARIZE() résumant le début de The Great Gatsby_

`**GPTX_TRANSLATE(text, language)**` traduit le texte d'entrée dans la langue spécifiée.

Celle-ci est simple et pas incroyablement utile pour mes feuilles de calcul... mais néanmoins, c'est plutôt sympa :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-122.png)
_Capture d'écran de GPTX_TRANSLATE()_

`**GPTX_CONVERT(text, format)**` convertit le texte d'entrée dans le format structuré spécifié.

`**GPTX_CODE(task, language)**` génère du code dans un langage spécifié, qui effectue la tâche spécifiée. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.21.54-PM.png)

`GPTX_CODE()` était vraiment sympa. Je vois aussi le plus de chances de problèmes ici car les novices seront tentés d'utiliser aveuglément du code sans savoir comment ou si cela fonctionne.

Cela semble être le plus bénéfique comme aide lorsque je sais comment le code devrait fonctionner, mais que je peux demander le squelette de base au lieu de devoir rechercher des méthodes par moi-même.

## Limites de GPT Copilot

Y a-t-il des limites au nombre d'invites que vous pouvez alimenter ces fonctions ? Oui. Bien sûr que oui. 😆

Pour rester gratuit, vous obtenez 10 000 exécutions. Les plans mensuels commencent à 100 000 exécutions par mois.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.33.46-PM.png)
_capture d'écran de la FAQ de Coefficient GPT Copilot_

## Ce que j'en pense

Je passe en revue quelques trucs de base que j'aurais pu générer moi-même dans la [vidéo d'exemple](https://youtu.be/HaKYyPLaOFA) que je vous encourage à regarder. Mais je vois le potentiel pour que cela soit un outil très utile à mesure que l'écosystème mature.

En ce qui concerne les données fictives, il est vraiment utile de simplement générer des trucs dans une feuille de calcul rapidement.

Et cela fonctionne très bien pour remplir les blancs où vous pourriez auparavant faire un peu plus de travail manuel, extraire des valeurs, formater des choses, classer des choses, et ainsi de suite.

En plus de ces fonctions intégrées, l'extension Coefficient contient également un constructeur de tableaux croisés dynamiques, un constructeur de formules et un outil de construction de graphiques.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-09-at-8.25.26-PM.png)
_capture d'écran de l'extension Coefficient_

Celles-ci vous permettent de fournir une invite à l'extension basée sur les données de votre feuille de calcul, et elle générera soit un tableau croisé dynamique, une formule, ou un graphique.

Ce sont des béquilles pour effectuer certaines opérations assez basiques dans Google Sheets. Mais elles ont une utilité intéressante et sont assez fiables lorsque vous leur donnez des invites bien rédigées.

## Conclusion

🤔 Les outils d'IA peuvent être une grande perte de temps. Il est assez facile de passer plus de temps à obtenir des résultats médiocres avec eux qu'il n'en aurait fallu pour faire les choses manuellement.

Mais cela fait partie de la courbe d'apprentissage de tout outil. Les investissements initiaux peuvent certainement porter leurs fruits à long terme. Je continuerai à utiliser ces outils pour, espérons-le, créer de meilleures feuilles de calcul plus efficacement.

 2753Qu'en pensez-vous ? Est-ce un autre exemple de sur-ingénierie de choses simples ? Ou est-ce la prochaine grande chose dans Google Sheets ?

Venez rejoindre la conversation sur ma chaîne YouTube : [https://www.youtube.com/@eamonncottrell?sub_confirmation=1](https://www.youtube.com/@eamonncottrell?sub_confirmation=1)

Ou sur mon LinkedIn : [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)

Passez une bonne journée ! 👋