"""给定一个包含字符串的列表，例如 words = ["Apple", "banana", "kiwi", "orange", "grape"]。
使用列表推导式创建一个新的列表，其中包含原列表中所有长度大于 5 的字符串,并小写。
使用字典推导式创建一个新的字典，其中键为原列表中所有长度小于等于 5 的字符串，值为这些字符串的长度。

请将实现这两个功能的代码合并到一个函数中，该函数接收一个字符串列表作为输入，并返回一个包含两个元素的元组：
第一个元素是符合列表推导式条件的新列表，第二个元素是符合字典推导式条件的新字典。"""
words = ["Apple", "banana", "kiwi", "orange", "grape"]
words_cond = [word.lower() for word in words if len(word)>5]
dict_cond = {word.lower(): len(word) for word in words if len(word)<=5} 
tuple = (words_cond,dict_cond)
print(tuple)

