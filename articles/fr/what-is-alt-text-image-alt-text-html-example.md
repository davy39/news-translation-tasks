---
title: Qu'est-ce que le texte alternatif ? Exemple HTML de texte alternatif pour les
  images
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-16T20:39:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-alt-text-image-alt-text-html-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--1-.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
- name: image
  slug: image
seo_title: Qu'est-ce que le texte alternatif ? Exemple HTML de texte alternatif pour
  les images
seo_desc: 'Images play a significant role on our web pages. They help explain concepts
  better, make our web pages visually attractive, and lots more.

  In HTML, you use the <img> tag to embed an image into your web page.

  This <img> tag has two required attributes...'
---

Les images jouent un rôle significatif sur nos pages web. Elles aident à expliquer les concepts de manière plus claire, rendent nos pages web visuellement attrayantes, et bien plus encore.

En HTML, vous utilisez la balise `<img>` pour intégrer une image dans votre page web.

Cette balise `<img>` possède deux attributs obligatoires : `src` pour spécifier le chemin vers l'image, et `alt` pour spécifier un texte alternatif pour l'image. L'attribut `alt` est présent au cas où, pour une raison quelconque (peut-être un chemin d'image incorrect), l'image ne s'affiche pas.

```html
<img src="/my-image.jpg" alt="Ceci est le texte alternatif pour mon image">
```

Bien que l'attribut `alt` soit obligatoire dans la balise `<img>`, beaucoup de gens décident de le laisser vide ou d'y écrire un texte qui n'a aucun rapport avec l'image, juste pour s'assurer qu'il y a du texte.

La plupart des développeurs prêtent peu ou pas d'attention au texte alternatif car ils ne connaissent pas son utilité, et la plupart des tutoriels ne soulignent pas son importance.

Dans cet article, vous comprendrez ce que signifie le texte alternatif, à quoi il sert et à quel point il est utile lors de l'intégration d'une image dans votre page web. Nous mettrons également en évidence quelques points à considérer lors de la rédaction de textes alternatifs pour vos images.

## Qu'est-ce que le texte alternatif ?

Le texte alternatif ou alt est également appelé attribut alt. Il s'agit d'un texte concis et descriptif qui décrit avec précision une image.

Par défaut, ce texte n'est pas affiché lorsque vous consultez une page web dans le navigateur. Cependant, dans une situation où vous ne pouvez pas voir une image pour une raison quelconque, le texte alternatif devient visible. Ce texte doit être informatif et descriptif suffisamment pour donner au lecteur ou à l'utilisateur une idée de ce que représente l'image et du message qu'elle véhicule.

Par exemple, si vous avez une image comme celle-ci :

