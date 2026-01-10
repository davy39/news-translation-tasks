---
title: Série de posts « tmux en pratique »
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T14:27:33.000Z'
originalURL: https://freecodecamp.org/news/tmux-in-practice-series-of-posts-ae34f16cfab0
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb240740569d1a4cac0c7.jpg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Série de posts « tmux en pratique »
seo_desc: 'By Alexey Samoshkin

  Explore tmux and its tough questions and tricks, including features, nested sessions,
  scrollback buffer, clipboard integration, and iTerm2 integration.

  I just finished my writings on tmux topic.

  There are several topics I’ve cover...'
---

Par Alexey Samoshkin

#### Explorez tmux et ses questions complexes et astuces, incluant les fonctionnalités, les sessions imbriquées, le tampon de défilement, l'intégration du presse-papiers et l'intégration avec iTerm2.

Je viens de terminer mes écrits sur le sujet tmux.

Il y a plusieurs sujets que j'ai couverts jusqu'à présent. L'objectif de ce post est d'être une page d'index pour toutes les parties de la série « tmux en pratique ». Bonne lecture :

**Partie 1.** [Tmux en pratique : exploration des sessions tmux locales et imbriquées à distance](https://medium.com/@alexeysamoshkin/tmux-in-practice-local-and-nested-remote-tmux-sessions-4f7ba5db8795). Il discute également des fonctionnalités de tmux en général, de leur pertinence pour les scénarios locaux et distants, et de la manière de configurer et paramétrer tmux pour supporter les sessions imbriquées.

**Partie 2.** [tmux en pratique : intégration de iTerm2 et tmux](https://medium.com/@alexeysamoshkin/tmux-in-practice-iterm2-and-tmux-integration-7fb0991c6c01) inclut les avantages et inconvénients de l'utilisation de iTerm2 vs tmux localement. Il montre comment configurer un profil iTerm2 pour outrepasser les mappings de touches afin de déclencher des actions analogues à tmux.

**Partie 3.** [tmux en pratique : tampon de défilement](https://medium.com/@alexeysamoshkin/tmux-in-practice-scrollback-buffer-47d5ffa71c93). Explore la différence entre les tampons de défilement du terminal et de tmux. Montre comment ajuster le mode copie, le défilement et le comportement de sélection de la souris dans tmux.

**Partie 4.** [tmux en pratique : intégration avec le presse-papiers système](https://medium.com/@alexeysamoshkin/tmux-in-practice-integration-with-system-clipboard-bcd72c62ff7b). Crée un pont entre le tampon de copie de tmux et le presse-papiers système, pour stocker le texte sélectionné dans le presse-papiers d'OSX ou de Linux de manière à répondre aux scénarios d'utilisation locaux et distants.

**Partie 5.** [tmux en pratique : copier du texte depuis une session distante en utilisant un tunnel SSH distant et un service systemd](https://medium.com/@alexeysamoshkin/tmux-in-practice-copy-text-from-remote-session-using-ssh-remote-tunnel-and-systemd-service-dd3c51bca1fa). Une autre manière de copier du texte depuis une session distante vers le presse-papiers local.

Tout ce qui est discuté ici peut être vu en action en consultant mon projet de configuration tmux sur Github : [tmux-config](https://github.com/samoshkin/tmux-config)