

PATH_FILE_ALTIUM = "/Users/lida/Downloads/netlist_Altium.net"
PATH_FILE_CADENCE = "/Users/lida/Downloads/netlist_Cadence.txt"


list_altium = set()
list_altium_current = []
list_cadence = set()


class OneElement:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties


    def __eq__(self, other):
        if len(self.properties) != len(other.properties):
            return False
        for elem in other.properties:
            if elem not in self.properties:
                return False
        return self.name == other.name

    def __hash__(self):
        a = 0
        for elem in self.properties:
            a += hash(elem)
        return hash(self.name) ^ a


def read_altium():
    f = open(PATH_FILE_ALTIUM)

    while True:
        line = f.readline()
        line = line.replace('\n', '')
        
        if not line:
            break

        if line == '(':
            a = ""
            while  a != ')':
                a = f.readline()
                a = a.replace('\n', '')
                a = a.replace('-', '.')
                if a != ')' and a != '(':
                    list_altium_current.append(a)
            #list_altium.append(list_altium_current.copy())
            list_altium.add(OneElement(list_altium_current[0], list_altium_current[1:]))
            list_altium_current.clear()
    f.close()

def read_cadence():
    f = open(PATH_FILE_CADENCE)

    while True:
        b = f.readline()

        if not b:
            break

        list_cadence_current = b.split(' ')
        if ',' in b:
            tmp = f.readline()
            detect_comma = False
            while ',' in tmp:
                detect_comma = True
                tmp = tmp.split(' ')
                for elem in tmp:
                    list_cadence_current.append(elem)
                while '' in list_cadence_current:
                    list_cadence_current.remove('')
                tmp = f.readline()
            if detect_comma:
                tmp = tmp.split(' ')
                for elem in tmp:
                    list_cadence_current.append(elem)
                while '' in list_cadence_current:
                    list_cadence_current.remove('')
        while ';' in list_cadence_current:
            list_cadence_current.remove(';')
        while '\n' in list_cadence_current:
            list_cadence_current.remove('\n')
        while ',\n' in list_cadence_current:
            list_cadence_current.remove(',\n')
        #list_cadence.append(list_cadence_current.copy())
        list_cadence.add(OneElement(list_cadence_current[0], list_cadence_current[1:]))


    f.close()


if __name__ == '__main__':
    
    read_altium()

    read_cadence()

    file = open('answer.txt', 'w+')

    answer = list_altium ^ list_cadence

    answer_set = set()

    ans = answer.copy()

    for elem in answer:


        flag1 = False
        flag2 = False

    
        for elem_list_altium in list_altium: 
            if len(elem_list_altium.properties) == len(elem.properties): 
                for one_prop_elem in elem.properties: 
                    if one_prop_elem not in elem_list_altium.properties: 
                        continue
                flag1 = True
    
    
        for elem_list_cadence in list_cadence: 
            if len(elem_list_cadence.properties) == len(elem.properties): 
                for one_prop_elem in elem.properties: 
                    if one_prop_elem not in elem_list_cadence.properties: 
                        continue
                flag2 = True   

        if flag1 and flag2:
            ans.remove(elem)


    answer = ans


    for elem in answer:
        answer_set.add(elem.name)


    for elem in answer_set:
        file.write(elem+ '\n')