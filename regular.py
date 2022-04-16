from pprint import pprint
import re
import csv
with open("C:\Projects\\regular\phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

def reg_cont():

  dict_cont = {}
  for contact in contacts_list:    
    cont = ' '.join(contact[0:2])
    cont1 = list(cont.split())
    names = f'{cont1[0]} {cont1[1]}'
    number = contact[5]
    pattern = re.compile(r"(\+7|8)\D*([\d]{3})\D{0,2}(\d{3})\D?([\d]{2})\D?([\d]{2})\s?\(?(доб\.[\s]?[\d]{4})?\)?")
    new_number = pattern.sub(r"+7(\2)\3-\4-\5 \6", number)
    contact[5] = new_number
    if len(cont1) == 2:
            cont1.append('')
    surname = [cont1[2]]
    cont_info = [*surname, *contact[3::]]
    if names not in dict_cont:
      dict_cont[names] = cont_info
    else:
      i = 0
      while i < 5:
        dict_info = dict_cont[names]
        if len(dict_info[i]) == 0:
          dict_info[i] = cont_info[i]
        i += 1

      dict_cont[names] = dict_info
  cont_list = list(dict_cont.items())

  full_list = []

  for contacts in cont_list:
    fin_cont = list(contacts)
    name = fin_cont[0]
    final_cont = [*name.split(), *fin_cont[1]]
    full_list.append(final_cont)

  return full_list

pprint(reg_cont())

with open("C:\Projects\\regular\phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(reg_cont())