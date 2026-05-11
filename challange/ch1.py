tet_lst = [100, 4, 200, 1, 3, 2]
def longest_consecutive(tet_lst):
    if not tet_lst:
        return 0

    sorted_lst = sorted(tet_lst)
    
    longest = 1
    current = 1

    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i+1] == sorted_lst[i] + 1:
            current += 1
        elif sorted_lst[i+1] == sorted_lst[i]:
            continue
        else:
            if current > longest:
                longest = current
            current = 1

    if current > longest:
        longest = current
        
    return longest

result = longest_consecutive(tet_lst)
print(result)
def longest_consecutive(tet_lst):
    # 1. თუ სია ცარიელია, გრძელი ჯაჭვი არ არსებობს
    if not tet_lst:
        return 0

    # 2. ვახარისხებთ სიას (მაგ: [1, 2, 3, 4, 100, 200])
    sorted_lst = sorted(tet_lst)
    
    longest = 1  # ეს არის ჩვენი "რეკორდი" (საუკეთესო რაც ვნახეთ)
    current = 1  # ეს არის "დროებითი" მთვლელი (რასაც ახლა ვითვლით)

    # 3. მივყვებით სიას და სათითაოდ ვადარებთ მეზობლებს
    for i in range(len(sorted_lst) - 1):
        
        # თუ მომდევნო რიცხვი ზუსტად 1-ით მეტია (ჯაჭვი გრძელდება)
        if sorted_lst[i+1] == sorted_lst[i] + 1:
            current += 1
            
        # თუ რიცხვები მეორდება (მაგ: 2, 2), ჯაჭვი არც წყდება და არც იზრდება
        elif sorted_lst[i+1] == sorted_lst[i]:
            continue
            
        # თუ ჯაჭვი გაწყდა (მომდევნო რიცხვი ბევრად დიდია)
        else:
            # აქ ხდება "შენახვა": ვადარებთ ახალ ნაპოვნს რეკორდთან
            if current > longest:
                longest = current
            
            # დროებით მთვლელს ვაბრუნებთ 1-ზე, რომ ახალი ჯაჭვი დავიწყოთ
            current = 1

    # 4. ბოლო შემოწმება (თუ ყველაზე გრძელი ჯაჭვი სიის ბოლოში აღმოჩნდა)
    if current > longest:
        longest = current

    return longest

# გამოყენება:
tet_lst = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(tet_lst)
print(f"ყველაზე გრძელი ჯაჭვის სიგრძე: {result}")