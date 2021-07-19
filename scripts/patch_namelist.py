import sys

import f90nml
import pandas as pd


# Takes two arguments, csv patch file and namelist to patch
(patchfile, namelist) = sys.argv[1:]

# Read in csv of data to patch namelist
patchdata = pd.read_csv(patchfile)

# Read in namelist to alter
namelist = f90nml.read(namelist)

for (group,variable,value) in patchdata.values:
    # Remove leading ampersand
    group = group[1:]

    # Check if this is a string repr of a python variable
    try:
        value = eval(value.title())
    except (NameError, SyntaxError) as e:
        pass

    # Special case for values to remove from namelist
    # otherwise just patch
    if value == 'DELETE':
        del(namelist[group][variable])
    else:
        namelist.patch({group: {variable: value}})

# Remove empty groups for neatness
for group in list(namelist.keys()):
    if len(namelist[group]) == 0:
        del(namelist[group])

# Print result to stdout
print(namelist)