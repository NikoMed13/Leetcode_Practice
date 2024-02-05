def two_sums(int_array, target):
    for i in range(len(int_array)):
        index1 = i
        num = target - int_array[i]
        for j in range(len(int_array)):
            if num == int_array[j]:
                index2 = j
                return index1,index2
    return None
        
        
def main():
    print(two_sums([2,7,11,15], 9))

if __name__ == "__main__":
    
    main()