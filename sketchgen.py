import argparse

#parameter defaults
basefile = 'base.template'

#argument parser
parser = argparse.ArgumentParser()

parser.add_argument('-b', '--basefile', help='Specify a different base file')

required = parser.add_argument_group('required arguments')
required.add_argument('-o', '--outfile', help='Address of file to be created or overwritten', required=True)
required.add_argument('-i', '--infile', help='Address of macro config file', required=True)

args = parser.parse_args()

#set parameters from arguments
outfile = args.outfile
infile = args.infile
if args.basefile:
    basefile = args.basefile

#get macro config file as list of lines
with open(infile, 'r') as f:
    lines = f.readlines()

#make macros
macros = {
    'A': '',
    'B': '',
    'C': '',
    'D': ''
}
for line in lines:
    s = line.rstrip().split(' ', 1)
    if len(s) > 0:
        if s[0] == "START":
            current = s[1]
            macros[current] += 'void macro' + current + '() {\n'
        elif s[0] == "END":
            macros[current] += '}\n'
        elif s[0] == "HOLD":
            for key in s[1].split('+'):
                macros[current] += '    Keyboard.press(' + key + ');\n'
        elif s[0] == "WAIT" or s[0] == "DELAY":
            macros[current] += '    delay(' + s[1] + ');\n'
        elif s[0] == "TYPE":
            macros[current] += '    Keyboard.print(' + s[1] + ');\n'
        elif s[0] == "RELEASE":
            macros[current] += '    Keyboard.release(' + s[1] + ');\n'
        elif s[0] == "RELEASEALL":
            macros[current] += '    Keyboard.releaseAll();\n'
        elif s[0] == "COMBO":
            for key in s[1].split('+'):
                macros[current] += '    Keyboard.press(' + key + ');\n'
            macros[current] += '    Keyboard.releaseAll();\n'
        elif s[0] == "KEY" or s[0] == "PRESS":
            macros[current] += '    Keyboard.write(' + s[1] + ');\n'

#put together the sketch
with open(outfile, 'w') as out:
    with open(basefile, 'r') as base:
        out.write(base.read())
        out.write(macros['A'])
        out.write(macros['B'])
        out.write(macros['C'])
        out.write(macros['D'])
