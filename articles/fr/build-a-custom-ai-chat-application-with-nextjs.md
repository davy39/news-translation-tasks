---
title: 'Comment créer une application de chat IA personnalisée avec Next.js : Fine-tuner
  GPT avec vos propres données'
subtitle: ''
author: Sharvin Shah
co_authors: []
series: null
date: '2025-10-07T11:11:07.070Z'
originalURL: https://freecodecamp.org/news/build-a-custom-ai-chat-application-with-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759834368425/fc26010c-077e-4af9-86cd-e16f1c218560.png
tags:
- name: Next.js
  slug: nextjs
- name: AI
  slug: ai
- name: Chat
  slug: chat
seo_title: 'Comment créer une application de chat IA personnalisée avec Next.js :
  Fine-tuner GPT avec vos propres données'
seo_desc: In 2025, AI-powered applications have advanced from generic chatbots to
  highly specialised assistants that understand your specific field, communicate in
  your style, and give contextually relevant answers. While Large Language Models
  (LLMs) like GPT-...
---

En 2025, les applications alimentées par l'IA sont passées de simples chatbots génériques à des assistants hautement spécialisés qui comprennent votre domaine spécifique, communiquent selon votre style et fournissent des réponses pertinentes au contexte. Bien que les grands modèles de langage (LLM) comme GPT-5 possèdent des capacités générales impressionnantes, il existe une demande croissante pour une IA qui comprenne profondément des entreprises particulières, des marques personnelles ou des domaines de connaissances spécialisés.

Imaginez avoir un assistant IA qui ne connaît pas seulement le développement web en général, mais qui comprend également votre style de codage spécifique, connaît l'historique de vos projets et peut répondre aux questions avec votre propre voix. Ce n'est pas de la science-fiction : c'est ce que le fine-tuning rend possible aujourd'hui.

Dans ce tutoriel, vous apprendrez à affiner les derniers modèles GPT-4.1 d'OpenAI et à créer une application de chat prête pour la production en utilisant Next.js 15. Je vous guiderai tout au long du processus : de la préparation de votre jeu de données et de sa soumission pour le fine-tuning, à la construction d'une interface de chat élégante utilisant votre modèle personnalisé.

Je vous montrerai ce processus en utilisant le contenu du site web de mon agence, mtechzilla.com, comme exemple de données. Vous apprendrez à scraper, nettoyer et formater du contenu réel pour l'entraînement. Naturellement, vous voudrez utiliser vos propres données — qu'il s'agisse de documentation, d'articles de blog, de transcriptions de support client ou de tout autre texte reflétant les connaissances et le style que vous souhaitez donner à votre IA.

Ce tutoriel s'adresse aux développeurs familiers avec React et Node.js mais novices dans le fine-tuning de modèles d'IA. À la fin, vous disposerez d'une application de chat IA personnalisée entièrement fonctionnelle et prête à être déployée.

En septembre 2025, le fine-tuning de GPT-5 n'est pas encore pris en charge. Ce tutoriel utilise GPT-4.1. Lorsque le fine-tuning de GPT-5 sera disponible, il vous suffira principalement de changer le nom du modèle de base.

## Table des matières :

