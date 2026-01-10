---
title: Tutoriel React – Comment construire une PWA de traduction de texte
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-16T14:54:16.000Z'
originalURL: https://freecodecamp.org/news/react-tutorial-build-a-text-translation-pwa
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/How-to-Build-a-Weather-Application-using-React--7-.png
tags:
- name: JavaScript
  slug: javascript
- name: projects
  slug: projects
- name: PWA
  slug: pwa
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Tutoriel React – Comment construire une PWA de traduction de texte
seo_desc: "By Nishant Kumar\nIn this article, I'll show you how to build a text translator\
  \ application using React. It will support 17 languages, and you can do cross translation\
  \ too. \nHere's what we'll create:\n\nThis is how our application will look after\
  \ we're ..."
---

Par Nishant Kumar

Dans cet article, je vais vous montrer comment construire une application de traduction de texte en utilisant React. Elle supportera 17 langues, et vous pourrez également faire des traductions croisées. 

Voici ce que nous allons créer :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-123442-1.png)

Voici à quoi ressemblera notre application une fois terminée. Elle dispose de deux zones de texte – l'une contiendra notre Texte Source, et l'autre contiendra notre Texte Résultat. Nous avons également un champ de sélection où l'utilisateur peut choisir les langues souhaitées. 

Alors, commençons sans plus tarder.

## Comment construire l'interface utilisateur

Afin de créer l'interface sans effort, nous allons utiliser une bibliothèque d'interface utilisateur appelée Semantic UI.

Alors, rendez-vous sur le site web de Semantic UI à l'adresse [https://react.semantic-ui.com/](https://react.semantic-ui.com/).

Ensuite, sélectionnez Get Started dans le menu de la barre latérale :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-112404.png)

Installez-le en utilisant l'une des commandes ci-dessous. Vous pouvez utiliser yarn add ou npm install.

```
$  yarn add semantic-ui-react semantic-ui-css
## Ou
$  npm install semantic-ui-react semantic-ui-css
```

Après l'installation, nous devons importer le package dans notre fichier index.js comme ceci :

```js
import 'semantic-ui-css/semantic.min.css'
```

Maintenant, nous pouvons utiliser Semantic UI.

### Comment créer les composants de l'application

Créons un composant appelé **Translate**. Celui-ci contiendra tous les éléments dont nous avons besoin. 

Tout d'abord, nous avons besoin d'un titre pour l'application. Donc, à l'intérieur du composant Translate, créez un titre comme ceci :

```
import React from 'react';

export default function Translate() {
    return (
        <div>
            <div className="app-header">
                <h2 className="header">Texty Translator</h2>
            </div>
        </div>
    )
}

```

Maintenant, ajoutons un peu de style avec CSS :

```
@import url('https://fonts.googleapis.com/css2?family=Azeret+Mono&display=swap');

.app-header{
  text-align: center;
  padding: 20px;
}

.header{
  font-family: 'Azeret Mono', monospace;
  font-size: 30px;
}
```

Ici, nous utilisons une police appelée Azeret Mono de Google Fonts, et nous avons aligné l'en-tête et lui avons donné un peu de padding.

Voici à quoi ressemblera notre en-tête à ce stade :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-113234.png)

Nous avons également besoin de quatre autres éléments. Le premier est notre zone de texte d'entrée, le second est le menu déroulant de sélection pour choisir la langue, le troisième est la zone de texte de sortie où notre texte traduit sera affiché, et le dernier est un bouton qui traduira notre texte.

Nous pouvons importer les éléments Form, TextArea, Button et Icon directement depuis Semantic UI comme ceci :

```
import {
    Form,
    TextArea,
    Button,
    Icon
} from 'semantic-ui-react';
```

Ensuite, nous créerons une autre div après `app-header` appelée `app-body` avec le code suivant :

