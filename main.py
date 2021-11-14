


class text_editor:
    def format_number(C_list):
        number_patern = r"\+*(7|8)??\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(доб.\s*\d+)*\)*"
        number_repl = r'+7(\2)\3-\4-\5 \6'
        new_number_list = []
        for i in C_list:
            i_str = ','.join(i)
            format_i = re.sub(number_patern, number_repl, i_str)
            i_list = format_i.split(',')
            new_number_list.append(i_list)
        return (new_number_list)

    def format_name(C_list_2):
        name_patern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
        name_repl = r'\1\3\10 \4\6\9 \7\8'
        new_number_list = []
        for i in C_list_2:
            i_str = ','.join(i)
            format_i = re.sub(name_patern, name_repl, i_str)
            i_list = format_i.split(',')
            new_number_list.append(i_list)
        return (new_number_list)

    def duplicates(C_list_3):
        for i in C_list_3:
            for k in C_list_3:
                if i[0] == k[0] and i[1] == k[1] and k is not i:
                    if i[2] == '':
                        i[2] = k[2]
                    if i[3] == '':
                        i[3] = k[3]
                    if i[4] == '':
                        i[4] = k[4]
                    if i[5] == '':
                        i[5] = k[5]
                    if i[6] == '':
                        i[6] = k[6]
        new_number_list = []
        for j in C_list_3:
            if j not in new_number_list:
                new_number_list.append(j)
        return new_number_list


if __name__ == "__main__":
    import re
    import csv

    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    text = text_editor
    change_numbers = text.format_number(contacts_list)
    change_name = text.format_name(change_numbers)
    del_duplicates = text.duplicates(change_name)

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(del_duplicates)