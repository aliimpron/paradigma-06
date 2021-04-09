def postfix_eval (string):
	
	Stack = [ ]
	for token in String.split ( ) :
		if '0' <= token <= '9' :
			Stack . append ( token ) 
		else : # Operator
			operand2 = Stack . pop ( )
			operand1 = Stack . pop ( )
			result = eval ( operand1 + token + operand2 )
			Stack.append ( str (result) ) 
	return stack[0]