# List ip adresses using python
![Static Badge](https://img.shields.io/badge/On%20Date-True-green?style=plastic&logoColor=blue)
>Le script est lent a run, complexité pourrie ? peut-etre 🧙🏼

## Description
Ce projet scan votre reseau (si vos firewalls l'autorise 🤯) et retourne une comprehension list de toutes les adresses ip sur le reseau dans un fichier json. 

**Exemple**:
```
[192.1.1.1, 192.2.2.2, 192.3.3.3] ...
```

## Requis

```bash
pip install python-dotenv 

```

- Créez un fichier .env dans la racine du projet
- Dans .env, créez la variable **NETWORK_RANGE** par rapport a votre réseau
- La plupart des cas : ```NETWORK_RANGE=192.168.1.0/24```

## Execution 
```
cd src/
python main.py
```

**Le script créera un fichier results/real dans lequel sera stocké votre fichier ips.json** 😎
 
made by Mathieu A. 🤭
