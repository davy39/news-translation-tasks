---
title: Comment construire votre propre Roue des Noms avec React et TypeScript
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2024-10-23T15:00:52.592Z'
originalURL: https://freecodecamp.org/news/build-your-own-wheel-of-names
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729695428229/56ac185a-bed1-4bbc-ab6d-a12f2ac5adee.png
tags:
- name: React
  slug: reactjs
- name: TypeScript
  slug: typescript
- name: Bun
  slug: bun
- name: vite
  slug: vite
- name: ' Wheel of Names'
  slug: wheel-of-names
seo_title: Comment construire votre propre Roue des Noms avec React et TypeScript
seo_desc: 'A while ago, I stumbled upon a website listing various coding challenges,
  and I decided to give some a try.

  Last week, I came across one that involved building a "Wheel of Names." It reminded
  me of a similar project I built years ago using Flash and ...'
---

Il y a quelque temps, je suis tombé sur un site web listant divers défis de codage, et j'ai décidé d'en essayer quelques-uns.

La semaine dernière, je suis tombé sur un défi qui consistait à construire une "Roue des Noms". Cela m'a rappelé un projet similaire que j'avais réalisé il y a des années en utilisant Flash et ActionScript 3—des technologies qui ne sont plus utilisées aujourd'hui. J'ai donc pensé qu'il serait amusant de recréer la roue, mais cette fois en utilisant une pile technologique moderne.

Dans ce tutoriel, je vais vous guider à travers les étapes de sa construction à partir de zéro.

## Table des Matières

