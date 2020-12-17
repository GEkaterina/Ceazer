file1 = open("chapter.txt", "r", encoding="utf8")
chapter = list(file1.read().lower())
file1.close()

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
a=0


'''
Шифрование одной главы "Война и мир"
'''
encrypted = ''
key = int(input("Введите сдвиг от 1 до 25:  "))
for i in chapter:
    if i in alphabet:
        '''if i.isupper():
            encrypted += alphabet[(alphabet.index(i) + key) % len(alphabet)].upper()
        else:'''
        encrypted += alphabet[(alphabet.index(i) + key) % len(alphabet)]
        a+=1
    else:
        encrypted += i
        a+=1

encrypted = ''.join(encrypted)
file2 = open("encrypt.txt", "w", encoding="utf8")
file2.write(encrypted)
print(encrypted)
file2.close()



'''
Таблица частот для всей книги "Война и мир"
'''
full_table={'а':0,'б':0,'в':0,'г':0,'д':0,'е':0,'ё':0,'ж':0,'з':0,'и':0,'й':0,'к':0,'л':0,'м':0,
            'н':0,'о':0,'п':0,'р':0,'с':0,'т':0,'у':0,'ф':0,'х':0,'ц':0,'ч':0,'ш':0,'щ':0,'ъ':0,
            'ы':0,'ь':0,'э':0,'ю':0,'я':0}
file3 = open("voyna-i-mir.txt", "r", encoding="utf8")
book = list(file3.read().lower())
file3.close()

def similar(book,full_table):
    for i in full_table.keys():
        count=0
        for word in book:
            if i==word:
                count+=1
                full_table[word]=count
    return(full_table)

table_full = similar(book, full_table) # таблиц частот по всей книге



'''
Таблица частот по зашифрованной главе
'''
tom_table={'а':0,'б':0,'в':0,'г':0,'д':0,'е':0,'ё':0,'ж':0,'з':0,'и':0,'й':0,'к':0,'л':0,'м':0,'н':0,'о':0,'п':0,'р':0,
           'с':0,'т':0,'у':0,'ф':0,'х':0,'ц':0,'ч':0,'ш':0,'щ':0,'ъ':0,'ы':0,'ь':0,'э':0,'ю':0,'я':0}
file2 = open("encrypt.txt", "r", encoding="utf8")
encrypted = list(file2.read().lower())
file2.close()

table_tom = similar(encrypted, tom_table) # таблица чистот по зашифрованной главе

print('\n',"Тaблица частот всей книги:",table_full,'\n\n',"Tаблица частот зашифрованной главы",table_tom)



'''
Сортировка зашифрованной главы и всей книги Война и мир
'''

print('\n',"Отсортированный список всей книги Война и мир")
list_file3 = list(table_full.items())
list_file3.sort(key=lambda i: i[1])
for i in list_file3:
    print(i[0], ':', i[1])


print('\n',"Отсортированный список зашифрованной главы")
list_file2 = list(table_tom.items())
list_file2.sort(key=lambda i: i[1])
for i in list_file2:
    print(i[0], ':', i[1])

list1=[]
list2=[]
for i in range(0, len(alphabet)):
    list1.append(list_file3[i][0])
    list2.append(list_file2[i][0])



encrypted = ''.join(encrypted)
list_encrypted=list(encrypted)
dencrypted=''
for n in list(encrypted):
    if n in alphabet:
            l=list1[list2.index(n)]
            dencrypted = dencrypted + l
    else:
        dencrypted = dencrypted + n
print('\n', "ОБРАТНАЯ ЗАМЕНА ")
print(dencrypted)
