from Interpreter import *

initialize('Test Webpage')
writeHeader('h1', 1, 'This is a test, stand by!')
setColor('h1', 'RED')
setUnderline('h1', True)
setAlignment('h1', 'CENTER')
writeParagraph('p1', 'Paragraph1')
setBold('p1', True)
setItalic('p1', True)
setUnderline('p1', True)
setAlignment('p1', 'RIGHT')
writeImage('image1', 'http://www.uprm.edu/wdt/resources/portico1.gif', 'http://www.uprm.edu')
finalize()
