---
title: Tutoriel NextJS et HarperDB – Créez une application Full Stack de minuteur
  de productivité
subtitle: ''
author: Danny
co_authors: []
series: null
date: '2022-04-01T16:25:42.000Z'
originalURL: https://freecodecamp.org/news/nextjs-and-harperdb-tutorial-build-a-full-stack-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/feature.jpg
tags:
- name: full stack
  slug: full-stack
- name: Next.js
  slug: nextjs
seo_title: Tutoriel NextJS et HarperDB – Créez une application Full Stack de minuteur
  de productivité
seo_desc: "Building full stack applications can be tough. You have to think about\
  \ frontend, APIs, databases, authentication - and how all of these things work together.\
  \ \nSo, in this article, I'll show you how to do all of those things using NextJS\
  \ and HarperDB...."
---

Construire des applications full stack peut être difficile. Vous devez penser au frontend, aux API, aux bases de données, à l'authentification - et à la façon dont tous ces éléments fonctionnent ensemble.

Ainsi, dans cet article, je vais vous montrer comment faire tout cela en utilisant NextJS et HarperDB.

Nous allons construire une application full stack de minuteur de tâches qui inclut l'authentification par JSON Web Token, la récupération de données via l'API intégrée de HarperDB, et le rendu des données avec NextJS. Nous utiliserons également l'API de NextJS.

Si vous vous demandez ce qu'est HarperDB, il s'agit d'une base de données en tant que service (database-as-a-service) qui vous permet de requêter des données en utilisant soit SQL soit NoSQL. HarperDB dispose également d'une API intégrée, nous évitant d'avoir à écrire beaucoup de code backend.

