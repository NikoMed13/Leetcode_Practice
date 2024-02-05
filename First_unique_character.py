def unique_character(word):
    for i in range(len(word)):
        char = word[i]
        if word.count(char) == 1:
            return i

    else:
        return -1
            
        
def main():
    print(unique_character("leetcode"))
    print(unique_character('loveleetcode'))
    print(unique_character('aabb'))
if __name__ == "__main__":
        main()