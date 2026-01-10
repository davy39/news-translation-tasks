---
title: Tendances du développement Front End à surveiller en 2022
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-02-08T19:13:00.000Z'
originalURL: https://freecodecamp.org/news/front-end-development-trends
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/shutterstock_1610721214-min.jpg
tags:
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Tendances du développement Front End à surveiller en 2022
seo_desc: 'By Adam Zaczek

  Front end development hasn''t always gotten the respect it deserves compared to
  back end development.

  Many engineers used to look down on JavaScript. But times have changed. Web applications
  are growing rapidly, mainly due to the develo...'
---

Par Adam Zaczek

Le développement front end n'a pas toujours reçu le respect qu'il mérite par rapport au développement back end.

De nombreux ingénieurs méprisaient autrefois JavaScript. Mais les temps ont changé. Les applications web se développent rapidement, principalement grâce au développement d'outils open-source.

Cette évolution nous a éloignés de jQuery et a fait que presque toutes les entreprises technologiques utilisent le dernier JavaScript et des outils comme Eslint, Babel et Webpack.

De nos jours, le front end évolue à une vitesse qui rend difficile le suivi.

Cet article traite de rattraper les directions de ce domaine de développement en 2022. Peut-être trouverez-vous quelque chose pour vous dans ces tendances.

## Svelte gagne en popularité

Svelte est un outil relativement nouveau, qui en théorie a commencé beaucoup trop tard pour avoir une chance contre React, Vue et Angular. Mais il gagne régulièrement en popularité à un rythme sans précédent.

