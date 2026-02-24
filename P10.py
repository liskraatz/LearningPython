# Lisa Kraatz

def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    
# Length
    print('Length: ',len(thetext))
    print('\n')
    
    # Remove Spaces
    thetext = thetext.strip()
    print('Text without spaces:\n',thetext)
    print('\n')
    print('New Length: ',len(thetext))
    
# Count 'the'
    count = thetext.count('the')
    print('\nCount of "the": ',count)
    print('\n')
    
# Check for "little"
    if ('little' not in thetext):
        print('The text does not include the word "little".')
    else:
        print('The text includes the word "little".')
    print('\n')
        
# Check for "titan"
    if ('titan' in thetext):
        print('The text includes the word "titan".')
    else:
        print('The text does not include the word "titan".')
    print('\n')
    
    # Find position of "appl"
    position = thetext.find('appl')
    print('Position of "appl" is: ',position)
    print('\n')
    
    # Copy string to another variable
    thetext2 = thetext[0:]
    thetext2 = thetext2.replace("Python","PYTHON")
    print('The new string:\n',thetext2)
    print('\n')
    
    return

# Main

main()