```
import React from 'react';
import {
    Form,
    TextArea,
    Button,
    Icon
} from 'semantic-ui-react';

export default function Translate() {
    return (
        <div>
            <div className="app-header">
                <h2 className="header">Texty Translator</h2>
            </div>

            <div className='app-body'>
                <div>
                    <Form>
                        <Form.Field
                            control={TextArea}
                            placeholder='Tapez le texte à traduire..'
                        />

                        <select className="language-select">
                            <option>Veuillez sélectionner une langue..</option>
                        </select>

                        <Form.Field
                            control={TextArea}
                            placeholder='Votre résultat de traduction..'
                        />

                        <Button
                            color="orange"
                            size="large"
                        >
                            <Icon name='translate' />
                            Traduire</Button>
                    </Form>
                </div>
            </div>
        </div>
    )
}

```

Et nous ajouterons un peu de style avec le CSS suivant :

```
@import url('https://fonts.googleapis.com/css2?family=Azeret+Mono&display=swap');

.app-header{
  text-align: center;
  padding: 20px;
}

.header{
  font-family: 'Azeret Mono', monospace;
  font-size: 30px;
}

.app-body{
  padding: 20px;
  text-align: center;
}

.language-select{
  height: 40px !important;
  margin-bottom: 15px;
  outline: none !important;
}
```

Voici à quoi ressemblera notre application maintenant. Vous pouvez voir que nous avons les zones de texte, les options de sélection et un bouton pour traduire.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-114039.png)

### Comment configurer les API

Pour activer la traduction, nous utiliserons l'API [LibreTranslate](https://libretranslate.de/docs). Alors, rendez-vous sur leur site web pour choisir votre API.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-114304.png)

Comme vous pouvez le voir sur l'image ci-dessus, il y a quatre API.

Pour commencer, nous devons détecter notre langue d'entrée en utilisant l'API POST /detect.

### Comment installer Axios

Mais d'abord, installons Axios, car nous en aurons besoin pour faire des requêtes API.

Pour installer Axios, tapez simplement la commande ci-dessous :

```
yarn add axios

## OU

npm i axios
```

Nous pouvons utiliser soit yarn add axios soit npm i axios, selon le gestionnaire de paquets que vous avez installé.

Maintenant, importons-le dans notre composant Translate.

```
import axios from 'axios';
```

Nous avons également besoin des hooks useState et useEffect.

```
import React, { useState, useEffect } from 'react';
```

Ensuite, créez un état appelé inputText.

```
const [inputText, setInputText] = useState('');
```

Et dans le champ de zone de texte d'entrée, liez-le à un gestionnaire d'événement onChange.

```
<Form.Field
 control={TextArea}
 placeholder='Tapez le texte à traduire..'
 onChange={(e) => setInputText(e.target.value)}
/>
```

Si nous entrons un texte, il sera stocké dans l'état inputText.

### Comment appeler l'API de détection de langue

Maintenant, appelons l'API de détection de langue pour détecter notre langue d'entrée.

Créez une fonction appelée `getLanguageSource()` comme ceci :

```
const getLanguageSource = () => {
        axios.post(`https://libretranslate.de/detect`, {
            q: inputText
        })
        .then((response) => {
            console.log(response.data[0].language)
        })
    }
```

Ici, nous appelons l'API de détection, et nous passons notre entrée en tant que corps.

Nous utilisons axios.post pour envoyer le texte d'entrée en tant que corps, et nous utilisons q comme paramètre d'en-tête.

De plus, nous voudrons appeler cette fonction lors du clic sur le bouton Traduire, alors liez cette fonction au bouton Traduire comme ceci :

```
<Button
                            color="orange"
                            size="large"
                            onClick={getLanguageSource}
                        >
                            <Icon name='translate' />
                            Traduire</Button>
