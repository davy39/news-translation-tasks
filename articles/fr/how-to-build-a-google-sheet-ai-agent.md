---
title: Comment créer un agent IA pour Google Sheets avec Composio et le support Gemini
  TTS
subtitle: ''
author: Shrijal Acharya
co_authors: []
series: null
date: '2025-09-26T14:21:26.712Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-google-sheet-ai-agent
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758896336162/ed8b3c6b-2b3a-49ad-b60d-b2a42efbe19e.png
tags:
- name: Next.js
  slug: nextjs
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
seo_title: Comment créer un agent IA pour Google Sheets avec Composio et le support
  Gemini TTS
seo_desc: With the rise of AI agents and agentic systems, we’re no longer just generating
  text or images, we’re teaching AI how to take actions. Instead of asking, “Can AI
  write this for me?” you can now ask, “Can AI do this for me?” From updating CRMs
  to mana...
---

Avec l'essor des agents IA et des systèmes agentiques, nous ne nous contentons plus de générer du texte ou des images, nous apprenons à l'IA comment entreprendre des actions. Au lieu de demander : « L'IA peut-elle écrire ceci pour moi ? », vous pouvez désormais demander : « L'IA peut-elle faire ceci pour moi ? ». De la mise à jour des CRM à la gestion des tâches, les agents peuvent désormais se connecter à de réels outils et accomplir des missions.

Dans cet article, vous allez construire un agent IA capable de parler, de réfléchir et même de mettre à jour vos Google Sheets en utilisant Composio, Next.js et Gemini TTS.

## Ce qui est abordé ?

Dans ce tutoriel, vous apprendrez à construire votre propre agent IA pour Google Sheets avec un support vocal capable d'utiliser les outils de Composio. Vous découvrirez également :

* Ce qu'est un Agent IA.
    
* Comment utiliser Composio pour ajouter des intégrations à votre agent.
    
* Comment streamer des réponses à partir d'une route API Next.js avec le Vercel AI SDK.
    
* Comment travailler avec l'API Gemini text-to-speech.
    

## Table des matières