[Voici ce que nous allons construire](https://next-js-harper-db-task-timer.vercel.app/).

[Voici le code source](https://github.com/DoableDanny/NextJS-HarperDB-Task-Timer) (n'oubliez pas de lui donner une étoile ⭐).

## Sommaire

- [Installation](#heading-installation)
- [Créer le composant Layout](#heading-creer-un-composant-layout-pour-envelopper-chaque-page)
- [Créer des composants réutilisables](#heading-creer-quelques-composants-reutilisables)
- [Créer la page d'inscription](#heading-creer-la-page-dinscription)
- [Comment déconnecter l'utilisateur](#heading-comment-deconnecter-lutilisateur)
- [La page de connexion](#heading-la-page-de-connexion)
- [Créer un contexte de tâches](#heading-creer-un-contexte-de-taches)
- [Créer la page du minuteur de tâches](#heading-creer-la-page-du-minuteur-de-taches)
- [Créer la barre d'ajout/sélection de tâches](#heading-creer-la-barre-dajoutselection-de-taches)
- [Créer la page de statistiques](#heading-la-page-de-statistiques)

## Installation

### 1. Installer NextJS avec TypeScript :

```bash
npx create-next-app@latest --ts
```

Il vous sera ensuite demandé un nom de projet. Je l'appelle "task timer".

Nous pouvons ensuite nous déplacer dans le répertoire du projet :

```bash
cd "task timer"
```

### 2. Installer et configurer TailwindCSS

Nous allons styliser ce projet avec [Tailwind](https://tailwindcss.com/), installons donc tout ce dont nous aurons besoin.

Installez TailwindCSS et ses dépendances via npm, puis lancez la commande d'initialisation pour générer les fichiers tailwind.config.js et postcss.config.js :

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

Ajoutez les chemins vers tous vos fichiers de composants React dans votre fichier tailwind.config.js :

```js
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Ensuite, créez un dossier `src` à la racine du projet, et déplacez les dossiers `styles` et `pages` dans `src`. Dans `styles/global.css`, ajoutez les directives Tailwind suivantes pour importer les classes Tailwind :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

![directives tailwind](https://www.freecodecamp.org/news/content/images/2022/03/tailwind.JPG)

Notre projet NextJS est maintenant configuré et prêt à être utilisé avec Tailwind.

Nettoyons notre page `src/pages/index.tsx` et ajoutons ce qui suit :

```tsx
import type { NextPage } from "next"

const Home: NextPage = () => {
  return (
    <div>
      <h1 className="text-red-500">Hello World</h1>
    </div>
  )
}

export default Home
```

Lancez le processus de build et démarrez le serveur de développement avec :

```bash
npm run dev
```

Notre serveur fonctionnera désormais sur http://localhost:3000

![Hello world](https://www.freecodecamp.org/news/content/images/2022/03/hello_world.JPG)

### 3. Configurer HarperDB

Tout d'abord, [créez un compte sur HarperDB](https://studio.harperdb.io/).

Créez ensuite une nouvelle instance cloud HarperDB :

![créer une instance HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/harper_instance.JPG)

Pour faciliter les choses, sélectionnez l'instance cloud :

![sélectionner le type d'instance HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/instance-type.JPG)

Sélectionnez le fournisseur cloud (j'ai choisi AWS) :

![sélectionner le fournisseur cloud HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/cloud_provider.JPG)

Nommez votre instance cloud et créez vos identifiants d'instance :

![sélectionner les identifiants d'instance HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/instance_credentials.JPG)

HarperDB propose un niveau gratuit généreux que nous pouvons utiliser pour ce projet, sélectionnez-le donc :

![sélectionner les spécifications de l'instance HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/instance_specs.JPG)

Vérifiez que vos informations sont correctes, puis créez l'instance.

La création de l'instance prendra quelques minutes, alors continuons et créons l'interface utilisateur de notre application !

![chargement de l'instance HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/instance_loading.JPG)

## Créer un composant Layout pour envelopper chaque page

Créez le dossier `src/components`. Ici, nous allons créer des composants qui pourront être réutilisés dans tout le projet.

Tout d'abord, créons un fichier pour stocker toutes les constantes qui seront utilisées dans notre application, comme le titre du site. Il est utile de garder une source unique de vérité pour des valeurs comme celle-ci, afin que si nous voulons les changer, nous n'ayons à le faire qu'à un seul endroit.

```tsx
// src/constants/constants.ts

export const SITE_TITLE = "Super Simple Task Timer"
```

Créons maintenant notre barre de navigation :

```tsx
// src/components/layout/Navbar.tsx

import Link from "next/link"
import { SITE_TITLE } from "../../constants/constants"

const Navbar = () => {
  return (
    <header className="flex justify-between items-center bg-green-600 text-white py-4 px-4">
      <h2 className="text-lg">
        <Link href="/">
          <a>{SITE_TITLE}</a>
        </Link>
      </h2>
      <nav>
        <ul className="flex">
          <NavLink href="/login">Login</NavLink>
          <NavLink href="/signup">Signup</NavLink>
        </ul>
      </nav>
    </header>
  )
}

interface NavLinkProps {
  href: string
  children: string
}

const NavLink: React.FC<NavLinkProps> = ({ href, children }) => {
  return (
    <li className="ml-8">
      <Link href={href}>
        <a>{children}</a>
      </Link>
    </li>
  )
}

export default Navbar
```

Créez le pied de page :

```tsx
// src/components/layout/Footer.tsx

import { SITE_TITLE } from "../../constants/constants"

const Footer = () => {
  return (
    <footer className="bg-green-600 text-white text-center py-4">
      <p className="mb-1">{SITE_TITLE} &copy;</p>
      <p>Designed & developed by Danny Adams</p>
    </footer>
  )
}

export default Footer
```

Nous pouvons maintenant créer notre composant layout pour envelopper chaque page. L'utilisation de flex-grow sur la balise `<main>` garantit que le contenu de la page occupe tout l'espace disponible entre l'en-tête et le pied de page.

```tsx
// src/components/layout/Layout.tsx

import Navbar from "./Navbar"
import Footer from "./Footer"

const Layout: React.FC = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex flex-col grow">{children}</main>
      <div className="mt-auto">
        <Footer />
      </div>
    </div>
  )
}

export default Layout
```

Ensuite, dans `src/pages/_app.tsx`, nous pouvons envelopper chaque composant de page avec `Layout` :

```tsx
import "../styles/globals.css"
import type { AppProps } from "next/app"
import Layout from "../components/layout/Layout"

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Layout>
      <Component {...pageProps} />
    </Layout>
  )
}

export default MyApp
```

Et voilà ! Chaque page a maintenant une barre de navigation, une zone de contenu qui occupe 100 % de l'espace disponible, et un pied de page qui reste toujours en bas.

![Composant Layout](https://www.freecodecamp.org/news/content/images/2022/03/layout.JPG)

## Créer quelques composants réutilisables

Nous allons maintenant créer quelques composants de base qui pourront être réutilisés tout au long du projet.

Créez un composant bouton :

```tsx
// src/components/Button.tsx

interface Props {
  children: React.ReactNode
  color: "primary" | "success" | "secondary" | "warning" | "danger"
  handleClick?: () => void
  type?: "button" | "submit"
  extraClasses?: string
}

const Button: React.FC<Props> = ({
  children,
  color,
  handleClick,
  type,
  extraClasses,
}) => {
  let colors: string
  switch (color) {
    case "primary":
      colors = "bg-blue-500 hover:bg-blue-600"
      break
    case "success":
      colors = "bg-green-500 hover:bg-green-600"
      break
    case "warning":
      colors = "bg-yellow-300 hover:bg-yellow-400 text-black"
      break
    case "secondary":
      colors = "bg-pink-500 hover:bg-pink-600"
      break
    default:
      colors = "bg-red-500 hover:bg-red-600"
  }
  const classes = `rounded text-white py-2 px-4 ${colors} ${extraClasses}`

  return (
    <button className={classes} onClick={handleClick} type={type}>
      {children}
    </button>
  )
}

export default Button
```

Créez un composant lien qui utilise NextJS Link pour pré-charger automatiquement en arrière-plan les pages vers lesquelles il renvoie - rendant les chargements de page rapides :

```tsx
// src/components/Link.tsx

import NextLink from "next/link"

interface Props {
  href: string
  children: React.ReactNode
}

const Link = ({ href, children }: Props) => {
  return (
    <NextLink href={href}>
      <a className="underline underline-offset-1 text-blue-700">{children}</a>
    </NextLink>
  )
}

export default Link
```

Créons également un composant `Alert` pour afficher des messages d'alerte, par exemple si un utilisateur saisit des données de formulaire invalides, un message d'erreur rouge sera affiché :

```tsx
// src/components/Alert.tsx

interface Props {
  children: React.ReactNode
  type: "success" | "warning" | "danger"
  key?: number
  extraClasses?: string
}
const Alert = ({ children, type, key, extraClasses }: Props) => {
  let color
  switch (type) {
    case "success":
      color = "bg-blue-500"
      break
    case "warning":
      color = "bg-yellow-300 text-yellow-800"
      break
    default:
      color = "bg-red-500"
  }
  const classes = `text-white text-center p-2 rounded mt-4 ${color} ${extraClasses}`

  return (
    <div key={key} className={classes}>
      {children}
    </div>
  )
}

export default Alert
```

Créez un composant de titre de page principale :

```tsx
// src/components/PageHeading.tsx

interface Props {
  extraClasses: string
}

const PageHeading: React.FC<Props> = ({ children, extraClasses }) => {
  const classes = "text-4xl text-green-900 font-semibold " + extraClasses

  return <h1 className={classes}>{children}</h1>
}

export default PageHeading
```

Créons également un composant à réutiliser dans nos formulaires de connexion et d'inscription qui contient un label et un input :

```tsx
// src/components/Form.tsx

interface InputProps {
  inputType: "text" | "email" | "password"
  inputName: string
  handleChange: (e: React.ChangeEvent<HTMLInputElement>) => void
  value: string
}

interface LabelAndInputProps extends InputProps {
  label: string
}

export const LabelAndInput: React.FC<LabelAndInputProps> = ({
  label,
  inputType,
  inputName,
  handleChange,
  value,
}) => {
  return (
    <div className="flex flex-col mb-2">
      <label htmlFor="name">{label}</label>
      <Input
        inputType={inputType}
        inputName={inputName}
        handleChange={handleChange}
        value={value}
      />
    </div>
  )
}

export const Input: React.FC<InputProps> = ({
  inputType,
  inputName,
  handleChange,
  value,
}) => {
  return (
    <input
      className="px-3 py-2 border-gray-200 border-2 rounded"
      type={inputType}
      name={inputName}
      id={inputName}
      onChange={handleChange}
      value={value}
    />
  )
}
```

## Créer la page d'inscription

[Voici à quoi ressemblera la page d'inscription](https://next-js-harper-db-task-timer.vercel.app/signup).

### UI de la page d'inscription

Tout d'abord, créons un composant de formulaire d'inscription à l'emplacement `src/components/signup-page/SignupForm.tsx` :

```tsx
// src/components/signup-page/SignupForm.tsx

import { useState } from "react"
import { LabelAndInput } from "../Form"
import Button from "../Button"

const SignupForm = () => {
  const [username, setUsername] = useState("")
  const [password1, setPassword1] = useState("")
  const [password2, setPassword2] = useState("")

  return (
    <form className="w-full sm:w-96">
      <LabelAndInput
        label="Username"
        inputType="text"
        inputName="username"
        handleChange={e => setUsername(e.target.value)}
        value={username}
      />
      <LabelAndInput
        label="Password"
        inputType="password"
        inputName="password1"
        handleChange={e => setPassword1(e.target.value)}
        value={password1}
      />
      <LabelAndInput
        label="Confirm password"
        inputType="password"
        inputName="password2"
        handleChange={e => setPassword2(e.target.value)}
        value={password2}
      />
      <Button
        color="success"
        type="submit"
        extraClasses="w-full mt-3 py-3 font-semibold"
      >
        Create Account
      </Button>
    </form>
  )
}

export default SignupForm
```

Nous pouvons créer la page d'inscription dans `src/pages/signup.tsx` et importer le formulaire ci-dessus :

```tsx
// src/pages/signup.tsx

import type { NextPage } from "next"
import SignupForm from "../components/signup-page/SignupForm"
import PageHeading from "../components/PageHeading"

const Signup: NextPage = () => {
  return (
    <div className="mx-auto mt-20">
      <PageHeading extraClasses="text-center mb-8">
        Create an account
      </PageHeading>
      <SignupForm />
    </div>
  )
}

export default Signup
```

L'interface utilisateur de notre page d'inscription est maintenant terminée :

![UI page d'inscription](https://www.freecodecamp.org/news/content/images/2022/03/signup_page.JPG)

### Logique de la page d'inscription

De retour dans notre composant `SignupForm`, ajoutez une fonction de rappel `handleSubmit` qui sera appelée lors de la soumission du formulaire :

```tsx
// src/components/signup-page/SignupForm.tsx

<form className='w-full sm:w-96' onSubmit={handleSubmit}>
```

Dans la fonction `handleSubmit`, nous devrons envoyer les données du formulaire à notre API NextJS. Notre API transmettra ensuite ces données à HarperDB pour créer un nouvel utilisateur dans notre base de données HarperDB.

Écrivons d'abord le début de notre fonction `handleSubmit` :

```tsx
// src/components/signup-page/SignupForm.tsx

// ...
import { postFormData } from "../../utils/postFormData"

const SignupForm = () => {
  // ...

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const formData = { username, password1, password2 };
    const { response, result } = await postFormData(formData, '/api/signup');

    console.log({ response, result });
  };
```

Créez maintenant un dossier `src/utils` et définissez une fonction utilitaire qui prend n'importe quel objet de données et une route API, puis renvoie la réponse et le résultat :

```tsx
// src/utils/postFormData.ts

export const postFormData = async (data: { [k: string]: any }, url: string) => {
  const requestOptions: RequestInit = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }
  const response = await fetch(url, requestOptions)
  const result = await response.json()
  return { response, result }
}
```

Nous devons créer notre première route API dans `src/pages/api/signup`.

Mais avant cela, nous allons installer le package `next-connect`, qui nous permet d'écrire nos API avec une syntaxe proche d'expressJS et nous fait gagner du temps sur la gestion des erreurs :

```bash
npm install next-connect
```

Créez un fichier dans `src/middleware/_defaultHandler.ts` et ajoutez ce qui suit :

```tsx
// src/middleware/_defaultHandler.ts

import { NextApiRequest, NextApiResponse } from "next"
import nextConnect from "next-connect"

// Cette fonction middleware s'exécutera entre chaque requête et gestionnaire d'API
const handler = nextConnect<NextApiRequest, NextApiResponse>({
  onError: (err, req, res) => {
    res.status(501).json({ error: `Something went wrong! ${err.message}` })
  },
  onNoMatch: (req, res) => {
    res.status(405).json({ error: `Method ${req.method} Not Allowed` })
  },
})

export default handler
```

La fonction middleware ci-dessus s'exécutera avec chaque requête API et gérera toutes les erreurs de requête.

Nous pouvons maintenant créer notre route API dans `src/pages/api/signup`. Tout d'abord, vérifions s'il y a des erreurs dans les données du formulaire envoyé, et renvoyons un tableau de messages d'erreur au client si c'est le cas :

```tsx
// src/pages/api/signup

import type { NextApiRequest, NextApiResponse } from "next"
import handler from "../../middleware/_defaultHandler"

export default handler.post(
  async (req: NextApiRequest, res: NextApiResponse) => {
    const { username, password1, password2 } = req.body

    const errors: string[] = getFormErrors(username, password1, password2)
    if (errors.length > 0) {
      return res.status(400).json({ error: errors })
    }
  }
)

const getFormErrors = (
  username: string,
  password1: string,
  password2: string
) => {
  const errors: string[] = []
  if (!username || !password1 || !password2) {
    errors.push("All fields are required")
  }
  if (password1.length < 6) {
    errors.push("Password must be at least 6 characters")
  }
  if (password1 !== password2) {
    errors.push("Passwords do not match")
  }
  return errors
}
```

Désormais, si nous envoyons des données de formulaire incorrectes depuis le frontend, nous obtenons des messages d'erreur enregistrés dans la console :

![Mauvaises données de formulaire](https://www.freecodecamp.org/news/content/images/2022/03/bad_request.JPG)

Une fois que nous savons que les données du formulaire sont valides, nous devons les envoyer à l'API HarperDB, qui créera un nouvel utilisateur pour nous. Écrivons une fonction qui s'en chargera.

Tout d'abord, nous avons besoin de l'URL de notre instance HarperDB. Si vous cliquez sur votre instance, puis allez dans "config", vous trouverez l'URL de votre instance et votre en-tête d'authentification API d'instance – c'est-à-dire votre mot de passe "super_user" qui vous permet d'effectuer n'importe quelle requête à la base de données – À GARDER SECRET !

![Infos de l'instance](https://www.freecodecamp.org/news/content/images/2022/03/instance_auth.JPG)

Nous aurons besoin de l'URL de l'instance à la fois sur le frontend et le backend, stockons-la donc dans notre fichier de constantes :

```ts
// src/constants/constants.ts

export const SITE_TITLE = "Super Simple Task Timer"
export const DB_URL = "Votre_URL_HDB_Ici"
```

Notre mot de passe doit rester secret, il ne doit donc jamais être disponible sur le frontend. Notre mot de passe sera chargé dans le serveur sous forme de variable d'environnement. Ajoutez votre mot de passe à `.env.local` à la racine de votre projet :

```bash
HARPERDB_PW=Basic votre_mot_de_passe_ici
```

HarperDB liste toutes les opérations pouvant être effectuées par catégorie dans l'onglet "example code" :

![exemples de code harperdb](https://www.freecodecamp.org/news/content/images/2022/03/harper_code_examples.JPG)

Nous voulons utiliser l'opération "add_user" de HarperDB, créons donc notre propre fonction pour faire cela :

```ts
// src/utils/harperdb/createNewUser.ts

import { DB_URL } from "../../constants/constants"

// Cette fonction ne peut être exécutée que sur le backend car elle nécessite un mot de passe "super_user"
export const harperCreateNewUser = async (
  username: string,
  password: string
) => {
  const DB_PW = process.env.HARPERDB_PW
  if (!DB_URL || !DB_PW) {
    console.log("Error: .env variables are undefined")
    throw "Internal server error"
  }
  const myHeaders = new Headers()
  myHeaders.append("Content-Type", "application/json")
  myHeaders.append("Authorization", DB_PW)
  const raw = JSON.stringify({
    operation: "add_user",
    role: "standard_user",
    username: username.toLowerCase(),
    password: password,
    active: true,
  })
  const requestOptions: RequestInit = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  }

  const response = await fetch(DB_URL, requestOptions)
  const result = await response.json()
  return { response, result }
}
```

Remarquez que le "role" est "standard_user". Si nous donnions à tous ceux qui créent un compte un rôle "super_user", n'importe qui pourrait supprimer vos tables et semer le chaos dans notre base de données !

Configurons maintenant ce rôle "standard_user" et créons les tables dont nous aurons besoin.

Créez un schéma appelé "productivity_timer" (un schéma est un groupe de tables). Dans ce schéma, créez une table appelée "tasks" avec l'attribut de hachage (la clé unique de chaque entrée) "id" :

![Créer une table HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/harper_make_tables.JPG)

Nous devons maintenant créer le rôle "standard_user" pour limiter l'accès de nos utilisateurs. Allez dans "roles" et créez un rôle standard appelé "standard_user". Modifiez ensuite toutes les autorisations d'accès à la table tasks sur true :

![Rôles utilisateur HarperDB](https://www.freecodecamp.org/news/content/images/2022/03/user_roles.JPG)

Ajoutons également quelques tâches à notre table que nous pourrons récupérer dans notre application plus tard :

![Ajouter des données](https://www.freecodecamp.org/news/content/images/2022/03/add_to_db.JPG)

Ajoutez le JSON suivant pour ajouter quelques tâches :

```json
[
  { "username": "dan", "task_name": "make header", "time_in_seconds": 0 },
  { "username": "dan", "task_name": "make footer", "time_in_seconds": 0 },
  { "username": "sally", "task_name": "learn NextJS", "time_in_seconds": 0 }
]
```

De retour à notre route API dans `src/pages/api/signup`, nous pouvons maintenant ajouter le code pour créer un nouvel utilisateur dans HarperDB :

```ts
// src/pages/api/signup

import type { NextApiRequest, NextApiResponse } from "next"
import handler from "../../middleware/_defaultHandler"
import { harperCreateNewUser } from "../../utils/harperdb/createNewUser"

export default handler.post(
  async (req: NextApiRequest, res: NextApiResponse) => {
    const { username, password1, password2 } = req.body

    const errors: string[] = getFormErrors(username, password1, password2)
    if (errors.length > 0) {
      return res.status(400).json({ error: errors })
    }

    // Créer un nouvel utilisateur avec HarperDB et renvoyer le résultat
    try {
      const { response, result } = await harperCreateNewUser(
        username,
        password1
      )
      return res.status(response.status).json(result)
    } catch (err) {
      return res.status(500).json({ error: err })
    }
  }
)
```

Pour tester la création d'un nouvel utilisateur, vous devrez maintenant arrêter le serveur de développement avec "ctrl + c", puis redémarrer avec `npm run dev` – afin de charger les variables .env.

Allez sur la page d'inscription, remplissez le formulaire et soumettez. YOUPI ! Nous avons créé notre premier utilisateur !

![Utilisateur créé](https://www.freecodecamp.org/news/content/images/2022/03/created_user.JPG)

Et si nous regardons dans la table users sur HarperDB, nous voyons que le nouvel utilisateur a été ajouté avec succès :

![Nouvel utilisateur dans la table](https://www.freecodecamp.org/news/content/images/2022/03/new_user.JPG)

Maintenant, côté frontend, nous devons gérer la réponse et le résultat renvoyés par le serveur.

Si le code de statut de la réponse renvoyé par le serveur n'est pas 200, nous savons que quelque chose s'est mal passé. Nous pouvons donc définir les erreurs dans une variable d'état et quitter `handleSubmit` prématurément :

```tsx
// src/components/signup-page/SignupForm.tsx

const [errors, setErrors] = useState<string | string[]>("")

const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault()
  setErrors("")

  const formData = { username, password1, password2 }
  const { response, result } = await postFormData(formData, "/api/signup")

  // Compte non créé avec succès
  if (response.status !== 200) {
    setErrors(result.error)
    return
  }
}
```

Affichons ces erreurs en bas du formulaire :

```tsx
// src/components/signup-page/SignupForm.tsx

// ...
import Alert from "../Alert"

const SignupForm = () => {
  // ...
  const [errors, setErrors] = useState<string | string[]>("")

  // ...

  const displayErrors = () => {
    if (errors.length === 0) return

    return typeof errors === "string" ? (
      <Alert type="danger">{errors}</Alert>
    ) : (
      errors.map((err, i) => (
        <Alert key={i} type="danger">
          {err}
        </Alert>
      ))
    )
  }

  return (
    <form className="w-full sm:w-96" onSubmit={handleSubmit}>
      {/* contenu du formulaire... */}

      {displayErrors()}
    </form>
  )
}

export default SignupForm
```

Désormais, si l'utilisateur saisit des données de formulaire invalides, des erreurs s'afficheront :

![Données de formulaire invalides](https://www.freecodecamp.org/news/content/images/2022/03/invalid_form.JPG)

Et si l'utilisateur existe déjà, HarperDB nous enverra un message d'erreur approprié :

![L'utilisateur existe déjà](https://www.freecodecamp.org/news/content/images/2022/03/user_exists.JPG)

Super !

Mais si le code de statut de la réponse est 200, alors nous savons que le compte a été créé avec succès. Nous pouvons donc obtenir un JSON Web Token (JWT) pour l'utilisateur, qui sera utilisé pour l'authentifier et lui permettre d'accéder aux routes protégées.

### Comment obtenir un JSON Web Token pour l'utilisateur

HarperDB peut créer des JWT pour chaque utilisateur de la base de données, ce qui signifie que nous n'avons pas besoin d'installer de packages et de gérer la logique nous-mêmes - génial !

Comment fonctionnera notre authentification JWT ? Lorsque HarperDB renverra un JWT au frontend, nous l'enregistrerons dans le localStorage du navigateur. Ensuite, chaque fois que l'utilisateur fera une requête, nous récupérerons le JWT du localStorage et l'attacherons à l'en-tête de la requête. HarperDB vérifiera automatiquement s'il y a un JWT dans l'en-tête de la requête et s'il est valide. Si c'est le cas, la requête sera traitée.

Mais d'abord, nous devons créer un contexte utilisateur en utilisant l'API Context de React afin que le nom d'utilisateur soit disponible dans toute l'application.

```ts
// src/contexts/UserContext.ts

import { createContext } from "react"

export const UserContext = createContext({
  username: "",
  setUsername: (username: string) => {},
})
```

Nous devons ensuite envelopper toute notre application dans le `UserContext.Provider`, afin que `username` et `setUsername` soient disponibles sur chaque page. Initialement, `username` sera une chaîne vide.

```tsx
// src/pages/_app.tsx

import { useState } from "react"
// ...
import { UserContext } from "../contexts/UserContext"

function MyApp({ Component, pageProps }: AppProps) {
  const [username, setUsername] = useState("")

  return (
    <UserContext.Provider value={{ username, setUsername }}>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </UserContext.Provider>
  )
}

export default MyApp
```

Écrivons maintenant une fonction qui récupérera les JWT depuis HarperDB. HarperDB vérifiera que le nom d'utilisateur et le mot de passe sont corrects, puis créera les JWT à partir du nom d'utilisateur et les renverra à notre application :

```ts
// src/utils/harperdb/fetchJWTTokens.ts

import { DB_URL } from "../../constants/constants"

export const harperFetchJWTTokens = async (
  username: string,
  password: string
) => {
  if (!DB_URL) {
    console.log("Error: DB_URL undefined")
    throw "Internal server error"
  }

  const myHeaders = new Headers()
  myHeaders.append("Content-Type", "application/json")

  const raw = JSON.stringify({
    operation: "create_authentication_tokens",
    username: username,
    password: password,
  })

  const requestOptions: RequestInit = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  }

  const response = await fetch(DB_URL, requestOptions)
  const result = await response.json()
  return { response, result }
}
```

De retour à `SignupForm.tsx`, nous devons récupérer les JWT en utilisant la fonction ci-dessus, vérifier si HarperDB les a créés et renvoyés avec succès, et si c'est le cas, authentifier l'utilisateur :

```tsx
// src/components/signup-page/SignupForm.tsx

import { useState, useContext } from "react"
import { UserContext } from "../../contexts/UserContext"
import { useRouter } from "next/router"
import { harperFetchJWTTokens } from "../../utils/harperdb/fetchJWTTokens"
// ...

const SignupForm = () => {
  //...

  const user = useContext(UserContext)
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    // ...

    // Compte créé avec succès ; récupérer les JWT
    try {
      const { response, result } = await harperFetchJWTTokens(
        username,
        password1
      )
      const accessToken = result.operation_token
      if (response.status === 200 && accessToken) {
        authenticateUser(username, accessToken)
      } else {
        // Compte créé, mais échec de récupération des JWT
        // Rediriger vers la page de connexion
        router.push("/login")
      }
    } catch (err) {
      console.log(err)
      setErrors("Whoops, something went wrong :(")
    }
  }

  const authenticateUser = (username: string, accessToken: string) => {
    user.setUsername(username)
    localStorage.setItem("access_token", accessToken)
  }

  // ...
}

export default SignupForm
```

Ci-dessus, si HarperDB renvoie le jeton d'opération avec succès, nous l'enregistrons dans le localStorage afin qu'il puisse être utilisé pour authentifier l'utilisateur tant que le JWT n'a pas expiré, et nous définissons le nom d'utilisateur dans le contexte.

Testons cela. Lorsque nous créons un nouvel utilisateur, nous devrions avoir un jeton d'accès stocké dans le localStorage. Créez un nouvel utilisateur, ouvrez vos outils de développement Chrome, puis sous "Application", vous devriez voir le jeton d'accès.

![Jeton d'accès dans le localStorage](https://www.freecodecamp.org/news/content/images/2022/03/access_token.JPG)

Génial !

Dans `src/pages/signup.tsx`, affichons un composant différent selon que le nom d'utilisateur est défini :

```tsx
// src/pages/signup.tsx

import { useContext } from "react"
import { UserContext } from "../contexts/UserContext"
import Alert from "../components/Alert"
// ...

const Signup: NextPage = () => {
  const { username } = useContext(UserContext)

  return (
    <div className="mx-auto mt-20">
      {username ? (
        <Alert type="success">You are logged in as {username}</Alert>
      ) : (
        <>
          <PageHeading extraClasses="text-center mb-8">
            Create an account
          </PageHeading>
          <SignupForm />
        </>
      )}
    </div>
  )
}

export default Signup
```

Maintenant, quand nous créons un compte, nous obtenons ceci :

![Alerte connecté](https://www.freecodecamp.org/news/content/images/2022/03/logged_in.JPG)

Mais nous avons un problème : le contexte ne conserve pas le nom d'utilisateur lorsque nous rafraîchissons la page, ce qui signifie qu'au rafraîchissement, le formulaire d'inscription s'affichera à nouveau, même si l'utilisateur est connecté.

Pour résoudre ce problème, nous pouvons créer un hook personnalisé appelé `useUser`.

### Créer un hook personnalisé useUser

Le hook `useUser` s'exécutera une fois chaque fois que l'utilisateur accède à une nouvelle page ou rafraîchit la page actuelle.

Commençons par créer le hook. Nous allons également déplacer `username` et `setUsername` dans ce hook pour garder les choses organisées.

```ts
// src/custom-hooks/useUser.ts

import { useState, useEffect } from "react"
import { harperGetUsername } from "../utils/harperdb/getUsername"

export const useUser = () => {
  const [username, setUsername] = useState("")

  useEffect(() => {
    // L'utilisateur est connecté
    if (username) return

    // Vérifier le jeton d'accès et essayer de connecter l'utilisateur
    const accessToken = localStorage.getItem("access_token")
    if (accessToken) {
      tryLogUserIn(accessToken)
    }

    async function tryLogUserIn(accessToken: string) {
      const username = await harperGetUsername(accessToken)
      if (username) {
        setUsername(username)
      }
    }
  })

  return { username, setUsername }
}
```

Nous devons maintenant créer la fonction `harperGetUsername`. Cette fonction enverra le jeton d'accès à HarperDB. HarperDB vérifiera ensuite si le jeton d'accès est valide et à quel utilisateur il appartient. Si tout est correct, HarperDB renverra les informations de l'utilisateur correspondant.

```ts
// src/utils/harperdb/getUsername.ts

import { DB_URL } from "../../constants/constants"

export const harperGetUsername = async (accessToken: string) => {
  const myHeaders = new Headers()
  myHeaders.append("Content-Type", "application/json")
  myHeaders.append("Authorization", "Bearer " + accessToken)

  const raw = JSON.stringify({
    operation: "user_info",
  })

  const requestOptions: RequestInit = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  }

  try {
    const response = await fetch(DB_URL, requestOptions)
    const result = await response.json()
    if (response.status === 200) {
      return result.username
    }
  } catch (err) {
    console.log(err)
  }
  return null
}
```

Notre hook `useUser` est prêt. Instancions-le dans `_app.tsx` afin qu'à chaque visite d'une nouvelle page, la fonction `useEffect` s'exécute et authentifie l'utilisateur :

```tsx
// src/pages/_app.tsx

// ...
import { useUser } from "../custom-hooks/useUser"

function MyApp({ Component, pageProps }: AppProps) {
  // Supprimer la ligne ci-dessous
  // const [username, setUsername] = useState('');
  const { username, setUsername } = useUser()

  return (
    <UserContext.Provider value={{ username, setUsername }}>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </UserContext.Provider>
  )
}

export default MyApp
```

Maintenant, quand nous rafraîchissons la page, le nom d'utilisateur est récupéré à l'aide du JWT d'accès stocké dans le localStorage, maintenant notre utilisateur connecté. Génial !

![Image](https://www.freecodecamp.org/news/content/images/2022/03/logged_in-1.JPG)
_Alerte connecté_

## Comment déconnecter l'utilisateur

Le système d'authentification que nous implémentons est "sans état" (stateless) – ce qui signifie qu'aucune information n'est stockée dans la base de données ou sur le serveur pour nous dire qui est connecté et qui ne l'est pas. Seul un JWT d'accès est stocké sur le client pour authentifier les utilisateurs.

La seule façon dont nous disposons pour déconnecter un utilisateur est de supprimer le jeton d'accès dans le localStorage de l'utilisateur. Bien sûr, s'ils sont connectés sur plusieurs appareils, ils ne peuvent se déconnecter que de l'appareil sur lequel ils se trouvent.

De plus, si le jeton d'accès était volé, n'importe qui pourrait se faire passer pour cet utilisateur et accéder à ses données. C'est une faiblesse majeure de notre système d'authentification.

Une façon de résoudre cela serait d'utiliser des [refresh tokens](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/), mais nous allons garder les choses simples dans ce tutoriel et utiliser un seul JWT pour accéder aux routes protégées.

Dans nos composants `Navbar`, ajoutons un bouton de déconnexion. Nous utiliserons un opérateur ternaire pour afficher les liens "Login" et "Signup" si `username` n'est pas défini. Si `username` est défini, l'utilisateur est connecté, nous pouvons donc lui montrer des liens vers les pages "Timer" et "Stats", ainsi que le bouton "Logout".

```tsx
// src/components/layout/Navbar.tsx

import Link from "next/link"
import { useContext } from "react"
import { SITE_TITLE } from "../../constants/constants"
import { UserContext } from "../../contexts/UserContext"

const Navbar = () => {
  const { username, setUsername } = useContext(UserContext)

  const handleLogout = () => {
    localStorage.removeItem("access_token")
    setUsername("")
  }

  return (
    <header className="flex justify-between items-center bg-green-600 text-white py-4 px-4">
      <h2 className="text-lg">
        <Link href="/">
          <a>{SITE_TITLE}</a>
        </Link>
      </h2>
      <nav>
        <ul className="flex items-center">
          {username ? (
            <>
              <NavLink href="/">Timer</NavLink>
              <NavLink href="/stats">Stats</NavLink>
              <button
                onClick={handleLogout}
                className="border py-1 px-3 ml-8 rounded hover:bg-green-700"
                type="button"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <NavLink href="/login">Login</NavLink>
              <NavLink href="/signup">Signup</NavLink>
            </>
          )}
        </ul>
      </nav>
    </header>
  )
}
// ...
```

## La page de connexion

[Voici la page de connexion](https://next-js-harper-db-task-timer.vercel.app/login) que nous allons construire dans cette section.

### UI de la page de connexion

Créons l'interface utilisateur pour la page de connexion. D'abord :

```tsx
// src/pages/login.tsx

import { useContext } from "react"
import type { NextPage } from "next"
import { UserContext } from "../contexts/UserContext"
import PageHeading from "../components/PageHeading"
import LoginForm from "../components/login-page/LoginForm"

const Login: NextPage = () => {
  const { username } = useContext(UserContext)

  return (
    <div className="grow flex flex-col items-center mt-20">
      {username ? (
        <p>
          You are logged in as{" "}
          <span className="text-green-600 font-semibold">{username}</span> 👋
        </p>
      ) : (
        <>
          <PageHeading extraClasses="text-center mb-8">Log in</PageHeading>
          <LoginForm />
        </>
      )}
    </div>
  )
}

export default Login
```

Ensuite, créez `LoginForm` :

```tsx
// src/components/login-page/LoginForm.tsx

import { useState } from "react"
import { LabelAndInput } from "../Form"
import Button from "../Button"
import Alert from "../Alert"

const LoginForm = () => {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  return (
    <form className="w-full sm:w-96">
      <LabelAndInput
        label="Username"
        inputType="text"
        inputName="username"
        handleChange={e => setUsername(e.target.value)}
        value={username}
      />
      <LabelAndInput
        label="Password"
        inputType="password"
        inputName="password"
        handleChange={e => setPassword(e.target.value)}
        value={password}
      />
      <Button color="success" extraClasses="w-full mt-3 py-3 font-semibold">
        Login
      </Button>

      {error && <Alert type="danger">{error}</Alert>}
    </form>
  )
}

export default LoginForm
```

Maintenant, nous pouvons créer une fonction `handleSubmit` sur notre formulaire de connexion :

```tsx
// src/components/login-page/LoginForm.tsx

import { useState, useContext } from "react"
// ...
import { UserContext } from "../../contexts/UserContext"

const LoginForm = () => {
  // ...
  const [error, setError] = useState("")
  const user = useContext(UserContext)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    setError("")
  }

  return (
    <form className="w-full sm:w-96" onSubmit={handleSubmit}>
      {/* ... */}
    </form>
  )
}

export default LoginForm
```

Terminer le reste de notre fonction `handleSubmit` :

```tsx
// src/components/login-page/LoginForm.tsx

const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault()
  setError("")
  if (!username || !password) {
    setError("Username and password required")
    return
  }

  try {
    const { response, result } = await harperFetchJWTTokens(username, password)
    const { status } = response
    const accessToken = result.operation_token
    if (status === 200 && accessToken) {
      authenticateUser(username, accessToken)
    } else if (status === 401) {
      setError("Check your username and password are correct")
    } else {
      setError("Whoops, something went wrong :(")
    }
  } catch (err) {
    console.log(err)
    setError("Whoops, something went wrong :(")
  }
}

const authenticateUser = (username: string, accessToken: string) => {
  user.setUsername(username)
  localStorage.setItem("access_token", accessToken)
}
```

Maintenant, si nous saisissons les informations d'un utilisateur absent de notre base de données, nous obtenons une erreur :

![erreur de connexion](https://www.freecodecamp.org/news/content/images/2022/03/login_error.JPG)

Si nous nous connectons avec un utilisateur qui existe :

![Connexion réussie](https://www.freecodecamp.org/news/content/images/2022/03/login_success.JPG)

Nous pouvons maintenant créer un compte et nous connecter à notre application. Génial !

## Créer un contexte de tâches

Notre page de minuteur ('/') et notre page de statistiques ('/stats') auront toutes deux besoin de connaître les tâches ajoutées par l'utilisateur, ainsi que le nombre de secondes passées sur chaque tâche. Nous pouvons partager l'état des tâches entre les pages à l'aide de l'API Context.

Tout d'abord, créons un type pour les tâches afin que TypeScript puisse nous avertir si une tâche manque d'une propriété, ou si nous essayons d'accéder à une propriété inexistante sur les tâches, rendant notre code plus robuste :

```ts
// src/types/Task.ts

export interface Task {
  __createdtime__: number
  __updatedtime__: number
  username: string
  time_in_seconds: number
  id: string
  task_name: string
}
```

Ensuite, nous pouvons créer notre contexte de tâches :

```tsx
// src/contexts/TasksContext.ts

import React, { createContext } from "react"
import type { Task } from "../types/Task"

interface TasksContext {
  tasks: Task[]
  setTasks: React.Dispatch<React.SetStateAction<Task[]>>
  getAndSetTasks: (username: string) => Promise<void>
}

export const TasksContext = createContext({} as TasksContext)
```

Avant d'envelopper notre application avec le fournisseur de contexte de tâches, créons un hook personnalisé qui contiendra un hook `useEffect` s'exécutant à chaque visite d'une nouvelle page ou à chaque rafraîchissement. Il vérifiera si l'utilisateur est connecté et si l'état des tâches est vide, il tentera de récupérer les tâches depuis la base de données :

```tsx
// src/custom-hooks/useTasks.ts

import { useState, useCallback, useEffect } from "react"
import type { Task } from "../types/Task"
import { harperGetTasks } from "../utils/harperdb/getTasks"

export const useTasks = (username: string) => {
  const [tasks, setTasks] = useState<Task[]>([])

  // Récupérer les tâches de la db puis définir l'état des tâches
  const getAndSetTasks = useCallback(
    async (username: string) => {
      try {
        const tasks: Task[] = await harperGetTasks(username)
        setTasks(tasks)
      } catch (err) {
        console.log(err)
      }
    },
    [setTasks]
  )

  useEffect(() => {
    if (!username || tasks.length > 0) return
    getAndSetTasks(username)
  }, [username, tasks.length, getAndSetTasks])

  return { tasks, setTasks, getAndSetTasks }
}
```

Maintenant, nous devons définir la fonction `harperGetTasks` pour récupérer toutes les tâches de la base de données ayant le nom d'utilisateur de notre utilisateur. Comme vous pouvez le voir, HarperDB prend en charge les opérations SQL et NoSQL. Nous trions les tâches pour afficher celles sur lesquelles l'utilisateur a travaillé le plus récemment en haut :

```ts
// src/utils/harperdb/getTasks.ts

import { harperFetch } from "./harperFetch"

export const harperGetTasks = async (username: string) => {
  const data = {
    operation: "sql",
    sql: `SELECT * FROM productivity_timer.tasks WHERE username = '${username}' ORDER BY __updatedtime__ DESC`,
  }

  const { result } = await harperFetch(data)
  return result
}
```

Toutes nos fonctions HarperDB incluront désormais le même code répétitif, j'ai donc créé une fonction utilitaire `harperFetch` pour garder le code DRY (ne pas se répéter) :

```ts
// src/utils/harperFetch.ts

import { DB_URL } from "../../constants/constants"

export const harperFetch = async (data: { [key: string]: any }) => {
  const accessToken = localStorage.getItem("access_token")
  if (!accessToken) throw { error: "You need to log in" }

  const myHeaders = new Headers()
  myHeaders.append("Content-Type", "application/json")
  myHeaders.append("Authorization", "Bearer " + accessToken)

  const raw = JSON.stringify(data)

  const requestOptions: RequestInit = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  }

  const response = await fetch(DB_URL, requestOptions)
  const result = await response.json()
  return { response, result }
}
```

OK, donnons maintenant à toutes les pages de notre application l'accès à l'état `tasks` :

```tsx
// src/pages/_app.tsx

