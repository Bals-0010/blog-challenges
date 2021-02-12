"""
Create my_math class with methods 
get_average, get_mean, get_median, get_mode, get_variance_ get_standard_deviation


Note: Without using math, scipy, numpy, etc,..
Only len and sum inbuilt functions can be used

Examples:

a = my_math([11,22,33,44,55,66])
a.get_mean()
46.2
a.get_median()
38.5
a.get_mode()
11
a.get_variance()
352.9166
a.get_standard_deviation()
18.7860.....
"""


class my_math:
    def __init__(self,my_list=None):
        if my_list!=None:
            self.my_list = my_list
               
    def get_average(self):
        self.avg = sum(self.my_list)/len(self.my_list)
        return self.avg 
    
    
    def get_mean(self):
        return self.avg
    
    def get_median(self):
        middle_number = len(self.my_list)
        if middle_number%2==0:
            print((self.my_list[middle_number//2]))
            return ((self.my_list[middle_number//2]) + (self.my_list[(middle_number//2)-1]))/2
        else:
            return (self.my_list[(middle_number//2)])
            
            
    def get_mode(self):
        mode = {i: self.my_list.count(i) for i in self.my_list}
        from scipy import stats
        mode2 = stats.mode(self.my_list)
        return mode, mode2
    
    
    def get_variance(self):
        self.avg = self.get_average()
        var = [(i-self.avg)**2 for i in self.my_list]
        self.variance = sum(var)/len(var)
        return self.variance
    
    
    def get_standard_deviation(self):
        self.std_deviation = (self.get_variance())**0.5
        return self.std_deviation



# if __name__ == "__main__":
#     print("This code run from same file")
# else:
#     print("This code run from other file")
    