def moyenne (notes):
  return sum(notes)/ len(notes)
def note_max(notes):
    return max(notes)
def mediane (notes):
    tri= sorted(notes)
    n=len(tri)
    return tri[n//2]

def note_min(notes):
    return min(notes)
notes=[12,15,9,18]


print("moyenne :",moyenne (notes))
print("note maximale :",note_max(notes))
print("mediane :",mediane(notes))
print("notemonimale :",note_min(notes))
    