// ...
import { TasksContext } from "../contexts/TasksContext"
import { useTasks } from "../custom-hooks/useTasks"

function MyApp({ Component, pageProps }: AppProps) {
  // ...
  const { tasks, setTasks, getAndSetTasks } = useTasks(username)

  console.log(tasks)

  return (
    <UserContext.Provider value={{ username, setUsername }}>
      <TasksContext.Provider value={{ tasks, setTasks, getAndSetTasks }}>
        <Layout>
          <Component {...pageProps} />
        </Layout>
      </TasksContext.Provider>
    </UserContext.Provider>
  )
}

export default MyApp
```

Maintenant, je suis connecté en tant que "dan", je devrais donc voir toutes les tâches de dan affichées dans la console – et c'est le cas :

![tâches de dan](https://www.freecodecamp.org/news/content/images/2022/03/dans_tasks.JPG)

## Créer la page du minuteur de tâches

L'interface de la page d'accueil doit ressembler à ceci :

![page d'accueil](https://www.freecodecamp.org/news/content/images/2022/03/home_page.JPG)

La ligne du haut est l'endroit où l'utilisateur peut sélectionner l'une de ses tâches stockées dans la base de données via un menu déroulant. Il peut également ajouter une nouvelle tâche à la base de données.

En dessous, nous avons le minuteur qui suivra le temps passé par l'utilisateur sur chaque tâche.

[Voici la page que nous allons construire](https://next-js-harper-db-task-timer.vercel.app/) dans cette section.

## Créer la barre d'ajout/sélection de tâches

Commençons par créer la ligne de sélection ou d'ajout de tâche, sous forme de composant à importer dans la page d'accueil :

```tsx
// src/components/home-page/Taskbar.tsx

