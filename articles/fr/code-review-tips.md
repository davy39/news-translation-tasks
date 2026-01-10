---
title: Comment donner un bon feedback pour des revues de code efficaces
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-04-03T16:49:44.000Z'
originalURL: https://freecodecamp.org/news/code-review-tips
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Cover-for-first-FCC-article.png
tags:
- name: code review
  slug: code-review
- name: Feedback
  slug: feedback
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: Comment donner un bon feedback pour des revues de code efficaces
seo_desc: "Hey, open sourcer! \U0001F60A I’ve heard through the digital webs that\
  \ you’ve become quite the wordsmith when it comes to giving feedback on pull requests\
  \ and want to learn something new. \nNo worries, I’ve been there myself when I started\
  \ getting more comfor..."
---

Hey, contributeur open source ! 😊 J'ai entendu à travers les toiles numériques que tu es devenu assez doué pour donner des feedbacks sur les pull requests et que tu veux apprendre quelque chose de nouveau. 

Pas de souci, j'ai été à ta place lorsque j'ai commencé à me sentir plus à l'aise dans le monde de l'open source. Alors, prends une chaise, ton en-cas ou ta boisson préféré(e) (je recommande fortement l'eau. C'est frais et bon pour la santé ! 😉), et ton carnet (ou dans ce cas, ton ordinateur portable). Parce que je vais partager cinq techniques qui te feront passer pour un boss dans la revue des pull requests.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/neil-encouragement.gif)
_Neil deGrasse Tyson dit "Allons-y !" pour te donner confiance !_

## Technique de Feedback 1 : La Revue "Montrer et Raconter"

Pour cette technique, tu fournis des captures d'écran ou des liens vers d'autres sources qui aident à expliquer le bénéfice de la nouvelle approche que tu suggères à ton fellow contributeur. Voici comment faire :

D'abord, prends une capture d'écran de ce que tu veux transmettre dans ton feedback. Je recommande fortement d'utiliser [Fireshot](https://getfireshot.com/using.php). C'est un moyen facile de prendre des captures d'écran sur ton ordinateur.  
 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/screenshot-Gif.gif)
_Ceci est un GIF de quelqu'un prenant une capture d'écran d'une image via un Mac_

Ensuite, va dans le dépôt de ton choix et clique sur **Pull Requests** 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/repo-tabs.png)
_Un cercle jaune entoure le troisième onglet appelé "Pull Requests". Clique là pour choisir la PR que tu veux revoir._

Une fois que tu as choisi la pull request que tu veux revoir, clique sur **Files Changed** : 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-1-1.png)

Ajoute tes commentaires, puis fais glisser et dépose ton image dans la zone de texte. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/chameleon-example.png)
_Dans une zone de texte,_

Clique sur **Submit review** et voilà, c'est fait ! 😊  


![Image](https://www.freecodecamp.org/news/content/images/2023/04/Submit.png)
_Il y a un bouton vert disant "Submit Review". Clique dessus après avoir terminé ta revue._

D'après mon expérience, ce type de revue est utile lorsque tu donnes un feedback sur des pull requests qui nécessitent l'ajout d'une fonctionnalité au site web d'un projet open source (par exemple un logo) ou une image dans l'un de ses fichiers Markdown. Cela peut aider la personne à voir comment sa contribution impacte le projet global. 

C'est comme si tu regardais une publicité pour un savon facial et que tu vois les scènes où ils montrent des gros plans de la façon dont le produit rend ta peau plus saine. Montrer à quelqu'un une image de ce qui doit être corrigé peut aider à transmettre plus clairement ce qui se passe.

En parlant de peau, voici une autre stratégie où tes pouvoirs de caméléon, je veux dire tes compétences d'adaptabilité, peuvent être utiles.   

## Technique de Feedback 2 : La Revue "Caméléon"

Le "Caméléon" est une technique de feedback où tu adaptes ta revue de PR en fonction du type de contribution que ton pair fait. C'est comme la façon dont un caméléon change la couleur de sa peau pour s'intégrer à son environnement (sans la partie se cacher des prédateurs, bien sûr 😉). 

Par exemple, si tu révise une pull request basée sur du texte comme celle dans l'image ci-dessous, je recommande fortement de donner un feedback via des questions dialogiques (par exemple, comment cette ressource se démarque-t-elle des autres cours qui enseignent JavaScript ?). 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Chameleon-example.png)

Cette technique est utile car elle encourage le destinataire de ta revue à réfléchir profondément à sa contribution. Elle t'apprend également à adapter ton feedback en fonction du type de pull request que tu révise.  

Maintenant que tu connais le Caméléon, la prochaine technique que tu vas apprendre est celle qui peut t'aider à parcourir des champs, je veux dire, de longues lignes de code.   

## Technique de Feedback 3 : Deux Petits Pois dans une Cosse

Les "Deux Petits Pois dans une Cosse" est une technique de revue de PR où tu commentes une ligne de code dans la conversation tandis qu'un autre contributeur donne un feedback sur une autre ligne de code dans la même pull request.  

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/two-peas-in-a-pod-one.png)
_Deux contributeurs commentent une ligne de code_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/two-peas-in-a-pod.png)
_Mon commentaire sur une ligne de code différente dans la même pull request_

Comme montré dans la première image, il est utile de souligner pourquoi certaines méthodes ne fonctionneront pas et de discuter de certaines alternatives que le demandeur de pull request peut utiliser. De plus, envisage de commenter une autre façon d'améliorer la PR une fois que tu as choisi la ligne de code que tu veux améliorer. 

