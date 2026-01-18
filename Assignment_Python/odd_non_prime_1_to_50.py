print("Odd Non-Prime Numbers from 1 to 50:")
for num in range(1, 51):
    if num % 2 != 0:       
        if num < 1:        
            print(num, end=" ")
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                print(num, end=" ")

