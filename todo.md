# ЗАМЕТКИ

## ПРОВЕРКИ:
1. Листы
  - Дата
  - Формат
  - Номера листов
  - Все ли листы попали в ведомость

2. Общие данные
  - Вычитка общих данных

3. Помещения
 - У всех ли внутриквартирных помещений проставлен параметр Номер квартиры
 - У всех ли помещений высчитан коэффициент площади
 - У всех ли помещений выставлено значение *П_Тип помещения*
 - Получается ли сумма помещений в маркере квартиры
   - Получить значение маркера(?)
   - Если сумма не сошлась, то **сигнализировать** об этом
 -
4. Двери
 - Соответствует ли открывание на плане открыванию в ведомости
 - Все ли двери учтен- [ ] ы  (Подсветить на плане)
 - Название, обозначение в ведомости
 - Количество штук на этаже в ведомости
---
## Правила именования видов
Разделитель - _
1. Сегмент 1 - Номер листа или Назначение или оба (Э), (П), (З) (К)
2. Сегмент 2 - Тип вида (План)
3. Сегмент 3 - Уровень, имя помещения, фрагмент
4. Сегмент 4 - Функция, дисциплина, аббревиатура

#### Назначение
- (Э) - рабочий вид, используемый для построения модели, непечатаемый
- (П) - вид для экспорта в CAD
- (К) - вид, используемый для координации между дисциплинами
- (ПР) - презентационный
- (Персп.) - перспективный вид

#### Типы видов
- ПЛН (план этажа)
- ПОТ (план потолка)
- 3D (3д вид)
- ФСД (фасад)
- ФР (фрагмент)
- ИН (интерьер)
- РАЗ (разрез)
- ЗОН (план зонирования)

### ПЛАНЫ ЭТАЖЕЙ
- Пример: ```А04_ПЛН_01``` _(План этажа 1 на листе А04)_
- Пример: ```(Э)_ПЛН_01``` _(План этажа 1 рабочий)_

### ФРАГМЕНТЫ
- Пример: ```А12-1_01_ФР_Помещение 1.25```
- Пример: ```А12-2_01_ФР_Вестибюль 2```

### ПЛАНЫ ПОТОЛКОВ
- Пример: ```А5-1_ПОТ_01```
- Пример: ```А5-1_ПОТ_Вестибюль 1```

### 3Д ВИДЫ
- Пример: ```3D_COORD```
- Пример: ```3D_Иванов```
- Пример: ```(Персп.)_Квартира 5```

### ФАСАДЫ
- Пример: ```(Э)_ФСД_1-12```
- Пример: ```А13_ФСД_1-12```

### РАЗРЕЗЫ
- Пример: ```А08_РАЗ_Ось А```
- Пример: ```А08_РАЗ_1-1```

### РАЗВЕРТКА ИНТЕРЬЕРА
- Пример: ```А08-1_ИН_Кухня_Север```

### УЗЛЫ
- Пример: ```А9-1_Примыкание облицовки```

### ЧЕРТЕЖНЫЙ ВИД
- Пример: ```А9-1_Примыкание облицовки```

### СХЕМЫ ЗОНИРОВАНИЯ
- Пример: ```А9_ЗОН_01```

---
## ПЛОЩАДИ
- Определить контур помещения
- В зависимости от параметра *Толщина отделки*, сдвигаем контур помещения внутрь
  - Реализовать проверки на случай П-образных маленьких закутков
- Вычисляем площадь полученного контура с учетом коэффициента
- Записываем полученное значение в параметр *П_Площадь*
- Ставим маркер соответствующий
- ...
