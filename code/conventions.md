# Les conventions

Pour upload ton code tu vas avoir besoin de savoir des choses très importantes ! Sinon on ne va pas ajouter ta fonction ! :(

## Documenter vos fonctions !

Il faut documenter vos fonctions car comme le dit [Guido van Rossum](https://fr.wikipedia.org/wiki/Guido_van_Rossum), *"le code est plus souvent lu qu'écrit"*

```python
def sendMessage(message, member):
  """
  (La description de votre fonction)
  Cette fonction va envoyer un message à un membre
  
  Syntaxe : sendMessage(message, member)
  
  message -> Le message. (Type : Texte)
  member -> Le membre. (Type : discord.Member)
  """
  
#Your code...
```

## Explicite qu'implicite

Ai-je vraiment besoin de le dire ? Votre code doit contenir des commentaires et ne doit pas être difficile à comprendre, les commentaires sont très utiles car nous devons comprendre ce qui se passe dans votre fonction ! Regardez :

```python
def sendMessage(message, member):
  """
  Cette fonction va envoyer un message à un membre...
  """
  
  member.send(message) # Envoie le message au membre
  
```

## Chasseur d'erreur

Si le chasseur repère des erreurs, il les abat, mais le chasseur est vieux, alors assurez-vous de produire un code sans erreur !
