# lt=[1,2,3,4,5]
# sum=0
# for i in lt:
#   sum+=i
# print(sum)

# lt=[10, 15, 22, 33, 40, 51]
# even=0
# odd=0
# for i in lt:
#   if i%2==0:
#     even+=1
#   else:
#     odd+=1
# print('even:',even)
# print('odd:',odd)

# lt=[12, 45, 7, 89, 34]
# largest=0
# for i in lt:
#   if i>largest:
#     largest=i
# print(largest)

# lt=['p','y','t','h','o','n']
# rev=""
# for i in lt:
#   rev=i+rev
# print(rev)  

# lt=[10, 5, 20, 8, 20, 15]
# largest=lt[0]
# second_largest=None
# for i in lt:
#   if i>largest:
#     second_largest=largest
#     largest=i
#   elif i!=largest and(second_largest is None or i>second_largest):
#     second_largest=i
# print(second_largest)

# lt = [0, 1, 0, 3, 12]
# result=[]
# for i in lt:
#   if i!=0:
#     result.append(i)
# zero_count=lt.count(0)
# result.extend([0]*zero_count)
# print(result)

# text="aabbcdd"
# for i in text:
#   if text.count(i)==1:
#     print(i)
#     break

# a = "listen"
# b = "silent"

# # if sorted(a)==sorted(b):
# #   print("anagram")
# # else:
# #   print("not anagram")

# if len(a)!=len(b):
#   print("not anagram")
# else:
#   for i in a:
#     if a.count(i)!=b.count(i):
#       print("not anagram")
#   else:
#     print('anagram')

# text = "apple banana apple mango banana apple"
# text1=text.split()
# d={}
# for i in text1:
#   if i in d:
#     d[i]+=1
#   else:
#     d[i]=1
# print(d)


# lt = [1, 2, 3, 5, 6]
# n=6
# expected=n*(n+1)//2
# actual=sum(lt)
# missing=expected - actual
# print(missing)


# lt = [1, 2, 3, 2, 4, 5, 3]
# seen=[]
# duplicate=[]
# for i in lt:
#   if i not in seen:
#     seen.append(i)
#   else:
#     duplicate.append(i)
# print(duplicate)

# text = "python programming"
# count=0
# for i in text:
#   if i in "AEIOUaeiou":
#     count+=1
# print(count)


# lt = [25, 10, 45, 3, 18]
# smallest=lt[0]
# for i in lt:
#   if i<smallest:
#     smallest=i
# print(smallest)

# lt = [10, 15, 22, 33, 40, 51]
# even=0
# for i in lt:
#   if i%2==0:
#     even+=i
# print(even)

# lt = [1, 2, 2, 3, 4, 3, 5, 1]
# seen=[]
# for i in lt:
#   if i not in seen:
#     seen.append(i)
# print(seen)

# lt = [10, 5, 20, 8, 5, 15]
# smallest=lt[0]
# second_smallest=None
# for i in lt:
#   if i<smallest:
#     second_smallest=smallest
#     smallest=i
#   elif i!=smallest and (second_smallest is None or i<second_smallest):
#     second_smallest=i
# print(second_smallest)

# text = "hello world python"
# text1=text.split()
# result=""
# for i in text1:
#   rev=""
#   for j in i:
#     rev=j+rev
#   result=result+rev+" "
# print(result)


# text = "I love learning Python programming"
# text1=text.split()
# longest=""
# for i in text1:
#   if len(i)>len(longest):
#     longest=i
# print(longest)

# text = "banana"
# d={}
# for i in text:
#   if i in d:
#     d[i]+=1
#   else:
#     d[i]=1
# print(d)

# lt1 = [1, 2, 3, 4, 5]
# lt2 = [3, 4, 5, 6, 7]
# common=[]
# for i in lt1:
#   if i in lt2:
#     common.append(i)
# print(common)


    

# lt = [1, -2, 3, -4, 5, -6]
# lt1=[]
# lt2=[]
# for i in lt:
#   if i<0:
#     lt1.append(i)
#   else:
#     lt2.append(i)
    
# print(lt1+lt2)

# text="madam"
# rev=""
# for i in text:
#   rev=i+rev
# if rev==text:
#   print('palindrome')
# else:
#   print('not')

# lt = [2, 7, 11, 15]
# target = 9
# for i in lt:
#   for j in lt:
#     if i+j==9:
#       print(i,j)

# text = "programming"
# for i in text:
#   if text.count(i)>1:
#     print(i)
#     break

# lt = [1, 2, 3, 5, 6]
# n = 6
# expected=n*(n+1)//2
# actual=sum(lt)
# missing=expected-actual
# print(missing)

# lt = [10, 15, 22, 33, 40, 51]
# even=[]
# odd=[]
# for i in lt:
#   if i%2==0:
#     even.append(i)
#   else:
#     odd.append(i)
#print('even:',even)
# print('odd:',odd)

# text = "apple banana orange mango"
# text1=text.split()
# for i in text1:
#   for j in i:
#     if i.count(j)>1:
#       print(i)
#       break

# text = "I love Python coding"
# text1=text.split()
# d={}
# for i in text1:
#   if len(i) in d:
#     d[len(i)]+=1
#   else:
#     d[len(i)]=1
# print(d)

# lt = [1, 2, 3, 2, 4, 2, 5]
# l=[]
# for i in lt:
#   if lt.count(i)==1:
#     l.append(i)
# print(l)


# name="tEJas32$#sWINi"
# cap=""
# small=""
# special=""
# for i in name:
#   var=ord(i)
#   if var>=65 and var<=90:
#     cap+=i
#   elif var>=97 and var<=122:
#     small+=i
#   else:
#     special+=i
# print(cap,small,special )


# v="tej__as_w_ini__"
# h=""
# for i in v:
#   if i!="_":
#     h+=i
# print(h)
















