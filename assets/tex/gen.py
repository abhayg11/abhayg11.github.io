
import sys
import os
import re

USAGE = """For generating problems in a chapter/section, execute:
python gen.py <bookname> <chapter/section> <problem_count>
E.g.
python gen.py qingliu 3/2 21

For generating a chapter tex file, execute:
python gen.py <bookname> <chapter>
E.g.
python gen.py qingliu 3
"""

PREAMBLE = r"""\documentclass{article}
\input{../tmpl/packages.tex}
\input{../tmpl/defs.tex}

\begin{document}
\pagestyle{plain}
\thispagestyle{empty}

\noindent
\begin{tabular*}{\textwidth}{l @{\extracolsep{\fill}} r @{\extracolsep{6pt}} l}
\textbf{<book>: Solutions} & \textbf{Name:} & Abhay Goel \\
\textbf{Chapter <chapter>} & \textbf{Date:} & \today \\
\end{tabular*} \\
\rule[2ex]{\textwidth}{2pt}

"""

if len(sys.argv) < 3:
    print(USAGE)
    exit()

book = sys.argv[1]
section = sys.argv[2]
section_dot = section.replace('/','.')
if len(sys.argv) > 3:
    problem_count = int(sys.argv[3])
    for i in range(problem_count):
        fout = open(book+'/Chapters/'+section+'/'+str(i+1)+'.tex','x')
        fout.write('\\mtexe{'+section_dot+'.'+str(i+1)+'}\n\\begin{proof}\n\t\n\\end{proof}\n')
        fout.close()
else:
    fout = open(book+'/Chapter'+section+'.tex','x')
    preamble = PREAMBLE.replace('<book>', book).replace('<chapter>', section)
    fout.write(preamble)
    for (dir,_,fs) in os.walk(book+'/Chapters/'+section):
        for x in sorted(fs,key=lambda y:int(re.sub(r'\D','',y))):
            fout.write('\\input{'+(dir.replace('\\','/')[len(book)+1:]+'/'+x)+'}\n')
    fout.write('\n\\end{document}\n')
    fout.close()