Lorsque tu utilises cette méthode, je recommande fortement d'encourager toi et ton fellow relecteur à choisir une ligne de code qui correspond à vos forces car cela rendra le feedback plus facile à donner. 

Étant donné que mon expérience est dans l'écriture et l'éducation, j'ai décidé de commenter la ligne basée sur du texte que tu vois dans la deuxième image tandis que les autres contributeurs se sont concentrés sur l'amélioration de l'élément image en raison de leur expérience plus poussée en codage. 

Cette méthode t'aide à développer tes compétences en communication écrite et rend finalement la revue des pull requests moins stressante. C'est deux bénéfices pour le prix d'un ! 😊 Cool, non ? 😉 

En parlant de réduire ton stress, j'ai une autre stratégie qui te fera passer pour [the Flash de _The Justice League_](https://dcau.fandom.com/wiki/Flash) dans la revue des pull requests !

## Technique de Feedback 4 : La Revue "Apprends-leur"

Cette revue "Apprends-leur" est une technique de revue de PR où tu instructes essentiellement ton pair sur la façon d'améliorer sa PR au lieu de simplement pointer les problèmes dans la PR. 

Voici quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Teach-em-example-2-jpg.jpg)
_Ma suggestion : transformer l'élément &lt;div&gt; en un élément HTML plus sémantique._

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Teach-em-example-1.jpg)
_Je donne des conseils au contributeur sur la façon de rendre ses contributions basées sur du code plus accessibles_

Lorsque tu utilises cette technique, je recommande fortement de pointer une zone d'amélioration. Ensuite, tu peux brièvement enseigner une stratégie qu'ils pourraient utiliser à l'avenir. 

Cette approche peut aider à améliorer tes compétences en codage et développer tes compétences en communication écrite, ce qui est très utile dans le monde de la tech.  

Maintenant, il ne reste plus qu'une technique qui t'aidera à améliorer tes compétences en revue de PR. 

## Technique de Feedback 5 : La Revue "Suggestion"

Si tu te concentres sur d'autres projets open source, que tu as une date limite pour une tâche, ou que tu es simplement fatigué après une longue journée de travail mais que tu veux revoir des pull requests, cette technique de feedback sera l'outil ultime dans ton kit de contributeur open source. Elle se concentre sur le fait de donner un feedback constructif à travers ta revue.

Voici comment faire : 

1. Clique sur l'onglet **Files Changed** d'une pull request d'une personne :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-1.png)
_Il y a quatre onglets sous une pull request d'une personne. Le dernier "Files changed" est encerclé en jaune. C'est l'onglet que tu choisis dans la première étape_

2.  Survole la ligne de code que tu veux revoir et clique sur le signe plus bleu :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-2.png)
_Il y a un signe plus bleu sur la ligne de code qui a un couvert jaune. Cela indique que tu as choisi une ligne de code que tu veux revoir._

3.  Clique sur l'icône de fichier qui a un plus en haut et un signe moins en bas :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-3-2.png)

4.  Réécris la ligne de code, en l'améliorant comme tu le juges nécessaire :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-4.png)
_Il y a une flèche jaune pointant vers une zone qui dit ```suggestion. C'est là que tu réécris la ligne de code que tu as choisie de revoir._

5.  Clique sur **Add Single Comment**

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Suggestion-Step-5-1.png)
_Il y a une flèche jaune pointant vers le bouton "Add single comment". C'est ce sur quoi tu cliques pour insérer ta suggestion dans la ligne de code de la personne._

6.  Écris ton commentaire dans la zone de texte, clique sur **Request Changes**, et **Submit Review**.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Final-Suggestion-Step-2.png)
_La première flèche pointe vers une zone de texte, l'endroit où tu tapes ton commentaire. La deuxième flèche pointe vers le dernier bouton radio étiqueté "Request Changes". La flèche finale pointe vers un bouton vert étiqueté "Submit review"._

Je recommande fortement d'utiliser cette technique de feedback pour les pull requests basées sur du texte car elle montrera ta suggestion à la personne qui a fait la pull request, ce qui est particulièrement utile si tu es trop fatigué ou que tu n'as pas le temps de donner une leçon de grammaire (fais-moi confiance, j'y ai été). 

Comme les autres techniques de feedback que j'ai mentionnées précédemment, la revue de suggestion peut également t'aider à améliorer tes compétences orientées détail car elle t'encourage à penser à la meilleure façon de transmettre ton feedback. C'est plutôt génial ! 😊

## Conclusion

Félicitations, tu as maintenant cinq techniques de feedback dans ta boîte à outils Open Sourcer !  

Avant de te laisser partir, je veux que tu te souviennes de ceci. Les contributions open source commencent et finissent avec toi, alors utilise tes pouvoirs avec sagesse. Maintenant, sors et sois le meilleur relecteur de pull requests dans l'open source ! 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/deadpool.gif)
_Deadpool et son équipe marchent lentement vers leur prochain défi. Sois comme Deadpool avec tes revues de pull requests ! :)_



## Crédits

GIF Let's Do This par [National Geographic](https://giphy.com/gifs/natgeochannel-startalk-JykvbWfXtAHSM)

GIF Super Hero Walking par [20th Century Fox Home Entertainment](https://media.giphy.com/media/l0Iy6hheGg52GcJt6/giphy.gif)

GIF Screenshot de "How to Take a Screenshot on a MacBook" par [Hung Nguyen](https://smallpdf.com/blog/how-to-screenshot-on-mac)