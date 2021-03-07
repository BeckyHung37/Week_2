#Q1
def calculate(min, max):
    sum=0
    if min==max:
        print(min)

        return(min)
    else:
        for i in range(min,max+1):
            sum=sum+i
        print(sum)

        return(sum)

calculate(1, 3)
calculate(4, 8)


#Q2
def avg(data):
    number_of_employee=data['count']
    total_salary=0
    for employee in data['employees']:
        total_salary=total_salary+employee['salary']
    avg_salary=total_salary/number_of_employee
    print(avg_salary)
    return(avg_salary)

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})


#Q3
def maxProduct(nums):
    sort_nums=sorted(nums)
    ans1=sort_nums[0]*sort_nums[1]
    ans2=sort_nums[-1]*sort_nums[-2]
    if ans1 > ans2 :
        print(ans1)
        return(ans1)
    else :
        print(ans2)
        return(ans2)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3]) 


#Q4
def twoSum(nums, target):
    for num in nums:
        rem=target-num
        if rem in nums:
            index1=nums.index(num)
            index2=nums.index(rem)
            return[index1,index2]
result=twoSum([2, 11, 7, 15], 9)
print(result)
