class_math262 = {'start_time':(2022,11,21,8,30,0,0),'end_time':(2022,11,21,9,30,0,0)}

class_comp202 = {'start_time':(2022,11,21,9,30,0,0),'end_time':(2022,11,21,10,30,0,0)}

class_ecse200 = {'start_time':(2022,11,21,10,30,0,0),'end_time':(2022,11,21,11,30,0,0)}

exam_math263 = {'start_time':(2022,11,22,13,00,0,0),'end_time':(2022,11,22,14,30,0,0)}

exam_wcom206 = {'start_time':(2022,11,22,14,30,0,0),'end_time':(2022,11,22,16,00,0,0)}




ass_math262 = {'due_date':(2022,11,29,00,00,0,0)}

ass_comp202 = {'due_date':(2022,11,29,00,00,0,0)}

ass_ecse200 = {'due_date':(2022,11,29,00,00,0,0)}

ass_math263 = {'due_date':(2022,11,30,00,00,0,0)}

ass_wcom206 = {'due_date':(2022,11,30,00,00,0,0)}





exam = {'math262'}

def create_schedule(to_do_list):
    index = None
    init_list = [1]*16 + [0]*8 + [1]*2 + [0]*10 + [1]*2 + [0]*6 + [1]*4
    output = []
    for item in to_do_list:
        if type(item) == Lecture:
            if item['start_time'][4] == 30:
                init_list[item['start_time'][3] * 2 + 1] = 1
                index = item['start_time'][3] * 2 + 2
            else:
                init_list[item['start_time'][3] * 2] = 1
                index = item['start_time'][3] * 2 + 1
            init_list[index] = 1
        
        
        elif type(item) == Exam:
            if item['start_time'][4] == 30:
                init_list[item['start_time'][3] * 2 + 1] = 1
                index = item['start_time'][3] * 2 + 2
            else:
                init_list[item['start_time'][3] * 2] = 1
                index = item['start_time'][3] * 2 + 1
            init_list[index] = 1
    
        elif type(item) == Assignment:
            for i in range(len(init_list[:])):
                if init_list[:][i] == 0:
                    init_list[i] = 1
                    output.append('Do ' + str(item) + ' assignment from ' + str(i/2) + '00 to ' + str((i+2)/2) + '00.')  
    return output
    
    

