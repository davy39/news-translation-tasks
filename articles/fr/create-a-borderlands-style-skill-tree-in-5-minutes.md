---
title: Comment créer un arbre de compétences style Borderlands en 5 minutes
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2019-10-01T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/create-a-borderlands-style-skill-tree-in-5-minutes
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca02c740569d1a4ca4706.jpg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: TypeScript
  slug: typescript
- name: User Interface
  slug: user-interface
- name: Video games
  slug: video-games
seo_title: Comment créer un arbre de compétences style Borderlands en 5 minutes
seo_desc: 'Growing up, I spent my spare time doing what most programmers did: played
  video games every waking moment. I loved Adventure games and what a time sink they
  were. If time was the Mary Rose, and I was the French, my artillery were games like
  Kingdom H...'
---

En grandissant, je passais mon temps libre à faire ce que la plupart des programmeurs faisaient : jouer à des jeux vidéo à chaque moment de veille. J'adorais les jeux d'aventure et quel gouffre de temps ils étaient. Si le temps était le Mary Rose, et que j'étais les Français, mon artillerie était des jeux comme Kingdom Hearts, Ōkami et Borderlands.

Pourquoi moi, et les autres, passions-nous autant de notre temps libre à explorer, survivre, mourir, et (tellement, tellement) grinder ? Des centaines de facteurs contribuent à créer une expérience engageante, mais celui sur lequel je vais me concentrer est la notion de progression.

