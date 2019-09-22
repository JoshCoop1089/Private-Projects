def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", 
    "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    ans = []
    for i in range(len(doc_list)):
        index = doc_list[i].lower().find(keyword) 
        if index != -1:
            end = index+len(keyword)
            if (doc_list[i][end] == ' ' or doc_list[i][end] == '.' 
                or doc_list[i][end] == ',' or end == len(doc_list[i])-1):
                ans.append(i)
    return ans

doc_list = ["casino", "The Learn Python Challenge Casino", "They bought a car, and a horse", 
            "Casinoville"]
ans = word_search(doc_list, 'car')
print(ans)