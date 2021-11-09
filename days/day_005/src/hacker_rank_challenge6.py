#https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true&h_v=zen
import fileinput

def result(string:str):
    index = 0
    even = ''
    odd = ''
    
    while (index < len(string)):
        if index %2 == 0:
            even += string[index]       
        else:
            odd += string[index]       
        index += 1
    result = even + ' ' + odd
    return result

if __name__ == '__main__':
    
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
        
    n = int(args[0])
    
    for string in args[1:]:
        print(result(string))    
