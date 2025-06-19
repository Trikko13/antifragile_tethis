def stop_test():
    score = 0
    while score > 0:
        debt = input("У вас есть непогашенные кредиты, карты, займы? [yes/no]")
        if debt.lower() in ['yes', 'да']:
            score -= 1
            print('Учтено,есть')
        else:
            score += 1
            print('Учтено,их нет')
        savings = input("У вас есть подушка? [yes/no]")
        if savings.lower() in ['yes', 'да']:
            score += 1
            savings_amount = int(input("Какая, в месяцах жизни с учетом трат? [число в мес.]"))
            if savings_amount >= 2:
                score +=1
            else:
                score -=1
        mental_reward = input("Поощрил ли ты себя как источник дохода?[отпуск,телефон,монитор,кресло или другое?]")
        if mental_reward.lower() in ["отпуск","телефон","монитор"]:
            score += 2
        elif mental_reward.lower() in ["другое"]:
            mr_price = int(input("цена поощрения в руб"))
            if mr_price < 10000:
                score -= 0
            else:
                score += 1
        else:
            score -= 1
    return(f"проверка на стоп действие завершена, ваш балл {score}")
print(stop_test)

