---
title: Comment créer des blocs de notice en Markdown
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2024-06-10T09:00:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-notice-blocks-in-markdown
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Note--Tip--Warning
seo_title: Comment créer des blocs de notice en Markdown
---

Caution-specific-blocks-in-MarkDown-1.png
tags:
- name: markdown
  slug: markdown
seo_title: null
seo_desc: 'Le Markdown est un langage de balisage léger très populaire. Il est utilisé pour
  écrire de la documentation et même pour créer un site web complet. Par conséquent, presque
  tous nous utilisons fréquemment ce langage de balisage de temps en temps.

  Cependant, il y a quelques limi...'
---

Le Markdown est un langage de balisage léger très populaire. Il est utilisé pour écrire de la documentation et même pour créer un site web complet. Par conséquent, presque tous nous utilisons fréquemment ce langage de balisage de temps en temps.

Cependant, il y a quelques limitations à ce langage. Dans certains cas, nous ne pouvons pas ajouter autant de style ou de modifications.

Heureusement pour nous, il existe cinq fonctionnalités de mise en évidence pour des blocs de segments spécifiques tels que notice, tip, caution, important, et warning. Ces fonctionnalités sont également applicables dans le Markdown de GitHub.

Dans cet article, je vais parler de ces fonctionnalités en détail.

## Vidéo de présentation

Si vous souhaitez regarder une vidéo complète avec des directives étape par étape, alors vous pouvez regarder la vidéo dès maintenant !

%[https://www.youtube.com/watch?v=HMeCXobi90E]

## Comment créer un bloc de note en Markdown

Utilisez un bloc de note si vous voulez mettre en évidence des informations que les utilisateurs doivent prendre en compte – même lorsqu'ils parcourent simplement le texte.

Pour écrire un segment lié à une note, vous devez commencer par un crochet angulaire ( `>` ), puis vous devez spécifier le bloc de mise en évidence comme Note avec `[!NOTE]`.

Après cela, vous devez ajouter un crochet angulaire ( `>` ) à chaque nouvelle ligne que vous souhaitez inclure dans votre bloc de note spécifique.

Si vous voulez fermer le bloc de note, alors retirez le crochet angulaire supplémentaire dans la nouvelle ligne.

```markdown
> [!NOTE]
> Je veux que les lecteurs le lisent attentivement car il contient de nombreux documents importants.
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085135.png)
_Bloc de note_

Vous voyez que l'aperçu a déjà un joli symbole lié à la note.

## Comment créer un bloc de conseil en Markdown

Utilisez un bloc de conseil si vous voulez fournir des informations optionnelles pour aider un utilisateur à être plus performant.

Pour écrire un segment lié à un conseil, vous devez commencer par un crochet angulaire ( `>` ), puis vous devez spécifier le bloc de mise en évidence comme Tip avec `[!TIP]`.

Après cela, vous devez ajouter un crochet angulaire ( `>` ) à chaque nouvelle ligne que vous souhaitez inclure dans votre bloc de conseil spécifique.

Si vous voulez fermer le bloc de conseil, alors retirez le crochet angulaire supplémentaire dans la nouvelle ligne.

```markdown
> [!TIP]
> Utilisez la ligne de commande pour détecter et résoudre les erreurs !
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085600.png)
_Bloc de conseil_

Vous voyez que l'aperçu a déjà un joli symbole lié au conseil.

## Comment créer un bloc d'avertissement en Markdown

Utilisez un bloc d'avertissement si vous voulez fournir un contenu critique qui demande une attention immédiate de l'utilisateur en raison de risques potentiels.

Pour écrire un segment lié à un avertissement, vous devez commencer par un crochet angulaire ( `>` ), puis vous devez spécifier le bloc de mise en évidence comme Warning avec `[!WARNING]`.

Après cela, vous devez ajouter un crochet angulaire ( `>` ) à chaque nouvelle ligne que vous souhaitez inclure dans votre bloc d'avertissement spécifique.

Si vous voulez fermer le bloc d'avertissement, alors retirez le crochet angulaire supplémentaire dans la nouvelle ligne.

```markdown
> [!WARNING]
> NE SUPPRIMEZ PAS le fichier `package.json` !
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-085842.png)
_Bloc d'avertissement_

Vous voyez que l'aperçu a déjà un joli symbole lié à l'avertissement.

## Comment créer un bloc d'attention en Markdown

Utilisez un bloc d'attention si vous voulez sensibiliser les utilisateurs aux conséquences négatives potentielles d'une action.

Pour écrire un segment lié à une attention, vous devez commencer par un crochet angulaire ( `>` ), puis vous devez spécifier le bloc de mise en évidence comme Caution avec `[!CAUTION]`.

Après cela, vous devez ajouter un crochet angulaire ( `>` ) à chaque nouvelle ligne que vous souhaitez inclure dans votre bloc d'attention spécifique.

Si vous voulez fermer le bloc d'attention, alors retirez le crochet angulaire supplémentaire dans la nouvelle ligne.

```markdown
> [!CAUTION]
> N'exécutez pas le code sans commenter les cas de test.
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-090155.png)
_Bloc d'attention_

Vous voyez que l'aperçu a déjà un joli symbole lié à l'attention.

## Comment créer un bloc important en Markdown

Utilisez un bloc important si vous voulez fournir des informations cruciales nécessaires pour que les utilisateurs réussissent.

Pour écrire un segment lié à un important, vous devez commencer par un crochet angulaire ( `>` ), puis vous devez spécifier le bloc de mise en évidence comme Important avec `[!IMPORTANT]`.

Après cela, vous devez ajouter un crochet angulaire ( `>` ) à chaque nouvelle ligne que vous souhaitez inclure dans votre bloc important spécifique.

Si vous voulez fermer le bloc important, alors retirez le crochet angulaire supplémentaire dans la nouvelle ligne.

```markdown
> [!IMPORTANT]  
> Lisez les directives de contribution avant d'ajouter une pull request.
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-09-090430.png)
_Bloc important_

Vous voyez que l'aperçu a déjà un joli symbole lié à l'important.

## Conclusion

Merci d'avoir lu l'article entier. J'espère que vous avez appris quelque chose de nouveau ici.

Si vous avez apprécié les procédures étape par étape, alors n'oubliez pas de me le faire savoir sur [Twitter/X](https://twitter.com/Fahim_FBA) ou [LinkedIn](https://www.linkedin.com/in/fahimfba/). Je vous serais reconnaissant si vous pouviez m'endosser pour certaines compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/fahimfba/). Je vous recommande également de vous abonner à ma [chaîne YouTube](https://youtube.com/@FahimAmin) pour du contenu régulier lié à la programmation.

Vous pouvez également me suivre sur [GitHub](https://github.com/FahimFBA) si vous êtes intéressé par l'open source. Assurez-vous de vérifier [mon site web](https://fahimbinamin.com/) également.

Merci beaucoup ! 😀

### Référence

[[Markdown] An option to highlight a "Note" and "Warning" using blockquote (Beta) #16925](https://github.com/orgs/community/discussions/16925)