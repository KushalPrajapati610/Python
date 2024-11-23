#31. You have a list of your favourite marvel super heroes.

#heros=['spider man','thor','hulk','iron man','captain america']

#Using this find out,

#1. Length of the list
heros = ['spider man','thor','hulk','iron man','captain america']
print(len(heros))


#2. Add 'black panther' at the end of this list
heros = ['spider man','thor','hulk','iron man','captain america']
heros.append("black panther")
print(heros)


#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'
heros = ['spider man','thor','hulk','iron man','captain america','black panther']
heros.remove("black panther")
print(heros)
heros[3] = 'black panther'
print(heros)


#4. Now you don't like thor and hulk because they get angry easily :)
#   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
heros = ['spider man','thor','hulk','iron man','captain america','black panther']
heros.pop(2)
heros[1]="doctor strange"
print(heros)