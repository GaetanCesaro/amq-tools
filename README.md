# AMQ-Tools

AMQ-Tools est un utilitaire d'exploitation des files ActiveMQ.

## Configuration Workspace

L'outil est actuellement en Python 2.7, à migrer en Python 3 avant 2020.

1. Installation Python 2.7 [ici](https://www.python.org/downloads/release/python-2716/)
2. Lancer pip install à la racine du repo pour récupérer les requirements

```
pip install -r requirements.txt
```

## Utilisation

```
python AMQTools.py
```

### Liste des options

**TODO**

| Option                    | Description               |
|---------------------------|---------------------------|
| -p, --pwd PASSWORD        | Password                  |
| -l, --login LOGIN         | Login                     |
| -e, --env ENVIRONNEMENT   | DEV ou INT ou VAL ou IQUA |
| -h, --help                | Aide                      |

NB : Pour consulter l'ensemble des options disponibles 
```
java -jar ladutils.jar options-summary
```

### Liste des actions

**TODO**

| Action             | Description                                          |
|--------------------|------------------------------------------------------|
| rapport AAAA-MM-JJ | Rapport avec les DN demat de la journee              |
| reset ID_DN_DEMAT  | Reinitialise une DN demat                            |
| resetp ID_DN_DEMAT | Reinitialise en conservant les prelistes (mises a 0) |
| supp ID_DN_DEMAT   | Supprime une DN demat                                |
| verif ID_DN_DEMAT  | Rapport sur une DN demat                             |
| verifdn ID_DN      | Rapport sur une DN                                   |
| suppdn ID_DN       | Supprime une DN                                      |
| compte NUM SUFF AAAAMMJJ AAAAMMJJ AAAAMMJJ | Information sur le compte en fonction de 3 dates : Début période ; Fin période ; Début période RBS |
| xmlencod FILE_NAME | Encode un xml de utf8 vers iso-8859-1 |


### Exemples d'utilisation

**TODO**

```
java -jar ladutils.jar -l INFTEST -p INFTEST -e INT rapport 2017-03-10
java -jar ladutils.jar -l INFTEST -p INFTEST -e INT verifdn 123456
java -jar ladutils.jar -l INFTEST -p INFTEST -e INT suppdn 123456
```