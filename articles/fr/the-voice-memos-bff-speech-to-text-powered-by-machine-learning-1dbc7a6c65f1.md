---
title: "Le meilleur ami des mémos vocaux\n\x14\nComment faciliter la conversion Speech2Text\
  \ avec le Machine Learning"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:07:43.000Z'
originalURL: https://freecodecamp.org/news/the-voice-memos-bff-speech-to-text-powered-by-machine-learning-1dbc7a6c65f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9NU-RPt9yreyuqqOLQKQYA.jpeg
tags:
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Machine Learning
  slug: machine-learning
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
- name: writing
  slug: writing
seo_title: "Le meilleur ami des mémos vocaux\n\x14\nComment faciliter la conversion\
  \ Speech2Text avec le Machine Learning"
seo_desc: 'By Rafael Belchior

  Do you think recording voice memos is inconvenient because you have to transcribe
  them? Do you waste your precious voice memos because you never write them down?
  Do you feel like you are not unlocking the full potential of what you...'
---

Par Rafael Belchior

Pensez-vous que l'enregistrement de mémos vocaux est inconvénient car vous devez les transcrire ? Gâchez-vous vos précieux mémos vocaux parce que vous ne les écrivez jamais ? Avez-vous l'impression de ne pas exploiter tout le potentiel de ce que vous enregistrez ?

Oui, c'est frustrant. ?

