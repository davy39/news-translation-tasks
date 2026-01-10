---
title: Comment j'ai rendu mon site portfolio ultra-rapide avec Gatsby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-12T19:25:48.000Z'
originalURL: https://freecodecamp.org/news/how-i-made-my-portfolio-website-blazing-fast-with-gatsby-82ccddc2f671
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lJOurCBMozvgBjmxG-Ljiw.jpeg
tags:
- name: GatsbyJS
  slug: gatsbyjs
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: Comment j'ai rendu mon site portfolio ultra-rapide avec Gatsby
seo_desc: "By Maribel Duran\nIf you are thinking of building a static site with React\
  \ and want it to perform as fast as a cheetah, you should consider using GatsbyJS.\
  \ \nI decided to try it out and was amazed with how easy it was to setup, deploy,\
  \ and how fast the..."
---

Par Maribel Duran

Si vous envisagez de créer un site statique avec React et que vous souhaitez qu'il soit aussi rapide qu'un guépard, vous devriez envisager d'utiliser GatsbyJS.

J'ai décidé de l'essayer et j'ai été émerveillée par la facilité de configuration, de déploiement et par la rapidité de chargement du site. Gatsby utilise les meilleurs éléments d'autres outils front-end pour rendre l'expérience de développement aussi agréable que des vacances.

