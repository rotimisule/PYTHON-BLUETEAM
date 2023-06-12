connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

x= 0  # Variable to count the number of connections to Rome
flight_time=0  # Variable to calculate the total flight time

for cities in connections:
    if "Rome" in (cities[1]) :
        x = x+1  # Increment x by 1 for each connection to Rome
        flight_time=(cities[2]+flight_time)  # Add the flight time of each connection to the total flight time 
print(x,"connections lead to Rome with an average flight time of" ,(flight_time/x), "minutes")
