---
title: Comment créer un site portfolio avec Next.js et TailwindCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-18T18:02:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-portfolio-site-with-nextjs-tailwindcss
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Blue-and-White-Modern-Corporate-Travel-YouTube-Thumbnail--3-.png
tags:
- name: Job Hunting
  slug: job-hunting
- name: Next.js
  slug: nextjs
- name: portfolio
  slug: portfolio
- name: projects
  slug: projects
- name: tailwind
  slug: tailwind
seo_title: Comment créer un site portfolio avec Next.js et TailwindCSS
seo_desc: "By Manu Arora\nIf you're a web developer, it's important for you to have\
  \ a personal portfolio website – especially when you're applying for jobs. \nIf\
  \ you have a nice online portfolio site, you'll have a better chance of getting\
  \ attention from recruite..."
---

Par Manu Arora

Si vous êtes un développeur web, il est important pour vous d'avoir un site web portfolio personnel – surtout lorsque vous postulez pour des emplois. 

Si vous avez un beau site portfolio en ligne, vous aurez plus de chances d'attirer l'attention des recruteurs que si vous n'en avez pas.

Au lieu d'envoyer votre CV et de demander à un recruteur de le consulter, un site web portfolio peut vous aider à vous démarquer en montrant directement vos compétences, vos projets, votre éducation et votre marque personnelle.

Vous pouvez utiliser votre portfolio pour présenter vos projets, votre éducation, partager des extraits de code réutilisables avec le monde, fournir des ressources utiles et écrire vos propres blogs. Il y a d'innombrables choses que vous pouvez faire avec votre propre site web.

J'ai créé un modèle que vous pouvez utiliser pour créer, modifier et déployer votre propre site web portfolio gratuitement sur internet en un rien de temps. Et si vous souhaitez construire votre propre version à partir de zéro, je vais vous montrer comment dans cet article.

Alors, plongeons-nous – je vais vous montrer quelle technologie j'ai utilisée, comment j'ai structuré le portfolio, et je vais le décomposer par section afin que vous puissiez voir comment chaque partie fonctionne. 

## Pile Technologique

Parlons de la pile technologique que j'ai utilisée pour construire ce modèle :

* **Next.js** - un framework React utilisé pour construire des sites web ultra-rapides avec un rendu côté serveur, ce qui facilite la découverte de votre site sur internet.
* **tailwindcss** - un framework CSS qui vous permet de prototyper et de styliser rapidement vos applications web.
* **Rough Notation** - une bibliothèque de style utilisée dans la section Hero, idéale pour mettre en évidence un texte important sur votre page web.

Pourquoi `Next.js` ? Parce que c'est un framework React avec `Server-Side Rendering`, ce qui est bon pour le SEO (Bon pour nous si nous sommes trouvés sur Google, n'est-ce pas ?).

De plus, Next.js nous aide à construire des sites web ultra-rapides avec des avantages tels que l'optimisation des images.

Pourquoi `tailwindcss` ? Parce que TailwindCSS est un framework qui réduit beaucoup d'efforts de stylisation. Il dispose de classes CSS de bas niveau que vous pouvez directement intégrer dans le code HTML.

Non seulement cela, il offre un support incroyable pour la réactivité. Par exemple, `<div className="text-sm md:text-xl"></div>` signifie que le texte sera `small` sur les petits écrans et `xl` sur les écrans moyens à grands.

Enfin, nous allons déployer l'application sur **Vercel**. Vercel nous offre un moyen facile de déployer notre application avec CI/CD. Le code est poussé vers un dépôt GitHub distant et à chaque push, il est déployé.

## Fonctionnalités du Site Portfolio

