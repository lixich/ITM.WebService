from flask import Blueprint, jsonify, abort, request
from db import update_record, create_record

app_requirement = Blueprint('requirement', __name__)
requirement_set = [
	# Проект "Сумма"
    {
        "Id": 1,
        "Name": 'Сумма А и В',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": True,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": None
    },
    {
        "Id": 2,
        "Name": 'Ввод a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 1
    },
    {
        "Id": 3,
        "Name": 'Ввод целых числе a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 8,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 2
    },
    {
        "Id": 4,
        "Name": 'Ввод вещественных чисел a, b',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 1,
        "StakeholderId": 1,
        "MainRequirementId": 2
    },
	# Проект "Уравнение"
    {
        "Id": 5,
        "Name": 'Вычисление квадратного уравнения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": True,
        "IsFound": True,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 6,
        "Name": 'Ввод a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": True,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 7,
        "Name": 'Ввод целых чисел a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 6
    },
    {
        "Id": 8,
        "Name": 'Ввод вещественных чисел a, b, c',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 7
    },
    {
        "Id": 9,
        "Name": 'Решение квадратного уравнения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 10,
        "Name": 'Решение квадратного неравенства',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 4,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 5
    },
    {
        "Id": 11,
        "Name": 'Проверка решения пользователя',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 12,
        "Name": 'Таймер (время на решение)',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 13,
        "Name": '10 мин',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 14,
        "Name": '20 мин',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 15,
        "Name": 'Отключение таймера',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 0,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 12
    },
    {
        "Id": 16,
        "Name": 'Отображение ответа',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 17,
        "Name": 'С помощью графика',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 18,
        "Name": 'С помощью формулы',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 19,
        "Name": 'Голосовое сообщение',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 16
    },
    {
        "Id": 20,
        "Name": 'Отображение решения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 2,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 11
    },
    {
        "Id": 21,
        "Name": 'Статистика пользователей',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": None
    },
    {
        "Id": 22,
        "Name": 'Среднее время решения',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 21
    },
    {
        "Id": 23,
        "Name": 'Кол-во решенных примеров',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 0,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 2,
        "MainRequirementId": 21
    },
    {
        "Id": 24,
        "Name": 'Процент решенных примеров',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 2,
        "StakeholderId": 3,
        "MainRequirementId": 21
    },
	# Проект "Терминал"
    {
        "Id": 25,
        "Name": 'Сохранение информации обо всех проданных билетах в течение дня',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 26,
        "Name": 'Локальная база данных в устройстве',
        "MinimumSkill": 35,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 27,
        "Name": 'Сохранение номера билета',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 7,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 28,
        "Name": 'Сохранение серии билета',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 29,
        "Name": 'Сохранение даты и времени продажи билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 30,
        "Name": 'Сохранение номера маршрута',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 4,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 31,
        "Name": 'Сохранение идентификационного номера кондуктора',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 25
    },
    {
        "Id": 32,
        "Name": 'Передача данных из устройства в базу данных заказчика',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 33,
        "Name": 'Соединение с базой данных заказчика',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 34,
        "Name": 'Передача номера билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 35,
        "Name": 'Передача серии билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 36,
        "Name": 'Передача даты и времени продажи билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 37,
        "Name": 'Передача номера маршрута',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 38,
        "Name": 'Передача идентификационного номера кондуктора',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 32
    },
    {
        "Id": 39,
        "Name": 'Печать билета',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 40,
        "Name": 'Печать названия организации',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 41,
        "Name": 'Печать ИНН',
        "MinimumSkill": 80,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 42,
        "Name": 'Печать номера билета',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 43,
        "Name": 'Печать серии билета',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 44,
        "Name": 'Печать даты и времени продажи билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 45,
        "Name": 'Печать цены билета',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 2,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 46,
        "Name": 'Печать номера маршрута',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 47,
        "Name": 'Печать идентификационного номера кондуктора',
        "MinimumSkill": 65,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 8,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 48,
        "Name": 'Печать типа транспорта',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 49,
        "Name": 'Печать «Автобус»',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 48
    },
    {
        "Id": 50,
        "Name": 'Печать «Троллейбус»',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 48
    },
    {
        "Id": 51,
        "Name": 'Печать «Трамвай»',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 48
    },
    {
        "Id": 52,
        "Name": 'Печать предупреждения «Сохраняйте билет до конца поездки»',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 53,
        "Name": 'Печать рекламы на обратной стороне',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 39
    },
    {
        "Id": 54,
        "Name": 'Внесение информации о маршруте на день',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 7,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 55,
        "Name": 'Номер маршрута',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 7,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 54
    },
    {
        "Id": 56,
        "Name": 'Идентификационный номер кондуктора',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 54
    },
    {
        "Id": 57,
        "Name": 'Инициализация устройства',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 54
    },
    {
        "Id": 58,
        "Name": 'Обнуление номера первого проданного билета (счетчик смены)',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 57
    },
    {
        "Id": 59,
        "Name": 'Проверка информации',
        "MinimumSkill": 75,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 57
    },
    {
        "Id": 60,
        "Name": 'Картинка с рекламой',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 4,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 54
    },
    {
        "Id": 61,
        "Name": 'Уведомления',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 62,
        "Name": 'Уведомление о необходимости передачи информации из устройства в базу данных заказчика в конце дня',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 7,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 61
    },
    {
        "Id": 63,
        "Name": 'Уведомление о переполнении базы данных устройства и необходимости вызова работника сервисной службы для очистки базы данных устройства',
        "MinimumSkill": 70,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": 61
    },
    {
        "Id": 64,
        "Name": 'Возможность считывания информации с рабочей карты кондуктора об идентификации пользователя при запросе продажи билета через сканер устройства',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 4,
        "MainRequirementId": None
    },
    {
        "Id": 65,
        "Name": 'Отображение информации на экране устройства',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": None
    },
    {
        "Id": 66,
        "Name": 'Отображение текущих даты и времени',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 65
    },
    {
        "Id": 67,
        "Name": 'Отображение количества билетов, которые будут напечатаны',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 65
    },
    {
        "Id": 68,
        "Name": 'Отображение текущего состояния устройства',
        "MinimumSkill": 55,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 2,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 65
    },
    {
        "Id": 69,
        "Name": 'Готово',
        "MinimumSkill": 10,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 68
    },
    {
        "Id": 70,
        "Name": 'Оплата билета',
        "MinimumSkill": 10,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 68
    },
    {
        "Id": 71,
        "Name": 'Печать билета',
        "MinimumSkill": 10,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 68
    },
    {
        "Id": 72,
        "Name": 'Билет напечатан',
        "MinimumSkill": 10,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 5,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 68
    },
    {
        "Id": 73,
        "Name": 'Автоматическое вычисление сдачи',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 65
    },
    {
        "Id": 74,
        "Name": 'Ввод количества билетов',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 73
    },
    {
        "Id": 75,
        "Name": 'Ввод полученной суммы',
        "MinimumSkill": 60,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": 73
    },
    {
        "Id": 76,
        "Name": 'Обеспечение безопасности (при краже устройства)',
        "MinimumSkill": 80,
        "DetectionIterationNumber": 2,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 5,
        "MainRequirementId": None
    },
    {
        "Id": 77,
        "Name": 'Отображение информации на экране устройства)',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": None
    },
    {
        "Id": 78,
        "Name": 'Отображение уровня заряда устройства (батарейка с тремя секциями)',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 77
    },
    {
        "Id": 79,
        "Name": 'Отображение признака, что устройство заряжается (батарейка с молнией)',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 77
    },
    {
        "Id": 80,
        "Name": 'Отображение признака, что в устройстве кончается бумага',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 77
    },
    {
        "Id": 81,
        "Name": 'Отображение признака, что в устройстве кончается чернила',
        "MinimumSkill": 35,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 77
    },
    {
        "Id": 82,
        "Name": 'Изменение значений внутри устройства',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 9,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": None
    },
    {
        "Id": 83,
        "Name": 'Цена билета',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 6,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 82
    },
    {
        "Id": 84,
        "Name": 'Информационные сообщения (поздравления, реклама…)',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 3,
        "ImportantIndex": 1,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 82
    },
    {
        "Id": 85,
        "Name": 'Подача питания',
        "MinimumSkill": 50,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": None
    },
    {
        "Id": 86,
        "Name": 'Включить устройство',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 85
    },
    {
        "Id": 87,
        "Name": 'Выключить устройство',
        "MinimumSkill": 30,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 85
    },
    {
        "Id": 88,
        "Name": 'Перезагрузить устройство',
        "MinimumSkill": 40,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 6,
        "MainRequirementId": 85
    },
    {
        "Id": 89,
        "Name": 'Возможность скачивания фискальных данных',
        "MinimumSkill": 0,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 8,
        "IsFound": True,
        "ContentId": 3,
        "StakeholderId": 7,
        "MainRequirementId": None
    },
    {
        "Id": 90,
        "Name": 'Суммовые показатели',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 7,
        "MainRequirementId": 89
    },
    {
        "Id": 91,
        "Name": 'Дата и время',
        "MinimumSkill": 20,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 7,
        "MainRequirementId": 89
    },
    {
        "Id": 92,
        "Name": 'Защита фискальных данных',
        "MinimumSkill": 80,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 7,
        "MainRequirementId": None
    },
    {
        "Id": 93,
        "Name": 'Очистка базы данных устройства посредством пароля',
        "MinimumSkill": 80,
        "DetectionIterationNumber": 1,
        "ImportantIndex": 10,
        "IsFound": False,
        "ContentId": 3,
        "StakeholderId": 7,
        "MainRequirementId": 92
    }
]
requirement_class = {
    "Id": int,
    "Name": str,
    "MinimumSkill": int,
    "DetectionIterationNumber": int,
    "ImportantIndex": int,
    "IsFound": bool,
    "ContentId": int,
    "StakeholderId": int,
    "MainRequirementId": int
}

