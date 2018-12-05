
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

        if i>50:
           break
    print('\n\n\n\n\n\n******Finished****\nLines correct: ',correct_count,' out of',i,'\n\n\n\n\n')

def advtest(new, old):
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
        linenews,lineolds=linenew.replace(' ',""),lineold.replace(' ',"")
        if linenews==lineolds:
            print('\nLine: '+str(i)+' Elem: ',elementnew,lengths,' TRUE MATCH ')
            print(linenew)
            print(lineold)
            good_line, bad_line = '', ''
            for charnew, charold in zip(linenew,lineold):
                if charnew == charold:
                    good_line+=charnew
                else:
                    good_line+=''
            print('GOOD LINE: ', good_line)
            correct_count +=1
        else:
            status=[]
            for elemnew, elemold in zip(linenew, lineold):
                if elemold != elemnew:
                    status.append(elemold)
            print('\nLine: '+str(i)+' Elem: ',elementmatch,lengths, ' False . . . Old codeissues: ', ''.join(status),'\nNew:',linenews,'\nOld:',lineolds)       

        # if i>100:
        #    break
    print('\n\n\n\n\n\n******Finished****\nLines correct: ',correct_count,' out of',i,'\n\n\n\n\n')

def contenttest(new, old):
    with open(old) as file:  
        old = file.read()
    new = new.splitlines()
    old = old.splitlines()
    i, match_count=0,0
    new = [line.rstrip() for line in new]
    old = [line.rstrip() for line in old]
    print(new, old)
    for line in new:
        i+=1
        try:
            old.index(line)
            print('LINE '+str(i), 'Length: ',len(line),' is a MATCH')
            match_count+=1
        except:
            print('LINE '+str(i),'Length: ',len(line),' NOT MATCH')
            print('New: ',line)
            try:
                print('Old: ',old[i])
            except:
                print(' Out of old range')
    print('\n\n\n******* TESTS COMPLETE************')
    print('\nMATCH COUNT : ',match_count, ' out of ', i)