En 2021, les utilisateurs de StackOverflow [l'ont annoncé comme le framework front-end le plus apprécié](https://insights.stackoverflow.com/survey/2021#technology-most-loved-dreaded-and-wanted).

Mais Svelte est plus que cela. C'est un compilateur qui construit un front end optimisé. 
Svelte n'est pas importé dans l'application comme les autres frameworks populaires. Au lieu de cela, le code écrit en Svelte est compilé en JavaScript pur. Cela permet à Svelte de gagner en termes de vitesse contre des frameworks tels que React ou Vue.  
  
L'utilisation du framework Svelte est très facile. Voici un exemple de la façon dont vous utiliseriez l'état + les formulaires :

```JavaScript
L'utilisation du framework est très facile. Voici un exemple d'utilisation de l'état + des formulaires.
<script>
 let a = 1;
 let b = 2;
</script>
 
<label>
 <input type=number bind:value={a} min=0 max=10>
 <input type=range bind:value={a} min=0 max=10>
</label>
 
<label>
 <input type=number bind:value={b} min=0 max=10>
 <input type=range bind:value={b} min=0 max=10>
</label>
 
<p>{a} + {b} = {a + b}</p>
```

C'est aussi simple que cela ! Remarquez trois choses ici :

1. Les formulaires sont gérés de manière simple et élégante, comme dans le bon vieux temps, avant les frameworks SPA. Il n'est pas nécessaire d'attacher des props onChange aux entrées.
2. Le balisage et la logique coexistent, encapsulant la logique et une couche visible.
3. L'état est facile à gérer.

Pas étonnant que le framework gagne du terrain dans la communauté. Ce n'est qu'une question de temps avant que de nouvelles plateformes populaires soient créées en Svelte.

## React, Vue et Angular sont là pour rester

J'ai commencé mon aventure avec le front end juste avant la sortie d'Angular 2, il y a environ six ans. Je ne peux pas compter le nombre de fois où j'ai lu depuis que Vue, React ou Angular était en train de mourir.

La vérité s'est avérée être assez différente, cependant. Chacun de ces trois frameworks a gagné en popularité depuis sa création.

Voici le graphique ([Source : Npm Trends](https://www.npmtrends.com/react-vs-vue-vs-@angular/core)). Il est intéressant d'ajouter que chaque chute soudaine sur le graphique est due à décembre.

![Image](https://lh6.googleusercontent.com/ilDTORi3UIlBJdZXPoQ5u9Y2SQbLdhXeJXLHt_KaRKT-BGKv1WZEYuHnQEDk73ZTfKdUUANCMIHljewTGACDB_6xma8ISwzAV-cU50mj2YJ0L0yAsN_hhF28XRJA9bVRtuVtyCeO)
_Tendances de téléchargement Angular vs React vs Vue_

Jetez un coup d'œil au graphique ci-dessus. Remarquez qu'Angular a gagné en popularité d'un facteur de plus de dix. React et Vue ont crû encore plus vite. Les trois frameworks supportent pratiquement les mêmes cas d'utilisation.

Cela signifie que peu importe lequel des trois frameworks vous choisissez, vous pouvez vous attendre à ce qu'il soit utilisé et supporté pendant des années.

Il est intéressant de noter que React n'a pas eu de changements significatifs en 2021. Pourtant, le rythme de son adaptation est stupéfiant. C'est probablement grâce à l'écosystème autour de la technologie. React a la plus grande sélection de bibliothèques et de frameworks de support.

Deux exemples valent la peine d'être mentionnés : Next et Gatsby. Ce dernier est l'un des instigateurs de la prochaine tendance.

## Les frameworks doivent supporter à la fois les pages statiques et dynamiques

Établissons ce que sont les pages statiques et dynamiques en termes pratiques.

Les pages dynamiques récupèrent et traitent le contenu lorsque l'utilisateur les ouvre. Les pages statiques sont prédéfinies lors de la construction. Elles deviennent des fichiers générés séparés sur le disque. Elles peuvent avoir la même apparence que les pages dynamiques, mais le navigateur de l'utilisateur a moins de travail à faire.

Si vous avez une boutique, vous pouvez avoir une seule page de produit dynamique, ou des milliers de pages de produits statiques, une pour chaque produit.

Cela signifie que les pages statiques sont plus performantes pour les utilisateurs, mais prennent beaucoup plus de temps à construire.

La raison de l'abandon des pages statiques était la popularisation des frameworks de type single-page application (SPA) comme React et Vue. Ils les ont également remis au goût du jour.

Le contenu dynamique que les SPA génèrent typiquement est beaucoup plus lent qu'un contenu prêt à être affiché écrit en HTML. La différence est particulièrement grande lorsque la page récupère des données depuis le serveur. Une page dynamique devrait typiquement télécharger et traiter de telles données.

Cela a abouti à la renaissance des pages statiques dans les SPA. Gatsby a abordé ce problème en construisant un framework et une infrastructure pour les pages statiques dans React.

Un site web comme un blog, un portfolio, ou même une plateforme de cours comme freeCodeCamp sera beaucoup plus rapide en statique. Même le rendu côté serveur, comme c'est généralement le cas avec Next.js, ne garantit pas une meilleure vitesse ([Source : Sidney Alcantara](https://hackernoon.com/gatsby-won-against-nextjs-in-this-heads-up-competition-xa7p3ysc)).

L'accent mis sur le temps jusqu'au premier rendu de contenu significatif aboutit à un grand nombre de solutions pour générer des pages statiques dans d'autres frameworks, comme Vue ou Svelte.

D'un autre côté, les pages statiques sont difficiles à mettre à l'échelle pour des millions de pages. Si vous construisez une application avec beaucoup de contenu dynamique comme des profils utilisateurs, vous êtes probablement mieux loti en utilisant des pages dynamiques. Les deux façons de gérer le contenu sont là pour rester.

## Les plateformes transforment les développeurs individuels en départements IT entiers

Les années récentes ont apporté une multitude de plateformes qui accélèrent le développement front-end. C'est énorme car cela permet aux petites équipes de se déplacer rapidement. 

Vous pouvez facilement implémenter de la vidéo en utilisant [Twilio](https://www.twilio.com/) ou [Agora.io](https://www.agora.io/). Vous pouvez ajouter une authentification en un rien de temps en utilisant [Firebase](https://firebase.google.com/docs/auth), [Amazon Cognito](https://aws.amazon.com/cognito/) ou [Okta](https://www.okta.com/) (Okta a également acquis [Auth0](https://auth0.com/)).

Le déploiement automatique et global du code front-end est particulièrement intéressant à mentionner. Il existe trois solutions incontournables : Vercel, Gatsby Cloud et Netlify. Elles peuvent transformer un développeur front-end avec un compte GitHub en un département DevOps entier en 5 minutes.  
  
Au moment de l'écriture, les trois plateformes offrent des temps de chargement moyens relativement similaires (Sources : [Netlify vs Vercel](https://bejamas.io/compare/netlify-vs-vercel/), [Netlify vs Gatsby Cloud](https://bejamas.io/compare/netlify-vs-gatsby-cloud/)).

Gatsby Cloud est uniquement pour React mais rend le travail avec d'innombrables pages statiques presque trop facile. Si vous construisez une application Gatsby, c'est probablement votre meilleur choix.

Vercel supporte les principaux frameworks, y compris ceux côté serveur, comme le framework propre aux fondateurs de l'entreprise, Next.js. Si vous travaillez sur une application rendue côté serveur, Vercel facilitera grandement votre vie.

Netlify se concentre sur les frameworks côté client, comme React et Vue purs. Il offre une large gamme d'outils utiles tels que des formulaires prêts à l'emploi, une authentification et des fonctions serverless. Je crois que c'est le meilleur choix pour les applications traditionnelles côté client.

Un outsider qui mérite d'être mentionné est Shuffle.dev. Il peut créer une mise en page de site web professionnelle de manière aléatoire, en quelques secondes. Il dispose d'une sélection relativement large de thèmes et de frameworks CSS et ajoute de nouvelles fonctionnalités et du contenu chaque semaine. Chez [CodeAlly.io](https://codeally.io/), nous l'utilisons beaucoup pour accélérer le prototypage.

## L'optimisation du front end est clé

Le front end a fait un tour complet ces dernières années. Les sites légers se sont transformés en plateformes lourdes avec des temps de rendu longs. Certaines personnes se souviennent peut-être encore lorsque Slack utilisait la version développeur de React ([Source : Robert Pankowecki](https://twitter.com/pankowecki/status/892294002040594434)). La tendance à rendre les SPA plus rapides existe depuis des années mais gagne encore en élan.

Les bibliothèques qui impactent négativement les performances, comme Moment.js, sont remplacées par leurs homologues plus légers et performants tels que Day.js. D'autres sont refactorisées pour réduire la taille du bundle. Les exemples incluent Material UI et Lodash.

Sentry, le leader du marché dans la journalisation des erreurs, n'a commencé à travailler sur l'optimisation de la taille du bundle que depuis quelques mois. Dans tout l'écosystème front-end, il y a un accent croissant sur l'utilisation du lazy loading, le rendu du front end côté serveur, ou l'utilisation de fichiers CSS au lieu de styliser l'application avec JavaScript, comme c'était le cas avec, par exemple, styled-components.

Tailwind a gagné beaucoup en popularité récemment et, en 2022, il restera sûrement populaire. Il gère la réduction du temps de chargement de l'application comme presque aucun autre outil CSS. 

Cela dit, il a une courbe d'apprentissage raide. Le code Tailwind est souvent difficile à lire. 

Je recommande vivement d'essayer Linaria également. Linaria combine les avantages de styled-components et la vitesse de l'utilisation de fichiers CSS statiques. Nous l'utilisons depuis un certain temps chez [CodeAlly.io](https://codeally.io/) et toute l'équipe front-end adore cette bibliothèque : [https://github.com/callstack/linaria](https://github.com/callstack/linaria).

Exemple de code en Linaria :

```JavaScript
import { styled } from '@linaria/react';
import mainTheme from 'themes/mainThemeV2';
 
export const Wrapper = styled.div`
 display: flex;
 flex-direction: column;
 align-items: center;
 height: 100%;
 width: 30px;
 max-height: 60px;
 border-bottom: 1px solid ${mainTheme.colors.neutral300};
 background-color: ${mainTheme.colors.primary300};
 border-radius: 8px;
`;
```

Remarquez comment vous pouvez utiliser JavaScript dans les styles. Il est également possible de réutiliser les styles puisqu'ils sont des constantes JS régulières. Le code est compilé en un fichier CSS lors du processus de construction.

Cela aboutit à une combinaison d'une excellente expérience développeur et d'un front-end ultra-rapide.

## Conclusion

Lorsque je commençais, les choses évoluaient beaucoup plus lentement. Il y a beaucoup d'innovation qui se produit et le front end évolue rapidement.  
  
Si vous voulez travailler dans l'industrie, vous pourriez vouloir jeter un coup d'œil à [CodeAlly](https://codeally.io/). C'est une plateforme que j'ai fondée avec des amis où les entreprises technologiques se disputent les programmeurs en les invitant à des emplois.

Les nouveaux programmeurs avec peu ou pas d'expérience peuvent également prouver leurs compétences avec des défis de code intégrés VSCode et Docker.  
  
J'espère que cet article a été agréable à lire et que vous y avez trouvé quelque chose de précieux. À la prochaine fois !