![Image par Erik-Jan Leusink sur Unplash](https://paper-attachments.dropbox.com/s_95E44C54B681F0DAF38695280E5CE127D3338A54647F8EF9DBA670394BC64304_1663348516195_cat.avif align="left")

Plutôt que de lui donner un texte alternatif aléatoire comme "chat" ou "Chat qui dort", vous pouvez être plus descriptif et spécifique en ajoutant un texte alternatif comme "Un chat dormant sur une couverture" ou "Un chat somnolant sur une couverture".

```html
<img src="/imgs/cat-sleeping.jpg" alt="Un chat dormant sur une couverture">
```

## Pourquoi le texte alternatif des images est-il important ?

L'attribut alt est obligatoire pour la balise `<img>`, ce qui est une raison pour laquelle vous devriez l'ajouter à vos images.

Mais il existe plusieurs autres raisons pour lesquelles vous devriez non seulement envisager d'ajouter un texte alternatif, mais plutôt un texte alternatif descriptif et informatif à vos images :

1. Lorsque vous avez des problèmes de connectivité ou que le chemin de votre image est incorrectement déclaré, votre image peut ne pas être chargée sur votre page web. Dans ce cas, la valeur du texte alternatif est affichée à la place de l'image.
    
2. Le texte alternatif fournit la signification descriptive d'une image que les moteurs de recherche peuvent utiliser pour améliorer le référencement de votre page web. Il donne aux moteurs de recherche de meilleures informations pour classer votre page web, ce qui signifie que disposer d'un texte alternatif approprié aidera votre page web à obtenir un meilleur classement.
    
3. Les utilisateurs malvoyants qui utilisent des lecteurs d'écran peuvent entendre une description de l'image. Cela montre à quel point il est utile d'améliorer l'accessibilité pour les personnes qui ne peuvent pas voir l'écran.
    
4. Lorsque vous souhaitez lier votre image à une autre page ou à un document, le texte alternatif est utilisé comme texte d'ancrage lorsque l'image ne parvient pas à se charger.
    

## Conseils pour rédiger un bon texte alternatif

Un dicton célèbre dit que "tout ce qui vaut la peine d'être fait vaut la peine d'être bien fait". Le même principe s'applique à la rédaction de votre texte alternatif – il est préférable de ne pas écrire de texte alternatif plutôt que d'écrire un mauvais ou un texte alternatif sans signification.

Voici quelques conseils à garder à l'esprit lors de la rédaction de votre texte alternatif :

### Décrivez avec précision l'image

Le principal objectif de la rédaction d'un texte alternatif est qu'il puisse servir d'alternative à une image (comme lorsque les images ne s'affichent pas ou pour les lecteurs d'écran).

Pour que le texte alternatif remplisse son rôle, il doit décrire de manière adéquate et précise l'image.

Un conseil utile est de réfléchir à une manière de décrire une image à un utilisateur qui ne peut pas voir l'image ou comme si vous la décriviez à quelqu'un au téléphone. Ensuite, rédigez le texte alternatif de cette manière.

### Gardez-le court

À ce stade, vous pourriez commencer à penser que ces textes alternatifs finiraient par prendre la forme d'un paragraphe – mais ils ne devraient pas. Dans la plupart des cas, nous devons toujours chercher la meilleure façon d'expliquer et de décrire nos images en quelques mots.

N'oubliez pas que les lecteurs d'écran peuvent tronquer le texte alternatif à environ 125 caractères, il est donc préférable de rester dans cette limite. Cependant, vous devez également toujours éviter d'utiliser un seul mot comme texte alternatif.

Par exemple, dans l'image ci-dessous, nous pouvons voir un homme debout sur un rocher surélevé regardant le ciel avec les mains tendues :

![image par Joshua Earle sur unsplash](https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80 align="left")

Un mauvais texte alternatif serait "Homme debout" ou "Homme regardant le ciel". Un meilleur texte alternatif consisterait à ajouter plus d'informations descriptives comme "Homme debout au sommet d'une montagne rocheuse pendant l'heure dorée" ou "Homme debout au sommet d'une montagne rocheuse et regardant le ciel", et ainsi de suite.

**Note :** Il existe toujours de nombreuses façons de décrire une image, mais réfléchissez toujours à une meilleure façon de décrire vos images à quelqu'un qui ne peut pas voir l'image, en rendant votre texte court mais précis.

### Utilisez des mots-clés mais évitez le bourrage de mots-clés

Lors de la description d'une image, le mot-clé ne doit pas être votre priorité absolue. Au lieu de cela, vous devez vous concentrer sur la description fidèle de votre image.

Bien que l'inclusion de vos mots-clés dans votre texte alternatif aidera votre page web à obtenir un meilleur classement sur les moteurs de recherche, il est essentiel de savoir que les moteurs de recherche ne peuvent pas reconnaître les textes alternatifs non utiles ou mauvais. Et si vous avez des mots-clés excessifs dans votre texte alternatif (bourrage de mots-clés), cela peut faire baisser le classement de votre page web.

Cela signifie que vous ne devez utiliser que des images importantes qui améliorent l'essence de votre page web et n'utiliser que les mots-clés les plus importants pour les décrire.

### Ne vous répétez pas

Évitez la répétition à tout prix. Pourquoi utiliseriez-vous le titre ou l'en-tête de votre page web comme texte alternatif ? Il est préférable de le laisser vide plutôt que de répéter les légendes ou le contenu web.

Le meilleur conseil est, lorsque vous ne pouvez pas bien décrire une image, il est préférable de laisser le texte alternatif vide plutôt que d'ajouter un texte aléatoire ou d'utiliser les légendes des images comme texte alternatif, ce qui est une répétition.

#### Légendes des images vs. Texte alternatif

Il est facile de confondre les légendes des images et le texte alternatif ou de répéter le contenu de votre texte alternatif comme légende d'image.

Les légendes décrivent les images pour aider les utilisateurs à se référer au texte environnant, tandis que le texte alternatif explique les informations dans une image ou décrit une image pour les utilisateurs de lecteurs d'écran.

Les légendes n'ont pas besoin de correspondre exactement à ce que montre l'image, mais plutôt elles expliquent comment l'image se rapporte au texte ou au contenu dans lequel elle est placée.

### N'incluez pas les mots "image" ou "photo"

L'attribut alt est utilisé dans une balise d'image, ce qui signifie que les moteurs de recherche sauront que cela est une image, il n'est donc pas nécessaire d'utiliser le mot image ou photo lors de la rédaction de textes alternatifs.

Cependant, il est bon d'aider les gens à comprendre le contexte ou le type d'image ou de photo qu'il s'agit. Par exemple, vous pourriez dire portrait, illustration, capture d'écran, graphique, et bien plus encore.

## Conclusion

Dans cet article, vous avez appris ce que signifie le texte alternatif et pourquoi il est essentiel. Vous avez également vu quelques conseils importants sur la façon de l'utiliser lors de l'intégration d'images sur votre page web.

Enfin, il est essentiel de noter que vous devez toujours ajouter un texte alternatif à vos images, y compris votre logo, les images utilisées comme boutons, et bien d'autres – et il est crucial de savoir pourquoi vous faites cela.

Mais notez que les images décoratives, dont le but principal est de décorer vos pages web plutôt que de transmettre des informations, ne nécessitent pas de texte alternatif.

Merci d'avoir lu, et assurez-vous de vous amuser en codant !