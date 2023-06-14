
from model.contact import Contact


def test_refactor_contact_fields(app):
        if app.contact.count() == 0:
                app.contact.open_form()
                app.contact.filling_in_the_fields(Contact(firstname="goga", middlename="gogievich", lastname="ovakimidis",
                                               nickname="levanich",
                                              company="levancompany", address="Moscow ave.", home_num="9884737",
                                              mob_num="+3993774", work_num="44444", email1="goga@gms.tech", bday="18",
                                              bmanth="December", byear="1998", amonth="November",
                                               aday="17", ayear="2000"))
                app.contact.return_home_page()
        app.contact.edit_contacts(Contact(firstname="levandovski", middlename="Levich", lastname="ovakimidis",
                                               nickname="leonixleo",
                                              company="gogita", address="Moscow ave.", home_num="234",
                                              mob_num="+3993774", work_num="44444", email1="levan@gms.tech", bday="22",
                                              bmanth="December", byear="1998", amonth="November",
                                               aday="17", ayear="1998"))
        app.contact.return_home_page()

