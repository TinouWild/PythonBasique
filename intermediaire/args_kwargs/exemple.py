def addition(a, b):
    return a + b


print(addition(5, 2))

print('-----------------------------')


def addition(*args):
    return sum(args)


print(addition(10, 23, 50, 1, 2, 5))

print('-----------------------------')


def liste_invites(invite_vip, *args):
    print('{} est un VIP'.format(invite_vip))
    for invite in args:
        print('{} est un invite normal'.format(invite))


liste_invites('Paul', 'Pierre', 'Marie', 'Max')

print('-----------------------------')


def liste_invites(invite_vip, *args, **kwargs):
    print('{} est un VIP'.format(invite_vip))
    for invite in args:
        print('{} est un invite normal'.format(invite))

    oufs= kwargs.get('oufs')
    if oufs:
        print('Ces invites sont oufs: {}'.format(', '.join(oufs)))


liste_invites('Paul', 'Pierre', 'Marie', 'Max', oufs=['Julie'])
