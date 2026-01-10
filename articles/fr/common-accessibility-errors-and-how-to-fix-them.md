---
title: Erreurs d'accessibilité courantes et comment les corriger
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2022-01-05T21:15:24.000Z'
originalURL: https://freecodecamp.org/news/common-accessibility-errors-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/accessibility-errors-article-image.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
seo_title: Erreurs d'accessibilité courantes et comment les corriger
seo_desc: 'The Web Content Accessibility Guidelines, or WCAG, defines how to make
  websites accessible for people with disabilities.

  When we evaluate whether or not website is accessible, we look to see if software
  meets WCAG 2 standards.

  Accessibility should no...'
---

Les Règles pour l'accessibilité des contenus Web, ou WCAG, définissent comment rendre les sites web accessibles aux personnes handicapées.

Lorsque nous évaluons si un site web est accessible ou non, nous vérifions si le logiciel respecte les normes WCAG 2.

L'accessibilité ne doit pas être une réflexion après coup, mais plutôt une partie majeure du processus de développement. Pourtant, malheureusement, de nos jours, de nombreux sites web présentent des erreurs d'accessibilité.

[L'audit de WCAG](https://webaim.org/projects/million/#errors) montre que de nombreuses erreurs d'accessibilité se répartissent en seulement six domaines/catégories.

<table><tbody><tr><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p>Types les plus courants d'échecs WCAG 2</p></td></tr><tr><th colspan="1" rowspan="1"><p>Type d'échec WCAG</p></th><th colspan="1" rowspan="1"><p>% des pages d'accueil en février 2021</p></th><th colspan="1" rowspan="1"><p>% des pages d'accueil en février 2020</p></th><th colspan="1" rowspan="1"><p>% des pages d'accueil en février 2019</p></th></tr><tr><td colspan="1" rowspan="1"><p>Texte à faible contraste</p></td><td colspan="1" rowspan="1"><p>86,4%</p></td><td colspan="1" rowspan="1"><p>86,3%</p></td><td colspan="1" rowspan="1"><p>85,3%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Texte alternatif manquant pour les images</p></td><td colspan="1" rowspan="1"><p>60,6%</p></td><td colspan="1" rowspan="1"><p>66,0%</p></td><td colspan="1" rowspan="1"><p>68,0%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Étiquettes de saisie de formulaire manquantes</p></td><td colspan="1" rowspan="1"><p>54,4%</p></td><td colspan="1" rowspan="1"><p>53,8%</p></td><td colspan="1" rowspan="1"><p>52,8%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Liens vides</p></td><td colspan="1" rowspan="1"><p>51,3%</p></td><td colspan="1" rowspan="1"><p>59,9%</p></td><td colspan="1" rowspan="1"><p>58,1%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Langue du document manquante</p></td><td colspan="1" rowspan="1"><p>28,9%</p></td><td colspan="1" rowspan="1"><p>28,0%</p></td><td colspan="1" rowspan="1"><p>33,1%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Boutons vides</p></td><td colspan="1" rowspan="1"><p>26,9%</p></td><td colspan="1" rowspan="1"><p>28,7%</p></td><td colspan="1" rowspan="1"><p>25,0%</p></td></tr></tbody></table>

> 96,7 % de toutes les erreurs détectées tombent dans ces six catégories. S'attaquer à ces quelques types de problèmes améliorerait considérablement l'accessibilité sur le web. – [WebAIM](https://webaim.org/projects/million/#errors)

Si nous résolvons ces six problèmes, nous pouvons nous assurer que plus de sites web sont accessibles pour les personnes qui utilisent diverses technologies d'assistance.

Examinons chacun de ces problèmes d'accessibilité courants plus en détail.

## Mettre à jour le texte à faible contraste

%[https://codepen.io/ilkxeren/pen/qBPVRxL]

Dans l'exemple de code ci-dessus, nous pouvons voir un exemple de combinaison de couleurs de premier plan/arrière-plan qui respecte les normes WCAG et un autre qui ne les respecte pas.

Le faible contraste de couleur est celui avec un fond bleu et un texte gris. Il est vraiment difficile de différencier visuellement les couleurs de premier plan et d'arrière-plan, et la combinaison de couleurs ne respecte pas les normes WCAG. Le texte de premier plan se fond dans l'arrière-plan.

Dans le deuxième exemple, le premier plan est de couleur blanchâtre et il est facile de lire le texte. Cette combinaison de couleurs respecte la norme WCAG, et le texte se détache et est facile à lire.

Si la couleur du texte est difficile à différencier de l'arrière-plan dans lequel il se trouve, nous avons une erreur d'accessibilité de faible contraste. Au cours des trois dernières années, de loin la plus grande erreur d'accessibilité est le texte à faible contraste. Plus de 80 % des sites web présentent cette erreur d'accessibilité.

Vous pouvez corriger les erreurs d'accessibilité de faible contraste en auditant simplement votre site web et en changeant la couleur du texte ou de l'arrière-plan. Vous pouvez [exécuter un test lighthouse](https://developers.google.com/web/tools/lighthouse) pour voir si le contraste des couleurs est un problème sur votre site web.

Vous pouvez également vérifier si la combinaison de couleurs de premier plan/arrière-plan respecte les normes WCAG dans le lien suivant : [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/).

## Ajouter un texte alternatif manquant pour les images

En 2021, il a été rapporté que 60,6 % de toutes les images des pages d'accueil manquaient de texte alternatif.

Il est important d'ajouter un texte alternatif aux images car vous devez décrire le contenu de la page à ceux qui ne peuvent pas voir le contenu. Les utilisateurs malvoyants utiliseront un lecteur d'écran, qui lira le contenu de la page à voix haute.

Par exemple, si nous avons une image d'un panier de frites belges, nous pouvons ajouter une balise alternative à cette image avec un simple attribut alt :

```html
<img src="example.png" alt="panier de frites"/>
```

Avec un attribut, `alt`, nous sommes en mesure de rendre l'image accessible pour les utilisateurs de lecteurs d'écran. Lorsqu'un utilisateur de lecteur d'écran passe à l'image, il lui indiquera qu'il est concentré sur une image et que cette image est un "panier de frites".

Si nous n'avions pas d'attribut alt, alors l'utilisateur de lecteur d'écran ne saurait pas que l'image sur laquelle il était concentré était un panier de frites.

Il est également important de noter qu'un attribut `alt` n'est pas suffisant pour des images 100 % accessibles. Nous devons également nous assurer que la balise alt est descriptive et informe l'utilisateur de l'apparence de l'image.

Un mauvais exemple de balise alt serait si elle n'est pas assez descriptive. Supposons que nous avons la même image du panier de frites et que nous ajoutons une balise alt à l'image comme suit :

```html
<img src="example.png" alt="image"/>
```

Dans l'exemple ci-dessus, nous respecterions les normes d'accessibilité en ajoutant la balise alt, mais la balise alt n'est pas utile ou assez descriptive pour les utilisateurs de lecteurs d'écran. Lorsqu'un utilisateur de lecteur d'écran se concentre sur cette image, il dira "image, image", ce qui ne permet pas à l'utilisateur de savoir ce qu'est cette image.

Il est très important d'ajouter une balise alternative descriptive aux images sur la page.

## Ajouter des étiquettes de saisie de formulaire manquantes

Environ la moitié des sites web manquaient d'étiquettes de saisie de formulaire en 2021. Une étiquette de formulaire est un élément HTML utilisé dans les formulaires pour décrire à quoi servent les différents champs du formulaire.

Si vous avez un type de formulaire sur la page, qu'il s'agisse d'une case à cocher, d'un bouton radio ou d'une liste déroulante, vous devez avoir une balise `<label>` associée à ce formulaire.

Une erreur courante pour les saisies de formulaire manquantes concerne les formulaires de recherche. Souvent, les formulaires de recherche sur une page ont généralement seulement une image de loupe pour indiquer aux utilisateurs visuels qu'ils peuvent rechercher avec ce formulaire, mais aucune étiquette pour indiquer la recherche. Mais si nous n'ajoutons pas d'étiquette à ce formulaire, les utilisateurs de lecteurs d'écran ne sauront pas à quoi sert le formulaire lorsqu'ils se concentrent dessus.

Nous pouvons corriger cette erreur d'accessibilité en ajoutant une étiquette de lecteur d'écran.

Exemple HTML :

```php
<label for="searchLabel" class="sr-only">Recherche</label>
<input type="text" name="search" id="searchLabel">
<input type="submit" value="Recherche">
```

Exemple CSS :

```php
.sr-only{
   position:absolute;
   left:-10000px;
   top:auto;
   width:1px;
   height:1px;
   overflow:hidden;
}
```

Dans l'exemple ci-dessus, nous avons ajouté une étiquette "Recherche" au formulaire à l'aide de CSS. Lorsqu'un utilisateur se concentre sur ce formulaire particulier, le lecteur d'écran lira "Recherche" pour lui. La classe `sr-only` dans ce formulaire rendra cet élément lisible uniquement lorsqu'il est utilisé avec un lecteur d'écran.

## Corriger les liens vides

Les liens sont utilisés pour naviguer vers une nouvelle page ou vue. Un lien peut être focalisé par le clavier et peut être déclenché par la touche Entrée.

Similaire à l'erreur d'étiquette de formulaire manquante, une autre erreur d'accessibilité est les liens vides. Environ la moitié des sites web avaient des liens vides en 2021.

Par exemple, si nous utilisons le logo Facebook pour indiquer aux utilisateurs voyants que le lien mène à Facebook, mais que nous n'ajoutons aucune étiquette pour les utilisateurs de lecteurs d'écran, alors nous obtiendrons une erreur d'accessibilité de lien vide.

Si nous n'ajoutons pas de texte pour les lecteurs d'écran, alors les utilisateurs de lecteurs d'écran ne sauront pas qu'ils sont concentrés sur un logo Facebook.

Un bon exemple d'ajout d'une étiquette à un lien est ci-dessous :

```php
<a href="/facebook-page">
   <i aria-hidden="true"></i>
   <span class="sr-only">Facebook</span>
</a>
```

CSS correspondant :

```php
.sr-only{
   position:absolute;
   left:-10000px;
   top:auto;
   width:1px;
   height:1px;
   overflow:hidden;
}
```

Dans l'exemple ci-dessus, nous avons utilisé un logo Facebook pour indiquer qu'il s'agit d'un lien Facebook. Nous avons également ajouté le texte "Facebook" qui sera lu lorsque les utilisateurs se concentreront dessus en utilisant un lecteur d'écran.

## Ajouter la langue du document manquante

Au cours des trois dernières années, entre 28 % et 33 % des pages d'accueil manquaient d'une langue de document sur leur page. Il s'agit de l'un des problèmes d'accessibilité les moins courants, mais c'est toujours une erreur d'accessibilité à laquelle nous devons prêter attention et corriger.

Nous pouvons ajouter la langue à la balise HTML comme suit :

```php
<html lang="fr">
...
</html>
```

L'exemple ci-dessus indique que la page est en français. Nous pouvons utiliser d'autres codes pour indiquer d'autres langues.

Il est important d'indiquer la langue de la page car les lecteurs d'écran utilisent la langue du document pour savoir comment prononcer les mots. La langue du document est également bonne pour le SEO.

## Corriger les boutons vides

Les boutons sont utilisés pour effectuer des actions sur une page, par exemple soumettre un formulaire ou afficher/masquer des éléments. Un bouton peut être focalisé et peut être déclenché par la touche espace.

Similaire aux liens vides, nous devons nous assurer que les boutons ont du texte pour que les lecteurs d'écran puissent le lire lorsqu'ils sont focalisés.

La solution pour corriger les boutons vides est similaire à celle pour corriger les liens vides, c'est-à-dire s'assurer que l'étiquette de texte est présente sur les boutons.

Si une image est utilisée à l'intérieur d'un bouton, nous pouvons ajouter une balise alt à l'image. Cela garantira que lorsque l'utilisateur utilise un lecteur d'écran, la balise alt de l'image est lue. Voici un exemple de la manière de procéder ci-dessous :

```php
<button type="submit">
   <img src="/search.svg" alt="Recherche"/>
</button>
```

De manière similaire à une image, si vous utilisez un SVG à l'intérieur d'un bouton, vous pouvez ajouter un titre à l'intérieur du SVG. Voici un exemple de la manière de procéder ci-dessous :

```php
<button type="submit">
   <svg id="search" role="img" aria-describedby="search" viewBox="0 0 16 16.9">
      <title id="search">Recherche</title>
      <path d="M14, 2L8690, 89.1,13,6.5G87"></path>
   </svg>
</button>
```

Nous devons nous assurer que les boutons ne sont pas vides et que les lecteurs d'écran lisent ce que le bouton est à l'utilisateur.

## Conclusion

L'accessibilité ne doit jamais être une réflexion après coup, mais plutôt une grande partie du processus de développement. La plupart des erreurs d'accessibilité proviennent de six catégories et si nous les corrigeons, nous rendrons nos sites web plus accessibles à tous.

Les corrections d'accessibilité ne doivent pas être difficiles et ne doivent nécessiter que des connaissances de base en HTML et CSS.

Si nous prêtons plus d'attention à l'accessibilité, nous ouvrirons nos sites web à un public plus large et nous nous assurerons également que notre code est bon et respecte les normes. L'accessibilité aide non seulement tout le monde à utiliser les sites web, mais améliore également la base de notre code.