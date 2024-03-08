error_messages = {
    'field_not_filled_in': 'Поле не заполнено',
    'correct_referral_code_message': 'Реферальный код дает скидку',
    'referral_incorrect_link_format': 'Неверный формат ссылки',
    'username': 'Допустимые символы (от 6 до 32): a-z, 0-9, _. Имя должно начинаться с буквы',
    'email': 'Формат e-mail: somebody@somewhere.ru',
    'password_too_short': 'Пароль должен содержать минимум 8 символов',
    'password_general': 'Пароль должен содержать от 8 до 64 символов, включая заглавные буквы и цифры',
}

sign_up_data = [
     {   # ID теста
         'test_id': 1,
         # Имя пользователя
         'username': '',
         # Ожидаемая ошибка в валидации имени пользователя
         'username_error': error_messages['field_not_filled_in'],
         # Email
         'email': '',
         # Ожидаемая ошибка в валидации email
         'email_error': error_messages['field_not_filled_in'],
         # Пароль
         'password': '',
         # Проходит ли пароль валидацию? True - да, False - нет
         'is_password_correct': False,
         # Ожидаемая ошибка в валидации пароля (Если не прошёл валидацию)
         'password_error': error_messages['field_not_filled_in'],
         # Реферальный код
         'referral_code': 'asdf',
         # Ожидаемое сообщение в валидации реферального кода
         'referral_code_message': error_messages['correct_referral_code_message'],
         # Кликнуть чекбокс? True - да, False - нет
         'click_checkbox': False,
         # Ожидаемый статус чекбокса. Unchecked - ошибка при отправке формы, Checked - Чекнут, Off - не чекнут
         'expected_checkbox_status': 'Unchecked',
         # Отправлять ли форму? True - да, False - нет
         'submit_form': True,
         # Неактивна ли кнопка отправки формы? True - неактивна False - активна
         'is_submit_button_inactive': False,
     },
     {
        'test_id': 2,
        'username': 'Walde',
        'username_error': error_messages['username'],
        'email': 'asdf',
        'email_error': error_messages['email'],
        'password': 'Asdfgh9',
        'is_password_correct': False,
        'password_error': error_messages['password_too_short'],
        'referral_code': 'www',
        'referral_code_message': error_messages['referral_incorrect_link_format'],
        'click_checkbox': True,
        'expected_checkbox_status': 'Checked',
        'submit_form': False,
        'is_submit_button_inactive': True,
     },
     {
        'test_id': 3,
        'username': 'СиаКономик',
        'username_error': error_messages['username'],
        'email': 'asdfg',
        'email_error': error_messages['email'],
        'password': 'SecurePassw0rd2024WithNumbersAndCapitalLetterForYou123XYZ456ABC78',
        'is_password_correct': False,
        'password_error': error_messages['password_general'],
        'referral_code': '8hTb2pRqK',
        'referral_code_message': error_messages['referral_incorrect_link_format'],
        'click_checkbox': False,
        'expected_checkbox_status': 'Off',
        'submit_form': False,
        'is_submit_button_inactive': True,
     },
     {
        'test_id': 4,
        'username': '4headers',
        'username_error': error_messages['username'],
        'email': 'fafghhj@gmail.com',
        'email_error': '',
        'password': 'adgdgadsfdfhjk',
        'is_password_correct': False,
        'password_error': error_messages['password_general'],
        'referral_code': 'wwwwww',
        'referral_code_message': error_messages['correct_referral_code_message'],
        'click_checkbox': False,
        'expected_checkbox_status': 'Unchecked',
        'submit_form': True,
        'is_submit_button_inactive': False,
     },
     {
        'test_id': 5,
        'username': 'Header4)_(',
        'username_error': error_messages['username'],
        'email': 'adfsafd',
        'email_error': error_messages['email'],
        'password': 'headers4',
        'is_password_correct': False,
        'password_error': error_messages['password_general'],
        'referral_code': 'wwww',
        'referral_code_message': error_messages['correct_referral_code_message'],
        'click_checkbox': False,
        'expected_checkbox_status': 'Unchecked',
        'submit_form': True,
        'is_submit_button_inactive': False,
     },
]

