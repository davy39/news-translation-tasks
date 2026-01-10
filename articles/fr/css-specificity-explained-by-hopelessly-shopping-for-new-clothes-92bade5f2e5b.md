---
title: La Spécificité CSS Expliquée en Faisant des Achats Désespérés de Nouveaux Vêtements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-15T04:52:15.000Z'
originalURL: https://freecodecamp.org/news/css-specificity-explained-by-hopelessly-shopping-for-new-clothes-92bade5f2e5b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Cmd1yXcbw-hv3lb1AEenMA.jpeg
tags:
- name: coding
  slug: coding
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: La Spécificité CSS Expliquée en Faisant des Achats Désespérés de Nouveaux
  Vêtements
seo_desc: 'By Kevin Kononenko

  If you have ever wandered into a department store or other clothing store, then
  you can understand how CSS selectors apply their styles.

  If you are a beginner to CSS, you have probably seen plenty of scenarios already
  where CSS sty...'
---

Par Kevin Kononenko

Si vous êtes déjà entré dans un grand magasin ou un autre magasin de vêtements, alors vous pouvez comprendre comment les sélecteurs CSS appliquent leurs styles.

Si vous êtes débutant en CSS, vous avez probablement déjà vu de nombreux scénarios où les règles de style CSS entrent en conflit. Vous pensez avoir ajouté un nouveau style à un élément, mais après avoir actualisé le navigateur plusieurs fois… vous réalisez que le style n'est pas appliqué pour une raison quelconque.

Voici un exemple. Supposons que vous avez une règle générale selon laquelle toutes les balises de paragraphe doivent avoir une hauteur de ligne de 140 %, comme ceci.

```
p {   line-height: 140%; }
```

Mais vous souhaitez également créer une classe `subtitle` qui aura une hauteur de ligne de 120 %, qui s'appliquera généralement aux éléments de paragraphe.

```
.subtitle {   line-height: 120%; }
```

Alors, lequel s'appliquera lorsque vous l'assignez comme suit ?

```
<p class="subtitle">Ceci est un sous-titre</p>
```

La réponse est le style de la classe `subtitle`, mais je veux trouver une meilleure façon d'expliquer les règles derrière cette logique. Vous ne voulez pas ouvrir l'Inspecteur chaque fois que vous n'êtes pas sûr du style le plus spécifique.

Voici un scénario pour vous aider : imaginez que vous êtes un vendeur dans un grand magasin ou un autre magasin de vêtements. Vous êtes payé en fonction du nombre de vêtements que vous vendez au cours de la journée, vous devez donc passer votre temps avec les meilleurs clients si vous voulez gagner le plus d'argent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*72O7r9E5Nvxkaglc.)

Les clients qui semblent les plus susceptibles d'acheter ont la **priorité**. Les clients qui viennent avec une idée précise de ce qu'ils veulent sont plus susceptibles d'acheter.

CSS fonctionne de manière similaire. Il donnera la priorité aux styles les plus spécifiques, qui remplaceront les styles moins spécifiques. Les moyens les plus courants d'ajouter du style sont :

* Niveau d'élément (balise `p`)
* Niveau de classe (`.subtitle`)
* ID
* Style en ligne

Voici comment déterminer lesquels des sélecteurs ci-dessus sont les plus spécifiques. Dans chaque cas, le client cherche un costume sur mesure, et vous devez vendre autant de vêtements que possible.

### Sélecteurs d'Éléments — Avoir Seulement une Idée Vague

Êtes-vous déjà entré dans un grand magasin avec seulement une pensée vague, comme « J'ai besoin d'un costume pour un événement la semaine prochaine » ?

D'après mon expérience personnelle, je peux vous dire que c'est une excellente façon de rester bloqué dans le magasin pendant des heures, en essayant des costumes au hasard. Quoi qu'il en soit, ces types de clients mettront le plus de temps à trouver quelque chose qui leur plaît. Ils devront parler à plusieurs personnes et essayer plusieurs costumes. Leur image mentale de ce qu'ils veulent ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*medgGe7inXZjhhrj.)

Oui, ils n'ont aucune idée de ce qu'ils veulent. Ils doivent encore choisir un style, trouver leur gamme de prix et ensuite vous devez les mesurer pour que vous puissiez le tailler.

C'est la manière la moins spécifique de chercher un costume, et c'est similaire au style pour un type général d'élément. Comme ceci, un `div` avec un fond noir :

```
div {   background-color: black; }
```

### Sélecteurs de Classe — Au Moins Vous Connaissez la Marque…

D'accord, le niveau au-dessus d'un type général de vêtement est une marque. Donc, vous pourriez dire que vous aimez les vêtements Ralph Lauren, alors vous commencerez à la partie du magasin.

