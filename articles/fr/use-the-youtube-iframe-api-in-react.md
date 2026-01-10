---
title: Comment utiliser l'API YouTube IFrame dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-17T22:55:52.000Z'
originalURL: https://freecodecamp.org/news/use-the-youtube-iframe-api-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6024fe5b0a2838549dcc345f.jpg
tags:
- name: api
  slug: api
- name: React
  slug: react
- name: youtube
  slug: youtube
seo_title: Comment utiliser l'API YouTube IFrame dans React
seo_desc: "By Kevin Cunningham\nAs a digital prototyping agency, my company works\
  \ with clients to help them quickly test the core of their ideas with their clients\
  \ and investors. \nOne of our clients is a group of doctors exploring ways to help\
  \ support older pati..."
---

Par Kevin Cunningham

En tant qu'agence de prototypage numérique, [mon entreprise](https://spin-up.io) travaille avec des clients pour les aider à tester rapidement le cœur de leurs idées avec leurs clients et investisseurs. 

L'un de nos clients est un groupe de médecins explorant des moyens pour aider à soutenir les patients âgés avec des soins post-opératoires.

Il y a plusieurs aspects à l'application, mais l'un d'eux est le partage d'exercices avec les patients et le suivi de leur succès. Les exercices sont hébergés sur YouTube et partagés dans une application NextJS.

La semaine dernière, nous avons reçu cette demande du chef de produit :

> Salut,  
> Peut-on déclencher une fenêtre contextuelle pour demander au patient s'il a terminé l'exercice ? Cela devrait se déclencher lorsque la vidéo se termine ou est mise en pause à plus de 95 %.

Jusqu'à ce point, nous intégrions le lecteur YouTube sans interagir avec l'API. Cela allait être amusant.

## Explorer la documentation

La documentation pour l'[API YouTube Player](https://developers.google.com/youtube/iframe_api_reference#Events) est très claire. J'ai pu voir qu'il y avait divers écouteurs d'événements et propriétés de données disponibles à explorer. Le léger problème que j'ai eu est qu'elle est écrite dans un paradigme JavaScript vanilla alors que je travaillais en React.

J'ai déjà fait ce genre de conversion auparavant. Explorer la création et le passage de `refs`, l'utilisation de `_document.js` dans NextJS pour utiliser des scripts externes et gérer certaines des idiosyncrasies qui se font connaître au fur et à mesure que vous travaillez sur un projet comme celui-ci.

Avant de me lancer, j'ai décidé de chercher une bibliothèque React qui pourrait tout gérer pour moi.

## Bibliothèque react-youtube

Parfois, il est difficile de trouver la bibliothèque que vous cherchez et parfois ce n'est pas le cas. Dans ce cas, la description de cette bibliothèque semblait être exactement ce que je voulais :

> Composant [React](http://facebook.github.io/react/) simple agissant comme une couche mince sur l'[API YouTube IFrame Player](https://developers.google.com/youtube/iframe_api_reference)

Je n'ai pas trouvé la documentation de la bibliothèque très utile, mais comme elle prétendait être une couche mince, j'espérais pouvoir m'appuyer sur la documentation YouTube elle-même (spoiler alert : j'ai pu !).

## Structurer le projet

J'allais avoir besoin de :

* Une modale et un moyen de suivre son état ;
* Une fonction pour convertir une URL YouTube en videoid que `react-youtube` nécessite
* Une fonction pour tester si la vidéo était au point cible
* L'intégration `react-youtube`.

## react-modal

J'ai tendance à apprécier les projets qui sont bien nommés et c'en est un autre.

Pour certains, il peut sembler un peu excessif d'utiliser une bibliothèque pour les modales, mais je suis fan. Sans une bibliothèque comme celle-ci, je devrais construire beaucoup de fonctionnalités moi-même (événements clavier, accessibilité, cliquer en dehors de la modale). 

La documentation donne quelques styles par défaut décents, donc je vais les ajouter en haut du projet.

```js
const modalStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)"
  }
};
```

À l'intérieur de ma fonction, je vais ajouter un hook `useState` pour gérer le statut de la modale.

```js
 const [modalIsOpen, setModalIsOpen] = React.useState(false);
```

Maintenant, je suis prêt à ajouter ma modale. Je l'ajoute normalement en bas du composant, mais en réalité, vous pouvez l'ajouter où cela a du sens.

```js
      <Modal
        isOpen={modalIsOpen}  
        onRequestClose={() => setModalIsOpen(false)}
        contentLabel="Exercice terminé"
        style={modalStyles}
      >
        <div>
          <h3>Exercice terminé ?</h3>
          <button
            onClick={handleExerciseComplete}
          >
            Terminer l'exercice
          </button>
        </div>
      </Modal>
```

