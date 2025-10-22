def hello(*args,**kwargs):
    print(args)
    print(kwargs)

hello('krishna', 'radha', ageA=16, ageB=14)


list = list(('krishna', 'radha'))
dict = {'ageA': 16, 'ageB': 14} 