---
title: Comment créer un composant Timeline avec React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-26T15:03:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-timeline-component-with-react-1b216f23d3d4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*WP3O7p7DkELIQIfs.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer un composant Timeline avec React
seo_desc: 'By Florin Pop

  These days I’ve been working on a new page for my website. I wanted to have a Timeline
  to showcase some of my professional accomplishments over the years.

  I did it for a couple of reasons:


  My future self will look back one day and say:...'
---

Par Florin Pop

Ces jours-ci, j'ai travaillé sur une nouvelle page pour mon site web. Je voulais avoir une [Timeline](https://www.florin-pop.com/timeline) pour présenter certaines de mes réalisations professionnelles au fil des années.

Je l'ai fait pour plusieurs raisons :

1. Mon moi futur regardera un jour en arrière et dira : « Wow… Je me souviens du jour où j'ai fait ça ! Comme j'étais heureux d'avoir atteint cet objectif ! » Notre succès est un voyage, pas une destination, et je veux écrire chaque objectif que j'atteins en cours de route
2. Cela pourrait attirer plus de clients (on verra comment cela se passe ?)
3. À mon avis, c'est un type de portfolio différent. Un portfolio unique, peut-être ? ?

Quoi qu'il en soit… Construisons quelque chose maintenant !

Sur l'image ci-dessus, vous pouvez voir ce que nous allons construire aujourd'hui avec React ! Avant de commencer, décomposons les étapes que nous devons suivre :

1. Créer les `data` dont nous aurons besoin
2. Créer le composant `TimelineItem` - chaque entrée individuelle de la timeline
3. Créer un conteneur `Timeline` - il prendra les `data` et les passera aux `TimelineItem`s
4. Styler le tout

### Créer les données

Avant de passer à la création des composants React, nous devons savoir exactement à quoi ressembleront les données afin de planifier la structure du DOM.

Pour cette application Timeline, nous aurons besoin d'un _tableau_ d'objets. Nous appellerons ce tableau : `timelineData`.

Voyons à quoi cela pourrait ressembler :

```js
[
    {
        text: 'J\'ai écrit mon premier article de blog sur Medium',
        date: '3 mars 2017',
        category: {
            tag: 'medium',
            color: '#018f69'
        },
        link: {
            url:
                'https://medium.com/@popflorin1705/javascript-coding-challenge-1-6d9c712963d2',
            text: 'Lire plus'
        }
    },
    {
        // Un autre objet avec des données
    }
];
```

Les propriétés sont assez simples, n'est-ce pas ? J'ai utilisé des données similaires à celles que j'ai sur ma page de timeline, donc nous pouvons dire que cela est prêt pour la production ! ?

Ensuite, nous construirons le composant `TimelineItem`. Celui-ci utilisera les données de l'objet ci-dessus :

### Le composant TimelineItem

```js
const TimelineItem = ({ data }) => (
    <div className="timeline-item">
        <div className="timeline-item-content">
            <span className="tag" style={{ background: data.category.color }}>
                {data.category.tag}
            </span>
            <time>{data.date}</time>
            <p>{data.text}</p>
            {data.link && (
                <a
                    href={data.link.url}
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    {data.link.text}
                </a>
            )}
            <span className="circle" />
        </div>
    </div>
);
```

Nous avons les balises suivantes :

