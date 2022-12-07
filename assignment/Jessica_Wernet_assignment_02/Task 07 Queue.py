def movingQueue():
  queue = []
  while len(queue) >= 0:
    print('Pls enter a new name if there is a new person in the queue \nif the queue can move along write "next"')
    input_list = input()
    
    if input_list != 'next':
      queue.append(input_list)
      print('is on position:', len(queue))
    
    else:
        if len(queue) > 0:
          print(queue[0],'leaves the queue')
          queue.pop(0)
        else:
          print('the queue is empty')
          break

movingQueue()