---
title: How to Work with YAML in Python – A Guide with Examples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2025-12-10T22:58:47.038Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-yaml-in-python-a-guide-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1765407508788/61769835-bd12-486e-8f8e-ba0f3a7af83c.png
tags:
- name: Python
  slug: python
- name: YAML
  slug: yaml
seo_title: null
seo_desc: 'If you''ve ever worked with configuration files, Docker Compose, Kubernetes,
  or CI/CD pipelines, you''ve probably used YAML. It''s everywhere in modern development,
  and for good reason: it’s human-readable, simple, and powerful.

  In this guide, you''ll le...'
---

If you've ever worked with configuration files, Docker Compose, Kubernetes, or CI/CD pipelines, you've probably used YAML. It's everywhere in modern development, and for good reason: it’s human-readable, simple, and powerful.

In this guide, you'll learn how to work with YAML files in Python. We'll cover reading, writing, and manipulating YAML data in practice.

🔗 [**You can find the code on GitHub**](https://github.com/balapriyac/python-basics/tree/main/config-management-basics/working-with-yaml).

## Prerequisites

Before working with YAML in Python, you should have:

* Python 3.8 or a later version installed
    
* **Basic Python knowledge**: Variables, data types, functions, and control structures
    
* **Understanding of data structures**: Dictionaries, lists, and nested data structures
    
* **File handling basics**: Reading from and writing to files in Python
    
* **Command line familiarity**: Running Python scripts and installing packages with `pip`
    

You'll also need to install the [PyYAML](https://pypi.org/project/PyYAML/) library:

```bash
pip install pyyaml
```

## Table of Contents

1. [What Is YAML and Why Should You Care?](#heading-what-is-yaml-and-why-should-you-care)
    
2. [How to Read YAML Files](#heading-how-to-read-yaml-files)
    
3. [How to Write YAML Files](#heading-how-to-write-yaml-files)
    
4. [How to Work with Lists in YAML](#heading-how-to-work-with-lists-in-yaml)
    
5. [Build a YAML Config Manager](#heading-build-a-yaml-config-manager)
    

## What Is YAML and Why Should You Care?

YAML (YAML Ain't Markup Language) is a data serialization format designed to be easy to read and write. Think of it as JSON's more readable cousin. :)

Here's the same data in JSON and YAML:

JSON:

```json
{
  "database": {
    "host": "localhost",
    "port": 5432,
    "credentials": {
      "username": "admin",
      "password": "secret"
    }
  }
}
```

YAML:

```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: admin
    password: secret
```

The YAML version is cleaner and easier to read, especially for configuration files.

## How to Read YAML Files

Let's say you have a configuration file for a web application. We'll create a simple [`config.yaml`](https://github.com/balapriyac/python-basics/blob/main/config-management-basics/working-with-yaml/config.yaml) file and learn how to read it in Python.

First, let's understand what we're trying to do. You have configuration data stored in a YAML file, and you want to load it into Python so you can use it in your application. Here’s how you can do it:

```python
import yaml

# Open and read the YAML file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

# Access the data
print(config['database']['host'])
```

Output:

```plaintext
localhost
```

Here's what's happening in this code:

* We import the `yaml` module.
    
* Then we open the file using a context manager (`with` statement), which automatically closes the file when we're done.
    
* We use `yaml.safe_load()` to parse the YAML content into a Python dictionary so we can access the data just like any Python dictionary.
    

⚠️ Note that you should **always use** `yaml.safe_load()` **instead of** `yaml.load()`**.** The `safe_load()` function protects you from arbitrary code execution vulnerabilities. Unless you have a very specific reason (and you probably don't), stick with `safe_load()`.

## How to Write YAML Files

Now let's go in the opposite direction. You have Python data structures and you want to save them as YAML files. This is useful when you're generating configuration files or exporting data.

```python
import yaml

# Your configuration data as Python dictionaries
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'name': 'myapp_db',
        'credentials': {
            'username': 'admin',
            'password': 'secret123'
        }
    },
    'server': {
        'host': '0.0.0.0',
        'port': 8000,
        'debug': True
    },
    'features': {
        'enable_cache': True,
        'cache_ttl': 3600
    }
}

# Write to a YAML file
with open('generated_config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
```

Let's break down what's happening:

* We create a nested Python dictionary with our configuration.
    
* We open a file in write mode (`'w'`).
    
* We use `yaml.dump()` to convert the Python dictionary to YAML format and write it to the file.
    
* The `default_flow_style=False` parameter ensures the output uses block style (the readable, indented format) instead of inline style.
    

The resulting `generated_config.yaml` file will be properly formatted and ready to use.

## How to Work with Lists in YAML

YAML handles lists elegantly, and they're common in configuration files. Suppose you're building a microservices application and need to configure multiple service endpoints. Here's how you'd work with that data:

```python
import yaml

# Configuration with lists
services_config = {
    'services': [
        {
            'name': 'auth-service',
            'url': 'http://auth.example.com',
            'timeout': 30
        },
        {
            'name': 'payment-service',
            'url': 'http://payment.example.com',
            'timeout': 60
        },
        {
            'name': 'notification-service',
            'url': 'http://notification.example.com',
            'timeout': 15
        }
    ],
    'retry_policy': {
        'max_attempts': 3,
        'backoff_seconds': 5
    }
}

# Write to file
with open('services.yaml', 'w') as file:
    yaml.dump(services_config, file, default_flow_style=False, sort_keys=False)

# Read it back
with open('services.yaml', 'r') as file:
    loaded_services = yaml.safe_load(file)

# Access list items
for service in loaded_services['services']:
    print(f"Service: {service['name']}, URL: {service['url']}")
```

Output:

```plaintext
Service: auth-service, URL: http://auth.example.com
Service: payment-service, URL: http://payment.example.com
Service: notification-service, URL: http://notification.example.com
```

This code helps us understand a few key concepts.

We can nest lists and dictionaries freely in our Python data structures. The `sort_keys=False` parameter preserves the order of keys as we defined them. When we read the YAML back, we can iterate over lists just like any Python list. The data structures in Python match the structures in YAML.

## Build a YAML Config Manager

Let's put everything together with a practical example. We'll build a simple configuration manager class that handles environment-specific configs (a common need in real projects):

```python
import yaml
import os

class ConfigManager:
    def __init__(self, config_dir='configs'):
        self.config_dir = config_dir
        self.config = {}
    
    def load_config(self, environment='development'):
        """Load configuration for a specific environment"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        try:
            with open(config_file, 'r') as file:
                self.config = yaml.safe_load(file)
            print(f"✓ Loaded configuration for {environment}")
            return self.config
        except FileNotFoundError:
            print(f"✗ Configuration file not found: {config_file}")
            return None
        except yaml.YAMLError as e:
            print(f"✗ Error parsing YAML: {e}")
            return None
    
    def get(self, key_path, default=None):
        """Get a configuration value using dot notation"""
        keys = key_path.split('.')
        value = self.config
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def save_config(self, environment, config_data):
        """Save configuration to a file"""
        config_file = os.path.join(self.config_dir, f'{environment}.yaml')
        
        os.makedirs(self.config_dir, exist_ok=True)
        
        with open(config_file, 'w') as file:
            yaml.dump(config_data, file, default_flow_style=False)
        
        print(f"✓ Saved configuration for {environment}")
```

This `ConfigManager` class shows you how to build a practical utility:

1. **Initialization**: We set up a directory for config files.
    
2. **Loading**: The `load_config()` method reads environment-specific YAML files with proper error handling.
    
3. **Accessing data**: The `get()` method lets you access nested values using dot notation (like `'database.host'`).
    
4. **Saving**: The `save_config()` method writes configuration data to YAML files.
    

This is the kind of pattern you might actually use in projects. You can extend it further by adding validation, environment variable overrides, or configuration merging. Here’s how you can use the `ConfigManager` class we’ve coded:

```python
if __name__ == '__main__':
    # Create config manager
    config_mgr = ConfigManager()
    
    # Create a sample development config
    dev_config = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'name': 'dev_db'
        },
        'api': {
            'base_url': 'http://localhost:8000',
            'timeout': 30
        }
    }
    
    # Save it
    config_mgr.save_config('development', dev_config)
    
    # Load and use it
    config_mgr.load_config('development')
    print(f"Database host: {config_mgr.get('database.host')}")
    print(f"API timeout: {config_mgr.get('api.timeout')}")
```

Running the above code should give you the following output:

```plaintext
✓ Saved configuration for development
✓ Loaded configuration for development
Database host: localhost
API timeout: 30
```

## Conclusion

YAML is a powerful tool in your developer toolkit. It comes in handy when you’re configuring applications, defining CI/CD pipelines, or working with infrastructure as code.

In this article, you learned how to work with YAML files in Python. You can read configuration files, write data to YAML format, handle lists and nested structures, and build practical utilities like the `ConfigManager` we coded.

Start small. Try replacing a JSON config file in one of your projects with YAML. You'll quickly appreciate how much more readable it is, and you'll be comfortable working with YAML across the tools and platforms that use it.

Happy coding!
