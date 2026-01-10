---
title: 5 Erreurs que les Développeurs Web Débutants Commettent – Et Comment les Corriger
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-05T16:48:42.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-beginning-web-development-students-make
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/varvara-grabova-NCSARCecw4U-unsplash-1.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: coding
  slug: coding
- name: lessons learned
  slug: lessons-learned
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: Web Development
  slug: web-development
seo_title: 5 Erreurs que les Développeurs Web Débutants Commettent – Et Comment les
  Corriger
seo_desc: 'By Dave Gray

  This list is made up of the most common mistakes I''ve witnessed during nearly a
  decade of teaching beginning web development students.

  My idea for writing this article is not to make fun of beginner mistakes or embarrass
  anyone who is be...'
---

Par Dave Gray

Cette liste est composée des erreurs les plus courantes que j'ai observées pendant près d'une décennie d'enseignement auprès d'étudiants en développement web débutants.

Mon idée en écrivant cet article n'est pas de se moquer des erreurs des débutants ou d'embarrasser qui que ce soit.

Plutôt, mon objectif est d'éduquer les débutants et, espérons-le, de les sauver de certaines de ces erreurs courantes.

## Nous Étions Tous Débutants

Si vous n'êtes pas un débutant, vous pouvez penser que les erreurs listées ci-dessous sont évidentes... mais rappelez-vous, l'évidence est relative à l'expérience.

Il fut un temps où ceux d'entre nous qui avons de l'expérience avons également lutté avec certaines de ces erreurs.

Si vous êtes un débutant, j'espère que cette liste vous fera gagner du temps et de l'anxiété dans un avenir proche.

Que le compte à rebours commence !

## Erreur #5 : Ajouter des Espaces dans les Noms de Fichiers

Vous pouvez enregistrer votre fichier HTML avec le nom "my cool page.html", mais ces espaces entre les mots sont une erreur.

Les adresses web (aka URLs) ne peuvent pas contenir d'espaces.

Si vous chargez ce fichier dans votre navigateur, vous allez voir "my%20cool%20page.html" dans la barre d'adresse du navigateur. Les espaces doivent être encodés car ils ne sont pas autorisés dans les URLs.

Si vous voulez voir une séparation entre les mots dans vos noms de fichiers, utilisez un trait de soulignement (my_cool_page.html) ou un trait d'union (my-cool-page.html).