![Image](https://cdn-media-1.freecodecamp.org/images/0*JAEsVtLxAOqcfOjv.)

(**Note** : Ce n'est pas un présentoir Ralph Lauren sur la photo, juste la seule photo de stock que j'ai pu obtenir)

C'est mieux que de chercher tous les costumes dans le magasin, mais cela signifie toujours que le client devra prendre un peu de temps avant d'être prêt à acheter. Voici à quoi ressemble le CSS :

```
.ralphLauren { }
```

C'est plus spécifique qu'un `div`, que nous avons utilisé dans l'exemple ci-dessus. Mais cette déclaration CSS pourrait en fait être plus spécifique. Puisque nous savons que le client cherche un costume Ralph Lauren, combinons l'élément et la classe. Après tout, Ralph Lauren pourrait être n'importe quel type de vêtement, des bottes aux pantalons en passant par les chemises.

```
div.ralphLauren { }
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*hSinWUd9x-BdU2NJ.)

Ce style remplacera :

1. Tout le style général `div`
2. Le style de la classe `ralphLauren` lorsque la classe est appliquée à un `div`.

C'est parce qu'il est plus spécifique en impliquant à la fois un élément et une classe. Donc, si nous avons ce qui suit :

```
.ralphLauren {   background-color: black; }
```

```
div.ralphLauren {   background-color: grey; }
```

La deuxième déclaration est plus spécifique, donc elle aura la priorité pour tous les `div` avec la classe `ralphLauren`.

### Sélecteur d'ID — Ils Connaissent le Modèle Exact Qu'ils Veulent

Le sélecteur d'ID est presque aussi spécifique que possible. C'est un peu comme la personne qui a fait autant de shopping en ligne que possible, et qui vient au magasin avec une photo imprimée du costume qu'elle veut.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IviYwcuWUEVHewYL.)

Oui, les gens font encore cela. D'accord, peut-être qu'ils l'ont comme un lien enregistré pour pouvoir l'ouvrir sur leur téléphone et vous le montrer, le vendeur.

D'accord, je pourrais faire cela parfois.

Quoi qu'il en soit, si le client connaît déjà le modèle spécifique de costume qu'il/elle veut, vous n'avez besoin que de mesurer ses dimensions et ensuite il/elle sera prêt à acheter.

Le [sélecteur d'ID](https://www.w3schools.com/css/css_syntax.asp) n'est destiné qu'à être utilisé pour un seul élément sur toute la page, ce qui est beaucoup plus spécifique que les sélecteurs de classe ou d'élément. Voici un exemple de modèle de costume `RL123` que le client a choisi avant même de vous rencontrer :

```
#rl123 {   background-color: navy; }
```

Si la couleur par défaut pour les costumes Ralph Navy est grise, cette déclaration signifie que ce modèle particulier a en fait une couleur marine.

Une note rapide sur la scalabilité : vous ne voulez **pas** d'éléments HTML avec des ID et des styles personnalisés partout sur votre page. Cela deviendra un énorme casse-tête à maintenir. Vous devez toujours utiliser des styles de niveau élément et classe pour créer rapidement des styles universels. Mais vous devez également savoir comment remplacer ces règles dans des cas individuels.

### Style en Ligne — Le Client Connaît Leur Modèle et Leurs Dimensions

C'est la manière la plus spécifique de le faire, et aussi la moins scalable. Vous pouvez utiliser le **style en ligne** directement dans l'élément HTML pour remplacer les styles écrits en CSS.

C'est un peu comme le client qui vient au magasin et qui non seulement connaît le costume qu'il veut, mais connaît aussi ses dimensions. Il a une idée très précise de ce qu'il veut, et il est prêt à commander le costume et à quitter le magasin le plus rapidement possible. C'est génial pour un vendeur ! Donc, cela obtient la priorité la plus élevée.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DxVV0_pwLyFp4DwA.)

Voici à quoi cela ressemble en termes de HTML.

Nous allons assigner les attributs `**width**` et `**height**` au `div` avec la classe `ralphLauren` :

```
<div class="ralphLauren" style="height:100px; width:100px"></div>
```

Si nous avions assigné la largeur et la hauteur dans le CSS, comme dans les exemples ci-dessus, cela serait écrasé ici.

### Le Joker — !important

Il y a une autre façon de changer la priorité des règles de style de CSS. Je ne vais pas en parler, cependant, car il ne devrait être utilisé que dans des situations où il n'y a pas d'autre alternative. Cela brise toutes les règles que nous venons d'établir…

Vous pouvez [en savoir plus sur !important ici](https://appendto.com/2016/04/css-important-rule-how-to-use-it-correctly/).

### Résumé Final

Voici l'ordre de spécificité pour différentes façons d'appliquer le style :

![Image](https://cdn-media-1.freecodecamp.org/images/0*0KoWiUMj7yRS4Uln.)

### Obtenez Plus de Tutoriels de Codage Visualisés

Avez-vous apprécié ce tutoriel ? Donnez-lui un « clap » pour que d'autres puissent le découvrir aussi.

Ou inscrivez-vous à mes derniers tutoriels [ici](http://www.codeanalogies.com/) :