# The conventions

To upload your code you will need to know some very important things ! Else we aren't going to append your function ! :(

## Document your functions !

You will need to document your functions because if someone wants to use your code he will needs to understand ! So let's see how to make a good documentation !

```python
def sendMessage(message, member):
  """
  (The description of your function)
  This function will send a message to a member.
  
  Use it like that : sendMessage(message, member)
  
  message -> Your message. (Type : Str)
  member -> The member who will get your message. (Type : discord.Member)
  """
  
  #Your code...
```

## Add to help

Now you know how to document a function, but the users of the Bot doesn't know that this command exists because it's not on the help message ! Don't worry we have a function for this ;-)

It's called help_append and it takes 3 parametres :
- type : The type of your command (mod/fun/use)
- name : The name of your command
- value : The description of your command

This command must be before your command in the code ! Now let's see how it works !

```python
help_append("mod", "ban", "This function ban a member !\nHow to use : `/ban <member> (reason)`\nRequired Permission : Ban Members")
@slash.slash(...)
async def ban(...):
  ...
  
```

## Easily readable

Do I realy need to say that ? Your code must contains comments and don't be hard to understand, the comments are very usefull because we need to understand what happend in your function ! Look :

```python
def sendMessage(message, member):
  """
  The doc...
  """
  
  member.send(message) # Send a message to the member
  
```

## No errors !!!!

YOUR CODE MUSN'T CONTAINS ERRORS !!!!!!
