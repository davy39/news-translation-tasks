import os
import sys
import time
import yaml
import json
import requests
import csv
from openai import OpenAI

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================

# Chemins relatifs basés sur l'emplacement du script (dossier 'scripts')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR) # Remonte d'un cran

CSV_FILE = os.path.join(REPO_ROOT, "articles", "published_fr.csv")
EN_DIR = os.path.join(REPO_ROOT, "articles", "_raw")
FR_DIR = os.path.join(REPO_ROOT, "articles", "fr")

# API Keys
HASHNODE_API_KEY = os.getenv("HASHNODE_API_KEY")
HASHNODE_PUBLICATION_ID = os.getenv("HASHNODE_PUBLICATION_ID")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Configs API
SOURCE_API_URL = "https://gql.hashnode.com"
SOURCE_HOST = "freecodecamp.org/news"
LLM_BASE_URL = "https://openrouter.ai/api/v1"
LLM_MODEL = "mistralai/devstral-2512:free"

# Tags par défaut
DEFAULT_TAGS = [
    {"slug": "programming", "name": "Programming"},
    {"slug": "technology", "name": "Technology"}
]

# Initialisation des dossiers
os.makedirs(EN_DIR, exist_ok=True)
os.makedirs(FR_DIR, exist_ok=True)
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow(["slug_en", "slug_fr"])

def log(message):
    print(f"[{time.strftime('%H:%M:%S')}] {message}")
    sys.stdout.flush()

def get_llm_client():
    return OpenAI(base_url=LLM_BASE_URL, api_key=OPENROUTER_API_KEY)

# ==========================================
# 💾 GESTION CSV
# ==========================================

def load_processed_slugs():
    processed = set()
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("slug_en"): processed.add(row["slug_en"].strip())
    return processed

def append_to_csv(slug_en, slug_fr):
    try:
        with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
            csv.writer(f).writerow([slug_en, slug_fr])
    except Exception as e:
        log(f"⚠️ Erreur écriture CSV: {e}")

# ==========================================
# 📡 GRAPHQL
# ==========================================

GET_FULL_POSTS_QUERY = """
query GetPosts($host: String!, $first: Int!, $after: String) {
  publication(host: $host) {
    posts(first: $first, after: $after) {
      edges {
        node {
          title subtitle slug brief publishedAt url canonicalUrl
          coverImage { url }
          tags { name slug }
          author { name username }
          content { markdown }
        }
      }
      pageInfo { endCursor hasNextPage }
    }
  }
}
"""

PUBLISH_MUTATION = """
mutation PublishPost($input: PublishPostInput!) {
  publishPost(input: $input) {
    post { id url slug }
  }
}
"""

# ==========================================
# 🛠️ CORE FUNCTIONS
# ==========================================

def extract_meta(post):
    cover_url = post['coverImage']['url'] if post.get('coverImage') else None
    source_url = post.get('canonicalUrl') or post['url']
    tags = [{"name": t['name'], "slug": t['slug']} for t in post.get('tags', [])]
    return {
        'title': post['title'],
        'subtitle': post.get('subtitle') or '',
        'author': post['author']['name'],
        'date': post['publishedAt'],
        'originalURL': source_url,
        'coverImage': cover_url,
        'tags': tags,
        'seo_title': post.get('seo', {}).get('title'),
        'seo_desc': post.get('seo', {}).get('description') or post['brief']
    }

def save_article_to_en(post):
    filename = f"{post['slug']}.md"
    file_path = os.path.join(EN_DIR, filename)
    meta = extract_meta(post)
    content = f"---\n{yaml.dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{post['content']['markdown']}\n"

    is_new = not os.path.exists(file_path)
    if is_new:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        log(f"  📥 [DOWNLOAD] {filename}")
    return is_new, filename

def smart_split_content(content, max_size=100000):
    if len(content) <= max_size: return [content]
    import math
    chunks = []
    start = 0
    total_len = len(content)
    while start < total_len:
        end = min(start + max_size, total_len)
        if end < total_len:
            split_point = content.rfind('\n', start, end)
            if split_point == -1: split_point = end
        else:
            split_point = total_len
        chunks.append(content[start:split_point])
        start = split_point + 1
    return chunks