En tant que débutant, vous n'êtes probablement pas trop inquiet de l'optimisation pour les moteurs de recherche (SEO), mais [Google a noté qu'ils préfèrent les traits d'union](https://developers.google.com/search/docs/advanced/guidelines/url-structure) dans les noms de fichiers plutôt que les traits de soulignement.

## Erreur #4 : Ignorer la Sensibilité à la Casse

Si vous utilisez Windows pour votre environnement de développement, vous ne remarquerez peut-être pas de problème lorsque vous utilisez de manière incohérente des lettres minuscules et majuscules. C'est une erreur.

Supposons que vous avez créé un dossier CSS nommé "Css" et un fichier à l'intérieur nommé "Main.css". Mais dans votre code, vous le liez comme ceci :

```
<link rel="stylesheet" href="css/main.css">
```

Pendant que vous travaillez sur votre projet, il n'y a pas de problème.

Mais lorsque vous chargez votre projet sur un serveur web... **Boum !** Aucun CSS n'est appliqué.

De nombreux serveurs web exécutent une version de Linux ou Unix au lieu de Windows. Vous avez peut-être entendu parler de la pile LAMP. Linux est le L dans LAMP.

Ces systèmes sont sensibles à la casse.

Par conséquent, il est préférable d'utiliser des noms de fichiers et de répertoires en minuscules tout le temps, sauf s'il existe une convention de nommage spécifique qui utilise une lettre majuscule. À ce moment-là, les noms de fichiers seront toujours cohérents. Et la cohérence est ce qui empêchera cette erreur.

## Erreur #3 : Ne Pas Comprendre les Chemins de Fichiers

Les étudiants qui ne comprennent pas comment lier des fichiers dans différents répertoires mettent souvent tous leurs fichiers dans le répertoire racine afin d'y accéder. C'est une erreur qui conduit à une arborescence de fichiers désorganisée.

Peu de temps après avoir commencé à apprendre le HTML, vous commencez à apprendre comment lier d'autres fichiers HTML et CSS.

Cela est assez simple lorsque les fichiers sont dans le même répertoire. Même dans l'exemple ci-dessus, nous avons simplement regardé à l'intérieur du répertoire CSS pour le fichier main.css.

Cela commence à devenir plus compliqué lorsque nous devons remonter d'un répertoire au lieu de (ou avant de) descendre dans un autre.

Dans l'exemple ci-dessous, nous définissons l'image de fond pour une page web dans notre fichier main.css. Le fichier main.css est dans le répertoire CSS. Nous faisons un lien vers une image dans le répertoire img.

```
body {
     background-image: url("../img/moon.png");
}
```

Ces deux répertoires (aka dossiers) sont dans le répertoire racine. Par conséquent, nous devons remonter et sortir du répertoire CSS, puis descendre dans le répertoire img.

Nous remontons d'un répertoire avec deux points : ".."

De là, nous descendons dans le répertoire img pour lier le fichier moon.png.

Si nous devions remonter de deux répertoires, le chemin de fichier commencerait comme ceci : "../../"

Rappelez-vous, un point indique le répertoire dans lequel vous vous trouvez. Deux points indiquent le répertoire au-dessus de celui où vous vous trouvez actuellement.

## Erreur #2 : Ne Pas Nommer Votre Page par Défaut Index

Nommer votre page par défaut autre chose que "index" est une erreur.

Les serveurs web recherchent un fichier index.

Lorsque vous travaillez avec HTML, vous devriez avoir un fichier index.html.

Ce fichier se chargera par défaut sans afficher le nom du fichier à la fin de l'URL.

C'est pourquoi vous pouvez aller sur votre site .com préféré ou une autre adresse web et ne pas voir "/index.html" après leur ".com". Le fichier index se charge par défaut.

Certes, votre site préféré peut utiliser plus que du HTML, mais ce concept s'applique à d'autres technologies comme PHP (index.php), React (index.js), et plus encore.

Alors que vous continuez à apprendre, vous trouverez que certains développeurs choisissent d'autres noms de fichiers lorsqu'ils utilisent d'autres technologies, mais en tant que débutant, restez avec index.

## Erreur #1 : Ne Pas Prendre de Pause !

Je reçois des emails lorsque les étudiants sont frustrés.

Ils ont passé des heures sur leur projet et ne trouvent pas l'erreur.

Souvent, le problème est une balise ou une variable mal orthographiée, un point-virgule manquant, ou une autre petite erreur de syntaxe.

_Cela arrive à nous tous._

Après avoir fixé le code pendant une période prolongée, notre vision se trouble, notre cerveau s'embrouille, et ce qui aurait été facile à voir avec des yeux frais devient impossible.

Ne vous sentez pas mal. Ne vous blâmez pas. Levez-vous simplement !

Faites une promenade. Prenez un café. Faites une sieste. Tout ce qui vous sort de la brume et vous donne des yeux frais et un esprit clair à nouveau.

Vraiment, cette erreur n'est pas seulement pour les débutants. Cela peut arriver à n'importe qui.

Je dois me rappeler de prendre des pauses, aussi.

Revenez au code lorsque vous êtes rafraîchi et cette erreur que vous ne trouviez pas sera souvent évidente !

## Conclusion

À mesure que vous gagnez de l'expérience, vous dépasserez rapidement ces erreurs courantes.

Ce qui était autrefois difficile à comprendre deviendra clair.

Si ces erreurs courantes vous semblaient évidentes, félicitations ! Vous avez déjà acquis de l'expérience.

Si vous commencez tout juste, j'espère que cette revue des erreurs courantes des débutants vous fera gagner du temps et de la frustration dans un avenir proche.

Je vous laisse avec une vidéo de ma chaîne YouTube qui compte les 10 plus grosses erreurs des débutants. Regardez pour voir des exemples des 5 erreurs dont j'ai discuté dans cet article plus 5 erreurs courantes supplémentaires des débutants :

%[https://youtu.be/5xkztyg12FU]