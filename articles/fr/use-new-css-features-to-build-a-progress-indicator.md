---
title: Comment utiliser les nouvelles fonctionnalités CSS pour créer un indicateur
  de progression
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2024-01-09T15:39:50.000Z'
originalURL: https://freecodecamp.org/news/use-new-css-features-to-build-a-progress-indicator
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/open-graph.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les nouvelles fonctionnalités CSS pour créer un indicateur
  de progression
seo_desc: 'For the last 7 months, I’ve had my head down building Component Odyssey.
  It’s been a richly fulfilling project and I’m eager for people to take the course
  and learn heaps about building component libraries using web components.

  I’ve seen some incredi...'
---

Pendant les 7 derniers mois, j'ai travaillé sans relâche sur [Component Odyssey](https://component-odyssey.com/). Ce projet a été extrêmement enrichissant et je suis impatient que les gens suivent le cours et apprennent énormément sur la création de bibliothèques de composants en utilisant les composants web.

J'ai vu des démonstrations incroyables au cours de l'année passée et je voulais me plonger dans certaines de ces nouvelles fonctionnalités passionnantes. J'ai donc utilisé un peu de temps libre pendant la période de Noël pour intégrer de nombreuses nouvelles fonctionnalités CSS dans un indicateur de progression de leçon pour la plateforme Component Odyssey.

Le résultat est l'indicateur de progression suivant qui montre combien de la page l'utilisateur a fait défiler :

