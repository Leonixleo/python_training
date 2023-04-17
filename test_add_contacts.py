# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_for_contacts import Application_for_contact


@pytest.fixture
def app(request):
    fixture = Application_for_contact
    request.addfinalizer(fixture.destroy)
    return fixture



def filling_contact_fields_test_case(app):
        app.login(username="admin", password="secret")
        app.open_contact_form()
        app.filling_in_the_fields(Contact(firstname="levan", middlename="levanovich", lastname="ovakimidis",
                                               nickname="levanich",
                                               company="levancompany", address="Moscow ave.", home_num="9884737",
                                               mob_num="+3993774", work_num="44444", email1="levan@gms.tech", bday="18",
                                               bmanth="December", byear="1998", amonth="November",
                                               aday="17", ayear="2000"))
        app.return_home_page()
        app.logout()
