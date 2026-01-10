---
title: Comment créer un éditeur de code avec React qui compile et exécute dans 40+
  langages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-24T16:54:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-react-based-code-editor
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/Build-a-React-Code-Editor-That-Compiles-and-Executes-in-10--Languages--1-.png
tags:
- name: Next.js
  slug: nextjs
- name: React
  slug: react
- name: tailwind
  slug: tailwind
seo_title: Comment créer un éditeur de code avec React qui compile et exécute dans
  40+ langages
seo_desc: "By Manu Arora\nAn online code execution platform lets you write code in\
  \ your favourite programming language and run that code on the same platform. \n\
  You can ideally see an output of the program that you've written (for example, a\
  \ binary search program..."
---

Par Manu Arora

Une plateforme d'exécution de code en ligne vous permet d'écrire du code dans votre langage de programmation préféré et d'exécuter ce code sur la même plateforme. 

Vous pouvez idéalement voir un résultat du programme que vous avez écrit (par exemple, un programme de recherche binaire écrit en JavaScript).  
  
Aujourd'hui, nous allons créer une plateforme d'exécution de code en ligne appelée CodeRush qui peut compiler et exécuter du code dans plus de 40 langages de programmation différents.

## Qu'allons-nous créer ?

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-18-at-9.05.14-PM.png)

