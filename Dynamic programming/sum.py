

def jc(n):
    if n == 1:
        return 1
    else:
        return n*jc(n-1)



if __name__ == "__main__":
    print(jc(10))