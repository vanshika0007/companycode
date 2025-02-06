import time  
from typing import List, Set  

def read_words_from_file(filename: str) -> List[str]:  
    """Reads words from a file and returns a list of words."""  
    with open(filename, 'r') as file:  
        return [line.strip() for line in file]  

def is_compound_word(word: str, word_set: Set[str], memo: dict) -> bool:  
    """Checks if a word is a compound word using backtracking with memoization."""  
    if word in memo:  
        return memo[word]  
    
    for i in range(1, len(word)):  
        prefix, suffix = word[:i], word[i:]  
        if prefix in word_set and (suffix in word_set or is_compound_word(suffix, word_set, memo)):  
            memo[word] = True  
            return True  
    
    memo[word] = False  
    return False  

def find_longest_compounded_words(words: List[str]) -> tuple:  
    """Finds the longest and second-longest compounded words."""  
    word_set = set(words)  
    memo = {}  
    longest, second_longest = "", ""  
    
    for word in sorted(words, key=len, reverse=True):  
        word_set.remove(word)  # Avoid using the word itself  
        if is_compound_word(word, word_set, memo):  
            if not longest:  
                longest = word  
            elif not second_longest:  
                second_longest = word  
            if longest and second_longest:  
                break  
        word_set.add(word)  # Restore for the next iteration  
    
    return longest, second_longest  

def main():  
    """Main function to process files and print results."""  
    filenames = ["Input_01.txt", "Input_02.txt"]  
    
    for filename in filenames:  
        start_time = time.time()  
        words = read_words_from_file(filename)  
        longest, second_longest = find_longest_compounded_words(words)  
        time_taken = int((time.time() - start_time) * 1000)  # Convert to milliseconds  
        
        print(f"File: {filename}")  
        print(f"Longest Compound Word: {longest}")  
        print(f"Second Longest Compound Word: {second_longest}")  
        print(f"Time taken: {time_taken} milliseconds\n")  

if __name__ == "__main__":  
    main()