Quelques points à noter :

* La prop isOpen prend la valeur d'état que nous avons créée ci-dessus.
* La prop onRequestClose bascule cette valeur d'état à false. Vous pourriez avoir une fonction de gestion séparée, mais cela semble un peu excessif.
* La prop style reçoit la constante que nous avons créée ci-dessus.

À l'intérieur de la modale, nous posons la question et fournissons un bouton à cliquer si le patient a effectivement terminé l'exercice. Je ne vais pas explorer ce que nous faisons avec la fonction `handleExerciseComplete` dans le code en direct, donc pour l'instant, nous allons simplement journaliser dans la console.

```js
const handleExerciseComplete = () => console.log("Faire quelque chose");
```

## Préparer le videoID

La bibliothèque `react-youtube` utilise le videoID plutôt que l'URL. Notre équipe de contenu est plus à l'aise avec les URL et je ne veux pas leur compliquer la vie.

Normalement, je source cela à partir d'un système de gestion de contenu, mais pour cet exemple, je vais ajouter un champ de saisie avec un `useState` pour suivre la valeur.

```js
const [videoUrl, setVideoUrl] = React.useState("");
```

```js
<input value={videoUrl} onChange={(e) => setVideoUrl(e.target.value)} />
```

Super ! Maintenant, nous devons pouvoir obtenir l'id à partir de l'URL. Si vous n'avez jamais regardé une URL YouTube en détail, elle peut ressembler à ceci [https://www.youtube.com/watch?t=746&v=LRini_YIs2I&feature=youtu.be](https://www.youtube.com/watch?t=746&v=LRini_YIs2I&feature=youtu.be). L'id de la vidéo est la chaîne après `v=` et avant le `&`. 

Une forme plus simple de l'URL pourrait ressembler à ceci [https://www.youtube.com/watch?v=N1pIYI5JQLE](https://www.youtube.com/watch?v=N1pIYI5JQLE) et nous devons pouvoir gérer cela aussi.

Voici ma tentative de résoudre ce problème.

```js
  let videoCode;
  if (videoUrl) {
    videoCode = videoUrl.split("v=")[1].split("&")[0];
  }
```

## Vérifier le temps écoulé

L'API YouTube met à disposition de nombreuses fonctions d'assistance. Les deux que nous allons utiliser sont `.getDuration()` et `.getCurrentTime()`.  

Nous allons utiliser ces deux valeurs pour vérifier si plus de 95 % de la vidéo s'est écoulé. Si c'est le cas, nous allons déclencher l'ouverture de la modale.

```js
  const checkElapsedTime = (e) => {
    const duration = e.target.getDuration();
    const currentTime = e.target.getCurrentTime();
    if (currentTime / duration > 0.95) {
      setModalIsOpen(true);
    }
  };
```

Le `e.target` est équivalent au `player` dans la documentation YouTube. Vous pouvez donc [consulter les docs](https://developers.google.com/youtube/iframe_api_reference#onStateChange) pour trouver d'autres moyens d'interagir avec la vidéo pour votre projet.

## react-youtube

Maintenant, nous pouvons enfin ajouter le composant YouTube. Nous allons utiliser la prop `onStateChange` du wrapper et lui passer notre fonction.

```js
          <YouTube
            videoId={videoCode}
            onStateChange={(e) => checkElapsedTime(e)}
          />
```

Cela semble légèrement anticlimactique de voir cela maintenant, mais nous avons terminé. Nous passons l'événement à notre fonction `checkElapsedTime` et, si elle passe la conditionnelle, la modale s'ouvrira.

Il y a beaucoup d'autres moyens de se connecter à cette API. La documentation liste les suivants :

```js
  onReady={func}                   
  onPlay={func}                   
  onPause={func}                    
  onEnd={func}                     
  onError={func}                    
  onStateChange={func}              
  onPlaybackRateChange={func}      
  onPlaybackQualityChange={func}   
```

Chacun de ceux-ci acceptera une fonction comme celle que nous avons créée ci-dessus. 

## Essayez-le

J'ai configuré un [Code Sandbox](https://codesandbox.io/s/react-youtube-demo-f6l29) avec le code d'exemple de cet article. Rendez-vous là-bas et déposez une URL YouTube dans la boîte de saisie. Testez ce qui se passe lorsque vous parcourez la vidéo et, en particulier, lorsque vous mettez en pause ou atteignez 95 % ou plus.