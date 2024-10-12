# Задание 3.
# Каждый год ваша компания предоставляет различным государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные. Используя механизм декораторов, решите вопрос
# отчетности для организаций.


def format_txt(func):
    def wrapper(*args, **kwargs):
        with open('Финансовый отчет для ФСН.txt', 'w', encoding='utf') as f:
            f.write(generate_report())

    return wrapper()


def format_JSON(func):
    def wrapper(*args, **kwargs):
        with open('Финансовый отчет для бухгалтерии.JSON', 'w', encoding='utf') as f:
            f.write(generate_report())

    return wrapper()


@format_txt
@format_JSON
def generate_report():
    return f'Финансовый отчет'


print(generate_report())
