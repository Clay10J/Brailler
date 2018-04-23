def makeScript(filenames):
    with open('script.gcode', 'w') as outfile:
            for fname in filenames:
                     with open(fname) as infile:
                                     outfile.write(infile.read())
    return True
