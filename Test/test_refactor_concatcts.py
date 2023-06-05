

def test_filling_contact_fields(app):
        app.session.login(username="admin", password="secret")
        app.contact.edit_contacts()
        app.contact.return_home_page()
        app.session.logout()
