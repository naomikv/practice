import re

replacements = {
    'wallnut' : 'walnut',
    'acer' : 'Acer',
    'maple' : 'Acer',
    'maple' : 'Acer',
    'vine maples' : 'Acer circinatum',
    'box elder' : 'Acer negundo',
    'Norway Maple' : 'Acer platanoides',
    'Sycamore' : 'Acer pseudoplatanus',
    'silver maple' : 'Acer saccharinum',
    'sugar maple' : 'Acer saccharum',
    'Horse Chestnut' : 'Aesculus hippocastanum',
    'alder' : 'Alnus',
    'Italian alder' : 'Alnus cordata',
    'Common Alder' : 'Alnus glutinosa',
    'grey alder' : 'Alnus incana',
    'speckled alder' : 'Alnus incana',
    'red alder' : 'Alnus rubra',
    'Red Alder' : 'Alnus rubra',
    'Amelanchier alnifolia' : 'Amelanchier alnifolia',
    'Juneberry' : 'Amelanchier alnifolia',
    'saskatoon' : 'Amelanchier alnifolia',
    'Strawberry tree' : 'Arbustus',
    'Pawpaw' : 'Asimina',
    'papaw' : 'Asimina',
    'paw paw' : 'Asimina',
    'birch' : 'Betula',
    'Silver Birch' : 'Betula pendula',
    'Siberian pea tree' : 'Caragana arborescens',
    'Hornbeam' : 'Carpinus',
    'hickory' : 'Carya',
    'pecan' : 'Carya illinoinensis',
    'Chestnut' : 'Castanea',
    'sweet cheestnut' : 'Castanea sativa',
    'Catalpa' : 'Catalpa',
    'Californian lilac' : 'Ceanothus',
    'cedar' : 'cedar',
    'redbud' : 'Cercis canadensis',
    'cornus capitata' : 'Cornus capitata',
    'dogwood' : 'Cornus capitata',
    'Hazel' : 'Corylus',
    'Hazel, C. avellana' : 'Corylus avellana',
    'hazelnut' : 'Corylus avellana',
    'heartnut' : 'Corylus avellana',
    'western hazelnut' : 'Corylus cornuta',
    'Hawthorn' : 'Crataegus',
    'American hawthorn' : 'Crataegus',
    'hawthorn' : 'Crataegus',
    'black hawthorn' : 'Crataegus douglasii',
    'cob nut' : 'crataegus monogyna',
    'Chinese hawthorn' : 'Crataegus pinnatifida',
    'Quince' : 'Cydonia oblonga',
    'quince, cydonia ' : 'Cydonia oblonga',
    'persimmon' : 'Diospyros',
    'Sharon' : 'Diospyros kaki',
    'American persimmon' : 'Diospyros virginiana',
    'Autumn olive' : 'Elaeagnus umbellata',
    'loquat' : 'Eriobotrya japonica',
    'Mespila' : 'Eriobotrya japonica',
    'beech' : 'Fagus',
    'fig' : 'Ficus',
    'fig apple' : 'Ficus',
    'Fig wall trained' : 'Ficus',
    'Ash' : 'Fraxinus',
    'Fruit' : 'fruit',
    'fruit and nut' : 'fruit',
    'gingko' : 'ginkgo biloba',
    'go' : 'ginkgo biloba',
    'honey locust' : 'Gleditsia triacanthos',
    'sea buckthorn' : 'Hippophae',
    'Holly' : 'Ilex',
    'wallnut' : 'Juglans',
    'Walnut' : 'Juglans',
    'butternut' : 'Juglans cinerea',
    'black walnut' : 'Juglans nigra',
    'Walnut, J. regia' : 'Juglans regia',
    'buartnut' : 'Juglans x brixby',
    'juniper' : 'Juniperus',
    'larch' : 'Larix',
    'Ligustrum lucidum' : 'Ligustrum lucidum',
    'tulip poplar' : 'Liriodendron tulipifera',
    'goji berry' : 'Lycium barbarum',
    'apple' : 'Malus domestica',
    'old apple' : 'Malus domestica',
    'Malus fusca' : 'Malus fusca',
    'pacific crabapple' : 'Malus fusca',
    'crab apple' : 'Malus sylvestris',
    'crab' : 'Malus sylvestris',
    'crab apple' : 'Malus sylvestris',
    'crabapple' : 'Malus sylvestris',
    'Malus sylvestris' : 'Malus sylvestris',
    'medlar' : 'Mespilus germanica',
    'mimosa' : 'Mimosa',
    'Mulberry' : 'Morus',
    'white mulberry' : 'Morus alba',
    'black mulberry' : 'Morus nigra',
    'nut trees' : 'nut',
    'nuts' : 'nut',
    'olive' : 'Olea europaea',
    'Chums' : 'other',
    'Mixed conifers and deciduous' : 'Other',
    'Native woodland mixed' : 'Other',
    'Native woodland trees' : 'Other',
    'more are in separate locations on the edge of a forest that surrounds the fields and forest garden.' : 'Other',
    'Other' : 'other',
    'tree' : 'Other',
    'Phyllostachys bamboo' : 'Phyllostachys',
    'bamboo' : 'Phyllostachys',
    'spruce' : 'Picea',
    'Pine' : 'Pinus',
    'Swiss pine' : 'Pinus cembra',
    'pinus koreana' : 'pinus koreana',
    'pinus pinaster' : 'pinus pinaster',
    'pinus pinea' : 'pinus pinea',
    'stone pine' : 'Pinus pinea',
    'poplar' : 'Populus',
    'prunus' : 'Prunus',
    'Apricot' : 'Prunus armeniaca',
    'Prunus avium' : 'Prunus avium',
    'Wild cherries' : 'Prunus avium',
    'bird cherry' : 'Prunus avium (poss P. padus)',
    'Cherry plum' : 'Prunus ceras',
    'Plum' : 'Prunus domestica',
    'Plum' : 'Prunus domestica',
    'Plumb' : 'Prunus domestica',
    'Plum, Herman' : 'Prunus domestica',
    'damson tree' : 'Prunus domestica',
    'damson' : 'Prunus domestica',
    'gage' : 'Prunus domestica',
    'Gauges/Plums/Damsons' : 'Prunus domestica',
    'greengage' : 'Prunus domestica',
    'mirabelle' : 'Prunus domestica',
    'Plum, Herman' : 'Prunus domestica',
    'VIctoria plum' : 'Prunus domestica',
    'almond' : 'Prunus dulcis',
    'Beach plum' : 'Prunus maritima',
    'peach' : 'Prunus persica',
    'peaches' : 'Prunus persica',
    'Japanese plum' : 'Prunus salicina',
    'blackthorn' : 'Prunus spinosa',
    'black thorn' : 'Prunus spinosa',
    'cherry' : 'Prunus_cherry',
    'cherries' : 'Prunus_cherry',
    'Pomegranet' : 'Punica granatum',
    'pear' : 'Pyrus',
    'Asian pear' : 'Pyrus pyrifolia',
    'Chines pears' : 'Pyrus pyrifolia',
    'nashi/asian pear' : 'Pyrus pyrifolia',
    'nashis' : 'Pyrus pyrifolia',
    'Oak' : 'Quercus',
    'Oregon White Oak' : 'Quercus garryana',
    'black oak' : 'Quercus velutina',
    'buckthorn' : 'Rhamnus',
    'Rhamnus purshiana' : 'Rhamnus purshiana',
    'black locust' : 'Robinia pseudoacacia',
    'Stubbed Willows' : 'Salix',
    'willow' : 'Salix',
    'elder' : 'Sambucus',
    'Elder, red leaved' : 'Sambucus',
    'elderberry' : 'Sambucus',
    'sasafras' : 'Sassafras',
    'Rowan' : 'Sorbus acuparia',
    'whitebeam' : 'Sorbus aria',
    'sorbus devoniensis' : 'sorbus devoniensis',
    'sorbus domestica' : 'sorbus domestica',
    'true service tree' : 'Sorbus domestica',
    'lilac' : 'Syringa',
    'lime' : 'Tilia',
    'linden' : 'Tilia',
    'Small leaved lime' : 'Tilia cordata',
    'hemlock' : 'Tsuga',
    'elm' : 'Ulmus',
    'walnut wayfaring tree' : 'Viburnum lantana',
    'guelder rose' : 'Viburnum opulus ',
    'yellowhorn' : 'Xanthoceras sorbifolium',
    'Szechuan pepper' : 'Zanthoxylum',
    'ZANTHOXYLUM' : 'Zanthoxylum',
    'chinese date' : 'Ziziphus jujuba'    
}