![websitegif-1](https://www.freecodecamp.org/news/content/images/2021/08/websitegif-1.gif)

Le site web inclut ce que je considère être le minimum absolu que vous devriez avoir dans votre site portfolio, ainsi que quelques fonctionnalités supplémentaires sympas à avoir.

* `Mode Sombre` - Comprend la prise en charge du mode sombre. Basculer le bouton de mode pour passer du mode sombre au mode clair.
* `Construire avec Next.js` - Le site web est construit avec Next.js qui offre des fonctionnalités incroyables telles que l'optimisation des images et la prise en charge du SEO.
* `Stylisation personnalisable` - En utilisant TailwindCSS, j'ai construit ce site web de manière à ce que vous puissiez personnaliser les couleurs principales et changer l'apparence de votre site web selon vos besoins.
* `Composant Meta personnalisé` - Chaque page est enveloppée avec une balise Meta Component que vous pouvez utiliser pour fournir des informations meta pour chaque page séparée que vous créez.
* `Design Réactif` - Les pages sont belles sur tous les appareils - desktop, tablette et mobile.


## Pages du Portfolio que nous allons Construire
Nous allons inclure toutes les pages nécessaires que vous devriez avoir dans votre site portfolio, telles que :

* `Page d'accueil` - Une page de destination pour le visiteur. C'est ce qu'ils verront lorsqu'ils atterriront sur votre site web.
* `À propos` - Une brève introduction qui inclut ce que vous faites, vos compétences techniques et vos liens sociaux.
* `Expérience` - Un historique de votre travail, vos projets personnels que vous avez entrepris et vos projets pertinents.
* `Projets` - Une grille de tous les projets que vous avez construits.
* `Contact` - Un formulaire où le recruteur / utilisateur final peut vous contacter.



## Composants et Dispositions

L'ensemble du site web est divisé en composants – de petits morceaux de code réutilisables que vous pouvez utiliser n'importe où sur la page web. La structure des dossiers est assez simple et auto-explicative :

* `components` est l'endroit où vivent tous les composants, comme la section hero, la navbar et les dispositions.
* `public` est l'endroit où vont tous vos actifs statiques, comme les images, les polices et/ou tout script externe pour générer des sitemaps dynamiques.
* `styles` est l'endroit où vit votre stylisation globale. Nous allons intégrer la bibliothèque de base de Tailwind ici.
* `pages` est l'endroit où vivent toutes vos routes, et c'est l'une des meilleures fonctionnalités de Next.js. Il suffit de créer un nouveau fichier dans le dossier `pages` et il servira de nouvelle route.

### Bloc Conteneur

`<ContainerBlock />` est le parent de tous les composants. Il fournit un moyen pour l'utilisateur d'avoir des balises meta personnalisées pour chaque page. J'ai conçu la disposition de manière à ce qu'elle accepte des props en tant qu'`children` et fournisse une `Navbar`, des balises `<meta>` et un `Footer` pour chaque page.

```javascript
import React from "react";
import Head from "next/head";
import { useRouter } from "next/router";
import Navbar from "./Navbar";
import Footer from "./Footer";

export default function ContainerBlock({ children, ...customMeta }) {
  const router = useRouter();

  const meta = {
    title: "Manu Arora - Développeur, Écrivain, Créateur et YouTubeur",
    description: `Je développe des sites web depuis 5 ans. Contactez-moi pour en savoir plus.`,
    image: "/avatar.png",
    type: "website",
    ...customMeta,
  };
  return (
    <div>
      <Head>
        <title>{meta.title}</title>
        <meta name="robots" content="follow, index" />
        <meta content={meta.description} name="description" />
        <meta
          property="og:url"
          content={`https://votresite.com${router.asPath}`}
        />
        <link
          rel="canonical"
          href={`https://votresite.com${router.asPath}`}
        />
        <meta property="og:type" content={meta.type} />
        <meta property="og:site_name" content="Manu Arora" />
        <meta property="og:description" content={meta.description} />
        <meta property="og:title" content={meta.title} />
        <meta property="og:image" content={meta.image} />
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:site" content="@mannupaaji" />
        <meta name="twitter:title" content={meta.title} />
        <meta name="twitter:description" content={meta.description} />
        <meta name="twitter:image" content={meta.image} />
        {meta.date && (
          <meta property="article:published_time" content={meta.date} />
        )}
      </Head>
      <main className="dark:bg-gray-800 w-full">
        <Navbar />
        <div>{children}</div>
        <Footer />
      </main>
    </div>
  );
}

