
import random
def misslen():
    size = random.randint(2, 5)
    vars = []
    for i in range(size):
       vars.append(random.randint(1, 5))
    symbols = ['+', '-', '*', '/','^']
    brackets = "("*size
    ques = f"what is the value of {brackets}{vars[0]}"
    ans = vars[0]
    for i in range(1, size):
        curr_symbol =  random.choice(symbols)
        ques +=''if curr_symbol=='^' else curr_symbol
        ques += ''if curr_symbol=='^' else str(vars[i])+")"
        curr_ans = ans
        match curr_symbol:
            case '+':
                curr_ans += vars[i]
            
            case '-':
                curr_ans -= vars[i]
            
            case '*':
                curr_ans *= vars[i]
                
            case '/':
                curr_ans /= vars[i]
                
            case '^':
                pow = random.randint(2, 4)
                ques += f"^{pow}"+")"
                curr_ans = curr_ans**(pow)
                
        ans = curr_ans

        options = [
            ans + random.randint(-ans, ans),
            ans + random.randint(-ans, ans),
            ans + random.randint(-ans, ans),
            ans
        ]   
        
        random.shuffle(options)
        if options[0] == ans:
            correct_option_key = "optionA"
        elif options[1] == ans:
            correct_option_key = "optionB"
        elif options[2] == ans:
            correct_option_key = "optionC"
        else:
            correct_option_key = "optionD"

        data_to_be_transferred = {
            "question": ques,
            "optionA": options[0],
            "optionB": options[1],
            "optionC": options[2],
            "optionD": options[3],
            "correctOption": correct_option_key
        } 
    return(data_to_be_transferred)
# print(misslen())