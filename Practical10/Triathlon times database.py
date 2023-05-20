# write a class named 'triathlon'
# initialise the class
# class should have first name, last name, location, swim, cycle, run and total time (sum of swim, cycle and run)
# call a function to print out the information in the class in a single line


class triathlon:
    def __init__(self, first_name, last_name, location, swim, cycle, run):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim = swim
        self.cycle = cycle
        self.run = run
        self.total_time = swim + cycle + run
    def athletic_information(self):
        print('First name:',self.first_name,' Last name:', self.last_name,' Location where the competition take place:',self.location,' Time_swim:',self.swim,' Time_cycle:',self.cycle,' Time_run:',self.run,' Total time:',self.total_time)
        return

# Example
athletic1 = triathlon('Sam','Jane','China',10,20,30)
athletic1.athletic_information()