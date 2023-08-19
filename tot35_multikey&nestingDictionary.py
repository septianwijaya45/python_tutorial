import datetime

mhs1 = {
    "nama"      : "Andi Firmansyah",
    "nim"       : "19021992",
    "sks_lulus" : 130,
    "beasiswa"  : False,
    "lahir"     : datetime.datetime(1992,8,12)
}

mhs2 = {
    "nama"      : "Budi Oran",
    "nim"       : "19021992",
    "sks_lulus" : 130,
    "beasiswa"  : False,
    "lahir"     : datetime.datetime(1994,11,2)
}
mhs3 = {
    "nama"      : "Jajan Nurmanto",
    "nim"       : "19021992",
    "sks_lulus" : 130,
    "beasiswa"  : True,
    "lahir"     : datetime.datetime(2000,10,3)
}

dtMhs = {
    "MAH0001": mhs1,
    "MAH0002": mhs2,
    "MAH0003": mhs3
}

print('\n Key Data Mahasiswa \n')
print(dtMhs)

print('\n ==== Dictionary ==== \n')
print(f"{'Key': <6} {'Nama': <17} {'SKS': <3} {'Beasiswa': <9} {'Lahir': <10}")
print('='*50)

for index in dtMhs:
    key = index

    nama        = dtMhs[key]['nama']
    nim         = dtMhs[key]['nim']
    sks         = dtMhs[key]['sks_lulus']
    beasiswa    = dtMhs[key]['beasiswa']
    lahir       = dtMhs[key]['lahir'].strftime("%x")

    print(f"{key: <6} {nama: <17} {sks: <3} {beasiswa: <9} {lahir : <10}")