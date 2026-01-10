---
title: Transformer une recherche d'emploi en un projet de développement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-30T18:08:00.000Z'
originalURL: https://freecodecamp.org/news/turning-a-job-hunt-into-a-dev-project-2018
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/cover-4.png
tags:
- name: careers
  slug: careers
- name: Job Hunting
  slug: job-hunting
- name: learning
  slug: learning
seo_title: Transformer une recherche d'emploi en un projet de développement
seo_desc: 'By Scott Spence

  Cliffs/TL;DR

  I made a recruiter FAQ on my personal site for recruiters and created an online
  CV.

  Preamble

  Apologies up front about this post if it comes across as entitled or ranty and I''m
  sure a lot of people will disagree with my ap...'
---

Par Scott Spence

## Cliffs/TL;DR

J'ai créé une [FAQ pour les recruteurs](https://scottspence.me/faq) sur mon site personnel et un [CV en ligne](https://cv.scottspence.me/).

## Préambule

Je m'excuse d'avance si cet article semble prétentieux ou râleur, et je suis sûr que beaucoup de gens ne seront pas d'accord avec mon approche.

Je vais essayer de ne pas être trop cynique ici, alors commençons par cela. Je pense que le recrutement technique est dans un très mauvais état ! Cela dure depuis longtemps (au moins depuis 2010).

Appelons cela la fatigue de la recherche d'emploi/trouver des talents, car en tant que développeurs, nous avons des fatigues dans d'autres domaines, mais celle-ci n'est pas de notre fait.

Commencer une recherche d'emploi et diffuser votre CV générera beaucoup d'appels où le mot-clé le plus irrelevant sur votre CV générera des appels indésirables de la part de recruteurs qui semblent parfois désespérés.

Poste urgent à pourvoir : Team Lead, 6+ ans d'expérience - début immédiat £900 par jour, contrat de 3 mois.

D'accord, c'est un peu dur ! mais c'est la vérité, Ruth ! Cela semble aussi un peu cliché maintenant.

En tant que développeur, j'ai commencé à remarquer des schémas avec chaque appel que je recevais, les mêmes questions étaient posées encore et encore. En tant que développeur, je veux aussi garder les choses [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) pour économiser du temps (à moi et au recruteur).

