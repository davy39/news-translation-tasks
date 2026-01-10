---
title: 'Tutoriel sur les variables CSS : Comment rendre votre HTML réactif avec les
  variables CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-26T16:42:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-responsiveness-super-simple-with-css-variables-8c90ebf80d7f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tLQrkgJJhKV3YrzPxsVVFA.png
tags:
- name: CSS
  slug: css
- name: mobile
  slug: mobile
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: 'Tutoriel sur les variables CSS : Comment rendre votre HTML réactif avec
  les variables CSS'
seo_desc: 'By Per Harald Borgen


  _Learn how to create the following responsiveness with CSS Variables._

  A quick tutorial on how to create responsive websites in 2019.

  If you haven’t heard of CSS Variables before, it’s a new feature of CSS which gives
  you the po...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/IuMWwaRBH-1VTyCpRImIsyYwp36b1lR6ObIM)
_[Apprenez à créer la réactivité suivante avec les variables CSS.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_tutorial_article)_

#### Un tutoriel rapide sur la création de sites web réactifs en 2019.

Si vous n'avez jamais entendu parler des variables CSS, c'est une nouvelle fonctionnalité de CSS qui vous donne le pouvoir des variables dans votre feuille de style, sans avoir à faire de configuration.

En essence, les variables CSS vous permettent de sauter l'ancienne méthode de définition des styles :

```css
h1 {  
  font-size: 30px;  
}

navbar > a {  
  font-size: 30px;  
}

…en faveur de ceci :

:root {  
  --base-font-size: 30px;  
}

h1 {  
  font-size: var(--base-font-size);  
}

navbar > a {  
  font-size: var(--base-font-size);  
}

```

Bien que la syntaxe puisse sembler un peu étrange, cela vous offre l'avantage évident de pouvoir modifier les tailles de police dans toute votre application en ne changeant que la variable `--base-font-size`.

Si vous souhaitez apprendre correctement les variables CSS, consultez [mon cours gratuit et interactif sur les variables CSS](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) sur Scrimba :

![Le cours contient huit screencasts interactifs](https://cdn-media-1.freecodecamp.org/images/1*MxS9trU9nmVDttW_IqQTyA.png)

_Le cours contient huit screencasts interactifs._

Ou si vous souhaitez en savoir plus sur le cours, vous pouvez également lire un aperçu de ce que vous apprendrez dans l'article ci-dessous :

[Vous voulez apprendre les variables CSS ? Voici mon cours gratuit en 8 parties !](https://medium.freecodecamp.org/want-to-learn-css-variables-heres-my-free-8-part-course-f2ff452e5140)

Maintenant, voyons comment cette nouvelle technologie peut faciliter votre vie lors de la création de sites web réactifs.

#### L'installation

Nous allons ajouter de la réactivité à un site web de portfolio qui ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*tLQrkgJJhKV3YrzPxsVVFA.png)

Il a l'air bien lorsque vous le consultez sur votre bureau. Cependant, comme vous pouvez le voir sur l'image de gauche ci-dessous, cette mise en page ne fonctionne pas bien sur mobile.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CZkMgq0rp9nTdChVxwq33g.png)

_Comment cela apparaît initialement sur mobile._

