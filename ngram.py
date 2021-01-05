## n-grams using python
## input string = "banana" , n = 2 
## output = { 'ba':1,'an':2,'na':2 }

def n_gram(input_text, n):
    length = len(input_text)
    output = {}
    if n<=length:
        for i in range(length-1):
            gram = input_text[i:n+i]
            if len(gram)==n:
                if gram not in output:
                    output[gram] = 1
                else:
                    output[gram] += 1
        print("\nInput String:",input_text)
        print("n:",n)
        print("\nOutput:",output)
        print()

    else:
        print("n",n,"is greater than input length")
                
# tt = "coconut"
# n_gram(tt,2)