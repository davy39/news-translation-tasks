---
title: "React.js vs React Native \x13 Quelles sont les diff\trences ?"
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-02-01T00:41:21.000Z'
originalURL: https://freecodecamp.org/news/react-js-vs-react-native-whats-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-pixabay-209339.jpg
tags:
- name: React Native
  slug: react-native
- name: React
  slug: reactjs
seo_title: "React.js vs React Native \x13 Quelles sont les diff\trences ?"
seo_desc: 'Are React.js and React Native the same?

  If you''re new to the world of web and mobile development, you might be wondering
  the same thing.

  As a newbie, it''s easy to assume that React.js are React Native are the same. After
  all, they both have "React" a...'
---

React.js et React Native sont-ils identiques ?

Si vous 	tes nouveau dans le monde du d	veloppement web et mobile, vous vous posez peut-	tre la m	me question.

En tant que d	butant, il est facile de supposer que React.js et React Native sont identiques. Aprs tout, ils ont tous les deux "React" dans leur nom.

Bien que React.js et React Native aient beaucoup en commun, ils sont diff	rents l'un de l'autre. Dans cet article, j'expliquerai React.js et React Native, puis je listerai leurs similitudes et leurs diff	rences.  la fin de cet article, vous aurez une connaissance claire des deux outils et du type d'application qu'ils permettent de construire.

Pour bien comprendre la diff	rence entre React.js et React Native, nous devons d'abord plonger dans la faon dont un site web est rendu dans un navigateur.

## Comment les sites web sont rendus : HTML, CSS et JavaScript

Lorsque vous tapez l'URL d'un site web dans la barre d'adresse de votre navigateur et que vous cliquez sur Entr	e, le navigateur demande le site web, et le serveur web envoie un fichier HTML au navigateur.

Le fichier HTML contient le contenu de la page web et les fichiers li	s tels que les images, les vid	os et les feuilles de style. Le navigateur web analyse le fichier HTML et construit un Document Object Model (DOM), qui est une structure en forme d'arbre contenant les 	l	ments de la page (par exemple, des boutons, des paragraphes, des liens, etc.).

Le navigateur initie des demandes pour les fichiers li	s et les t	l	charge sur l'ordinateur. Il analyse ensuite les fichiers li	s, tels que CSS et JavaScript, et applique le style au contenu, le rendant plus pr	sentable pour l'utilisateur. Aprs que tous les fichiers soient t	l	charg	s, le navigateur rend le contenu  l'	cran.

Le navigateur ex	cute 	galement tout code JavaScript pour rendre la page interactive. Par exemple, si l'utilisateur remplit les mauvaises informations dans un formulaire, JavaScript peut 	tre utilis	 pour ins	rer un 	l	ment `<div>` dans la page montrant un message d'erreur  l'utilisateur.

Cependant, l'un des plus grands problmes de l'insertion d'	l	ments dans le DOM avec JavaScript est que le code n'est pas r	utilisable. Par exemple, si vous voulez ins	rer le m	me bouton dans la page, mais avec des couleurs de fond diff	rentes, vous devez cr	er l'	l	ment deux fois en JavaScript :

```c
let blueBtn = document.createElement("button").style.backgroundColor("blue")
let redBtn = document.createElement("button").style.backgroundColor("red")

// Ins	rer les boutons bleu et rouge dans la page
```

Ce n'est qu'un simple exemple. Avec des interfaces utilisateur complexes, vous pouvez imaginer  quel point les choses peuvent devenir longues et confuses. React a 	t	 d	velopp	 pour r	soudre ce problme en rendant le processus de cr	ation d'applications web beaucoup plus organis	 et intuitif.

## Qu'est-ce que React.js ?

Techniquement parlant, ReactJS est une bibliothque JavaScript open-source, front-end pour la construction d'interfaces utilisateur ou de composants UI. En termes simples, cela signifie que vous pouvez utiliser React pour construire toutes les parties d'un site web que l'utilisateur peut voir et avec lesquelles il peut interagir sur sa fen	tre de navigateur.

Alors, quelle est la diff	rence entre l'utilisation de JavaScript simple et React ? Eh bien, React rend le processus de conception de l'interface utilisateur beaucoup plus facile. Il vous permet de cr	er des 	l	ments que vous pouvez facilement r	utiliser dans d'autres parties du site web ou de l'application.

Avec JavaScript, j'ai pr	c	demment mentionn	 comment vous devrez 	crire le m	me code deux fois pour cr	er le m	me bouton avec des couleurs diff	rentes, ce qui pourrait conduire  une complexit	 dans les grands projets.

L'architecture de composants de React r	sout ce problme de manire brillante. Avec React, vous d	finissez une seule partie de l'UI, par exemple un bouton, comme un composant.