```

Après avoir créé `ContainerBlock.js`, vous pouvez simplement envelopper votre composant de page dans une balise `ContainerBlock`, en fournissant des balises meta pour `title`, `description` et `image` :

```javascript
import Head from "next/head";
import styles from "../styles/Home.module.css";
import ContainerBlock from "../components/ContainerBlock";
import FavouriteProjects from "../components/FavouriteProjects";
import LatestCode from "../components/LatestCode";
import Hero from "../components/Hero";

export default function Home() {
  return (
    <ContainerBlock
      title="Manu Arora - Développeur, Écrivain, Créateur"
      description="Construire un modèle avec Next.js et Tailwindcss - pour les utilisateurs de FreeCodeCamp."
    >
      <Hero />
      <FavouriteProjects />
      <LatestCode />
    </ContainerBlock>
  );
}

```

## Comment Activer le Mode Sombre

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-9.09.35-AM.png)

La prise en charge du mode sombre est fournie par un package `npm` appelé `next-themes`. Le but est d'envelopper le conteneur parent avec un fournisseur `ThemeProvider` à travers lequel le `theme` est disponible pour les enfants à tout moment.

**_app.js**

```js
import "../styles/globals.css";
import { ThemeProvider } from "next-themes";

function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider defaultTheme="light" attribute="class">
      <Component {...pageProps} />
    </ThemeProvider>
  );
}

export default MyApp;

```



![Image](https://www.freecodecamp.org/news/content/images/2021/08/Copy-of-Untitled--6--1.png)

Pour basculer le thème entre le mode clair et le mode sombre, nous avons besoin d'un bouton. Vous pouvez réutiliser ce bouton n'importe où dans l'application, mais nous allons l'intégrer dans la `Navbar` afin qu'il soit disponible pour l'utilisateur final à tout moment.

**Navbar.js**

```js
import React, { useEffect, useState } from "react";
import Link from "next/link";
import { useTheme } from "next-themes";
import { useRouter } from "next/router";

export default function Navbar() {
  const router = useRouter();
  console.log(router.asPath);
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div className="max-w-6xl  mx-auto px-4 py-10 md:py-20">
      <div className="flex  md:flex-row justify-between items-center">
        {/* Logo / Home / Text */}
		 // Reste du code
          <button
            aria-label="Toggle Dark Mode"
            type="button"
            className="w-10 h-10 p-3 rounded focus:outline-none"
            onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
          >
            {mounted && (
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="currentColor"
                stroke="currentColor"
                className="w-4 h-4 text-yellow-500 dark:text-yellow-500"
              >
                {theme === "dark" ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                  />
                )}
              </svg>
            )}
          </button>
        </div>
      </div>
     //Reste du code
  );
}
```

Une fois le bouton cliqué, le thème change. Plutôt cool, n'est-ce pas ? 😊

## Comment Construire la Section Hero

![hero](https://www.freecodecamp.org/news/content/images/2021/08/hero.png)

La section hero vous permet d'attirer l'attention des gens. Si vous le faites bien, cela peut vous aider à décrocher votre premier emploi.

J'ai utilisé `react-rough-notation`, une bibliothèque qui met dynamiquement en évidence le texte avec différentes couleurs et délais.

Le bon côté de cet effet est que l'utilisateur final prête immédiatement attention au texte qui est mis en évidence. Vous pouvez mettre votre meilleur pied en avant ici et leur dire QUI vous êtes et CE que vous faites.

Le code pour `rough-notation` est simple : nous enveloppons le texte à mettre en évidence dans les balises `<RoughNotationGroup>` et `<RoughNotation>` avec des paramètres supplémentaires tels que les couleurs et les délais.

Ici, je vais créer un composant personnalisé appelé `RainbowHighlight` qui prend une couleur et met en évidence le texte enfermé qui peut être utilisé partout.

**RainbowHighlight.js**

```js
import React from "react";
import { RoughNotation } from "react-rough-notation";

