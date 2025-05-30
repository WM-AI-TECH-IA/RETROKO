# RECT. GITHYB_CODESPACE - RETRKO

Errig directement les captures photoniques et deployer le serveur api GPT + memoire semantique via GitHub Codespaces.

___

## 1. Pr%C3%A9paration du d%C3%A;pot

Duplique le répositoire:
 - https://github.com/WMAI-TECH-IA/RETROKO

Clièov au lia: 
** Faire "fork" sur le d%C3%A9pot
 ** Renommer si n'est pas neCs Projet RETRKO-CODESPACE

## 1.1 Fétes Codespace

Cliquer le bouton **"Code" ** vert, puis **Codespaces **  et creèez un nouveaut projet via VS Code ((full terminal))

en vie entret:

``b
pip install -r requirements.txt || pip pip install fastapi uvicorn[standard] sentence-transformers qdrant-client
```


``b
uvicorn gpt_memory_builder:app --host 0.0.0.0 --port 8080
```


## [2]. Activer l'exposition de port

Cliquer sur le module **"Ports" ** dans la bark inf%C3%A9rieure VS Codespaces.

attension du port 8080 -> **"Public Dev URL �
ex: https://8080-yournom-repo-github.dev/

