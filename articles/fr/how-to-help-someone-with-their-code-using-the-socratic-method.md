---
title: Comment aider quelqu'un avec son code en utilisant la méthode socratique
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2025-01-07T19:33:01.192Z'
originalURL: https://freecodecamp.org/news/how-to-help-someone-with-their-code-using-the-socratic-method
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/2RRq1BHPq4E/upload/904ec5e77783268f025191b07da29f08.jpeg
tags:
- name: coding
  slug: coding
- name: learning
  slug: learning
- name: freeCodeCamp.org
  slug: freecodecamp
seo_title: Comment aider quelqu'un avec son code en utilisant la méthode socratique
seo_desc: 'As a programming community, freeCodeCamp helps many people who have questions
  about their code. It can be quite tempting to simply provide the learner with the
  answer and move on, but that’s actually detrimental to the learning process. Here’s
  why:

  W...'
---

En tant que communauté de programmation, freeCodeCamp aide de nombreuses personnes qui ont des questions sur leur code. Il peut être très tentant de simplement fournir la réponse à l'apprenant et de passer à autre chose, mais cela est en réalité préjudiciable au processus d'apprentissage. Voici pourquoi :

Lorsque vous donnez la réponse à quelqu'un, vous le privez de ce moment "aha". Vous lui retirez l'opportunité d'apprendre à atteindre la conclusion par sa propre réflexion, et vous lui permettez plutôt de progresser avec un effort ou une réflexion minimale.

Alors, comment pouvez-vous aider au mieux quelqu'un avec son code ?

## Qu'est-ce que la méthode socratique ?

Le philosophe grec Platon était un élève d'un autre philosophe, Socrate. Dans les œuvres de Platon, il écrit souvent sur les débats que Socrate avait avec ses collègues et ses élèves.

Socrate commençait ces discussions en soulevant des croyances communes et en les examinant pour questionner leur compatibilité avec d'autres croyances, et guidait les gens à atteindre la vérité.

Mais comment cela se traduit-il dans nos interactions modernes à l'ère numérique ?

Considérons un exemple réel de l'une de nos communautés :

