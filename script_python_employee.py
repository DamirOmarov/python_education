# Отчет по сотрудникам
import json
import pandas as pd

# Чтение данных из test_1.json
try:
    with open('test_1.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Файл не найден. Проверьте имя и местоположение файла.")
    exit()
except json.JSONDecodeError:
    print("Ошибка декодирования JSON. Проверьте структуру файла.")
    exit()

# Сбор названий УК
ksk_name = [
    obj.get("employee_positions", {}).get("ksk", {}).get("name")
    for obj in data
    if not obj.get("employee_workers")  # Если список пуст
]

# Удаление None значений, если есть
ksk_name = [name for name in ksk_name if name]

# Создание DataFrame
df = pd.DataFrame({'УК/ОСИ': ksk_name})

# Запись результата в Excel
output_file = 'employee.xlsx'
df.to_excel(output_file, index=False, engine='openpyxl')
print(f"Результаты сохранены в файл: {output_file}")
