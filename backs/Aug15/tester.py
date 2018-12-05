
def test(new, old):
    print( '\n**************** TESTER TIME, ALL CHANGES HAVE BEEN SAVED...*********************')
    print('                 THE FOLLOWING IS FOR PROMPT ONLY:')
    with open(old) as file:  
        old = file.read()
    i=0
    correct_count = 0
    old = old.splitlines()
    new=new.splitlines()
    for linenew, lineold in zip(new,old):
        i+=1
        elementnew=linenew[:2]
        elementold=lineold[:2]
        elementmatch = elementnew==elementold
        lengths = 'Old len: ',len(lineold),'New len: ',len(linenew)
        linenew,lineold=linenew.replace(' ',""),lineold.replace(' ',"")
        if linenew==lineold:
            print('\nLine: '+str(i)+' Elem: ',elementnew,lengths,' TRUE MATCH ')
            correct_count +=1
        else:
            status=[]
            for elemnew, elemold in zip(linenew, lineold):
                if elemold != elemnew:
                    status.append(elemold)
            print('\nLine: '+str(i)+' Elem: ',elementmatch,lengths, ' False . . . Old codeissues: ', ''.join(status),'\nNew:',linenew,'\nOld:',lineold)       

        if i>100:
            break
    print('\n\n\n\n\n\n******Finished****\nLines correct: ',correct_count,' out of',i,'\n\n\n\n\n')