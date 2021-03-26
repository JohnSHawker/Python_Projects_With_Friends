
line_counter = 0

#variables for finding the max/min life expectancy information in entire .csv file
lowest = 999
lowest_year = ''
lowest_country = ''
highest = 0
highest_year = ''
highest_country = ''

#variables for finding the max/min life expectancy information based on the year the user inputs
minimum = 999
min_country = ''
maximum = 0
max_country = ''

avg_sum = 0
i = 0

with open ('Week 11\life-expectancy.csv') as f:
    print()
    input_year = int(input('What year would you like to learn about? '))
    print()
    for line in f:
        line_counter = line_counter + 1
        parts = line.strip().split(',')

        

        if line_counter > 1: #Skips the title line of .csv file

            #Variables
            entity = parts[0]
            year = int(parts[2])
            life_expectancies = float(parts[3])


            if input_year == year:
                avg_sum += life_expectancies
                i = i + 1

                if life_expectancies < minimum:
                    minimum = life_expectancies
                    min_country = entity

                if life_expectancies > maximum:
                    maximum = life_expectancies
                    max_country = entity

            

            #This locates the lowest life expectancy and pairs it with the country and the year
            if life_expectancies < lowest:
                lowest = life_expectancies
                lowest_year = year
                lowest_country = entity


            
        # if line_counter > 1: #Skips the title line of .csv file    
            
            #This locates the highest life expectancy and pairs it with the country and the year
            if life_expectancies > highest:
                highest = life_expectancies
                highest_year = year
                highest_country = entity

                
    
                if life_expectancies < lowest:
                    lowest = life_expectancies
                    lowest_country = entity
    
average = avg_sum / i
print(f'For the year {input_year}:')
print(f'The average life expectancy across all countries was {average:.3f}')
print(f'The max life expectancy was in {max_country} at {maximum:.3f} years.')
print(f'The min life expectancy was in {min_country} at {minimum:.3f} years.')
print()
print()
    

print(f'The overall max life expectancy is: {highest} from {highest_country} in {highest_year}')
print(f'The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}') 
# print(avg_sum)
# print(line_counter)

                

         