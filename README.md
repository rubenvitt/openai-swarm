## OpenAI swarm test

1. Install this project by adding dependencies:

```python
pip install git+https://github.com/openai/swarm.git
```

2. Run this project by setting your API key as env variable (e.g. with 1Pass CLI):

```sh
OPENAI_API_KEY=$(op item get "OpenAI API Key" --fields password --reveal) python main.py
```
