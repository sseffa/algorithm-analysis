def getModeMedian(lst):

    # mode
    # best time = O(n)
    # average time = O(n)
    # worst time = O(n)
    # tek bir for döngüsü olduğu için karmaşıklık n dir
    dict = {}
    max = 0
    for values in lst:
       if values in dict:
          dict[values] += 1
       else:
          dict[values] = 1
    if not max or dict[values] > max[0]:
        max = (values, dict[values])
    mode = max[0]
    
    # sort 
    # best time = O(n)
    # average time = O(n^2)
    # worst time = O(n^2)
    # iç içe 2 for döngüsü olduğundan n^2
    lstLen = len(lst)
    for i in range(lstLen):
        for j in range(0, lstLen-i-1):
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    
    # median
    # best time = O(1)
    # average time = O(1)
    # worst time = O(1)
    # alttaki kod 1 sefer çalıştığı için karmaşıklığı 1 dir
    index = (lstLen - 1) // 2
    median = 0
    if (lstLen % 2):
        median = lst[index]
    else:
         median = (lst[index] + lst[index + 1])/2.0
   
    return mode, median


print(getModeMedian([-5, -4, 0, 3, 3, 5, 5]))