```c
const Button (props) => {
	return (
    	<div>
        	<button style={props.color}>Submit</button>
        </div>
    )
}
```

Le composant dans ce cas est une fonction qui retourne une syntaxe similaire  HTML appel	e JSX, qui d	finit la pr	sentation et l'apparence du composant sur le navigateur web.

Maintenant, supposons que vous voulez utiliser le m	me bouton (mais avec des couleurs diff	rentes)  plusieurs endroits sur votre site web. Au lieu de cr	er chaque bouton  partir de z	ro avec diff	rentes propri	t	s de couleur (comme vous le feriez avec JavaScript), avec React, vous utilisez simplement le m	me 	l	ment `<Button>` et vous passez une couleur diff	rente  chacun d'eux en tant que `props`, cr	ant des variations du m	me bouton.

```c
<Button color="red" />
<Button color="blue" />
<Button color="green" />
```

Cette m	thode garde tout simple et organis	, ce qui est toute l'essence de la bibliothque React.js.

Un autre avantage de l'utilisation de React pour le d	veloppement d'UI est la s	paration des pr	occupations. Cela signifie que les donn	es utilis	es dans un composant existent s	par	ment de la logique, qui existe s	par	ment de la couche de pr	sentation.

Voici un exemple :

```c
const Button (props) => {
	// donn	es du composant
    const [btnText, setBtnText] = useState("Submit")
    
    // logique du composant
    function onClick() {
    	setBtnText("Submitted!")
    }
    
	return (
    	// vue du composant
    	<div>
        	<button style={props.color}>{btnText}</button>
        </div>
    )
}
```

Comme vous pouvez le voir ici, l'	tat, la logique et la pr	sentation d'un composant sont tous s	par	s les uns des autres, rendant les composants UI React plus faciles  comprendre et  composer.

Pour conclure, React est une bibliothque JavaScript conue pour simplifier le processus de construction du frontend des applications web.

## Qu'est-ce que React Native ?

Voici la principale diff	rence entre ReactJS et React Native :

* React JS est utilis	 pour construire l'interface utilisateur des applications web (c'est--dire des applications qui s'ex	cutent sur un navigateur web)
    
* React Native est utilis	 pour construire des applications qui s'ex	cutent sur les appareils iOS et Android (c'est--dire des applications mobiles multiplateformes)
    
* React utilise HTML, CSS et JavaScript pour cr	er des interfaces utilisateur interactives. React Native, en revanche, utilise des composants UI natifs et des API pour cr	er des applications mobiles.
    

React JS et React Native partagent la m	me syntaxe. React Native a 	t	 cr		 comme un moyen pour les d	veloppeurs de construire des applications mobiles multiplateformes en utilisant leurs connaissances existantes des outils de d	veloppement web comme HTML, CSS, JavaScript et la bibliothque principale React.

En fait, certaines des bibliothques couramment utilis	es avec React pour d	velopper des applications web ont 	galement une version mobile pour construire des applications dans React Native  par exemple, Axios, Bootstrap CSS et Tailwind CSS.

Voici les points communs entre React DOM et React Native :

1. Ils utilisent tous les deux la m	me bibliothque principale React.
    
2. Ils utilisent tous les deux la m	me architecture bas	e sur les composants, ce qui signifie que les d	veloppeurs peuvent d	composer leurs applications en morceaux plus petits et plus faciles  g	rer.
    
3. Ils utilisent tous les deux JavaScript comme langage de programmation, et JSX comme langage de modlisation.
    
4. React DOM et React Native utilisent tous les deux des DOM virtuels pour rendre leurs applications.
    
5. React DOM et React Native utilisent 	galement les m	mes techniques et composants de style, bien que ceux de React Native soient un peu diff	rents.
    
6. Ils utilisent tous les deux Chrome DevTools pour d	boguer les applications.
    
7. Ils utilisent les m	mes API JavaScript.
    
8. Tous deux ont 	t	 d	velopp	s chez Meta. React a 	t	 d	velopp	 par un ing	nieur logiciel nomm	 Jordan Walke tandis que React Native est n	 d'un hackathon.
    
## Conclusion

Cet article a explor	 les diff	rences entre React DOM et React Native, deux outils JavaScript populaires. React DOM est principalement utilis	 pour le d	veloppement web, tandis que React Native est utilis	 pour le d	veloppement mobile.

React DOM utilise HTML, CSS et JavaScript pour la mise en page et le style, et permet aux d	veloppeurs de cr	er des interfaces utilisateur interactives. React Native, en revanche, utilise des composants UI natifs et des API pour cr	er des applications mobiles multiplateformes.

Merci d'avoir lu. Obtenez ma checklist gratuite de r	daction freelance [ici](https://kingchuks.gumroad.com/l/fwc).