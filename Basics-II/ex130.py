from datetime import date
def test(month, year): 
    return str(date(year,month,13).strftime("%A")=='Monday')

month = 11;
year = 2022;            
print("Month No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year));
month = 6;
year = 2022;            
print("\nMonth No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year)); 