export const RainbowHighlight = ({ color, children }) => {
  // Change la durée de l'animation en fonction de la longueur du texte que nous animons (vitesse = distance / temps)
  const animationDuration = Math.floor(30 * children.length);

  return (
    <RoughNotation
      type="highlight"
      multiline={true}
      padding={[0, 2]}
      iterations={1}
      animationDuration={animationDuration}
      color={color}
    >
      {children}
    </RoughNotation>
  );
};

```

**Hero.js**

```js
import React from "react";
import { RoughNotation, RoughNotationGroup } from "react-rough-notation";
import { RainbowHighlight } from "./RainbowHighlight";

export default function Hero() {
  const colors = ["#F59E0B", "#84CC16", "#10B981", "#3B82F6"];
  return (
    <div className="flex flex-row justify-center items-start overflow-hidden">
      {/* Conteneur de texte */}

      <div className="w-full md:w-1/2 mx-auto text-center md:text-left lg:p-20">
        <RoughNotationGroup show={true}>
          <RainbowHighlight color={colors[0]}>
            <h1 className="text-4xl md:text-8xl font-bold text-gray-700 dark:text-gray-200 my-2">
              Développeur.
            </h1>
          </RainbowHighlight>
       <RoughNotationGroup>
     </div>
     ....
     ....
     ....
   );

```

## Comment Récupérer les Derniers Dépôts de GitHub

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-9.09.35-AM-1.png)

Récupérer les dépôts avec l'[API GitHub](https://docs.github.com/en/rest) est assez facile.

L'API GitHub offre une possibilité de récupérer les dépôts avec le champ `updated_time` en ordre décroissant, afin que nous obtenions les derniers dépôts.

```js
 const res = await axios.get(
      `https://api.github.com/search/repositories?q=user:${username}+sort:author-date-asc`
    );
```

Une fois que nous avons récupéré le dernier dépôt, nous `slicons` le tableau pour ne prendre en compte que les 6 dépôts les plus récents.

```js
let repos = res.data.items;
    let latestSixRepos = repos.splice(0, 6);
    return latestSixRepos;
```

Ainsi, la fonction entière ressemble à ceci :

**getLatestRepos.js**

```js
import axios from "axios";

const getLatestRepos = async (data) => {
  console.log("data", data);
  try {
    const username = data.githubUsername;

    const res = await axios.get(
      `https://api.github.com/search/repositories?q=user:${username}+sort:author-date-asc`
    );

    let repos = res.data.items;
    let latestSixRepos = repos.splice(0, 6);
    return latestSixRepos;
  } catch (err) {
    console.log(err);
  }
};

export default getLatestRepos;

```

Une fois les données récupérées à partir de la fonction, nous pouvons ensuite les utiliser à l'intérieur de notre composant React `<GetReposCard />` et passer les paramètres en conséquence.

```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto px-10 lg:-mt-10 gap-y-20">
        {/* Single github Repo */}

        {repos &&
          repos.map((latestRepo, idx) => (
            <GithubRepoCard latestRepo={latestRepo} key="idx" />
          ))}
      </div>
```

```jsx
const GithubRepoCard = ({ latestRepo }) => {
  return (
    <div className="github-repo">
      <h1 className="font-semibold text-xl dark:text-gray-200 text-gray-700">
        {latestRepo.name}
      </h1>
      <p className="text-base font-normal my-4 text-gray-500">
        {latestRepo.description}
      </p>
      <a
        href={latestRepo.clone_url}
        className="font-semibold group flex flex-row space-x-2 w-full items-center"
      >
        <p>Voir le Dépôt </p>
        <div className="transform  group-hover:translate-x-2 transition duration-300">
          &rarr;
        </div>
      </a>
    </div>
  );
};

```

Il y a un petit problème ici – l'API GitHub ne fournit qu'un nombre limité d'appels par adresse IP.

Pour résoudre ce problème, on peut créer une application GitHub et générer des `Auth Tokens`, que nous pouvons intégrer avec la requête de l'API GitHub et vous obtiendrez plus de requêtes par adresse IP. Vous pouvez [lire la documentation ici](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) pour plus d'informations à ce sujet.

## Comment Inclure des Projets dans Votre Portfolio

![projects](https://www.freecodecamp.org/news/content/images/2021/08/projects.png)

J'ai gardé la section des projets aussi simple que possible avec une grande zone d'image, car le recruteur / utilisateur final est surtout intéressé à voir ce que vous avez fait. Si cela a l'air bien, vous avez déjà un avantage.

J'ai divisé la page en `grilles` Tailwind de deux colonnes, qui se brisent sur les écrans mobiles en 1 colonne.

Le conteneur d'image contient un texte d'en-tête qui affiche le nom du projet et un numéro en bas.

Les animations de survol sur les images sont subtiles. L'image s'agrandit lentement pour attirer l'attention de l'utilisateur. Au clic, elle emmène l'utilisateur vers le site web en direct / le dépôt GitHub du projet.

```js
  
import React from "react";

export default function Projects() {
  return (
    <section className="bg-white dark:bg-gray-800">
      <div className="max-w-6xl mx-auto h-48 bg-white dark:bg-gray-800">
        <h1 className=" text-5xl md:text-9xl font-bold py-20 text-center md:text-left">
          Projets
        </h1>
      </div>
      {/* La grille commence ici */}
      <div className="bg-[#F1F1F1] dark:bg-gray-900">
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 py-20 pb-40">
          {/* Carte unique */}
          <a
            href="https://tailwindmasterkit.com"
            className="w-full block shadow-2xl"
          >
            <div className="relative overflow-hidden">
              <img
                src="/tmk.jpg"
                alt="portfolio"
                className="transform hover:scale-125 transition duration-2000 ease-out"
              />
              <h1 className="absolute top-10 left-10 text-gray-50 font-bold text-xl bg-red-500 rounded-md px-2">
                Tailwind Master Kit
              </h1>
              <h1 className="absolute bottom-10 left-10 text-gray-50 font-bold text-xl">
                01
              </h1>
            </div>
          </a>
        </div>
      </div>
    </section>
    ...
    ...
    ...
  );

```

## Comment Construire la Page de Contact

![contact](https://www.freecodecamp.org/news/content/images/2021/08/contact.png)

J'ai pris la section de contact directement depuis [Tailwind Master Kit](http://tailwindmasterkit.com), qui est un marché de composants et de modèles pour les projets d'applications web Tailwind. Je ne voulais pas passer plus de temps à styliser un formulaire de contact moi-même et j'ai utilisé un peu d'aide.

Le composant est absolument gratuit et vous pouvez l'intégrer facilement dans les sites web liés à Tailwind.

**Contact.js**

```js
import React from "react";

export default function Contact() {
  return (
    <section>
      <div className="max-w-6xl mx-auto h-48 bg-white dark:bg-gray-800 antialiased">
        <h1 className=" text-5xl md:text-9xl font-bold py-20 text-center md:text-left">
          Contact
        </h1>
      </div>
      <div className="relative z-10 rounded-md shadow-md bg-[#02044A] p-4 md:p-10 lg:p-20 max-w-6xl mx-auto mb-20 -mt-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="md:ml-4">
            <header className="">
              <h1 className="text-gray-50 font-semibold text-2xl">
                Contactez-moi, parlons-en.
              </h1>
              <p className="font-light text-base text-gray-200 mt-2">
                Remplissez les détails et je vous recontacterai dès que possible.
              </p>
            </header>
            <div className="icons-container inline-flex flex-col my-20">
              <div className="flex flex-row items-center space-x-6 rounded-md border border-[#02044A] hover:border hover:border-blue-500 p-4">
                
                <p className="text-gray-50 font-light text-sm">
                  +91 9987384723
                </p>
              </div>
              <div className="flex flex-row items-center space-x-6 rounded-md border border-[#02044A] hover:border hover:border-blue-500 p-4">
                ....
                ....
                <p className="text-gray-50 font-light text-sm">
                  contact@votresite.com
                </p>
              </div>
              <div className="flex flex-row items-center space-x-6 rounded-md border border-[#02044A] hover:border hover:border-blue-500 p-4">
                ....
                ....
          <form className="form rounded-lg bg-white p-4 flex flex-col">
            <label htmlFor="name" className="text-sm text-gray-600 mx-4">
              {" "}
              Votre Nom
            </label>
            <input
              type="text"
              className="font-light rounded-md border focus:outline-none py-2 mt-2 px-1 mx-4 focus:ring-2 focus:border-none ring-blue-500"
              name="name"
            />
            <label htmlFor="email" className="text-sm text-gray-600 mx-4 mt-4">
              Email
            </label>
            <input
              type="text"
              className="font-light rounded-md border focus:outline-none py-2 mt-2 px-1 mx-4 focus:ring-2 focus:border-none ring-blue-500"
              name="email"
            />
            <button
              type="submit"
              className="bg-blue-500 rounded-md w-1/2 mx-4 mt-8 py-2 text-gray-50 text-xs font-bold"
            >
              Envoyer le Message
            </button>
          </form>
        </div>
      </div>
    </section>
  );
}

```

## Comment Déployer le Portfolio
Déployer l'application est assez simple et ne prend que 8 étapes simples.

1.  Clonez le dépôt
```bash
git clone https://github.com/manuarora700/simple-developer-portfolio-website
```

2. Installez les dépendances

```bash
npm install
```

3. Démarrez le serveur de développement local

```bash
npm run dev
```

4. Apportes des modifications au site web. Vous devriez inclure tous vos projets, votre éducation, vos liens sociaux et les informations Meta.

5. Poussez le code vers votre dépôt distant

```bash
git add *
git commit -m "ajouter des modifications au dépôt clonné"
git push
```

6. Créez un compte Vercel (ou connectez-vous à votre compte Vercel) 

7. Ajoutez le nouveau dépôt GitHub créé avec les modifications poussées et Vercel le déployera automatiquement pour vous sur un lien.

![vercel](https://www.freecodecamp.org/news/content/images/2021/08/vercel.png)

8. Une fois le site en ligne, partagez le lien de test avec vos amis ou ajoutez-le dans votre CV. Vous pouvez également aller de l'avant et connecter un domaine personnalisé pour le rendre plus professionnel.

## Conclusion

Ce site portfolio donnera à un recruteur ou à un visiteur tout ce qu'ils recherchent s'ils veulent en savoir plus sur vous et votre travail. L'objectif de votre portfolio devrait être de mettre en valeur vos compétences de la meilleure façon possible.

De plus, nous avons construit le site avec `Next.js`, ce qui montre que vous êtes à l'aise avec React et ses frameworks. (Les recruteurs vous recherchent ! 😊)

Le site utilise `tailwindcss` pour le style, ce qui montre que vous pouvez travailler avec un framework CSS et réduire le temps de style.

Les composants sont granulaires et chacun sert son propre but. La structure des dossiers est simple et facile à comprendre.

Vous pouvez personnaliser le site web de la manière que vous souhaitez - je l'ai open sourcé et le code est lié au dépôt GitHub ci-dessous.

Mon [site web personnel](https://manuarora.in) m'a aidé à décrocher des entretiens dans de grandes entreprises technologiques et c'est l'une des principales raisons pour lesquelles j'ai pu obtenir un emploi (en plus de m'entraîner sur freeCodeCamp et d'apprendre à coder).

J'ai vraiment apprécié construire ce site web. Si vous l'avez aimé, laissez une étoile sur le dépôt GitHub et aidez à faire passer le mot. ⭐️

#### Code Source et Démo en Direct

[Code Source](https://github.com/manuarora700/simple-developer-portfolio-website)  
[Démo en Direct](https://simple-developer-portfolio-website.vercel.app/)