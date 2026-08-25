

for i in range (1,11):
    print("="*30) 
    print(f"TABUADA DO {i}".center(30,"="))   
    print(f"{i}*{i} = {i*i} ")    
    for j in range(1,11):
        print(f"{i}x{j} = {i*j}".center(30))