
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
	        print("���A��˵Ϊ��")
	        b[0] = 0; b[3] = 0; b[1] = 0; b[3] = 1
	        if (distinguish(i)):
	            print("���۳���")
	        else:
	            print("���۲�����")
	    if (i == 1):
	        print("���B��˵Ϊ��")
	        b[0] = 1; b[3] = 1; b[1] = 0; b[3] = 1
	        if (distinguish(i)):
	            print("���۳���")
	        else:
	            print("���۲�����")
	    if (i == 2):
	        print("���C��˵Ϊ��")
	        b[0] = 1; b[3] = 0; b[1] = 1; b[3] = 1
	        if (distinguish(i)):
	            print("���۳���")
	        else:
	            print("���۲�����")
	    if (i == 3):
	        print("���D��˵Ϊ��")
	        b[0] = 1; b[3] = 0; b[1] = 0; b[3] = 0
	        if (distinguish(i)):
	            print("���۳���")
	        else:
	            print("���۲�����")
	
	def ma():
	    for i in range(4):
	        for x in range(4):
	            b[x] = 0
	        true_(i)
	
	    for i in range(4):
	        if (b[i] == 1):
	            if (i == 0):
	                print("A��С͵��")
	            if (i == 1):
	                print("B��С͵��")
	            if (i == 2):
	                print("C��С͵��")
	            if (i == 3):
	                print("D��С͵��")
	
	    return 0
	
	ma()