@app_requirement.route('/', methods=['GET'])
def get_requirement_set():
    return jsonify(requirement_set)

@app_requirement.route('/', methods=['POST'])
def create_requirement():
    if not request.json:
        abort(400)
    requirement = { 'Id': requirement_set[-1]['Id'] + 1 if len(requirement_set) else 1 }
    create_record(requirement_class, request, requirement)
    requirement_set.append(requirement)
    return jsonify(requirement), 201

@app_requirement.route('/<int:requirement_id>', methods = ['GET'])
def get_requirement(requirement_id):
    requirements = list(filter(lambda t: t['Id'] == requirement_id, requirement_set))
    if len(requirements) == 0:
        abort(404)
    return jsonify(requirements[0])

@app_requirement.route('/<int:requirement_id>', methods=['PUT'])
def update_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0 or not request.json:
        abort(404)
    requirement = requirements[0]
    update_record(requirement_class, request, requirement)
    return jsonify( requirement)

@app_requirement.route('/<int:requirement_id>', methods=['DELETE'])
def delete_requirement(requirement_id):
    requirements = [requirement for requirement in requirement_set if requirement['Id'] == requirement_id]
    if len(requirements) == 0:
        abort(404)
    requirement_set.remove(requirements[0])
    return jsonify({'Result': True})
