---
title: Twitter Emoji – Comment utiliser Twemoji sur votre site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-25T21:08:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-twitter-emoji-on-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Frame-451-4.png
tags:
- name: CSS
  slug: css
- name: emoji
  slug: emoji
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Twitter Emoji – Comment utiliser Twemoji sur votre site web
seo_desc: 'By Shayan

  In this article, I''ll explain what Twitter Emoji – or Twemoji – are and why you
  might want to use them.

  Why should you use Twitter Emojis?

  A couple of months ago, I started working on a project of mine, and I needed to
  allow users to select...'
---

Par Shayan

Dans cet article, je vais expliquer ce que sont les Twitter Emoji – ou Twemoji – et pourquoi vous pourriez vouloir les utiliser.

## Pourquoi utiliser les emojis Twitter ?

Il y a quelques mois, j'ai commencé à travailler sur un projet et j'avais besoin de permettre aux utilisateurs de sélectionner différentes icônes pour leurs entrées.

Après y avoir réfléchi, j'ai décidé d'utiliser des emojis au lieu d'icônes, car tout le monde les connaît déjà et ils sont disponibles presque partout.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Frame-448.png)
_Exemple d'application web avec des emojis natifs_

Assez facile, n'est-ce pas ? Eh bien, pas vraiment. Comme tout le reste, les emojis viennent avec leurs propres problèmes que vous ne connaissez peut-être pas jusqu'à ce que vous passiez du temps à travailler avec eux.

L'un des problèmes les plus courants avec les emojis est qu'ils sont très incohérents en termes de design et de support sur différents systèmes d'exploitation et même différents navigateurs.

Par exemple, si vous sélectionnez un emoji spécifique sur votre téléphone, il peut apparaître très différemment sur votre ordinateur portable, ou il peut finir par s'afficher comme un carré ou une boîte si votre système d'exploitation n'a pas la dernière prise en charge Unicode.

Si vous avez beaucoup d'emojis partout dans votre projet, cela pourrait devenir un problème significatif d'expérience utilisateur et commencer à ennuyer vos utilisateurs. Il était donc temps pour moi de trouver un moyen de le résoudre avant que cela ne commence à éloigner les utilisateurs du projet.

Après avoir fait quelques recherches, je suis tombé sur le jeu d'emojis de Twitter ! Twemoji est une bibliothèque open-source qui fournit un support standard pour les emojis sur toutes les plateformes. Elle facilite grandement la prise en charge de tous les derniers emojis sur différents systèmes d'exploitation et navigateurs et les fait tous apparaître de la même manière.

C'est tout ce dont j'avais besoin, alors je n'ai pas hésité une minute à l'intégrer dans mon projet, et cela a résolu tous mes problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Frame-447.png)
_Exemple d'application web avec des emojis Twitter_

D'accord, c'est à peu près tout pour l'histoire. Maintenant, mettons les mains dans le cambouis avec un peu de code et voyons comment fonctionne Twemoji.

## Comment fonctionne Twemoji ?

En bref, Twemoji dispose d'une alternative SVG et PNG pour chaque emoji Unicode. Il nous permet de les importer soit depuis leur CDN, soit localement, et de les rendre sous forme d'image au lieu de texte Unicode.

Cela signifie qu'ils sont supportés partout, et nous avons toujours accès aux derniers emojis.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Frame-449.png)
_Exemples de Twemoji_

## Comment commencer avec Twemoji

Pour commencer, nous devons importer Twemoji dans notre document HTML. Pour ce faire, copions et collons ce qui suit dans la balise `<head>` de notre document.

```html
<script src="https://twemoji.maxcdn.com/v/latest/twemoji.min.js" crossorigin="anonymous"></script>
```

Ensuite, nous devons utiliser la bibliothèque que nous venons d'importer et la faire analyser notre Unicode pour en faire des Twemojis.

Il existe deux façons de procéder pour analyser vos emojis, et je vais couvrir les deux pour que vous puissiez décider laquelle convient le mieux à vos besoins.

### Analyser tout le contenu du corps

La première et plus facile option est de faire analyser tout notre DOM par Twemoji et de convertir automatiquement chaque emoji Unicode et de le remplacer par un Twemoji.

Pour implémenter cela, tout ce que nous avons à faire est d'utiliser le package que nous venons d'importer et de lui passer le corps de notre document comme ceci :

```javascript
twemoji.parse(document.body);
```

Une fois que nous appelons `twemoji.parse` et que nous lui passons le corps du document comme argument, il analysera tout ce qui se trouve à l'intérieur du corps. Et il remplacera les emojis Unicode texte par des images Twemoji sans compromettre les notes environnantes.

