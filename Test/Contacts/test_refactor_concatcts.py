
from model.contact import Contact


def test_refactor_contact_fields(app):
        if app.contact.count() == 0:
                app.contact.open_form()
                app.contact.filling_in_the_fields(Contact(firstname="goga", middlename="gogievich", lastname="garagarik",
                                nickname="gogich",
                                company="gogacompany", address="Moscow ave.", home_num="9884737",
                                mob_num="+3993774", work_num="4442344", email1="levan@gms.tech",
                                bday="18",
                                bmanth="December", byear="1998", amonth="November",
                                aday="17", ayear="2000"))
                app.contact.return_home_page()
        app.contact.edit_contacts(Contact(firstname="levandovski", middlename="astraxan", lastname="Пражский",
                                          nickname="pochka"))
        app.contact.return_home_page()