![Image](https://cdn-media-1.freecodecamp.org/images/1*zpFS--eNMyAzkdZWS1lLRQ.png)

_Comment nous voulons qu'il apparaisse._

Sur l'image de droite, nous avons modifié quelques éléments des styles pour qu'ils fonctionnent mieux sur mobile. Voici ce que nous avons fait :

1. **Réorganisé** la grille pour qu'elle soit empilée verticalement au lieu de deux colonnes.
2. **Déplacé** l'ensemble de la mise en page un peu plus haut.
3. **Redimensionné** les polices.

Pour ce faire, nous avons dû modifier le CSS suivant :

```css
h1 {  
  font-size: 30px;  
}

#navbar {  
  margin: 30px 0;  
}

#navbar a {  
  font-size: 30px;  
}

.grid {  
  margin: 30px 0;  
  grid-template-columns: 200px 200px;  
}

```

Plus précisément, nous avons dû apporter les ajustements suivants à l'intérieur d'une requête média :

* Réduire la taille de la police du `h1` à 20px
* Réduire la marge au-dessus et en dessous de la `#navbar` à 15px
* Réduire la taille de la police à l'intérieur de la `#navbar` à 20px
* Réduire la marge au-dessus de la `.grid` à 15px
* Changer la `.grid` de deux colonnes à une colonne

**Note :** Il y a, bien sûr, beaucoup plus de CSS dans cette application, même au sein de ces sélecteurs. Cependant, pour les besoins de ce tutoriel, j'ai supprimé tout ce que nous ne modifions pas dans la requête média. Consultez [ce terrain de jeu Scrimba](https://scrimba.com/c/cwJmLhn?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=cssvariables_tutorial_article) pour obtenir le code complet.

#### L'ancienne méthode

Il était possible de faire tout cela sans les variables CSS. Mais cela nécessiterait une quantité inutile de code, car la plupart des points ci-dessus auraient besoin de leur propre sélecteur à l'intérieur de la requête média, comme ceci :

```css
@media all and (max-width: 450px) {  
    
  navbar {  
    margin: 15px 0;  
  }  
    
  navbar a {  
    font-size: 20px;  
  }  
    
  h1 {  
    font-size: 20px;  
  }

  .grid {  
    margin: 15px 0;  
    grid-template-columns: 200px;  
  }

}

```

#### La nouvelle méthode

Maintenant, voyons comment cela peut être résolu avec les variables CSS. Pour commencer, nous allons plutôt stocker les valeurs que nous réutilisons ou modifions à l'intérieur des variables :

```css
:root {  
  --base-font-size: 30px;  
  --columns: 200px 200px;  
  --base-margin: 30px;  
}

Et ensuite, nous allons simplement utiliser ces variables dans toute l'application :

#navbar {  
  margin: var(--base-margin) 0;  
}

#navbar a {  
  font-size: var(--base-font-size);  
}

h1 {  
  font-size: var(--base-font-size);  
}

.grid {  
  margin: var(--base-margin) 0;  
  grid-template-columns: var(--columns);  
}

```

Une fois cette configuration en place, nous pouvons simplement modifier les valeurs des variables à l'intérieur de la requête média :

```css
@media all and (max-width: 450px) {  
  :root {  
    --columns: 200px;  
    --base-margin: 15px;  
    --base-font-size: 20px;  
}

```

Cela est beaucoup plus propre que ce que nous avions avant. Nous ne ciblons que le `:root`, au lieu de spécifier tous les sélecteurs.

Nous avons réduit notre requête média de **quatre sélecteurs à un seul** et de **treize lignes à quatre**.

Et ce n'est qu'un exemple simple. Imaginez un site web complet où, par exemple, le `--base-margin` contrôle la plupart de l'espacement libre autour de l'application. Il est beaucoup plus facile de simplement inverser la valeur de celui-ci, plutôt que de remplir votre requête média avec des sélecteurs complexes.

En résumé, les variables CSS sont définitivement l'avenir de la réactivité. Si vous souhaitez apprendre cette technologie une fois pour toutes, je vous recommande de consulter [mon cours gratuit sur le sujet sur Scrimba.](https://scrimba.com/g/gcssvariables?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article)

Vous deviendrez un maître des variables CSS en un rien de temps :)

Merci d'avoir lu ! Je suis Per Borgen, développeur front-end et co-fondateur de [Scrimba.](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) N'hésitez pas à me contacter [via Twitter](https://twitter.com/perborgen) si vous avez des questions ou des commentaires.

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) – le moyen le plus simple d'apprendre à coder. Vous devriez consulter notre [bootcamp de conception web réactive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gcssvariables_tutorial_article) si vous souhaitez apprendre à créer des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gcssvariables_tutorial_article)_