* [Comprendre le Fine-Tuning](#heading-comprendre-le-fine-tuning)
    
* [Prérequis](#heading-prerequis)
    
* [Étape 1 : Préparation du jeu de données](#heading-etape-1-preparation-du-jeu-de-donnees)
    
* [Étape 2 : Soumission du Fine-Tuning](#heading-etape-2-soumission-du-fine-tuning)
    
* [Étape 3 : Configuration de l'application Next.js](#heading-etape-3-configuration-de-l-application-nextjs)
    
* [Étape 4 : Construction de l'interface de chat](#heading-etape-4-construction-de-l-interface-de-chat)
    
* [Étape 5 : Intégration de la route API](#heading-etape-5-integration-de-la-route-api)
    
* [Étape 6 : Tester votre application](#heading-etape-6-tester-votre-application)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre le Fine-Tuning

Avant de plonger dans le code, expliquons ce que signifie réellement le fine-tuning et quand c'est la meilleure option pour votre projet.

Le fine-tuning consiste à prendre un modèle de langage pré-entraîné et à l'entraîner davantage avec votre jeu de données spécifique. C'est comme enseigner à un étudiant brillant votre domaine d'expertise particulier et votre style de communication. Le modèle conserve ses connaissances générales mais devient spécialisé dans votre domaine.

C'est assez différent des autres méthodes de personnalisation du comportement de l'IA. La génération augmentée par récupération (RAG) consiste à fournir un contexte pertinent au modèle lors d'une requête, un peu comme si l'on donnait à quelqu'un des documents de référence à utiliser pour répondre à des questions. Le Prompt Engineering, quant à lui, consiste à créer des instructions intelligentes pour diriger le comportement du modèle sans entraînement supplémentaire. Le fine-tuning, cependant, aboutit à un modèle qui a profondément appris et internalisé vos données.

Les compromis en 2025 sont plus clairs que jamais. Le fine-tuning nécessite un investissement initial dans la préparation des données et des coûts d'entraînement, mais il permet une inférence plus rapide, élimine le besoin d'injection de contexte et offre une personnalité plus cohérente. Les systèmes RAG sont moins chers à mettre en place et plus faciles à mettre à jour, mais ils nécessitent des bases de données vectorielles et peuvent avoir du mal à égaler des styles nuancés. Le Prompt Engineering est gratuit et immédiat, mais il limite le degré de personnalisation que vous pouvez atteindre.

En septembre 2025, OpenAI prend en charge le fine-tuning supervisé pour trois nouveaux modèles : GPT-4.1, GPT-4.1-mini et GPT-4.1-nano. Chaque modèle a des capacités et des coûts différents. GPT-4.1-nano est l'option la plus abordable, idéale pour les tâches simples. GPT-4.1-mini équilibre performance et coût, tandis que GPT-4.1 offre l'intelligence la plus élevée pour les applications complexes et spécifiques à un domaine.

Le fine-tuning est préférable lorsque vous avez besoin d'une voix et d'un style cohérents, que vous possédez des connaissances spécialisées mal couvertes par le modèle de base, que vous souhaitez réduire le délai en supprimant l'injection de contexte, ou que vous devez garantir des comportements spécifiques sans prompts compliqués. Si vos besoins impliquent des informations changeant fréquemment, des recherches factuelles simples ou seulement une personnalisation occasionnelle, envisagez plutôt d'utiliser le RAG ou le Prompt Engineering.

## Prérequis

Avant de commencer, assurez-vous d'avoir configuré les outils et comptes suivants :

1. Node.js v22+ et npm (vérifiez avec `node --version`)
    
2. Connaissances de base en JavaScript pour les scripts
    
3. Familiarité avec React et TypeScript pour l'application web
    
4. Une clé API OpenAI avec facturation activée (obtenez-en une sur [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview))
    
5. Un éditeur de code
    

Vous aurez également besoin de contenu pour entraîner votre modèle. Il peut s'agir d'articles de blog, de documentation, de transcriptions ou de tout texte représentant les connaissances et le style que vous souhaitez transmettre à votre IA.

Si vous êtes bloqué, vous pouvez consulter le dépôt GitHub pour obtenir de l'aide ou me contacter (je suis ravi d'aider mes collègues développeurs).

**Lien du dépôt :** [https://github.com/Sharvin26/ai-fine-tuning-project](https://github.com/Sharvin26/ai-fine-tuning-project)

## Étape 1 : Préparation du jeu de données

La clé d'un projet de fine-tuning réussi est d'avoir un jeu de données bien préparé. OpenAI nécessite des données d'entraînement au format JSONL (JSON Lines), où chaque ligne est un objet JSON complet représentant une conversation. Le JSONL est un format où chaque ligne est un objet JSON distinct, ce qui est idéal pour gérer efficacement de grands jeux de données. Il permet un streaming et une manipulation faciles des données, ce qui le rend idéal pour les tâches d'apprentissage automatique.

La structure JSONL requise par OpenAI pour le fine-tuning est la suivante :

```json
{
   "messages":[
      {
         "role":"system",
         "content":"You are a helpful assistant."
      },
      {
         "role":"user",
         "content":"What is React?"
      },
      {
         "role":"assistant",
         "content":"React is a JavaScript library..."
      }
   ]
}
```

Chaque ligne représente une conversation complète. Pour que le fine-tuning soit efficace, vous avez besoin d'au moins 10 exemples, bien que 50 à 100 donnent généralement de meilleurs résultats.

Construisons un scraper Node.js qui extrait le contenu d'un site web et le convertit au format approprié.

Tout d'abord, configurons la structure de notre dossier de scripts :

```bash
mkdir ai-fine-tuning-project
cd ai-fine-tuning-project
mkdir scripts
cd scripts
npm init -y
npm install cheerio axios dotenv openai
touch scraper.js fine-tune.js .gitignore .env
```

Ouvrez `ai-fine-tuning-project` dans un éditeur de code et copiez les valeurs suivantes dans un fichier `.env` dans le dossier scripts.

```bash
OPENAI_API_KEY=sk-...votre-cle-api-ici...
OPENAI_ORG_ID=org-...votre-id-organisation...
```

Mettez à jour les variables d'environnement avec une clé API et un ID d'organisation valides d'OpenAI.

1. Générez une clé API en suivant ce guide : [Où trouver ma clé API OpenAI ?](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key). Voici les meilleures pratiques pour sécuriser votre clé API : [Meilleures pratiques pour la sécurité des clés API](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety).
    
2. Vous pouvez trouver votre ID d'organisation OpenAI ici : [Paramètres de l'organisation OpenAI](https://platform.openai.com/settings/organization/general).
    

Ajoutez le code suivant au fichier `.gitignore` :

```plaintext
# Environment variables
.env
.env.local
.env.*.local

# Dependencies
node_modules/

# Logs
*.log
logs/

# Cache and temporary files
.cache/
temp/
tmp/

# OS files
.DS_Store
Thumbs.db

# IDE files
.vscode/
.idea/
*.swp
*.swo
```

Mettez à jour le script du scraper (`scraper.js`) avec le code suivant :

```javascript
const cheerio = require("cheerio");
const axios = require("axios");
const fs = require("fs");
const OpenAI = require("openai");
require("dotenv").config();

const config = {
    urls: [
        {
            url: "https://www.mtechzilla.com/",
            contentType: "general",
        },
        {
            url: "https://www.mtechzilla.com/company/about-us",
            contentType: "about",
        },
        {
            url: "https://www.mtechzilla.com/services",
            contentType: "services",
        },
    ],
    openai: {
        apiKey: process.env.OPENAI_API_KEY,
        model: "gpt-5",
        trainingExamples: 50,
    },
    outputFile: "training_data.jsonl",
};

class AIScraper {
    constructor(config) {
        this.urls = config.urls;
        this.openaiConfig = config.openai;
        this.outputFile = config.outputFile;
        this.scrapedContent = [];
        this.trainingData = [];
        this.openai = new OpenAI({
            apiKey: this.openaiConfig.apiKey,
        });
        this.totalCost = 0;
    }

    async fetchPage(url) {
        try {
            const response = await axios.get(url, {
                timeout: 30000,
                headers: {
                    'User-Agent': 'Mozilla/5.0 (compatible; AI-Training-Data-Scraper/1.0)'
                }
            });
            return response.data;
        } catch (error) {
            console.error(`Failed to fetch ${url}: ${error.message}`);
            return null;
        }
    }

    extractContent(html, urlConfig) {
        const $ = cheerio.load(html);
        
        $('script, style, nav, header, footer').remove();
        $('[class*="cookie"], [class*="popup"], [class*="ad"]').remove();
        $('button, .btn').remove();
        
        const headings = [];
        $('h1, h2, h3, h4').each((_, elem) => {
            const text = $(elem).text().trim();
            if (text.length > 3 && text.length < 200) {
                headings.push(text);
            }
        });
        
        const paragraphs = [];
        $('p').each((_, elem) => {
            const text = $(elem).text().trim();
            if (text.length > 20) {
                paragraphs.push(text);
            }
        });
        
        const listItems = [];
        $('ul li, ol li').each((_, elem) => {
            const text = $(elem).text().trim();
            if (text.length > 5 && text.length < 200) {
                listItems.push(text);
            }
        });
        
        return {
            url: urlConfig.url,
            contentType: urlConfig.contentType,
            title: $('title').text().trim(),
            metaDescription: $('meta[name="description"]').attr('content') || '',
            headings: headings.slice(0, 10),
            paragraphs: paragraphs.slice(0, 15),
            listItems: listItems.slice(0, 20)
        };
    }

    formatContentForPrompt(content) {
        let formattedContent = `URL: ${content.url}\n`;
        formattedContent += `Content Type: ${content.contentType}\n`;
        formattedContent += `Title: ${content.title}\n\n`;
        
        if (content.metaDescription) {
            formattedContent += `Description: ${content.metaDescription}\n\n`;
        }
        
        if (content.headings.length > 0) {
            formattedContent += `Headings:\n${content.headings.map(h => `- ${h}`).join('\n')}\n\n`;
        }
        
        if (content.paragraphs.length > 0) {
            formattedContent += `Content:\n${content.paragraphs.join('\n\n')}\n\n`;
        }
        
        if (content.listItems.length > 0) {
            formattedContent += `Features/Services:\n${content.listItems.map(item => `- ${item}`).join('\n')}\n\n`;
        }
        
        return formattedContent;
    }

    async generateTrainingDataWithAI() {
        const allContent = this.scrapedContent.map(content => 
            this.formatContentForPrompt(content)
        ).join('\n' + '='.repeat(50) + '\n');
        
        const prompt = `Based on the website content below, generate ${this.openaiConfig.trainingExamples} diverse, natural Q&A pairs for training a customer service chatbot.

Website Content:
${allContent}

Create varied questions a real customer might ask, including:
- Company/business information
- Services or products offered  
- Contact and support questions
- General greetings and conversational questions
- FAQ-style questions

Make questions natural and human-like. Generate accurate answers based ONLY on the provided website content. Keep answers concise but informative.

Return a JSON object with a "training_data" array containing the Q&A pairs.`;

        try {
            const response = await this.openai.chat.completions.create({
                model: this.openaiConfig.model,
                messages: [
                    {
                        role: "system",
                        content: "You are an expert at creating training data for AI chatbots. Always return valid JSON. Output your final JSON response directly without any reasoning or explanation."
                    },
                    {
                        role: "user",
                        content: prompt,
                    },
                ],
                response_format: { 
                    type: "json_schema",
                    json_schema: {
                        name: "training_data_generation",
                        schema: {
                            type: "object",
                            properties: {
                                training_data: {
                                    type: "array",
                                    items: {
                                        type: "object",
                                        properties: {
                                            question: {
                                                type: "string",
                                                description: "A natural question a customer might ask"
                                            },
                                            answer: {
                                                type: "string", 
                                                description: "An accurate answer based on the website content"
                                            }
                                        },
                                        required: ["question", "answer"]
                                    }
                                }
                            },
                            required: ["training_data"]
                        }
                    }
                }
            });
            
            const generatedContent = response.choices[0].message.content?.trim();
            
            const actualInputTokens = response.usage.prompt_tokens;
            const actualOutputTokens = response.usage.completion_tokens;
            const actualCost = (actualInputTokens * 1.25 / 1000000) + (actualOutputTokens * 10 / 1000000);
            this.totalCost += actualCost;
            
            if (!generatedContent) {
                throw new Error("No content generated in response");
            }
            
            const structuredData = JSON.parse(generatedContent);
            const validTrainingData = [];
            
            if (structuredData.training_data && Array.isArray(structuredData.training_data)) {
                structuredData.training_data.forEach(item => {
                    if (item.question && item.answer) {
                        validTrainingData.push({
                            messages: [
                                {
                                    role: "system",
                                    content: "You are a helpful assistant. Answer questions accurately based on the website content."
                                },
                                {
                                    role: "user", 
                                    content: item.question
                                },
                                {
                                    role: "assistant",
                                    content: item.answer
                                }
                            ]
                        });
                    }
                });
            }
            
            this.trainingData = validTrainingData;
            console.log(`Generated ${validTrainingData.length} training examples`);
            
        } catch (error) {
            console.error(`OpenAI API error: ${error.message}`);
            throw error;
        }
    }

    async scrape() {
        console.log(`Starting scraper for ${this.urls.length} URLs`);
        
        for (const urlConfig of this.urls) {
            const html = await this.fetchPage(urlConfig.url);
            
            if (html) {
                const content = this.extractContent(html, urlConfig);
                this.scrapedContent.push(content);
                console.log(`Scraped: ${content.title || urlConfig.url}`);
            }
            
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
        
        if (this.scrapedContent.length === 0) {
            throw new Error("No content scraped successfully");
        }
        
        await this.generateTrainingDataWithAI();
        
        console.log(`Scraped ${this.scrapedContent.length} pages, generated ${this.trainingData.length} examples`);
        console.log(`Total cost: $${this.totalCost.toFixed(4)}`);
    }

    saveToFile() {
        if (this.trainingData.length === 0) {
            console.error("No training data to save!");
            return;
        }
        
        const jsonl = this.trainingData
            .map(example => JSON.stringify(example))
            .join('\n');
        
        fs.writeFileSync(this.outputFile, jsonl);
        console.log(`Saved ${this.trainingData.length} examples to ${this.outputFile}`);
    }
}

async function main() {
    try {
        if (!config.openai.apiKey) {
            console.error("Please set your OpenAI API key in .env file");
            return;
        }
        
        const scraper = new AIScraper(config);
        await scraper.scrape();
        scraper.saveToFile();
        
        console.log("Scraping complete!");
        
    } catch (error) {
        console.error("Error:", error.message);
    }
}

main();
```

Si vous utilisez une version de Node.js antérieure à 22, vous pourriez rencontrer des problèmes lors de l'exécution du script. La version recommandée est `v22.18.0`.

Ce code met en place un système automatisé pour le web scraping et la création de données d'entraînement alimentées par l'IA. Il génère des jeux de données d'entraînement à partir du contenu d'un site web. Le script utilise Cheerio pour analyser le HTML des URL fournies, extrayant des informations utiles telles que les titres, les paragraphes et les éléments de liste tout en ignorant les parties inutiles comme les scripts, les menus de navigation et les publicités. Après avoir rassemblé le contenu, il utilise l'API d'OpenAI (configurée pour utiliser GPT-4.1 avec une sortie JSON structurée) pour créer intelligemment des paires de questions-réponses naturelles à des fins de fine-tuning.

Les paires Q&R générées sont formatées dans des fichiers JSONL selon le format de fine-tuning d'OpenAI. Chaque entrée comprend un message système, une question utilisateur et une réponse de l'assistant. Le scraper dispose également de fonctionnalités utiles telles que la limitation du débit entre les requêtes, la gestion des erreurs et le suivi des coûts basé sur l'utilisation des tokens (1,25 $ par million de tokens d'entrée et 10 $ par million de tokens de sortie). Cela vous permet de suivre vos dépenses tout en générant des données d'entraînement.

Cependant, il s'agit d'un script de base qui peut être amélioré en fonction de la conception de votre site web, de votre public et de vos objectifs. Bien qu'il extraie diverses sections de contenu et crée des paires de questions-réponses diversifiées, vous devrez vérifier manuellement la sortie pour garantir la qualité et le formatage correct, car OpenAI rejettera les données mal formatées. Dans les environnements de production, ce processus de vérification peut être automatisé en mettant à jour le script avec une logique de validation supplémentaire et des contrôles de qualité.

Maintenant, créons notre fichier `training_data.jsonl` en lançant notre scraper :

```bash
node scraper.js
```

Vous devriez voir la sortie suivante :

```bash
Starting scraper for 3 URLs
Scraped: MTechZilla: Custom Software and App Development Company
Scraped: About MTechZilla | Custom Software Development Agency
Scraped: Expert App & Web Development Services | MTechZilla
Generated 50 training examples
Scraped 3 pages, generated 50 examples
Total cost: $0.0632
Saved 50 examples to training_data.jsonl
Scraping complete!
```

**Conseil de pro** : La qualité est plus importante que la quantité. Examinez le fichier `training_data.jsonl` généré et affinez tous les exemples qui ne reflètent pas fidèlement le contenu ou le ton que vous souhaitez que votre IA adopte.

## Étape 2 : Soumission du Fine-Tuning

Avec notre jeu de données préparé, créons un script pour le soumettre à OpenAI pour le fine-tuning. Nous utiliserons les modèles GPT-4.1 et gérerons l'ensemble du processus, du téléchargement à la finalisation.

Mettez à jour le script de fine-tuning (`fine-tune.js`) :

```javascript
const OpenAI = require("openai");
const fs = require("fs");
require("dotenv").config();

const CONFIG = {
    // Choose your base model for fine-tuning
    MODEL: "gpt-4.1-nano-2025-04-14", // Options: gpt-4.1-nano-2025-04-14, gpt-4.1-mini-2025-04-14, gpt-4.1-2025-04-14

    // Training file path
    TRAINING_FILE: "training_data.jsonl",

    // Polling interval for job status (in milliseconds)
    POLL_INTERVAL: 30000, // 30 seconds
};

class FineTuningManager {
    constructor() {
        if (!process.env.OPENAI_API_KEY) {
            throw new Error("OPENAI_API_KEY environment variable is required");
        }
        
        this.openai = new OpenAI({
            apiKey: process.env.OPENAI_API_KEY,
            organization: process.env.OPENAI_ORG_ID,
        });
    }

    // Step 1: Validate training data format
    validateTrainingData() {
        console.log("🔍 Validating training data format...");
        
        if (!fs.existsSync(CONFIG.TRAINING_FILE)) {
            throw new Error(`Training file not found: ${CONFIG.TRAINING_FILE}`);
        }

        const content = fs.readFileSync(CONFIG.TRAINING_FILE, "utf-8");
        const lines = content.split("\n").filter(line => line.trim());
        
        if (lines.length < 10) {
            throw new Error(`Need at least 10 examples. Found: ${lines.length}`);
        }

        let validExamples = 0;
        lines.forEach((line, index) => {
            try {
                const data = JSON.parse(line);
                
                // Validate JSONL structure as per OpenAI documentation
                if (!data.messages || !Array.isArray(data.messages) || data.messages.length < 2) {
                    throw new Error(`Invalid structure at line ${index + 1}`);
                }
                
                // Check for required roles
                const hasUser = data.messages.some(m => m.role === 'user');
                const hasAssistant = data.messages.some(m => m.role === 'assistant');
                
                if (!hasUser || !hasAssistant) {
                    throw new Error(`Missing user or assistant message at line ${index + 1}`);
                }
                
                validExamples++;
            } catch (e) {
                console.warn(`⚠️ Skipping line ${index + 1}: ${e.message}`);
            }
        });

        if (validExamples < 10) {
            throw new Error(`Need at least 10 valid examples. Found: ${validExamples}`);
        }

        console.log(`✅ Validation passed: ${validExamples} valid examples`);
        return validExamples;
    }

    // Step 2: Upload training file to OpenAI
    async uploadTrainingFile() {
        console.log("📤 Uploading training file...");

        const file = await this.openai.files.create({
            file: fs.createReadStream(CONFIG.TRAINING_FILE),
            purpose: "fine-tune",
        });

        console.log(`✅ File uploaded: ${file.id}`);
        return file.id;
    }

    // Step 3: Create fine-tuning job
    async createFineTuningJob(fileId) {
        console.log(`🚀 Creating fine-tuning job with model: ${CONFIG.MODEL}`);

        const job = await this.openai.fineTuning.jobs.create({
            training_file: fileId,
            model: CONFIG.MODEL,
            method: {
                type: "supervised"
            }
        });

        console.log(`✅ Fine-tuning job created: ${job.id}`);
        return job.id;
    }

    // Step 4: Monitor job until completion
    async monitorJob(jobId) {
        console.log("⏳ Monitoring fine-tuning job...");
        console.log("This typically takes 10-30 minutes...\n");

        while (true) {
            const job = await this.openai.fineTuning.jobs.retrieve(jobId);
            
            console.log(`Status: ${job.status}`);

            if (job.status === "succeeded") {
                console.log("\n🎉 Fine-tuning completed successfully!");
                console.log(`🎆 Your fine-tuned model ID: ${job.fine_tuned_model}`);
                return job.fine_tuned_model;
            } 
            
            if (job.status === "failed") {
                throw new Error(`Fine-tuning failed: ${job.error?.message || 'Unknown error'}`);
            }
            
            if (job.status === "cancelled") {
                throw new Error("Fine-tuning was cancelled");
            }

            // Wait before checking again
            await new Promise(resolve => setTimeout(resolve, CONFIG.POLL_INTERVAL));
        }
    }

    // Complete supervised fine-tuning workflow
    async runFineTuning() {
        try {
            console.log("🤖 Starting OpenAI Supervised Fine-Tuning\n");
            console.log(`📋 Using model: ${CONFIG.MODEL}`);
            console.log(`📄 Training file: ${CONFIG.TRAINING_FILE}\n`);
            
            // Step 1: Validate data
            const validExamples = this.validateTrainingData();
            
            // Step 2: Upload file
            const fileId = await this.uploadTrainingFile();
            
            // Step 3: Create job
            const jobId = await this.createFineTuningJob(fileId);
            
            // Step 4: Monitor completion
            const modelId = await this.monitorJob(jobId);
            
            console.log("\n" + "=".repeat(60));
            console.log("SUCCESS! Your fine-tuned model is ready!");
            console.log("=".repeat(60));
            console.log(`\n Model ID: ${modelId}`);
            console.log(`Trained on ${validExamples} examples`);
            console.log("\n Next steps:");
            console.log("1. Copy the Model ID above");
            console.log("2. Use it in your application to access your custom model");
            
            return modelId;
            
        } catch (error) {
            console.error(`\n❌ Fine-tuning failed: ${error.message}`);
            
            if (error.message.includes("not found")) {
                console.log("💡 Tip: Make sure training_data.jsonl exists in the current directory");
            } else if (error.message.includes("API_KEY")) {
                console.log("💡 Tip: Set OPENAI_API_KEY in your .env file");
            }
            
            throw error;
        }
    }
}

// Main execution
async function main() {
    const manager = new FineTuningManager();
    await manager.runFineTuning();
}

if (require.main === module) {
    main().catch(console.error);
}

module.exports = FineTuningManager;
```

Ce script gère l'ensemble du processus de fine-tuning une fois que vos données d'entraînement sont prêtes via le scraper. Il fonctionne comme un gestionnaire automatisé, prenant votre fichier d'entraînement JSONL et le transformant en un modèle OpenAI personnalisé conçu pour vos besoins spécifiques. Le processus commence par une validation approfondie, garantissant que votre fichier d'entraînement existe, contient au moins 10 exemples valides et suit le format requis par OpenAI avec les rôles de message corrects (utilisateur et assistant). Cette étape de validation est importante car OpenAI rejettera les données qui ne sont pas formatées correctement, donc identifier les problèmes tôt vous fait gagner du temps et économise des coûts d'API.

Ce script fournit un flux de travail complet de fine-tuning avec les nouveaux modèles GPT-4.1. Vous pouvez choisir entre les modèles nano (le moins cher), mini (équilibré) ou complet (le plus performant), selon vos besoins et votre budget. Une fois la validation réussie, le script télécharge votre fichier d'entraînement sur les serveurs d'OpenAI et lance un travail de fine-tuning en utilisant le modèle de base sélectionné. Le script utilise le fine-tuning supervisé, ce qui signifie que votre modèle apprend directement des paires questions-réponses que vous avez fournies, ajustant ses réponses pour correspondre aux informations et au ton de votre site web.

La partie la plus simple est la phase de surveillance, où le script vérifie automatiquement l'état du travail de fine-tuning toutes les 30 secondes jusqu'à ce qu'il soit terminé. Le fine-tuning prend généralement de 10 à 30 minutes, selon la taille de votre jeu de données et le modèle de base choisi. Pendant le processus, vous recevrez des mises à jour d'état claires dans la console. Une fois terminé, le script vous donne votre ID de modèle personnalisé, que vous pouvez utiliser immédiatement dans vos applications. Il fournit également des messages d'erreur utiles et des conseils si quelque chose ne va pas, comme vous rappeler de vérifier votre clé API ou de vérifier que votre fichier d'entraînement existe.

Maintenant, soumettons notre fichier `training_data.jsonl` pour le fine-tuning avec la commande suivante :

```bash
node fine-tune.js
```

Vous devriez voir la sortie suivante :

```bash
🎉 Fine-tuning completed successfully!
🎆 Your fine-tuned model ID: ft:gpt-4.1-nano-2025-04-14:...

============================================================
SUCCESS! Your fine-tuned model is ready!
============================================================

 Model ID: ft:ft:gpt-4.1-nano-2025-04-14:...
Trained on 50 examples

 Next steps:
1. Copy the Model ID above
2. Use it in your application to access your custom model
```

**Conseil de pro** : Commencez par le modèle nano pour tester votre jeu de données et votre flux de travail. C'est l'option la plus rentable et elle est souvent suffisante pour des connaissances spécifiques à un domaine. Vous pourrez toujours vous entraîner avec un modèle plus grand plus tard en mettant à jour la configuration dans `fine-tune.js`.

## Étape 3 : Configuration de l'application Next.js

Maintenant que notre modèle est entraîné, construisons une application de chat moderne. Nous allons configurer un dossier web séparé avec une application Next.js utilisant TypeScript et shadcn/ui pour les composants.

Tout d'abord, revenez à la racine du projet :

```bash
cd ..
```

Puis créez l'application web :

```bash
npx create-next-app@latest web
```

Choisissez les options suivantes lors de la configuration :

```bash
✔ Would you like to use TypeScript? › Yes
✔ Which linter would you like to use? › ESLint
✔ Would you like to use Tailwind CSS? › Yes
✔ Would you like your code inside a `src/` directory? › Yes
✔ Would you like to use App Router? (recommended) › Yes
✔ Would you like to use Turbopack? (recommended) › No
✔ Would you like to customize the import alias (`@/*` by default)? › No
```

Allez dans le répertoire web :

```bash
cd web
```

Installez les paquets requis en utilisant la commande suivante :

```bash
npm install ai @ai-sdk/openai @ai-sdk/react openai lucide-react
```

Maintenant, configurons shadcn/ui pour de beaux composants :

```bash
npx shadcn@latest init
```

Choisissez l'option suivante lors de la configuration :

```bash
✔ Which color would you like to use as the base color? › Slate
```

Et ajoutez les composants shadcn suivants :

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add scroll-area
npx shadcn@latest add avatar
```

Créez le fichier `.env.local` en utilisant la commande suivante :

```json
touch .env.local
```

Ajoutez vos variables d'environnement dans `web/.env.local` :

```bash
OPENAI_API_KEY=sk-...votre-cle-api...
OPENAI_ORG_ID=org-...votre-id-organisation...
FINE_TUNED_MODEL=ft:gpt-4.1-nano-2025-04-14:... # Votre ID de modèle issu du fine-tuning
```

Dans le répertoire `src`, créez un nouveau dossier nommé `types`. À l'intérieur de ce dossier, créez un fichier appelé `chat.ts` et copiez-y le code suivant :

```typescript
// web/src/types/chat.ts
export interface Message {
    id: string;
    role: "user" | "assistant" | "system";
    content: string;
    createdAt?: Date;
}

export interface ChatRequest {
    messages: Message[];
    model?: string;
}

export interface ChatResponse {
    message: Message;
    usage?: {
        prompt_tokens: number;
        completion_tokens: number;
        total_tokens: number;
    };
}
```

Ce code TypeScript définit les structures de données (interfaces) pour une application de chat, établissant une norme sur la manière dont les messages et les interactions API doivent être formatés dans votre application. L'interface `Message` spécifie ce que chaque message de chat doit inclure : un ID unique, un rôle indiquant s'il provient de l'utilisateur, de l'assistant ou du système, le contenu du message et un horodatage optionnel. L'interface `ChatRequest` organise les données que vous envoyez à votre modèle affiné, y compris un tableau de messages (l'historique de la conversation) et un paramètre de modèle optionnel pour spécifier quel modèle affiné utiliser.

Enfin, l'interface `ChatResponse` définit ce que vous recevrez de l'API : le message de réponse de l'assistant et des statistiques d'utilisation optionnelles indiquant combien de tokens ont été utilisés pour les prompts et les complétions. Cela vous aide à suivre les coûts. En définissant ces interfaces, TypeScript garantit la sécurité des types dans toute votre application, capturant les erreurs pendant le développement et fournissant des suggestions d'autocomplétion dans votre éditeur de code. Cela rend votre application de chat plus robuste et plus facile à maintenir.

Mettez à jour `app/layout.tsx` avec les méta-informations et la mise en page du chat :

```typescript
// web/app/layout.tsx
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "AI Chat - Powered by Custom Fine-Tuned Model",
    description: "Chat with an AI trained on custom content",
};

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en" className="h-full">
            <body
                className={`${inter.className} h-full bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-950 dark:to-slate-900`}
                suppressHydrationWarning={true}
            >
                {children}
            </body>
        </html>
    );
}
```

Ce code configure la mise en page racine (root layout) d'une application Next.js, agissant comme une enveloppe autour de chaque page de votre application de chat. Il commence par importer la police Inter de Google Fonts et la configure pour utiliser des caractères latins, donnant à votre application une apparence propre et moderne.

L'objet `metadata` définit le titre et la description de la page qui apparaissent dans les onglets du navigateur et les résultats des moteurs de recherche, ce qui est important pour le SEO et l'expérience utilisateur. Le composant `RootLayout` rassemble tout : il enveloppe toutes les pages de votre application (en utilisant la prop `children`) dans une structure HTML cohérente avec un style pleine hauteur (`h-full`) et un arrière-plan en dégradé agréable. Cet arrière-plan passe de tons ardoise clairs en mode clair à de l'ardoise foncée en mode sombre, s'adaptant automatiquement aux paramètres système de l'utilisateur. L'attribut `suppressHydrationWarning` résout un problème courant de Next.js où le HTML rendu par le serveur peut légèrement différer du HTML rendu par le client (souvent dû à des éléments comme les horodatages ou la détection de thème), empêchant ainsi les avertissements dans la console.

Cette mise en page garantit que chaque page de votre application de chat partage le même style de base, la même typographie et les mêmes métadonnées, de sorte que vous n'avez pas besoin de répéter le code sur chaque page. Elle nous donne une base solide avec TypeScript pour la sécurité des types, shadcn/ui pour les composants standard, une gestion efficace des variables d'environnement et une structure de projet propre, facile à maintenir et à étendre.

## Étape 4 : Construction de l'interface de chat

Construisons une interface de chat magnifique et réactive en utilisant les composants shadcn et les puissantes fonctionnalités de streaming du SDK AI de Vercel.

Tout d'abord, créez le composant de chat principal dans `src/components/chat.tsx` :

```typescript
// web/src/components/chat.tsx
"use client";

import { useChat } from "@ai-sdk/react";
import { useRef, useEffect, useState } from "react";
import { Send, Bot, User, Loader2, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
    CardDescription,
} from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { cn } from "@/lib/utils";

export default function Chat() {
    const scrollAreaRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);
    const [input, setInput] = useState("");

    const {
        messages,
        sendMessage,
        status,
        error,
        regenerate,
        stop,
        setMessages,
    } = useChat({
        onError: (error) => {
            console.error("Chat error:", error);
        },
        onFinish: () => {
            inputRef.current?.focus();
        },
    });

    const isLoading = status === "streaming" || status === "submitted";

    // Add welcome message on mount
    useEffect(() => {
        if (messages.length === 0) {
            setMessages((prev) => [
                ...prev,
                {
                    id: "welcome",
                    role: "assistant" as const,
                    parts: [
                        {
                            type: "text" as const,
                            text: "Hello! I'm your custom AI assistant, trained on specific content. How can I help you today?",
                        },
                    ],
                },
            ]);
        }
    }, [messages.length, setMessages]);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim() || isLoading) return;
        
        sendMessage({
            role: "user",
            parts: [{ type: "text", text: input }],
        });
        setInput("");
    };

    const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setInput(e.target.value);
    };

    // Auto-scroll to bottom when new messages arrive
    useEffect(() => {
        if (scrollAreaRef.current) {
            const scrollContainer = scrollAreaRef.current.querySelector(
                "[data-radix-scroll-area-viewport]"
            );
            if (scrollContainer) {
                scrollContainer.scrollTop = scrollContainer.scrollHeight;
            }
        }
    }, [messages]);


    return (
        <div className="flex h-screen max-w-5xl mx-auto p-4">
            <Card className="flex-1 flex flex-col shadow-xl overflow-hidden">
                {/* Header */}
                <CardHeader className="border-b flex-shrink-0">
                    <div className="flex items-center space-x-4">
                        <div className="relative">
                            <Avatar className="h-10 w-10">
                                <AvatarFallback className="bg-primary text-primary-foreground">
                                    <Bot className="h-6 w-6" />
                                </AvatarFallback>
                            </Avatar>
                            <div className="absolute -bottom-0.5 -right-0.5 w-3 h-3 bg-green-500 rounded-full border-2 border-background animate-pulse" />
                        </div>
                        <div className="flex-1">
                            <CardTitle>Custom AI Assistant</CardTitle>
                            <CardDescription>
                                Powered by your fine-tuned model
                            </CardDescription>
                        </div>
                    </div>
                </CardHeader>

                {/* Messages Area */}
                <ScrollArea ref={scrollAreaRef} className="flex-1 min-h-0">
                    <div className="p-4 space-y-4 pb-4">
                        {messages.map((message) => {
                            const isUser = (message.role as string) === "user";
                            return (
                                <div
                                    key={message.id}
                                    className={cn(
                                        "flex",
                                        isUser ? "justify-end" : "justify-start"
                                    )}
                                >
                                    <div
                                        className={cn(
                                            "flex items-start gap-3 max-w-[85%] min-w-0",
                                            isUser && "flex-row-reverse"
                                        )}
                                    >
                                        {/* Avatar */}
                                        <Avatar className="h-8 w-8 shrink-0">
                                            <AvatarFallback
                                                className={cn(
                                                    isUser
                                                        ? "bg-primary text-primary-foreground"
                                                        : "bg-muted"
                                                )}
                                            >
                                                {isUser ? (
                                                    <User className="h-4 w-4" />
                                                ) : (
                                                    <Bot className="h-4 w-4" />
                                                )}
                                            </AvatarFallback>
                                        </Avatar>

                                        {/* Message Content */}
                                        <div className="space-y-1 min-w-0 flex-1">
                                            <div
                                                className={cn(
                                                    "rounded-lg px-4 py-2.5 text-sm max-w-full",
                                                    isUser
                                                        ? "bg-primary text-primary-foreground"
                                                        : "bg-muted"
                                                )}
                                            >
                                                <div className="whitespace-pre-wrap break-words leading-relaxed overflow-wrap-anywhere">
                                                    {message.parts?.map((part, index) => {
                                                        if (part.type === "text") {
                                                            return <p key={index}>{part.text}</p>;
                                                        }
                                                        return null;
                                                    })}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            );
                        })}

                        {/* Loading Indicator */}
                        {isLoading && (
                            <div className="flex justify-start">
                                <div className="flex items-center gap-3 max-w-[85%]">
                                    <Avatar className="h-8 w-8">
                                        <AvatarFallback className="bg-muted">
                                            <Bot className="h-4 w-4" />
                                        </AvatarFallback>
                                    </Avatar>
                                    <div className="bg-muted rounded-lg px-4 py-2.5">
                                        <div className="flex items-center gap-2">
                                            <Loader2 className="h-3 w-3 animate-spin" />
                                            <span className="text-sm text-muted-foreground">
                                                Thinking...
                                            </span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Error Message */}
                        {error && (
                            <div className="flex justify-center px-4">
                                <div className="bg-destructive/10 border border-destructive/20 rounded-lg p-3 max-w-md">
                                    <div className="flex items-start gap-2">
                                        <AlertCircle className="h-4 w-4 text-destructive mt-0.5" />
                                        <div className="space-y-1">
                                            <p className="text-sm text-destructive">
                                                {error.message ||
                                                    "Something went wrong. Please try again."}
                                            </p>
                                            <Button
                                                onClick={() => regenerate()}
                                                variant="ghost"
                                                size="sm"
                                                className="h-7 px-2 text-xs"
                                            >
                                                Retry last message
                                            </Button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}
                    </div>
                </ScrollArea>

                {/* Input Area */}
                <CardContent className="border-t p-4 flex-shrink-0">
                    <form onSubmit={handleSubmit} className="flex gap-2">
                        <input
                            ref={inputRef}
                            type="text"
                            value={input}
                            onChange={handleInputChange}
                            placeholder="Type your message..."
                            disabled={isLoading}
                            className={cn(
                                "flex-1 px-3 py-2 text-sm rounded-md border border-input bg-background",
                                "placeholder:text-muted-foreground",
                                "focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
                                "disabled:cursor-not-allowed disabled:opacity-50"
                            )}
                            autoFocus
                        />

                        {isLoading ? (
                            <Button
                                type="button"
                                onClick={stop}
                                variant="destructive"
                                size="sm"
                            >
                                Stop
                            </Button>
                        ) : (
                            <Button
                                type="submit"
                                disabled={!input.trim()}
                                size="sm"
                            >
                                <Send className="h-4 w-4" />
                                <span className="ml-2 hidden sm:inline">
                                    Send
                                </span>
                            </Button>
                        )}
                    </form>

                    {/* Character Counter */}
                    {input.length > 0 && (
                        <div className="mt-2 text-xs text-muted-foreground text-right">
                            {input.length} / 4000
                        </div>
                    )}
                </CardContent>
            </Card>
        </div>
    );
}
```

Ce code crée le composant principal de l'interface de chat où les utilisateurs interagissent avec votre modèle d'IA affiné. Il utilise principalement le hook `useChat` du SDK AI de Vercel, qui gère toutes les tâches complexes de messagerie, telles que l'envoi de messages, la réception de réponses en streaming, la gestion de l'état de la conversation et la gestion des erreurs. Le composant configure plusieurs hooks React : `useRef` pour gérer les éléments du DOM comme la zone de défilement et le champ de saisie, `useState` pour le texte de saisie, et `useEffect` pour les effets secondaires comme le défilement automatique et l'affichage d'un message de bienvenue lors du premier chargement du chat.

L'interface utilisateur est construite à l'aide de composants shadcn/ui pour créer un aspect poli et professionnel avec un effort minimal. La mise en page comporte trois sections principales : un en-tête affichant l'état de l'assistant IA (avec un point vert clignotant pour indiquer qu'il est en ligne), une zone de messages défilante au milieu et un formulaire de saisie en bas. Chaque message est affiché avec un avatar (une icône utilisateur pour les messages humains et une icône robot pour les réponses de l'IA) et stylisé différemment selon l'expéditeur. Les messages de l'utilisateur apparaissent à droite avec un arrière-plan de couleur primaire, tandis que les messages de l'assistant apparaissent à gauche avec un arrière-plan discret. Le composant inclut des détails d'expérience utilisateur (UX) réfléchis comme le défilement automatique vers le dernier message, la gestion du focus qui revient au champ de saisie après l'envoi, et un compteur de caractères indiquant à quel point vous êtes proche de la limite de 4000 caractères.

Le composant gère également différents états de manière fluide : il affiche une animation "Thinking..." avec un chargeur rotatif pendant que l'IA génère une réponse, affiche des messages d'erreur avec un bouton de réessai si quelque chose ne va pas, et permet même aux utilisateurs d'arrêter la réponse en cours si elle prend trop de temps. Lors du chargement, le bouton d'envoi se transforme en bouton "Stop", donnant aux utilisateurs un contrôle total sur la conversation. Tout est enveloppé dans un style réactif qui s'adapte aux différentes tailles d'écran, garantissant que votre interface de chat est superbe, que les utilisateurs soient sur ordinateur ou sur mobile.

Maintenant, mettez à jour la page principale pour utiliser le composant de chat :

```typescript
// web/app/page.tsx
import Chat from "@/components/chat";

export default function Home() {
    return (
        <main className="h-screen">
            <Chat />
        </main>
    );
}
```

Cette interface de chat utilise les composants shadcn/ui pour créer un aspect poli et professionnel. Elle comprend des fonctionnalités telles que le streaming de messages en temps réel, des états de chargement animés, la gestion des erreurs avec options de réessai, le défilement automatique vers les derniers messages, un design réactif pour tous les appareils, des raccourcis clavier, des fonctionnalités d'accessibilité et un compteur de caractères pour tenir les utilisateurs informés.

## Étape 5 : Intégration de la route API

Créons maintenant la route API backend qui connecte notre interface de chat au modèle OpenAI affiné avec un support de streaming approprié.

```typescript
// web/app/api/chat/route.ts
import { openai } from "@ai-sdk/openai";
import { streamText, convertToModelMessages } from "ai";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    try {
        // Parse request body
        const body = await req.json();
        const { messages } = body;

        // Validate messages
        if (!messages || !Array.isArray(messages)) {
            return NextResponse.json(
                { error: "Invalid request format" },
                { status: 400 }
            );
        }

        // Convert UI messages to model messages using AI SDK utility
        const modelMessages = convertToModelMessages(messages);

        // Check if we have any valid messages
        if (modelMessages.length === 0) {
            return NextResponse.json(
                { error: "No valid messages provided" },
                { status: 400 }
            );
        }

        // Add system prompt to prevent hallucination and guide the model
        const systemPrompt = {
            role: "system" as const,
            content: `You are a helpful assistant answering questions about MTechZilla, a software development company. 

IMPORTANT INSTRUCTIONS:
- Only answer questions based on information you were specifically trained on about MTechZilla
- If you don't know something or weren't trained on specific information, say "I don't have that specific information in my training data"
- Never make up or guess information about MTechZilla
- Be accurate and only provide information you're confident about

Answer questions accurately based on your training data about MTechZilla's services, technologies, and approach.`
        };

        // Prepend system message if not already present
        const hasSystemMessage = modelMessages.some(msg => msg.role === 'system');
        if (!hasSystemMessage) {
            modelMessages.unshift(systemPrompt);
        }

        // Load fine-tuned model ID from environment variable
        const fineTunedModelId = process.env.FINE_TUNED_MODEL;

        // Ensure we have a valid model ID
        if (!fineTunedModelId) {
            throw new Error("No fine-tuned model ID available");
        }

        // Call OpenAI with streaming using the new AI SDK
        const result = streamText({
            model: openai(fineTunedModelId),
            messages: modelMessages,
            temperature: 0.1, // Lower temperature for more deterministic, factual responses
        });

        // Log stream start
        console.log(`Stream started`);

        // Return UI message stream response for useChat compatibility
        return result.toUIMessageStreamResponse({
            headers: {
                "Cache-Control": "no-cache, no-transform",
                "X-Accel-Buffering": "no",
            },
        });
    } catch (error: unknown) {
        console.error("Chat API Error:", error);

        // Handle specific errors
        if (error && typeof error === "object" && "status" in error) {
            const errorWithStatus = error as { status: number };

            if (errorWithStatus.status === 401) {
                return NextResponse.json(
                    {
                        error: "Authentication failed. Check API key configuration.",
                    },
                    { status: 401 }
                );
            }

            if (errorWithStatus.status === 404) {
                return NextResponse.json(
                    {
                        error: "Model not found. Check your fine-tuned model ID.",
                    },
                    { status: 404 }
                );
            }

            if (errorWithStatus.status === 429) {
                return NextResponse.json(
                    {
                        error: "OpenAI rate limit reached. Please try again later.",
                    },
                    { status: 429 }
                );
            }
        }

        // Generic error
        return NextResponse.json(
            { error: "An error occurred. Please try again." },
            { status: 500 }
        );
    }
}
```

Ce code configure le point de terminaison de l'API backend qui connecte votre interface de chat à votre modèle OpenAI affiné. Lorsqu'un utilisateur envoie un message, cette route API Next.js reçoit la requête, vérifie si les messages sont correctement formatés et les convertit du format UI vers la structure requise par l'API d'OpenAI à l'aide de l'outil `convertToModelMessages` du SDK AI. Une fonctionnalité clé est l'injection d'un prompt système avant d'envoyer les messages à votre modèle. Le code ajoute automatiquement des instructions spécifiques, demandant à l'IA de ne répondre qu'en fonction de ses données d'entraînement sur MTechZilla (dans cet exemple) et de dire clairement "Je n'ai pas cette information spécifique" au lieu d'inventer des choses. C'est crucial pour prévenir les erreurs et garantir que le chatbot reste précis et fiable.

La route charge votre ID de modèle affiné à partir des variables d'environnement pour sécuriser les paramètres sensibles. Elle utilise le SDK AI de Vercel pour appeler OpenAI avec le streaming activé, de sorte que les réponses apparaissent mot par mot en temps réel au lieu d'attendre la réponse complète. La température est réglée sur 0,1, ce qui rend le modèle plus prévisible et factuel — parfait pour un chatbot de service client où la précision est plus importante que la créativité. La fonction `streamText` gère tous les détails du streaming, et la réponse est renvoyée dans un format qui fonctionne directement avec le hook `useChat` de votre composant frontend.

Le code inclut une gestion approfondie des erreurs pour les problèmes courants : échecs d'authentification (clés API invalides), erreurs de modèle non trouvé (ID de modèle incorrect), limitation du débit (trop de requêtes) et erreurs générales du serveur. Chaque type d'erreur renvoie un message spécifique et utile pour faciliter le débogage pendant le développement et fournir un retour clair aux utilisateurs en cas de problème. Les en-têtes de réponse incluent des directives de contrôle du cache pour garantir des données fraîches et éviter les problèmes de mise en mémoire tampon pendant le streaming, garantissant ainsi une expérience de chat fluide et en temps réel pour vos utilisateurs.

## Étape 6 : Tester votre application

Une fois que tout est configuré, testons l'application complète et assurons-nous qu'elle fonctionne correctement.

Tout d'abord, assurez-vous d'avoir ajouté votre ID de modèle affiné au fichier d'environnement :

```bash
OPENAI_API_KEY=sk-...votre-cle-api...
OPENAI_ORG_ID=org-...votre-id-organisation...
FINE_TUNED_MODEL=ft:gpt-4.1-nano-2025-04-14:... # Copiez depuis scripts/model_info.json
```

Lancez le serveur de développement :

```bash
npm run dev
```

Ouvrez [http://localhost:3000](http://localhost:3000) dans votre navigateur, et vous verrez l'interface suivante :

![Capture d'écran d'une fenêtre de chat avec "Custom AI Assistant" en haut. L'IA salue l'utilisateur en disant : "Bonjour ! Je suis votre assistant IA personnalisé, entraîné sur un contenu spécifique. Comment puis-je vous aider aujourd'hui ?" Un champ de saisie de message et un bouton d'envoi se trouvent en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1757941475393/692f92ff-11bc-451d-a9fa-a288c87f7d78.png align="center")

Testez divers scénarios :

1. **Test de connaissances du domaine** : Posez des questions liées à vos données d'entraînement
    
2. **Flux de conversation** : Ayez une conversation à plusieurs tours
    
3. **Cas limites** : Essayez des entrées très longues, des messages rapides, des interruptions de réseau
    
4. **Tests mobiles** : Testez sur différentes tailles d'écran
    

## Conclusion

Félicitations ! Vous avez réussi à affiner un modèle GPT-4.1 et à créer une application de chat prête pour la production, démontrant ainsi la puissance de l'IA personnalisée. Nous avons transformé le contenu brut d'un site web en données d'entraînement structurées, utilisé les derniers modèles d'OpenAI pour le fine-tuning et construit une application Next.js moderne avec streaming en temps réel et une interface soignée. La clé d'un fine-tuning réussi est de savoir quand c'est le bon choix — utilisez-le pour une voix de marque cohérente, des connaissances spécialisées du domaine et pour réduire la complexité du RAG, mais envisagez l'option RAG pour les informations qui changent souvent. Notre structure de projet modulaire sépare les scripts d'entraînement de l'application web, ce qui facilite le réentraînement des modèles et l'ajout de nouvelles fonctionnalités.

En continuant, n'oubliez pas que le fine-tuning est un processus étape par étape. Observez comment les utilisateurs interagissent, recueillez des commentaires et continuez à améliorer votre modèle avec de nouveaux exemples d'entraînement. Évitez les erreurs courantes comme l'utilisation de trop peu de données (visez plus de 50 bons exemples), l'ignorance des erreurs de validation et l'absence de limites de débit et de gestion des erreurs appropriées. En 2025, la personnalisation de l'IA évolue rapidement, avec des tendances vers des modèles plus efficaces, l'apprentissage continu et des méthodes hybrides mélangeant différentes techniques. Ce qui nécessitait auparavant une équipe d'ingénieurs ML peut désormais être réalisé par quelques développeurs possédant les bonnes compétences. Vous disposez maintenant des outils et des connaissances nécessaires pour créer des applications d'IA spécialisées qui comprennent et servent véritablement votre domaine spécifique.

*Pour les fondateurs envisageant l'adoption de l'IA, j'ai créé un guide gratuit :* [*AI or No AI? The 2025 Founder's Decision Playbook*](https://www.notion.so/AI-or-No-AI-The-2025-Founder-s-Decision-Playbook-25ec9ed724ec80668a8fc42bb804515a) *— un cadre pour aider à décider quand l'IA apporte réellement de la valeur.*

*N'hésitez pas à me contacter sur* [*LinkedIn*](https://www.linkedin.com/in/sharvinshah/) *et* [*Twitter*](https://twitter.com/sharvinshah26)*.*