![l'indicateur de progression entièrement complété tel qu'il existe sur Component Odyssey](https://www.freecodecamp.org/news/content/images/2024/01/component-odyssey-indicator.gif)

La création de cet indicateur m'a permis de découvrir certaines des dernières fonctionnalités CSS comme :

* `animation-timeline: scroll()`
* Les fonctions trigonométriques CSS, `sin()` et `cos()`
* `color-mix()`
* La règle `@property`

Je connais les risques de construire quelque chose avec un outil particulier en tête. Comme le dit le proverbe, « Quand on n'a qu'un marteau, alors quelque chose quelque chose clous ».

Oui, j'ai un marteau, et je vais m'en servir pour abattre les murs.

Dans cet article, je vais vous expliquer comment créer une version simplifiée de cette animation de progression élégante tout en utilisant toutes les fonctionnalités CSS mentionnées ci-dessus. Je vais également vous montrer comment gérer élégamment les navigateurs qui ne supportent pas ces fonctionnalités grâce à l'**amélioration progressive**.

Si vous souhaitez suivre ce tutoriel, il est préférable d'utiliser les dernières versions de Chrome ou Safari - actuellement, Firefox ne supporte pas généralement des propriétés comme `animation-timeline`. Commencez par plonger dans le [Codepen de démarrage](https://codepen.io/andrico1234/pen/WNmQrGK).

Si vous souhaitez consulter le code final, vous pouvez [le vérifier ici](https://codepen.io/andrico1234/pen/qBvdjLd).

## Comment créer le balisage

J'ai déjà fourni un peu de balisage pour simuler une page avec suffisamment de contenu pour que vous deviez faire défiler jusqu'en bas. Pour commencer à créer l'indicateur de progression, vous devrez ajouter un peu plus de balisage.

Le balisage lui-même est vraiment simple - nous n'aurons besoin de créer que 3 éléments div.

L'élément extérieur est responsable du positionnement et de la mise en page du chargeur. Nous lui donnerons une classe `wrapper`.

L'élément du milieu est responsable du rendu de la piste à l'écran. Nous donnerons à cet élément une classe `progress`. Nous utiliserons plus tard un pseudo-élément `::after` pour créer le _curseur de l'indicateur_.

L'élément le plus interne sera utilisé pour créer le trou circulaire au milieu, faisant ressembler l'indicateur à un beignet hypocalorique. Celui-ci aura une classe `inner`.

Jetez un coup d'œil à ce qui suit si vous avez besoin d'aide pour visualiser la structure :

![Une représentation visuelle des informations décrites ci-dessus](https://www.freecodecamp.org/news/content/images/2024/01/markup-structure.png)
_Illustration de la structure du balisage_

Fournissez le balisage suivant comme premier enfant de l'élément `main` crée le balisage suivant :

```html
<div class="wrapper">
	<div class="progress">
		<div class="inner"></div>
	</div>
</div>
```

### Application du CSS de base au balisage

Vous devrez également appliquer les styles suivants pour donner au balisage une apparence visuelle de base :

```css
.wrapper {
	--size: 80px;

	position: fixed;
	width: var(--size);
	aspect-ratio: 1/1;
	top: 24px;
	left: 24px;
	display: flex;
	align-items: center;
	justify-content: center;
}

.progress {
	--track-size: 16px;

	width: var(--size);
	aspect-ratio: 1/1;
	border-radius: 50%;
}

.inner {
	position: absolute;
	width: calc(100% - var(--track-size));
	aspect-ratio: 1/1;
	background: var(--background-color);
	border-radius: 50%;
	top: 0;
	left: 0;
	right: 0;
	bottom: 0;
	margin: auto;
}
```

La plupart du CSS ici ne devrait pas vous surprendre, donc je ne vais pas le passer en revue ligne par ligne. Mais je vais aborder quelques-uns des éléments les plus intéressants.

Dans `.wrapper`, nous fixons l'élément en haut à gauche de l'écran, et nous utilisons Flexbox pour centrer les enfants horizontalement et verticalement.

💡 J'ai appris que si vous voulez qu'un élément partage la même valeur pour sa largeur et sa hauteur, vous définissez simplement la largeur et utilisez `aspect-ratio: 1/1`. Le navigateur définira implicitement la hauteur.

C'est une astuce pratique car vous n'aurez pas à définir la même valeur deux fois, et cela facilite la garantie que la largeur et la hauteur partagent la même valeur.

En ce qui concerne l'élément `.inner`, j'ai utilisé un mélange de positionnement absolu et de `margin: auto` pour le centrer au milieu de l'élément `.progress`. Nous avons également déduit la `--track-size` de la largeur totale du conteneur, pour nous assurer qu'il est correctement positionné sur l'élément `.progress`.

Vous ne pourrez pas encore voir grand-chose, mais si vous ajoutez un `background-color: red` temporaire à l'élément `.progress`, il devrait s'afficher comme suit :

![un indicateur en forme de beignet basique sans aucune animation](https://www.freecodecamp.org/news/content/images/2024/01/basic-ui.png)
_Image montrant l'état actuel de l'indicateur de progression - un cercle rouge_

## Comment créer un indicateur de progression animé

La création d'une animation pilotée par le défilement de ce type nécessite de nombreuses nouvelles fonctionnalités CSS que vous n'avez peut-être pas utilisées auparavant. Au lieu d'apprendre tout en même temps, nous allons commencer par découpler l'animation des mécanismes de défilement.

De cette façon, à la fin de cette section, vous devriez avoir l'animation suivante qui se joue automatiquement :

![Un indicateur de progression jouant automatiquement en boucle infinie](https://www.freecodecamp.org/news/content/images/2024/01/infinite-loading.gif)
_Animation montrant la phase initiale de l'indicateur de progression_

Nous allons commencer par créer une nouvelle animation appelée `load` :

```css
@keyframes load {
	0% {
		--progress: 0%;
	}

	100% {
		--progress: 100%;
	}
}
```

Tout ce que cela fait est de faire avancer la progression de 0 à 100 au cours de l'animation.

### Utilisation de `conic-gradient` pour indiquer la progression actuelle

Dans votre règle `.progress`, ajoutez les propriétés CSS suivantes :

```css
.progress {
	# Règles existantes

	animation: load linear 1s infinite;
	background: conic-gradient(
		from 0deg at 50% 50%,
		var(--red) var(--progress),
		var(--black) var(--progress)
	)
}
```

La propriété `animation` devrait être assez simple, mais il se passe beaucoup de choses avec la règle `background`, alors décomposons-la.

Pour commencer, nous utilisons un `conic-gradient` car cela nous permet d'animer facilement l'arrière-plan sur 360 degrés, comme montré dans l'animation ci-dessus. Nous commençons à partir de la position `0deg`, qui est en haut et au centre. Nous décrivons où nous voulons que le centre du dégradé soit en utilisant `at 50% 50%`.

`conic-gradient(from 0deg at 50% 50%)` seul rendrait quelque chose comme ce qui suit :

![Une visualisation d'un dégradé radial commençant à partir du centre, comme un radar sonar](https://www.freecodecamp.org/news/content/images/2024/01/radial-gradient.png)
_Image montrant un cercle rouge avec un léger dégradé, le résultat de `conic-gradient(from 0deg at 50% 50%)` seul_

J'espère avoir rendu clair pourquoi c'est le cas.

En ce qui concerne les deuxième et troisième arguments de la fonction `conic-gradient`, nous relions la variable `--progress` (qui est calculée via l'animation `load`) aux deux couleurs. Le `--red` est utilisé pour désigner la progression terminée, tandis que le `--black` est utilisé pour désigner la position restante.

Il peut être déroutant de savoir pourquoi ils partagent la même valeur `--progress`. La valeur `--progress` pour la valeur `--red` indique où l'arrêt du dégradé se termine, tandis que la valeur `--progress` pour le `--black` indique où l'arrêt du dégradé commence.

Parce que c'est le dernier arrêt du dégradé, il est sous-entendu qu'il se termine à 100%. En définissant la même valeur `--progress` pour les deux arrêts du dégradé, nous créons une transition nette entre les deux couleurs. Sans cela, notre indicateur de progression (avec une valeur `--progress` définie à 16%) ressemblerait à ceci :

![L'indicateur de progression où le dégradé de couleur passe lentement du rouge au noir](https://www.freecodecamp.org/news/content/images/2024/01/radial-gradient-no-stop.png)
_Indicateur de progression avec un dégradé de rouge à noir et sans animation_

### Animation du dégradé

Maintenant, quelque chose d'étrange se produit probablement. Au lieu que votre indicateur de progression passe en douceur sur tout le périmètre du cercle, il clignote entre le noir et le rouge.

Pourquoi cela se produit-il ?

C'est parce que nous demandons au navigateur d'interpoler entre des valeurs de pourcentage, ce qu'il ne peut pas faire automatiquement. Même si nous avons donné à la variable `--progress` une valeur de pourcentage, le navigateur ne suppose pas qu'elle sera toujours une valeur de pourcentage.

Nous pouvons résoudre ce problème en indiquant au navigateur que `--progress` sera toujours une valeur de pourcentage. Nous pouvons le faire en définissant explicitement la propriété `--progress` en utilisant la règle `@property` CSS. Il suffit d'ajouter ce qui suit au niveau supérieur de votre CSS :

```css
@property --progress {
	syntax: '<percentage>';
	inherits: false;
	initial-value: 0%;
}
```

Nous indiquons au navigateur que `--progress` doit uniquement supporter les valeurs de pourcentage et que la valeur initiale est 0%. Nous ne sommes également pas intéressés à ce que l'élément personnalisé hérite de sa valeur.

Enfin, je n'aime pas trop l'utilisation de la variable `--black` pour signifier une progression vide. Cela semble trop marqué. J'aimerais créer une teinte plus claire à partir du noir pour garantir une palette visuelle plus homogène. C'est quelque chose que nous pouvons facilement réaliser en utilisant la fonction CSS `color-mix()`.

Remontez à la règle CSS `:root` et ajoutez la variable suivante :

```css
:root {
	# vos autres variables CSS

	--grey: color-mix(in srgb, var(--black), transparent 60%);
}
```

La fonction `color-mix` nous permet de mélanger deux couleurs ensemble. Dans ce cas, nous mélangeons la couleur stockée dans notre variable noire avec un peu de transparence, ce qui donnera une couleur grise partiellement transparente. Vous devrez remplacer la référence à la variable `--black` dans la fonction `conic-gradient` par `--grey` pour voir l'effet du changement de couleur.

Maintenant que nous avons défini notre propriété personnalisée, le navigateur pourra interpoler les valeurs correctes pendant toute l'animation, donc elle devrait maintenant passer en douceur du début à la fin.

![Un indicateur de progression jouant automatiquement en boucle infinie](https://www.freecodecamp.org/news/content/images/2024/01/infinite-loading-1.gif)
_Montrant l'animation fonctionnant correctement_

## Comment activer les animations pilotées par le défilement

La prochaine étape de notre parcours d'animation est de lier notre animation au défilement de la page.

Cela ne devrait nous prendre que quelques lignes de CSS.

Vous devrez faire deux choses : d'abord ajuster la propriété `animation` dans votre classe `.progress` pour supprimer la valeur `infinite`, et changer la durée de `1s` à `1ms`. Nous ne pouvons pas supprimer la valeur complètement car Firefox en a besoin pour que les animations de défilement fonctionnent.

Ensuite, mettez à jour votre classe `.progress` pour inclure ce qui suit :

```css
.progress {
  # autres propriétés CSS

	animation-timeline: scroll(nearest block);
}
```

La propriété `animation-timeline` indique au navigateur de lier la progression de l'animation à une timeline spécifique. Dans ce cas, il s'agit de la timeline de défilement, que nous spécifions en utilisant la fonction `scroll`.

Vous pouvez voir que je fournis deux arguments à `scroll()` : `nearest` et `block`.

La valeur `nearest` est utilisée pour lier l'animation à l'ancêtre le plus proche qui a une barre de défilement. Dans ce cas, il s'agit du document. Si vous êtes certain de ne vouloir lier l'animation qu'à la barre de défilement du document, vous pouvez remplacer `nearest` par `root`.

La propriété `block` désigne l'axe auquel nous voulons lier notre animation. Dans la plupart des cas, il s'agira de la barre de défilement verticale, mais pour les modes d'écriture verticaux, il s'agira de la barre de défilement horizontale.

Maintenant que vous avez lié l'animation au défilement de votre page, vous devriez pouvoir faire défiler la page vers le haut et vers le bas et observer comment votre animation change en conséquence.

![L'indicateur de progression de base dont l'animation est liée à la progression du défilement de la page](https://www.freecodecamp.org/news/content/images/2024/01/progress-complete.gif)
_Démo montrant un utilisateur faisant défiler et l'animation de l'élément de défilement changeant_

## Comment améliorer progressivement votre animation de défilement

Bien qu'il soit passionnant d'utiliser ces nouvelles fonctionnalités dans le navigateur, la propriété `animation-timeline` ne bénéficie pas encore d'un support universel dans tous les navigateurs. Elle est encore très nouvelle dans Chrome, et elle n'est disponible dans Firefox que derrière un drapeau de fonctionnalité. Si vous essayez d'ouvrir le code dans Firefox, vous remarquerez que l'anneau de progression apparaît simplement avec une animation terminée.

Dans des cas comme celui-ci, il est important de mettre en place une expérience de base solide pour tous les navigateurs, puis d'_améliorer progressivement_ votre page web avec les nouvelles fonctionnalités sur les navigateurs compatibles. Comme l'indicateur de progression n'est pas critique pour le fonctionnement de l'application, nous pouvons simplement le masquer si le navigateur ne supporte pas la propriété `animation-timeline`.

Nous pouvons le faire en déplaçant nos classes `.wrapper`, `.progress` et `.inner` à l'intérieur de la règle `@supports` de CSS, comme suit :

```css
@supports (animation-timeline: scroll()) {
	.wrapper {}

	.progress {}

	.inner {}
}
```

En faisant cela, nous nous assurons que si le navigateur ne supporte pas `scroll()`, il ignorera tous les styles contenus dans la règle.

## Comment ajouter le curseur de l'indicateur

La dernière chose que nous devons ajouter est un petit curseur d'indicateur, pour donner à notre indicateur de progression un peu plus d'intérêt visuel et pour nous permettre de jouer avec les fonctions trigonométriques CSS élégantes.

Le _curseur de l'indicateur_ est le petit élément circulaire qui indique la progression exacte actuelle.

![Le curseur de l'indicateur placé à 4 heures sur l'indicateur de progression](https://www.freecodecamp.org/news/content/images/2024/01/thumb-indicator.png)
_Illustration montrant le curseur de l'indicateur (un point sombre sur l'indicateur de progression)_

### Création de l'apparence visuelle du curseur

Pour créer le curseur de l'indicateur, commencez par écrire le CSS suivant à l'intérieur du bloc `@supports` :

```css
.progress::after {
	--radius: calc(var(--size) / 2);
	--track-offset: calc(var(--track-size) / 4);

	content: '';
	position: absolute;
	aspect-ratio: 1/1;
	width: calc(var(--track-size) / 2);
	background: var(--red-dark);
	border-radius: 50%;
	left: calc(50% - var(--track-offset));
	top: calc(50% - var(--track-offset));
	transform: scale(1.5);
}
```

Cela crée un nouvel élément pseudo à partir de la classe `.progress`, et lui donne son apparence visuelle. Une fois ajouté, le curseur de l'indicateur devrait se trouver dans l'élément de progression central. Nous utilisons la variable `--track-offset` pour positionner correctement le curseur en tenant compte des dimensions de la piste.

⚠️ Je augmente également la taille du curseur en utilisant `scale()` afin que sa taille dans le DOM soit toujours relative à la variable `--size`. Cela signifie simplement un peu moins de mathématiques pour nous lorsque nous définissons la valeur de `--track-offset`. L'utilisation de `scale()` facilite le changement de la taille de l'élément sans provoquer de décalage dans le DOM.

L'étape suivante consiste à utiliser à nouveau la fonction `color-mix()` pour créer un rouge foncé à partir de la couleur rouge de base. Ajoutez ce qui suit à votre règle `:root`.

```css
:root {
	# vos autres variables CSS

	--red-dark: color-mix(in srgb, var(--red), var(--black) 60%);
}
```

Votre indicateur de progression devrait ressembler moins à un widget d'interface utilisateur et plus à une cible de fléchettes :

![le curseur est au centre de l'indicateur de progression](https://www.freecodecamp.org/news/content/images/2024/01/bullseye.png)
_Animation/curseur de l'indicateur en cours_

### Positionnement du curseur sur la piste

Positionnons le curseur sur la piste.

```css
.progress::before {
  # reste des propriétés

	translate: calc((var(--radius) - var(--track-offset)) * cos(var(--angle)))
      calc((var(--radius) - var(--track-offset)) * sin(var(--angle)));
}

```

C'est probablement le morceau de CSS le plus compliqué de tout cet article. Il n'est pas aussi complexe si nous le décomposons en deux. Voici la première moitié :

```css
calc((var(--radius) - var(--track-offset)) * cos(var(--angle)))
```

Cela utilise un peu de trigonométrie pour calculer la position du curseur en fonction de l'angle actuel (qui sera lié à la progression du défilement) et du rayon du cercle. La fonction `cos()` est utilisée pour déterminer la valeur horizontale de la position.

La deuxième moitié de la valeur est identique, sauf que nous utilisons la fonction `sin()` pour déterminer la position verticale de l'indicateur :

```css
calc((var(--radius) - var(--track-offset)) * sin(var(--angle)))
```

⚠️ Je ne vais pas utiliser cet article comme une introduction à la trigonométrie, mais je peux vous orienter vers des ressources incroyables :

* [Fonctions trigonométriques en CSS](https://web.dev/articles/css-trig-functions)
* [Fonctions trigonométriques en CSS et JavaScript : Au-delà des triangles](https://tympanus.net/codrops/2021/06/04/trigonometry-in-css-and-javascript-beyond-triangles/)

Vous avez peut-être remarqué que j'ai spécifié une variable, `--angle`, que je n'ai pas encore définie. Comme nous allons animer le `--angle`, nous devons le définir explicitement en utilisant la règle `@property`, comme nous l'avons fait pour la propriété `--progress`. La seule différence est que nous devrons spécifier une valeur de syntaxe différente. Au lieu de `<percentage>`, la valeur devra être `<angle>` :

```css
@property --angle {
	syntax: '<angle>';
	inherits: false;
	initial-value: -90deg;
}
```

En définissant la valeur initiale à `-90deg`, nous nous assurons que le curseur est placé à la position 12 heures sur l'indicateur de progression.

Votre indicateur devrait maintenant ressembler à ceci :

![Le curseur est positionné au centre supérieur de l'indicateur de progression](https://www.freecodecamp.org/news/content/images/2024/01/positioned-thumb.png)
_Montrant le curseur maintenant sur la piste de l'indicateur de progression_

L'étape suivante consiste à créer l'animation pour le curseur, puis à lier la timeline de l'animation à la position de défilement de la page.

### Animation du curseur de l'indicateur

Commençons par créer une nouvelle animation :

```css
@keyframes rotate {
	0% {
		--angle: -90deg;
	}

	100% {
		--angle: 270deg;
	}
}
```

Au cours de toute l'animation, le curseur effectuera une rotation de 360 degrés, effectuant une révolution complète sur l'élément de progression.

Enfin, nous devons ajouter les deux propriétés suivantes au curseur :

```css
.progress::after {
	# autres propriétés CSS

	animation: rotate linear 1ms;
	animation-timeline: scroll(nearest block);
}
```

En faisant cela, nous appliquons l'animation de rotation à notre curseur et la lions à la position de défilement.

Tout devrait maintenant fonctionner sans accroc :

![L'interface utilisateur de l'indicateur de progression complétée](https://www.freecodecamp.org/news/content/images/2024/01/thumb-complete.gif)
_Produit final montrant l'animation fonctionnant en douceur lors du défilement de l'utilisateur_

## Conclusion

J'ai créé cet indicateur de progression spécifiquement pour me familiariser avec les outils incroyables que CSS a livrés au cours des dernières années. J'espère que vous avez appris autant de cette leçon que j'en ai appris en la créant.

Il y avait d'autres fonctionnalités CSS que je voulais explorer, comme `popover` et `:has`, mais je n'ai pas trouvé le moyen de les intégrer dans cette animation. Si vous trouvez cet article intéressant, je pourrais essayer de créer d'autres petits changements sur la plateforme Component Odyssey, en utilisant des fonctionnalités CSS de pointe.

Soyez prudent, car beaucoup des fonctionnalités CSS que j'ai couvertes sont encore très nouvelles. Vous devriez donc vérifier la compatibilité des navigateurs avant de les utiliser en production.

Si elles ne sont pas supportées dans un ou plusieurs navigateurs, mais que vous êtes désespéré de les utiliser, alors utilisez une stratégie d'**amélioration progressive** (comme je l'ai expliqué dans ce tutoriel) pour vous assurer que ceux avec des navigateurs compatibles obtiennent l'expérience complète, tout en offrant aux utilisateurs de navigateurs non supportés une expérience de base solide.

Si vous avez aimé cet article et que vous aimeriez en savoir plus sur Component Odyssey ou d'autres astuces de développement web, envisagez de [vous abonner à la newsletter](https://component-odyssey.com/subscribe).

### Ressources

* [Devenir pratique avec les timelines de progression de défilement](https://developer.chrome.com/docs/css-ui/scroll-driven-animations#getting_practical_with_scroll_progress_timelines)
* [Nous pouvons enfin animer les dégradés CSS](https://dev.to/afif/we-can-finally-animate-css-gradient-kdk)
* [Chargeurs inspirés du fitness](https://codepen.io/LukyVj/pen/rNqvowZ)
* [MDN : règle @property](https://drafts.css-houdini.org/css-properties-values-api-1/#at-property-rule)
* [MDN : Animation Timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timeline)