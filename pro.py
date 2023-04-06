# def analyze_string(lst:list):
#     length=len(lst)
#     if length>1:
#         first_half=analyze_string(lst[0:length//2])
#         second_half=analyze_string(lst[length//2:])
#         joint_a_count=0
#         if first_half['right_most_a_count']!=0 and second_half['left_most_a_count']!=0:
#             joint_a_count=first_half['right_most_a_count'] + second_half['left_most_a_count']

#             if first_half['left_most_a_count']== len(lst[0:length//2]):
#                 left_most_a_count = first_half['left_most_a_count']+second_half['left_most_a_count']
#             else:
#                 left_most_a_count=first_half['left_most_a_count']

#             if second_half['right_most_a_count']== len(lst[length//2:]):
#                 right_most_a_count= second_half['right_most_a_count']+first_half['right_most_a_count']
#             else:
#                 right_most_a_count= second_half['right_most_a_count']
#             highest_a_count= max(left_most_a_count,right_most_a_count,joint_a_count,first_half['highest_a_count'], second_half['highest_a_count'])
        
#         else:
#             left_most_a_count=first_half['left_most_a_count']
#             right_most_a_count=second_half['right_most_a_count']


#             highest_a_count=max(first_half['highest_a_count'],second_half['highest_a_count'])
        
#         res={
#             'left_most_a_count':left_most_a_count,
#             'right_most_a_count':right_most_a_count,
#             'highest_a_count':highest_a_count,
#             }
#         return res

#     if length==1:
#         if lst[0]=='a':
#             res={ 'left_most_a_count':1,
#                   'right_most_a_count':1,
#                   'highest_a_count':1, }
#         else:
#             res={ 'left_most_a_count':0,
#                   'right_most_a_count':0,
#                   'highest_a_count':0 , }
#         return res

# input_string= input('enter your string.. ')
# result_dictionary=analyze_string(input_string)
# final_result=result_dictionary['highest_a_count']
# print('''length of the longest sequence of consecutive'a' within the string is ''',final_result)
print('done')
print('we_done')

