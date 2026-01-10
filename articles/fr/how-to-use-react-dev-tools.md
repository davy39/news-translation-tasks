---
title: Comment utiliser React Dev Tools – Avec des exemples de code et des vidéos
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-11T18:18:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-react-dev-tools
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/thumbnail.jpeg
tags:
- name: Developer Tools
  slug: developer-tools
- name: React
  slug: react
seo_title: Comment utiliser React Dev Tools – Avec des exemples de code et des vidéos
seo_desc: 'By Aman Kalra

  When you''re working on a React project, one of the easiest ways to debug your code
  is using the React Dev Tools.

  React Dev Tools is an extension created by the React team. It enables developers
  to debug their code inside their Developer...'
---

Par Aman Kalra

Lorsque vous travaillez sur un projet React, l'une des manières les plus simples de déboguer votre code est d'utiliser les React Dev Tools.

React Dev Tools est une extension créée par l'équipe React. Elle permet aux développeurs de déboguer leur code directement dans leurs outils de développement.

Une fois que vous avez ajouté l'extension, vous obtiendrez 2 nouveaux onglets dans DevTools appelés respectivement Composants et Profiler.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Components-and-Profiler-Tabs-1.png)
_Onglets Composants et Profiler dans Chrome Dev Tools_

Pour utiliser toutes les fonctionnalités de l'extension, vous devez être en mode développement. En effet, en mode production, les noms des composants sont remplacés par des lettres (comme vous pouvez le voir dans la capture d'écran ci-dessus) et vous ne pourrez pas profiler vos composants.

## Comment utiliser l'onglet Composants

L'onglet Composants vous permet de déboguer votre code dans les outils de développement avec diverses fonctionnalités. Passons-les en revue une par une :

### Vous pouvez vérifier les props/état/hooks du composant

