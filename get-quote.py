import random

def primary():
    print("Keep it logically awesome.")

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    
    last = len(quotes) -1
    rnd = random.randint(0, last)
    print("This is the first line of quote.txt: "+quotes[0])
    print("This is the last line of quote.txt: "+quotes[13])

    print("This is a randomly generated line: "+quotes[rnd])

if __name__== "__main__":
  primary()
