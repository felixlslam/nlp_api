# Simple NLP APIs

# What is this ? 

A Python that exposes some commonly used API endpoints that can be used for NLP (National Language Processing). 

# Prequisites

* Python 3
* Virtualenv
* Internet Access to github for downloading Spacy model files

# How to run ? 

* Run the following commands in your environment
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python server3.py
```

* Then you can launch the Swagger UI with the URL below to see what APIs are supported, and play with them

[http://localhost:8080/ui/]

