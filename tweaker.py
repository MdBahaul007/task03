accuracy_file = open('/root/task_03/accuracy.txt','r')
input_file = open('/root/task_03/input.txt','r')
data_file = open('/root/task_03/data.txt','r')
#display_Acc=open('root/task_03/display_Acc.html','r')


new_accuracy = float(accuracy_file.read())

data = data_file.read()
data = data.split('\n')
epochs = int(data[0])


inputs = input_file.read()
inputs = inputs.split('\n')


if( new_accuracy < 99 ):
    epochs = epochs + 1


data_file.close()
input_file.close()

#input_file = open('/root/task_03/input.txt','w')
#input_file.close()
input_file = open('/root/task_03/input.txt','w')
input_file.write(str(epochs))
input_file.close()
#display_Acc=open('root/task_03/display_Acc.html','w')

#display_Acc.write('\nLayer -1')
#display_Acc.write('\nNumber Of Filters : 20')
#display_Acc.write('\nFilter Size : 5')
#display_Acc.write('\nPool Size : 2')

#display_Acc.write('\nLayer -2')
#display_Acc.write('\nNumber Of Filters : 50')
#display_Acc.write('\nFilter Size : 5')
#display_Acc.write('\nPool Size : 2')
#display_Acc.write('\nEpochs :'+ str(epochs))
#display_Acc.close()

#display_Acc = open('/task_03/display_Acc.html','r+')
#display_Acc.read()
#display_Acc.write('<pre>\n---------------------------------------------\n')
##display_Acc.write(model.summary())

#display_Acc.write('\nLayer -1')
#display_Acc.write('\nNumber Of Filters : 20')
#display_Acc.write('\nFilter Size : 5')
#display_Acc.write('\nPool Size : 2')

#display_Acc.write('\nLayer -2')
#display_Acc.write('\nNumber Of Filters : 50')
#display_Acc.write('\nFilter Size : 5')
#display_Acc.write('\nPool Size : 2')
#display_Acc.write('\nEpochs :'+ str(epochs))


#display_Acc.write('\nAccuracy achieved : ' + str(scores[1])+'\n</pre>')
#display_Acc.close()