```

Tapez quelque chose dans la première zone d'entrée, puis appuyez sur le bouton Traduire. Vous verrez la clé de l'objet de la langue détectée dans la console, dont nous avons besoin.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-115444.png)

Maintenant, nous devons stocker cette clé de langue dans un état. Alors, créez un état appelé `detectLanguageKey`.

Ensuite, définissez l'état à partir de la réponse comme ceci :

```
const getLanguageSource = () => {
        axios.post(`https://libretranslate.de/detect`, {
            q: inputText
        })
            .then((response) => {
                setdetectedLanguageKey(response.data[0].language)
            })
    }
```

Nous définissons l'index zéro à partir des données de réponse, car c'est là que nos données commencent.

Voici le code complet jusqu'à ce point :

```
import React, { useState, useEffect } from 'react';
import {
    Form,
    TextArea,
    Button,
    Icon
} from 'semantic-ui-react';
import axios from 'axios';

export default function Translate() {
    const [inputText, setInputText] = useState('');
    const [detectLanguageKey, setdetectedLanguageKey] = useState('')
    const getLanguageSource = () => {
        axios.post(`https://libretranslate.de/detect`, {
            q: inputText
        })
            .then((response) => {
                setdetectedLanguageKey(response.data[0].language)
            })
    }

    return (
        <div>
            <div className="app-header">
                <h2 className="header">Texty Translator</h2>
            </div>

            <div className='app-body'>
                <div>
                    <Form>
                        <Form.Field
                            control={TextArea}
                            placeholder='Tapez le texte à traduire..'
                            onChange={(e) => setInputText(e.target.value)}
                        />

                        <select className="language-select">
                            <option>Veuillez sélectionner une langue..</option>
                        </select>

                        <Form.Field
                            control={TextArea}
                            placeholder='Votre résultat de traduction..'
                        />

                        <Button
                            color="orange"
                            size="large"
                            onClick={getLanguageSource}
                        >
                            <Icon name='translate' />
                            Traduire</Button>
                    </Form>
                </div>
            </div>
        </div>
    )
}

```

### Comment appeler l'API des langues supportées pour le menu déroulant de sélection

Maintenant, la deuxième API obtient les langues supportées. Nous utiliserons la liste dans notre menu déroulant de sélection.

Créez un hook useEffect pour appeler notre API des langues supportées. useEffect est une fonction qui s'exécutera chaque fois que notre composant sera rendu ou chargé.

```
useEffect(() => {
        axios.get(`https://libretranslate.de/languages`)
            .then((response) => {
                console.log(response.data)
            })
    }, [])
```

Ici, nous appelons l'API pour les langues supportées en utilisant la méthode axios.get. Ensuite, nous affichons la réponse dans la console.

Ouvrez la console pour vérifier la liste des langues. Vous devriez voir quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-120348.png)

Définissons ces données dans un état. Alors, créez un état appelé languagesList. Ce sera un tableau vide.

```
const [languagesList, setLanguagesList] = useState([])
```

```
useEffect(() => {
        axios.get(`https://libretranslate.de/languages`)
            .then((response) => {
                setLanguagesList(response.data)
            })
    }, [])
```

Ensuite, dans le hook useEffect, nous devons définir la liste des langues en utilisant `setLanguagesList`.

Nous devons afficher cette liste de langues dans l'option de sélection. Alors, mappons le menu déroulant de sélection en utilisant l'état `languagesList` comme ceci :

```
<select className="language-select">
                            <option>Veuillez sélectionner une langue..</option>
                            {languagesList.map((language) => {
                                return (
                                    <option value={language.code}>
                                        {language.name}
                                    </option>
                                )
                            })}
                        </select>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot--605-.png)

Maintenant, nous pouvons sélectionner notre langue dans le menu déroulant de sélection.

### Comment obtenir le code de la langue sélectionnée

Maintenant, si nous sélectionnons une langue – disons l'espagnol – nous devons obtenir le code de la langue, car nous avons besoin de ce code de langue dans notre API de traduction finale.

