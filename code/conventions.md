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

## Implémenter au help

Une commande n'existe pas si elle n'est pas affichée au help, nous développeur, nous qui avons accès au code, nous qui voyons le code, les membres ne le voient pas.

La fonction se nomme `help_append()` et doit remplir trois critères :
- type : Le type de la commande (mod/fun/use) (A renseigner seulement si vous travaillez dans le main.py !)
- name : Le nom de votre commande
- value : La desciption de votre commande

La fonction doit être **avant** la commande !

```python
help_append("mod", "ban", "Cette fonction va bannir un membre !\nSyntaxe : `/ban <member> (reason)`\nPremission requise : `Ban Members`")
@slash.slash(...)
async def ban(...):
  ...
  
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
