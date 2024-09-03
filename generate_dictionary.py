import os
import re


# Set the directory to search for '.tex' files
directory = '.'

# Define the pattern to match against
pattern = r'\\پاورق\s*?{(.+?)}\s*?{(.+?)}'

# Initialize a list to store the matched results
matched_results = []

# Traverse the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    # Loop over each file in the directory
    for filename in files:
        # Check if the file is a '.tex' file
        if filename.endswith('.tex'):
            # Read the content of the file
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding="utf-8") as file:
                content = file.read()
            # Match the content against the pattern
            matches = re.findall(pattern, content)
            # Append the matched results to the list
            for match in matches:
                matched_results.append([m.strip() for m in match])


matched_results = sorted(matched_results, key=lambda x: x[0])


with open('front/dictionary.tex','w',encoding='utf-8') as texfile:
    texfile.write(r"""
    \rhead{واژه‌نامه فارسی به انگلیسی}

    \chapter*{واژه‌نامه فارسی به انگلیسی}
    \begin{multicols}{2}
    \small
    """)
    previous_letter = ''
    for farsi,english in matched_results:
        current_letter = farsi[0]
        if previous_letter != current_letter:
            texfile.write(f'\n\t\\dicalphabet{{{current_letter}}}\n')
            previous_letter = current_letter

        texfile.write(f'\t\\dic{{{english.capitalize()}}}{{{farsi}}}\n')


    texfile.write(r"""
    \end{multicols}

    \newpage
    """)

matched_results = sorted(matched_results, key=lambda x: x[1])

with open('front/dictionary_en.tex','w',encoding='utf-8') as texfile:
    texfile.write(r"""
    \rhead{واژه‌نامه انگلیسی به فارسی}

    \chapter*{واژه‌نامه انگلیسی به فارسی}
    \begin{multicols}{2}
    \LTRmulticolcolumns
    \small
    """)
    previous_letter = ''
    for farsi,english in matched_results:
        current_letter = english[0]
        if previous_letter != current_letter:
            texfile.write(f'\n\t\\dicalphabet{{{current_letter.upper()}}}\n')
            previous_letter = current_letter

        texfile.write(f'\t\\dic{{{english.capitalize()}}}{{{farsi}}}\n')


    texfile.write(r"""
    \end{multicols}

    \newpage
    """)