* [Ce qui est abordé ?](#heading-ce-qui-est-aborde)
    
* [Qu’est-ce que cet agent Sheets ?](#heading-qu-est-ce-que-cet-agent-sheets)
    
* [Comment configurer le projet](#heading-comment-configurer-le-projet)
    
* [Composants principaux de l'application](#heading-composants-principaux-de-l-application)
    
* [L'agent Google Sheets en action](#heading-l-agent-google-sheets-en-action)
    
* [Conclusion](#heading-conclusion)
    

## Qu’est-ce que cet agent Sheets ?

Tout d'abord, qu'est-ce qu'un Agent IA ? Un agent IA est un système capable d'agir de manière indépendante pour atteindre des objectifs. Par exemple, il peut réserver un vol, envoyer un e-mail ou interroger une base de données.

L'IA générative, comme ChatGPT, se concentre principalement sur la création de contenus tels que du texte, des images ou du code. Un agent est différent car il peut prendre des décisions, planifier et entreprendre des actions dans le monde réel, et pas seulement générer du contenu.

![Fonctionnement d'un agent IA](https://cdn.hashnode.com/res/hashnode/image/upload/v1757925559119/187f2b32-ddf0-46fb-8359-8cb62699da57.webp align="center")

Les grands modèles de langage (LLM) alimentent souvent ces agents. Le LLM fournit les capacités de raisonnement et de conversation, tandis que la couche agent ajoute des outils qui lui permettent d'agir au-delà de la simple génération.

Vous l'avez donc deviné. Aujourd'hui, nous construisons un agent IA capable d'accéder à des données réelles de Google Sheets et même d'y apporter des modifications.

## Comment configurer le projet

Il est assez simple de mettre ce projet en place. Suivez ces étapes :

Premièrement, vous devez cloner le dépôt :

```bash
git clone https://github.com/shricodev/google-sheet-super-agent.git
cd google-sheet-super-agent
```

Ensuite, vous devez installer les dépendances :

```bash
npm install
```

Puis configurez les variables d'environnement et lancez le serveur de développement :

```bash
# Clé API pour Google Gemini (accès direct)
GEMINI_API_KEY=

# Clé API pour Composio pour accéder aux intégrations d'outils (notamment Google Sheets)
COMPOSIO_API_KEY=

# ID utilisateur Composio (récupérez-le sur votre tableau de bord Composio après connexion)
COMPOSIO_GOOGLE_SHEET_USER_ID=

# ID de configuration d'authentification pour Google Sheets dans Composio
GOOGLE_SHEETS_AUTH_CONFIG_ID=

# Clé API pour le SDK Google Generative AI (client SDK Gemini)
GOOGLE_GENERATIVE_AI_API_KEY=

# Clé secrète pour signer/chiffrer les sessions.
# Générez avec `openssl rand -base64 32`
SESSION_SECRET=<secret_key_for_session>
```

Pour obtenir la clé API Composio, créez un [compte](https://platform.composio.dev/auth) et connectez-vous au tableau de bord. Vous trouverez la clé API dans les paramètres de votre projet par défaut.

Pour le `COMPOSIO_GOOGLE_SHEET_USER_ID`, vous pouvez l'obtenir après avoir connecté un compte dans la configuration d'authentification Google Sheets dans Composio.

![Bouton de connexion au compte Google Sheets dans Composio](https://cdn.hashnode.com/res/hashnode/image/upload/v1757925645287/a727f2d0-c151-4dea-96bf-3d2b6317cc8d.png align="center")

## Composants principaux de l'application

Il y a principalement trois composants logiques centraux dans ce projet :

### 1\. Initier la connexion

C'est assez simple. Vous devez initier une connexion avec Composio pour utiliser les intégrations, qui dans notre cas est Google Sheets.

```tsx
// ...Reste du code

const connection = await composio.connectedAccounts.initiate(
  userID,
  googleSheetAuthConfigID,
  // Décommentez ceci si vous souhaitez autoriser plusieurs comptes
  // {
  //   allowMultiple: true,
  // },
);

infoLog(
  "Veuillez visiter l'URL suivante pour autoriser : ",
  connection.redirectUrl ? connection.redirectUrl : "Quelque chose s'est mal passé !",
);

```

### 2\. Configurer le TTS avec l'API Gemini

Pour ce projet, j'ai décidé d'utiliser Gemini pour la génération TTS au lieu d'OpenAI uniquement parce qu'ils ont récemment (fin août 2025) lancé leur API TTS.

Vous pouvez en savoir plus ici : [Gemini Speech Generation (text-to-speech)](https://ai.google.dev/gemini-api/docs/speech-generation).

```tsx
import { errorLog } from "@/lib/logger";
import { ttsSchema } from "@/lib/validators/tts";
import { GoogleGenAI } from "@google/genai";
import { StatusCodes } from "http-status-codes";
import { NextRequest, NextResponse } from "next/server";
import { Readable } from "stream";
import wav from "wav";

const ai = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY,
});

async function convertL16ToWav(pcmBuffer: Buffer): Promise<Buffer> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];

    const writer = new wav.Writer({
      channels: 1,
      sampleRate: 24000,
      bitDepth: 16,
    });

    writer.on("data", (chunk) => {
      chunks.push(chunk);
    });

    writer.on("end", () => {
      resolve(Buffer.concat(chunks));
    });

    writer.on("error", reject);

    const readable = new Readable({
      read() {
        this.push(pcmBuffer);
        this.push(null); // Fin du flux
      },
    });

    readable.pipe(writer);
  });
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const parsedBody = ttsSchema.safeParse(body);

    if (!parsedBody.success) {
      return NextResponse.json(
        {
          error: parsedBody.error.message,
        },
        { status: StatusCodes.BAD_REQUEST },
      );
    }

    const { text } = parsedBody.data;

    const result = await ai.models.generateContent({
      model: "gemini-2.5-flash-preview-tts",
      contents: [{ parts: [{ text: text }] }],
      config: {
        responseModalities: ["AUDIO"],
        speechConfig: {
          voiceConfig: {
            prebuiltVoiceConfig: { voiceName: "Kore" },
          },
        },
      },
    });

    const data = result.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
    const mimeType =
      result.candidates?.[0]?.content?.parts?.[0]?.inlineData?.mimeType;

    if (typeof data !== "string") {
      errorLog("Données audio invalides reçues :", { data, mimeType });
      return NextResponse.json(
        { error: "Les données audio ne sont pas une chaîne de caractères." },
        { status: StatusCodes.INTERNAL_SERVER_ERROR },
      );
    }

    if (!data || data.length === 0) {
      errorLog("Données audio vides reçues :", { data, mimeType });
      return NextResponse.json(
        { error: "Données audio vides reçues." },
        { status: StatusCodes.INTERNAL_SERVER_ERROR },
      );
    }

    try {
      const audioBuffer = Buffer.from(data, "base64");

      console.log("Audio généré :", {
        bufferSize: audioBuffer.length,
        contentType: mimeType || "unknown",
        mimeType,
        textLength: text.length,
      });

      // Vérifier s'il s'agit du format L16 PCM qui nécessite une conversion
      if (
        mimeType?.startsWith("audio/L16") ||
        mimeType?.startsWith("audio/l16")
      ) {
        const wavBuffer = await convertL16ToWav(audioBuffer);

        return new NextResponse(new Uint8Array(wavBuffer), {
          headers: {
            "Content-Type": "audio/wav",
            "Content-Length": wavBuffer.length.toString(),
            "Cache-Control": "no-cache",
            "Accept-Ranges": "bytes",
          },
        });
      }

      return new NextResponse(new Uint8Array(audioBuffer), {
        headers: {
          "Content-Type": mimeType || "audio/mpeg",
          "Content-Length": audioBuffer.length.toString(),
          "Cache-Control": "no-cache",
          "Accept-Ranges": "bytes",
        },
      });
    } catch (bufferError) {
      errorLog(bufferError, "API /tts (erreur de buffer)");
      return NextResponse.json(
        { error: "Données audio base64 invalides." },
        { status: StatusCodes.INTERNAL_SERVER_ERROR },
      );
    }
  } catch (error) {
    errorLog(error, "API /tts");
    return NextResponse.json(
      { message: "Erreur lors de la génération de l'audio." },
      { status: 500 },
    );
  }
}

```

Celui-ci est un peu plus complexe. Pour une raison quelconque, l'API de Gemini renvoie les données au format `audio/L16` et non au format `mp3` ou `wav` auxquels nous sommes habitués.

Et vous ne pouvez pas vraiment lire ce format audio directement dans votre navigateur. Donc, d'abord, nous devons le convertir au format `wav` en utilisant la fonction `convertL16ToWav`. Ensuite, nous pouvons renvoyer le buffer `wav` comme réponse.

Cela m'a pris une éternité à implémenter. Je ne savais pas qu'il existait quelque chose comme `audio/L16` que je ne pouvais pas lire dans mon navigateur. J'ai dû faire beaucoup de recherches sur Google pour comprendre cela.

En résumé, tout ce qu'il fait est d'envelopper l'audio brut dans un fichier WAV qui ressemble à du PCM mono, 24kHz, 16 bits.

Et si vous souhaitez utiliser le package OpenAI, qui est beaucoup plus facile à utiliser car il renvoie la parole au format `mp3`, consultez mon projet ici : [shricodev/voice-chat-ai-agent (TTS)](https://github.com/shricodev/voice-chat-ai-configurable-agent/blob/main/app/api/tts/route.ts).

### 3\. Gérer les requêtes des utilisateurs

C'est la dernière pièce du puzzle. C'est ici que se déroule la logique réelle d'appel d'outil (tool call).

```tsx
import { google } from "@ai-sdk/google";
import { streamText } from "ai";
import { Composio } from "@composio/core";
import { NextResponse } from "next/server";
import { chatSchema } from "@/lib/validators/chat";
import { StatusCodes } from "http-status-codes";
import { errorLog } from "@/lib/logger";
import { VercelProvider } from "@composio/vercel";

// ...Reste du code

const tools = await composio.tools.get(userID, {
  toolkits: ["GOOGLESHEETS"],
});

let conversationContext = "";
if (conversationHistory && conversationHistory.length > 0) {
  conversationContext = conversationHistory
    .map((conversation) => {
      return `${conversation.role}: ${conversation.content}`;
    })
    .join("\n");
}

const systemPrompt = `
Vous êtes un assistant intelligent pour Google Sheets. Vous pouvez aider les utilisateurs à analyser, interroger et manipuler des données dans leurs Google Sheets.

ID de la feuille : ${sheetID}
ID utilisateur : ${userID}

Directives :
- Utilisez toujours les outils Google Sheets pour accéder aux données réelles de la feuille de calcul
- Fournissez des informations claires et exploitables basées sur les données réelles
- Si vous devez lire des données, utilisez d'abord les outils Google Sheets appropriés
- Formatez vos réponses de manière claire et professionnelle
- Si on vous interroge sur des calculs, utilisez les données réelles de la feuille

Générez toujours un court résumé de ce que vous avez accompli. Par exemple, si l'utilisateur vous a demandé
de faire des modifications, écrivez brièvement quelles modifications vous avez apportées. S'il
vous a demandé de résumer les données, écrivez brièvement de quoi il s'agit.

---

Conversation précédente dans ce document :

${conversationContext}
`;

const result = streamText({
  model: google("gemini-2.5-pro"),
  system: systemPrompt,
  prompt,
  tools: tools,
  toolChoice: "auto",
});

return result.toUIMessageStreamResponse({ sendReasoning: true });

```

Ce code réside dans l'App Router de Next.js. Tout d'abord, nous récupérons les outils de Composio en utilisant la fonction `composio.tools.get`. Nous utilisons `auto` comme choix d'outil, ce qui signifie que l'agent utilisera les outils en lesquels il a le plus confiance.

Ensuite, nous créons le prompt système qui guidera l'agent sur la façon de se comporter.

Enfin, nous appelons la fonction `streamText`, qui streame la réponse au lieu d'attendre la réponse complète avant de l'envoyer au client, en passant les outils, le prompt système et le modèle à utiliser. Ensuite, nous envoyons la réponse au format `UIMessageStreamResponse` afin qu'elle puisse être facilement affichée sur l'interface utilisateur.

## L'agent Google Sheets en action

Voici une courte démo de l'agent en action :

%[https://youtu.be/emXE8q1Irao] 

## Conclusion

Alors, que pensez-vous du projet jusqu'à présent ? C'était un projet vraiment amusant sur lequel travailler.

Allez-y, clonez le dépôt et essayez-le avec votre propre Google Sheet. Malgré tout cela, c'est un projet assez petit avec une logique très simple, que je pense que vous avez déjà complètement comprise.

Est-ce que je vous suggère de l'utiliser sur une Google Sheet importante ? Pas du tout. N'oubliez pas, c'est juste un modèle d'IA qui peut accéder à des outils via Composio. On ne peut jamais être sûr à 100 % avec l'IA. En construisant ce projet, j'ai rencontré des cas où l'IA a choisi les mauvais outils et a même complètement gâché la feuille. Mais vous pouvez toujours l'essayer sur une feuille sans importance pour voir comment tout cela fonctionne.

Vous pouvez trouver l'intégralité du code source ici : [shricodev/google-sheet-super-agent](https://github.com/shricodev/google-sheet-super-agent).