* [Description du Projet](#heading-description-du-projet)
    
* [Pourquoi aurais-je besoin d'une Roue des Noms ?](#heading-pourquoi-aurais-je-besoin-dune-roue-des-noms)
    
* [Le Plan pour l'Application](#heading-le-plan-pour-lapplication)
    
    * [Fonctionnalités de l'Application](#heading-fonctionnalites-de-lapplication)
        
    * [La Pile Technologique](#heading-la-pile-technologique)
        
* [Construisons l'Application](#heading-construisons-lapplication)
    
    * [Structure du Projet](#heading-structure-du-projet)
        
    * [Comment construire les Composants](#heading-comment-construire-les-composants)
        
* [Comment Déployer l'Application sur Vercel](#heading-comment-deployer-lapplication-sur-vercel)
    
* [Conclusion](#heading-conclusion)
    

## Description du Projet

Ce sera une application qui, je présume, est inspirée de l'émission de télévision "La Roue de la Fortune". Dans cette émission, les candidats tentent de deviner une phrase courte en proposant des lettres. Si elles sont correctes, les lettres sont révélées. Ils font tourner la roue pour déterminer la valeur monétaire de chaque lettre correcte.

![La roue dans "La Roue de la Fortune" affichant les différents montants/prix que les candidats peuvent gagner](https://cdn.hashnode.com/res/hashnode/image/upload/v1729622283461/8fde5307-eadd-4b4a-8f39-fe8e47478bd3.png align="center")

La Roue des Noms est similaire, mais permet de créer une roue virtuelle sur laquelle on peut placer nos propres noms. On peut ensuite la faire tourner virtuellement pour déterminer un gagnant.

### **Dépôt GitHub**

Si vous souhaitez passer la lecture, voici le [dépôt GitHub](https://github.com/mihailgaberov/Wheel-of-Names) avec un [README](https://github.com/mihailgaberov/Wheel-of-Names/blob/main/README.md) détaillé. Vous pouvez également voir la démo en direct [ici](https://wheel-of-names-three.vercel.app/).

## Pourquoi aurais-je besoin d'une Roue des Noms ?

Tout d'abord, c'est très amusant à construire ! Un cas d'utilisation pratique et réel serait pour organiser des jeux de type loterie où vous devez choisir un gagnant aléatoire.

Par exemple, imaginez que vous faites partie d'une équipe agile qui organise des rétrospectives toutes les deux semaines, et que vous devez choisir aléatoirement un membre de l'équipe pour animer chaque session. Il suffit d'ajouter le nom de tout le monde à la liste des participants, de faire tourner la roue et de laisser la roue décider pour vous ! 🎡

## Le Plan pour l'Application

L'application est composée de plusieurs composants, la fonctionnalité principale étant la roue tournante. La roue aura une section pour chaque participant, et chaque section sera colorée de manière unique, avec une taille calculée proportionnellement au nombre de participants. Une fois l'animation de rotation terminée, le gagnant sera révélé avec une fenêtre contextuelle amusante, de style confettis.

D'autres parties de l'application incluent une section pour entrer la question ou la phrase à laquelle la rotation est destinée, ainsi que des contrôles pour ajouter des noms de participants et les afficher dans une liste bien organisée.

La liste offrira des options pour trier et mélanger les noms. Le tri organisera les noms par ordre alphabétique, tandis que l'option de mélange les randomisera. Vous pouvez également supprimer tout participant précédemment ajouté.

Toutes ces modifications sont reflétées dynamiquement sur le composant de la roue, garantissant que la roue reste à jour avec la dernière liste de participants.

Voici quelques captures d'écran qui montrent à quoi ressemblera l'application une fois terminée.

![Application Roue des Noms - état vide initial](https://cdn.hashnode.com/res/hashnode/image/upload/v1729578916704/0634a255-99a3-4a9c-8d64-6468cd732d40.png align="center")

![Application Roue des Noms - ajout de question](https://cdn.hashnode.com/res/hashnode/image/upload/v1729578959007/33b8c9a5-73d0-4c61-bdad-1006107358a8.png align="center")

![Application Roue des Noms - ajout de participants](https://cdn.hashnode.com/res/hashnode/image/upload/v1729578989621/fa954e01-52be-4e60-8a01-27a7a2b12a70.png align="center")

Voici quelques vidéos YouTube que j'ai enregistrées après avoir terminé l'application, montrant ses fonctionnalités en action.

%[https://youtu.be/sugUnci1Rlw] 

%[https://youtu.be/gIc6wtH9fK8] 

### **Fonctionnalités de l'application :**

**I. Question**

1. C'est ici que les utilisateurs peuvent soumettre une question ou une phrase qui déterminera le sujet des tours.
    
2. Toute modification apportée dans le champ de saisie est enregistrée lorsque l'utilisateur clique en dehors de celui-ci (perte de focus).
    

**II. Roue**

1. Le composant de la roue tourne avec une animation d'assouplissement et détermine le gagnant.
    
2. Le sens de rotation peut être ajusté à l'aide des boutons, pour une rotation dans le sens des aiguilles d'une montre ou dans le sens inverse.
    
3. Chaque secteur adjacent est coloré de manière unique, et leurs tailles sont calculées proportionnellement au nombre de participants.
    

**III. Ajout de Participants**

1. La zone de saisie des participants comprend un champ de saisie pour entrer le nom d'un participant et un bouton "AJOUTER" pour l'ajouter à la liste des participants.
    
2. Pour ajouter des participants plus rapidement, l'utilisateur peut appuyer sur la touche ENTRÉE du clavier.
    

**IV. Liste des Participants**

1. Cette section affiche tous les noms des participants.
    
2. La liste offre des options pour trier les noms par ordre alphabétique ou les mélanger aléatoirement, les deux actions mettant à jour dynamiquement le composant de la roue.
    

### La Pile Technologique

Voici une liste des principales technologies que nous allons utiliser :

* **Bun** – Un bundler et gestionnaire de paquets JavaScript rapide, connu pour sa vitesse et sa simplicité.
    
* **Vite** – Un outil de build qui fournit un environnement de développement rapide, particulièrement optimisé pour les projets web modernes.
    
* **React** – Une bibliothèque JavaScript populaire pour construire des interfaces utilisateur, permettant un rendu efficace et une gestion d'état.
    
* **TypeScript** – Un sur-ensemble de JavaScript qui ajoute une typisation statique, améliorant la qualité et la maintenabilité du code.
    
* **styled-components** – Une bibliothèque pour écrire du CSS-in-JS, permettant de scoper les styles aux composants et offrant une approche plus dynamique au stylisme.
    
* **canvas** – Un élément HTML puissant utilisé pour dessiner des graphiques, des animations et d'autres contenus dynamiques directement sur la page web.
    
* **canvas-confetti** – Une bibliothèque JavaScript pour ajouter des animations de confettis amusantes et festives au canvas, parfaite pour annoncer les gagnants.
    

## **Construisons l'Application**

À partir de ce point, je vais vous guider à travers le processus que j'ai suivi pour construire cette application.

### **Structure du Projet**

La structure du projet est assez simple, grâce à React et styled-components, qui rendent cette approche modulaire facile à mettre en œuvre. Vous pouvez consulter la structure du projet dans mon dépôt GitHub.

Ci-dessous, je vais vous expliquer la logique derrière la structure et les décisions que j'ai prises pour chaque partie.

![Structure du Projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1729579163492/2b406e15-c8f6-4533-9a93-4c6e7b1435f4.png align="center")

* **main.tsx** : Le point d'entrée de l'application React créée avec Vite.
    
* **App.tsx** : Le composant parent qui inclut tous les autres composants et gère la gestion des noms des participants (ajout, suppression, tri, mélange).
    
* **Header.tsx** : La partie supérieure de l'application, qui affiche le titre de l'application.
    
* **Participants.tsx** : Affiche les contrôles pour ajouter et afficher les participants. Il inclut une fonction de validation pour empêcher les noms vides ou invalides.
    
* **Question.tsx** : Affiche la section de la question, gère l'état et les fonctionnalités de base du clavier et des clics.
    
* **Wheel.tsx** : Le composant principal contenant la logique d'animation, la taille/coloration des secteurs et le rendu des noms des participants. Il utilise l'élément `canvas` pour une rotation fluide et intègre `confetti` pour annoncer le gagnant.
    
* **utils.ts** : Un fichier avec des fonctions utilitaires utilisées dans toute l'application.
    
* **styles.ts** : Contient des composants stylés partagés, exportés pour une utilisation dans toute l'application.
    

#### Fichiers CSS et Configurations

Les fichiers restants du projet incluent des styles CSS standard de la configuration initiale de Vite, ainsi que des fichiers de configuration pour Vite, TypeScript, Prettier et ESLint. Ces configurations sont couramment utilisées dans les projets modernes et ne sont pas spécifiques à cette application, donc je ne vais pas les détailler ici. Vous pouvez facilement trouver de la documentation pour chacun en ligne.

### Comment construire les Composants

Dans cette section, nous allons passer en revue le processus de construction de chaque composant de l'application, étape par étape. À la fin, vous aurez une application entièrement fonctionnelle avec des composants modulaires et autonomes.

#### 1. Composant App

Le composant App sert de conteneur central pour l'ensemble de l'application. Il encapsule tous les blocs de construction principaux et est responsable de la gestion de l'état des noms des participants. Au-delà du rendu de l'interface utilisateur, il gère la logique principale de l'application, telle que l'ajout, la suppression, le tri et le mélange des participants.

Le composant utilise un état local pour stocker la liste des noms. Cet état est mis à jour via des fonctions de rappel qui sont déclenchées par des interactions dans les composants enfants — spécifiquement, les composants `Participants` et `Wheel`.

Les fonctions de gestion principales, `handleAddName` et `handleRemoveName`, gèrent l'ajout et la suppression de noms de la liste. De plus, il y a deux autres gestionnaires dédiés à la manipulation de l'ordre des noms : un pour le tri (`handleSortNames`) et un pour le mélange (`handleShuffleNames`). Ces gestionnaires offrent une flexibilité dans la manière dont la liste des participants est affichée et interagie dans l'application.

```typescript
const [names, setNames] = useState<string[]>([]);

  const handleAddName = (name: string) => {
    if (names.length < MAX_PARTICIPANTS) {
      setNames([...names, name]);
    }
  };

  const handleRemoveName = (index: number) => {
    setNames(names.filter((_, i) => i !== index));
  };

  const shuffleNames = () => {
    const shuffledNames = [...names].sort(() => Math.random() - 0.5);
    setNames(shuffledNames);
  };

  const sortNames = () => {
    const sortedNames = [...names].sort((a, b) => a.localeCompare(b));
    setNames(sortedNames);
  };
```

Une partie cruciale du composant est la constante `MAX_PARTICIPANTS`, qui définit une limite au nombre de participants autorisés. Cela garantit que l'application ne dépasse pas un certain nombre d'entrées, maintenant ainsi les performances et l'utilisabilité.

La structure de rendu de ce composant est la suivante :

```typescript
 return (
    <>
      <Header />
      <Question />
      <Main>
        <Participants
          handleAddName={handleAddName}
          handleRemoveName={handleRemoveName}
          shuffleNames={shuffleNames}
          sortNames={sortNames}
          names={names}
        />
        <Wheel participants={names} />
      </Main>
    </>
  );
```

#### 2. Composant Header

Le [composant Header](https://github.com/mihailgaberov/Wheel-of-Names/blob/main/src/Header.tsx) est la partie la plus simple de l'application. Son rôle principal est d'afficher le titre en haut de la page. Ce composant est essentiel pour définir le ton et la marque de l'application. Malgré sa simplicité, il pose les bases de la structuration de l'interface utilisateur et peut être facilement personnalisé ou étendu à l'avenir.

Voici à quoi il ressemble :

![Composant Header](https://cdn.hashnode.com/res/hashnode/image/upload/v1729581820870/9384834a-8657-435d-89f5-e404a67d6ac0.png align="center")

#### 3. Composant Question

Le [composant](https://github.com/mihailgaberov/Wheel-of-Names/blob/main/src/Question.tsx) qui affiche l'entrée pour saisir une question ou une phrase est relativement simple. Il rend un champ de texte et utilise quelques fonctions de gestion pour améliorer l'expérience utilisateur. Ces gestionnaires gèrent le comportement du focus : définir le focus lorsque le champ de saisie est cliqué, supprimer le focus lorsque l'utilisateur clique en dehors du champ, et permettre à l'utilisateur d'utiliser les touches ENTRÉE ou ÉCHAP pour soumettre ou annuler leur saisie, respectivement.

![Composant Question au Focus](https://cdn.hashnode.com/res/hashnode/image/upload/v1729581877713/94fa416b-48e0-4a33-8ed4-1db975ce7542.png align="center")

#### 4. Participants

Dans cette partie de l'application, nous affichons la liste de tous les participants ajoutés. Le composant inclut une fonction de validation locale qui s'exécute à chaque fois avant d'ajouter un nouveau participant, garantissant que la saisie répond aux critères nécessaires (par exemple, pas de doublons ou de noms vides).

Nous utilisons également des attributs HTML intégrés pour activer ou désactiver dynamiquement les boutons en fonction de l'état de la liste des participants. Par exemple, les boutons "Trier" et "Mélanger" sont désactivés lorsque la liste est vide, tandis que le bouton "Ajouter" est désactivé une fois que la limite maximale de participants (`MAX_PARTICIPANTS`) est atteinte. Cela garantit une expérience utilisateur fluide et intuitive en empêchant les actions invalides.

Vous avez probablement déjà remarqué comment nous utilisons une fonction utilitaire du fichier `utils.ts` pour mettre en majuscule les noms des participants avant de les afficher. Cela garantit que tous les noms sont présentés dans un format cohérent et convivial.

Cela se produit à l'intérieur d'une boucle `map()`, où nous itérons sur la structure de données `names` et affichons le nom de chaque participant dans une ligne séparée au sein du composant de liste. La fonction utilitaire est appliquée lors de cette itération pour garantir que les noms sont correctement mis en majuscule avant le rendu.

#### 5. Composant Wheel

C'est le plus grand composant de notre application. En haut, vous trouverez les styles nécessaires pour positionner la fenêtre contextuelle du gagnant, qui est accompagnée de confettis lorsqu'un gagnant est sélectionné. En dessous, nous définissons un tableau contenant toutes les couleurs possibles utilisées pour colorer les secteurs de la roue. Ensuite, nous passons au code du composant lui-même.

Le composant utilise plusieurs états pour garantir que l'animation de rotation se comporte comme prévu. De plus, il gère le moment où déclencher et afficher la fenêtre contextuelle du gagnant, avec le nom du gagnant affiché à l'intérieur. Ces états et gestionnaires travaillent ensemble pour créer une expérience fluide et interactive.

```typescript
 const [spinning, setSpinning] = useState(false);
  const [rotation, setRotation] = useState(0);
  const [spinDirection, setSpinDirection] = useState<
    'clockwise' | 'counterclockwise'
  >('clockwise');
  const [showPopup, setShowPopup] = useState(false);
  const [popupWinner, setPopupWinner] = useState<string | null>(null);
```

La méthode `drawWheel()` est responsable du rendu de la roue avec le nombre spécifié de secteurs sur le canvas. Cette méthode repose fortement sur l'élément `canvas` et son API associée pour dessiner chaque secteur et le nom du participant. Nous utilisons également notre fonction utilitaire pour mettre en majuscule les noms des participants dans la roue, garantissant ainsi la cohérence avec le composant de liste.

Lorsque le bouton "Spin" est cliqué, la méthode `startSpin()` est déclenchée. C'est ici que la logique d'animation est implémentée. Nous générons un nombre aléatoire de rotations, allant de 5 à 10 rotations complètes, pour rendre la rotation imprévisible.

La direction de la rotation est déterminée par la sélection de l'utilisateur, permettant à la roue de tourner soit dans le sens des aiguilles d'une montre, soit dans le sens inverse. Nous définissons également la durée de la rotation à 6000 ms (6 secondes) pour une animation fluide et engageante.

Pour améliorer le réalisme de l'animation, nous appliquons une fonction d'assouplissement qui implémente l'effet "Ease-out cubic", ce qui fait que la roue ralentit progressivement à mesure qu'elle atteint la fin de la rotation.

```typescript
 const easing = (t: number) => {
      // Ease-out cubic
      return 1 - Math.pow(1 - t, 3);
    };
```

L'animation est gérée par une fonction interne appelée `animate()`, qui utilise l'API `requestAnimationFrame`, une fonctionnalité prise en charge par tous les navigateurs modernes pour des animations fluides et haute performance. À l'intérieur de cette fonction, nous calculons le temps écoulé et la rotation actuelle, mettant à jour l'état du composant en conséquence pour garantir que la roue tourne en douceur.

Lors de chaque frame d'animation, nous invoquons également la fonction `determineWinner()`, qui est définie ci-dessous. Cette fonction calcule le secteur gagnant en déterminant sur quel secteur la roue atterrit à la fin de la rotation. Elle met ensuite à jour l'état de la fenêtre contextuelle pour afficher le nom du gagnant à l'intérieur de la fenêtre contextuelle.

```typescript
const determineWinner = (finalRotation: number) => {
    const sliceAngle = 360 / numSectors;
    const normalizedRotation = ((finalRotation % 360) + 360) % 360;
    const winningSector = Math.floor(normalizedRotation / sliceAngle);

    setPopupWinner(participants[winningSector]);
    setShowPopup(true);
  };
```

Changer la direction de la rotation est simple. Nous mettons simplement à jour l'état du composant en fonction de la valeur de l'étiquette du bouton, qui bascule entre "Clockwise" et "Counterclockwise". En définissant l'état en conséquence, nous pouvons facilement contrôler la direction de la rotation avec un seul clic sur le bouton.

Le code restant avant la partie de rendu de ce composant inclut un effet qui contrôle la visibilité de la fenêtre contextuelle de confettis. La fonction `startConfetti` est responsable de l'initiation de l'animation de confettis lorsqu'un gagnant est sélectionné. Cet effet garantit que l'animation de confettis est déclenchée et affichée au bon moment, ajoutant une touche festive à l'expérience.

Et avec tout cela, nous sommes prêts à rendre notre composant Wheel comme suit :

```typescript
return (
    <div>
      <canvas
        ref={canvasRef}
        width={400}
        height={400}
        style={{ borderRadius: '50%', border: '2px solid black' }}
      />
      <ButtonsContainer>
        <Button
          onClick={changeSpinDirection}
          disabled={participants.length === 0 || spinning}
        >
          {capitalize(spinDirection)}
        </Button>
        <Button
          onClick={startSpin}
          disabled={participants.length === 0 || spinning}
        >
          Spin
        </Button>
      </ButtonsContainer>
      {showPopup && popupWinner && (
        <Popup>
          <h2>Félicitations !</h2>
          <h3>{capitalize(popupWinner)}</h3>
        </Popup>
      )}
    </div>
```

## **Comment Déployer l'Application sur Vercel**

Enfin 🎉 nous sommes prêts à déployer notre application.

J'ai utilisé Vercel pour ce déploiement car il offre un moyen rapide, gratuit et facile de déployer des applications web. Si vous souhaitez un guide plus détaillé sur la façon de déployer avec Vercel, consultez mon [tutoriel précédent](https://www.mihailgaberov.com/build-a-real-time-order-book-application-with-react-and-websockets) pour des instructions étape par étape.

## **Conclusion**

J'espère que vous avez trouvé ce processus aussi intéressant et agréable à suivre que je l'ai trouvé à créer !

Maintenant, prenons un moment pour réfléchir à ce que nous avons accompli et mettons en avant quelques points clés qui pourraient s'avérer utiles pour de futurs projets.

1. **Conception Modulaire** : Diviser l'application en petits composants gérables a facilité la maintenance et l'évolutivité.
    
2. **React et Styled-Components** : Ces outils ont rationalisé le développement, permettant un stylisme dynamique et une gestion efficace de l'interface utilisateur.
    
3. **Canvas pour les Animations** : L'utilisation de l'élément `canvas` a permis des animations fluides et visuellement attrayantes.
    
4. **Déploiement sur Vercel** : La simplicité et la rapidité de Vercel en ont fait le choix idéal pour déployer rapidement l'application.
    

Ce projet a mis en lumière la puissance des outils modernes comme React, TypeScript et canvas, tout en garantissant que l'application reste modulaire et facile à maintenir.

Merci d'avoir lu ! 👋