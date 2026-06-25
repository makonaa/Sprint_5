# DOSKA UI-Automation
## test files
### test_user_sign_up.py

contains tests:

- test_new_user_sign_up_successful
- test_incorrect_email_error_shown
- test_signup_of_existing_user_error_shown

### test_user_login_and_logout

contains tests:

- test_user_login
- test_user_logout

### test_create_listing

contains tests:

- test_create_listing_unauthorized_login_popup_shown
- test_create_listing_success

## other files

### conftest.py

- contains setup for driver and generation of emails, item name and price

### testdata.py

- contains some data pieces for comparison or filling in the info (password, error_color)

### locators.py

- contains classes of different locators for every page/flow covered by tests

### help_functions.py

- contains functions for repeated actions throughout the tests - sign up, login, exit
