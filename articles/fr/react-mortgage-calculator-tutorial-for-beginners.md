---
title: Apprendre React en construisant une calculatrice de prêt hypothécaire
subtitle: ''
author: Joy Shaheb
co_authors: []
series: null
date: '2023-03-27T22:56:14.000Z'
originalURL: https://freecodecamp.org/news/react-mortgage-calculator-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/thumbnail_EN--2-.png
tags:
- name: beginner
  slug: beginner
- name: React
  slug: react
seo_title: Apprendre React en construisant une calculatrice de prêt hypothécaire
seo_desc: 'Today we will learn and practice ReactJs by building a mortgage calculator
  step by step. This is the project that we will build today 👇



  Heres a live demo of the project

  And here''s the Github Repo Link


  Objectives

  The topics we''ll cover while build...'
---

Aujourd'hui, nous allons apprendre et pratiquer ReactJs en construisant une calculatrice de prêt hypothécaire étape par étape. Voici le projet que nous allons construire aujourd'hui 👇

![Image du projet](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ryoc8jihbyprgp50ulhm.png)

* [Voici une démo en direct du projet](https://mortgage-calculator-tutorial.vercel.app/)
* [Et voici le lien du dépôt GitHub](https://github.com/JoyShaheb/mortgage-calculator-tutorial)

## Objectifs

Les sujets que nous aborderons lors de la construction de ce projet sont :
* Composants fonctionnels React
* Material UI
* Entrées utilisateur (User Inputs)
* Gestion des Props
* Déstructuration des props
* Hook useState

Et bien plus encore ! Ce cours est excellent pour les débutants qui souhaitent apprendre ReactJs en construisant un projet concret.

## Vous pouvez également regarder ce tutoriel sur YouTube si vous le souhaitez :

%[https://youtu.be/uluphP4xXD8]


## Table des matières

- [Configuration du projet](#configuration-du-projet)
- [Structure des dossiers](#structure-des-dossiers)
- [Thème Material UI](#theme-material-ui)
- [Comment construire la barre de navigation](#comment-construire-la-barre-de-navigation)
- [Système de grille Material UI](#systeme-de-grille-material-ui)
- [Comment construire le composant Slider](#comment-construire-le-composant-slider)
- [Faites une pause](#faites-une-pause)
- [Comment utiliser le hook useState](#comment-utiliser-le-hook-usestate)
- [Comment construire le composant SliderSelect](#comment-construire-le-composant-sliderselect)
- [Comment construire le composant TenureSelect](#comment-construire-le-composant-tenureselect)
- [Comment construire le composant Result](#comment-construire-le-composant-result)
- [Conclusion](#heading-conclusion)
- [Mes liens vers les réseaux sociaux](#mes-liens-vers-les-reseaux-sociaux)

## Configuration du projet

![Configuration du projet](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/02wjpjpo4k6tjg78ynu4.png)

Afin de configurer le projet, nous devons installer `react`, `material-ui` et d'autres packages nécessaires. 

Commencez par créer un dossier nommé `mortgage-calculator`, ouvrez-le dans VS Code, puis exécutez la commande suivante dans le terminal :

```bash
npx create-react-app .
npm install @mui/material @emotion/react @emotion/styled
npm install --save chart.js react-chartjs-2
```

### App.js

Nous allons supprimer tout le code passe-partout de `app.js` et conserver cette portion 👇

```js
import React from "react";

function App() {
  return <div className="App">Bonjour à tous</div>;
}

export default App;
```

Ensuite, exécutez cette commande dans le terminal pour démarrer le serveur :

```bash
npm start
```

Le projet devrait maintenant apparaître totalement vide sur le navigateur web.

### Commençons à coder

![Commençons à coder](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qew6q8zwn723s86md4rf.png)

Tout est configuré et prêt. Nous allons maintenant commencer à construire le projet :)

## Structure des dossiers

![Structure des dossiers](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7hujbmnjhri7470r2rxk.png)

Notre structure de dossiers devrait ressembler à ceci afin que nous puissions facilement gérer et maintenir nos fichiers et dossiers :

```bash
mortgage-calculator/
├── src/
│   ├── Components/
│   │   ├── Common/
│   │   │   └── SliderComponent.js
│   │   ├── Navbar.js
│   │   ├── Result.js
│   │   ├── SliderSelect.js
│   │   └── TenureSelect.js
│   ├── theme.js
│   ├── App.js
│   └── index.js
├── .gitignore
├── package.json
└── package-lock.json
```

Voici une image de la structure des dossiers de notre projet si vous êtes confus :

![Structure des dossiers](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9q9ezw36rp0mcfo12qsw.png)

## Thème Material UI

![Thème MUI](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/mxoseeckq7zgnidn4yol.png)

Nous utiliserons le thème sombre de Material UI. Pour cela, nous devons créer un fichier nommé `theme.js` dans le dossier `src` et ajouter le code suivant :

### theme.js

```js
import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    mode: 'dark',
  },
})
```

### index.js

Ensuite, nous devons importer le `theme` dans le fichier `index.js` et envelopper l'application avec le `ThemeProvider`. Suivez les étapes ci-dessous : 👇

```js
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import { theme } from "./theme";

<React.StrictMode>
  <ThemeProvider theme={theme}>
    <App />
    <CssBaseline />
  </ThemeProvider>
</React.StrictMode>
```

**Note :** Si vous ne passez pas le composant `CssBaseline`, nous ne pourrons pas voir le thème sombre de MUI.

Voici le résultat jusqu'à présent : 👇

![Résultat jusqu'à présent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/j117t2x35qebkx3qf21r.png)

L'écran entier sera sombre. Cela signifie que le mode sombre a été appliqué à notre projet depuis Material UI.

## Comment construire la barre de navigation

![Configuration de la barre de navigation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tx7urj6lh5710anwtqa8.png)

Ensuite, nous allons créer une barre de navigation (Navbar) très simple pour afficher le logo. Pour cela, nous devons créer un fichier nommé `Navbar.js` dans le dossier `src/Components` et ajouter le code suivant :

### Navbar.js

```js
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import { Container } from "@mui/system";

const Navbar = () => {
  return (
    <AppBar position="static">
      <Container maxWidth='xl'>
        <Toolbar>
          <Typography variant="h5">
            Bank of React
          </Typography>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Navbar;
```

Voici une explication rapide des composants utilisés de Material UI :

- **AppBar :** Le composant Appbar de Material UI est utilisé pour créer une barre de navigation supérieure dans l'interface utilisateur. [En savoir plus ici](https://mui.com/material-ui/react-app-bar/)
- **Container :** Le composant Container de Material UI est utilisé pour créer un élément conteneur permettant de créer une mise en page responsive, de centrer et de contenir d'autres éléments. [En savoir plus ici](https://mui.com/material-ui/react-container/)
- **ToolBar :** Le composant Toolbar peut contenir des éléments tels que des boutons, du texte et des icônes, et peut également être utilisé pour créer une mise en page responsive s'adaptant à différentes tailles d'écran. [En savoir plus ici](https://mui.com/material-ui/api/toolbar/)
- **Typography :** Le composant Typography de Material UI est utilisé pour appliquer des styles typographiques prédéfinis aux éléments de texte. Il aide à créer une mise en page cohérente et visuellement agréable avec une police, une taille, un poids et un espacement personnalisables. [En savoir plus ici](https://mui.com/material-ui/react-typography/)

### App.js

Enfin, importez-le dans `App.js` et écrivez le code comme ceci : 👇

```js
import React from "react";
import Navbar from "./Components/Navbar";

function App() {
  return (
    <div className="App">
      <Navbar />
    </div>
  );
}

export default App;
```

Voici le résultat jusqu'à présent : 👇

![Résultat de la barre de navigation](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lv52resgdtg2wpgqq4xa.png)

## Système de grille Material UI

![Système de grille MUI](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bd60xyrgs28g75eulshc.png)

Dans le projet finalisé, nous pouvons voir que notre contenu est divisé en 2 parties. À gauche, nous avons les composants curseurs (sliders) et à droite, nous avons le diagramme circulaire. Ceci est rendu possible grâce au [système de grille (Grid) de Material UI](https://mui.com/material-ui/react-grid/).

![Image du projet finalisé](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ezdk2jrt1dg88wac6iyu.png)

De plus, nous pouvons également voir que le contenu est responsive sur les écrans de plus petite taille. Ceci est également possible grâce au système de grille de Material UI.

![Contenu responsive](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5a1e5356nbnr74y6r6ze.png)

Pour reproduire cela, nous devons écrire ces éléments dans notre fichier App.js. Vous pouvez suivre ici. 👇

Tout d'abord, nous devons importer tous les composants requis de Material UI et de notre dossier de composants :

```js
import React, { useState } from "react";
import { Grid } from "@mui/material";
import { Container } from "@mui/system";
import Navbar from "./Components/Navbar";
import Result from "./Components/Result";
import SliderSelect from "./Components/SliderSelect";
import TenureSelect from "./Components/TenureSelect";
```

Ensuite, nous écrivons ce code à l'intérieur de l'instruction `return` comme ceci : 👇

```js
<div className="App">
  <Navbar />
  <Container maxWidth="xl" sx={{marginTop:4}}>
    <Grid container spacing={5} alignItems="center">
      <Grid item xs={12} md={6}>
        <SliderSelect />
        <TenureSelect />
      </Grid>
      <Grid item xs={12} md={6}>
        <Result/>
      </Grid>
    </Grid>
  </Container>
</div>
```

Explication du code :

- **Container :** Sur le `Container`, nous avons écrit `sx={{marginTop:4}}`. C'est la façon d'ajouter du style en ligne (inline-style) à un composant dans Material UI.
- **Grid :** Le composant Grid est utilisé pour créer une mise en page responsive s'adaptant à différentes tailles d'écran. `Grid container` représente l'élément parent et `Grid item` représente l'élément enfant.
- Sur le composant `Grid`, nous avons écrit `spacing={5}`. C'est la façon d'ajouter de l'espacement entre les éléments de la grille.
- Sur le composant `Grid`, nous avons également écrit `xs={12}`, ce qui signifie que l'élément de grille occupera toute la largeur de l'écran sur les très petits écrans. De même, `md={6}` signifie que l'élément occupera la moitié de l'écran sur les écrans moyens et plus grands. C'est ainsi que nous rendons nos composants responsives.

Voici le résultat jusqu'à présent : 👇

![Image du résultat du système Grid](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/jr80ud2oawv7nj6xti75.png)

## Comment construire le composant Slider

![Composant Slider](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1psq4l7lbwl1c2aizo6j.png)

Ensuite, nous allons créer un composant curseur (slider) pour obtenir le montant d'entrée de l'utilisateur. Il ressemblera à ceci : 👇

![Composant Slider](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oth4rtfgebeylr1kjktn.png)

Pour cela, nous devons créer un fichier nommé `SliderComponent.js` dans le dossier `src/Components/Common`. Listons d'abord toutes les props que nous devons passer à notre composant slider réutilisable :

- **label**
- **min**
- **max**
- **defaultValue**
- **unit**
- **value**
- **steps**
- **amount**
- **onChange**

### SliderComponent.js

C'est parti. Tout d'abord, importez les composants suivants de MUI dans le fichier `SliderComponent.js` :

```js
import React from "react";
import Slider from "@mui/material/Slider";
import { Typography } from "@mui/material";
import { Stack } from "@mui/system";
```

Nous utiliserons le [composant Stack de MUI](https://mui.com/material-ui/react-stack/) pour empiler les composants verticalement. `my` est le raccourci pour `marginY` [margin-top & margin-bottom]. Nous utiliserons le composant `Typography` de MUI pour afficher le libellé (label), l'unité et d'autres données. Nous utiliserons le composant `Slider` de MUI pour afficher le curseur.

Écrivez d'abord cette petite portion de code, avec nos props déstructurées :

```js
const SliderComponent = ({
  defaultValue,
  min,
  max,
  label,
  unit,
  onChange,
  amount,
  value,
  steps
}) => {
  return (
    <Stack my={1.4}>

    </Stack>
  )
}

export default SliderComponent
```

Nous allons écrire ce code pour afficher le libellé, l'unité et le montant.

```jsx
<Stack gap={1}>
  <Typography variant="subtitle2">{label}</Typography>
  <Typography variant="h5">
    {unit} {amount}
  </Typography>
</Stack>
```

Nous écrirons ce code pour afficher le curseur. Nous passerons les props au composant slider comme ceci : 👇

```jsx
<Slider
  min={min}
  max={max}
  defaultValue={defaultValue}
  aria-label="Default"
  valueLabelDisplay="auto"
  onChange={onChange}
  value={value}
  marks
  step={steps}
/>
```

Nous écrirons ce code pour afficher les valeurs min et max du curseur. Nous utiliserons le composant `Stack` de MUI pour empiler les composants horizontalement. `direction="row"` est le raccourci pour `flex-direction: row`. `justifyContent="space-between"` est le raccourci pour `justify-content: space-between`.

```js
<Stack direction="row" justifyContent="space-between">
  <Typography variant="caption" color="text.secondary">
    {unit} {min}
  </Typography>
  <Typography variant="caption" color="text.secondary">
    {unit} {max}
  </Typography>
</Stack>
```

Beau travail jusqu'ici !

## Faites une pause

![Faites une pause](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k9s9yorz1gwt380tbr7t.png)

Faites une pause – vous le méritez ! 🎉

## Comment utiliser le Hook useState

![Hook useState](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/89cx3gxzdl5h7q0okf8f.png)

Nous devons utiliser le hook useState de React dans notre projet. Mais avant cela, nous devons comprendre ce qu'est ce hook et pourquoi nous devons l'utiliser.

Le hook useState est une fonction intégrée à React qui vous permet d'ajouter un état (state) aux composants fonctionnels. Il renvoie un `tableau` contenant deux éléments : la valeur d'état actuelle et une fonction pour mettre à jour cette valeur. La syntaxe générale du hook useState est la suivante :

```js
const [state, setState] = useState(initialState);
```

Voici ce qui se passe : 👇

- `state` : Le nom de la constante ou variable qui stockera l'état.
- `setState` : Une fonction pour mettre à jour l'état.
- `initialState` : La valeur initiale de l'état.

### Exemple du hook useState

Nous allons créer un bouton à bascule (toggle) qui change son texte entre "ON" et "OFF" lorsqu'on clique dessus.

```js
import React, { useState } from 'react';

const ToggleButton = () => {
  const [isOn, setIsOn] = useState(false);

  const toggle = () => setIsOn(!isOn)

  return (
      <button onClick={toggle}>{isOn ? 'ON' : 'OFF'}</button>
  );
};

export default ToggleButton;

```

Ici, nous initialisons l'état `isOn` avec une valeur initiale de `false`. La fonction `toggle` met à jour l'état `isOn` à sa valeur opposée lorsque l'utilisateur clique sur le bouton. Nous utilisons un `opérateur ternaire` pour rendre le texte à l'intérieur du bouton en fonction de la valeur actuelle de `isOn`.

### App.js

Revenons maintenant à notre projet. Tout d'abord, allez dans le fichier `App.js` et importez le hook `useState` de React.

```js
import React, { useState } from 'react';
```

Ensuite, nous allons déclarer un état pour stocker la valeur des curseurs à l'aide du hook `useState`. Nous passerons la valeur initiale de l'état sous forme de `{}` à l'intérieur du hook `useState`, car nous stockons nos données sous forme d'objet.

```js
function App() {
  const [data, setData] = useState({})

  // les autres codes sont ici
}
```

Nous utilisons le hook useState pour créer une nouvelle variable d'état appelée `data` et une fonction appelée `setData` que nous pouvons utiliser pour mettre à jour l'état.

Ensuite, nous passerons ces valeurs comme valeurs par défaut pour notre composant slider.

```js
function App() {
  const [data, setData] = useState({
    homeValue: 3000,
    downPayment: 3000 * 0.2,
    loanAmount: 3000 * 0.8,
    loanTerm: 5,
    interestRate: 5,
  })

  // les autres codes sont ici
}
```

Ensuite, nous passerons les états `data` et `setData` en tant que prop au composant `SliderSelect` comme ceci : 👇

```js
<div className="App">
  <Navbar />
  <Container maxWidth="xl" sx={{marginTop:4}}>
    <Grid container spacing={5} alignItems="center">
      <Grid item xs={12} md={6}>

        {/* c'est ici que nous écrivons le code 👇 */}
        <SliderSelect data={data} setData={setData}/>

        <TenureSelect />
      </Grid>
      <Grid item xs={12} md={6}>
        <Result/>
      </Grid>
    </Grid>
  </Container>
</div>
```

## Comment construire le composant SliderSelect

![Composant SliderSelect.js](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/001ovrcapajjl5i480dn.png)

Maintenant que notre `SliderComponent` réutilisable est prêt, utilisons-le dans notre composant `SliderSelect.js`. Tout d'abord, importez le composant `SliderComponent` du dossier `Common`.

### SliderSelect.js

```js
import SliderComponent from "./Common/SliderComponent";
```

Ensuite, nous allons déstructurer nos props que nous recevons de `App.js`. De plus, nous créerons une variable nommée `bank_limit` et lui assignerons une valeur de `10000`. Cela représente le montant maximum qu'une personne peut emprunter à notre banque.

```js
import React from "react";
import SliderComponent from "./Common/SliderComponent";

const SliderSelect = ({ data, setData }) => {
  const bank_limit = 10000;
  return (
    <div>
      
    </div>
  );
};

export default SliderSelect;

```

Ensuite, nous utiliserons notre `SliderComponent` pour afficher le curseur nommé `Home Value` (Valeur du bien). Ici, nous passerons les props comme ceci au composant `SliderComponent`.

```js
const SliderSelect = ({ data, setData }) => {
  const bank_limit = 10000;
  return (
    <div>
      <SliderComponent
        onChange={(e, value) => {
          setData({
            ...data,
            homeValue: value.toFixed(0),
            downPayment: (0.2 * value).toFixed(0),
            loanAmount: (0.8 * value).toFixed(0),
          });
        }}
        defaultValue={data.homeValue}
        min={1000}
        max={bank_limit}
        steps={100}
        unit="$"
        amount={data.homeValue}
        label="Valeur du bien"
        value={data.homeValue}
      />
    </div>
  );
};

```

Voici le résultat jusqu'à présent : 👇

![Curseur Valeur du bien](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tc8ymi79urkugw7kd4ci.png)

De la même manière, nous créerons les curseurs pour `Down Payment` (Apport initial) et `Loan Amount` (Montant du prêt) comme ceci : 👇

```js
  return (
    <div>
      {/* les autres codes sont ici */}

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            downPayment: value.toFixed(0),
            loanAmount: (data.homeValue - value).toFixed(0),
          })
        }
        defaultValue={data.downPayment}
        min={0}
        max={data.homeValue}
        steps={100}
        unit="$"
        amount={data.downPayment}
        label="Apport initial"
        value={data.downPayment}
      />

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            loanAmount: value.toFixed(0),
            downPayment: (data.homeValue - value).toFixed(0),
          })
        }
        defaultValue={data.loanAmount}
        min={0}
        max={data.homeValue}
        steps={100}
        unit="$"
        amount={data.loanAmount}
        label="Montant du prêt"
        value={data.loanAmount}
      />
    </div>
  );
```

Encore une fois, voici le résultat jusqu'à présent : 👇

![le résultat jusqu'à présent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/nvhfgzpf1aq02p3kwdqz.png)

Enfin, nous allons créer le curseur pour notre `Interest Rate` (Taux d'intérêt). Vous pouvez suivre ici : 👇

```js
return (
    <div>
      {/* les autres codes sont ici */}

      <SliderComponent
        onChange={(e, value) =>
          setData({
            ...data,
            interestRate: value,
          })
        }
        defaultValue={data.interestRate}
        min={2}
        max={18}
        steps={0.5}
        unit="%"
        amount={data.interestRate}
        label="Taux d'intérêt"
        value={data.interestRate}
      />
    </div>
  );
```

Voici le résultat jusqu'à présent : 👇

![Curseur Taux d'intérêt](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/snlpyvu2qfqzt81ecbvo.png)

## Comment construire le composant TenureSelect

Ensuite, nous allons construire le composant `TenureSelect`. Ce composant sera utilisé pour sélectionner la durée du prêt. Il ressemblera à ceci : 👇

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/70arqood9dwqj9j46apk.png)

### App.js

Tout d'abord, passez les états `data` et `setData` en tant que prop au composant `TenureSelect` comme ceci : 👇

```js
return (
  <div className="App">
    <Navbar />
    <Container maxWidth="xl" sx={{marginTop:4}}>
      <Grid container spacing={5} alignItems="center">
        <Grid item xs={12} md={6}>
          <SliderSelect data={data} setData={setData} />

          {/* c'est ici que nous écrivons le code 👇 */}
          <TenureSelect data={data} setData={setData}/>

        </Grid>
        <Grid item xs={12} md={6}>
          <Result data={data}/>
        </Grid>
      </Grid>
    </Container>
  </div>
);
```

### TenureSelect.js

Ensuite, importez ces composants requis de la bibliothèque `MUI` :

```js
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
```

Puis déstructurez les props que nous recevons de `App.js`. Créez également une fonction nommée `handleChange` qui sera utilisée pour définir l'état `tenure`, comme ceci : 👇

```js
const TenureSelect = ({ data, setData }) => {

  const handleChange = (event) => {
    setData({...data, loanTerm: event.target.value});
  };

  return ()
};

export default TenureSelect;
```

Ensuite, nous allons construire le composant `TenureSelect`. Il ressemblera à ceci : 👇

```js
return (
  <FormControl fullWidth>
    <InputLabel id="demo-simple-select-label">Durée</InputLabel>
    <Select
      labelId="demo-simple-select-label"
      id="demo-simple-select"
      value={data.loanTerm}
      label="Durée"
      defaultValue={5}
      onChange={handleChange}
    >
      <MenuItem value={5}>5 ans</MenuItem>
      <MenuItem value={10}>10 ans</MenuItem>
      <MenuItem value={15}>15 ans</MenuItem>
      <MenuItem value={20}>20 ans</MenuItem>
      <MenuItem value={25}>25 ans</MenuItem>
    </Select>
  </FormControl>
);
```

Le résultat jusqu'à présent : 👇

![Le résultat jusqu'à présent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fl0fsfk2lv9dnh588eyh.png)

## Comment construire le composant Result

Enfin, nous allons construire le composant `Result`. Ce composant sera utilisé pour afficher la mensualité du prêt et le diagramme circulaire. Il ressemblera à ceci : 👇

![Composant Result](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/7f5vgfcsk6aj6yseqvi1.png)

### App.js

Tout d'abord, passez l'état `data` en tant que prop au composant `Result` comme ceci : 👇

```js
return (
  <div className="App">
    <Navbar />
    <Container maxWidth="xl" sx={{marginTop:4}}>
      <Grid container spacing={5} alignItems="center">
        <Grid item xs={12} md={6}>
          <SliderSelect data={data} setData={setData} />
          <TenureSelect data={data} setData={setData}/>
        </Grid>
        <Grid item xs={12} md={6}>

          {/* c'est ici que nous écrivons le code 👇 */}
          <Result data={data}/>
          
        </Grid>
      </Grid>
    </Container>
  </div>
);
```

### Result.js

Ensuite, importez les composants requis comme ceci : 👇

```js
import React from "react";
import { Stack, Typography } from "@mui/material";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Pie } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);
```

Ensuite, déstructurez l'état `data` que nous recevons de `App.js` comme ceci : 👇

```js
const Result = ({ data }) => {
  const { homeValue, loanAmount, loanTerm, interestRate } = data;
  return ();
};

export default Result;
```

Ensuite, nous allons écrire tous ces éléments qui nous aideront à effectuer le calcul : 👇

```js
  const totalLoanMonths = loanTerm * 12;
  const interestPerMonth = interestRate / 100 / 12;
  const monthlyPayment =
    (loanAmount *
      interestPerMonth *
      (1 + interestPerMonth) ** totalLoanMonths) /
    ((1 + interestPerMonth) ** totalLoanMonths - 1);

  const totalInterestGenerated = monthlyPayment * totalLoanMonths - loanAmount;
```

Ensuite, nous avons besoin de cette variable pour stocker toutes les données de notre diagramme circulaire, comme ceci : 👇

```js
const pieChartData = {
  labels: ["Principal", "Intérêts"],
  datasets: [
    {
      label: "Ratio du Principal et des Intérêts",
      data: [homeValue, totalInterestGenerated],
      backgroundColor: ["rgba(255, 99, 132, 0.2)", "rgba(54, 162, 235, 0.2)"],
      borderColor: ["rgba(255, 99, 132, 1)", "rgba(54, 162, 235, 1)"],
      borderWidth: 1,
    },
  ],
};
```

Enfin, nous allons construire le composant `Result`. Il ressemblera à ceci : 👇

```js
return (
  <Stack gap={3}>
    <Typography textAlign="center" variant="h5">
      Mensualité : $ {monthlyPayment.toFixed(2)}
    </Typography>
    <Stack direction="row" justifyContent="center">
      <div>
        <Pie data={pieChartData} />
      </div>
    </Stack>
  </Stack>
);
```

Voici le résultat final : 👇

![Le résultat jusqu'à présent](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gqs2st1o5fhlpoqnpqol.png)

## Conclusion

![Félicitations](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z7w7p11dm81ggzxd6a1t.png)

Félicitations pour avoir lu jusqu'au bout ! Vous pouvez désormais utiliser React JS et Material UI avec confiance et efficacité pour construire des projets sympas.

Vous avez également appris à utiliser le hook useState de React et à gérer les props. J'espère que vous avez apprécié ce tutoriel.

## Programme de mentorat

Si vous souhaitez en savoir plus sur React JS et le développement web, je propose un programme de mentorat. Vous pouvez consulter les détails ici 👉 [Mentor Labs Academy](https://www.mentorlabs.academy/)

![Programme de mentorat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v5oyscu7l16tr636ekqj.png)

## Mes liens vers les réseaux sociaux

- [LinkedIn / JoyShaheb](https://www.linkedin.com/in/joyshaheb/)
- [YouTube / JoyShaheb](https://www.youtube.com/c/joyshaheb)
- [Twitter / JoyShaheb](https://twitter.com/JoyShaheb)
- [Instagram / JoyShaheb](https://www.instagram.com/joyshaheb/)