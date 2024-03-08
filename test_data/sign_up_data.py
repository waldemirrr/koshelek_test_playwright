sign_up_data = [
     {
         # Имя пользователя
         'username': '',
         # Ожидаемая ошибка в валидации имени пользователя
         'username_error': ' Поле не заполнено ',
         # Email
         'email': '',
         # Ожидаемая ошибка в валидации email
         'email_error': ' Поле не заполнено ',
         # Пароль
         'password': '',
         # Проходит ли пароль валидацию? True - да, False - нет
         'is_password_correct': False,
         # Ожидаемая ошибка в валидации пароля (Если не прошёл валидацию)
         'password_error': ' Поле не заполнено ',
         # Реферальный код
         'referral_code': '',
         # Ожидаемое сообщение в валидации реферального кода
         'referral_code_message': ' Реферальный код дает скидку ',
         # Кликнуть чекбокс? True - да, False - нет
         'click_checkbox': False,
         # Ожидаемый статус чекбокса. Unchecked - ошибка при отправке формы, Checked - Чекнут, Off - не чекнут
         'expected_checkbox_status': 'Unchecked',
         # Отправлять ли форму? True - да, False - нет
         'submit_form': True,
         # Неактивна ли кнопка отправки формы? True - неактивна False - активна
         'is_submit_button_inactive': False
     },
     {
        'username': 'walder13556',
        'username_error': '',
        'email': 'walders@gmail.com',
        'email_error': '',
        'password': 'Passwordio13576',
        'is_password_correct': True,
        'password_error': '',
        'referral_code': 'www.com',
        'referral_code_message': ' Реферальный код дает скидку ',
        'click_checkbox': True,
        'expected_checkbox_status': 'Checked',
        'submit_form': True,
        'is_submit_button_inactive': False
     },
]