data_list = []
output = {}

locations = set()
names = set()

# All lines in the file
lines1 = open('data.txt').readlines()
# All lines in file with leading/trailng whitespace removed
lines2 = map(lambda s : s.strip(), lines1)
# Only non-empty lines from the file
lines3 = filter(lambda l : len(l) > 0, lines2)

for line in lines3:
    line = line.replace(',', '')
    m = re.search('^([0-9]+)\s+(.*)\s+(\.|[0-9]+)$', line)
    if not m:
        raise ValueError('Bad line ' + line)

    location = m.group(1)    

    name = m.group(2).lower()
    name = replacements[name] if name in replacements else name

    count = m.group(3)
    count = 1 if count == '.' else int(count)

    locations.add(location)
    names.add(name)

    data_list.append([location, name, count])

# Initialise the count for each location/name to 0
for location in locations:
    output[location] = {name: 0 for name in names}

# Go through the data read from the file and update the counts in 'output'
for item in data_list:
    location, name, count = item

    output[location][name] = count

sorted_names = sorted(names)
sorted_locations = sorted(locations, key=int)

# Print out the first row of the CSV
print ','.join(['Location'] + sorted_names)

# Prit out the row for each location
for location in sorted_locations:
    count_dict = output[location]
    csv_row = [location]

    for name in sorted_names:
        count_value = count_dict[name]
        csv_row.append(count_value if count_value > 0 else '')

    print ','.join(map(str, csv_row))