![Image](https://cdn-media-1.freecodecamp.org/images/Ldug-95Ai5jva-tYYx4uQTcqzRj7bAFHqdsa)
_Écrivez, écrivez, écrivez._

Je suis étudiant en master d'informatique. Comme je pense que tout travail et pas de jeu fait de moi un garçon terne, j'ai décidé d'investir un peu de temps à faire quelque chose de différent. Où ? Dans [le groupe d'étudiants auquel j'appartiens](http://www.gce-neiist.org), [en interviewant un professeur.](http://www.gce-neiist.org/articles)

J'ai parlé au professeur Rui Henriques, assistant enseignant @ Técnico Lisboa et chercheur @ INESC-ID. Il est expert en Data Mining et Bioinformatique. L'interview de 20 minutes s'est transformée en une conversation d'environ une heure.

Rui n'est pas seulement un brillant académique mais aussi une personne très honnête, joyeuse et facile à vivre, ce qui a rendu les choses très faciles. J'ai beaucoup appris en parlant avec lui, et je suis sûr que vous aussi pouvez. L'interview sera en ligne bientôt. ?

En tout cas, j'avais un problème et un besoin. Je voulais gagner du temps en n'ayant pas à transcrire toute l'interview. L'idée était d'investir seulement vingt à soixante minutes afin d'améliorer considérablement la performance en matière de transcription. Cela ne se limite pas aux interviews, bien sûr. Vous pouvez transcrire des notes audio prises à partir de plusieurs sources comme des cours, des notes d'écriture, des pensées, votre liste de courses, ou vos pièces les plus philosophiques.

### Alors, comment faire cela ?

Je donne également des cours sur [_Gestion et Administration des Infrastructures IT_](https://fenix.tecnico.ulisboa.pt/disciplinas/AGISIT/2018-2019/1-semestre) _@ [Técnico Lisboa](https://tecnico.ulisboa.pt/en/)._ En classe, nous avons utilisé Google Cloud Engine. Je me suis souvenu d'un service appelé [Google Speech-To-Text](https://cloud.google.com/speech-to-text/), que nous pourrions utiliser dans ce cas. Et non, [Google](https://www.freecodecamp.org/news/the-voice-memos-bff-speech-to-text-powered-by-machine-learning-1dbc7a6c65f1/undefined) ne me paie pas pour écrire cela ?

Alors, comment transformer une interview de 55 minutes en texte facilement éditable ? Comment réduire nos efforts et nous concentrer sur ce qui compte ? ?

? Au fait, pour tirer le meilleur parti de cette méthode, veuillez couper le bruit et essayer d'enregistrer avec une voix forte et claire. ?

### Étape 1 : Installer le logiciel requis

J'utilise Vagrant pour gérer les machines virtuelles. L'avantage est que pour utiliser l'environnement, vous devez instancier le service Speech-To-Text. [Dans cet article, je montre étape par étape comment configurer ces outils](https://hackernoon.com/devops101-vagrant-6737c8c29904) (lisez-le jusqu'à la section « The Experiment »). Si vous préférez faire cela sur votre machine locale, passez directement à la troisième étape.

### Étape 2 : Démarrer la machine virtuelle

Maintenant, ouvrez votre console et exécutez :

```
$ vagrant up --provision && vagrant ssh
```

La machine virtuelle démarre et installe toutes les dépendances requises. Cela peut prendre un certain temps.

Attendez un peu. Fini. Bien. Bravo à vous ?

### Étape 3 : Obtenir les fichiers de support

[Fork ce dépôt contenant les fichiers de support](https://github.com/RafaelAPB/gce-speech2text) puis clonez-le sur votre ordinateur. Placez-le dans le dossier qui est synchronisé avec votre machine invitée.

### Étape 4 : Créer un compte sur Google Cloud Engine

Vous pouvez [demander une subvention gratuite (300 $)](https://cloud.google.com/free/) pour cette expérience ? Après avoir créé le compte, allez sur la [console Google.](https://goo.gl/jo2qQL) Créez un projet. Vous pouvez le nommer « easy-interview » si vous êtes suffisamment confiant. Vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/bjkBeRT3UGJIqilASbqpnwHS5amzLE4D5thc)

Après cela, allez dans « APIs & Services », afin d'activer l'API dont nous avons besoin pour accomplir la tâche.

![Image](https://cdn-media-1.freecodecamp.org/images/6zhTG1GyeUS59a7hg5lCPUgytLIB6wr0Dky3)

Cliquez sur « Create Credentials ». Choisissez « Cloud Speech API ». À la question « Are you planning to use this API with App Engine or Compute Engine? » répondez « No ». À l'étape 2, « Create a service account », nommez le service « transcribing ». Le rôle est Project => Owner. Type de clé : JSON.

À ce stade, vous devriez avoir téléchargé un fichier appelé « file.txt ». Il contient les informations d'identification nécessaires pour utiliser le service. Renommez le fichier en « terraform-credentials.json ». Copiez-le dans le dossier contenant les fichiers de support. Comme ce dossier est synchronisé avec votre machine virtuelle, vous aurez accès à ces fichiers depuis la machine invitée. Maintenant, exécutez :

```
$ gcloud auth login
```

Suivez les instructions. Authentifiez-vous en suivant le lien qui est affiché. Maintenant, analysez le fichier request.json :

```
{  "config": {      "encoding":"FLAC",      "sampleRateHertz": 16000,      "languageCode": "en-US",      "enableWordTimeOffsets": false  },  "audio": {      "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"  }}
```

Assurez-vous d'ajuster les paramètres pour qu'ils correspondent à votre cas. Attention, il y a des limitations sur l'encodage que vous pouvez utiliser. Si votre fichier est dans un format différent de _flac_ ou _wav_, vous devrez le convertir. Vous pouvez convertir des fichiers audio avec [Audacity](https://www.audacityteam.org/), un logiciel audio gratuit et open-source. Après avoir converti l'audio, vous devez le télécharger sur Google Storage. Pour cela, [vous devez créer un bucket](https://console.cloud.google.com/storage/).

![Image](https://cdn-media-1.freecodecamp.org/images/3TefQe9BJtLH7UJrI87F2cgaAIA2f3mSBabD)

Les paramètres peuvent être :

![Image](https://cdn-media-1.freecodecamp.org/images/s3XAjTQlz1H3VEQLaWnM9Xw1fFBwQb3kgq5H)

Après cela, téléchargez votre fichier dans le bucket. Dans le menu Bucket, vous devriez pouvoir accéder à l'URI associé à votre fichier. Le format est _gs://BUCKET/FILE.EXTENSION_. Prenez cet URI et remplacez-le dans le fichier _my-request.json_.

Votre fichier devrait ressembler à ceci :

```
{  "config": {      "encoding":"FLAC",      "sampleRateHertz": 16000,      "languageCode": "pt-PT",      "enableWordTimeOffsets": false  },  "audio": {      "uri":"gs://easy-interview/interview.flac"  }}
```

Avant d'utiliser l'API, nous devons charger les informations d'identification. Exécutez le script load-credentials.sh pour les charger :

```
$ source load-credentials.sh
```

Cela a défini la variable d'environnement GOOGLE_APPLICATION_CREDENTIAL. Ensuite, pour tester si la connexion est réussie, exécutez :

```
$ curl -s -H "Content-Type: application/json" \    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \    https://speech.googleapis.com/v1/speech:recognize \    -d @test-request.json
```

Vous devriez pouvoir voir une réponse avec du texte transcrit. Notez que nous avons exécuté _test-request.json_, qui est juste à des fins de test. Maintenant, pour faire l'appel avec vos données, exécutez :

```
$ curl -s -H "Content-Type: application/json" \    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \    https://speech.googleapis.com/v1/speech:longrunningrecognize \    -d @my-request.json >> name.out
```

Si vous exécutez _more name.out_, vous verrez que la réponse contient un champ appelé name. Ce nom correspond au nom de l'opération qui a été créée pour répondre à la demande. Maintenant, vous devez attendre un peu jusqu'à ce que l'opération soit terminée. Exécutez (remplacez NAME par le nom de votre opération) :

```
$ curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \     -H "Content-Type: application/json; charset=utf-8" \     "https://speech.googleapis.com/v1/operations/NAME" >> result.out
```

Tant que l'opération n'est pas terminée, votre _result.out_ aura un contenu similaire à ceci :

{  
 "name": "8254262642733152416",  
 "metadata": {  
 "[@type](http://twitter.com/type)": "type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeMetadata",  
 "progressPercent": 33,  
 "startTime": "2018-12-08T01:15:08.969852Z",  
 "lastUpdateTime": "2018-12-08T01:19:25.105683Z"  
 }  
}

Pour un fichier de 60 Mo, encodé avec _flac_, cela a pris environ 12 minutes. Vous aurez un fichier appelé _results.out_ avec votre précieux contenu. Il sera également sur votre machine hôte. J'ai écrit un script Python très simple qui analyse _results.out_. Le script redirige la sortie vers un fichier nommé _results-parsed.out_. Pour l'exécuter, lancez :

```
$ python parse.py
```

Si vous n'aimez pas les résultats, ajustez les paramètres et réessayez.

Profitez de votre contenu ! Vous avez terminé ? Pour terminer cette expérience, quittez la machine :

```
$ gcemgmt: exit
```

Maintenant, arrêtez la machine virtuelle :

```
$ vagrant halt
```

**N'oubliez pas de supprimer les fichiers que vous avez téléchargés sur Google Cloud.**

Bien joué !?

Eh bien, cela m'a pris plusieurs heures à écrire, mais au moins je n'ai pas eu à transcrire toute l'interview. ?

### Conclusion

Tout d'abord, j'adorerais ? avoir votre avis ! Enregistrez-vous beaucoup de mémos vocaux ? Trouvez-vous cette procédure utile ? En avez-vous une différente ?

Si vous avez **aimé cet article**, veuillez cliquer sur le bouton ? à gauche. **Avez-vous un ami ou un membre de la famille qui bénéficierait de cette solution ? Partagez cet article !**

_Continuez à rocker_ ?

Entrepreneuriat [?](https://emojipedia.org/fire/)

[**Top 8 des leçons que j'ai apprises à l'European Innovation Academy 2017**](https://blog.startuppulse.net/top-8-lessons-ive-learned-in-european-innovation-academy-2017-50eeb82d74b4)  
[_Imaginez que vous voyez l'opportunité de vous améliorer à tous les niveaux. La prendriez-vous ?_blog.startuppulse.net](https://blog.startuppulse.net/top-8-lessons-ive-learned-in-european-innovation-academy-2017-50eeb82d74b4)

**DevOps101** ☀️

[**DevOps101  Améliorez votre flux de travail ! Premières étapes sur Vagrant**](https://hackernoon.com/devops101-vagrant-6737c8c29904)  
[_Et rendez les clients et les développeurs plus heureux._hackernoon.com](https://hackernoon.com/devops101-vagrant-6737c8c29904)[**DevOps101  Infrastructure as Code With Vagrant**](https://hackernoon.com/devops101-itinfrastructure-54337d6a148b)  
[_Et déployer une infrastructure IT simple (deux serveurs web LAMP et une machine cliente)._hackernoon.com](https://hackernoon.com/devops101-itinfrastructure-54337d6a148b)

Blockchain Pour les Étudiants ⚡️

[**Blockchain Pour les Étudiants 101 - Les Bases (Partie 1)**](https://hackernoon.com/blockchain-for-students-101-the-basics-part-1-f39b8201a7d5)  
[_Êtes-vous prêt à plonger profondément dans cette technologie qui change la vie ?_hackernoon.com](https://hackernoon.com/blockchain-for-students-101-the-basics-part-1-f39b8201a7d5)