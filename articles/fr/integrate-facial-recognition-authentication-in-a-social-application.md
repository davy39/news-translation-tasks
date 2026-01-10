---
title: Comment intégrer l'authentification par reconnaissance faciale dans une application
  sociale avec Face API
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2025-09-23T03:01:14.173Z'
originalURL: https://freecodecamp.org/news/integrate-facial-recognition-authentication-in-a-social-application
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758208687476/3ca6b95d-55c8-4bb6-a4aa-580409e1608f.png
tags:
- name: React
  slug: reactjs
- name: authentication
  slug: authentication
- name: facial recognition
  slug: facial-recognition
seo_title: Comment intégrer l'authentification par reconnaissance faciale dans une
  application sociale avec Face API
seo_desc: 'Social applications have evolved over the years, and there is a major need
  for secure methods to authenticate users'' identities.

  Integrating multifactor authentication capabilities into applications is crucial
  for strengthening their integrity. In so...'
---

Les applications sociales ont évolué au fil des ans, et il existe un besoin majeur de méthodes sécurisées pour authentifier l'identité des utilisateurs.

L'intégration de capacités d'authentification multifacteur dans les applications est cruciale pour renforcer leur intégrité. Dans les applications sociales, les mécanismes d'authentification éliminent l'accès non souhaité aux informations personnelles entre deux parties. L'authentification faciale n'est pas entièrement nouvelle, car la plupart des appareils l'intègrent déjà comme mesure de sécurité. Elle offre une protection plus forte que de nombreuses méthodes traditionnelles, notamment contre des risques tels que le phishing, les attaques par force brute et le piratage de compte.

## Sommaire

