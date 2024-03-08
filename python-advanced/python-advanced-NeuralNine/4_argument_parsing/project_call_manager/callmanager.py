# Lets say we want to record the incoming calls in one file and the outgoing ones in the other file 



# In the context of the getopt.getopt() function in Python, --incoming is a long option that can be used instead of the short option -i. Long options are more descriptive and self-explanatory compared to short options.

# The string 'hin:o:n:d:' specifies the short options that the program will accept. Each character in the string is an option, and if a character is followed by a colon :, it means that this option requires an argument.

# The list ['incoming', 'outgoing', 'name', 'duration'] specifies the long options that the program will accept. If a long option requires an argument, it should be followed by an equal sign =.

# So, in your case, --incoming is equivalent to -i, and it requires an argument, which should be the name of the incoming file. For example, you could use it like this in the command line:

# python your_program.py --incoming incoming_file.txt

# This would be equivalent to:

# python your_program.py -i incoming_file.txt

# Both of these command lines pass the name of the incoming file (incoming_file.txt) as an argument to the --incoming (or -i) option. This argument can then be accessed and used within your program.


import sys
import getopt

def write(file,name,duration):
    with open(file,'a+') as f:
        f.write(f"{name} - {duration} \n")
 
def main(argv):
    incoming_file = 'incoming_calls.txt'
    outgoing_file = 'outgoing_calls.txt'
    opts_dict = {}
    try:
        opts, args = getopt.getopt(argv, 'ht:n:d:', ['type','name','duration'])
        opts_dict = dict(opts)
         
        print(opts)
    except getopt.GetoptError:
        print('Usage: python program.py -i <incoming_calls_file> -o <outgoing_calls_file>')
        sys.exit(2)
        

    if '-h' in opts_dict:
        print('Help: python program.py -i <incoming_calls_file> -o <outgoing_calls_file>')
        return 
    if opts_dict['-t'] == 'outgoing':
        write(outgoing_file,opts_dict['-n'],opts_dict['-d'])
        print(opts_dict['-n'],opts_dict['-d']," written successfully in the outgoing file")
    elif opts_dict['-t'] == 'incoming':
        write(incoming_file,opts_dict['-n'],opts_dict['-d'])
        print(opts_dict['-n'],opts_dict['-d']," written successfully in the incoming file")

if __name__ == '__main__':
    main(sys.argv[1:])
    
    
    # python callmanager.py -t incoming  -n anand -d 100
    # python callmanager.py -t outgoing  -n ash -d 12