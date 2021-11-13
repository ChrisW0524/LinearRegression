from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression 
import random 

# y=mx+b 
def loss(data, m, b): 
    #loss = value that determines how acurate a lien of best fit fits the data 
    return sum(( m * x +b - data[x] )**2 for x in range(100) ) /len(data) #average of squares 

mm =14#max(min(int(input("Choose a slope from -100 to 100: ")), 100), -100) 
bb = 66#max(min(int(input("Choose a y-int from -100 to 100: ")), 100), -100) 
NOISE = 100#abs(int(input("Choose the amount of noise: "))) 

data = [random.gauss(mm * x +bb, NOISE) for x in range(100)] 
rate_a = 1 
rate_b = 0.1 

best_m = 0 
best_b = 0 

for _ in range(100): 
    min_loss = float('inf') 
    for db, dm in [(rate_a, 0), (-rate_a, 0), (0, rate_b), (0, -rate_b), 
                   (rate_a, rate_b), (-rate_a, rate_b), (rate_a, -rate_b), (-rate_a, -rate_b)]: 
        l = loss(data, best_m+dm, best_b+db) 
        if l < min_loss: 
            min_loss = l 
            best_m = best_m+dm 
            best_b = best_b+db 
    print(min_loss) 
    plt.scatter(range(100), data) 
    plt.plot(range(100), [best_m * x + best_b for x in range(100)], color='r', label="Model") 
    plt.plot(range(100), [mm * x + bb for x in range(100)], color='g', label="True Function") 

    plt.legend() 
    plt.show() 

  

    #m = random.uniform(-100, 100) 

    #b = random.uniform(-100, 100) 

    #l = loss(data, m, b) 

    #if l < min_loss: 

    #    min_loss = l 

    #    best_m = m 

    #      best_b = b 

print("Slope Learnt:", best_m) 
print("Y-int Learnt:", best_b) 
