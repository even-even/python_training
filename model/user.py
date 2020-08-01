from sys import maxsize


class User:
    def __init__(self, firstname = None, middlename = None, homepage = None, phone2 = None, notes = None,
                 address2 = None, email3 = None, email2 = None, email = None, fax = None, work = None, mobile = None,
                 home = None, address = None, company = None, title = None, nickname = None, lastname = None,
                 id = None, name = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.name = name

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name is None or other.name is None or self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
