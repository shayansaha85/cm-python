
# Normal dictionary
chandini_details = {

     "name" : "Chandini", # name --> Key, "Chandini" --> Value
     "city" : "Kolkata",
     "age" : 22

}

# print(chandini_details['name'])


nested_str = {
      "personalInformation" : {
            "name" : "Riya",
            "phone" : "1234567890",
            "dob" : "01-01-2003",
      },

      "professionalInformation" : {
            "company" : "ABC",
            "salaryPerAnnum" : 1850737,
            "designation" : "SDE3",
            "officeAddress" : "Kodathi, Bangalore"
      },

      "extraCurricular" : {
            "hobbies" : ['singing', 'writing'],
            "favorite_books" : ['Poirot', 'Do it today'],
      }
}

name = nested_str['personalInformation']['name']
print(f"Name = {name}") # Chandini

yearlySalary = nested_str['professionalInformation']['salaryPerAnnum'] # 1800000
monthlySalary = yearlySalary / 12 # 154000.083343434

monthlySalary_upto2decimal = round(monthlySalary, 2)
print(f"{name}'s Monthly Salary = {monthlySalary_upto2decimal}")

favoriteBook = nested_str['extraCurricular']['favorite_books'][0]
print(f"{name}'s Favorite Book = {favoriteBook}")