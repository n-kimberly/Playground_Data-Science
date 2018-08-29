import json
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from pygal.maps.world import World
from pygal.maps.world import COUNTRIES

filename = 'world_pop.json'

with open(filename) as f:
    objlist = json.load(f)

# Reverse index COUNTRIES dict
rev_COUNTRIES = {}
for code, name in COUNTRIES.items():
    rev_COUNTRIES[name] = code

# Create hash of code & population for year 2010
cc_populations = {}

for obj in objlist:
    if obj['Year'] == '2010':
        # Discrepancies should be skipped over or handled case by case
        code = rev_COUNTRIES.get(obj['Country Name'], None)
        if code is None:
            continue 
        population = int(float(obj['Value']))
        cc_populations[code] = population

print(cc_populations)

# Group countries into 3 population levels
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
part1 = 5*10**6
part2 = 25*10**6
for key, pop in cc_populations.items():
    if pop < part1:
        cc_pop1[key] = pop
    elif pop < part2:
        cc_pop2[key] = pop
    else:
        cc_pop3[key] = pop

# Create world map with pygal
print(len(cc_pop1), len(cc_pop2), len(cc_pop3))
wm = World(style=RS('#17A589', base_style=LCS))
wm.title = 'World Population in 2010, by Country'
wm.add('0-5m', cc_pop1)
wm.add('5m-25m', cc_pop2)
wm.add('25m+', cc_pop3)
wm.render_to_file('world_pop.svg')
