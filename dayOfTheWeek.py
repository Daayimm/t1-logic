import math
def dayOfTheWeek(d,m,y):
    month_code = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4] 
    if m < 3:                                                                                           
        y -= 1 
    year_code = (y % 100) + (y % 100) // 4   
    year_code = (year_code + (y // 100) // 4 + 5 * (y // 100)) % 7 
    
    if y % 4 == 0:
        month_code[1] = 1
    
    day_of_week = (d +month_code[m-1]+year_code) % 7
    
    return day_of_week

if __name__ == "__main__":
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(days[dayOfTheWeek(15, 6, 1995)])  # June 15, 1995
    print(days[dayOfTheWeek(1, 1, 2000)])   # Jan 1, 2000








