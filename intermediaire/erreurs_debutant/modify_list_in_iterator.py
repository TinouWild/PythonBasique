# prenoms = ['Pierre', 'Julien', 'Marie', 'Paul']
# for i in range(len(prenoms)):
#     if prenoms[i] == 'Julien':
#         del prenoms[i]

# bonne pratique
prenoms = ['Pierre', 'Julien', 'Marie', 'Paul']
prenoms_sans_julien = [p for p in prenoms if p != 'Julien']
print(prenoms_sans_julien)