L'idée de la gamification n'est pas nouvelle. De nombreuses applications populaires (comme [todoist](https://todoist.com/?lang=en), ou [challenge timer](https://productivitychallengetimer.com/)) ont incorporé une sorte de schéma de progression pour nous faire, les consommateurs, utiliser leur application, leur donner de l'argent et leur remettre nos données personnelles. J'ai donc décidé de permettre aux autres de faire de même, à travers de magnifiques arbres de compétences ! Note : Je n'attends ni argent ni données de ceux qui utilisent mes arbres de compétences.

Les dernières semaines m'ont vu travailler sans relâche pour créer ce que j'espère être un agréable package React plug'n'play pour vous aider à créer des arbres de compétences passionnants. Vous pouvez le tester vous-même en suivant le tutoriel. J'espère que ce sera une expérience sans friction.

Nous espérons avoir quelque chose ressemblant à l'arbre de compétences ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-2.png)
_« Un chiot mourant. Un bébé en larmes. Si les déclarations précédentes ont suscité une réaction émotionnelle, signalez-le à votre superviseur pour une destruction sommaire. »_

# beautiful-skill-tree@0.7.5

Récupérez le dépôt de démarrage en utilisant `git clone git@github.com:andrico1234/borderlands-skill-tree.git`

Déplacez-vous dans le répertoire et exécutez le script de démarrage, `yarn start`. Donnez un tour au site, vous ne verrez rien d'autre que le logo et l'environnement de Borderlands.

`beautiful-skill-tree` expose trois composants : les composants `SkillProvider`, `SkillTreeGroup` et `SkillTree`.

`SkillProvider` : Ce composant ne prend aucune propriété et fournit aux enfants le contexte de l'arbre de compétences. Ce composant gère toutes les données globales liées à l'arbre de compétences.

`SkillTreeGroup` : Il est plus impliqué car il peut prendre une propriété `theme` optionnelle, où nous pouvons passer quelques styles personnalisés, pour donner à notre arbre de compétences un vrai style Borderlands. Le `SkillTreeGroup` utilise également le modèle enfants-comme-fonction pour nous donner accès à certaines fonctionnalités API impératives, telles que la réinitialisation de l'arbre de compétences, le compteur de compétences sélectionnées, etc. Nous n'avons pas besoin de nous soucier de tout cela pour le cadre de cet article.

`SkillTree` : C'est le plus excitant des exports du package, à moins que vous ne soyez un amateur de typages (qui sont également exportés, pour tous les fans de TS). Le `SkillTree` ne prend aucun enfant mais nécessite 3 propriétés : `treeId`, `title` et `data`. Le `treeId` doit être un identifiant unique pour chaque arbre de compétences, mais doit être persistant à travers les sessions utilisateur car il est utilisé comme clé pour obtenir et définir les données dans le stockage local. Je ne vais pas expliquer ce que fait la propriété `title`, je vous laisse expérimenter. La `data` est le mélangeur de l'application. Vous passerez votre structure de données d'arbre de compétences que l'application utilisera pour rendre un `beautiful-skill-tree`. Commençons par un arbre très basique avant de passer à notre spectacle Borderlands multi-arbres et multi-branches.

Dans App.tsx, importez les 3 composants comme suit :

`import { SkillProvider, SkillTreeGroup, SkillTree } from 'beautiful-skill-tree';`

Placez-le sous votre balise `img`, à l'extérieur de la div conteneur de l'image, mais à l'intérieur de la div extérieure. Ajoutez le `SkillProvider`, en passant le `SkillTreeGroup` comme enfant. Avant de faire de même avec le `SkillTree`, rappelez-vous que comme `SkillTreeGroup` utilise le modèle fonction-comme-enfant, vous devrez rendre une fonction qui retourne les composants enfants. Retournez un seul `SkillTree` et donnez-lui un `treeId` et une propriété `title`. Passez un tableau vide dans la propriété `data` pour que votre `App.tsx` ressemble à ceci :

```js
function App() {
  return (
    <div>
    // <div headercontent />
      <SkillProvider>
        <SkillTreeGroup>
          {() => {
            return (
              <SkillTree treeId="basic-birch" title="Premier Arbre de Compétences" data={[]} />
            )
          }}
        </SkillTreeGroup>
      </SkillProvider>
    </div>
  );
}
```

Allez sur [localhost:3000](http://localhost:3000/) pour voir l'application en cours d'exécution. Vous devriez voir le logo, l'arrière-plan et un rectangle gris. Si vous rencontrez des erreurs, parcourez à nouveau l'introduction et vérifiez s'il y a des erreurs de syntaxe ou des imports incorrects.

Ensuite, créons un arbre très basique. Juste 3 éléments qui se déplacent en ligne droite. La structure de données pour `data` ressemble à ceci :

```ts
type Skill = {
  id: string;
  icon?: string;
  title: string;
  tooltip: {
    description : string;
  },
  children: Skill[];
}
```

Chaque compétence nécessite quatre propriétés, dont une est optionnelle. Vous devriez également remarquer que la propriété `children` est un type récursif, ce qui signifie qu'elle prend un tableau de la même structure de données, qu'elle utilise pour rendre les enfants de la compétence. Cela peut continuer à l'infini et créer des arbres très compliqués et sinueux. Je vais créer la première compétence pour vous, et je vous fais confiance pour continuer avec les deux prochains éléments.

```js
const data = [{
  id: 'first-skill',
  title: 'Le nœud racine',
  tooltip: {
    description : "Le nœud parent, tous les descendants seront verrouillés jusqu'à ce qu'il soit sélectionné",
  },
  children: [
  // rincez et répétez ; toujours répétez.
]}
```

Ajoutez l'extrait ci-dessus au fichier `App.tsx`, et remplacez le tableau vide à l'intérieur de la propriété `data` du `SkillTree` par notre définition `data`. Chargez votre page, et vous devriez avoir un nœud interactif. Survolez-le et cliquez dessus, il devrait réagir à vos actions. Si tout fonctionne, alors je vous charge de créer deux (ou plus) nœuds enfants. Expérimentez avec les longueurs des enfants et des frères et sœurs, pour voir ce que vous pouvez inventer. (Si vous arrivez également à casser mon précieux package, laissez-moi un problème GitHub pour que je puisse corriger les choses).

Une fois que vous êtes à l'aise avec la création d'un arbre de compétences, passons à la création de notre arbre de compétences Borderlands. Heureusement, j'ai fait tout le travail fastidieux pour vous et j'ai déjà créé les structures de données et accumulé les images.

Vous devrez importer les trois arbres depuis le fichier `data`, ce qui peut être fait via

`import { motion, harmony, cataclysm } from "./data/data";`

L'étape suivante consiste à créer deux `SkillTrees` supplémentaires à côté de celui actuel. Vous devrez les envelopper dans un `React.Fragment` car votre `SkillTreeGroup` essaiera maintenant de rendre 3 composants de niveau supérieur. Passez les données en conséquence, et si vous n'êtes pas sûr, j'ai posté l'extrait de code ci-dessous.

```js
<React.Fragment>
  <SkillTree treeId="motion" title="Mouvement" data={motion} />
  <SkillTree treeId="harmony" title="Harmonie" data={harmony} />
  <SkillTree treeId="cataclysm" title="Cataclysme" data={cataclysm} />
</React.Fragment>
```

Allez-y et vérifiez votre navigateur web, il devrait être **presque** prêt. Nous avons les compétences rendues, mais le style semble un peu terne. Cela ne ressemble pas vraiment à Borderlands. Heureusement pour vous, je suis un vrai [Neil Buchanan](https://www.youtube.com/watch?v=0evlWSY8kTc) et j'ai préparé un thème personnalisé. Importez le thème et passez-le à la propriété `theme` du `SkillTreeGroup`. L'objet thème est exporté via `import theme from './data/theme';`. Facile !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-3.png)
_« J'AI UNE QUESTION POUR VOUS. DES EXPLOSIONS ? »_

Une fois que vous avez fait ce qui précède, consultez le produit fini. Si vous n'êtes toujours pas satisfait des styles, consultez l'objet thème et personnalisez-le vous-même, il y a un tas d'attributs supplémentaires dont les styles peuvent être ajustés, alors jetez un coup d'œil aux typages du package.

J'ai mentionné plus tôt qu'il y a quelques propriétés et valeurs supplémentaires qui peuvent être utilisées pour ajuster l'arbre de compétences, alors amusez-vous et envoyez-moi des liens vers les arbres cool que vous créez. J'adorerais les ajouter à la liste croissante d'arbres trouvés [ici](https://github.com/andrico1234/beautiful-skill-tree#examples). [Voici](https://calisthenicsskills.com/) un exemple de l'arbre de compétences qui a lancé cette obsession.

J'espère que vous avez apprécié bidouiller avec le package `beautiful-skill-tree`. Je suis toujours en train d'ajouter de nouvelles fonctionnalités et de mettre à jour, alors donnez-lui une étoile sur GitHub ! Vous pouvez trouver une démonstration en ligne de l'arbre de compétences Borderlands [ici](http://borderlands-skill-tree.s3-website.eu-west-2.amazonaws.com/)

Vous pouvez me trouver sur Instagram ou GitHub si vous voulez discuter de code, de musique ou de fitness !