1. La div `.timeline-item` - utilisée comme enveloppe. Cette div aura la moitié de la largeur de son parent (`50%`) et chaque autre div `.timeline-item` sera placée du côté **droit** en utilisant le sélecteur `:nth-child(odd)`
2. La div `.timeline-item-content` - une autre enveloppe (plus d'informations sur pourquoi nous en avons besoin dans la section de style)
3. La span `.tag` - cette balise aura une couleur de fond personnalisée en fonction de la catégorie
4. Le `time`/`date` et le `text`
5. `link` - nous devons vérifier cela pour voir si un `link` est fourni car nous ne voulons pas toujours en avoir un
6. La span `.circle` - cette balise sera utilisée pour placer un cercle sur la ligne/barre du milieu

**Note** : Tout sera beaucoup plus clair lorsque nous arriverons à la partie **CSS**/style, mais avant cela, créons le composant `Timeline` :

### Le conteneur Timeline

Ce composant va essentiellement `map` sur le tableau et pour chaque objet, il créera un composant `TimelineItem`. Nous ajoutons également une petite vérification pour nous assurer qu'il y a au moins un élément dans le tableau :

```js
import timelineData from '_path_to_file_';

const Timeline = () =>
    timelineData.length > 0 && (
        <div className="timeline-container">
            {timelineData.map((data, idx) => (
                <TimelineItem data={data} key={idx} />
            ))}
        </div>
    );
```

Comme mentionné ci-dessus, `timelineData` est le tableau d'objets contenant toutes les informations requises. Dans mon cas, j'ai stocké ce tableau dans un fichier et je l'ai importé ici, mais vous pouvez le prendre de votre propre base de données ou d'un point de terminaison d'API, c'est à vous de voir.

### Le CSS

**Note** : la plupart des enveloppes seront des conteneurs `flexbox` car nous pouvons jouer plus facilement avec leur positionnement.

Commençons par le CSS de `.timeline-container` :

```css
.timeline-container {
    display: flex;
    flex-direction: column;
    position: relative;
    margin: 40px 0;
}

.timeline-container::after {
    background-color: #e17b77;
    content: '';
    position: absolute;
    left: calc(50% - 2px);
    width: 4px;
    height: 100%;
}
```

Nous utilisons le sélecteur `::after` pour créer cette ligne/barre rouge au milieu du `.timeline-container`. En utilisant la fonction `[calc()](https://developer.mozilla.org/en-US/docs/Web/CSS/calc)`, nous pouvons positionner la ligne exactement au milieu en soustrayant la moitié de sa taille (`2px`) de `50%`. Nous devons faire cela car par défaut, la propriété `left` la positionne selon le bord gauche d'un élément et non le milieu.

Maintenant, passons à l'enveloppe `.timeline-item`.

Ci-dessous, vous pouvez voir un exemple de la façon dont celles-ci sont positionnées dans leur parent (le `.timeline-container`). À des fins de démonstration, j'ai ajouté une bordure pour mettre en évidence ces enveloppes :

![Image](https://cdn-media-1.freecodecamp.org/images/5magmHaf8PAjsks68sGQsWm0CoYXoNqUZ1v6)

Comme vous pouvez le voir, chaque autre enveloppe va à **droite**, et l'enveloppe intérieure (le `.timeline-item-content`) prend moins de place — espace donné par la balise `p` qui est à l'intérieur (principalement).

Voyons le CSS pour cela :

```css
.timeline-item {
    display: flex;
    justify-content: flex-end;
    padding-right: 30px;
    position: relative;
    margin: 10px 0;
    width: 50%;
}

.timeline-item:nth-child(odd) {
    align-self: flex-end;
    justify-content: flex-start;
    padding-left: 30px;
    padding-right: 0;
}
```

La **clé** ici est que nous utilisons le sélecteur `:nth-child(odd)` et nous définissons la propriété `align-self` à `flex-end`, ce qui signifie : « Allez à droite autant que vous pouvez ! »

Parce que ces enveloppes ont une largeur de `50%`, vous pouvez voir que deux d'entre elles occupent toute la largeur. À partir de maintenant, chaque fois que nous voulons styler quelque chose différemment du côté **droit**, nous devrons utiliser cette approche.

Ensuite, l'enveloppe `.timeline-item-content` :

```css
.timeline-item-content {
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    border-radius: 5px;
    background-color: #fff;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    padding: 15px;
    position: relative;
    width: 400px;
    max-width: 70%;
    text-align: right;
}

.timeline-item-content::after {
    content: ' ';
    background-color: #fff;
    box-shadow: 1px -1px 1px rgba(0, 0, 0, 0.2);
    position: absolute;
    right: -7.5px;
    top: calc(50% - 7.5px);
    transform: rotate(45deg);
    width: 15px;
    height: 15px;
}

.timeline-item:nth-child(odd) .timeline-item-content {
    text-align: left;
    align-items: flex-start;
}

.timeline-item:nth-child(odd) .timeline-item-content::after {
    right: auto;
    left: -7.5px;
    box-shadow: -1px 1px 1px rgba(0, 0, 0, 0.2);
}
```

Nous avons plusieurs choses en cours :

1. Cette enveloppe a une largeur `fixed` et aussi une `max-width`. Cela est dû au fait que nous voulons qu'elle ait certaines limites, ce qui signifie que si il n'y a que quelques mots, nous voulons que la boîte fasse au moins `400px` de large, mais si il y a beaucoup de texte, elle ne devrait pas prendre tout l'espace (le `50%` de l'enveloppe `.timeline-item`) mais le texte devrait passer à la ligne suivante -> c'est la raison pour laquelle nous avons utilisé cette deuxième enveloppe : `.timeline-item-content`
2. Les propriétés `text-align` et `align-items` sont utilisées pour pousser les éléments intérieurs à gauche ou à droite, selon le parent
3. La petite **flèche** qui pointe vers la ligne du milieu est donnée par les styles appliqués sur le sélecteur `::after`. Basiquement, c'est une boîte avec une `box-shadow` appliquée qui est tournée à `45deg`
4. Comme mentionné ci-dessus, nous stylons le côté **droit** en sélectionnant le parent avec le sélecteur `:nth-child(odd)`

Ensuite, tous les éléments intérieurs :

```css
.timeline-item-content .tag {
    color: #fff;
    font-size: 12px;
    font-weight: bold;
    top: 5px;
    left: 5px;
    letter-spacing: 1px;
    padding: 5px;
    position: absolute;
    text-transform: uppercase;
}

.timeline-item:nth-child(odd) .timeline-item-content .tag {
    left: auto;
    right: 5px;
}

.timeline-item-content time {
    color: #777;
    font-size: 12px;
    font-weight: bold;
}

.timeline-item-content p {
    font-size: 16px;
    line-height: 24px;
    margin: 15px 0;
    max-width: 250px;
}

.timeline-item-content a {
    font-size: 14px;
    font-weight: bold;
}

.timeline-item-content a::after {
    content: ' ►';
    font-size: 12px;
}

.timeline-item-content .circle {
    background-color: #fff;
    border: 3px solid #e17b77;
    border-radius: 50%;
    position: absolute;
    top: calc(50% - 10px);
    right: -40px;
    width: 20px;
    height: 20px;
    z-index: 100;
}

.timeline-item:nth-child(odd) .timeline-item-content .circle {
    right: auto;
    left: -40px;
}
```

Quelques points à noter ici :

1. Comme vous l'avez peut-être deviné, le `.tag` est positionné `absolute` car nous voulons le garder dans le coin supérieur gauche (ou droit) peu importe la taille de la boîte
2. Nous voulons ajouter un petit caret _après_ la balise `a` pour mettre en évidence qu'il s'agit d'un lien
3. Nous créons un `.circle` et le positionnons sur la ligne/barre du milieu directement _devant_ la flèche

Nous avons presque terminé ! ? La seule chose qui reste à faire est d'ajouter le CSS pour rendre tout cela réactif sur toutes les tailles d'écran :

```css
@media only screen and (max-width: 1023px) {
    .timeline-item-content {
        max-width: 100%;
    }
}

@media only screen and (max-width: 767px) {
    .timeline-item-content,
    .timeline-item:nth-child(odd) .timeline-item-content {
        padding: 15px 10px;
        text-align: center;
        align-items: center;
    }
    
    .timeline-item-content .tag {
        width: calc(100% - 10px);
        text-align: center;
    }
    
    .timeline-item-content time {
        margin-top: 20px;
    }
    
    .timeline-item-content a {
        text-decoration: underline;
    }
    
    .timeline-item-content a::after {
        display: none;
    }
}
```

Nous avons deux requêtes média :

Sur les petits écrans d'ordinateurs portables — `max-width: 1023px` — nous voulons permettre au `.timeline-item-content` de s'étendre sur toute la largeur de son parent car l'écran est plus petit et sinon cela aurait l'air comprimé

1. Sur les téléphones — `max-width: 767px`

* définir le `.tag` pour qu'il soit en pleine `width` (et pour cela, nous n'oublions pas de soustraire `10px` du total de `100%` - cela est dû au fait que nous l'avons positionné à `left: 5px`, donc nous retirons le double de ce montant)
* centrer tout le texte et le pousser un peu vers le bas depuis le haut
* retirer le caret sur le lien et ajouter un soulignement — cela semble mieux sur mobile ?

Aaaand… Nous avons terminé !

![Image](https://cdn-media-1.freecodecamp.org/images/9kXUZLC3dRFtDKKoyhjxDsH1bRYdRpd2n0lG)

### Conclusion

Comme je l'ai mentionné, ce composant est sur ma page [Timeline](https://www.florin-pop.com/timeline). Allez-y pour le voir en action ! ?

Si quelque chose n'était pas clair dans cet article, assurez-vous de me contacter et je serai heureux de répondre à vos questions !

Bon codage ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/04/how-to-create-a-timeline-with-react/)._