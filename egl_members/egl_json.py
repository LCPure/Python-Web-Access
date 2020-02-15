import json

egl_data = {}
egl_data['people'] = []
egl_data['people'].append({
    'name': 'Baker, William',
    'initiation chapter': 'Beta',
    'id': '140679'
})
egl_data['people'].append({
    'name': 'Bell, Karl',
    'initiation chapter': 'Rho Theta',
    'id': '131442'
})
egl_data['people'].append({
    'name': 'Bellerand, Athelstan',
    'initiation chapter': 'Psi',
    'id': '143993 '
})
egl_data['people'].append({
    'name': 'Biggs, David',
    'initiation chapter': 'EGL',
    'id': '132349 '
})

with open('egl_data.txt', 'w') as outfile:
    json.dump(egl_data, outfile)
