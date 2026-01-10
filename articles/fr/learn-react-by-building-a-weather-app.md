---
title: Comment créer une application météo avec React et les Hooks React
date: '2021-03-15T21:16:45.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/nishant-kumar/
originalURL: https://freecodecamp.org/news/learn-react-by-building-a-weather-app
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--39-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_desc: "By Nishant Kumar\nReact is a super-awesome front-end library that you can\
  \ use to build user interfaces.\nOne of the best things about React is that the\
  \ components we create are encapsulated. In other words, they can't be seen. \n\
  Let's learn more about h..."
---


React est une bibliothèque front-end incroyable que vous pouvez utiliser pour construire des interfaces utilisateur.

<!-- more -->

L'un des plus grands atouts de React est que les composants que nous créons sont encapsulés. En d'autres termes, leur logique interne est isolée.

Apprenons-en davantage sur le fonctionnement de tout cela en construisant une application météo avec React.

## Comment installer Node et npm

Pour construire notre application React, nous avons besoin d'un environnement d'exécution appelé Node. Il est principalement utilisé pour exécuter du code JavaScript.

Pour le télécharger, rendez-vous sur [https://nodejs.org/en/][1].

Vous aurez également besoin de **npm**, qui est un gestionnaire de paquets intégré à Node. Vous pouvez l'utiliser pour installer des paquets pour vos applications JavaScript. Heureusement, il est fourni avec Node, vous n'avez donc pas besoin de le télécharger séparément.

Une fois l'installation terminée, ouvrez votre terminal ou votre invite de commande et tapez `node -v`. Cela permet de vérifier la version de Node installée.

## Comment créer une application React

Pour créer notre application React, tapez **`npx create-react-app <nom-de-votre-app>`** dans votre terminal, ou **`npx create-react-app my-weather-app`** dans ce cas précis.

Vous verrez les paquets s'installer.

Une fois l'installation terminée, allez dans le dossier du projet et tapez **`npm start`**.

Vous verrez le modèle React par défaut, comme ceci :

![Screenshot-2021-03-12-12-07-22](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-12-07-22.png)

Le modèle de Boilerplate React par défaut

![Screenshot-2021-03-12-12-08-28](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-12-08-28.png)

App.js

Nous n'avons pas besoin de tout cela pour le moment. Nettoyons donc un peu le code.

Dans votre fichier **app.js**, effacez tout ce qui se trouve à l'intérieur de la balise `div`. Supprimez l'importation du logo.

Une fois cela fait, vous obtiendrez un écran vide en sortie.

![Screenshot-2021-03-12-12-12-25](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-12-12-25.png)

App.js après nettoyage

## Comment installer les paquets nécessaires

Pour rendre cette application plus attrayante, nous avons besoin de paquets externes. Installons-les.

Nous avons besoin de la bibliothèque [Semantic React UI][2]. Pour l'installer, tapez la commande suivante dans le terminal :

```bash
npm install semantic-ui-react semantic-ui-css
```

Une fois installée, ouvrez **index.js** et importez la bibliothèque. Copiez et collez simplement la commande suivante dans votre fichier **index.js** :

```
import 'semantic-ui-css/semantic.min.css'
```

Nous avons également besoin de [moment.js][3] pour formater l'heure. Installez-le avec la commande suivante :

```
npm install moment --save
```

Vous pouvez consulter votre fichier package.json pour suivre tous les paquets installés.

![Screenshot-2021-03-12-12-21-01](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-12-21-01.png)

package.json

Ici, vous pouvez voir tous les paquets que vous avez installés jusqu'à présent.

## Comment créer notre application météo

Pour faire fonctionner notre application météo, nous avons besoin d'OpenWeatherMap, une API tierce qui nous permettra de récupérer les données météorologiques.

Allez sur [https://home.openweathermap.org/users/sign\_up][4] et créez votre propre compte.

Une fois terminé, cliquez sur l'option API dans la barre de navigation. Vous verrez différentes options comme "Current Weather Data", "Hourly 4 hour forecasts", "16 day forecasts", etc. Ce sont les points de terminaison (endpoints) de l'API dont vous aurez besoin pour récupérer les données.

![Screenshot-2021-03-12-12-30-10](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-12-30-10.png)

Vous avez également besoin d'une clé API pour appeler ces API. Pour obtenir votre clé API, cliquez sur votre nom d'utilisateur dans le coin supérieur droit, puis sur "my API keys".

Créez une clé API si elle n'existe pas déjà.

Dans le dossier principal de votre application, créez un fichier nommé **.env**.

Il s'agit d'un fichier de variables d'environnement qui contiendra tous vos points de terminaison et clés API.

```
REACT_APP_API_URL = 'https://api.openweathermap.org/data/2.5'
REACT_APP_API_KEY = Collez votre clé API ici.
REACT_APP_ICON_URL = 'https://openweathermap.org/img/w'
```

Collez votre clé API copiée dans la variable REACT\_APP\_API\_KEY.

## Comment utiliser les Hooks React

Les Hooks React nous permettent d'utiliser et de gérer l'état (state) dans nos composants fonctionnels.

Nous utiliserons le hook `useState` et le hook `useEffect`. Importons-les en haut du fichier.

```
import React, { useEffect, useState } from "react";
```

Créons deux états. L'un pour la latitude et l'autre pour la longitude.

```
const [lat, setLat] = useState([]);
const [long, setLong] = useState([]);
```

Maintenant, créez la fonction `useEffect`. Son but est de charger les fonctions lors du chargement et du rechargement de l'application.

```
useEffect(() => {
    navigator.geolocation.getCurrentPosition(function(position) {
      setLat(position.coords.latitude);
      setLong(position.coords.longitude);
    });

    console.log("Latitude is:", lat)
    console.log("Longitude is:", long)
  }, [lat, long]);
```

Nous obtenons notre latitude et notre longitude en utilisant `navigator.geolocation` et nous utilisons **setLong** et **setLat** pour définir nos états de longitude et de latitude.

```
import './App.css';
import React, { useEffect, useState } from "react";
export default function App() {

  const [lat, setLat] = useState([]);
  const [long, setLong] = useState([]);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(function(position) {
      setLat(position.coords.latitude);
      setLong(position.coords.longitude);
    });

    console.log("Latitude is:", lat)
    console.log("Longitude is:", long)
  }, [lat, long]);

  return (
    <div className="App">

    </div>
  );
}
```

app.js

Voici à quoi ressemble notre fichier app.js maintenant. Vous pouvez vérifier la console pour voir les valeurs de latitude et de longitude.

```
Latitude is: 25.5922166
Longitude is: 85.12761069999999
```

Notre latitude et notre longitude

## Comment obtenir notre position actuelle en utilisant la latitude et la longitude

Créons une autre fonction **getWeather** qui récupérera les données météo de l'API Weather, en fonction de notre latitude et de notre longitude.

Dans cette fonction, nous utilisons un appel fetch pour obtenir les données de l'API. **process.env.REACT\_APP\_API\_URL** récupère l'adresse de votre API et **process.env.REACT\_APP\_API\_KEY** récupère votre clé API depuis le fichier **.env**. Les variables lat et long sont la latitude et la longitude obtenues précédemment.

Ensuite, nous convertissons les données au format **JSON**.

À l'étape suivante, nous utilisons **setData** pour stocker notre résultat dans l'objet **data**.

```
await fetch(`${process.env.REACT_APP_API_URL}/weather/?lat=${lat}&lon=${long}&units=metric&APPID=${process.env.REACT_APP_API_KEY}`)
      .then(res => res.json())
      .then(result => {
        setData(result)
        console.log(result);
      });
```

Et nous affichons les données dans la console.

![Screenshot-2021-03-12-13-36-26](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-13-36-26.png)

Ici, vous pouvez voir toutes les données météo basées sur notre latitude et notre longitude.

Voici notre nouveau fichier app.js qui récupère les données météo :

```
import './App.css';
import React, { useEffect, useState } from "react";
import Weather from './components/weather';
export default function App() {
  
  const [lat, setLat] = useState([]);
  const [long, setLong] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      navigator.geolocation.getCurrentPosition(function(position) {
        setLat(position.coords.latitude);
        setLong(position.coords.longitude);
      });

      await fetch(`${process.env.REACT_APP_API_URL}/weather/?lat=${lat}&lon=${long}&units=metric&APPID=${process.env.REACT_APP_API_KEY}`)
      .then(res => res.json())
      .then(result => {
        setData(result)
        console.log(result);
      });
    }
    fetchData();
  }, [lat,long])
  
  return (
    <div className="App">
      
    </div>
  );
}
```

app.js

### Comment créer les composants météo

Créons nos composants météo où nous afficherons nos données.

Dans votre dossier src, créez un dossier nommé **components**, et dans ce dossier, créez un fichier nommé **weather.js**.

Maintenant, appelons notre composant weather dans notre fichier principal **app.js**.

```
import './App.css';
import React, { useEffect, useState } from "react";
import Weather from './components/weather';
export default function App() {
  
  const [lat, setLat] = useState([]);
  const [long, setLong] = useState([]);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      navigator.geolocation.getCurrentPosition(function(position) {
        setLat(position.coords.latitude);
        setLong(position.coords.longitude);
      });

      await fetch(`${process.env.REACT_APP_API_URL}/weather/?lat=${lat}&lon=${long}&units=metric&APPID=${process.env.REACT_APP_API_KEY}`)
      .then(res => res.json())
      .then(result => {
        setData(result)
        console.log(result);
      });
    }
    fetchData();
  }, [lat,long])
  
  return (
    <div className="App">
      {(typeof data.main != 'undefined') ? (
        <Weather weatherData={data}/>
      ): (
        <div></div>
      )}
      
    </div>
  );
}
```

Importation du composant Weather dans le fichier app.js

Vous pouvez voir que j'ai inclus une vérification dans l'instruction return. Si le type de données que nous recevons est indéfini, cela affichera une div vide. Comme la récupération de données est une fonction asynchrone, il est obligatoire d'inclure cette vérification. Elle charge la fonction après que toutes les autres fonctions ont fini de s'exécuter. Si vous supprimez cette vérification, vous obtiendrez une erreur.

![Screenshot-2021-03-13-05-19-29-1](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-05-19-29-1.png)

C'est parce que notre application effectue le rendu de l'instruction return avant que l'appel API ne soit effectué, et il n'y a rien à afficher dans ce cas, ce qui génère une erreur "undefined".

Pour en savoir plus sur async/await, consultez [cet article][5].

### Comment créer le corps de notre application météo

Pour cette partie, nous allons utiliser la bibliothèque Semantic UI pour concevoir notre interface.

Créons une carte (card) qui affichera nos informations météo.

```
import React from 'react';
import './styles.css';
import { Card } from 'semantic-ui-react'

const CardExampleCard = ({weatherData}) => (
  <Card>
    <Card.Content>
        <Card.Header className="header">{weatherData.name}</Card.Header>
    </Card.Content>
  </Card>
)

export default CardExampleCard;
```

Weather.js

Ici, nous importons une `Card` de semantic-ui-react, et à l'intérieur de cette carte, un `Header` qui affichera le nom de votre ville.

Mais la question est : comment faire passer les données de notre app.js au composant weather.js ?

La réponse est simple. Nous pouvons utiliser les **props** dans React pour envoyer des données d'un composant parent vers un composant enfant. Dans notre cas, notre composant parent est app.js et notre composant enfant est weather.js.

Pour ce faire, ajoutez simplement les props dans le composant dans **app.js**.

```
<Weather weatherData={data}/>
```

Ici, nous passons les données avec le nom de prop weatherData. Et nous recevrons la prop weatherData dans **Weather.js**.

```
import React from 'react';
import './styles.css';
import { Card } from 'semantic-ui-react'

const CardExampleCard = ({weatherData}) => (
  <Card>
    <Card.Content>
        <Card.Header className="header">{weatherData.name}</Card.Header>
    </Card.Content>
  </Card>
)

export default CardExampleCard;
```

![Screenshot-2021-03-12-17-36-56](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-17-36-56.png)

Vous pouvez voir que nous obtenons le nom de la ville en fonction de la localisation.

De la même manière, nous pouvons ajouter plus de champs à notre composant météo.

```
import React from 'react';
import './styles.css';
import { Card } from 'semantic-ui-react'

const CardExampleCard = ({weatherData}) => (
  <Card>
    <Card.Content>
        <Card.Header className="header">City Name: {weatherData.name}</Card.Header>
        <p>Temprature: {weatherData.main.temp}</p>
        <p>Sunrise: {weatherData.sys.sunrise}</p>
        <p>Sunset: {weatherData.sys.sunset}</p>
        <p>Description: {weatherData.weather[0].description}</p>
    </Card.Content>
  </Card>
)

export default CardExampleCard;
```

Nous pouvons obtenir la température, le lever du soleil, le coucher du soleil et la description à partir de l'API.

![Screenshot-2021-03-12-17-45-36-1](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-12-17-45-36-1.png)

Vous pouvez ajouter tous les autres champs que vous souhaitez, comme l'humidité, la vitesse du vent, la visibilité, etc.

### Comment formater les données et ajouter le jour et la date d'aujourd'hui

Formatons les données pour qu'elles soient faciles à comprendre. Nous allons ajouter quelques champs supplémentaires.

Pour commencer, ajoutez l'unité de température. Vous pouvez le faire en ajoutant **&deg;C** après la température.

De plus, changeons l'heure du lever et du coucher du soleil pour l'heure locale.

```
import React from 'react';
import './styles.css';
import { Card } from 'semantic-ui-react'

const CardExampleCard = ({weatherData}) => (
  <Card>
    <Card.Content>
        <Card.Header className="header">City Name: {weatherData.name}</Card.Header>
        <p>Temprature: {weatherData.main.temp} &deg;C</p>
        <p>Sunrise: {new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString('en-IN')}</p>
        <p>Sunset: {new Date(weatherData.sys.sunset * 1000).toLocaleTimeString('en-IN')}</p>
        <p>Description: {weatherData.weather[0].main}</p>
        <p>Humidity: {weatherData.main.humidity} %</p>
    </Card.Content>
  </Card>
)

export default CardExampleCard;
```

Maintenant, ajoutons le jour et la date d'aujourd'hui en utilisant **moment.js**.

```
import moment from 'moment';

<p>Day: {moment().format('dddd')}</p>
<p>Date: {moment().format('LL')}</p>
```

Utilisation de moment.js

Nous importons le paquet **moment** en haut et affichons respectivement le jour et la date d'aujourd'hui. L'avantage de ce paquet est qu'il met automatiquement à jour la date et le jour.

Voici à quoi ressemble notre **weather.js** maintenant :

```
import React from 'react';
import './styles.css';
import { Card } from 'semantic-ui-react';
import moment from 'moment';

const CardExampleCard = ({weatherData}) => (
  <Card>
    <Card.Content>
        <Card.Header className="header">City Name: {weatherData.name}</Card.Header>
        <p>Temprature: {weatherData.main.temp} &deg;C</p>
        <p>Sunrise: {new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString('en-IN')}</p>
        <p>Sunset: {new Date(weatherData.sys.sunset * 1000).toLocaleTimeString('en-IN')}</p>
        <p>Description: {weatherData.weather[0].main}</p>
        <p>Humidity: {weatherData.main.humidity} %</p>
        <p>Day: {moment().format('dddd')}</p>
        <p>Date: {moment().format('LL')}</p>
    </Card.Content>
  </Card>
)

export default CardExampleCard;
```

weather.js

![Screenshot-2021-03-13-12-16-14](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-12-16-14.png)

Et voici notre résultat.

## Ajoutons du style

Maintenant que nous avons toutes nos données, stylisons-les pour rendre l'application plus attrayante.

Tout d'abord, agrandissons la carte, changeons le border-radius, ajoutons une police et une couleur plus sympas, et supprimons l'alignement du texte.

```
import React from 'react';
import './styles.css';
import moment from 'moment';

const CardExampleCard = ({weatherData}) => (
  <div className="main">
      <p className="header">{weatherData.name}</p>
      <div>
        <p className="day">Day: {moment().format('dddd')}</p>
      </div>

      <div>
        <p className="temp">Temprature: {weatherData.main.temp} &deg;C</p>
      </div>
      
  </div>
)

export default CardExampleCard;
```

weather.js

```
@import url('https://fonts.googleapis.com/css2?family=Recursive&display=swap');

.main{
    width: 700px;
    border-radius: 15px;
    background-color: #01579b;
}

.header{
    background-color: #424242;
    color: whitesmoke;
    padding: 10px;
    font-size: 28px;
    border-radius: 15px;
    font-family: 'Recursive', sans-serif;
}

.day{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 24px;
    font-weight: 600;
}

.temp{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 18px;
}
```

styles.css

![Screenshot-2021-03-13-12-48-03](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-12-48-03.png)

Voici à quoi ressemble notre application maintenant.

Utilisons **flexbox** pour organiser les données en colonnes.

```
<div className="flex">
   <p className="day">Day: {moment().format('dddd')}</p>
</div>

<div className="flex">
   <p className="temp">Temprature: {weatherData.main.temp} &deg;C</p>
</div>
```

Nommez les divs 'flex' et ajoutez la propriété suivante dans **_styles.css_**.

```
.flex{
    display: flex;
    justify-content: space-between;
}
```

Notre weather.js ressemblera maintenant à ceci.

```
import React from 'react';
import './styles.css';
import moment from 'moment';

const CardExampleCard = ({weatherData}) => (
  <div className="main">
      <p className="header">{weatherData.name}</p>
      <div className="flex">
        <p className="day">Day: {moment().format('dddd')}</p>
        <p className="day">{moment().format('LL')}</p>
      </div>

      <div className="flex">
        <p className="temp">Temprature: {weatherData.main.temp} &deg;C</p>
        <p className="temp">Humidity: {weatherData.main.humidity} %</p>
      </div>
      
      
  </div>
)

export default CardExampleCard;
```

![Screenshot-2021-03-13-12-56-27](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-12-56-27.png)

De la même manière, ajoutez les champs restants.

```
import React from 'react';
import './styles.css';
import moment from 'moment';

const WeatherCard = ({weatherData}) => (
  <div className="main">
      <p className="header">{weatherData.name}</p>
      <div className="flex">
        <p className="day">{moment().format('dddd')}, <span>{moment().format('LL')}</span></p>
        <p className="description">{weatherData.weather[0].main}</p>
      </div>

      <div className="flex">
        <p className="temp">Temprature: {weatherData.main.temp} &deg;C</p>
        <p className="temp">Humidity: {weatherData.main.humidity} %</p>
      </div>

      <div className="flex">
        <p className="sunrise-sunset">Sunrise: {new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString('en-IN')}</p>
        <p className="sunrise-sunset">Sunset: {new Date(weatherData.sys.sunset * 1000).toLocaleTimeString('en-IN')}</p>
      </div>
    
  </div>
)

export default WeatherCard;
```

weather.js

```
@import url('https://fonts.googleapis.com/css2?family=Recursive&display=swap');

.main{
    width: 700px;
    border-radius: 20px;
    background-color: #01579b;
}

.top{
    height: 60px;
    background-color: #424242;
    color: whitesmoke;
    padding: 10px;
    border-radius: 20px 20px 0 0;
    font-family: 'Recursive', sans-serif;
    display: flex;
    justify-content: space-between;
}

.header{
    background-color: #424242;
    color: whitesmoke;
    margin: 10px 0px 0px 10px;
    font-size: 25px;
    border-radius: 20px 20px 0 0;
    font-family: 'Recursive', sans-serif;
}

.day{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 24px;
    font-weight: 600;
}

.temp{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 18px;
}

.flex{
    display: flex;
    justify-content: space-between;
}

.sunrise-sunset{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 16px;
}

.description{
    padding: 15px;
    color: whitesmoke;
    font-family: 'Recursive', sans-serif;
    font-size: 24px;
    font-weight: 600;
}
```

styles.css

Voici à quoi ressemble notre application maintenant :

![Screenshot-2021-03-13-13-37-46](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-13-37-46.png)

### Comment ajouter un bouton d'actualisation

Ajoutons un bouton d'actualisation en haut de notre page.

```
import React from 'react';
import './styles.css';
import moment from 'moment';
import { Button } from 'semantic-ui-react';

const refresh = () => {
  window.location.reload();
}

const WeatherCard = ({weatherData}) => (
  <div className="main">

      <div className="top">
        <p className="header">{weatherData.name}</p>
        <Button className="button" inverted color='blue' circular icon='refresh' onClick={refresh} />
      </div>
      <div className="flex">
        <p className="day">{moment().format('dddd')}, <span>{moment().format('LL')}</span></p>
        <p className="description">{weatherData.weather[0].main}</p>
      </div>

      <div className="flex">
        <p className="temp">Temprature: {weatherData.main.temp} &deg;C</p>
        <p className="temp">Humidity: {weatherData.main.humidity} %</p>
      </div>

      <div className="flex">
        <p className="sunrise-sunset">Sunrise: {new Date(weatherData.sys.sunrise * 1000).toLocaleTimeString('en-IN')}</p>
        <p className="sunrise-sunset">Sunset: {new Date(weatherData.sys.sunset * 1000).toLocaleTimeString('en-IN')}</p>
      </div>
    
  </div>
)

export default WeatherCard;
```

weather.js

```
.button{
    width: 35px;
    height: 35px;
}
```

styles.css

![Screenshot-2021-03-13-13-51-37](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-13-13-51-37.png)

Vous pouvez voir un bouton qui déclenchera la fonction d'actualisation. Lorsque vous appuyez dessus, la page sera actualisée.

### Comment ajouter un loader pendant le chargement de l'application

Ajoutons un loader pour rendre l'application encore plus professionnelle.

Importez `Loader` de Semantic UI et ajoutez-le dans la fonction return, là où nous vérifions si les données sont indéfinies.

```
import { Dimmer, Loader } from 'semantic-ui-react';

<div className="App">
      {(typeof data.main != 'undefined') ? (
        <Weather weatherData={data}/>
      ): (
        <div>
          <Dimmer active>
            <Loader>Loading..</Loader>
          </Dimmer>
       </div>
     )}
 </div>
```

app.js

## Récapitulons ce que nous avons fait

Nous avons créé une application React qui affiche la météo actuelle en fonction de votre position.

Passons en revue tout ce que nous avons accompli jusqu'à présent.

### Nous avons appris les concepts de State et de Props

Le State et les Props sont des fonctionnalités très puissantes de React. Ils sont utilisés pour gérer les données et contrôler leur flux entre les différents composants.

Dans notre application, nous gérons le state (l'état) de l'application. Par exemple, le nom de la ville, la température, la date, l'humidité, etc. Ces valeurs varient d'un utilisateur à l'autre, en fonction de leur localisation.

Les Props, quant à elles, sont utilisées pour passer des données entre les composants. Nous récupérons les données dans notre fichier **app.js**, mais nous les lisons dans **weather.js**. N'oubliez pas que les props ne peuvent être utilisées que pour passer des données d'un composant parent vers un composant enfant.

### Nous avons utilisé les Hooks React

Si vous avez déjà utilisé des composants de classe, vous connaissez sans doute les méthodes de cycle de vie. Sinon, sachez que ce sont des méthodes appelées lorsque notre page est rendue ou re-rendue. Mais nous ne pouvons pas utiliser de méthodes de cycle de vie dans les composants fonctionnels, car elles sont spécifiquement conçues pour les composants de classe.

Les Hooks React sont donc l'alternative. Nous avons utilisé deux hooks dans notre application. L'un est `useState`, utilisé pour gérer l'état de l'application. L'autre est `useEffect`, qui se charge lorsque la page est rendue ou chargée.

### Nous avons testé Semantic UI

Semantic UI est une bibliothèque pour React qui propose des composants prédéfinis de grande qualité.

C'est tout pour aujourd'hui. Vous pouvez ajouter d'autres fonctionnalités à l'application, comme des prévisions sur cinq jours, des icônes, et plus encore.

Vous pouvez [trouver le code sur GitHub][6] si vous souhaitez expérimenter davantage.

Vous pouvez également [regarder ce tutoriel sur ma chaîne YouTube][7] si vous le souhaitez.

> Expérimentez par vous-même, et bon apprentissage !

[1]: https://nodejs.org/en/
[2]: https://react.semantic-ui.com/usage/
[3]: https://momentjs.com/
[4]: https://home.openweathermap.org/users/sign_up
[5]: https://www.freecodecamp.org/news/async-await-in-javascript/
[6]: https://github.com/nishant-666/React-weather
[7]: https://youtu.be/Y1wKWIRNthQ