import { useState, useContext } from "react"
import { harperAddNewTask } from "../../utils/harperdb/addNewTask"
import { UserContext } from "../../contexts/UserContext"
import { TasksContext } from "../../contexts/TasksContext"
import Button from "../Button"

interface Props {
  selectedTaskId: string
  setSelectedTaskId: React.Dispatch<React.SetStateAction<string>>
  setErrorMessage: React.Dispatch<React.SetStateAction<string>>
  setSeconds: React.Dispatch<React.SetStateAction<number>>
  pauseTimer: () => void
}

const TaskBar = ({
  selectedTaskId,
  setSelectedTaskId,
  setErrorMessage,
  setSeconds,
  pauseTimer,
}: Props) => {
  const { username } = useContext(UserContext)
  const { tasks, getAndSetTasks } = useContext(TasksContext)

  const [isUserAddingNewTask, setIsUserAddingNewTask] = useState(false)
  const [taskInputValue, setTaskInputValue] = useState("")

  const handleChangeTaskInput = (e: { target: HTMLInputElement }) => {
    setTaskInputValue(e.target.value)
  }

  const handleSelectTask = (e: { target: HTMLSelectElement }) => {
    setErrorMessage("")
    setSelectedTaskId(e.target.value)
    setSeconds(0)
    pauseTimer()
  }

  const handleClickAddNewTask = () => {
    if (taskInputValue.trim() === "") {
      setErrorMessage("Type a task!")
      return
    }
    addNewTask()
    resetAddingNewTask()
  }

  const addNewTask = async () => {
    try {
      const { response } = await harperAddNewTask(username, taskInputValue)
      if (response.status === 200) {
        // Tâche ajoutée à la db avec succès
        getAndSetTasks(username)
      } else setErrorMessage("Whoops, something went wrong")
    } catch (err) {
      console.log(err)
      setErrorMessage("Whoops, something went wrong")
    }
  }

  const resetAddingNewTask = () => {
    setTaskInputValue("")
    setIsUserAddingNewTask(false)
  }

  return (
    <div>
      {isUserAddingNewTask ? (
        <>
          <input
            type="text"
            placeholder="Enter task here..."
            value={taskInputValue}
            onChange={handleChangeTaskInput}
            className="border p-2 mr-2"
          />
          <Button color="primary" handleClick={handleClickAddNewTask}>
            Add task
          </Button>
          <Button
            color="secondary"
            handleClick={() => setIsUserAddingNewTask(false)}
            extraClasses="ml-1"
          >
            Cancel
          </Button>
        </>
      ) : (
        <>
          <select
            className="mr-4 p-2 border"
            name="task"
            id="task"
            onChange={handleSelectTask}
          >
            {selectedTaskId === "" && (
              <option disabled selected value="" hidden>
                -- Select a task --
              </option>
            )}
            {tasks.map(task => (
              <option
                key={task.id}
                value={task.id}
                selected={task.id === selectedTaskId}
              >
                {task.task_name}
              </option>
            ))}
          </select>
          <Button
            handleClick={() => setIsUserAddingNewTask(true)}
            color="primary"
          >
            New Task
          </Button>
        </>
      )}
    </div>
  )
}

