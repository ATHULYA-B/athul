def fn(list):
    result=[]
    current=0
    count=0
    string=""
    for char in list:
        if char=='A':
          current+=1
          string+=char
        elif char=='B':
            count+=1
            string+=char
        if current==count:
                result.append(string) 
                string=""
    print(result)
fn("ABAABBAAABBB") 