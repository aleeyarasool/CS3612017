#a)-g)
a =[1,2,3,4,5,6]
b=a
b[1]=9
c=a[:]
c
c[2] = 13
a

#function set_first_elem_to_zero(1) which takes a list, sets the first entry to 0, and returns the list
def set_first_elem_to_zero(l):
    l[0]=0

def main():
    l = [3,4,5,7]
    set_first_elem_to_zero(l)
    print(l)
    
if __name__== "__main__":
      main()   