export default TaskBar
```

Ci-dessus, dans le JSX, quand l'utilisateur clique sur le bouton "New Task", `isUserAddingNewTask` est défini sur true, et la première partie de l'instruction ternaire est rendue. Cela permet à l'utilisateur d'ajouter une nouvelle tâche.

Créons la fonction `harperAddNewTask` :

```ts
// src/utils/harperdb/addNewTask.ts

import { harperFetch } from "./harperFetch"

export const harperAddNewTask = async (username: string, taskName: string) => {
  const data = {
    operation: "insert",
    schema: "productivity_timer",
    table: "tasks",
    records: [
      {
        username: username,
        task_name: taskName,
        time_in_seconds: 0,
      },
    ],
  }

  const responseAndResult = await harperFetch(data)
  return responseAndResult
}
```

Maintenant, si nous importons notre `Taskbar` dans la page d'accueil, nous la verrons :

```tsx
// src/pages/index.tsx

import type { NextPage } from "next"
import Taskbar from "../components/home-page/Taskbar"

const Home: NextPage = () => {
  return (
    <div>
      <Taskbar />
    </div>
  )
}

export default Home
```

![barre de tâches](https://www.freecodecamp.org/news/content/images/2022/03/taskbar.JPG)

TypeScript nous gronde à juste titre parce que `Taskbar` manque de certaines props, mais nous y reviendrons bientôt.

### Créer le minuteur

Tout d'abord, écrivons une fonction qui prendra un ID de tâche et un temps en secondes, et mettra à jour la tâche dans la base de données :

```ts
// src/utils/harperdb/saveTaskTime.ts