Créez une fonction appelée `languageKey()` comme ceci :

```
const languageKey = () => {
     
}
```

Et sur l'option de sélection, liez cette fonction en utilisant onChange :

```
<select className="language-select" onChange={languageKey}>
                            <option>Veuillez sélectionner une langue..</option>
                            {languagesList.map((language) => {
                                return (
                                    <option value={language.code}>
                                        {language.name}
                                    </option>
                                )
                            })}
                        </select>
```

De plus, nous devons stocker le code de la langue dans un état, alors créons-le.

Créez un état appelé `selectedLanguageKey`, qui contiendra notre clé de langue sélectionnée à partir de l'entrée de sélection.

```
const [selectedLanguageKey, setLanguageKey] = useState('')
```

Cette fonction languageKey acceptera un paramètre appelé `selectedLanguage`. Et nous stockerons ces données dans l'état `selectedLanguageKey`, que nous obtenons de l'option de sélection.

```
const languageKey = (selectedLanguage) => {
        setLanguageKey(selectedLanguage.target.value)
}
```

Maintenant, si vous regardez la documentation de LibreTranslate, nous avons besoin de trois entrées de données :

1. Le texte à traduire.
2. Le code de la langue source.
3. Le code de la langue cible.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-120659.png)

Nous n'avons pas besoin de la clé API car ce service est gratuit.

Nous avons les trois entrées dont nous avons besoin pour envoyer dans le corps contenues dans ces états ci-dessous :

```
const [inputText, setInputText] = useState('');
const [detectLanguageKey, setdetectedLanguageKey] = useState('');
const [selectedLanguageKey, setLanguageKey] = useState('')
```

Maintenant, appelons notre API finale, qui est /translate.

### Comment appeler l'API de traduction pour traduire notre texte

Créez un état final appelé resultText. Cet état contiendra notre texte traduit de sortie.

```
const [resultText, setResultText] = useState('');
```

Créez une fonction qui appellera l'API de traduction :

```
const translateText = () => {
       getLanguageSource();

        let data = {
            q : inputText,
            source: detectLanguageKey,
            target: selectedLanguageKey
        }
        axios.post(`https://libretranslate.de/translate`, data)
        .then((response) => {
            setResultText(response.data.translatedText)
        })
    }
```

Comme vous pouvez le voir, nous définissons inputText dans l'état resultText, et nous appelons la fonction getLanguageSource à l'intérieur de la fonction translateText. Donc, chaque fois que cette fonction s'exécute, getLanguageSource les déclenchera automatiquement pour obtenir la source de la langue. 

En d'autres termes, lors du clic sur cette fonction via le bouton Traduire, elle définira la source de la langue via getLanguageSource(), puis elle appellera l'API de traduction.

Alors, sur le bouton Traduire, liez cette fonction :

```
<Button
                            color="orange"
                            size="large"
                            onClick={translateText}
                        >
                            <Icon name='translate' />
                            Traduire</Button>
```

Ensuite, créons un objet appelé data. À l'intérieur, nous enverrons toutes les données que nous avons obtenues précédemment, comme inputText, detectLanguageKey et la clé selectedLanguage en tant que q, source et target respectivement.

```
let data = {
            q : inputText,
            source: detectLanguageKey,
            target: selectedLanguageKey
        }
```

Ensuite, nous appelons l'API de traduction en utilisant axios.post et envoyons l'objet data comme paramètre de corps.

```
let data = {
            q : inputText,
            source: detectLanguageKey,
            target: selectedLanguageKey
        }
        axios.post(`https://libretranslate.de/translate`, data)
```

Enfin, nous définissons les données de réponse entrantes dans l'état resultText.

```
.then((response) => {
            setResultText(response.data.translatedText)
        })
