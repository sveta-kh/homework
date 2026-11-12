import multiprocessing, time

def facttorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result

if __name__ ==  "__main__":
 
    #Single-process   
    start =time.time()
    facttorial(13000)
    facttorial(17000)
    end = time.time()
    print(f"Single-process time: {end - start:.2f}")

    #Multiprocessing
    
    start = time.time()
    p1 = multiprocessing.Process(target= facttorial, args=(13000,))
    p2 = multiprocessing.Process(target=facttorial, args=(17000,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print(f"Multiprocessing time: {end - start:.2f}")

