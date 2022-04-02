def find_the_nth_occurrence  (word , the_text , repeatance  ): 
    try :
        index=the_text.find(word ,0)
        while index>=0 and repeatance >1 :
            index =the_text.find (word, index+1)
            repeatance -= 1
            return index  
    except EXception as e :
        return (e)      
    

import re 

def  simple_string_matching (word_1 , word_2) :
    try :
        
        word_1 = word_1.replace('*','.*')
        match_or_not = bool(re.fullmatch(word_1 ,word_2)) 
        return match_or_not
    except Exception as e :
        return e


def is_the_text_palindrome(text):
    try:
        text_1=text[::-1]
        if text_1==text :  
            print(True)
        else :
            print(False)    
        return        
    except Exception as e :
        print(e)    

#BOUNS QUESTION :

def f(s):
    try :
        lst=[]
        lst_letters=[]
        last_lst=[]
        for i in range(len(s)):
            s="".join(s.split())
            lst_letters.append(s[0:i+2])
            lst.append(s.count(s[0:i+2]))
        
        max_val=max(lst)
        
        
        for j in range(len(lst_letters)):
            if lst[j]==max_val:
                last_lst.append(lst_letters[j])
                
    
        if max_val==1:
            return (s,max_val)
        else:
            return (max(last_lst,key=len),max_val)
        return (f(my_string))     

    except Exception as e :
        print(e)