À ce stade, votre document HTML devrait ressembler à ce qui suit. Une fois que vous l'ouvrez dans le navigateur, vous devriez voir le Twemoji.

```html
<html>
    <head>
        <script src="https://twemoji.maxcdn.com/v/latest/twemoji.min.js" crossorigin="anonymous"></script>
    </head>
    <body>
	    📮
    </body>
    <script>
	    twemoji.parse(document.body)
    </script>
</html>
```

Gardez à l'esprit que cette méthode entraîne des pénalités de performance, car nous exécutons cette opération sur tous les éléments à l'intérieur de notre corps, ce qui peut être assez coûteux.

### Analyser manuellement chaque emoji

Pour mon projet, j'ai fini par opter pour l'analyse manuelle. Cela m'a donné plus de contrôle sur la manière dont les choses étaient traitées et a réduit la pénalité de performance par rapport à l'analyse de l'ensemble du document.

Mais cette méthode est plus complexe, et je ne la recommanderais pas sauf si vous avez une bonne raison de décider d'analyser manuellement vos emojis au lieu d'analyser l'ensemble du document.

Pour comprendre la différence ici, il est important de savoir comment fonctionne la méthode d'analyse :

Si le premier argument de `twemoji.parse` est un HTMLElement, la méthode analysera automatiquement l'élément et remplacera les emojis à l'intérieur du document. Mais si le premier élément est une chaîne, la méthode analysera cet emoji unique et nous permettra de recevoir les données dans une fonction de rappel que nous pouvons définir.

Revenons à notre document HTML, passons notre emoji sous forme de chaîne, fournissons une méthode de rappel et imprimons les arguments dans la console.

```javascript
const emoji = "📮"
twemoji.parse(emoji, {
	callback: (icon, options) => {
		console.log(icon, options)
	}
})

// Sortie de la console
// 1f4ee {base: 'https://twemoji.maxcdn.com/v/14.0.2/', ext: '.png', size: '72x72', callback: ƒ, attributes: ƒ, …}
```

Comme vous pouvez le voir, les options de rappel nous donnent toutes les informations dont nous avons besoin pour construire l'URL source et l'ajouter à notre document sous forme d'image.

Ensuite, définissons une méthode qui prend les options et construit notre URL source.

```javascript
function constructTwemojiURL(icon, options) {
	return ''.concat(
		options.base, 
		options.size, 
		'/',
		icon,         
		options.ext   
	);
}
```

Nous pouvons maintenant appeler cette méthode depuis le rappel pour obtenir l'URL source, puis créer une nouvelle balise image et l'ajouter à notre document.

```javascript
const emoji = "📮"
twemoji.parse(emoji, {
	callback: (icon, options) => {
        
		// créer la balise image
		const img = document.createElement('img');

		// assigner la source de l'image
		img.src = constructTwemojiURL(icon, options)        
		img.alt = "Twemoji"

		// ajouter la balise à notre corps de document
		document.body.append(img)

	}
})
```

Enfin, si nous ouvrons le document HTML dans notre navigateur, nous devrions voir notre Twemoji. Votre document HTML devrait ressembler à ce qui suit à ce stade :

```javascript
<html>
	<head>
		<script src="https://twemoji.maxcdn.com/v/latest/twemoji.min.js" crossorigin="anonymous"></script>
	</head>
	<body></body>
	<script>
		function constructTwemojiURL(icon, options) {
			return ''.concat(
				options.base, 
				options.size, 
				'/',
				icon,         
				options.ext   
			);
		}
		
		const emoji = "📮"
		twemoji.parse(emoji, {
			callback: (icon, options) => {
		        
				// créer la balise image
				const img = document.createElement('img');
		
				// assigner la source de l'image
				img.src = constructTwemojiURL(icon, options)        
				img.alt = "Twemoji"
		
				// ajouter la balise à notre corps de document
				document.body.append(img)
		
			}
		})
		
		 
	</script>
</html>
```

## Conclusion

C'est à peu près tout ! Dans cet article, nous avons parlé de pourquoi vous pourriez décider d'utiliser les Twemojis dans votre application web, et nous avons couvert deux façons différentes de mettre en œuvre cela en fonction de votre cas d'utilisation.

Si vous êtes intéressé par le projet que je construis, il s'appelle LogSnag.

[LogSnag](https://logsnag.com) est un outil simple de suivi d'événements qui facilite le suivi de tout ce qui est important dans vos projets en temps réel et reçoit des notifications push personnalisées. Vous pouvez consulter [logsnag.com](https://logsnag.com) pour en savoir plus sur le projet.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Frame-450-2.png)
_Capture d'écran de LogSnag_