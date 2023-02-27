import threading

class OddNumberFinder:
    def __init__(self,numbers):
        self.numbers=numbers

    def find_odd_numbers(self):
        odd_numbers=[]
        for number in self.numbers:
            if number %2!=0:
                odd_numbers.append(number)
        return odd_numbers

def main():
    numbers=range(1,2501)
    odd_number_finder=OddNumberFinder(numbers)
    thread=threading.Thread(target=odd_number_finder.find_odd_numbers)
    thread.start()
    thread.join()

    odd_numbers=odd_number_finder.find_odd_numbers()
    print("Odd numbers:",odd_numbers)

if __name__=="__main__":
    main()
