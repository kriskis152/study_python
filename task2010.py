def validate_user(name, age, email):
    """
    Проверяет корректность данных пользователя

    Args:
        name: имя пользователя
        age: возраст пользователя
        email: email  пользователя
    Returns:
        Словарь с результатами проверки:
        - is_valid: булево значение, прошла ли проверка 
        - errors; список ошибок (пустой, если проверка пройдена)
    """
    errors = []
    if not name or name.strip() == "":
        errors.append("Имя не может быть пустым")
    if not (0 <= age <= 120):
        errors.append("Email должен быть от 0 до 120")
    if '@' not in email:
        errors.append("Email должен содержать @")
    return {
        'is_valid': len(errors) == 0,
        'errors': errors
    }


if __name__ == "__main__":
    print("=== Валидатор данных пользователя===\n")

    print("Тест 1 (неправельные данные): ")
    result1 = validate_user("", 150, "invalid")
    print(F"is_valid: {result1['is_valid']}")
    print("Ошибки: ", result1['errors'])

    print("Тест 2 (правельные данные): ")
    result2 = validate_user("Иван", 25, "test@email.com")
    print(F"is_valid: {result2['is_valid']}")
    print("Ошибки: ", result2['errors'])

    print("Тест 3 (правельные данные): ")
    result3 = validate_user(" ", 25, "test@email.com")
    print(F"is_valid: {result3['is_valid']}")
    print("Ошибки: ", result3['errors'])

    