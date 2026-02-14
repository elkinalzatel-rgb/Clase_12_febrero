party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
def late(list, name):
    if list.index(name) == len(list)-2 or list.index(name) == len(list)-3:
        print("el invitado ", name, "esta tardecito")
    else: print("el invitado ", name, "no esta tardecito")
late(party_attendees, 'Adela')
late(party_attendees, 'Mona')