from pytest_bdd import given, when, then
from model.add_new import AddNew
import random
import pytest


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <lastname>, <firstname> and <address>')
def new_contact(lastname, firstname, address):
    return AddNew(my_l_name=lastname, my_f_name=firstname, work_address=address)


# Add contact

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.create_contact(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=AddNew.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                    key=AddNew.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contacts.create_contact(AddNew(my_f_name="Petcold contact"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


# Delete contact

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contacts.delete_contact_by_id(random_contact.my_id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=AddNew.id_or_max) == sorted(app.contacts.get_contact_list(),
                                                                    key=AddNew.id_or_max)


# Modify contact

@given('a random contact from the list')
def index_random_contact(non_empty_contact_list):
    index_random_contact = random.randrange(len(non_empty_contact_list))
    return index_random_contact


@given('a contact with <lastname>, <firstname>, <address>, <homephone>, <mobilephone>, <workphone>, '
       '<secondaryphone>, <email>, <email2> and <email3>')
def contact_modify(lastname, firstname, address, homephone, mobilephone, workphone, secondaryphone, email, email2,
                   email3):
    return AddNew(my_l_name=lastname, my_f_name=firstname, work_address=address,
                  my_h_telefon=homephone, my_mobile=mobilephone, my_work_telefon=workphone,
                  my_secondary_phone=secondaryphone,
                  my_company_mail=email, my_second_mail=email2, my_third_mail=email3)


@when('I modify the contact in the list')
def modify_contact(app, non_empty_contact_list, index_random_contact, contact_modify):
    contact_modify.my_id = non_empty_contact_list[index_random_contact].my_id
    app.contacts.modify_contact_by_id(contact_modify.my_id, contact_modify)


@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, index_random_contact, contact_modify, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index_random_contact] = contact_modify
    assert sorted(old_contacts, key=AddNew.id_or_max) == sorted(new_contacts, key=AddNew.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=AddNew.id_or_max) == sorted(app.contacts.get_group_list(), key=AddNew.id_or_max)
