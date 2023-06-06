from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.open_form()
        app.contact.filling_in_the_fields(Contact(firstname="levan", middlename="levanovich", lastname="ovakimidis",
                                                  nickname="levanich",
                                                  company="levancompany", address="Moscow ave.", home_num="9884737",
                                                  mob_num="+3993774", work_num="44444", email1="levan@gms.tech",
                                                  bday="18",
                                                  bmanth="December", byear="1998", amonth="November",
                                                  aday="17", ayear="2000"))
        app.contact.return_home_page()
    app.contact.delete_first_contact()

