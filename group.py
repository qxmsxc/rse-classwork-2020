group = {'Jill':{
                  'age':26, 
                  'job':'biologist', 
                  'connections': {'friends' : ['Zalika'],
                                  'partner':'John'}
                },
         'Zalika':{
                   'age':28,
                   'job':'artist',
                   'connections': {
                                   'friends':['Jill'],
                                   'landlord':['Nash']
                                  }
                  },
         'John':{
                  'age':27, 
                  'job':'writer', 
                  'connections': {
                                  'partner':'Jill',
                                  'cousins':['Nash']
                                 }
                },
         'Nash':{
                  'age':34, 
                  'job':'chef', 
                  'connections': {
                                  'cousins':['John'],
                                  'tenants':['Zalika']
                                 }
                },
        }

print(group)