from kerem_qa.coding_examples.loop import result
for i in range (1,10):
    result = i * i
    print(result)
    if (result > 50):
        print(f"{i} is the first result above 50")
        break