[Code Source](https://github.com/manuarora700/react-code-editor) | [Démonstration en Direct](https://coderush.vercel.app)

Nous allons créer un éditeur de code riche qui possède les fonctionnalités suivantes :

- Un éditeur de code ([Monaco Editor](https://www.npmjs.com/package/monaco-editor)) qui alimente également VS Code.
- Il peut compiler du code sur une application web avec des entrées et sorties standard avec support pour plus de 40 langages de programmation.
- Vous pouvez changer le thème de l'éditeur à partir d'une liste de thèmes disponibles.
- Vous pouvez obtenir des informations sur le code exécuté (temps pris par le code, mémoire utilisée, statut, et plus).

## Stack Technique

Pour le projet, nous allons utiliser la stack technique suivante :

- [React.js](https://reactjs.org) – Pour le front-end
- [TailwindCSS](https://tailwindcss.com) – Pour les styles
- [Judge0](https://judge0.com) – Pour compiler et exécuter notre code.
- [RapidAPI](https://rapidapi.com) – Pour déployer rapidement le code Judge0.
- [Monaco Editor](https://www.npmjs.com/package/monaco-editor) – L'éditeur de code qui alimente le projet

## Structure du Projet

La structure du projet est assez simple et facile à comprendre :

- **Components** : Tous les composants / extraits de code réutilisables vivent ici (Exemple : CodeEditorWindow et Landing)
- **hooks** : Tous les hooks personnalisés sont présents ici. (Nous allons utiliser des hooks de pression de touche pour compiler notre code en utilisant des événements clavier)
- **lib** : Toutes les fonctions de bibliothèque vivent ici. (Nous allons créer une fonction pour définir notre thème ici)
- **constants** : Toutes les constantes comme `languageOptions` et `customStyles` pour les menus déroulants iront ici.
- **utils** : Les fonctions utilitaires générales pour aider à maintenir le code vont ici.

#### Flux de l'application :

Avant de plonger profondément dans le code, comprenons le flux de l'application et comment nous devons le coder à partir de zéro.

* Un utilisateur arrive sur l'application web et peut sélectionner ses langages de programmation préférés (par défaut JavaScript).
* Une fois que l'utilisateur a terminé d'écrire son code, il peut compiler son code et voir le résultat / les résultats dans la fenêtre de sortie.
* Ils verront soit un succès soit un échec pour leurs extraits de code. Tout est visible dans la fenêtre de sortie du code.
* L'utilisateur peut ajouter des entrées personnalisées à ses extraits de code, et le juge (notre compilateur en ligne) prendra en compte l'entrée personnalisée que l'utilisateur fournit.
* L'utilisateur peut voir les détails pertinents du code qui a été exécuté (Exemple : Il a fallu 5ms pour compiler et exécuter le code, 2024 ko de mémoire ont été utilisés, et le statut d'exécution était un succès).

Maintenant que nous sommes un peu plus familiers avec la structure des dossiers et le flux de l'application, plongeons dans le code et comprenons comment tout fonctionne.

## Comment créer le composant Code Editor

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-18-at-9.26.48-PM.png)

Le composant de l'éditeur de code est principalement constitué de Monaco Editor, qui est un package NPM que nous pouvons utiliser et personnaliser.

```javascript
// CodeEditorWindow.js

import React, { useState } from "react";

import Editor from "@monaco-editor/react";

const CodeEditorWindow = ({ onChange, language, code, theme }) => {
  const [value, setValue] = useState(code || "");

  const handleEditorChange = (value) => {
    setValue(value);
    onChange("code", value);
  };

  return (
    <div className="overlay rounded-md overflow-hidden w-full h-full shadow-4xl">
      <Editor
        height="85vh"
        width={`100%`}
        language={language || "javascript"}
        value={value}
        theme={theme}
        defaultValue="// some comment"
        onChange={handleEditorChange}
      />
    </div>
  );
};
export default CodeEditorWindow;

```

Le composant `Editor` provient du package `@monaco-editor/react` qui nous permet de lancer un éditeur de code avec une hauteur de `85vh` comme spécifié. 

Le composant `Editor` prend un ensemble de props :

*  `language` : Le langage pour lequel nous avons besoin de la coloration syntaxique et de l'intellisense.
* `theme` : Les couleurs et l'arrière-plan de l'extrait de code (nous allons le configurer dans la partie suivante du tutoriel).
* `value` : La valeur réelle du code qui va dans l'éditeur de code
* `onChange` : Cela est déclenché lorsque la valeur dans l'éditeur de code change. Nous devons sauvegarder la valeur modifiée dans l'état afin de pouvoir, plus tard, appeler l'API `Judge0` pour le compiler.

L'éditeur reçoit les props `onChange`, `language`, `code`, et `theme` de son composant parent, qui est `Landing.js`. Chaque fois que la `value` dans l'éditeur de code change, nous appelons le gestionnaire `onChange` qui est présent dans le composant parent `Landing`.

## Comment créer le composant Landing

Le composant landing se compose principalement de 3 parties :

* La `Barre d'Actions` qui contient les composants déroulants `Langages` et `Thèmes`.
* Le composant `Fenêtre de l'Éditeur de Code`
* Les composants `Sortie et Entrée Personnalisée`

```javascript
// Landing.js

import React, { useEffect, useState } from "react";
import CodeEditorWindow from "./CodeEditorWindow";
import axios from "axios";
import { classnames } from "../utils/general";
import { languageOptions } from "../constants/languageOptions";

import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

import { defineTheme } from "../lib/defineTheme";
import useKeyPress from "../hooks/useKeyPress";
import Footer from "./Footer";
import OutputWindow from "./OutputWindow";
import CustomInput from "./CustomInput";
import OutputDetails from "./OutputDetails";
import ThemeDropdown from "./ThemeDropdown";
import LanguagesDropdown from "./LanguagesDropdown";

const javascriptDefault = `// some comment`;

const Landing = () => {
  const [code, setCode] = useState(javascriptDefault);
  const [customInput, setCustomInput] = useState("");
  const [outputDetails, setOutputDetails] = useState(null);
  const [processing, setProcessing] = useState(null);
  const [theme, setTheme] = useState("cobalt");
  const [language, setLanguage] = useState(languageOptions[0]);

  const enterPress = useKeyPress("Enter");
  const ctrlPress = useKeyPress("Control");

  const onSelectChange = (sl) => {
    console.log("selected Option...", sl);
    setLanguage(sl);
  };

  useEffect(() => {
    if (enterPress && ctrlPress) {
      console.log("enterPress", enterPress);
      console.log("ctrlPress", ctrlPress);
      handleCompile();
    }
  }, [ctrlPress, enterPress]);
  const onChange = (action, data) => {
    switch (action) {
      case "code": {
        setCode(data);
        break;
      }
      default: {
        console.warn("case not handled!", action, data);
      }
    }
  };
  const handleCompile = () => {
    // Nous verrons l'implémentation plus tard dans le code
  };

  const checkStatus = async (token) => {
    // Nous verrons l'implémentation plus tard dans le code
  };

  function handleThemeChange(th) {
    // Nous verrons l'implémentation plus tard dans le code
  }
  useEffect(() => {
    defineTheme("oceanic-next").then((_) =>
      setTheme({ value: "oceanic-next", label: "Oceanic Next" })
    );
  }, []);

  const showSuccessToast = (msg) => {
    toast.success(msg || `Compilé avec succès !`, {
      position: "top-right",
      autoClose: 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  };
  const showErrorToast = (msg) => {
    toast.error(msg || `Quelque chose s'est mal passé ! Veuillez réessayer.`, {
      position: "top-right",
      autoClose: 1000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
    });
  };

  return (
    <>
      <ToastContainer
        position="top-right"
        autoClose={2000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
      />
      <div className="h-4 w-full bg-gradient-to-r from-pink-500 via-red-500 to-yellow-500"></div>
      <div className="flex flex-row">
        <div className="px-4 py-2">
          <LanguagesDropdown onSelectChange={onSelectChange} />
        </div>
        <div className="px-4 py-2">
          <ThemeDropdown handleThemeChange={handleThemeChange} theme={theme} />
        </div>
      </div>
      <div className="flex flex-row space-x-4 items-start px-4 py-4">
        <div className="flex flex-col w-full h-full justify-start items-end">
          <CodeEditorWindow
            code={code}
            onChange={onChange}
            language={language?.value}
            theme={theme.value}
          />
        </div>

        <div className="right-container flex flex-shrink-0 w-[30%] flex-col">
          <OutputWindow outputDetails={outputDetails} />
          <div className="flex flex-col items-end">
            <CustomInput
              customInput={customInput}
              setCustomInput={setCustomInput}
            />
            <button
              onClick={handleCompile}
              disabled={!code}
              className={classnames(
                "mt-4 border-2 border-black z-10 rounded-md shadow-[5px_5px_0px_0px_rgba(0,0,0)] px-4 py-2 hover:shadow transition duration-200 bg-white flex-shrink-0",
                !code ? "opacity-50" : ""
              )}
            >
              {processing ? "Traitement..." : "Compiler et Exécuter"}
            </button>
          </div>
          {outputDetails && <OutputDetails outputDetails={outputDetails} />}
        </div>
      </div>
      <Footer />
    </>
  );
};
export default Landing;

```

Comprenons la structure de base de la page d'accueil plus en détail.

### Composant CodeEditorWindow

Comme nous l'avons vu précédemment, le composant CodeEditorWindow prendra en compte le code (qui change constamment) et une méthode `onChange` qui suivra les changements dans le code.

```javascript
// implémentation de la méthode onChange

 const onChange = (action, data) => {
    switch (action) {
      case "code": {
        setCode(data);
        break;
      }
      default: {
        console.warn("case not handled!", action, data);
      }
    }
  };
```

Nous définissons simplement l'état du `code` et suivons les changements.

Le composant `CodeEditorWindow` prend également en compte la prop `language`, qui est le langage actuellement sélectionné pour lequel nous avons besoin de la coloration syntaxique et de l'intellisense.

J'ai créé un tableau `languageOptions` qui suit les props de langage acceptées par Monaco Editor et gère également la compilation (nous suivons le `languageId` qui est accepté par les API `judge0`).

```javascript
// constants/languageOptions.js

export const languageOptions = [
  {
    id: 63,
    name: "JavaScript (Node.js 12.14.0)",
    label: "JavaScript (Node.js 12.14.0)",
    value: "javascript",
  },
  {
    id: 45,
    name: "Assembly (NASM 2.14.02)",
    label: "Assembly (NASM 2.14.02)",
    value: "assembly",
  },
    ...
    ...
    ...
    ...
    ...
    ...
    
  {
    id: 84,
    name: "Visual Basic.Net (vbnc 0.0.0.5943)",
    label: "Visual Basic.Net (vbnc 0.0.0.5943)",
    value: "vbnet",
  },
];
```

Chaque objet `languageOptions` contient des clés `id`, `name`, `label` et `value`. L'ensemble du tableau `languageOptions` peut être pris et placé à l'intérieur du menu déroulant et fourni comme options. 

Chaque fois que l'état du menu déroulant change, la méthode `onSelectChange` suit l'`id` sélectionné et change l'état de manière appropriée.

### Composant LanguageDropdown 

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-19-at-10.42.43-PM.png)

```javascript
// LanguageDropdown.js

import React from "react";
import Select from "react-select";
import { customStyles } from "../constants/customStyles";
import { languageOptions } from "../constants/languageOptions";

const LanguagesDropdown = ({ onSelectChange }) => {
  return (
    <Select
      placeholder={`Filtrer par catégorie`}
      options={languageOptions}
      styles={customStyles}
      defaultValue={languageOptions[0]}
      onChange={(selectedOption) => onSelectChange(selectedOption)}
    />
  );
};

export default LanguagesDropdown;


```

Pour le menu déroulant, nous allons utiliser le package [react-select](https://react-select.com) qui gère les menus déroulants et leurs gestionnaires de changement.

React select prend `defaultValue` et `options` comme paramètres principaux. `options` est un tableau (et nous allons passer `languageOptions` ici) qui affiche automatiquement toutes les valeurs de menu déroulant pertinentes.

La prop `defaultValue` est la valeur par défaut fournie au composant. Nous allons garder JavaScript comme langage par défaut (qui est le premier dans notre tableau de langages).

Chaque fois que l'utilisateur change le langage, nous changeons le langage avec le callback `onSelectChange` :

```javascript
const onSelectChange = (sl) => {
    setLanguage(sl);
};
```

### Composant ThemeDropdown

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-19-at-10.42.43-PM-1.png)

Le composant `ThemeDropdown` est en fait très similaire au composant `LanguageDropdown` (avec l'interface utilisateur et le package react-select).

```javascript
// ThemeDropdown.js

import React from "react";
import Select from "react-select";
import monacoThemes from "monaco-themes/themes/themelist";
import { customStyles } from "../constants/customStyles";

const ThemeDropdown = ({ handleThemeChange, theme }) => {
  return (
    <Select
      placeholder={`Sélectionner un thème`}
      // options={languageOptions}
      options={Object.entries(monacoThemes).map(([themeId, themeName]) => ({
        label: themeName,
        value: themeId,
        key: themeId,
      }))}
      value={theme}
      styles={customStyles}
      onChange={handleThemeChange}
    />
  );
};

export default ThemeDropdown;

```

Ici, nous allons utiliser le package `monacoThemes` pour nous aider avec les différents beaux thèmes disponibles sur Internet pour Monaco Editor.

Nous avons une liste de thèmes disponibles à notre disposition.

```javascript
// lib/defineTheme.js

import { loader } from "@monaco-editor/react";

const monacoThemes = {
  active4d: "Active4D",
  "all-hallows-eve": "All Hallows Eve",
  amy: "Amy",
  "birds-of-paradise": "Birds of Paradise",
  blackboard: "Blackboard",
  "brilliance-black": "Brilliance Black",
  "brilliance-dull": "Brilliance Dull",
  "chrome-devtools": "Chrome DevTools",
  "clouds-midnight": "Clouds Midnight",
  clouds: "Clouds",
  cobalt: "Cobalt",
  dawn: "Dawn",
  dreamweaver: "Dreamweaver",
  eiffel: "Eiffel",
  "espresso-libre": "Espresso Libre",
  github: "GitHub",
  idle: "IDLE",
  katzenmilch: "Katzenmilch",
  "kuroir-theme": "Kuroir Theme",
  lazy: "LAZY",
  "magicwb--amiga-": "MagicWB (Amiga)",
  "merbivore-soft": "Merbivore Soft",
  merbivore: "Merbivore",
  "monokai-bright": "Monokai Bright",
  monokai: "Monokai",
  "night-owl": "Night Owl",
  "oceanic-next": "Oceanic Next",
  "pastels-on-dark": "Pastels on Dark",
  "slush-and-poppies": "Slush and Poppies",
  "solarized-dark": "Solarized-dark",
  "solarized-light": "Solarized-light",
  spacecadet: "SpaceCadet",
  sunburst: "Sunburst",
  "textmate--mac-classic-": "Textmate (Mac Classic)",
  "tomorrow-night-blue": "Tomorrow-Night-Blue",
  "tomorrow-night-bright": "Tomorrow-Night-Bright",
  "tomorrow-night-eighties": "Tomorrow-Night-Eighties",
  "tomorrow-night": "Tomorrow-Night",
  tomorrow: "Tomorrow",
  twilight: "Twilight",
  "upstream-sunburst": "Upstream Sunburst",
  "vibrant-ink": "Vibrant Ink",
  "xcode-default": "Xcode_default",
  zenburnesque: "Zenburnesque",
  iplastic: "iPlastic",
  idlefingers: "idleFingers",
  krtheme: "krTheme",
  monoindustrial: "monoindustrial",
};

const defineTheme = (theme) => {
  return new Promise((res) => {
    Promise.all([
      loader.init(),
      import(`monaco-themes/themes/${monacoThemes[theme]}.json`),
    ]).then(([monaco, themeData]) => {
      monaco.editor.defineTheme(theme, themeData);
      res();
    });
  });
};

export { defineTheme };
```

Le package `monaco-themes` nous fournit un ensemble de thèmes que nous pouvons utiliser pour définir l'apparence de notre éditeur de code.

La fonction `defineTheme` gère les différents thèmes que l'utilisateur pourrait sélectionner. La fonction `defineTheme` retourne une promesse qui définit réellement le thème de l'éditeur Monaco en utilisant l'action `monaco.editor.defineTheme(theme, themeData)`. Cette ligne de code est responsable du changement réel des thèmes à l'intérieur d'une fenêtre de code Monaco Editor.

La fonction `defineTheme` est appelée à l'aide du callback `onChange` que nous avons vu précédemment dans le composant `ThemeDropdown.js`.

```javascript
// Landing.js - fonction handleThemeChange()

function handleThemeChange(th) {
    const theme = th;
    console.log("theme...", theme);

    if (["light", "vs-dark"].includes(theme.value)) {
      setTheme(theme);
    } else {
      defineTheme(theme.value).then((_) => setTheme(theme));
    }
  }
  
```

La fonction `handleThemeChange()` vérifie si le thème est `light` ou `dark`. Ces thèmes sont par défaut disponibles sur le composant `MonacoEditor` et nous n'avons pas besoin d'appeler la méthode `defineTheme()` pour cela.

Sinon, nous appelons simplement le composant `defineTheme()` et définissons l'état du thème sélectionné.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-19-at-10.46.34-PM.png)

## Comment Compiler le Code avec Judge0

Passons à la partie principale de l'application – c'est-à-dire compiler le code avec différents langages.   
  
Pour compiler notre code, nous allons utiliser Judge0. Judge0 est un système d'exécution de code simple et open-source avec lequel nous pouvons interagir. 

Nous pouvons faire un simple appel API avec certains paramètres (code source, ID du langage) et obtenir la sortie en réponse.   
  
Configurons Judge0 et passons aux étapes suivantes :

* Rendez-vous sur [Judge0](https://judge0.com) et choisissez le Plan de Base
* Judge0 est en fait hébergé sur [RapidAPI](https://rapidapi.com). Allez-y et abonnez-vous au plan de base.
* Une fois abonné, vous pouvez copier le `RAPIDAPI_HOST` et le `RAPIDAPI_KEY` qui sont nécessaires pour faire les appels API à notre système d'exécution de code.

Le tableau de bord ressemble à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Untitled-design.png)

Les paramètres `X-RapidAPI-Host` et `X-RapidAPI-Key` seront nécessaires pour nos appels API. Enregistrez-les pour une utilisation future dans les fichiers `.env` comme suit :

```env
REACT_APP_RAPID_API_HOST = VOTRE_URL_D_HOTE
REACT_APP_RAPID_API_KEY = VOTRE_CLE_SECRETE
REACT_APP_RAPID_API_URL = VOTRE_URL_DE_SOUMISSIONS
```

Il est important dans React que nous initialisions nos variables d'environnement avec le préfixe `REACT_APP`.

L'`URL_DE_SOUMISSIONS` est l'URL que nous allons utiliser. Elle consiste essentiellement en votre `hôte`, suivi de la route `/submission`.  
  
Par exemple : `https://judge0-ce.p.rapidapi.com/submissions` sera l'URL de `soumissions` dans notre cas.

Une fois que nous avons les variables correctement configurées, nous pouvons passer à la logique de `compilation`.

#### Flux et Logique de Compilation

Le flux de compilation est le suivant :

* Lorsque le bouton `Compiler et Exécuter` est cliqué, une méthode `handleCompile()` est appelée.
* La fonction `handleCompile()` appelle notre backend `Judge0 RapidAPI` sur l'URL `submissions` avec `languageId`, `source_code` et `stdin` (customInput dans notre cas) comme paramètres du corps.
* Les `options` prennent également en compte l'`hôte` et le `secret` comme en-têtes.
* `base64_encoded` et `fields` sont des paramètres optionnels qui peuvent être passés.
* La requête POST `submission` enregistre notre demande sur le serveur et crée un processus. La réponse de la requête `post` est un `token` qui peut être utilisé pour vérifier le statut de notre exécution. (Il existe divers statuts – Traitement, Accepté, Temps Limite Expiré, Exceptions d'Exécution et plus.)
* Une fois nos résultats retournés, nous pouvons vérifier de manière conditionnelle si les résultats sont un succès ou un échec et afficher les résultats sur nos écrans de sortie.

Passons au code et comprenons la méthode `handleCompile()`.

```javascript
const handleCompile = () => {
    setProcessing(true);
    const formData = {
      language_id: language.id,
      // encoder le code source en base64
      source_code: btoa(code),
      stdin: btoa(customInput),
    };
    const options = {
      method: "POST",
      url: process.env.REACT_APP_RAPID_API_URL,
      params: { base64_encoded: "true", fields: "*" },
      headers: {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Host": process.env.REACT_APP_RAPID_API_HOST,
        "X-RapidAPI-Key": process.env.REACT_APP_RAPID_API_KEY,
      },
      data: formData,
    };

    axios
      .request(options)
      .then(function (response) {
        console.log("res.data", response.data);
        const token = response.data.token;
        checkStatus(token);
      })
      .catch((err) => {
        let error = err.response ? err.response.data : err;
        setProcessing(false);
        console.log(error);
      });
  };
```

Comme on peut le voir ci-dessus, la méthode `handleCompile()` prend `languageId`, `source_code` et `stdin`. Notez le `btoa` avant `source_code` et `stdin`. Cela permet d'encoder nos chaînes en base64 puisque nous utilisons `base64_encoded: true` dans nos paramètres pour l'API.

Lorsqu'il y a une réponse réussie et que nous avons un `token`, nous appelons la méthode `checkStatus()` pour interroger la route `/submissions/${token}`.

```javascript
const checkStatus = async (token) => {
    const options = {
      method: "GET",
      url: process.env.REACT_APP_RAPID_API_URL + "/" + token,
      params: { base64_encoded: "true", fields: "*" },
      headers: {
        "X-RapidAPI-Host": process.env.REACT_APP_RAPID_API_HOST,
        "X-RapidAPI-Key": process.env.REACT_APP_RAPID_API_KEY,
      },
    };
    try {
      let response = await axios.request(options);
      let statusId = response.data.status?.id;

      // Processed - we have a result
      if (statusId === 1 || statusId === 2) {
        // still processing
        setTimeout(() => {
          checkStatus(token)
        }, 2000)
        return
      } else {
        setProcessing(false)
        setOutputDetails(response.data)
        showSuccessToast(`Compilé avec succès !`)
        console.log('response.data', response.data)
        return
      }
    } catch (err) {
      console.log("err", err);
      setProcessing(false);
      showErrorToast();
    }
  };
```

Pour obtenir les résultats de notre code que nous avons soumis précédemment, nous devons interroger l'API `submissions` avec un `token` que nous avons reçu en réponse.

Comme montré ci-dessus, nous allons faire une requête GET à l'endpoint. Une fois que nous avons une réponse, nous vérifions si `statusId === 1 || statusId === 2`. Mais que signifie-t-il ?  
  
Nous avons un total de `14` statuts associés à tout morceau de code que nous soumettons à l'API, et ceux-ci sont :

```javascript
export const statuses = [
  {
    id: 1,
    description: "In Queue",
  },
  {
    id: 2,
    description: "Processing",
  },
  {
    id: 3,
    description: "Accepted",
  },
  {
    id: 4,
    description: "Wrong Answer",
  },
  {
    id: 5,
    description: "Time Limit Exceeded",
  },
  {
    id: 6,
    description: "Compilation Error",
  },
  {
    id: 7,
    description: "Runtime Error (SIGSEGV)",
  },
  {
    id: 8,
    description: "Runtime Error (SIGXFSZ)",
  },
  {
    id: 9,
    description: "Runtime Error (SIGFPE)",
  },
  {
    id: 10,
    description: "Runtime Error (SIGABRT)",
  },
  {
    id: 11,
    description: "Runtime Error (NZEC)",
  },
  {
    id: 12,
    description: "Runtime Error (Other)",
  },
  {
    id: 13,
    description: "Internal Error",
  },
  {
    id: 14,
    description: "Exec Format Error",
  },
];

```

Donc, si `statusId ===1` OU `statusId ===2`, cela signifie que notre code est toujours en cours de traitement et que nous devons appeler à nouveau l'API pour vérifier si nous obtenons des résultats ou non.  
  
Pour cette raison, nous avons un `setTimeout()` dans la condition `if` qui appelle à nouveau la fonction `checkStatus()`, qui appelle à son tour l'API et vérifie le statut.  
  
Si le statut est autre que `2` ou `3`, cela signifie que l'exécution de notre code est terminée et que nous avons un résultat. Soit il s'agit d'un code `compilé avec succès`, soit il s'agit d'un code `Temps Limite Expiré`, ou peut-être d'une `Exception d'Exécution`. Le `statusId` représente chaque scénario et nous pouvons les reproduire également.  
  
Par exemple, `while(true)` nous donnera une erreur de `dépassement de temps` :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-20-at-1.33.08-AM.png)

Ou si nous faisons une erreur de syntaxe, nous obtiendrons une erreur de compilation :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-20-at-1.34.42-AM.png)

Quoi qu'il en soit, nous allons obtenir un résultat. Et nous allons stocker ce résultat dans l'état `outputDetails`. Cela permet de s'assurer que nous avons quelque chose à afficher dans la partie droite de l'écran (qui est la Fenêtre de Sortie).

### Composant Fenêtre de Sortie

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-20-at-1.37.39-AM.png)

```javascript
import React from "react";

const OutputWindow = ({ outputDetails }) => {
  const getOutput = () => {
    let statusId = outputDetails?.status?.id;

    if (statusId === 6) {
      // compilation error
      return (
        <pre className="px-2 py-1 font-normal text-xs text-red-500">
          {atob(outputDetails?.compile_output)}
        </pre>
      );
    } else if (statusId === 3) {
      return (
        <pre className="px-2 py-1 font-normal text-xs text-green-500">
          {atob(outputDetails.stdout) !== null
            ? `${atob(outputDetails.stdout)}`
            : null}
        </pre>
      );
    } else if (statusId === 5) {
      return (
        <pre className="px-2 py-1 font-normal text-xs text-red-500">
          {`Temps Limite Expiré`}
        </pre>
      );
    } else {
      return (
        <pre className="px-2 py-1 font-normal text-xs text-red-500">
          {atob(outputDetails?.stderr)}
        </pre>
      );
    }
  };
  return (
    <>
      <h1 className="font-bold text-xl bg-clip-text text-transparent bg-gradient-to-r from-slate-900 to-slate-700 mb-2">
        Sortie
      </h1>
      <div className="w-full h-56 bg-[#1e293b] rounded-md text-white font-normal text-sm overflow-y-auto">
        {outputDetails ? <>{getOutput()}</> : null}
      </div>
    </>
  );
};

export default OutputWindow;

```

Il s'agit d'un composant simple qui n'affiche que les scénarios de succès ou d'échec appropriés.

La méthode `getOutput()` détermine à quoi ressemblera la couleur du texte et ce qui doit être imprimé.

* Si `statusId` est `6` – Nous avons une erreur de compilation. Pour cela, l'API retourne `compile_output` qui peut être utilisé pour afficher l'erreur.
* Si `statusId` est `3` – Nous avons un scénario de succès, qui est `Accepté`. L'API retourne un `stdout` qui signifie Sortie Standard. Cela est utilisé pour afficher les données qui sont retournées par le code que nous avons fourni à l'API.
* Si `statusId` est `5` – Nous avons une erreur de Temps Limite Expiré. Nous affichons simplement qu'il y a une condition de boucle infinie dans le code OU qu'il dépasse le temps standard de `5` secondes pour l'exécution du code.
* Pour tout autre statut, nous allons obtenir un objet `stderr` standard que nous pouvons utiliser pour afficher les erreurs.
* Remarquez la méthode `atob()` utilisée. Cela est dû au fait que nous obtenons la sortie sous forme de chaîne base64. Pour la décoder, nous utilisons la méthode `atob()`.

Voici un scénario de succès d'un programme de `Recherche Binaire` en JavaScript :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-20-at-1.42.55-AM.png)

### Composant Détails de Sortie

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-20-at-1.44.01-AM.png)

Le composant `OutputDetails` est un simple mapper pour afficher les détails associés à un extrait de code que nous avons initialement compilé. Les données sont déjà définies dans la variable d'état `outputDetails`.

```javascript
import React from "react";

const OutputDetails = ({ outputDetails }) => {
  return (
    <div className="metrics-container mt-4 flex flex-col space-y-3">
      <p className="text-sm">
        Statut :{" "}
        <span className="font-semibold px-2 py-1 rounded-md bg-gray-100">
          {outputDetails?.status?.description}
        </span>
      </p>
      <p className="text-sm">
        Mémoire :{" "}
        <span className="font-semibold px-2 py-1 rounded-md bg-gray-100">
          {outputDetails?.memory}
        </span>
      </p>
      <p className="text-sm">
        Temps :{" "}
        <span className="font-semibold px-2 py-1 rounded-md bg-gray-100">
          {outputDetails?.time}
        </span>
      </p>
    </div>
  );
};

export default OutputDetails;

```

Le `time`, `memory` et `status.description` sont tous reçus de la réponse de l'API qui sont ensuite stockés dans `outputDetails` et affichés.

### Événements Clavier

La dernière chose dans l'application est l'utilisation de `ctrl+enter` pour compiler notre code. Pour cela, nous allons créer un hook personnalisé (parce qu'ils sont géniaux et beaucoup plus propres) pour écouter divers événements clavier sur notre application web.

```javascript
// useKeyPress.js

import React, { useState } from "react";

const useKeyPress = function (targetKey) {
  const [keyPressed, setKeyPressed] = useState(false);

  function downHandler({ key }) {
    if (key === targetKey) {
      setKeyPressed(true);
    }
  }

  const upHandler = ({ key }) => {
    if (key === targetKey) {
      setKeyPressed(false);
    }
  };

  React.useEffect(() => {
    document.addEventListener("keydown", downHandler);
    document.addEventListener("keyup", upHandler);

    return () => {
      document.removeEventListener("keydown", downHandler);
      document.removeEventListener("keyup", upHandler);
    };
  });

  return keyPressed;
};

export default useKeyPress;

```

```javascript
// Landing.js

...
...
...
const Landing = () => {
    ...
    ...
      const enterPress = useKeyPress("Enter");
      const ctrlPress = useKeyPress("Control");
   ...
   ...
}

```

Ici, nous utilisons les `Event Listeners` natifs de JavaScript pour écouter notre `target` key que nous allons utiliser.

Le `Hook` écoute les événements `keydown` et `keyup`. Nous initialisons notre hook avec une touche cible de `Enter` et `Control`.  
  
Puisque nous vérifions si `targetKey === key` et définissons `keyPressed` en conséquence, nous pouvons utiliser le booléen `keyPressed` retourné, qui sera soit `true` soit `false`.  
  
Maintenant, nous pouvons écouter ces événements dans le hook `useEffect` pour nous assurer que les deux ont été pressés en même temps :

```javascript
useEffect(() => {
    if (enterPress && ctrlPress) {
      console.log("enterPress", enterPress);
      console.log("ctrlPress", ctrlPress);
      handleCompile();
    }
  }, [ctrlPress, enterPress]);
```

Ainsi, chaque fois que l'utilisateur appuie sur `control` et `enter` l'un après l'autre OU en même temps, la méthode `handleCompile()` sera appelée. 

## Quelques points à garder à l'esprit

Ce projet était amusant à réaliser. Mais le plan de base de Judge0 a certaines limitations, à savoir 100 requêtes/jour. 

Pour contourner cela, vous pourriez lancer votre propre serveur / droplet (sur Digital Ocean) et auto-héberger le projet open-source (ils ont une excellente documentation pour cela).

## Conclusion 

En fin de compte, nous avons :

* Un éditeur de code qui peut compiler dans 40+ langages
* Un sélecteur de thème pour changer l'apparence de notre éditeur de code
* Interagir et héberger des API sur RapidAPI
* Utiliser des événements clavier dans React en utilisant des hooks personnalisés
* Beaucoup de plaisir ! ;)

En fin de compte, si vous souhaitez approfondir le projet, voici quelques fonctionnalités que vous pourriez envisager d'implémenter :

* Module de connexion et d'inscription – afin que vous puissiez sauvegarder votre code dans votre propre tableau de bord personnel.
* Un moyen de partager du code avec d'autres personnes sur Internet
* Page de profil et personnalisations.
* Programmation en paire sur un seul extrait de code en utilisant la programmation Socket et les Transformations Opérationnelles.
* Marquer les extraits de code préférés
* Tableau de bord personnalisé de vos extraits de code (qui sont sauvegardés) - comme CodePen.

J'ai vraiment aimé coder cette application à partir de zéro, et TailwindCSS est ma ressource préférée et incontournable pour styliser mes applications. 

Si cet article vous a été utile, laissez un ⭐️ sur le [Dépôt GitHub](https://github.com/manuarora700/react-code-editor).   
Si vous avez des questions, n'hésitez pas à me contacter sur mon [Twitter](https://twitter.com/mannupaaji) et/ou [Site Web](https://manuarora.in) et je serais ravi de vous aider.

[Code Source](https://github.com/manuarora700/react-code-editor) | [Démonstration en Direct](https://coderush.vercel.app)