# AMQ-Tools

AMQ-Tools est un utilitaire d'exploitation des files ActiveMQ.

## Configuration Workspace

L'outil fonctionne en Python 3.7.

1. Installation Python 3.7 [ici](https://www.python.org/downloads/release/python-374/) ou spérieur 
2. Vérifier que la racine de l'installation Python est bien dans votre PATH (ainsi que le sous dossier Scripts)
2. Lancer la commande pip ci-dessous à la racine du repo pour récupérer les librairies nécessaires :


```
pip install -r requirements.txt
```

## Utilisation

### Exemples d'utilisation

```
python AMQTools.py -f PRD -a retryMessagesAllQueues
python AMQTools.py -f PRD -a retryMessages -q QGENGPP
python AMQTools.py -f PRD -a exportExcel -q QGENGPP
python AMQTools.py -f VAL -t LOCALHOST -a postFirstMessage -q Consumer.SGENGPP.VirtualTopic.TDATALEGACY
python AMQTools.py -f PRD -t DEV -a postAllMessages -q Consumer.SGENGPP.VirtualTopic.TDATALEGACY 
```

### Liste des options

| Option                              | Description                                                         |
|-------------------------------------|---------------------------------------------------------------------|
| -h, --help                          | Aide                                                                |
| -f <environnement_source> (--from)  | Environnement source où vont être récupérés les messages JMS        |
| -t <environnement_cible> (--to)     | Environnement cible où vont être envoyés les messages JMS           |
| -q <queue_cible> (--queue)          | File MQ cible. La file MQ source sera déduite en préfixant par DLQ. |
| -a <action> (--action)              | Action exécutée. Voir la liste des actions possibles ci-dessous     |

### Valeurs possibles

- Environnements possibles : LOCALHOST, DEV, INT, VAL, QUA, PRD
- Queues possibles : Consumer.SGENGPP.VirtualTopic.TDATALEGACY, Consumer.SGENCLI.VirtualTopic.TDATAGPP, QGENGPP, SRECDNO, SGENGED, SRECOBL, QDATALEGACY, ...

### Liste des actions

| Action                 | Description                                                                           |
|------------------------|---------------------------------------------------------------------------------------|
| retryMessages          | Réjoue tous les messages de la file DLQ associée sur l'environnement source           |
| retryMessagesAllQueues | Réjoue tous les messages de toutes les files DLQ                                      |
| exportExcel            | Un fichier Excel contenant les messages JMS de la DLQ associée est généré             |
| postFirstMessage       | Récupère les messages de la file source et poste le 1er message dans la file cible    |
| postAllMessages        | Récupère les messages de la file source et poste tous les messages dans la file cible |
