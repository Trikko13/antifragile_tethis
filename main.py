import math
'''
def evaluate_financial_health():
    score = 0
    score_recs = '3-5 - для начала консервативного инвестирования, 5-7 - средне-агрессивного, 10+ - позволительно все'
    monthly_salary = 140
    monthly_expenses = 67 # Текущая на 28.06.2025 - 67 к руб. (с мая 24 по июнь 25, минус крипту и подушка (337к-2025 + 610-2025 =945/14-67к)
    show_stats = (
        f"Твоя ЗП:{monthly_salary} руб., "
        f"Твои расходы по HM по 14мес сводке: {monthly_expenses} руб./мес, "
        f"Текущие очки: {score}, "
        f"Описание очков антихрупкости: {score_recs}"
    )

    debt = input("У вас есть непогашенные кредиты, карты, займы? [yes/no/show_stats]")

    if debt.lower() in ['yes', 'нуы']:
        print('Извините, вам нельзя сберегать. Разберитесь с долгами и приходите')
        return 0

    elif debt.lower() == 'show_stats':
        print(show_stats)
        return 0

    else:
        score += 1
        print('Учтено,долгов нет')
    # Блок про будущие расходы
    future_big_outflows,fbo_month = map(
        int,
        input(
            "Какая Планируются ближайшие большие покупки/расходы и в пределах каких месяцев? "
            "[отпуск, техника, подарки от 10к в пределах 3 мес (прим отпуск и техника в пределах 6 мес: 140, 6) ]"
        ).split()
    )
    expenses_with_fbo = monthly_expenses + future_big_outflows / fbo_month
    print(f"Учитывая расходы: {future_big_outflows} тыс., через {fbo_month} мес., {math.ceil(expenses_with_fbo)}")

    # Блок про подушку фиата
    savings = input(f"У вас есть подушка,учитывая эту цифру в данный момент: {int(math.ceil(expenses_with_fbo))} (идея в том, чтобы понять нагрузку целей на бюджет?) [yes/no]")
    if savings.lower() in ['yes', 'нуы']:
        score += 1
        savings_amount = int(input(f"Какая, в месяцах жизни с учетом трат?(желательно не менее половины срока будущей цели: {fbo_month/2} мес. или {int(fbo_month/2*expenses_with_fbo)} мес. [число в мес.]"))
        if savings_amount == fbo_month/2:
            score += 1
        elif savings_amount > fbo_month/2:
            score += 2
        else:
            score -= 1

    # Блок про поощрение
    mental_reward = input("Поощрил ли ты себя как источник дохода в последние 1-5 мес?[отпуск,телефон,монитор,кресло или другое?/ no - если нет]")
    if mental_reward.lower() in ["отпуск","телефон","монитор", "кресло", '1', '2', '3', '4']:
        score += 2
    elif mental_reward.lower() in ["другое",'lheujt']:
        mr_price = int(input("цена поощрения в тыс. руб"))
        if mr_price < 10:
            score -= 1
        else:
            score += 1
    else:
        score -= 1

    print(f"Проверка на стоп действие завершена, ваш балл {score}. (Минимально возможный балл за блок - 1, Максимально возможный балл за блок - 6)")
    return score


financial_health_score = evaluate_financial_health()

print (f"Финальный балл stop_test :{financial_health_score}")
'''

def evaluate_psycho_health():
# Идея данного блока в том, чтобы выдерживать заранее обговоренный баланс риска и атаки в каждую единицу времени при совершении сделки.
    psycho_score = 0
    sources_action_dict = {
        'ру': -2, # инфлы кек
        'твиттер': -1, # мой lists
        'Linn': 1, # пост от Линн в журнале
        'Мои': 2 # книги и тезисы
    }

# Сначала находим ключ по индексу: keys[idx], затем достаём значение из словаря d — и печатаем его.
# Пример:
# Ввёл 2 → keys[2] = 'Linn' → d['Linn'] = +1

    keys_list = list(sources_action_dict)
    for i, k in enumerate(keys_list):
        print(f"{i}:{k}")

    try:
        idx = int(input('Номер источника:'))
        print(f"Психо-оценка: {sources_action_dict[keys_list[idx]]}")
        psycho_score += sources_action_dict[keys_list[idx]]
    except:
        print('Ошибка ввода')

    fomo_index =  int(input("Уровень фомо по 5 бальной шкале:",
                            "1 - Идея старая и тезис  простой",
                            '2 - Идея старая, но цены хорошие'
                            '3 - Новый тезис, еще не поздно'
                            '4 - Актуальный тезис - нужно пробовать'
                            '5 - догоняем поезд'))
    psycho_score += fomo_index
evaluate_psycho_health()


