from fixture.orm import ORMFixture

db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")

try:
    l = orm.get_contacts_in_group(Group(id="108"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
