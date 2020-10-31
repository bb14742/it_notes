import functools #For functools.reduce()

def sum_stuff_using_reduce(a,b): #For functools.reduce()
    return a+b

if __name__ == '__main__':
    #Print
    x = 123
    print(f'Two print statements on the same line: ',end='')
    #or
    #print(f'Two print statements on the same line: ',end="")
    print(f'{x:}')
    #Two print statements on the same line: 123
    
    #lists:
    print(f'\nList stuff:')
    new_list = list()
    new_list2 = [1, 3, 56, 34, 67, 21, 43]
    new_list.append(1) # Add a number to a list
    new_list.append(2) # Add another number to a list
    new_list.append(7)
    if 56 in new_list2: #Have to check whether the element is in the list or new_list2.remove() will throw an error. 
        new_list2.remove(56) #Remove the element from the list, Don't pop beyond end of list.
    new_list.pop(1) #Pops 2 off the list as it is in the 1 position.
    print(f'{new_list}')  #[1, 7]
    print(f'new_list2; {new_list2}, new_list2[2]: {new_list2[2]}')
    #new_list2; [1, 3, 34, 67, 21, 43], new_list2[2]: 34

    new_list2.sort()
    print(f'\nnew_list2.sort():           {new_list2}')
    new_list2.sort(reverse=True)
    print(f'new_list2.sort(reverse=True): {new_list2}')

    #Init a list of length 20 with the chaacter A:
    listOfStrings1 = ['A'] * 20
    print(listOfStrings1)
    #['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']

    #list comprehension:
    x=1
    y=1
    z=1
    n=2
    print( [[i, j, k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n] )
    #[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    #list comprehension:
    #n, m = input().split() 
    n = '3' 
    m = '2'
    sc_ar = ['1', '5', '3'] #input().split()
    #A = set(input().split())
    #B = set(input().split())
    A = {'3', '1'}
    B = {'5', '7'}
    #Sum the values in A, which are in sc_ar, Sum B, subtract A - B:
    print(sum((i in A) - (i in B) for i in sc_ar))
    #1
    #This sums the occurrences of the values in sc_ar in A & B. 
    #A has 2 occurrences 1 + 3 = 2
    #B has 1 occurence       5 = 1   2 - 1 = 1

    #enumerate(): Produces the position (iterator) and the value of a list:
    my_list = ["Brian", "Blah", "Fred", "Simple"]
    for pos, val in enumerate(my_list):
        print(f'pos: {pos}, val: {val}')
        #pos: 0, val: Brian
        #pos: 1, val: Blah
        #pos: 2, val: Fred
        #pos: 3, val: Simple

    #dictionaries:
    print(f'\nDictionary stuff:')
    new_dict = dict()
    new_dict2 = {}
    new_dict = {"Brian": 60,
                "Bill": 30,
                "Fred": 15}
    #Add a new key/value pair to the dictionary, since it doesn't previously exist:
    new_dict.update({"Sam": 47})
    #Update an existing value for a previously existing key:
    new_dict.update({"Bill": 24})
    #Update an existing value for a previously existing key:
    new_dict["Fred"] = 25
    print(f'new_dict: : {new_dict}') #Outputs: new_dict: : {'Brian': 60, 'Bill': 24, 'Fred': 15, 'Sam': 47}
    name = "Bill"
    print(f'new_dict["Bill"]: {new_dict[name]}') #Outputs: new_dict["Bill"]: 24
    #Remove an element from a dictionary using <dictionary>.pop():
    removed_value = new_dict.pop("Bill")
    print(f'removed_value: {removed_value}, new_dict: {new_dict}') #Outouts: removed_value: 24, new_dict: {'Brian': 60, 'Fred': 15, 'Sam': 47}
    print(f'new_dict.keys():   {new_dict.keys()}')   #dict_keys(['Brian', 'Fred', 'Sam'])
    print(f'new_dict.values(): {new_dict.values()}') #dict_values([60, 25, 47])
    

    #Tuples:
    print(f'\nTuple stuff:')
    #Define and then update the tuple by recreating it:
    new_tuple = (1, 2)
    new_tuple2 = (3, 4)
    new_tuple3 = (7, 8)
    new_tuple = new_tuple + new_tuple2 + new_tuple3
    print(f'Tuple: {new_tuple}, new_tuple[2]: {new_tuple[2]}, new_tuple[2:4]: {new_tuple[2:4]}')
    #Outputs: Tuple: (1, 2, 3, 4, 7, 8), new_tuple[2]: 3, new_tuple[2:4]: (3, 4)

    #A tuple with 1 item requires a trailing , or it will be a string:
    tup1 = ('Michael',) #tuple
    str1 = ('Michael')  #string
    print(f'tup1: {type(tup1)}, str1: {type(str1)}')
    #Outputs: tup1: <class 'tuple'>, str1: <class 'str'>

    points_list = [1, 2, 3, 4, 5]
    points_tuple = tuple(points_list)
    points_tuple = points_tuple + (6,)
                                  # 0  1  2  3  4  5
                                  #(1, 2, 3, 4, 5, 6)
    print(max(points_tuple))      #6
    print(f"{points_tuple[1]}")   #2
    print(f"{points_tuple[1:3]}") #(2, 3)
    points_tuple = points_tuple[0:2] + points_tuple[3:]
    print(points_tuple) #(1, 2, 4, 5, 6)

    #Strings:
    print(f'\nString stuff:')
    str = 'abcdefghijklmnopqrstuvwxyz'
    print(f'             01234567890123456789012345')
                                       #             01234567890123456789012345
    print(f'str:         {str}')       #str:         abcdefghijklmnopqrstuvwxyz
    print(f'str[0:]:     {str[0:]}')   #str[0:]:     abcdefghijklmnopqrstuvwxyz
    print(f'str[4:]:     {str[4:]}')   #str[4:]:     efghijklmnopqrstuvwxyz
    print(f'str[4:6]:    {str[4:6]}')  #str[4:6]:    ef
    print(f'str[:5]:     {str[:5]}')   #str[:5]:     abcde
    print(f'             01234567890123456789012345')
                                       #             01234567890123456789012345
    print(f'str[:-5]:    {str[:-5]}')  #str[:-5]:    abcdefghijklmnopqrstu
    print(f'str[4:-5]:   {str[4:-5]}') #str[4:-5]:   efghijklmnopqrstu
    print(f'str[-4:]:    {str[-4:]}')  #str[-4:]:    wxyz
    print(f'str[-4:24]:  {str[-4:24]}')#str[-4:24]:  wx

    list1 = ['A', 'B', 'C']
    x = "-".join(list1)
    print(f'join: {x}')  #join: A-B-C

    list1 = ['Bill', 'Sam', 'Toast']
    x = "-".join(list1)
    print(f'join: {x}') #join: Bill-Sam-Toast

    '''
    string1 = input().strip() #Could also use: input().strip(' '), .strip() returns a string
    1 2 3 4 5 #<-- User inputs
    print(f'{string1}', {type(string1)})
    #1 2 3 4 5 {<class 'str'>}   <-- Outputs

    list1 = input().split()   #.split() returns a list, could also do: .split(' ')
    1 2 3 4 5 #<-- User inputs
    print(f'{list1}', {type(list1)})
    #['1', '2', '3', '4', '5'] {<class 'list'>}  <-- Outputs

    str_list = list(input())  #Same as: str_list = list(input().split(' '))
    1 2 3 4 5 #<-- User inputs
    print(f'{str_list}, {type(list1)}')
    ['1', ' ', '2', ' ', '3', ' ', '4', ' ', '5']   <-- Outputs

    a_int_num, b_int_num = map(int,input().split()) #Reads in 2 space seperated integers
    '''

    #Create a string by repeating a character some # of times:
    str_num = '1' * 5
    print(f'\nRepeat \'1\', 5 times: {str_num}, variable type: {type(str_num)}')
        #Repeat '1', 5 times: 11111, variable type: <class 'str'>


    #Counter from collections
    print(f'\nCounter() from collections stuff:')
    import collections
    shoe_sizes = ['2', '3', '4', '5', '6', '8', '7', '6', '5', '18']
    size_cnt = collections.Counter()
    #Count the # of occurrences of each shoe size.
    for size in shoe_sizes:
        size_cnt[size] += 1
    print(f'size_cnt: {size_cnt}')
    #  size_cnt: Counter({'5': 2, '6': 2, '2': 1, '3': 1, '4': 1, '8': 1, '7': 1, '18': 1})
    print(f'size_cnt["5"]: {size_cnt["5"]}')  #Outputs: 2
    size_cnt["5"] = size_cnt["5"] - 1
    print(f'size_cnt["5"]: {size_cnt["5"]}')  #Outputs: 1

    print(f'size_cnt["2"]: {size_cnt["2"]}')  #Outputs: 1
    # size_cnt["2"]: 1
    size_cnt["2"] = size_cnt["2"] - 1
    print(f'size_cnt["2"]: {size_cnt["2"]}')  #Outputs: 0
    # size_cnt["2"]: 0

    #Alternative way to populate collections.Counter():
    magazine = ['give', 'one', 'me', 'one', 'grand', 'today', 'grand', 'night']
    note = ['give', 'one', 'grand', 'today']
    m = collections.Counter(magazine)
    print(m) #Counter({'one': 2, 'grand': 2, 'give': 1, 'me': 1, 'today': 1, 'night': 1})
    n = collections.Counter(note)
    print(n) #Counter({'give': 1, 'one': 1, 'grand': 1, 'today': 1})
    #ret == True if all entries and sufficient counts in n are in m:
    ret = (n - m) == {}


    #itertools.combinations: For a string or list, produce all possible combinations:
    from itertools import combinations
    x = 'ABCD'
    print(f"\nPrint all 2-character combinations of string: {x}")
    print(list(combinations(x,2)))
    #Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

    print(f"Print all 3-character combinations of string: {x}")
    print(list(combinations('ABCD',3)))
    #Output: [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]

    x = ['A','B','C','D']
    print(f"Print all 2-character combinations of list: {x}")
    print(list(combinations(x,2)))
    print(f'')
    #Output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]



    #Read Input from stdin:
    print(f'Enter two integer numbers, like: 1 2, show use of map()')
    n, m = map(int,input().split()) #Use this to read in space-seperated values as integers, for example: 1 2
                                    #It puts n=1, m=2
    print(f'n: {n}, m: {m}') #n: 1, m: 2

    print(f'Enter two characters, like: A B, str1.split()')
    str1 = input() #Read in the string of values
    x, y = str1.split() #Seperate them on the spaces
    print(f'x: {x}, y: {y}') #x: A, y: B

    s1 = "HARRY"
    list_of_chars = list(map(list,s1))
    print(f'\nString: {s1}, List of characters: {list_of_chars}\n')
    #String: HARRY, List of characters: [['H'], ['A'], ['R'], ['R'], ['Y']]


    #Convert numbers
    #Convert an integer to a binary number:
    int_num=5
    bin_num = format(int_num, 'b')
    print(f'Converted integer {int_num} to binary format: {bin_num}')
    #Converted integer 5 to binary format: 101

    #Convert an binary number to integer:
    int_num = int(bin_num,2)  #The int() function can take a 2nd parm indicating the base of the num to convert
    print(f'This binary number {bin_num}, was converted to an integer number: {int_num}')

    #String searching
    print(f'\nSearch strings using re:')
    import re
    S = "aaa123aa"
    k = "aa"
    pattern = re.compile(k)
    r = pattern.search(S) #Search for value assigned to k in S
    if not r:
        print("(-1, -1)")
    while r:
        print("({0}, {1})".format(r.start(), r.end() - 1))
        r = pattern.search(S,r.start() + 1)

    #Use find() to search for substring in string:
    #The find() method returns -1 if it doesn't find the substring in string. 
    word = 'My mamma done told me'
    result = word.find('done')
    print(f'\nThe string, \'{word}\' contains the word \'done\' at position {result}. Used word.find(\'done\')')
    print(f'             0123456789')

    #string.index() is similar to find(), but index() raises a ValueErros exception if it 
    #doesn't find the subsrting in string. 
    result_index = word.index('done')
    print(f'The string, \'{word}\' contains the word \'done\' at position {result}. Used word.index(\'done\')')

    #functools.reduce(), requires: import functools
    #reduce() performs a function call on a list. reduce expects 2 parameters.
    lis = [ 1 , 3, 5, 6, 2 ] 
    print ("\nThe sum of the list elements using reduce() is : ",end="") 
    print (functools.reduce(lambda a,b : a+b,lis)) #The sum of the list elements is : 17

    print ("\nThe sum of the list elements using reduce() is : ",end="") #sum_stuff_using_reduce() defined at top
    print (functools.reduce(sum_stuff_using_reduce,lis)) #The sum of the list elements is : 17

    #zip() combines two tuples or lists, returns iterator, but you can put tuple() or list() around zip().
    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "Vicky")
    x = tuple(zip(a, b))
    print(f'\nzip() output of two tuples: {x}') #Output: (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
    #Note Vicky was dropped due to tuple length.
    #(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

    a = ["John", "Charles", "Mike"]
    b = ["Jenny", "Christy", "Monica", "Vicky"]
    x = list(zip(a, b))
    print(f'\nzip() output of two lists: {x}')
    #[('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]

    #lambda function: general form is: lambda: arguments : expression
    #In this example, check_num is a function:
    check_num = lambda x: 'Num greater than 5' if x > 5 else 'Num not greatrer than 5'
    print(check_num(2))

    #map(func,iterables) <-- passes each element of the iterable to the function:
    #map() returns an iterable, but you can cast it to a list or tuple:
    num_list = [2, 3, 4, 5, 6]
    increased = list(map(lambda x: x+3, num_list))
    print(increased)
    #[5, 6, 7, 8, 9]


    #Try Catch that will catch all exceptions:
    '''
    try:
        popThis = firstDay.index(day) #<-- Some code, whatever
    except:
        popThis=-1          #<-- Some code, whatever
        keepLooking = False #<-- Some code, whatever
        continue  #<-- Continue with the current loop
    '''

    #Math
    '''
    Challenge:
    https://www.hackerrank.com/challenges/winning-lottery-ticket/problem

    Past Challenges:
    A motor car is three times as old as its tires were when it was as old as the tires are now. When its tires are as old as the car is now, the car will be a year older than the tires are now. What are the present ages of car and tires?
    http://hr.gs/johndeere-softwareengineer-sampletest 
    *Including the sample test as well since many team members are already working on it. Can discuss common challenges.
    https://www.hackerrank.com/challenges/closest-number/problem
    https://www.hackerrank.com/challenges/interviews/problem
    https://www.hackerrank.com/challenges/common-child
    '''

    #To start MySQl on the Mac:
    #1. For my work Mac use: sudo /usr/local/mysql/bin/mysql -u root -p
    #2. When prompted enter the password for the logged in ID. At the second prompt, enter the password for MySQL. 

    #Display the DDL for table manager:
    #SHOW CREATE TABLE manager;