Ainsi, j'ai décidé d'ajouter une section [FAQ](https://scottspence.me/faq) à mon portfolio personnel, une liste de toutes les questions qui m'avaient été posées lors des nombreux appels précédents. Ainsi, plutôt que de passer dix minutes au téléphone avec le recruteur pour qu'il me qualifie pour le poste, il pouvait faire la *vaste* majorité de cela avec la [FAQ](https://scottspence.me/faq) fournie, presque comme une fiche de poste inversée. Tout ce qu'il avait à faire était de LIRE la [FAQ](https://scottspence.me/faq) ! Ensuite, il pouvait cocher mes souhaits et besoins à partir de la liste que j'avais déjà fournie.

Pour une raison quelconque, cependant, beaucoup de recruteurs insistaient pour me parler, prenant du temps dans ma journée. Ils procédaient ensuite à poser les mêmes questions que tous les autres recruteurs. Cela les qualifiait à mes yeux comme des personnes qui ne valorisaient pas mon temps et ils perdaient toute crédibilité qu'ils auraient pu avoir avec moi.

J'ai donc créé un site, un portfolio, qui listait tout ce que vous pourriez vouloir savoir sur moi. J'ai ajouté la section À propos, qui couvre mon histoire et mon parcours en codage, comment j'en suis arrivé là et où je suis maintenant. Il y a aussi une section Now et une section Uses. Elles décrivent ce que je fais maintenant dans ma vie et les outils que j'utilise, comme l'éditeur de code et le matériel.

Les pages du portfolio sont toutes en markdown générées par Gatsby, donc lorsqu'une question était posée qui n'était pas sur la liste, je pouvais l'ajouter rapidement. L'utilisation de Netlify a rendu cela encore plus simple, car il suffisait d'un push Git et les changements étaient en ligne en quelques minutes.

Créer un site, cela est plus destiné aux employeurs potentiels qu'aux recruteurs, et bien que la majorité des recruteurs vous parleront comme s'ils étaient ceux qui vous considèrent pour le poste, ils ne sont que la première étape d'un processus qui peut être assez long.

Alors, oublions les recruteurs pour l'instant et concentrons-nous sur la principale chose dont vous avez besoin pour vous faire connaître si vous cherchez un emploi : votre CV.

Créer un [CV](https://cv.scottspence.me/), j'ai fait l'effort de créer un site de base en utilisant ma stack technologique préférée **[teh JAMStack behbeh!](https://jamstack.org/)** J'ai utilisé l'outil [JSONresume](https://jsonresume.org/) pour détailler tous les rôles que j'avais occupés, puis j'ai utilisé le JSONresume comme guide pour la création des composants individuels du [CV](https://cv.scottspence.me/).

Si vous souhaitez commencer avec votre propre CV JSON, vous pouvez exécuter la commande npm `npx resume-cli init` pour démarrer le vôtre.

N'hésitez pas à [utiliser mon CV](https://github.com/spences10/cv) comme modèle pour le vôtre, tout ce que vous avez à faire est de générer votre CV et de le pousser vers now.sh.

C'était mon historique d'emploi complet et assez long, et comme je cherchais un emploi dans un nouveau domaine, la grande majorité n'était pas pertinente pour ma recherche d'emploi. C'est pourquoi j'ai décidé, plutôt que de diffuser mon [CV](https://cv.scottspence.me/) partout, de publier la liste des réponses aux questions que les recruteurs me posaient toujours lorsqu'ils m'appelaient. Ainsi, plutôt que de les faire parcourir mon historique d'emploi principalement irrelevant, ils pouvaient obtenir les réponses aux questions qu'ils voulaient poser. Le [CV](https://cv.scottspence.me/) était là s'ils voulaient plus de détails sur moi, tout ce qu'ils avaient à faire était de LIRE !

À mon avis, le [portfolio personnel](https://scottspence.me) et le site [CV](https://cv.scottspence.me/) étaient une bonne indication de mon niveau de compétence actuel en matière de style et de stack préférée. En réalité, personne ne s'en soucie tant que cela a l'air bien, et les recruteurs encore moins, car cela ne répond pas aux questions qu'ils veulent poser.

![build-it](https://thepracticaldev.s3.amazonaws.com/i/ptve31bchle6hgg6wuaq.gif)

Ce n'était pas un champ de rêves cependant ! Alors, comment faire pour que les recruteurs viennent sur ma page ? Eh bien, plutôt que d'avoir un CV au format MS Word que je posterais sur tous les sites d'emploi que je pourrais trouver, j'avais un lien vers ma [FAQ](https://scottspence.me/faq) sur un document MS Word ! ?

Sur le document MS Word, j'avais tous les termes de recherche qu'un recruteur rechercherait, JavaScript, React, HTML, CSS et ainsi de suite en bas du document. En haut, il y avait un message de salutation :

![jobsite-cv](https://www.freecodecamp.org/news/content/images/2019/06/jobsite-cv.jpg)

C'était un bonjour amical et quelque chose de différent de ce qui doit être très répétitif.

J'ai utilisé Google Analytics sur la [FAQ](https://scottspence.me/faq) et le [CV](https://cv.scottspence.me/) pour voir combien de trafic ils recevaient. La [FAQ](https://scottspence.me/faq) en recevait beaucoup plus que le [CV](https://cv.scottspence.me/), donc je pouvais en déduire que les recruteurs obtenaient les réponses à leurs questions sans avoir à décrocher le téléphone. Win Win, non ?

Les statistiques n'étaient cependant pas excellentes, avec un taux de rebond d'environ 3 secondes ? vous pouviez voir que la grande majorité des recruteurs préféraient décrocher le téléphone plutôt que LIRE les informations fournies.

> **Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://thelocalhost.blog/).**