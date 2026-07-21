from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Cookie пользователя 1
    user1_cookies = [
        {
            'name': 'sessionid',
            'value': 'MWU0YmIwMzUtZWJkZC00YmQ5LWI1MjQtYWUxODk3NGMzMzE3'
        },
        {
            'name': 'csrftoken',
            'value': 'b6dc73da-47c5-4e45-ae9e-017e1b6ca22a'
        },
    ]

    # Cookie пользователя 2
    user2_cookies = [
        {
            'name': 'sessionid',
            'value': 'NjQyYWEzYWEtYTVlOS00YzFlLWFmNDEtZTllMjIzOTYzNTBh'
        },
        {
            'name': 'csrftoken',
            'value': 'ca5c0b9d-9d95-496c-9c67-2bcca9d561ef'
        },
        # Добавьте другие необходимые cookie
    ]

    # Откройте страницу https://gitflic.ru/
    driver.get('https://gitflic.ru/')

    # Установите cookie пользователя 1
    for cookie in user1_cookies:
        driver.add_cookie(cookie)

    # Обновите страницу
    driver.refresh()

    # Перейдите на страницу пользователя 1
    user1_url = 'https://gitflic.ru/user/counsel'
    driver.get(user1_url)

    # Сохраните текущий URL пользователя 1
    url_user1 = driver.current_url

    # Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # Установите cookie пользователя 2
    for cookie in user2_cookies:
        driver.add_cookie(cookie)

    # Обновите страницу
    driver.refresh()

    # Перейдите на страницу пользователя 2
    user2_url = 'https://gitflic.ru/user/nay_lexicon1a'
    driver.get(user2_url)

    # Сохраните текущий URL пользователя 2
    url_user2 = driver.current_url

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_user1 != url_user2, (
        f'URL пользователей должны различаться, '
        f'но получены одинаковые: {url_user1}'
        )

    driver.quit()
