"""
Name:       Kevin Zhao
Program:    zhao_nested.py
Purpose:    Return a set of keys used in any of the inner dictionaries of a nested dictionary
"""

# The nested dictionaries below store information for three famous scientists

authors = {'jgoodall'  : {'surname'  : 'Goodall',
                          'forename' : 'Jane',
                          'born'     : 1934,
                          'died'     : None,
                          'notes'    : 'primate researcher',
                          'author'   : ['In the Shadow of Man',
                                      'The Chimpanzees of Gombe']},
           
           'rfranklin' : {'surname'  : 'Franklin',
                          'forename' : 'Rosalind',
                          'born'     : 1920,
                          'died'     : 1957,
                          'notes'    : 'contributed to discovery of DNA'},
           
           'rcarson'   : {'surname'  : 'Carson',
                          'forename' : 'Rachel',
                          'born'     : 1907,
                          'died'     : 1964,
                          'notes'    : 'raised awareness of effects of DDT',
                          'author'   : ['Silent Spring']}
           }
                         
# Code Here:

keys = set()                            # Define set to store keys

for value in authors.values():          # Loop through values of outer dictionary
    keys = keys | set(value.keys())     # Add each set of inner dictionary keys to keys

print(keys)                             # Print keys