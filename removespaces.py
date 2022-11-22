fname = 'mafft.txt'
with open(fname) as in_file:
    contents = in_file.read()
    while '  ' in contents:
        contents = contents.replace(',', '')
# write updated contents back to file
with open(fname, 'w') as out_file:
    out_file.write(contents.replace(',', ''))