![Props et État dans l'onglet Composant](https://www.freecodecamp.org/news/content/images/2023/01/Props-and-State-in-Component-s-Tab-1.png)
_Affichage des Props et de l'État_

Cet onglet vous aidera à rechercher un composant et à vérifier ses props/état respectifs dans vos outils de développement, sans avoir à les logger séparément dans la console.

### Vous pouvez modifier les props/état depuis les outils de développement

%[https://vimeo.com/787154069]

L'une des fonctionnalités incroyables est que vous pouvez modifier les props/état de votre composant directement dans le navigateur. Cela vous permet de refléter les changements en temps réel sans avoir à recharger ou rafraîchir votre page web. Ci-dessus se trouve une vidéo d'exemple pour que vous puissiez voir comment cela fonctionne.

### Vous pouvez rechercher un composant

%[https://vimeo.com/787155384]

Vous pouvez facilement rechercher un composant dans toute votre application en tapant simplement son nom dans la barre de recherche fournie. Il vous montrera tous les composants liés aux mots-clés tapés. Ensuite, vous pouvez naviguer entre les résultats correspondants.

### Vous pouvez vérifier l'arborescence du composant

![Hiérarchie du Composant](https://www.freecodecamp.org/news/content/images/2023/01/Component-s-Hierrarchy.png)
_Hiérarchie du Composant_

Lors du débogage, il est important de noter quels composants parents ont provoqué le re-rendu du composant enfant. Vérifier cela dans votre code est parfois fastidieux. Mais la section "**rendered by**" vous facilite la tâche en montrant tous les composants parents en un seul endroit.

### Vous pouvez logger les données d'un composant dans la console

![Image](https://www.freecodecamp.org/news/content/images/2024/08/logging-components.jpg)
_Logging des données d'un composant dans la console_

Il y a des développeurs qui aiment travailler dans la console, et cette fonctionnalité vous permet de logger toutes les données de votre composant dans la console en un seul clic. Elle montre toutes les informations pertinentes concernant le composant comme les props reçues, les hooks présents, quel nœud il occupe dans le DOM, et l'emplacement du fichier dans votre système.

### Vous pouvez vérifier les sous-composants

%[https://vimeo.com/787165596]

Tout comme vérifier les composants parents n'est pas toujours facile dans votre code, il en va de même pour vérifier les composants enfants.

Pour surmonter ce problème, vous pouvez double-cliquer sur le nom d'un composant, ce qui vous montrera tous les sous-composants présents à l'intérieur du composant cible en une seule fois.

## Comment utiliser l'onglet Profiler

Cet onglet vous permet de tester les performances de vos composants et montre quels composants doivent être optimisés.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Profiler-tab-1.png)
_Onglet Profiler_

Comme vous pouvez le voir ci-dessus, j'ai marqué quelques éléments sur la capture d'écran. Passons-les en revue un par un :

* **A** est le bouton d'enregistrement, qui vous aidera à enregistrer une session de profilage.
* **B** est le bouton de rafraîchissement, qui vous aidera à rafraîchir la page pour une session.
* **C** est le bouton de suppression, qui vous aidera à effacer les résultats de la session de profilage.
* **D** est le graphique des commits, qui vous montrera la liste des commits pendant une session.
* **E** est la liste des composants, qui vous montrera les composants rendus pendant une session.
* **F** est le bouton du graphique en flammes, qui vous montrera la liste des composants comme **E**.
* **G** est le bouton du graphique classé, qui vous montrera la liste des composants de manière classée.

Maintenant, plongeons dans les différentes fonctionnalités présentes dans cet onglet et comment vérifier les performances de votre page web :

### Comment lire le graphique des commits

Le graphique des commits montre la liste des commits pendant une session. Si vous pouvez voir dans l'image ci-dessus, dans la section **D**, il y a 3 barres. Celles-ci représentent 3 commits dans une session. Et chaque commit montre un effet secondaire qui a provoqué la mise à jour du DOM.

> [Selon la documentation](https://reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#browsing-commits), "La couleur et la hauteur de chaque barre correspondent à la durée de rendu de ce commit. (Les barres jaunes et plus hautes ont pris plus de temps que les barres bleues et plus courtes.)"

Vous pouvez même naviguer entre les barres et vérifier chaque commit séparément.

### Comment lire le graphique en flammes

Le graphique en flammes montre la liste des composants rendus dans un commit. Si vous pouvez voir dans l'image ci-dessus, lorsque vous cliquez sur la section étiquetée **F**, toutes les barres horizontales dans la section **E** représentent différents composants du premier commit.

> [Selon la documentation](https://reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html#flame-chart), "La couleur d'une barre indique combien de temps le composant (et ses enfants) a pris pour se rendre dans le commit sélectionné. Les composants jaunes ont pris plus de temps, les composants bleus ont pris moins de temps, et les composants gris ne se sont pas rendus du tout pendant un commit."

### Comment vérifier les performances de votre page web

Pour vérifier les performances de votre page web, tout ce que vous avez à faire est :

* Cliquez sur le bouton d'enregistrement.
* Utilisez votre page web afin que le Profiler puisse analyser le rendu des composants.
* Cliquez à nouveau sur le bouton d'enregistrement pour terminer l'enregistrement.

Ensuite, vous verrez le graphique en flammes, et vous pourrez analyser quels composants prennent plus de temps à se rendre.

Notez que le graphique en flammes montre également :

1. Quand exactement le composant a été rendu.
2. Et combien de temps il a pris pour se rendre dans une session de profilage.

**Par exemple** : Dans l'image ci-dessous, le **composant Home** a été rendu à **1,5s** de la session de profilage et il a pris **27,7 ms** pour se rendre.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Flame-Chart.png)
_Graphique en Flammes_

### Comment lire un graphique classé

Lorsque vous cliquez sur l'icône **Graphique classé** comme montré dans la section **G** de l'image, vous obtiendrez une vue graphique des composants. Cette vue est en ordre décroissant, c'est-à-dire que le composant qui a pris le plus de temps à se rendre sera en haut et le composant qui a pris le moins de temps sera en bas.

Vous pouvez voir cela dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Ranked-Chart.png)
_Graphique Classé_

**Note** : Vous pouvez obtenir plus d'informations sur pourquoi votre composant a été rendu en activant simplement la case à cocher "Record why each component rendered while profiling." dans les paramètres de l'onglet "Profiler". J'ai joint une image pour référence ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Render-description.png)
_Description du rendu_

## **Conclusion**

React Dev Tools est une excellente extension à avoir lorsque vous travaillez sur vos applications React. Elles peuvent vous aider à déboguer facilement votre code et à trouver les goulots d'étranglement de performance dans votre application.

N'hésitez pas à essayer ces fonctionnalités la prochaine fois dans votre projet React.

## Merci d'avoir lu !

Si vous avez trouvé cet article utile, n'hésitez pas à le partager avec vos amis et collègues.

Si vous aimez voir des conseils et astuces similaires en HTML, CSS, JavaScript et React, n'hésitez pas à [me suivre sur LinkedIn](https://www.linkedin.com/in/amankalra1).