import { harperFetch } from "./harperFetch"

export const harperSaveTaskTime = async (
  taskId: string,
  newSeconds: number
) => {
  const data = {
    operation: "sql",
    sql: `UPDATE productivity_timer.tasks SET time_in_seconds = '${newSeconds}' WHERE id = '${taskId}'`,
  }

  const responseAndResult = await harperFetch(data)
  return responseAndResult
}
```

Ensuite, créez un hook personnalisé pour conserver l'état des secondes (`seconds`), si le minuteur tourne (`isTimerOn`), et les fonctions nécessaires pour démarrer et arrêter le minuteur :

```ts
// src/custom-hooks/useTimer.ts

import { useState, useRef } from "react"

const useTimer = () => {
  const [isTimerOn, setIsTimerOn] = useState(false)
  const [seconds, setSeconds] = useState(0)

  const intervalRef = useRef<NodeJS.Timer | null>(null)

  const startTimer = () => {
    setIsTimerOn(true)

    const intervalId = setInterval(() => {
      setSeconds(prev => prev + 1)
    }, 1000)

    intervalRef.current = intervalId
  }

  const pauseTimer = () => {
    setIsTimerOn(false)
    clearInterval(intervalRef.current as NodeJS.Timeout)
  }

  return {
    isTimerOn,
    seconds,
    setSeconds,
    startTimer,
    pauseTimer,
  }
}

