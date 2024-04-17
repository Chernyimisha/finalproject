import json


def add_set_nm_id(detail):
    result = {11111111, 22222222, 33333333, 44444444, 55555555, 66666666}
    for line in detail:
        nm_id = line.nm_id
        if nm_id != 0 and nm_id is not result:
            result.add(nm_id)
    return result


def aggregation_by_item(detail, set_nm_id):
    result = []
    other_nm_id = {'Семена': 11111111,
                   'Блузки': 22222222,
                   'Рубашки': 33333333,
                   'Брюки': 44444444}

    for nm_id in set_nm_id:
        sa_name = ''
        count = 0
        sales = 0
        commission = 0
        logistic = 0
        for line in detail:
            subject_name = line.subject_name
            if subject_name not in other_nm_id and line.nm_id == nm_id:
                if line.doc_type_name.lower() == 'продажа':
                    count += line.quantity
                    sales += line.retail_amount
                    commission += (line.retail_amount - line.ppvz_for_pay)

                if line.doc_type_name.lower() == 'возврат':
                    count -= line.quantity
                    sales -= line.retail_amount
                    commission -= (line.retail_amount - line.ppvz_for_pay)

                if line.delivery_rub is not None:
                    logistic += line.delivery_rub
                sa_name = line.sa_name

            else:
                if subject_name in other_nm_id and other_nm_id[subject_name] == nm_id:
                    if line.doc_type_name.lower() == 'продажа':
                        count += line.quantity
                        sales += line.retail_amount
                        commission += (line.retail_amount - line.ppvz_for_pay)

                    if line.doc_type_name.lower() == 'возврат':
                        count -= line.quantity
                        sales -= line.retail_amount
                        commission -= (line.retail_amount - line.ppvz_for_pay)

                    if line.delivery_rub is not None:
                        logistic += line.delivery_rub
                    sa_name = subject_name

        if sa_name != '':
            result.append(
                {'nm_id': nm_id, 'article_wb': sa_name, 'count': round(count, 2), 'sales': round(sales, 2),
                 'commission': round(commission, 2), 'logistic': round(logistic, 2)})

    return result


def gluing_data(data_base: list, report: list):
    for d in report:
        data_base.append(d)
    return data_base


def write_report_json(report: list):
    with open('report_DetailByPeriod_data.txt', 'r') as file:
        temp_list = file.read()
    if not temp_list:
        with open('report_DetailByPeriod_data.txt', 'w') as file:
            json.dump(report, file, ensure_ascii=False)
    else:
        with open('report_DetailByPeriod_data.txt', 'r') as file:
            temp_list = json.load(file)
        data_base = gluing_data(temp_list, report)
        with open('report_DetailByPeriod_data.txt', 'w') as file:
            json.dump(data_base, file, ensure_ascii=False)


def control_method(report):
    count_product = 0
    sales = 0
    comiss = 0
    logistic = 0
    for item in report:
        print(item)
        count_product += item.get('count')
        sales += item.get('sales')
        comiss += item.get('commission')
        logistic += item.get('logistic')
    print(f"\nколичество = {count_product}, продажи = {round(sales, 2)}, комиссия = {round(comiss, 2)}, логистика = {round(logistic, 2)}")


# write_report_json(result)

