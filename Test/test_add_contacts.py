# -*- coding: utf-8 -*-
from model.contact import Contact


def test_filling_contact_fields(app):
        app.session.login(username="admin", password="secret")
        app.contacts.open_form()
        app.contacts.filling_in_the_fields(Contact(firstname="levan", middlename="levanovich", lastname="ovakimidis",
                                               nickname="levanich",
                                              company="levancompany", address="Moscow ave.", home_num="9884737",
                                              mob_num="+3993774", work_num="44444", email1="levan@gms.tech", bday="18",
                                              bmanth="December", byear="1998", amonth="November",
                                               aday="17", ayear="2000"))

        app.contacts.return_home_page()
        app.session.logout()