export default useTimer
```

Sur notre minuteur, nous voulons afficher le temps en heures:minutes:secondes, mais nous enregistrerons le temps écoulé en secondes. Nous avons donc besoin d'un moyen de convertir les secondes en HH:MM:SS. Nous le ferons avec une fonction utilitaire `formatTime` :

```ts
// src/utils/formatTime.ts

const SECONDS_PER_HOUR = 3600
const SECONDS_PER_MINUTE = 60

// HH:MM:SS
export const formatTime = (seconds: number) => {
  const { hours, mins, secs } = calculateHoursMinsAndSecs(seconds)

  const formattedHours = prependZeroIfLessThanTen(hours)
  const formattedMins = prependZeroIfLessThanTen(mins)
  const formattedSecs = prependZeroIfLessThanTen(secs)

  return {
    formattedHours,
    formattedMins,
    formattedSecs,
  }
}

// Préfixer le temps avec un 0 s'il est inférieur à 10. Ex: '1' => '01'.
const prependZeroIfLessThanTen = (time: number) => {
  const formattedTime: string = time < 10 ? `0${time}` : `${time}`
  return formattedTime
}

// Convertir les secondes en heures, minutes et secondes
const calculateHoursMinsAndSecs = (seconds: number) => {
  const hours = calculateHours(seconds)
  const mins = calculateMins(seconds)
  const secs = calculateSecs(seconds)

  return {
    hours,
    mins,
    secs,
  }
}

const calculateHours = (seconds: number) => {
  const hours = Math.floor(seconds / SECONDS_PER_HOUR)
  return hours
}

const calculateMins = (seconds: number) => {
  const mins = Math.floor((seconds % SECONDS_PER_HOUR) / SECONDS_PER_MINUTE)
  return mins
}

const calculateSecs = (seconds: number) => {
  const secs = Math.floor((seconds % SECONDS_PER_HOUR) % SECONDS_PER_MINUTE)
  return secs
}
```

Créons maintenant notre composant Timer (note : pas de panique, nous transmettrons toutes les props ensuite !) :

```tsx
// src/components/home-page/Timer.tsx

import { useContext } from "react"
import { TasksContext } from "../../contexts/TasksContext"
import { UserContext } from "../../contexts/UserContext"
import { formatTime } from "../../utils/formatTime"
import { harperSaveTaskTime } from "../../utils/harperdb/saveTaskTime"
import Button from "../Button"
import type { RecentTaskTime } from "../../types/RecentTaskTime"

interface TimerProps {
  seconds: number
  setSeconds: React.Dispatch<React.SetStateAction<number>>
  isTimerOn: boolean
  startTimer: () => void
  pauseTimer: () => void
  setErrorMessage: React.Dispatch<React.SetStateAction<string>>
  selectedTaskId: string
  selectedTaskName: string
  setRecentTaskTimes: React.Dispatch<React.SetStateAction<RecentTaskTime[]>>
}

export const Timer: React.FC<TimerProps> = ({
  seconds,
  setSeconds,
  isTimerOn,
  startTimer,
  pauseTimer,
  setErrorMessage,
  selectedTaskId,
  selectedTaskName,
  setRecentTaskTimes,
}) => {
  const { tasks, getAndSetTasks } = useContext(TasksContext)
  const { username } = useContext(UserContext)

  const { formattedHours, formattedMins, formattedSecs } = formatTime(seconds)

  const handleStartTimer = () => {
    setErrorMessage("")
    if (selectedTaskId == "") {
      setErrorMessage("Please select a task")
    } else {
      startTimer()
    }
  }

  const handleLogTime = async () => {
    pauseTimer()
    const prevTaskSeconds = getTaskTimeFromId(selectedTaskId)
    const newTaskSeconds = prevTaskSeconds + seconds
    const { response, result } = await harperSaveTaskTime(
      selectedTaskId,
      newTaskSeconds
    )
    if (response.status === 200) {
      getAndSetTasks(username)
      setSeconds(0)
      setRecentTaskTimes(prev => [
        { name: selectedTaskName, seconds: seconds },
        ...prev,
      ])
    } else setErrorMessage("Whoops, something went wrong :(")
    console.log({ response, result })
  }

  const getTaskTimeFromId = (id: string) => {
    const task = tasks.find(task => task.id === id)
    if (!task) return 0
    return task.time_in_seconds
  }

  const handleResetTimer = () => {
    pauseTimer()
    setSeconds(0)
  }

  return (
    <div>
      <div className="mt-8 border-2 border-gray-500 rounded p-14 text-5xl">
        {formattedHours} : {formattedMins} : {formattedSecs}
      </div>
      <div className="flex justify-center mt-10">
        {/* Boutons de pause et de démarrage du minuteur */}
        {isTimerOn ? (
          <>
            <Button color="warning" handleClick={pauseTimer}>
              Pause
            </Button>
          </>
        ) : (
          <Button color="success" handleClick={handleStartTimer}>
            Start
          </Button>
        )}

        {/* Bouton pour mettre à jour le temps dans la db pour la tâche choisie */}
        {(seconds > 0 || isTimerOn) && (
          <Button
            color="danger"
            handleClick={handleLogTime}
            extraClasses="ml-4"
          >
            Log time
          </Button>
        )}
      </div>

      {/* Arrêter le minuteur et réinitialiser à 0 sec */}
      {(seconds > 0 || isTimerOn) && (
        <button
          onClick={handleResetTimer}
          className="underline underline-offset-2 mt-8 cursor-pointer text-gray-500 mx-auto block"
        >
          Reset
        </button>
      )}
    </div>
  )
}

interface TimerBtnProps {
  handleClick: () => void
  text: string
  extraClasses?: string
}

export const TimerBtn: React.FC<TimerBtnProps> = ({
  handleClick,
  text,
  extraClasses,
}) => {
  return (
    <button
      className={`${
        text === "Start" ? "bg-blue-500" : "bg-red-500"
      } rounded px-4 py-2 text-white mt-8 ${extraClasses}`}
      onClick={handleClick}
    >
      {text}
    </button>
  )
}
```

Nous pouvons maintenant ajouter `Taskbar` et `Timer` à notre page d'index, et transmettre toutes les props nécessaires à ces composants :

```tsx
// src/pages/index.tsx

import { useState, useContext } from "react"
import type { NextPage } from "next"
import type { RecentTaskTime } from "../types/RecentTaskTime"
import { UserContext } from "../contexts/UserContext"
import useTimer from "../custom-hooks/useTimer"
import Taskbar from "../components/home-page/Taskbar"
import { Timer } from "../components/home-page/Timer"
import Alert from "../components/Alert"
import Link from "../components/Link"

const Home: NextPage = () => {
  const [selectedTaskId, setSelectedTaskId] = useState("")
  const [selectedTaskName, setSelectedTaskName] = useState("")
  const [errorMessage, setErrorMessage] = useState("")
  const [recentTaskTimes, setRecentTaskTimes] = useState<RecentTaskTime[]>([])

  const { isTimerOn, seconds, setSeconds, startTimer, pauseTimer } = useTimer()

  const { username } = useContext(UserContext)

  return (
    <div className="flex flex-col items-center justify-center pt-4 grow">
      {!username && (
        <Alert type="warning" extraClasses="mb-12">
          Please <Link href="/login">log in</Link> or{" "}
          <Link href="/signup">create an account</Link> to use Super
          Productivity Timer
        </Alert>
      )}

      <Taskbar
        selectedTaskId={selectedTaskId}
        setSelectedTaskId={setSelectedTaskId}
        setSelectedTaskName={setSelectedTaskName}
        setErrorMessage={setErrorMessage}
        setSeconds={setSeconds}
        pauseTimer={pauseTimer}
      />
      <Timer
        seconds={seconds}
        setSeconds={setSeconds}
        setRecentTaskTimes={setRecentTaskTimes}
        selectedTaskName={selectedTaskName}
        isTimerOn={isTimerOn}
        startTimer={startTimer}
        pauseTimer={pauseTimer}
        setErrorMessage={setErrorMessage}
        selectedTaskId={selectedTaskId}
      />

      {errorMessage && <div className="text-red-500 mt-4">{errorMessage}</div>}
    </div>
  )
}

