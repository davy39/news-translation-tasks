---
title: Comment créer un site portfolio avec React
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-06-21T18:15:53.000Z'
originalURL: https://freecodecamp.org/news/build-portfolio-website-react
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/react-portfolio-2021.png
tags:
- name: Netlify
  slug: netlify
- name: portfolio
  slug: portfolio
- name: React
  slug: react
- name: tailwind
  slug: tailwind
- name: Web Development
  slug: web-development
seo_title: Comment créer un site portfolio avec React
seo_desc: 'Today you''re going to create one of the most important apps you can build
  for yourself: your developer portfolio.

  Every React developer or web developer in general needs to be able to show off what
  they can do to any potential client or employer.

  Tha...'
---

Aujourd'hui, vous allez créer l'une des applications les plus importantes que vous puissiez construire pour vous-même : votre portfolio de développeur.

Chaque développeur React ou développeur web en général doit être capable de montrer ce qu'il peut faire à tout client ou employeur potentiel.

C'est exactement ce que nous allons construire maintenant, avec l'aide de plusieurs outils standards de l'industrie, dont React, Tailwind CSS et Netlify.

Commençons !

## À quoi ressemblera le portfolio ?

![Image](https://www.freecodecamp.org/news/content/images/2021/06/portfolio-1-min.gif)

Voici la version finale du portfolio que vous allez construire.

Il présentera des informations sur vous, les projets que vous avez réalisés, les compétences que vous avez utilisées pour réaliser ces projets, et inclura un formulaire de contact pour que les clients ou employeurs puissent vous contacter.

## Quels outils allons-nous utiliser ?

* Nous utiliserons React pour créer l'interface utilisateur de l'application. Cela nous permettra de composer chaque partie de notre page d'accueil à travers des composants réutilisables et d'étendre notre application si nous voulons ajouter des fonctionnalités supplémentaires, comme un blog.
* Pour styliser notre application, nous utiliserons Tailwind CSS. Pour donner à notre application une apparence professionnelle, Tailwind nous permettra d'appliquer facilement plusieurs styles en combinant des noms de classes sur nos éléments React.
* Pour publier notre application sur le web, nous utiliserons le service gratuit Netlify. Il servira notre projet sur un domaine personnalisé aux utilisateurs très rapidement avec l'aide d'un CDN (réseau de diffusion de contenu).

## Comment commencer

**[Vous pouvez télécharger les fichiers de départ pour notre projet ici](https://reedbarger.com/resources/react-portfolio).**

Lorsque vous récupérez le code, tout ce que vous avez à faire est de glisser votre dossier de projet (décompressé) dans votre éditeur de code et d'exécuter la commande :

```bash
npm install
```

Et vous êtes prêt à partir !

## Quels outils ai-je besoin pour construire mon portfolio ?

Pour passer par tout le processus de création de notre application, du début au déploiement, vous devrez avoir les éléments suivants :

1. Node.js installé sur votre ordinateur. Vous pouvez le télécharger sur nodejs.org.
2. Git installé sur votre ordinateur. Vous pouvez le télécharger sur git-scm.com.
3. Je recommanderais d'utiliser VS Code comme éditeur de code. Vous pouvez le télécharger sur code.visualstudio.com.
4. Un compte Netlify gratuit sur netlify.com.
5. Un compte GitHub gratuit sur github.com.

## Comment construire la structure du portfolio

L'avantage d'utiliser React est que nous pourrions étendre notre application à autant de pages que nous le souhaitons, très simplement, et ajouter beaucoup de contenu supplémentaire.

Cependant, puisque nous travaillons avec une seule page, nous pouvons déterminer très rapidement les différents composants dont nous avons besoin dans notre composant d'application. Nous aurons une barre de navigation en haut avec tous les liens pour sauter vers différentes sections de notre portfolio.

Après cela, nous inclurons une section à propos, une section pour nos projets, des témoignages, et enfin notre formulaire de contact.

Cette planification rapide nous permet de déterminer comment nos composants doivent être nommés et dans quel ordre. Nous pouvons ajouter tous les composants à notre fichier App.js (dans src) :

```js
// src/App.js

import React from "react";

export default function App() {
  return (
    <main>
      <Navbar />
      <About />
      <Projects />
      <Skills />
      <Testimonials />
      <Contact />
    </main>
  );
}
```

## Comment créer nos composants

Maintenant que nous avons tous ces composants listés, nous devons les créer.

Dans notre dossier source (src), nous allons créer un dossier appelé components avec tous les fichiers dont nous avons besoin :

```
my-portfolio
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.js
    ├── data.js
    ├── index.css
    ├── index.js
    └── components
        ├── About.js
        ├── Contact.js
        ├── Navbar.js
        ├── Projects.js
        ├── Skills.js
        └── Testimonials.js
```

Ensuite, nous allons créer la structure de base de chaque composant React et l'exporter depuis ce fichier avec `export default` :

```js
// src/components/About.js

export default function About() {}

// répétez la même structure de base pour tous les 6 composants
```

Et enfin, assurez-vous de l'importer à nouveau dans App.js :

```js
// src/App.js

import React from "react";
import About from "./components/About";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Projects from "./components/Projects";
import Skills from "./components/Skills";
import Testimonials from "./components/Testimonials";

export default function App() {
  return (
    <main>
      <Navbar />
      <About />
      <Projects />
      <Skills />
      <Testimonials />
      <Contact />
    </main>
  );
}
```

_Notez qu'il devrait y avoir six composants au total._

## Introduction à Tailwind CSS

Une fois cela fait, nous pouvons commencer à travailler avec Tailwind CSS, afin de commencer à donner à notre application une apparence de base.

L'avantage d'utiliser Tailwind CSS est que nous n'avons pas à écrire de styles manuellement dans une feuille de style CSS. Tout ce que nous avons à faire est de combiner plusieurs classes pour créer l'apparence que nous voulons.

Par exemple, pour donner à notre portfolio un fond sombre avec du texte gris appliqué à tous nos composants enfants, vous pouvez ajouter les classes suivantes à notre élément `main` :

```js
// src/App.js

import React from "react";
import About from "./components/About";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Projects from "./components/Projects";
import Skills from "./components/Skills";
import Testimonials from "./components/Testimonials";

export default function App() {
  return (
    <main className="text-gray-400 bg-gray-900 body-font">
      <Navbar />
      <About />
      <Projects />
      <Skills />
      <Testimonials />
      <Contact />
    </main>
  );
}
```

## Comment construire le composant About

Commençons par notre première section, la section à propos. Cela consistera en une introduction de base à nous-mêmes et aux compétences que nous spécialisons.

Cela inclura également quelques liens vers le formulaire de contact ainsi que nos projets passés. Puisque ces liens seront vers différentes parties de la même page, nous pouvons utiliser les hachages : "/#projects" et "/#contact".

Pour que ces liens fonctionnent et puissent sauter vers chaque section, nous définirons l'attribut `id` de la section des projets sur "projects" et celui de la section de contact sur "contact".

```js
// src/components/About.js

import React from "react";

export default function About() {
  return (
    <section id="about">
      <div className="container mx-auto flex px-10 py-20 md:flex-row flex-col items-center">
        <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
          <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-white">
            Salut, je suis Reed.
            <br className="hidden lg:inline-block" />J'adore construire des
            applications incroyables.
          </h1>
          <p className="mb-8 leading-relaxed">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Qui
            laborum quasi, incidunt dolore iste nostrum cupiditate voluptas?
            Laborum, voluptas natus?
          </p>
          <div className="flex justify-center">
            <a
              href="#contact"
              className="inline-flex text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-600 rounded text-lg">
              Travailler avec moi
            </a>
            <a
              href="#projects"
              className="ml-4 inline-flex text-gray-400 bg-gray-800 border-0 py-2 px-6 focus:outline-none hover:bg-gray-700 hover:text-white rounded text-lg">
              Voir mes travaux passés
            </a>
          </div>
        </div>
        <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
          <img
            className="object-cover object-center rounded"
            alt="hero"
            src="./coding.svg"
          />
        </div>
      </div>
    </section>
  );
}
```

Pour l'image du côté droit de la section, j'utilise un fichier svg du dossier `public`, coding.svg.

Cette image sert simplement de remplissage temporaire. Je recommande fortement d'utiliser une image réelle de vous-même.

## Comment construire le composant Projects

Notre section de projets consistera en un élément `section` avec un `id` de "projects". Cela présentera une galerie de tous les projets que nous avons construits, qui inclura des images.

Il aura le titre du projet, ainsi que les technologies que nous utilisons pour le réaliser, et un lien vers celui-ci (s'il est déployé).

```js
// src/components/Projects.js

import { CodeIcon } from "@heroicons/react/solid";
import React from "react";
import { projects } from "../data";

export default function Projects() {
  return (
    <section id="projects" className="text-gray-400 bg-gray-900 body-font">
      <div className="container px-5 py-10 mx-auto text-center lg:px-40">
        <div className="flex flex-col w-full mb-20">
          <CodeIcon className="mx-auto inline-block w-10 mb-4" />
          <h1 className="sm:text-4xl text-3xl font-medium title-font mb-4 text-white">
            Applications que j'ai construites
          </h1>
          <p className="lg:w-2/3 mx-auto leading-relaxed text-base">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo
            facilis repellat ab cupiditate alias vero aliquid obcaecati quisquam
            fuga dolore.
          </p>
        </div>
        <div className="flex flex-wrap -m-4">
          {projects.map((project) => (
            <a
              href={project.link}
              key={project.image}
              className="sm:w-1/2 w-100 p-4">
              <div className="flex relative">
                <img
                  alt="gallery"
                  className="absolute inset-0 w-full h-full object-cover object-center"
                  src={project.image}
                />
                <div className="px-8 py-10 relative z-10 w-full border-4 border-gray-800 bg-gray-900 opacity-0 hover:opacity-100">
                  <h2 className="tracking-widest text-sm title-font font-medium text-green-400 mb-1">
                    {project.subtitle}
                  </h2>
                  <h1 className="title-font text-lg font-medium text-white mb-3">
                    {project.title}
                  </h1>
                  <p className="leading-relaxed">{project.description}</p>
                </div>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
```

Notez que nous allons également utiliser la bibliothèque `@heroicons/react` afin de pouvoir écrire quelques icônes SVG en tant que composants React.

Nous importons un tableau de projets depuis un fichier data.js dans le même dossier. Là, nous exportons un tableau d'objets qui incluent chacun les données d'un projet individuel :

```js
// src/data.js

export const projects = [
  {
    title: "React Reserve",
    subtitle: "MERN Stack",
    description:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolore rerum laborum iure enim sint nemo omnis voluptate exercitationem eius?",
    image: "./project-1.gif",
    link: "https://reactbootcamp.com",
  },
  {
    title: "React Tracks",
    subtitle: "React et Python",
    description:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolore rerum laborum iure enim sint nemo omnis voluptate exercitationem eius?",
    image: "./project-2.gif",
    link: "https://reedbarger.com",
  },
  {
    title: "DevChat",
    subtitle: "React et Firebase",
    description:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolore rerum laborum iure enim sint nemo omnis voluptate exercitationem eius?",
    image: "./project-3.gif",
    link: "https://jsbootcamp.com",
  },
  {
    title: "Epic Todo App",
    subtitle: "React Hooks",
    description:
      "Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium dolore rerum laborum iure enim sint nemo omnis voluptate exercitationem eius?",
    image: "./project-4.gif",
    link: "https://pythonbootcamp.com",
  },
];
```

## Comment construire le composant Skills

Remplissons la section pour toutes les compétences et technologies que nous connaissons.

Cela consistera en une simple liste de tous les outils majeurs que nous connaissons et pouvons utiliser dans les projets de nos employeurs ou clients.

Une fois de plus, nous allons importer un tableau depuis notre dossier de données. Mais ce tableau se compose d'un certain nombre de chaînes qui représentent chacune des compétences que nous connaissons, comme JavaScript, React et Node :

```js
// src/components/Skills.js

import { BadgeCheckIcon, ChipIcon } from "@heroicons/react/solid";
import React from "react";
import { skills } from "../data";

export default function Skills() {
  return (
    <section id="skills">
      <div className="container px-5 py-10 mx-auto">
        <div className="text-center mb-20">
          <ChipIcon className="w-10 inline-block mb-4" />
          <h1 className="sm:text-4xl text-3xl font-medium title-font text-white mb-4">
            Compétences et technologies
          </h1>
          <p className="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Nisi sit
            ipsa delectus eum quo voluptas aspernatur accusantium distinctio
            possimus est.
          </p>
        </div>
        <div className="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-2">
          {skills.map((skill) => (
            <div key={skill} className="p-2 sm:w-1/2 w-full">
              <div className="bg-gray-800 rounded flex p-4 h-full items-center">
                <BadgeCheckIcon className="text-green-400 w-6 h-6 flex-shrink-0 mr-4" />
                <span className="title-font font-medium text-white">
                  {skill}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

## Comment construire le composant Testimonials

Dans le composant Testimonials, nous allons lister quelques témoignages, peut-être de clients passés ou de personnes qui connaissent notre travail.

Ceux-ci consisteront en quelques cartes qui présentent le témoignage lui-même ainsi que la personne qui l'a fait et l'entreprise de cette personne.

Nous importons également un tableau de témoignages avec un certain nombre d'objets qui présentent la citation, l'image, le nom et l'entreprise.

```js
// src/components/Testimonials

import React from "react";
import { TerminalIcon, UsersIcon } from "@heroicons/react/solid";
import { testimonials } from "../data";

export default function Testimonials() {
  return (
    <section id="testimonials">
      <div className="container px-5 py-10 mx-auto text-center">
        <UsersIcon className="w-10 inline-block mb-4" />
        <h1 className="sm:text-4xl text-3xl font-medium title-font text-white mb-12">
          Témoignages de clients
        </h1>
        <div className="flex flex-wrap m-4">
          {testimonials.map((testimonial) => (
            <div className="p-4 md:w-1/2 w-full">
              <div className="h-full bg-gray-800 bg-opacity-40 p-8 rounded">
                <TerminalIcon className="block w-8 text-gray-500 mb-4" />
                <p className="leading-relaxed mb-6">{testimonial.quote}</p>
                <div className="inline-flex items-center">
                  <img
                    alt="testimonial"
                    src={testimonial.image}
                    className="w-12 rounded-full flex-shrink-0 object-cover object-center"
                  />
                  <span className="flex-grow flex flex-col pl-4">
                    <span className="title-font font-medium text-white">
                      {testimonial.name}
                    </span>
                    <span className="text-gray-500 text-sm uppercase">
                      {testimonial.company}
                    </span>
                  </span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
```

## Comment construire le composant Contact

À la fin de notre page d'accueil, nous allons inclure notre formulaire de contact pour permettre aux employeurs potentiels de nous contacter.

Ce formulaire aura 3 champs : un nom, un email et un champ de message.

Pour recevoir ces soumissions de formulaire, nous allons utiliser l'outil Netlify Forms pour gérer très facilement l'enregistrement de ces messages.

```js
// src/components/Contact.js

import React from "react";

export default function Contact() {
  return (
    <section id="contact" className="relative">
      <div className="container px-5 py-10 mx-auto flex sm:flex-nowrap flex-wrap">
        <div className="lg:w-2/3 md:w-1/2 bg-gray-900 rounded-lg overflow-hidden sm:mr-10 p-10 flex items-end justify-start relative">
          <iframe
            width="100%"
            height="100%"
            title="map"
            className="absolute inset-0"
            frameBorder={0}
            marginHeight={0}
            marginWidth={0}
            style={{ filter: "opacity(0.7)" }}
            src="https://www.google.com/maps/embed/v1/place?q=97+warren+st+new+york+city&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8"
          />
          <div className="bg-gray-900 relative flex flex-wrap py-6 rounded shadow-md">
            <div className="lg:w-1/2 px-6">
              <h2 className="title-font font-semibold text-white tracking-widest text-xs">
                ADDRESSE
              </h2>
              <p className="mt-1">
                97 Warren St. <br />
                New York, NY 10007
              </p>
            </div>
            <div className="lg:w-1/2 px-6 mt-4 lg:mt-0">
              <h2 className="title-font font-semibold text-white tracking-widest text-xs">
                EMAIL
              </h2>
              <a className="text-indigo-400 leading-relaxed">
                reedbarger@email.com
              </a>
              <h2 className="title-font font-semibold text-white tracking-widest text-xs mt-4">
                TÉLÉPHONE
              </h2>
              <p className="leading-relaxed">123-456-7890</p>
            </div>
          </div>
        </div>
        <form
          netlify
          name="contact"
          className="lg:w-1/3 md:w-1/2 flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0">
          <h2 className="text-white sm:text-4xl text-3xl mb-1 font-medium title-font">
            Embauchez-moi
          </h2>
          <p className="leading-relaxed mb-5">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum
            suscipit officia aspernatur veritatis. Asperiores, aliquid?
          </p>
          <div className="relative mb-4">
            <label htmlFor="name" className="leading-7 text-sm text-gray-400">
              Nom
            </label>
            <input
              type="text"
              id="name"
              name="name"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>
          <div className="relative mb-4">
            <label htmlFor="email" className="leading-7 text-sm text-gray-400">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            />
          </div>
          <div className="relative mb-4">
            <label
              htmlFor="message"
              className="leading-7 text-sm text-gray-400">
              Message
            </label>
            <textarea
              id="message"
              name="message"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
            />
          </div>
          <button
            type="submit"
            className="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">
            Soumettre
          </button>
        </form>
      </div>
    </section>
  );
}
```

## Comment intégrer un emplacement Google Maps

À gauche du formulaire, nous allons inclure une carte Google Maps intégrée de l'endroit où nous nous trouvons.

Nous pouvons le faire avec l'aide d'un outil en ligne : embed-map.com. Tout ce que vous avez à faire est de simplement entrer votre emplacement et de cliquer sur "Générer le code HTML".

Dans le code qui nous est donné, ne copiez pas tout le code, seulement l'attribut `src` de l'élément iframe. Nous allons remplacer cette valeur par la valeur `src` par défaut que nous avons pour notre iframe.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/portfolio-2.png)

Pour envoyer les données de formulaire soumises à Netlify, Netlify Forms doit reconnaître un formulaire comme étant du HTML statique. Parce que notre application React est contrôlée par JavaScript et ne consiste pas en du HTML simple, nous devons ajouter un formulaire caché à notre fichier index.html dans le dossier public.

```html
<!-- public/index.html -->

<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- contenu de l'en-tête sauté -->
  </head>
  <body>

  <form name="contact" netlify netlify-honeypot="bot-field" hidden>
    <input type="text" name="name" />
    <input type="email" name="email" />
    <textarea name="message"></textarea>
  </form>
  
    <noscript>Vous devez activer JavaScript pour exécuter cette application.</noscript>
    <div id="root"></div>
  </body>
</html>
```

Nous devons cacher ce formulaire, car il n'a pas besoin d'être vu par l'utilisateur, seulement par Netlify.

Nous allons lui donner l'attribut `hidden` ainsi qu'un attribut `name` qui correspond au formulaire JSX dans Contact.js. Nous devons également lui donner l'attribut `netlify` afin que Netlify Forms le reconnaisse. Enfin, nous devons inclure tous les mêmes champs que notre formulaire JSX : pour le nom, l'email et le message.

## Comment soumettre le formulaire de contact

Une fois cela fait, nous allons retourner à Contact.js. Nous allons utiliser JavaScript afin de soumettre ce formulaire.

Tout d'abord, nous allons créer un état dédié pour chacune des valeurs tapées dans le formulaire pour le nom, l'email et le message :

```js
const [name, setName] = React.useState("");
const [email, setEmail] = React.useState("");
const [message, setMessage] = React.useState("");
```

Nous allons stocker ce que l'utilisateur tape dans chacun des champs dans l'état avec l'aide du gestionnaire `onChange`.

Pour gérer la soumission du formulaire, nous allons ajouter la propriété `onSubmit`. La fonction qui sera appelée, `handleSubmit`, fera une requête POST à l'endpoint "/" avec toutes nos données de formulaire.

Nous allons définir les en-têtes de la requête pour indiquer que nous envoyons des données de formulaire. Pour le corps de la requête, nous allons inclure le nom du formulaire ainsi que toutes les données du formulaire des variables d'état `name`, `email` et `message`.

```js
// src/components/Contact.js

import React from "react";

export default function Contact() {
  const [name, setName] = React.useState("");
  const [email, setEmail] = React.useState("");
  const [message, setMessage] = React.useState("");

  function encode(data) {
    return Object.keys(data)
      .map(
        (key) => encodeURIComponent(key) + "=" + encodeURIComponent(data[key])
      )
      .join("&");
  }

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: encode({ "form-name": "contact", name, email, message }),
    })
      .then(() => alert("Message envoyé !"))
      .catch((error) => alert(error));
  }

  return (
    <section id="contact" className="relative">
      <div className="container px-5 py-10 mx-auto flex sm:flex-nowrap flex-wrap">
        <div className="lg:w-2/3 md:w-1/2 bg-gray-900 rounded-lg overflow-hidden sm:mr-10 p-10 flex items-end justify-start relative">
          <iframe
            width="100%"
            height="100%"
            title="map"
            className="absolute inset-0"
            frameBorder={0}
            marginHeight={0}
            marginWidth={0}
            style={{ filter: "opacity(0.7)" }}
            src="https://www.google.com/maps/embed/v1/place?q=97+warren+st+new+york+city&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8"
          />
          <div className="bg-gray-900 relative flex flex-wrap py-6 rounded shadow-md">
            <div className="lg:w-1/2 px-6">
              <h2 className="title-font font-semibold text-white tracking-widest text-xs">
                ADDRESSE
              </h2>
              <p className="mt-1">
                97 Warren St. <br />
                New York, NY 10007
              </p>
            </div>
            <div className="lg:w-1/2 px-6 mt-4 lg:mt-0">
              <h2 className="title-font font-semibold text-white tracking-widest text-xs">
                EMAIL
              </h2>
              <a className="text-indigo-400 leading-relaxed">
                reedbarger@email.com
              </a>
              <h2 className="title-font font-semibold text-white tracking-widest text-xs mt-4">
                TÉLÉPHONE
              </h2>
              <p className="leading-relaxed">123-456-7890</p>
            </div>
          </div>
        </div>
        <form
          netlify
          name="contact"
          onSubmit={handleSubmit}
          className="lg:w-1/3 md:w-1/2 flex flex-col md:ml-auto w-full md:py-8 mt-8 md:mt-0">
          <h2 className="text-white sm:text-4xl text-3xl mb-1 font-medium title-font">
            Embauchez-moi
          </h2>
          <p className="leading-relaxed mb-5">
            Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum
            suscipit officia aspernatur veritatis. Asperiores, aliquid?
          </p>
          <div className="relative mb-4">
            <label htmlFor="name" className="leading-7 text-sm text-gray-400">
              Nom
            </label>
            <input
              type="text"
              id="name"
              name="name"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className="relative mb-4">
            <label htmlFor="email" className="leading-7 text-sm text-gray-400">
              Email
            </label>
            <input
              type="email"
              id="email"
              name="email"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 text-base outline-none text-gray-100 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="relative mb-4">
            <label
              htmlFor="message"
              className="leading-7 text-sm text-gray-400">
              Message
            </label>
            <textarea
              id="message"
              name="message"
              className="w-full bg-gray-800 rounded border border-gray-700 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-900 h-32 text-base outline-none text-gray-100 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
              onChange={(e) => setMessage(e.target.value)}
            />
          </div>
          <button
            type="submit"
            className="text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">
            Soumettre
          </button>
        </form>
      </div>
    </section>
  );
}
```

Comme vous pouvez le voir ci-dessus, nous encodons les données du formulaire avec une fonction spéciale `encode` que vous voyez ici.

Si le message est envoyé correctement, nous afficherons une alerte qui dit "Message envoyé". Sinon, s'il y a une erreur, nous allons alerter l'utilisateur de cette erreur.

## Comment construire le composant Navbar

La dernière étape consiste à construire notre composant Navbar.

Nous voulons que cette barre de navigation reste en haut de notre application sur les grands appareils et ne soit pas fixe sur les appareils mobiles.

De plus, nous voulons inclure des liens vers chacune de nos sections pertinentes pour nos projets, compétences, témoignages et notre formulaire de contact :

```js
// src/components/Navbar.js

import { ArrowRightIcon } from "@heroicons/react/solid";
import React from "react";

export default function Navbar() {
  return (
    <header className="bg-gray-800 md:sticky top-0 z-10">
      <div className="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
        <a className="title-font font-medium text-white mb-4 md:mb-0">
          <a href="#about" className="ml-3 text-xl">
            Reed Barger
          </a>
        </a>
        <nav className="md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-700	flex flex-wrap items-center text-base justify-center">
          <a href="#projects" className="mr-5 hover:text-white">
            Travaux passés
          </a>
          <a href="#skills" className="mr-5 hover:text-white">
            Compétences
          </a>
          <a href="#testimonials" className="mr-5 hover:text-white">
            Témoignages
          </a>
        </nav>
        <a
          href="#contact"
          className="inline-flex items-center bg-gray-800 border-0 py-1 px-3 focus:outline-none hover:bg-gray-700 rounded text-base mt-4 md:mt-0">
          Embauchez-moi
          <ArrowRightIcon className="w-4 h-4 ml-1" />
        </a>
      </div>
    </header>
  );
}
```

Comment cela reste-t-il en haut de la page sur un appareil plus grand ? Avec l'aide de la classe `md:sticky` sur notre élément `header`.

Cette classe signifie qu'elle aura la règle de style `position: sticky;` appliquée à partir d'un point d'arrêt de taille moyenne (768px).

## Comment déployer votre portfolio

Maintenant, pour rendre notre portfolio accessible, nous devons pousser notre application vers GitHub.

Si vous n'êtes pas familier avec Git et GitHub, je vous recommande de prendre un peu de temps pour apprendre à pousser votre code vers votre compte GitHub pour la première fois. C'est une compétence essentielle pour tout développeur.

Une fois que vous êtes familier avec ce processus, nous pouvons d'abord créer un nouveau dépôt GitHub. Après cela, nous allons exécuter `git add .`, `git commit -m "Deploy"`, créer notre dépôt distant git, et `git push -u origin master`.

Une fois notre projet sur GitHub, nous pouvons nous rendre sur Netlify et sélectionner l'option "Choisir un site depuis Git". Ensuite, nous allons choisir GitHub pour notre déploiement continu, et sélectionner le dépôt GitHub vers lequel nous venons de pousser notre code.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/portfolio-3-min.gif)

Après cela, notre projet sera automatiquement déployé sur le web !

## Quelles sont les prochaines étapes

Félicitations ! Vous avez maintenant une application portfolio en ligne sur le web qui montre tous vos projets et compétences aux employeurs potentiels.

La prochaine étape à suivre serait de configurer un domaine personnalisé, de préférence avec votre nom (par exemple, [reedbarger.com](https://reedbarger.com/)). Puisque Netlify inclut un DNS, vous pouvez facilement configurer un domaine personnalisé avec eux.

Envisagez peut-être d'ajouter un blog à votre application React pour montrer encore plus de vos connaissances en développement aux employeurs potentiels.

Faites de votre portfolio personnel une expression de vous-même et de ce qui vous passionne en tant que développeur et vous aurez du succès !

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*