* [À quoi s'attendre](#heading-a-quoi-s-attendre)
    
* [Prérequis](#heading-prerequis)
    
* [Une brève introduction à l'outil Face API](#heading-une-breve-introduction-a-l-outil-face-api)
    
* [Configuration du projet](#heading-configuration-du-projet)
    
* [Projet de démonstration : Intégration de la reconnaissance faciale et de l'authentification](#heading-projet-de-demonstration-integration-de-la-reconnaissance-faciale-et-de-l-authentification)
    
* [Informations supplémentaires et conseils](#heading-informations-supplementaires-et-conseils)
    
* [Conclusion](#heading-conclusion)
    

## À quoi s'attendre

Dans cet article, je vais vous guider dans la création d'un système d'authentification multifacteur pour une application de chat propulsée par [Stream.io](https://getstream.io), et assurer une authentification faciale efficace des utilisateurs pour ne permettre que l'accès autorisé à votre application. J'illustrerai tout cela avec des exemples de code pertinents.

## Prérequis

Voici les prérequis nécessaires pour suivre ce tutoriel :

* Connaissance intermédiaire de Node.js/Express pour l'aspect backend
    
* Connaissance de React pour l'aspect frontend
    
* Une clé API [Stream.io](https://getstream.io)
    

Avant de commencer, nous allons brièvement présenter l'outil d'authentification faciale choisi : [Face-Api.js](https://justadudewhohacks.github.io/face-api.js/docs/index.html).

## Une brève introduction à l'outil Face API

Face-Api.js est un package de reconnaissance faciale conçu pour être intégré aux applications JavaScript. Il a été construit au-dessus de la bibliothèque TensorFlow et fournit une détection faciale étendue basée sur des modèles de machine learning et des calculs abstraits.

En plus de toutes ces fonctionnalités, il est facile à utiliser et peut également être utilisé localement avec ses modèles prédéfinis. Voici un lien vers sa [page de documentation](https://justadudewhohacks.github.io/face-api.js/docs/index.html), qui fournit des exemples de code pertinents.

Il offre des fonctionnalités telles que la détection de visage, la capture de visage et la correspondance de visage, qui utilisent l'[algorithme euclidien](https://en.wikipedia.org/wiki/Euclidean_algorithm) pour établir des distinctions précises. Nous allons maintenant le configurer aux côtés de notre projet d'application de chat dans la section suivante.

## Configuration du projet

Comme mentionné précédemment, il s'agit d'un projet full-stack contenant à la fois des aspects frontend et backend. Dans cette section, nous allons configurer les deux bases de code avant de passer à la section du projet de démonstration.

### Frontend

Nous allons propulser l'application en utilisant le Framework Vite pour le frontend.

```javascript
npm create vite@latest
```

Après avoir créé l'application React, installez face-api.js avec cette commande :

```javascript
npm i face-api.js
```

Cela installera le package `face` et les dépendances requises. Vous pouvez ensuite installer le SDK de chat propulsé par Stream, qui constituera le cœur du projet.

```javascript
npm i stream-chat stream-chat-react
```

Une fois l'opération réussie, nous en avons terminé avec l'échafaudage de la structure du projet. Pour faciliter les tests locaux de notre application frontend, nous devrons héberger localement les modèles de visage nécessaires au package Face. Voici un [lien](https://github.com/justadudewhohacks/face-api.js-models) vers les modèles. Veuillez copier le dossier des modèles et le coller dans le dossier public du projet de code. Ensuite, nous allons configurer notre projet backend.

### Backend

Le backend est conçu pour stocker les détails des utilisateurs et assurer leur authentification avant d'accéder à l'application de chat. MongoDB sera la base de données de choix, et nous utiliserons la bibliothèque Express.js comme environnement de développement d'API backend. Pour faciliter la configuration, veuillez cloner cette [base de code](https://github.com/oluwatobi2001/stream-backend.git) et l'installer sur votre PC local. Elle est livrée préchargée avec les fichiers d'installation nécessaires. Pour profiter davantage d'une expérience backend fluide, vous pouvez utiliser l'option MongoDB [Atlas](https://www.mongodb.com/products/platform/atlas-database) comme base de données pour stocker les détails des utilisateurs. Sur ce, nous allons commencer le projet de code dans la section suivante.

## Projet de démonstration : Intégration de la reconnaissance faciale et de l'authentification

Dans cette section, nous allons passer en revue la configuration d'une page d'authentification sur le frontend où un utilisateur peut enregistrer ses coordonnées, son nom d'utilisateur, son e-mail et son mot de passe sur la page d'inscription. Il est également obligé de prendre un instantané de son visage, et l'API Face sera appelée pour détecter un visage dans l'image. Il ne sera pas autorisé à aller plus loin tant que cette étape n'aura pas réussi.

Ensuite, la fonction `faceDescriptor` de l'image est appelée, ce qui génère une valeur vectorielle unique de description faciale du visage de l'utilisateur basée sur les modèles de machine learning fournis. Ces valeurs sont stockées de manière sécurisée dans la base de données MongoDB via le backend Express.js après une inscription réussie. L'application est couplée à un système d'authentification multifacteur, qui possède à la fois des mécanismes d'authentification basés sur le mot de passe et l'authentification faciale.

Lorsque le premier obstacle (authentification par mot de passe) est franchi, l'utilisateur doit ensuite effectuer une correspondance faciale, en la comparant avec le descripteur facial de l'utilisateur stocké lors de l'inscription. La comparaison est réalisée à l'aide de la comparaison algorithmique euclidienne basée sur le seuil que nous fournissons. Si le seuil est atteint, le visage est considéré comme correspondant et l'utilisateur accède à l'application de chat ; sinon, l'accès à l'application de chat propulsée par Stream.io lui est refusé. Des extraits de code source pertinents illustrant ces étapes seront fournis en même temps que les images.

Nous allons commencer par construire une page d'inscription pour notre application de chat en utilisant React, bien sûr. Nous commencerons par importer et initialiser les packages nécessaires.

```javascript
import React, {useState, useRef, useEffect} from 'react';
import * as faceapi from 'face-api.js'
import {useNavigate} from 'react-router-dom'
import axios from 'axios';

const Register =()=> {

    const navigate= useNavigate("/")
    const userRef = useRef();
    const passwordRef= useRef();
    const emailRef = useRef();
    const FullRef = useRef()
```

Dans l'extrait de code ci-dessus, nous avons importé des hooks React utiles et initialisé notre outil `Face-api.js` installé. [Axios](https://www.npmjs.com/package/axios) servira d'outil de requête API de choix pour ce projet. Le hook `useRef` sera utilisé pour suivre les entrées de l'utilisateur. Nous avons ensuite défini la fonction register et initialisé les différents hooks `useRef` pour les différents champs de saisie.

```javascript


    useEffect(()=> {
const loadModels =async() => {
await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
await faceapi.nets.faceLandmark68Net.loadFromUri('/models');
await faceapi.nets.faceRecognitionNet.loadFromUri('/models');
await faceapi.nets.faceExpressionNet.loadFromUri('/models');
await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
setModelIsLoaded(true);
                startVideo();
}
  loadModels()  }, [])
```

Dans le code ci-dessus, le hook `useEffect` est appelé pour s'assurer que les différents modèles `face-api` stockés localement sont initialisés et actifs dans notre application. Les modèles sont stockés dans le sous-dossier `models` au sein du dossier `public`. Ensuite, après avoir initialisé nos modèles, nous allons configurer notre fonctionnalité de caméra sur notre page web.

```javascript
  const [faceDetected, setFaceDetected] = useState(false);
      
   
        // Démarrer le flux vidéo
        const startVideo = () => {
            navigator.mediaDevices
                .getUserMedia({ video: true })
                .then((stream) => {
                    videoRef.current.srcObject = stream;
                })
                .catch((err) => console.error("Erreur d'accès à la webcam : ", err));
        };
        const captureSnapshot = async () => {
            const canvas = snapshotRef.current;
            const context = canvas.getContext('2d');
            context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
            const dataUrl = canvas.toDataURL('image/jpeg');
            setSnapshot(dataUrl);
        
            // Générer le descripteur de visage (vecteur à 128 dimensions)
            const detection = await faceapi
                .detectSingleFace(canvas, new faceapi.TinyFaceDetectorOptions())
                .withFaceLandmarks()
                .withFaceDescriptor();
        
            if (detection) {
                const newDescriptor = detection.descriptor;
                setDescriptionValue(newDescriptor)
                console.log( newDescriptor);
               setSubmitDisabled(false)
                stopVid()
            } else {
                console.error("Aucun visage détecté dans l'instantané");
            }
        };
    const stopVid =() => {
   
        navigator.mediaDevices
                .getUserMedia({ video: false })
                const stream = videoRef?.current?.srcObject;
        if (stream) {
            stream.getTracks().forEach(track => {track.stop()})
            videoRef.current.srcObject = null;
            setCameraActive(false)
        }
    }
        // Détecter le visage dans le flux vidéo
        const handleVideoPlay = async () => {
            const video = videoRef.current;
            const canvas = canvasRef.current;
    
            const displaySize = { width: video.width, height: video.height };
            faceapi.matchDimensions(canvas, displaySize);
    
            setInterval(async () => {
                if (!cameraActive) return ;
                const detections = await faceapi.detectAllFaces(
                    video,
                    new faceapi.TinyFaceDetectorOptions()
                );
    
                const resizedDetections = faceapi.resizeResults(detections, displaySize);
    
                canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
                faceapi.draw.drawDetections(canvas, resizedDetections);
                    const detected = detections.length > 0;
                 if (detected && !faceDetected) {
                captureSnapshot();  // Capturer l'instantané dès qu'un visage est détecté
            }
    
                setFaceDetected(detections.length > 0);
            }, 100);
        };
```

Dans le code ci-dessus, nous commençons par définir un tableau `useState` lorsque le visage de l'utilisateur est détecté pendant le processus d'inscription. Ensuite, la fonction pour déclencher la caméra du navigateur est activée. Une fois activée, nous pouvons déclencher la fonction `handleVideoPlay` dans le code. Cette fonction surveille la détection faciale comme mis en évidence par les modèles de visage déjà initialisés. La fonction `stopVid` est également déclenchée lorsque la détection faciale de l'utilisateur a été effectuée avec succès.

Dans cette section, nous avons également activé l'outil de caméra du navigateur dans notre application pour nous fournir une vidéo en temps réel. La fonction `captureSnapshot` aide à obtenir un instantané de la vidéo en cours de diffusion.

```javascript
const RegSubmit = async (e) => {
  e.preventDefault();
  console.log("hello");

  try {
    const res = await axios.post(BACKEND_URL, {
      username: userRef.current.value,
      email: emailRef.current.value,
      FullName: FullRef.current.value,
      password: passwordRef.current.value,
      faceDescriptor: descriptionValue,
    });

    console.log(res.data);
    setError(false);
    navigate("/login");
    console.log("help");
  } catch (err) {
    console.error(err);
    setError(true);
  }
};

```

Une fois toutes les valeurs obtenues, la fonction `RegSubmit` est définie. Lorsqu'elle est exécutée, elle stocke les détails de l'utilisateur fournis avec l'objet de description faciale sur notre serveur backend, qui pourra ensuite être consulté dans la section suivante pour l'authentification.

Voici le code d'inscription complet.

```javascript
import React, { useState, useRef, useEffect } from 'react';
import * as faceapi from 'face-api.js';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Register = () => {
  const navigate = useNavigate("/");

  const userRef = useRef();
  const passwordRef = useRef();
  const emailRef = useRef();
  const FullRef = useRef();
  const snapshotRef = useRef(null);
  const videoRef = useRef(null);
  const canvasRef = useRef(null);

  const [modelIsLoaded, setModelIsLoaded] = useState(false);
  const [detections, setDetections] = useState([]);
  const [error, setError] = useState(false);
  const [snapshot, setSnapshot] = useState(null);
  const [cameraActive, setCameraActive] = useState(true);
  const [submitDisabled, setSubmitDisabled] = useState(true);
  const [descriptionValue, setDescriptionValue] = useState(null);
  const [faceDetected, setFaceDetected] = useState(false);

  useEffect(() => {
    const loadModels = async () => {
      await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
      await faceapi.nets.faceLandmark68Net.loadFromUri('/models');
      await faceapi.nets.faceRecognitionNet.loadFromUri('/models');
      await faceapi.nets.faceExpressionNet.loadFromUri('/models');
      await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
      setModelIsLoaded(true);
      startVideo();
    };

    loadModels();
  }, []);

  const RegSubmit = async (e) => {
    e.preventDefault();
    console.log("hello");

    try {
      const res = await axios.post('http://localhost:5000/v1/users', {
        username: userRef.current.value,
        email: emailRef.current.value,
        FullName: FullRef.current.value,
        password: passwordRef.current.value,
        faceDescriptor: descriptionValue
      });

      console.log(res.data);
      setError(false);
      navigate("/login");
      console.log("help");
    } catch (err) {
      console.log(err);
      setError(true);
    }
  };

  const startVideo = () => {
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((err) => console.error("Erreur d'accès à la webcam : ", err));
  };

  const stopVid = () => {
    navigator.mediaDevices.getUserMedia({ video: false });
    const stream = videoRef?.current?.srcObject;
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      videoRef.current.srcObject = null;
      setCameraActive(false);
    }
  };

  const captureSnapshot = async () => {
    const canvas = snapshotRef.current;
    const context = canvas.getContext('2d');
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
    const dataUrl = canvas.toDataURL('image/jpeg');
    setSnapshot(dataUrl);

    const detection = await faceapi
      .detectSingleFace(canvas, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceDescriptor();

    if (detection) {
      const newDescriptor = detection.descriptor;
      setDescriptionValue(newDescriptor);
      console.log(newDescriptor);
      setSubmitDisabled(false);
      stopVid();

      if (storedDescriptor && isMatchingFace(storedDescriptor, newDescriptor)) {
        setInterval(alert("visage correspondant"), 100);
      } else {
        alert("Aucune correspondance trouvée !");
      }
    } else {
      console.error("Aucun visage détecté dans l'instantané");
    }
  };

  const handleVideoPlay = async () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
      if (!cameraActive) return;

      const detections = await faceapi.detectAllFaces(
        video,
        new faceapi.TinyFaceDetectorOptions()
      );

      const resizedDetections = faceapi.resizeResults(detections, displaySize);
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
      faceapi.draw.drawDetections(canvas, resizedDetections);

      const detected = detections.length > 0;
      if (detected && !faceDetected) {
        captureSnapshot();
      }

      setFaceDetected(detected);
    }, 100);
  };

  return (
    <div className="flex flex-col w-full h-screen justify-center">
      <div className="flex flex-col">
        <form className="flex flex-col mb-2 w-full" onSubmit={RegSubmit}>
          <h3 className="flex flex-col mx-auto mb-5">Page d'inscription</h3>

          <div className="flex flex-col mb-2 w-[50%] mx-auto items-center">
            <input
              type="text"
              placeholder="E-mail"
              className="w-full rounded-2xl h-[50px] border-2 p-2 mb-2 border-gray-900"
              required
              ref={emailRef}
            />
            <input
              type="text"
              placeholder="Nom d'utilisateur"
              className="w-full rounded-2xl h-[50px] border-2 p-2 mb-2 border-gray-900"
              required
              ref={userRef}
            />
            <input
              type="text"
              placeholder="Nom complet"
              className="w-full rounded-2xl h-[50px] border-2 p-2 mb-2 border-gray-900"
              required
              ref={FullRef}
            />
            <input
              type="password"
              placeholder="Mot de passe"
              className="w-full rounded-2xl h-[50px] border-2 p-2 mb-2 border-gray-900"
              required
              ref={passwordRef}
            />

            <div>
              {!modelIsLoaded && cameraActive && !descriptionValue ? (
                <p>Chargement</p>
              ) : (
                <>
                  {!descriptionValue && (
                    <>
                      <video
                        ref={videoRef}
                        width="200"
                        height="160"
                        onPlay={handleVideoPlay}
                        autoPlay
                        muted
                      />
                      <canvas
                        ref={canvasRef}
                        width="200"
                        height="160"
                        style={{ position: 'absolute', top: 0, left: 0 }}
                      />
                      <p>
                        {faceDetected ? (
                          <span style={{ color: 'green' }}>Visage détecté</span>
                        ) : (
                          <span style={{ color: 'red' }}>Aucun visage détecté</span>
                        )}
                      </p>
                      <canvas
                        ref={snapshotRef}
                        width="480"
                        height="360"
                        style={{ display: 'none' }}
                      />
                    </>
                  )}
                </>
              )}

              {snapshot && (
                <div style={{ marginTop: '20px' }}>
                  <h4>Instantané du visage :</h4>
                  <img
                    src={snapshot}
                    alt="Instantané du visage"
                    width="200"
                    height="160"
                  />
                </div>
              )}
            </div>

            <div className="mt-2">
              <button type="button" onClick={stopVid}>
                Arrêter la vidéo
              </button>
            </div>

            <button
              disabled={submitDisabled}
              className="mx-auto mt-4 rounded-2xl cursor-pointer text-white bg-primary w-[80%] lg:w-[50%] h-[40px] text-center items-center justify-center"
              type="submit"
            >
              S'inscrire
            </button>
          </div>

          <div className="flex flex-col mt-1 w-full">
            <p className="flex justify-center">
              Déjà inscrit ?&nbsp;
              <a href="/login" className="text-blue-600 underline">
                Connexion
              </a>
            </p>
          </div>

          {error && (
            <p className="text-red-600 text-center mt-2">
              Erreur lors de l'inscription, réessayez
            </p>
          )}
        </form>
      </div>
    </div>
  );
};

export default Register;

```

Ensuite, nous allons travailler sur notre système d'authentification multifacteur. Dans le code ci-dessous, nous allons mettre en évidence la fonction `LoginSubmit` qui sera déclenchée lorsque l'e-mail et le mot de passe de l'utilisateur sont fournis pour se connecter à notre application de chat. Le hook `useRef` est initialisé pour garantir que les valeurs passées dans les champs de saisie sont analysées vers le backend via l'outil de requête `Axios`.

```javascript
import React, { useState, useRef, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import axios from 'axios';

function Login() {
  const navigate = useNavigate();
  const userRef = useRef();
  const passwordRef = useRef();

  const [error, setError] = useState(false);

  const LoginSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        'http://localhost:5000/v1/auth/login',
        {
          email: userRef.current.value,
          password: passwordRef.current.value,
        },
        { withCredentials: true }
      );

      console.log(res?.data);
      setError(false);
      navigate('/confirm-auth');
      console.log(res);
    } catch (err) {
      setError(true);
      console.log(err);
    }
  };
}  
```

L'exemple complet du code de la page de connexion sera fourni [ici](http://github.com/oluwatobi2001/Stream-frontend.git). Après avoir confirmé avec succès leur identité via la fonction d'authentification par mot de passe, nous pouvons ensuite passer à la confirmation de l'identité de l'utilisateur via le système de reconnaissance faciale.

```javascript
import axios from 'axios';
import React, { useRef, useEffect, useState } from 'react';
import * as faceapi from 'face-api.js';
import { useNavigate } from 'react-router-dom';
```

Tout d'abord, nous allons configurer l'application en important les dépendances nécessaires comme mis en évidence dans l'extrait de code ci-dessus.

```javascript

  useEffect(() => {
    const loadModels = async () => {
      await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
      await faceapi.nets.faceLandmark68Net.loadFromUri('/models');
      await faceapi.nets.faceRecognitionNet.loadFromUri('/models');
      await faceapi.nets.faceExpressionNet.loadFromUri('/models');
    };

    loadModels();
  }, []);

  const handleVideoPlay = async () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    const displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
      if (!cameraActive) return;

      const detections = await faceapi.detectAllFaces(
        video,
        new faceapi.TinyFaceDetectorOptions()
      );

      const resizedDetections = faceapi.resizeResults(detections, displaySize);
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
      faceapi.draw.drawDetections(canvas, resizedDetections);

      const detected = detections.length > 0;
      if (detected && !faceDetected) {
        captureSnapshot();
      }

      setFaceDetected(detected);
    }, 100);
  };

  const startVideo = () => {
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((err) => console.error("Erreur d'accès à la webcam : ", err));
  };

  const stopVid = () => {
    const stream = videoRef.current.srcObject;
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      videoRef.current.srcObject = null;
      setCameraActive(false);
    }
  };

  const deleteImage = () => {
    setSnapshot(null);
    setDescriptionValue(null);
    setFaceDetected(false);
    setCameraActive(true);
    startVideo();
  };

  const captureSnapshot = async () => {
    const canvas = snapshotRef.current;
    const context = canvas.getContext('2d');
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL('image/jpeg');
    setSnapshot(dataUrl);
    stopVid();

    const detection = await faceapi
      .detectSingleFace(canvas, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceDescriptor();

    if (detection) {
      const newDescriptor = detection.descriptor;
      setDescriptionValue(newDescriptor);
      console.log(newDescriptor);
    }
  };
```

Après avoir initialisé toutes les dépendances nécessaires, nous avons également importé nos modèles comme nous l'avons fait dans la page d'inscription pour détecter le visage de l'utilisateur puis générer une description faciale. Nous avons également permis à l'utilisateur de supprimer l'instantané et de reprendre l'image autant de fois que possible.

```javascript
  const FaceAuthenticate = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        'http://localhost:5000/v1/auth/face-auth',
        { faceDescriptor: descriptionValue },
        { withCredentials: true }
      );

      console.log(res?.data);
      navigate('/chat');
    } catch (err) {
      console.log(err);
    }
  };
```

Une fois l'objet descripteur de visage généré, nous l'avons envoyé au backend pour le comparer avec le descripteur de visage stocké obtenu lors de l'inscription. S'ils correspondent, nous sommes redirigés vers l'application de chat. Sinon, un message d'erreur approprié nous refusant l'accès à l'application de chat s'affiche.

Voici le code de la page `FaceAuth` :

```javascript
import axios from 'axios';
import React, { useRef, useEffect, useState } from 'react';
import * as faceapi from 'face-api.js';
import { useNavigate } from 'react-router-dom';

const FaceAuth = () => {
  const navigate = useNavigate("/");

  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const snapshotRef = useRef(null);

  const [cameraActive, setCameraActive] = useState(true);
  const [snapshot, setSnapshot] = useState(null);
  const [descriptionValue, setDescriptionValue] = useState(null);
  const [faceDetected, setFaceDetected] = useState(false);

  useEffect(() => {
    const loadModels = async () => {
      await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
      await faceapi.nets.faceLandmark68Net.loadFromUri('/models');
      await faceapi.nets.faceRecognitionNet.loadFromUri('/models');
      await faceapi.nets.faceExpressionNet.loadFromUri('/models');
    };

    loadModels();
  }, []);

  const handleVideoPlay = async () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;

    const displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
      if (!cameraActive) return;

      const detections = await faceapi.detectAllFaces(
        video,
        new faceapi.TinyFaceDetectorOptions()
      );

      const resizedDetections = faceapi.resizeResults(detections, displaySize);
      canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
      faceapi.draw.drawDetections(canvas, resizedDetections);

      const detected = detections.length > 0;
      if (detected && !faceDetected) {
        captureSnapshot();
      }

      setFaceDetected(detected);
    }, 100);
  };

  const startVideo = () => {
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((err) => console.error("Erreur d'accès à la webcam : ", err));
  };

  const stopVid = () => {
    const stream = videoRef.current.srcObject;
    if (stream) {
      stream.getTracks().forEach((track) => track.stop());
      videoRef.current.srcObject = null;
      setCameraActive(false);
    }
  };

  const deleteImage = () => {
    setSnapshot(null);
    setDescriptionValue(null);
    setFaceDetected(false);
    setCameraActive(true);
    startVideo();
  };

  const captureSnapshot = async () => {
    const canvas = snapshotRef.current;
    const context = canvas.getContext('2d');
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL('image/jpeg');
    setSnapshot(dataUrl);
    stopVid();

    const detection = await faceapi
      .detectSingleFace(canvas, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceDescriptor();

    if (detection) {
      const newDescriptor = detection.descriptor;
      setDescriptionValue(newDescriptor);
      console.log(newDescriptor);
    }
  };

  const FaceAuthenticate = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post(
        'http://localhost:5000/v1/auth/face-auth',
        { faceDescriptor: descriptionValue },
        { withCredentials: true }
      );

      console.log(res?.data);
      navigate('/chat');
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <>
      <div className="flex w-full h-screen flex-col justify-center">
        <p className="flex flex-col mx-auto items-center text-lg font-semibold mb-3">
          Prenez un instantané pour confirmer votre identité
        </p>
        <p className="text-center mb-4">Assurez-vous que la photo est prise dans une zone lumineuse</p>

        <button
          onClick={startVideo}
          className="flex w-[30%] mx-auto text-center items-center justify-center mb-5 h-[40px] bg-blue-600 rounded-md text-white"
        >
          Activer la webcam
        </button>

        {!snapshot ? (
          <>
            <video
              className="flex mx-auto items-center rounded-md"
              ref={videoRef}
              width="240"
              height="180"
              onPlay={handleVideoPlay}
              autoPlay
              muted
            />
            <canvas
              ref={snapshotRef}
              width="240"
              height="180"
              style={{ position: 'absolute', top: 0, left: 0 }}
            />
            <button onClick={captureSnapshot} className="mt-4 mx-auto block text-sm text-blue-600 underline">
              Prendre un instantané
            </button>
          </>
        ) : (
          <div className="flex w-full justify-center">
            <img
              src={snapshot}
              className="rounded-lg"
              width="240"
              height="180"
              alt="Instantané du visage"
            />
          </div>
        )}

        <div className="flex flex-row w-full justify-evenly mt-5">
          <button
            onClick={deleteImage}
            className="bg-purple-500 text-white p-2 h-[35px] rounded-lg"
          >
            Supprimer l'image
          </button>
          <button
            onClick={FaceAuthenticate}
            className="bg-purple-500 text-white p-2 h-[35px] rounded-lg"
          >
            Télécharger l'image
          </button>
        </div>
      </div>
    </>
  );
};

export default FaceAuth;

```

Voici à quoi devrait ressembler la page d'authentification faciale.

![page d'authentification faciale](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPFsPVo9dymrTmMCyskCszbMf_SdG2n_j5gd7ayT1nQ6jOlhX8a_KFRG51cnqMCxUqFaVgTR2hrdGipmudd9B2TQpNfm4FrFMlYRo7bbu1gtRq1bKB5FmPi4QcbEPTLyDtAPbNEA?key=bLpVfispbJQQ4phtxWLC7w align="left")

Après avoir configuré le frontend, dirigeons-nous vers le backend et configurons les points de terminaison d'inscription et de connexion pour notre projet. L'intégralité du code du projet backend peut être récupérée [ici](http://github.com/oluwatobi2001/stream-backend.git). Nous ne mettrons en évidence que la fonction backend `faceAuth` dans cet article.

Pour vérifier l'authentification, nous utiliserons l'option des sessions au lieu de l'option JWT. Les informations importantes sur l'utilisateur seront stockées et accessibles dans les cookies de session attachés aux requêtes et réponses vers le frontend. Voici la fonction `faceAuth` :

```javascript
const faceAuth = async (req, res) => {
  try {
    console.log(req.session);

    const id = req.session.passport?.user;
    console.log(id);

 
    const user = await User.findById(id);
    console.log(user);

    if (user == null) {
      return res.status(400).json({ err: "Utilisateur non trouvé" });
    }

    
  } catch (err) {
    console.error(err);
    res.status(500).json({ err: "Erreur interne du serveur" });
  }
};

```

Tout d'abord, nous avons défini une fonction asynchrone nommée `faceAuth`. Nous avons ensuite obtenu l'ID unique de l'utilisateur qui avait réussi à franchir le processus de connexion initial à partir de la session de requête.

Pour confirmer la similitude du descripteur de visage stocké de l'utilisateur et de la photo envoyée depuis le frontend, nous avons utilisé la fonction de correspondance de visage basée sur l'algorithme euclidien pour confirmer l'identité de l'utilisateur comme fait ci-dessous.

```javascript
const isMatchingFace = (descriptor1, descriptor2, threshold = 0.6) => {
  // Convertir les descripteurs stockés en Float32Array s'ils ne le sont pas déjà
  if (!(descriptor1 instanceof Float32Array)) {
    descriptor1 = new Float32Array(Object.values(descriptor1));
  }

  if (!(descriptor2 instanceof Float32Array)) {
    descriptor2 = new Float32Array(Object.values(descriptor2));
  }

  const distance = faceapi.euclideanDistance(descriptor1, descriptor2);
  console.log("Distance euclidienne :", distance);

  return distance < threshold;
};

```

Comme indiqué dans le code ci-dessus, le seuil de similitude de comparaison utilisé était de 0,6. Celui-ci est flexible et peut être modifié selon la préférence de l'utilisateur, car un seuil plus élevé offrira une meilleure précision globale.  
Si la fonction renvoie vrai, alors l'utilisateur a été authentifié avec succès et peut alors accéder à notre application de chat. Voici l'extrait de code complet.

```javascript
const faceAuth = async (req, res) => {
  try {
    console.log(req.session);

    const id = req.session.passport?.user;
    console.log(id);

    const { faceDescriptor } = req.body;
    const user = await User.findById(id);
    console.log(user);

    if (user == null) {
      return res.status(400).json({ err: "Utilisateur non trouvé" });
    }

    const isMatchingFace = (descriptor1, descriptor2, threshold = 0.6) => {
      // Convertir le descripteur stocké (objet) en un Float32Array
      if (!(descriptor1 instanceof Float32Array)) {
        descriptor1 = new Float32Array(Object.values(descriptor1));
      }

      if (!(descriptor2 instanceof Float32Array)) {
        descriptor2 = new Float32Array(Object.values(descriptor2));
      }

      const distance = faceapi.euclideanDistance(descriptor1, descriptor2);
      console.log("Distance euclidienne :", distance);

      return distance < threshold;
    };

    if (isMatchingFace(faceDescriptor, user.faceDescriptor)) {
      console.log("Correspondance faciale réussie");
      req.session.mfa = true;

      return res.status(200).json({
        msg: "L'authentification de l'utilisateur a réussi. Accédez à l'application de chat.",
      });
    } else {
      return res.status(401).json({ msg: "Le visage ne correspond pas. Accès refusé." });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({
      err: "Le visage de l'utilisateur n'a pas pu être authentifié. Veuillez réessayer plus tard",
    });
  }
};

```

Une fois l'obstacle principal franchi, nous pouvons alors naviguer vers notre application et profiter d'une expérience de chat fluide.

De plus, par mesure de sécurité, un limiteur de débit est également en place pour minimiser l'utilisation de techniques de force brute par des individus malveillants pour accéder à l'application de chat.

## Informations supplémentaires et conseils

L'objectif global de ces efforts est d'obtenir une méthode de validation des utilisateurs plus évolutive et sécurisée. Le seuil peut facilement être modifié et ajusté pour améliorer la précision de l'application. Alternativement, l'outil [AWS Rekognition](https://aws.amazon.com/rekognition/) peut avantageusement remplacer l'outil Face API avec des modèles efficaces propulsés par le cloud. Les limites de la reconnaissance faciale peuvent également être surmontées en explorant l'authentification biométrique, car il est de notoriété publique que l'empreinte digitale de chaque individu est unique, ce qui réduit considérablement le risque de compromission de l'utilisateur.

## Conclusion

Jusqu'à présent, nous avons passé en revue le processus de création d'un outil efficace basé sur l'authentification faciale multifacteur pour empêcher l'accès d'intrus à notre application de chat, garantissant et priorisant le plus haut niveau de confidentialité des utilisateurs. Besoin d'un SDK qui vous assure une expérience de chat fluide et sécurisée ? Essayez Stream.io dès aujourd'hui.