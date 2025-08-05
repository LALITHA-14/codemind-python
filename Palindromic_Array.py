# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for num in arr:
        original_number=num
        rev=0
        while num!=0:
            rev=(rev*10)+(num%10)
            num=num//10
        if original_number!=rev:
            return False
    return True
