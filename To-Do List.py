#To-Do List
data = []
print("To-Do List..")
print('''
      1. To add task
      2. To mark as complete
      3. To view task
      ''')

task = 'random'
while task != '4':
  choice = input("\nEnter you choice:")
  
  if(choice == '1'):
      task = input("Enter the task to be done:\n=>")
      data.append(task)
      
  elif(choice == '2'):
      task = input("Enter the completed task:\n=>")
      if task in data:
          data.remove(task)
      else:
          print("The task isn't present in the list")
          
  elif(choice == '3'):
      for task in data:
          print(task)
         
  elif(choice == '4'):
      print("Thank you!")
      break
  
 
  
           

    