![Image](https://cdn-media-1.freecodecamp.org/images/drwxddrKcWMNLOQ0Vc0Th9-DH2BAtln6DfzA)
_Après avoir reconstruit mon site web avec Gatsby et React ?_

### **Problèmes de performance avec le site web original**

Je devais optimiser les images de mon site portfolio, qui était l'un de mes premiers projets de développement frontend freeCodeCamp.

![Image](https://cdn-media-1.freecodecamp.org/images/ZAKgKErGeMpDsVyLQi9MUYZeV6nchQeK95Z3)
_Avant l'aide de Gatsby -_-_

Aïe ! Un score d'optimisation Google de 33/100 était douloureux à voir. Oui, j'avais besoin d'aide des dieux de l'optimisation. Mon site contenait au moins 17 captures d'écran de projets. Je ne voulais pas avoir à compresser chaque image, générer plusieurs tailles et résolutions de chaque image, et les charger paresseusement.

Lorsque j'ai créé ce site pour la première fois, la classe `img-responsive` de Bootstrap 3 s'occupait de redimensionner les images pour les adapter à différentes tailles d'écran, mais je n'avais pas pensé au fait qu'il chargeait encore certaines de mes captures d'écran d'environ 1400 x 860 pixels sur les appareils mobiles !

Mon score était également faible parce que je n'avais pas minifié mon CSS ni configuré la mise en cache du navigateur pour celui-ci, et je ne chargeais pas de manière asynchrone les ressources CSS externes.

### **Gatsby à la rescousse**

Je voulais vraiment reconstruire ce projet en utilisant React. J'aurais pu utiliser [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) qui fournit un script de construction et un serveur de développement prêts à l'emploi, mais cela ne résolvait toujours pas la longue tâche de devoir recadrer différentes tailles d'images pour toutes mes images.

Heureusement, j'écoutais [Syntax](https://syntax.fm/), « Pourquoi les générateurs de sites statiques sont géniaux » [épisode](https://syntax.fm/show/034/why-static-site-generators-are-awesome), et ils parlaient de quelques générateurs de sites statiques sur la liste [StaticGen.com](https://www.staticgen.com/). Si vous ne savez pas ce que font les générateurs de sites statiques, ils transforment votre site en un répertoire avec un seul fichier HTML et des actifs statiques. Aucune base de données ou code serveur nécessaire.

Gatsby m'a convaincu en raison des similitudes qu'il partage avec create-react-app, qui inclut le rechargement à chaud, une configuration facile de l'environnement de développement et un script de construction. Gatsby va plus loin en offrant un rendu côté serveur, un chargement intelligent des images et un engagement envers la performance.

Puisque Gatsby est construit sur la pile React, GraphQL et Webpack, nous pouvons écrire notre contenu sous forme de composants React ! Gagnant ! Gatsby s'occupe du rendu au moment de la construction vers le DOM en tant que HTML, CSS et JavaScript statiques.

### Le composant Gatsby-image est BAE

Venons-en maintenant à ce que je voulais vraiment partager avec vous. Gatsby-image ! [Gatsby-image](https://www.gatsbyjs.org/packages/gatsby-image/), est un composant React conçu pour fonctionner avec les requêtes GraphQL de Gatsby afin d'optimiser complètement le chargement des images pour les sites.

L'approche consiste à utiliser des requêtes GraphQL pour obtenir des images de la taille optimale, puis à les afficher avec le composant gatsby-image.

Comment ai-je utilisé ce composant pour créer automatiquement 3 miniatures pour chacune de mes 17 images de projet ? De la magie ! Pas vraiment, mais cela y ressemble !

Dans mon fichier src/pages/index.js, j'ai interrogé toutes les images de projet et je leur ai donné un alias **ProjectImgs**. Puisque les données interrogées sont maintenant accessibles via l'objet data en tant que prop, j'ai pu transmettre les données **projectImgData** (qui est une liste de nœuds de mes images de projet) à mon composant `<Projects />` :

```
//imports
const HomePage = ({ data }) => {
  const siteTitle = data.site.siteMetadata.title;
  console.log(data.ProjectImgs); 
  const { edges: projectImgData } = data.ProjectImgs;
  const { edges: iconImgData } = data.iconImgs;
  return (
    <div>
     <Helmet
      title={siteTitle}
      link={[{ rel: "icon", type: "image/png", href: `${favicon}`}]}
     />
     <Cover coverImg={data.coverImg} />
     <div className="container-fluid main">
      <Navigation />
      <AboutMe profileImg={data.profileImg} iconImgs={iconImgData} 
      />                
     <Projects projectImgs={projectImgData} />
     <Contacts />
     <Footer />
     </div>
    </div>
  );
};
export const query = graphql`
  query allImgsQuery {
    //requêtes supplémentaires
    ...
    ProjectImgs: allFile(
      sort: { order: ASC, fields: [absolutePath] }
      filter: { relativePath: { regex: "/projects/.*.png/" } }
    ) {
      edges {
        node {
          relativePath
          name
          childImageSharp {
            sizes(maxWidth: 320) {
              ...GatsbyImageSharpSizes
            }
          }
        }
      }
    }
//requêtes supplémentaires
...
  }
`;
```

> Note : J'ai eu quelques difficultés à faire fonctionner mes requêtes graphQL et j'ai dû faire quelques recherches pour comprendre comment interroger plusieurs images dans un dossier. Ce qui m'a aidé, c'est de regarder d'autres sites portfolio réalisés avec Gatsby.

En utilisant la console, nous pouvons voir ce que `data.ProjectImgs` retourne pour vous donner une meilleure idée de ce que je reçois de la requête et de ce que je transmets à mon composant Projects :

`Console.log(data.ProjectImgs)` retourne un tableau de edges :

```
{edges: Array(17)}
edges
:
(17) [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
__proto__
:
Object{edges: Array(17)}
```

En étendant l'un des edges, on voit un objet node qui contient une propriété **childImageSharp**. Celui-ci contient un objet sizes qui détient les sources de miniature de l'image. Cet objet sizes est ce que nous voulons finalement passer à notre composant `<Img />` de gatsby-image.

Étendre un edge pour montrer les informations dans un node :

```
{edges: Array(17)}
 edges: Array(17)
 0:
  node:
   childImageSharp: {sizes: {}}
   name: "CamperLeaderboard"
   relativePath:"projects/CamperLeaderboard.png"
   __proto__:Object
   __proto__:Object
 1:{node: {}}
//plus de nodes
...
```

Dans mon composant `<Projects />`, je reçois la liste de nœuds des images de projet en tant que prop et pour chaque projet, j'extrais l'objet **childImageSharp.sizes** (qui est renommé en **imageSizes**), et je le passe dans le composant `<Img />` de gatsby-image :

```
import React, { Component } from "react";
import Img from "gatsby-image";
//plus d'imports
...
class Projects extends Component {
  constructor(props) {
    super(props);
  this.state = {
      selectedType: "front-end"
   };
  this.onSelectChange = this.onSelectChange.bind(this);
  }
 
  onSelectChange(e) {
    this.setState({ selectedType: e.target.value });
 }
render() {
    const projectImgs = this.props.projectImgs;
    const { selectedType } = this.state;
    return (
      <section id="projects" className="section projects">
        <h2 className="text-center">PROJETS</h2>
        <div className="section-content">
          <div className="subheader">
            <FormGroup controlId="formControlsSelect">
             ...
            </FormGroup>
          </div>
          <div className="project-list">
            {projectList.map(project => {
              const isSelectedType = selectedType === project.type;
              const singleCardClass = classNames("single-card", {
                hide: !isSelectedType
               });
              const image = projectImgs.find(n => {
                return n.node.relativePath === 
                       `projects/${project.img}`;       
              });
              const imageSizes = image.node.childImageSharp.sizes;
              return (
                <a
                  href={project.url}
                  key={project.url}
                  className={singleCardClass}
                  target="_blank"
                >
                  <div className="card-img">
                    <Img
                      title={project.name}
                      alt="Capture d'écran du projet"
                      sizes={imageSizes}
                      className="card-img_src center-block"
                    />
                  </div>
                  <div className="blue-divider" />
                  <div className="card-info">
                    <h4 className="card-name">{project.name}</h4>
                    <p>{project.description}</p>
                  </div>
                </a>
              );
            })}
          </div>
        </div>
      </section>
    );
  }
}
export default Projects;
```

Et voici le résultat final :

![Image](https://cdn-media-1.freecodecamp.org/images/01dWYR9uwENmj6xQcoA-5uhSqdXywSDUMCyH)
_Exemple de chargement paresseux et d'effet de flou utilisant gatsby-image dans un réseau 3G lent_

C'est tout ! Le composant `<Img />` s'occupe d'utiliser la bonne taille d'image, de créer les effets de flou et de charger paresseusement mes images de projet, puisque elles sont situées plus bas sur l'écran. La requête ci-dessus était un peu plus complexe que la requête d'une seule image.

Si vous êtes nouveau dans GraphQL, voici quelques ressources qui expliquent mieux comment utiliser les requêtes GraphQL et le composant gatsby-image :

* [Travailler avec des images dans Gatsby](https://www.gatsbyjs.org/docs/working-with-images/)
* [gatsby-image](https://www.gatsbyjs.org/packages/gatsby-image/)
* [Optimisation d'images facilitée avec Gatsby.js](https://medium.com/@kyle.robert.gill/ridiculously-easy-image-optimization-with-gatsby-js-59d48e15db6e)

### **L'hébergement sur Netlify a été un jeu d'enfant**

Puisque Gatsby génère des fichiers statiques, vous pouvez utiliser presque n'importe quel fournisseur d'hébergement. J'ai décidé de changer mon fournisseur d'hébergement de GitHub Pages à Netlify. J'avais entendu dire à quel point il était facile de déployer un site web sur Netlify et ils ne mentaient pas. Leur niveau gratuit offre des fonctionnalités géniales qui rendent le processus de déploiement et la sécurisation d'un site web un jeu d'enfant. Il offre un HTTPS en un clic, un CDN global, un déploiement continu, et la liste est longue.

Le processus de configuration était si simple. Je me suis connectée à Netlify, j'ai cliqué sur le bouton « Nouveau site depuis Git » sur mon tableau de bord, et j'ai choisi le dépôt Git pour ce projet. J'ai configuré le site pour qu'il se déploie depuis la branche master et j'ai cliqué sur « Déployer le site ». C'était tout ! Netlify s'occupe du processus de construction et le publie sur le web.

Comme je l'ai mentionné, Netlify offre un déploiement continu, donc maintenant, chaque fois que je pousse des changements vers ma branche master sur GitHub, cela déclenche automatiquement une nouvelle construction sur Netlify. Une fois la construction terminée, mes changements seront en ligne sur le web.

![Image](https://cdn-media-1.freecodecamp.org/images/sslrobbMI6Gv3V0fhuG0AQyX6wpBjKY9Fmqy)
_Le paramètre de déploiement est défini sur la publication automatique_

### **L'avenir semble radieux**

En reconstruisant mon site web avec Gatsby, non seulement j'ai appris différentes techniques d'optimisation d'images pour les projets futurs, mais j'ai également appris un peu sur GraphQL, pratiqué mes compétences React et saisi l'opportunité d'essayer un nouveau fournisseur d'hébergement.

Je suis vraiment enthousiaste pour l'avenir de Gatsby et des outils front-end similaires qui éliminent les complexités de configuration des environnements et des outils de construction. Au lieu de cela, nous pouvons concentrer notre énergie et notre temps sur notre code pour construire des choses géniales pour nos utilisateurs.

> Si vous avez aimé cet article, cliquez sur le ? ci-dessous pour que d'autres personnes puissent le voir ici sur Medium.  
>   
> Soyons amis sur [Twitter](https://twitter.com/maribeldotduran). Bon codage :)