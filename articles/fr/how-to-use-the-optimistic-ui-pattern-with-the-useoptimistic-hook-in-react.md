---
title: Comment utiliser le motif Optimistic UI avec le hook useOptimistic() dans React
author: Tapas Adhikary
date: '2025-12-12T18:21:28.232Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-optimistic-ui-pattern-with-the-useoptimistic-hook-in-react
description: 'Avez-vous déjà cliqué sur une icône Like dans une application de réseau
  social et remarqué que le compteur augmente instantanément ? La couleur de l''icône
  change en même temps, avant même que le serveur ne termine l''action.

  Imaginez maintenant que vous cliquiez sur ce même bouton Like, mais qu''il prenne
  tout son temps...'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765561440350/c3546e6c-8b23-476a-86d4-b63fd2cb9f6c.png
tags:
- name: React
  slug: reactjs
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
seo_desc: 'Have you ever clicked a Like icon on a social media app and noticed the
  count jumps instantly? The colour of the icon changes at the same time, even before
  the server finishes the action.

  Now imagine you hit the same Like button, but it takes its swe...'
---


Avez-vous déjà cliqué sur une icône `Like` dans une application de réseau social et remarqué que le compteur augmente instantanément ? La couleur de l'icône change en même temps, avant même que le serveur ne termine l'action.

Imaginez maintenant que vous cliquiez sur ce même bouton Like, mais qu'il prenne tout son temps pour effectuer l'appel au serveur, réaliser les mises à jour de la base de données et vous renvoyer la réponse pour mettre à jour l'état du bouton Like.