```

Alors, maintenant, tapez quelque chose dans la zone d'entrée, sélectionnez la langue et cliquez sur Traduire. Vous obtiendrez votre texte traduit.

Voici le code complet jusqu'à ce point, pour votre référence :

```
import React, { useState, useEffect } from 'react';
import {
    Form,
    TextArea,
    Button,
    Icon
} from 'semantic-ui-react';
import axios from 'axios';

export default function Translate() {
    const [inputText, setInputText] = useState('');
    const [detectLanguageKey, setdetectedLanguageKey] = useState('');
    const [selectedLanguageKey, setLanguageKey] = useState('')
    const [languagesList, setLanguagesList] = useState([])
    const [resultText, setResultText] = useState('');
    const getLanguageSource = () => {
        axios.post(`https://libretranslate.de/detect`, {
            q: inputText
        })
            .then((response) => {
                setdetectedLanguageKey(response.data[0].language)
            })
    }
    useEffect(() => {
        axios.get(`https://libretranslate.de/languages`)
            .then((response) => {
                setLanguagesList(response.data)
            })
    }, [])

    const languageKey = (selectedLanguage) => {
        setLanguageKey(selectedLanguage.target.value)
    }

    const translateText = () => {
        getLanguageSource();

        let data = {
            q : inputText,
            source: detectLanguageKey,
            target: selectedLanguageKey
        }
        axios.post(`https://libretranslate.de/translate`, data)
        .then((response) => {
            setResultText(response.data.translatedText)
        })
    }

    return (
        <div>
            <div className="app-header">
                <h2 className="header">Texty Translator</h2>
            </div>

            <div className='app-body'>
                <div>
                    <Form>
                        <Form.Field
                            control={TextArea}
                            placeholder='Tapez le texte à traduire..'
                            onChange={(e) => setInputText(e.target.value)}
                        />

                        <select className="language-select" onChange={languageKey}>
                            <option>Veuillez sélectionner une langue..</option>
                            {languagesList.map((language) => {
                                return (
                                    <option value={language.code}>
                                        {language.name}
                                    </option>
                                )
                            })}
                        </select>

                        <Form.Field
                            control={TextArea}
                            placeholder='Votre résultat de traduction..'
                            value={resultText}
                        />

                        <Button
                            color="orange"
                            size="large"
                            onClick={translateText}
                        >
                            <Icon name='translate' />
                            Traduire</Button>
                    </Form>
                </div>
            </div>
        </div>
    )
}

```

Maintenant, la dernière étape. Dans le hook useEffect, appelez la fonction `getLanguageSource()`, et définissez inputText dans le tableau de dépendances. Cela signifie que chaque fois que notre texte inputText change, ou que cet état est mis à jour, la fonction useEffect s'exécutera, et elle appellera `getLanguageSource()` chaque fois qu'elle s'exécute.

```
useEffect(() => {
       axios.get(`https://libretranslate.de/languages`)
       .then((response) => {
        setLanguagesList(response.data)
       })

       getLanguageSource()
    }, [inputText])
```

Maintenant, vérifions notre sortie :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Screenshot-2021-09-12-123442.png)

Tapez un texte comme entrée, et sélectionnez la langue. Appuyez sur Traduire, et vous verrez vos données traduites dans la sortie.

## Conclusion

Maintenant, vous savez comment construire un traducteur de texte en utilisant React. Vous pouvez créer votre propre interface utilisateur si vous le souhaitez. 

Alors, allez-y, construisez et expérimentez un peu. Il y a des tonnes de choses que vous pouvez faire.

Vous pouvez consulter ma vidéo sur [Let's Build a Text Translator Application using React](https://www.youtube.com/watch?v=R_I5t8r5qsA&t=5s&ab_channel=Cybernatico), qui est sur ma chaîne YouTube.

N'hésitez pas à télécharger le code ici : [https://github.com/nishant-666/Sanjeet-s-Translator](https://github.com/nishant-666/Sanjeet-s-Translator). Ne vous souciez pas du nom.

> Bon apprentissage.