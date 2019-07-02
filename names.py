NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list(dict.fromkeys(x.title() for x in names))
#print(dedup_and_title_case_names(NAMES))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    namessort = sorted(names, key=lambda n:n.split()[1], reverse=True)
    return namessort
#print(sort_by_surname_desc(NAMES))


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    firstname = [x.split()[0] for x in names]
    namesshort = min(firstname, key=len)
    return namesshort
print(shortest_first_name(NAMES))
