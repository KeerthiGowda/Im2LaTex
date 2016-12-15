#parses the in files to get the data, labels and symbols
def parser_function(ink_file_name, output_file_name,current_dir):

	import re
	import string


	label_map = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52,'0':53,'1':54,'2':55,'3':56,'4':57,'5':58,'6':59,'7':60,'8':61,'9':62,'\\alpha':63,'\\beta':64,'\\gamma':65,'\\phi':66,'\\pi':67,'\\theta':68,'\\sigma':69,'\\mu':70,'\\Delta':71,'+':72,'-':73,'\\pm':74,'\div':75,'\!':76,'\\times':77,'\/':78
,'\\':79,'\\rightarrow':80,'|':81,'\\forall':82,'\\exists':83,'\\in':84,'\\sum':85,'\\int':86,'\\neq':87,'\\lt':88,'\\Ieq':89,'\\gt':90,'\\geq':91,'\\log':92,'\\sin':93,'\\cos':94,'\\tan':95,'\\lim':96,'(':97,')':98,'{':99,'}':100,'[':101,']':102
,'\\infty':103,'\\COMMA':104,'.':105,'\\Idots':106,'\\cdots':107,'\\lamda':108,'=':109,'\\sqrt':110,'\\ldots':111,'\\leq':112}

	
	#{'1':1,'2':2} 

	ink_file = open(ink_file_name,"r") 
	
	temp_file_name = current_dir+'temp.csv'
	temp_file = open(temp_file_name,"w") 

	count = 0
	count_trace = 0
	index = 0
	label_array = []

	output_file = open(output_file_name,"w") 

	for line in ink_file:
	#	print(line)
		if 'traceDataRef' in line:
			count_trace = count_trace + 1
				
		if 'annotation type="truth"' in line:

			count = count +1
			if(count > 2):
				if(count > 3):
					#print('number of trace = ' + str(count_trace))
					output_file.write(''+str(count_trace)+',')
				count_trace = 0
			
	#			print(line)
				parsed_str = re.findall(r'\>([^]]*)\<', line)
	#			print(parsed_str)
				for character in parsed_str:
						#print(character)
						if(character == '!'):
							label = 76;
						else:
							label = label_map[character]
							if(label):
								label_array.append(label);	
							else:
								print("symbol NOT found, add this new symbol !")
								print(input_file_name)
								print(label)
								raise Exception('This is the exception you expect to handle')
						#print('label = ' +str(label))
	
		if '<trace id=' in line:
			#print(line)
			parsed_str = re.findall(r'\>([^]]*)\<', line)
			for character in parsed_str:
				for string_number in character:
					if(string_number == ' '):
						temp_file.write(',')
					elif (string_number == ','):
						continue
					else:
						temp_file.write(string_number)
					
			temp_file.write('\n')
	#				print(string_number)
					#print('#')
		
			

	
	ink_file.close()
	#print('number of trace = ' + str(count_trace))
	output_file.write(''+str(count_trace))
	output_file.write('\n')
	first = 1
	for element in label_array:
		if(first == 0):
			output_file.write(',')
		output_file.write(str(element))
		first = 0
	

	temp_file.close()

	output_file.write('\n')
	temp_file = open(temp_file_name,"r") 
	for each_line in temp_file:
		output_file.write(each_line)

	output_file.close()

	return