Quelle expérience préféreriez-vous ? Vous choisirez très probablement le premier scénario. Nous aimons tous le « feedback instantané ». La magie du feedback instantané est propulsée par un motif de conception appelé le `Optimistic UI Pattern` (motif d'interface utilisateur optimiste).

Dans cet article, nous allons découvrir :

* Ce que signifie réellement l'Optimistic UI ?
    
* Comment cela fonctionne-t-il sous le capot ?
    
* Comment le nouveau hook useOptimistic() de React 19 rend-il cela plus facile que jamais ?
    
* Comment implémenter un scénario réel en utilisant le motif Optimistic.
    
* Plusieurs cas d'utilisation où vous pourrez utiliser ce motif.
    

À la fin, vous penserez proactivement à utiliser ce design pattern pour améliorer l'UX de votre projet.

Cet article est également disponible sous forme de tutoriel vidéo dans le cadre de l'initiative [15 Days of React Design Patterns](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC). N'hésitez pas à le consulter.

%[https://www.youtube.com/watch?v=x03yX-yNxas] 

## Table des matières

1. [Qu'est-ce que l'Optimistic UI ?](#heading-qu-est-ce-que-l-optimistic-ui)
    
2. [Comment cela fonctionne-t-il sous le capot ?](#heading-comment-cela-fonctionne-t-il-sous-le-capot)
    
3. [Comment construire un bouton Like optimiste](#heading-comment-construire-un-bouton-like-optimiste)
    
4. [Les pièges et les anti-patterns](#heading-les-pieges-et-les-anti-patterns)
    
5. [15 jours de design patterns React](#heading-15-jours-de-design-patterns-react)
    
6. [Avant de terminer...](#heading-avant-de-terminer)
    

## Qu'est-ce que l'Optimistic UI ?

L'`Optimistic UI` (également connu sous le nom de mises à jour optimistes) est un motif qui vous aide à mettre à jour l'interface utilisateur immédiatement, en supposant que l'opération serveur réussira, et si elle échoue plus tard, vous effectuez un rollback de l'UI vers l'état correct.

Au lieu d'attendre l'aller-retour de la requête client, l'écriture en base de données, la réponse du serveur, puis le rendu de l'UI, l'interface se met simplement à jour instantanément. Cela augmente considérablement ce qu'on appelle la `vitesse perçue`. L'utilisateur de l'application perçoit la mise à jour de l'UI comme instantanée – mais l'opération réelle peut se dérouler en arrière-plan.

### Sans mise à jour optimiste :

Si vous n'utilisez pas le motif optimiste, il s'agit d'un mécanisme client-serveur traditionnel, où :

* Côté client, un utilisateur interagit avec un élément de l'UI.
    
* Un [appel asynchrone](https://www.youtube.com/watch?v=WQdCffdPPKI) (requête) est effectué vers le serveur.
    
* Le serveur traite la requête et peut effectuer des mises à jour en base de données.
    
* En cas de succès, le serveur renvoie la réponse au client.
    
* Le client met à jour l'UI correspondante.
    
* En cas d'erreur, le serveur renvoie la réponse d'erreur au client.
    
* Le client informe l'utilisateur de l'erreur.
    

![Sans mise à jour optimiste](https://cdn.hashnode.com/res/hashnode/image/upload/v1765334108586/aabd3f16-b175-4b1d-ae33-94f33e1b894a.png align="center")

Dans ce cas, l'utilisateur doit attendre le succès ou l'échec de la requête pour percevoir un changement après son interaction. Cette attente n'est ni uniforme ni optimale. Elle peut varier en fonction de la vitesse du réseau, de la latence et des stratégies de déploiement de l'application.

### Avec une mise à jour optimiste :

Lorsque vous utilisez une mise à jour optimiste, voici comment les choses se passent :

* Côté client, un utilisateur interagit avec un élément de l'UI.
    
* L'UI est mise à jour instantanément, et l'utilisateur perçoit le feedback immédiatement.
    
* En parallèle, en arrière-plan, le client initie l'appel au serveur.
    
* Le serveur traite la requête et peut effectuer des mises à jour en base de données.
    
* En cas de succès, le serveur ne fait rien d'autre, car l'UI a déjà été mise à jour en supposant que cet appel réussirait.
    
* En cas d'erreur, le serveur renvoie la réponse d'erreur au client.
    
* Le client effectue un rollback de la mise à jour UI optimiste et anticipée qu'il avait faite.
    

![Avec une mise à jour optimiste](https://cdn.hashnode.com/res/hashnode/image/upload/v1765334174203/e8bef9ba-28b6-45e0-8f22-0fc1468e3219.png align="center")

Dans ce cas, l'utilisateur n'attend pas que l'aller-retour serveur se termine avant que l'UI ne soit mise à jour. C'est beaucoup plus rapide, en supposant que, dans la plupart des cas, l'appel serveur parallèle réussira.

Grâce à cette comparaison, nous pouvons maintenant comprendre pourquoi les mises à jour optimistes sont importantes dans les interfaces modernes.

* Elles améliorent la vitesse perçue.
    
* Elles maintiennent l'engagement des utilisateurs.
    
* Elles éliminent les sentiments d'incertitude du type « Est-ce que mon clic a fonctionné ? ».
    

Et ainsi de suite. Les mises à jour optimistes sont cruciales pour les fonctionnalités nécessitant une sensation de temps réel comme les messages de chat, les likes, les commentaires, les mises à jour de panier, les votes de sondage, l'édition collaborative, et plus encore. Même les applications basées sur l'IA qui prennent du temps à répondre bénéficient de placeholders optimistes comme « Réflexion... », « Envoi... », etc.

## Comment cela fonctionne-t-il sous le capot ?

Sous le capot, il y a en réalité deux états :

1. L'état réel (Actual State) : C'est la véritable source de vérité. Ces données doivent être synchronisées avec le serveur.
    
2. L'état optimiste (Optimistic State) : C'est un état temporaire affiché instantanément à l'utilisateur.
    

Lorsque la requête serveur réussit, ne faites rien. Votre état optimiste est maintenant correct. Si la requête serveur échoue, effectuez un rollback et ramenez l'UI à l'état réel.

React 19 a introduit un hook intégré pour aider avec ce motif appelé `useOptimistic()`. Dans la section suivante, nous allons l'explorer en profondeur avec du code et son fonctionnement interne.

### Le hook `useOptimistic()` dans React 19

`useOptimistic()` est un hook React introduit dans React 19 pour faciliter les mises à jour optimistes. La syntaxe et l'utilisation du hook se présentent comme suit :

```javascript
const [optimisticState, addOptimistic] = useOptimistic(state, updateFn);
```

Lorsqu'une action asynchrone est en cours, le hook `useOptimistic()` vous permet d'afficher différents états.

Il accepte :

1. **currentState** : votre véritable source de vérité (useState, Redux, état serveur, etc.).
    
2. **updateFn** : une fonction pure qui définit comment calculer la valeur optimiste.
    

Il retourne :

1. **optimisticState** : l'état temporaire de l'UI.
    
2. **addOptimisticUpdate(input)** : la fonction que vous appelez pour appliquer des mises à jour immédiates.
    

Regardez l'image ci-dessous. Elle montre clairement la relation entre l'état actuel et l'état optimiste :

![Anatomie](https://cdn.hashnode.com/res/hashnode/image/upload/v1765434835916/249e71eb-bba6-4b98-951a-feb397dc36e2.png align="center")

Voici ce qui s'y passe :

1. Nous passons l'état actuel et une fonction de mise à jour au hook `useOptimistic`.
    
2. La fonction de mise à jour prend l'état actuel et une entrée utilisateur pour calculer et retourner le prochain état optimiste.
    
3. L'entrée de la fonction de mise à jour est fournie via la fonction `addOptimistic(input)`.
    
4. Enfin, la valeur de l'état optimiste est utilisée dans le composant.
    

Construisons maintenant quelque chose d'excitant en utilisant ce hook pour mieux comprendre son fonctionnement interne.

## Comment construire un bouton Like optimiste

Nous allons construire la fonctionnalité d'un bouton Like de manière optimiste. Le flux sera le suivant :

* L'utilisateur clique sur le bouton Like.
    
* Nous mettons à jour l'état du bouton Like immédiatement et de manière optimiste.
    
* En parallèle, nous envoyons l'appel serveur pour persister la valeur dans la base de données (nous allons le simuler).
    
* Ensuite, nous gérons les scénarios d'erreur.
    

Tout d'abord, simulons un appel réseau vers le serveur en utilisant l'objet Promise de JavaScript et l'API web `setTimeout()` :

```javascript
// simuler un appel réseau vers le serveur
async function sendLikeToServer(postId) {
    await new Promise((r) => setTimeout(r, 700));

    if (Math.random() < 0.2) throw new Error("Network failed");
    console.log(`Sent a like for the post id ${postId}`);
    return { success: true };
}
```

La fonction `sendLikeToServer` prend un ID de post en paramètre et simule un faux appel réseau avec une Promise et un délai de 700 ms. Elle simule l'envoi d'une requête au serveur pour persister la valeur des likes d'un post.

Pour rendre cela un peu plus réaliste, nous avons créé une erreur aléatoire. La fonction lancera une erreur de manière aléatoire afin que nous puissions également comprendre le scénario de rollback.

Ensuite, nous allons créer la véritable source de vérité, l'état réel pour le compteur de likes :

```javascript
const [likes, setLikes] = useState(initialLikes);
```

Puis, créez la valeur d'état optimiste avec le hook `useOptimistic()` :

```javascript
 const [optimisticLikes, addOptimisticLike] = useOptimistic(
        likes, (currentLikes, delta) => currentLikes + delta);
```

Analysons bien cette déclaration :

* Nous avons passé la valeur de l'état réel (likes) et la fonction de mise à jour au hook `useOptimistic()`.
    
* Regardez la fonction de mise à jour, `(currentLikes, delta) => currentLikes + delta`. C'est une fonction fléchée qui reçoit la valeur actuelle des likes et un delta. Elle retourne la somme de la valeur actuelle et du delta. La logique de la valeur de retour correspond à votre propre logique métier. Pour incrémenter le compteur de likes, il est logique d'augmenter la valeur actuelle d'une valeur delta (de 1).
    
* Maintenant, la question est : comment obtenons-nous cette valeur delta ? Qui la passe ? C'est là que les valeurs de retour de `useOptimistic()` deviennent utiles. `addOptimisticLike` est une fonction par laquelle nous pouvons passer cette valeur delta. Comment ? Voyons cela.
    

Quand quelqu'un clique sur le bouton Like, nous devons gérer l'événement de clic et augmenter la valeur du compteur de likes. Voici donc une fonction `handleLike()` qui s'en occupe :

```javascript
const handleLike = async () => {
        addOptimisticLike(1);
        try {
            await sendLikeToServer(postId);
            setLikes((prev) => prev + 1);
        } catch (err) {
            console.error("Like failed:", err);
            setLikes((s) => s); 
        }
};
```

Beaucoup de choses se passent ici :

* Nous appelons la fonction `addOptimisticLike()` avec une valeur delta de 1. Cet appel garantit que la fonction de mise à jour `(currentLikes, delta) => currentLikes + delta` de `useOptimistic()` sera appelée. La valeur de retour sera affectée à l'état optimiste, c'est-à-dire `optimisticLikes`.
    
* Cette valeur d'état optimiste est celle que nous utilisons dans le JSX. Ainsi, nous voyons immédiatement le compteur de likes augmenter.
    
* Ensuite, nous effectuons le faux appel serveur, et nous mettons également à jour l'état réel, à condition que l'appel serveur ait réussi.
    
* En cas d'erreur, le contrôle passe dans le bloc catch, où nous effectuons un rollback de la valeur des likes vers la précédente. Cela synchronisera également la valeur de l'état optimiste avec un rollback.
    

Voici le code complet du composant `LikeButton` :

```javascript

import { startTransition, useOptimistic, useState } from "react";

// simuler un appel réseau vers le serveur
async function sendLikeToServer(postId) {
    await new Promise((r) => setTimeout(r, 700));

    if (Math.random() < 0.2) throw new Error("Network failed");
    console.log(`Sent a like for the post id ${postId}`);
    return { success: true };
}

// Le composant Like Button
export default function LikeButton({ postId, initialLikes = 0 }) {
    // la "vraie" source de vérité pour les likes (committée)
    const [likes, setLikes] = useState(initialLikes);
    // état optimiste et fonction de mise à jour
    const [optimisticLikes, addOptimisticLike] = useOptimistic(
        likes,
        (currentLikes, delta) => currentLikes + delta
    );

    const handleLike = async () => {
        // 1) Appliquer le changement optimiste *immédiatement*
        addOptimisticLike(1);

        // 2) Démarrer l'appel serveur en basse priorité pour éviter de bloquer l'UI

        try {
            await sendLikeToServer(postId);
            // En cas de succès, committer la mise à jour de l'état réel :
            // IMPORTANT : mettre à jour l'état réel pour que le snapshot optimiste finisse par correspondre
            setLikes((prev) => prev + 1);
        } catch (err) {
            // En cas d'erreur, rollback de l'état réel (ou déclencher un refetch)
            // Comme nous n'avons jamais incrémenté likes (réel), on laisse likes inchangé
            // Mais nous devrions afficher une erreur à l'utilisateur :
            console.error("Like failed:", err);
            // Optionnel : afficher un toast ou définir un état d'erreur
            // Et — pour forcer la vue optimiste à se rafraîchir et refléter l'état réel,
            // appeler setLikes avec la valeur actuelle
            setLikes((s) => s); // no-op mais forcera l'optimiste à refléter la
                                // valeur committée. Ou vous pouvez déclencher un re-fetch
                                // de l'état du post
        }
    };

    return (
        <div className="flex">
            <button onClick={handleLike}>❤️ {optimisticLikes}</button>
            <button onClick={() => startTransition(async () => handleLike())}>
                ❤️ {optimisticLikes}
            </button>
        </div>
    );
}
```

Avez-vous remarqué que nous avons enveloppé l'appel `handleLike()` avec `startTransition` ?

Sans cela, React nous donne un avertissement :

> « An optimistic state update occurred outside a transition or action. » (Une mise à jour d'état optimiste s'est produite en dehors d'une transition ou d'une action.)

C'est parce que les mises à jour optimistes sont des **mises à jour visuelles de basse priorité**, et non critiques.

L'utilisation de `startTransition()` garantit que :

* React ne bloque pas le rendu.
    
* Nous ne recevons pas l'avertissement.
    
* Nous obtenons une expérience optimiste fluide.
    

Les transitions font partie du modèle de concurrence de React qui nous aide à améliorer les performances des applications React. Si vous souhaitez apprendre diverses techniques d'optimisation des performances, [voici un guide en deux parties pour vous](https://www.youtube.com/watch?v=G8Mk6lsSOcw).

## Les pièges et les anti-patterns

Comme pour tout design pattern, nous devons être conscients des pièges possibles, des mauvaises utilisations et des anti-patterns. Voici quelques points à surveiller :

* Ne supposez pas que l'appel serveur sera toujours réussi. Les pannes de réseau arrivent, et vous devez avoir un moyen d'effectuer un rollback. Le rollback est le cœur de l'Optimistic UI. Omettre la logique de rollback entraînera des conséquences néfastes.
    
* N'essayez pas de cacher une mauvaise UX derrière des mises à jour optimistes. L'Optimistic UI n'est pas une solution miracle ou un remplacement pour des designs médiocres.
    
* N'effectuez pas de travail coûteux dans les mises à jour optimistes. Gardez la fonction de mise à jour optimiste légère, pure et rapide.
    

## **15 jours de design patterns React**

J'ai une excellente nouvelle pour vous : après mon initiative *40 days of JavaScript*, j'ai maintenant lancé une toute nouvelle initiative appelée [15 Days of React Design Patterns](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC).

Si vous avez aimé apprendre grâce à cet article, je suis sûr que vous adorerez cette série, présentant les 15+ design patterns React les plus importants. Découvrez-la et rejoignez-nous GRATUITEMENT :

[![https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC](https://cdn.hashnode.com/res/hashnode/image/upload/v1765439781697/751c2051-5dc2-4a88-bcc2-037f6ce0e91e.png align="center")](https://www.youtube.com/playlist?list=PLIJrr73KDmRyQVT__uFZvaVfWPdfyMFHC)

## **Avant de terminer...**

C'est tout ! J'espère que vous avez trouvé cet article instructif. Vous pouvez trouver tout le code source utilisé dans ce tutoriel sur le [GitHub de tapaScript](https://github.com/tapascript/15-days-of-react-design-patterns/tree/main/day-08).

[Restons connectés :](https://github.com/tapascript/15-days-of-react-design-patterns/tree/main/day-03/compound-components-patterns)

* Abonnez-vous à ma [chaîne YouTube](https://www.youtube.com/tapasadhikary?sub_confirmation=1).
    
* Récupérez la [React Hooks Cheatsheet](https://www.tapascript.io/books/react-hooks-cheatsheet).
    
* Suivez-moi sur [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) pour ne pas manquer les conseils quotidiens de montée en compétences.
    
* Rejoignez mon [serveur Discord](https://discord.gg/zHHXx4vc2H), et apprenons ensemble.
    
* Abonnez-vous à ma newsletter bimensuelle, [The Commit Log](https://tapascript.substack.com/subscribe?utm_medium=fcc).
    

À bientôt pour mon prochain article. D'ici là, prenez soin de vous et continuez d'apprendre.