def translate_file(filename):
    source_path = os.path.join(EN_DIR, filename)
    target_path = os.path.join(FR_DIR, filename)

    if os.path.exists(target_path): return True

    with open(source_path, 'r', encoding='utf-8') as f:
        parts = f.read().split("---", 2)

    meta = yaml.safe_load(parts[1])
    body = parts[2]
    chunks = smart_split_content(body.strip())

    final_body = ""
    translated_title = meta.get('title', '')
    translated_subtitle = meta.get('subtitle', '')
    previous_context = ""

    for i, chunk in enumerate(chunks):
        log(f"  🤖 Traduction {filename} ({i+1}/{len(chunks)})...")

        input_json = {
            "chunk_index": i + 1,
            "markdown_content": chunk,
            "previous_context": previous_context[-1000:] if i > 0 else None
        }
        if i == 0:
            input_json["title"] = meta.get('title')
            input_json["subtitle"] = meta.get('subtitle')

        system_prompt = (
            "You are an expert technical translator. Translate the JSON content from English to French.\n"
            "Output JSON keys must be valid.\n"
            "If 'title' is provided in input, return 'translated_title' and 'translated_subtitle'.\n"
            "ALWAYS return 'translated_content' containing the translated Markdown.\n"
            "IMPORTANT: The 'translated_content' field can contain Markdown with code blocks.\n"
            "Do not use Unicode escape sequences (\\uXXXX). Write characters directly in UTF-8.\n"
            "Keep emojis (💡, ✨) and chars (—) as literal UTF-8. DO NOT unicode escape them.\n"
            "Properly escape double quotes inside the JSON string.\n"
            "Do not translate wikipedia url or any href at all.\n"
            "IMPORTANT: always translate anchor slugs in Table of Contents :\n"
            "Update anchor slugs based on the translated headings (e.g. #heading-setup -> #heading-installation).\n"
            "All anchors should begin with #heading-, should not contain accentuated char, and ' should not be replaced with - (ie. # L'icône -> #heading-licone).\n"
        )

        try:
            client = get_llm_client()
            resp = client.chat.completions.create(
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": json.dumps(input_json)}
                ],
                response_format={"type": "json_object"}
            )
            result = json.loads(resp.choices[0].message.content)

            if i == 0:
                translated_title = result.get('translated_title', translated_title)
                translated_subtitle = result.get('translated_subtitle', translated_subtitle)

            final_body += "\n" + result.get('translated_content', '')
            previous_context = final_body

        except Exception as e:
            log(f"  ❌ Erreur traduction chunk {i+1}: {e}")
            return False

    meta['title'] = translated_title
    meta['subtitle'] = translated_subtitle

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(f"---\n{yaml.dump(meta, sort_keys=False, allow_unicode=True)}---\n\n{final_body.strip()}")

    log(f"  ✨ [SAVED FR] {filename}")
    return publish_to_hashnode(target_path, filename)

def publish_to_hashnode(filepath, filename):
    slug_en = filename.replace(".md", "")
    processed = load_processed_slugs()
    if slug_en in processed: return True

    with open(filepath, 'r', encoding='utf-8') as f:
        parts = f.read().split("---", 2)
    meta = yaml.safe_load(parts[1])

    variables = {
        "input": {
            "publicationId": HASHNODE_PUBLICATION_ID,
            "title": meta.get('title'),
            "subtitle": meta.get('subtitle'),
            "contentMarkdown": parts[2].strip(),
            "tags": meta.get('tags', []) or DEFAULT_TAGS,
            "coverImageOptions": {"coverImageURL": meta.get('coverImage')} if meta.get('coverImage') else {},
            "originalArticleURL": meta.get('originalURL'),
            "metaTags": {"title": meta.get('title'), "description": f"Original: {meta.get('originalURL')}"}
        }
    }

    try:
        resp = requests.post(SOURCE_API_URL, json={'query': PUBLISH_MUTATION, 'variables': variables}, headers={"Authorization": HASHNODE_API_KEY})
        data = resp.json()
        if 'errors' in data:
            log(f"  ⚠️ Erreur Upload: {data['errors'][0]['message']}")
            return False

        slug_fr = data['data']['publishPost']['post']['slug']
        append_to_csv(slug_en, slug_fr)
        log(f"  🚀 [PUBLISHED] {slug_fr}")
        return True
    except Exception as e:
        log(f"  ❌ Exception Upload: {e}")
        return False

# ==========================================
# 🚀 MAIN LOOP
# ==========================================

def run():
    log("🚀 Démarrage Update...")
    processed_slugs = load_processed_slugs()
    new_files = []
    has_next, cursor = True, None
    stop = False

    # 1. Collecte
    while has_next and not stop:
        resp = requests.post(SOURCE_API_URL, json={'query': GET_FULL_POSTS_QUERY, 'variables': {"host": SOURCE_HOST, "first": 10, "after": cursor}})
        data = resp.json().get('data', {}).get('publication', {})
        if not data: break

        for edge in data['posts']['edges']:
            node = edge['node']
            slug = node['slug']

            if slug in processed_slugs or os.path.exists(os.path.join(FR_DIR, f"{slug}.md")):
                log(f"🛑 Article existant trouvé : {slug}. Arrêt collecte.")
                stop = True
                break

            _, filename = save_article_to_en(node)
            new_files.append(filename)

        cursor = data.get('posts', {}).get('pageInfo', {}).get('endCursor')
        has_next = data.get('posts', {}).get('pageInfo', {}).get('hasNextPage')

    # 2. Traitement (Inversé)
    if not new_files:
        log("✅ Tout est à jour.")
        return

    new_files.reverse()
    log(f"📦 Traitement de {len(new_files)} nouveaux articles...")

    for filename in new_files:
        success = False
        for attempt in range(1, 6):
            if translate_file(filename):
                success = True
                break
            log(f"  ⚠️ Retry {attempt}/5 dans 10s...")
            time.sleep(10)

        if not success:
            log(f"❌ ÉCHEC CRITIQUE sur {filename}. Arrêt.")
            sys.exit(1) # Fait échouer le GitHub Action

if __name__ == "__main__":
    run()
