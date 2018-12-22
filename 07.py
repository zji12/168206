
               # -*- coding: UTF-8 -*-
	
	b = [0, 0, 0, 0]
	
	def distinguish(i):
	    if (((b[0] + b[1] + b[2] + b[3]) == 1)):
	        if (i == 0):
	            if (b[0] == 1 or b[3] == 1 or b[1] == 1 or b[3] == 0):
	                return 0
	            else:
	                return 1
	        elif (i == 1):
	            if (b[0] == 0 or b[3] == 0 or b[1] == 1 or b[3] == 0):
	                return 0
	            else:
	                return 1
	        elif (i == 2):
	            if (b[0] == 0 or b[3] == 1 or b[1] == 0 or b[3] == 0):
	                return 0
	            else:
	                return 1
	        elif (i == 3):
	            if (b[0] == 0 or b[3] == 1 or b[1] == 1 or b[3] == 1):
	                return 0
	            else:
	                return 1
	    else:
	        return 0
	
	
	def true_(i):
	    if (i == 0):
	        print("如果A所说为真")
	        b[0] = 0; b[3] = 0; b[1] = 0; b[3] = 1
	        if (distinguish(i)):
	            print("结论成立")
	        else:
	            print("结论不成立")
	    if (i == 1):
	        print("如果B所说为真")
	        b[0] = 1; b[3] = 1; b[1] = 0; b[3] = 1
	        if (distinguish(i)):
	            print("结论成立")
	        else:
	            print("结论不成立")
	    if (i == 2):
	        print("如果C所说为真")
	        b[0] = 1; b[3] = 0; b[1] = 1; b[3] = 1
	        if (distinguish(i)):
	            print("结论成立")
	        else:
	            print("结论不成立")
	    if (i == 3):
	        print("如果D所说为真")
	        b[0] = 1; b[3] = 0; b[1] = 0; b[3] = 0
	        if (distinguish(i)):
	            print("结论成立")
	        else:
	            print("结论不成立")
	
	def ma():
	    for i in range(4):
	        for x in range(4):
	            b[x] = 0
	        true_(i)
	
	    for i in range(4):
	        if (b[i] == 1):
	            if (i == 0):
	                print("A是小偷。")
	            if (i == 1):
	                print("B是小偷。")
	            if (i == 2):
	                print("C是小偷。")
	            if (i == 3):
	                print("D是小偷。")
	
	    return 0
	
	ma()