![Un message Discord de l'utilisateur Razzle Dazzle, disant "Comment trouver la somme des nombres dans un tableau ?"](https://cdn.hashnode.com/res/hashnode/image/upload/v1736179977371/7e087ee9-4b7e-4321-ade9-18019289320d.png align="center")

Vous pourriez être tenté de leur donner la réponse directe, comme cet exemple de code :

```javascript
const sum = nums.reduce((acc, el) => acc + el, 0);
```

Mais en faisant cela, vous avez effectué le raisonnement logique à la place de l'apprenant.

Au lieu de cela, vous devriez vous concentrer sur poser des questions précises pour les *guider* vers la réponse. Par exemple, vous pourriez commencer par demander :

> ❓ Comment trouveriez-vous la somme d'une liste de nombres sur papier, sans code ?

Il peut sembler contre-intuitif de poser à l'apprenant une question qui nécessite de s'éloigner du code, mais vous pointez en réalité vers la logique sous-jacente derrière sa question.

Supposons que l'apprenant réponde avec quelque chose comme :

> Je passerais chaque nombre, un par un, et je l'ajouterais à la somme des nombres précédents.

Alors que l'apprenant commence à répondre à vos questions, le dialogue devrait progresser dans ce format de question-réponse. Vos questions devraient devenir de plus en plus précises et ciblées avec la progression de l'apprenant vers la solution.

Par exemple, une série de questions pourrait ressembler à :

> Instructeur : "Bien, maintenant qu'est-ce qu'un tableau de nombres ?"  
> Élève : "Une liste ?"  
> Instructeur : "Bien ! Comment parcouririez-vous cette liste ?"  
> Élève : "Avec une boucle for."  
> Instructeur : "Et que doit faire votre boucle à chaque itération ?"  
> Élève : "Ajouter le nombre actuel à la somme."  
> Instructeur : "Où pouvez-vous trouver la somme ?"  
> Élève : "Je pourrais la mettre dans une variable en dehors de la boucle."  
> Instructeur : "Bien, maintenant vous êtes prêt à essayer d'écrire le code."  
> — exemple original écrit pour cet article

À ce stade, l'apprenant connectera probablement les points et atteindra la solution finale.

## Socrate dans la culture moderne

Apprendre la méthode socratique est difficile. En fait, beaucoup ne la rencontrent pas avant leurs études universitaires. Mais il existe des exemples dans la culture pop moderne qui peuvent vous aider à comprendre comment fonctionne la méthode socratique.

La série télévisée House, M.D. regorge d'exemples. Prenons cet échange de l'épisode intitulé "Trois Histoires" :

> House : "Les calculs rénaux causeraient quoi ?"  
> Élève : "Du sang dans les urines."  
> House : "De quelle couleur est votre pipi ?"  
> Élève : "Jaune."  
> House : "De quelle couleur est votre sang ?"  
> Élève : "Rouge."  
> House : "Quelles couleurs ai-je utilisées ?"  
> Élève : "Rouge, jaune et marron.  
> House : "Et marron. Qu'est-ce qui cause le marron ?"  
> Élève : "Des déchets".  
> — (Frapier, 2008)¹

Vous remarquerez comment cet échange a eu lieu. Le but de House ici n'était pas de *donner* la réponse à l'apprenant, mais de poser des questions déductives pour *guider* l'apprenant à atteindre la réponse par lui-même.

Considérons le film populaire The Matrix :

> Morpheus : "As-tu déjà fait un rêve, Neo, dont tu étais si sûr qu'il était réel ?"  
> Neo : "Ce n'est pas possible..."  
> Morpheus : "Être quoi ? Être réel ?"  
> Morpheus : "Et si tu ne pouvais pas te réveiller de ce rêve, Neo ? Comment ferais-tu la différence entre le monde du rêve et le monde réel ?"  
> — (Wachowski & Wachowski, 1999)²

Dans cette scène, Morpheus applique la méthode socratique pour amener Neo à remettre en question ses perceptions de la réalité. C'est un exemple plutôt dramatique, mais le principe reste le même : au lieu de dire à l'apprenant comment il devrait penser, vous le guidez pour qu'il atteigne la conclusion par sa propre volonté.

Enfin, regardons un exemple de Legally Blonde :

> Elle : "Votre père a été abattu alors que vous étiez sous la douche ?"  
> ...  
> Chutney : "Oui. Je me lavais les cheveux."  
> Elle : "Mademoiselle Windham, pouvez-vous nous dire ce que vous faisiez plus tôt dans la journée ?"  
> Chutney : "Je me suis levée, je suis allée chez Starbucks, je suis allée à la salle de sport, j'ai fait une permanente et je suis rentrée chez moi."  
> Elle : "Où vous êtes allée sous la douche."  
> Chutney : "Oui."  
> ...  
> Elle : "...Aviez-vous déjà fait une permanente auparavant, Mademoiselle Windham ?"  
> Chutney : "Oui."  
> Elle : "Combien, diriez-vous ?"  
> Chutney : "Deux par an depuis mes douze ans. Faites le calcul."  
> ...  
> Elle : "Chutney, pourquoi les boucles de Tracy Marcinko ont-elles été ruinées lorsqu'elle a été arrosée ?"  
> Chutney : "Parce qu'elles ont été mouillées."  
> Elle : "C'est exact. Parce que la première règle cardinal de l'entretien des permanentes n'est-elle pas que vous êtes interdit de mouiller vos cheveux pendant au moins vingt-quatre heures après une permanente, au risque de désactiver l'ammonium thiglycolate ? Et quelqu'un qui a eu — trente permanentes ? — tout au long de sa vie, ne serait-il pas bien conscient de cette règle ? Et si vous n'étiez pas, en fait, en train de vous laver les cheveux, comme je le suspecte, puisque vos boucles sont toujours intactes, n'auriez-vous pas entendu le coup de feu ?"  
> —(Luketic, 2001)³

La méthode socratique peut souvent être observée dans le domaine du droit, et cela sert d'excellent exemple. À travers cet échange, Elle ne cherche pas à guider Chutney vers une conclusion, mais plutôt les *spectateurs* (dans ce cas, le jury). C'est une distinction importante pour une communauté comme la nôtre : où engager une discussion socratique avec un membre peut en réalité bénéficier aux membres actuels et futurs qui peuvent observer ou revisiter votre conversation.

## But de la méthode socratique

Il est important de reconnaître que le but de la méthode socratique n'est *pas* de présenter un échange rapide d'informations. Au lieu de cela, l'objectif est d'abord de faire réaliser à l'apprenant qu'il sait moins qu'il ne le croit, puis de le guider vers la réponse à travers des questions qui suscitent certains processus de pensée.⁴

Lorsque l'on applique cela à l'apprentissage de la programmation, il est important de se rappeler la phrase "remettez en question vos hypothèses". Nous supposons souvent que nous savons ce que le code que nous avons écrit fait, donc notre première étape lorsqu'il ne fonctionne pas est d'examiner ces hypothèses.

Alors que nous guidons les apprenants à travers le processus de débogage, nous voulons poser des questions qui font de même. Une question courante dans votre répertoire devrait être "Que fait cette ligne de code ?". Lorsque l'apprenant répond avec des informations inexactes, répondez avec des questions qui creusent dans des composants plus petits du code – brisez le problème en morceaux, pour ainsi dire.

Considérons cet exemple :

> Apprenant : "mais peut-être que cela ne fonctionnerait pas parce que je dois trouver le livre et non l'id dans le livre"  
> Instructeur : "Correct. Maintenant, la bonne nouvelle est que nous avons une fonction qui ferait ostensiblement cela. La mauvaise nouvelle est que cette fonction ne fait pas cela. Que fait cette fonction à la place ?"  
> Apprenant : "retourne bookId"  
> — source de notre communauté Discord⁵

En posant la question "Que fait cette fonction à la place ?", l'instructeur a fourni la direction pour que l'apprenant atteigne la conclusion correcte sans avoir à fournir d'informations spécifiques. L'apprenant savait déjà que la fonction ne se comportait pas comme prévu, et l'instructeur a posé la question pour remettre en question l'hypothèse de l'apprenant selon laquelle la fonction *se comportait*.

Voici un autre exemple :

> Instructeur : "C'est l'exemple du Chalenge (sic). Avez-vous suivi cet exemple qu'ils ont donné ?"  
> Apprenant : "oui mais je n'ai pas compris la boucle for-in, je n'ai pas compris "(const food in refigerator)", devoir indiquer le nom de la propriété de chaîne avec const ou let était confus (ce n'est plus le cas)"  
> Instructeur : "Ok, alors commençons ici au lieu de la solution complète au Challenge"  
> Instructeur : "Que fait ce code lorsque vous l'exécutez ?"  
> ...  
> Apprenant : "chacune des clés de l'objet a été définie sur la variable food qui a été créée dans la boucle for-in, elle parcourt ensuite l'objet et enregistre la clé et la valeur assignée à la clé ?"  
> — source de notre communauté Discord⁶

Encore une fois, nous pouvons voir comment l'instructeur se concentre sur poser des questions précises qui guident l'utilisateur vers les solutions *par son propre raisonnement*.

> ❗ C'est l'objectif ultime de la méthode socratique : guider l'apprenant à atteindre la conclusion logique uniquement par son propre raisonnement.

## Avantages à long terme de la méthode socratique

La méthode socratique n'est pas uniquement bénéfique pour résoudre la solution immédiate. Le processus de raisonnement déductif appliqué dans cette approche peut également servir l'apprenant sur le long terme.

Le processus de poser des questions à un apprenant pour remettre en question ses hypothèses et ses connaissances, et le guider vers la solution, est quelque chose qui peut également être internalisé. C'est un outil puissant à avoir dans votre répertoire pour aborder le débogage, isoler les hypothèses, et même apprendre à articuler un problème.

C'est-à-dire qu'en guidant un apprenant à travers cette conversation de question-réponse, l'apprenant peut également repartir avec la capacité de se poser *lui-même* ces questions. Il peut prendre le même processus de poser des questions de plus en plus précises comme un cheminement logique et le parcourir mentalement lorsqu'il rencontre des problèmes futurs avec son code (ou même dans d'autres aspects de la vie) !

## Conclusion

Fournir une solution directement à un apprenant inhibe sa croissance intellectuelle et le prive de l'expérience gratifiante qui vient de l'atteinte de sa propre conclusion logique. En utilisant des techniques comme la méthode socratique, nous pouvons favoriser un environnement éducatif plus fort et plus efficace qui permet aux apprenants de grandir et de s'épanouir.

> 💡 Si vous avez reçu cet article en réponse à un message sur un forum, un commentaire Reddit, un message Discord, ou une autre communication où vous avez donné une solution fonctionnelle à un autre apprenant, veuillez considérer les mérites de cette méthode à la place.

Cette approche peut sembler fastidieuse et longue, et parfois elle l'est. Il est bien plus rapide (et probablement plus facile) de donner à quelqu'un le code qui résout son problème.

Mais cette approche, plus souvent qu'autrement, nuit à l'apprenant à la fin. Et, si vous pardonnerez à cet auteur une anecdote, j'ai vu des gens se frustrer lorsqu'ils sont le sujet d'une approche socratique, ou perdre patience avec la conversation de va-et-vient. Mais je ne les ai *jamais* vus mécontents ou déçus par ce résultat final – le moment "aha" où ils déduisent la solution au problème par leur propre raisonnement.

### Sources :

1. ¹ Frapier, M. (2008). Being Nice is Overrated: House and Socrates on the Necessity of Conflict. In *House and Philosophy* (pp. 100–101). John Wiley & Sons, Inc.
    
2. ² Wachowski, L., & Wachowski, L. (Directeurs). (1999, 24 mars). *The Matrix* (Z. Staenberg, Ed.). Warner Bros.
    
3. ³ Luketic, R. (Directeur). (2001, 13 juillet). *Legally Blonde* (A. Brandt-Burgoyne, Ed.). MGM Distribution Co.
    
4. ⁴ Frapier, M. (2008). Being Nice is Overrated: House and Socrates on the Necessity of Conflict. In *House and Philosophy* (p. 103). John Wiley & Sons, Inc.
    
5. ⁵ lightskingeneral & plamoni (2024, 4 janvier). [Conversation Discord]. Discord. Récupéré le 2025, 6 janvier, de [https://discord.com/channels/692816967895220344/718214639669870683/1192488621043888198](https://discord.com/channels/692816967895220344/718214639669870683/1192488621043888198)
    
6. ⁶ lightskingeneral & jeremylt (2023, 13 novembre). [Conversation Discord]. Discord. Récupéré le 2025, 6 janvier, de [https://discord.com/channels/692816967895220344/718214639669870683/1173733715109761065](https://discord.com/channels/692816967895220344/718214639669870683/1173733715109761065)
    

Un merci spécial à ArielLeslie et JeremyLT pour leur aide avec cet article.