def birthday_match(students):
    '''
    Find a pair of students with the same birthday
    Input: tuple of student (name, bday) tuples
    Output: tuple of student names or None
    Returning first pair we found is enough
    '''
    match_pair = None
    for i,(name_1,bday_1) in enumerate(students[:-1]):
        for (name_2,bday_2) in students[i+1:]:
            if bday_1 == bday_2:
                match_pair = (name_1,name_2) 
                return match_pair
    return match_pair