export default Home
```

Notre minuteur devrait maintenant fonctionner. Essayez d'ajouter une tâche, de démarrer le minuteur, puis d'enregistrer le temps. Cela devrait apparaître dans votre base de données HarperDB :

![temps db](https://www.freecodecamp.org/news/content/images/2022/03/db_times.JPG)

### Ajouter un journal des temps récemment complétés

Terminons notre page de minuteur en ajoutant un journal pour donner à l'utilisateur un retour visuel indiquant que les temps ont été enregistrés avec succès. Cela ressemblera à ceci :

![journal des temps](https://www.freecodecamp.org/news/content/images/2022/03/log.JPG)

Créez un type appelé `RecentTaskTime` :

```ts
// src/types/RecentTaskTime.ts

export interface RecentTaskTime {
  name: string
  seconds: number
}
```

Ensuite, dans `index.tsx` :

```tsx
// ...
import LogOfRecentTaskTimes from "../components/home-page/LogOfRecentTaskTimes"

const Home: NextPage = () => {
  // ...
  const [recentTaskTimes, setRecentTaskTimes] = useState<RecentTaskTime[]>([])

  return (
    <div className="flex flex-col items-center justify-center pt-4 grow">
      {/* ... */}

      {recentTaskTimes.length > 0 && (
        <LogOfRecentTaskTimes recentTaskTimes={recentTaskTimes} />
      )}
    </div>
  )
}
```

Maintenant, créons le composant `LogOfRecentTaskTimes` :

```tsx
// src/components/home-page/LogOfRecentTaskTimes.tsx

import type { RecentTaskTime } from "../../types/RecentTaskTime"

interface Props {
  recentTaskTimes: RecentTaskTime[]
}

const LogOfRecentTaskTimes = ({ recentTaskTimes }: Props) => {
  return (
    <div className="mt-8 max-h-56 overflow-y-auto px-8">
      {recentTaskTimes.map((t, i) => (
        <div key={i} className="flex shadow rounded px-8 py-4 mt-2">
          <p>
            <span className="text-green-600">{t.seconds}</span> seconds added to{" "}
            <span className="text-green-600">{t.name}</span>
          </p>
        </div>
      ))}
    </div>
  )
}

export default LogOfRecentTaskTimes
```

Notre page de minuteur est terminée 🥳

## La page de statistiques

Bravo si vous êtes arrivé jusqu'ici ! Il ne nous reste plus qu'une page : [la page de statistiques](https://next-js-harper-db-task-timer.vercel.app/stats).

Dans la page de statistiques, nous allons récupérer toutes les tâches de l'utilisateur depuis la table tasks de HarperDB et les afficher joliment dans un tableau.

Tout d'abord, nous aurons besoin de quelques fonctions utilitaires pour afficher l'heure et la date joliment dans notre tableau de statistiques. Ajoutez les deux fonctions suivantes à notre fichier utilitaire formatTime :

```ts
// src/utils/formatTime.ts

// ...

export const displayTimeString = (seconds: number) => {
  const { formattedHours, formattedMins, formattedSecs } = formatTime(seconds)
  return `${formattedHours}h ${formattedMins}m ${formattedSecs}s`
}

// timestamp => dd/mm/yyyy
export const timestampToDayMonthYear = (timestamp: number) => {
  const date = new Date(timestamp)
  const formattedDate = date.toLocaleDateString()
  return formattedDate
}

// ...
```

Nous pouvons maintenant créer un tableau et boucler sur `tasks` pour afficher les données dans les lignes du tableau. À la fin de chaque ligne, j'ai ajouté un bouton de suppression pour que l'utilisateur puisse supprimer définitivement des tâches de la base de données :

```tsx
// src/pages/stats.tsx

import { useState, useContext } from "react"
import type { NextPage } from "next"
import { UserContext } from "../contexts/UserContext"
import { TasksContext } from "../contexts/TasksContext"
import Header from "../components/PageHeading"
import Link from "../components/Link"
import Alert from "../components/Alert"
import { displayTimeString, timestampToDayMonthYear } from "../utils/formatTime"
import { harperDeleteTask } from "../utils/harperdb/deleteTask"

const Stats: NextPage = () => {
  const [errorMessage, setErrorMessage] = useState("")

  const { username } = useContext(UserContext)
  const { tasks, getAndSetTasks } = useContext(TasksContext)

  const handleDeleteRow = async (taskId: string) => {
    setErrorMessage("")
    const areYouSure = confirm("Are you sure you want to delete this row?")
    if (!areYouSure) return

    try {
      // Supprimer la tâche de la db
      const { response } = await harperDeleteTask(taskId)
      if (response.status === 200) {
        // Récupérer les tâches de la db et mettre à jour l'état
        getAndSetTasks(username)
        return
      }
    } catch (err) {
      console.log(err)
    }
    setErrorMessage("Whoops, something went wrong :(")
  }

  return (
    <div>
      {!username && (
        <Alert type="warning" extraClasses="mb-12">
          Please <Link href="/login">log in</Link> or{" "}
          <Link href="/signup">create an account</Link> to use Super
          Productivity Timer
        </Alert>
      )}

      <Header extraClasses="mb-6 text-center mt-8">Stats</Header>

      {errorMessage && (
        <p className="text-center text-red-500 mb-8">{errorMessage}</p>
      )}

      <div className="overflow-x-auto ">
        <table className="table-auto border-collapse border border-slate-400 w-full sm:w-3/4 mx-auto">
          <thead className="bg-slate-100 text-left">
            <tr>
              <TH>Task</TH>
              <TH>Total Time</TH>
              <TH>Last Updated</TH>
              <TH>Start Date</TH>
              <TH>Delete</TH>
            </tr>
          </thead>
          <tbody>
            {tasks.length > 0 &&
              tasks.map(task => (
                <tr key={task.id}>
                  <TD>{task.task_name}</TD>
                  <TD>{displayTimeString(task.time_in_seconds)}</TD>
                  <TD>{timestampToDayMonthYear(task.__updatedtime__)}</TD>
                  <TD>{timestampToDayMonthYear(task.__createdtime__)}</TD>
                  <TD>
                    <button
                      onClick={() => handleDeleteRow(task.id)}
                      className="bg-red-500 text-white rounded px-3 py-1"
                    >
                      x
                    </button>
                  </TD>
                </tr>
              ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

const TH: React.FC<{ children: string }> = ({ children }) => {
  const classes = "border border-slate-300 rounded-top p-4"
  return <th className={classes}>{children}</th>
}

interface TDProps {
  children: React.ReactNode
}
const TD = ({ children }: TDProps) => {
  const classes = "border border-slate-300 p-4"
  return <td className={classes}>{children}</td>
}

export default Stats
```

Et voici notre page de statistiques :

![Tableau de statistiques](https://www.freecodecamp.org/news/content/images/2022/03/stats_table.JPG)

Une dernière chose à faire : créer la fonction `harperDeleteTask` :

```ts
// src/utils/harperdb/deleteTask.ts

import { harperFetch } from "./harperFetch"

export const harperDeleteTask = async (taskId: string) => {
  const data = {
    operation: "delete",
    schema: "productivity_timer",
    table: "tasks",
    hash_values: [taskId],
  }

  const responseAndResult = await harperFetch(data)
  return responseAndResult
}
```

Maintenant, essayez de supprimer une tâche et vérifiez votre base de données – elle aura disparu. Parfait !

Essayez également d'ajouter une nouvelle tâche, puis d'enregistrer du temps. Allez ensuite sur la page des statistiques et vous verrez que la page est également mise à jour.

Vous savez maintenant comment construire une application full stack avec NextJS et HarperDB.

## Merci de m'avoir lu !

Si vous avez trouvé cet article utile, n'hésitez pas à :

- [Vous abonner à ma chaîne YouTube](https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA). Je prévois d'en faire une chaîne axée sur React/NextJS/Node.
- [Me suivre sur Twitter](https://twitter.com/doabledanny) où je tweete sur mon parcours de freelance, mes projets personnels et mes apprentissages actuels.


Santé !