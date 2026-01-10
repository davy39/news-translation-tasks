---
title: Comment créer un composant Countdown en utilisant React & MomentJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-16T16:41:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-countdown-component-using-react-momentjs-4717edc4ac3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*uxd3eEv1EyIUdvNi.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un composant Countdown en utilisant React & MomentJS
seo_desc: 'By Florin Pop

  Recently I had to create a Countdown for one of my other projects, and I thought
  that it could also make a good tutorial. So in this post we’re going to create this
  component using React and a little bit of SVG. ?

  You can find the final...'
---

Par Florin Pop

Récemment, j'ai dû créer un Countdown pour l'un de mes autres projets, et j'ai pensé que cela pourrait également faire un bon tutoriel. Donc dans cet article, nous allons créer ce composant en utilisant React et un peu de `SVG`. ?

Vous pouvez trouver le résultat final dans cet [exemple Codepen](https://codepen.io/FlorinPop17/pen/YbpwyG):

%[https://codepen.io/FlorinPop17/pen/YbpwyG]

Tout d'abord, nous allons créer la fonctionnalité de compte à rebours, puis nous verrons comment créer l'arc animé en utilisant `SVG` avec quelques fonctions élégantes. ?

### Création de la fonctionnalité Countdown

Pour cela, nous allons utiliser la bibliothèque [MomentJS](https://momentjs.com/) qui nous aidera à _analyser, valider, manipuler_ et _afficher_ les dates et les heures.

Basiquement, ce dont nous aurons besoin, c'est d'avoir 2 dates:

* la date actuelle ou `now`
* la date finale ou `then`

Lorsque nous avons ces 2 dates, nous pouvons soustraire `now` de `then` en utilisant `moment` et nous obtiendrons le temps restant (ou la valeur `countdown`).

Pour la date `then`, nous devrons passer 2 chaînes de caractères:

* une, la chaîne `timeTillDate` contenant la date finale jusqu'à laquelle nous voulons compter (par exemple : **26 05 2019, 6:00 am**)
* deux, la chaîne `timeFormat` qui est utilisée par `moment` afin de valider le format de l'heure (dans notre exemple, ce serait : **DD MM YYYY, h:mm a**)

Vous pouvez en savoir plus sur l'analyse des chaînes de caractères et leur formatage dans la [documentation](https://momentjs.com/docs/#/parsing/string/).

Voyons à quoi cela ressemble en code:

```javascript
import moment from 'moment';

const then = moment(timeTillDate, timeFormat);
const now = moment();
const countdown = moment(then - now);
```

**Note** : les valeurs `timeTillDate`, `timeFormat` seront fournies à l'intérieur du composant React. Pour l'instant, nous les utilisons comme exemples.

À partir de l'objet `countdown`, nous pouvons obtenir toutes les valeurs que nous voulons afficher dans notre composant - `days`, `hours`, `minutes` et `seconds` restants jusqu'à ce que nous atteignions le temps `then`.

```javascript
import moment from 'moment';

const then = moment(timeTillDate, timeFormat);
const now = moment();
const countdown = moment(then - now);
const days = countdown.format('D');
const hours = countdown.format('HH');
const minutes = countdown.format('mm');
const seconds = countdown.format('ss');
```

Plus tard, nous ajouterons ce code dans un `interval` JS qui serait appelé chaque seconde, mais avant cela, mettons en place le composant React pour cela.

### Le composant Countdown

Pour cela, nous allons créer un composant basé sur une _classe_, car nous avons besoin d'accéder à l'`state` du composant car nous allons sauvegarder ces 4 valeurs (`days`, `hours`, `minutes`, `seconds`) dans celui-ci. Par défaut, ces valeurs sont `undefined`.

```javascript
import React from 'react';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };

    render() {
        const { days, hours, minutes, seconds } = this.state;
      
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    <div className="countdown-item">
                        {days}
                        <span>jours</span>
                    </div>
                    <div className="countdown-item">
                        {hours}
                        <span>heures</span>
                    </div>
                    <div className="countdown-item">
                        {minutes}
                        <span>minutes</span>
                    </div>
                    <div className="countdown-item">
                        {seconds}
                        <span>secondes</span>
                    </div>
                </div>
            </div>
        );
    }
}
```

Ensuite, créons l'`interval` qui s'exécute chaque seconde et sauvegarde les valeurs dans le `state` du composant. Nous allons faire cet `interval` à l'intérieur de la méthode de cycle de vie `componentDidMount`. Nous allons `clear` l'intervalle dans la méthode de cycle de vie `componentWillUnmount`, car nous ne voulons pas le garder en cours d'exécution après que le composant ait été retiré du DOM.

```javascript
import React from 'react';
import moment from 'moment';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };

    componentDidMount() {
        this.interval = setInterval(() => {
            const { timeTillDate, timeFormat } = this.props;
            const then = moment(timeTillDate, timeFormat);
            const now = moment();
            const countdown = moment(then - now);
            const days = countdown.format('D');
            const hours = countdown.format('HH');
            const minutes = countdown.format('mm');
            const seconds = countdown.format('ss');
            this.setState({ days, hours, minutes, seconds });
        }, 1000);
    }

    componentWillUnmount() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }

    render() {
        const { days, hours, minutes, seconds } = this.state;
      
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    <div className="countdown-item">
                        {days}
                        <span>jours</span>
                    </div>
                    <div className="countdown-item">
                        {hours}
                        <span>heures</span>
                    </div>
                    <div className="countdown-item">
                        {minutes}
                        <span>minutes</span>
                    </div>
                    <div className="countdown-item">
                        {seconds}
                        <span>secondes</span>
                    </div>
                </div>
            </div>
        );
    }
}
```

### Le CSS

Nous avons la fonctionnalité de compte à rebours qui fonctionne maintenant, alors stylisons-la un peu:

```javascript
@import url('https://fonts.googleapis.com/css?family=Lato');

* {
    box-sizing: border-box;
}

body {
    font-family: 'Lato', sans-serif;
}

h1 {
    letter-spacing: 2px;
    text-align: center;
    text-transform: uppercase;
}

.countdown-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
}

.countdown-item {
    color: #111;
    font-size: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    line-height: 30px;
    margin: 10px;
    padding-top: 10px;
    position: relative;
    width: 100px;
    height: 100px;
}

.countdown-item span {
    color: #333;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
}
```

Rien de fancy dans le CSS; nous utilisons `flexbox` pour positionner les éléments dans le wrapper.

Enfin, créons l'arc `SVG` qui entourera chaque élément de notre compte à rebours.

### Le composant SVGCircle

Avant de faire cela, il y a quelques fonctions dont nous avons besoin pour créer l'arc `SVG` personnalisable. Je les ai trouvées sur [StackOverflow](https://stackoverflow.com/questions/5736398/how-to-calculate-the-svg-path-for-an-arc-of-a-circle). Pour plus d'informations, vous devriez aller là-bas et lire l'explication détaillée des fonctions.

```javascript
function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    var angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
  
    return {
        x: centerX + radius * Math.cos(angleInRadians),
        y: centerY + radius * Math.sin(angleInRadians)
    };
}

function describeArc(x, y, radius, startAngle, endAngle) {
    var start = polarToCartesian(x, y, radius, endAngle);
    var end = polarToCartesian(x, y, radius, startAngle);
    var largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1';
    var d = [
        'M',
        start.x,
        start.y,
        'A',
        radius,
        radius,
        0,
        largeArcFlag,
        0,
        end.x,
        end.y
    ].join(' ');
  
    return d;
}
```

Basiquement, la fonction ci-dessus calcule comment l'arc doit être dessiné en fournissant un ensemble de valeurs telles que : les points de départ et de fin, le rayon et les angles.

Retour à notre composant React : nous allons créer le `svg` et nous aurons une balise `path` à l'intérieur qui dessinerá l'arc (la prop `d`) en lui donnant une propriété `radius`. Les 4 autres valeurs dans la fonction `describeArc` sont fixes, car nous ne voulons pas les modifier et nous les personnalisons pour qu'elles soient belles pour notre exemple.

```javascript
const SVGCircle = ({ radius }) => (
    <svg className="countdown-svg">
        <path
            fill="none"
            stroke="#333"
            stroke-width="4"
            d={describeArc(50, 50, 48, 0, radius)}
        />
    </svg>
);
```

Et nous avons également besoin d'un peu de CSS pour le positionner à l'intérieur du `.countdown-item` (Voir où ce composant va dans la section du résultat final):

```css
.countdown-svg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100px;
    height: 100px;
}
```

Avant d'ajouter ce composant à l'intérieur du composant `Countdown`, nous devons convertir les valeurs que nous avons (`days`, `hours`, `minutes` et `seconds`) en leurs valeurs de rayon correspondantes.

Pour cela, nous aurons besoin d'une autre fonction simple qui mappera un nombre dans une plage (dans notre cas, les valeurs de date) à une autre plage de nombres (dans notre cas, le rayon). Cette fonction provient également de [StackOverflow](https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers):

```javascript
function mapNumber(number, in_min, in_max, out_min, out_max) {
    return (
        ((number - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min
    );
}
```

### Le résultat final

Enfin, ajoutons le nouveau composant `SVGCircle` à l'intérieur de chacun des `.countdown-item`s et mettons tout ensemble:

```js
import React from 'react';
import moment from 'moment';

class Countdown extends React.Component {
    state = {
        days: undefined,
        hours: undefined,
        minutes: undefined,
        seconds: undefined
    };
    
    componentDidMount() {
        this.interval = setInterval(() => {
            const { timeTillDate, timeFormat } = this.props;
            const then = moment(timeTillDate, timeFormat);
            const now = moment();
            const countdown = moment(then - now);
            const days = countdown.format('D');
            const hours = countdown.format('HH');
            const minutes = countdown.format('mm');
            const seconds = countdown.format('ss');
            this.setState({ days, hours, minutes, seconds });
        }, 1000);
    }
    
    componentWillUnmount() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }
    
    render() {
        const { days, hours, minutes, seconds } = this.state;
        
        // Mapping des valeurs de date aux valeurs de rayon
        const daysRadius = mapNumber(days, 30, 0, 0, 360);
        const hoursRadius = mapNumber(hours, 24, 0, 0, 360);
        const minutesRadius = mapNumber(minutes, 60, 0, 0, 360);
        const secondsRadius = mapNumber(seconds, 60, 0, 0, 360);
        
        if (!seconds) {
            return null;
        }
        
        return (
            <div>
                <h1>Countdown</h1>
                <div className="countdown-wrapper">
                    {days && (
                        <div className="countdown-item">
                            <SVGCircle radius={daysRadius} />
                            {days}
                            <span>jours</span>
                        </div>
                    )}
                    {hours && (
                        <div className="countdown-item">
                            <SVGCircle radius={hoursRadius} />
                            {hours}
                            <span>heures</span>
                        </div>
                    )}
                    {minutes && (
                        <div className="countdown-item">
                            <SVGCircle radius={minutesRadius} />
                            {minutes}
                            <span>minutes</span>
                        </div>
                    )}
                    {seconds && (
                        <div className="countdown-item">
                            <SVGCircle radius={secondsRadius} />
                            {seconds}
                            <span>secondes</span>
                        </div>
                    )}
                </div>
            </div>
        );
    }
}

const SVGCircle = ({ radius }) => (
    <svg className="countdown-svg">
        <path
            fill="none"
            stroke="#333"
            stroke-width="4"
            d={describeArc(50, 50, 48, 0, radius)}
        />
    </svg>
);

// From StackOverflow: https://stackoverflow.com/questions/5736398/how-to-calculate-the-svg-path-for-an-arc-of-a-circle

function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
    var angleInRadians = ((angleInDegrees - 90) * Math.PI) / 180.0;
    
    return {
        x: centerX + radius * Math.cos(angleInRadians),
        y: centerY + radius * Math.sin(angleInRadians)
    };
}

function describeArc(x, y, radius, startAngle, endAngle) {
    var start = polarToCartesian(x, y, radius, endAngle);
    var end = polarToCartesian(x, y, radius, startAngle);
    var largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1';
    var d = [
        'M',
        start.x,
        start.y,
        'A',
        radius,
        radius,
        0,
        largeArcFlag,
        0,
        end.x,
        end.y
    ].join(' ');
    
    return d;
}

// From StackOverflow: https://stackoverflow.com/questions/10756313/javascript-jquery-map-a-range-of-numbers-to-another-range-of-numbers

function mapNumber(number, in_min, in_max, out_min, out_max) {
    return (
        ((number - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min
    );
}
```

Tout ce que vous avez à faire maintenant pour utiliser le composant `Countdown` est de lui passer les deux props (`timeTillDate` et `timeFormat`) et vous êtes prêt ?:

```javascript
<Countdown 
    timeTillDate="26 05 2019, 6:00 am" 
    timeFormat="DD MM YYYY, h:mm a" 
/>
```

### Conclusion

C'était un petit projet amusant avec React, n'est-ce pas ? ?

Quand j'ai construit cela, j'ai appris un peu plus sur la façon de travailler avec la bibliothèque `momentjs` et aussi avec les `svg` pour dessiner un arc.

Faites-moi savoir si vous avez des questions concernant ce tutoriel.

Bon codage ! ?

_Publié à l'origine sur [www.florin-pop.com](https://www.florin-pop.com/blog/2019/05/countdown-built-with-react/)_