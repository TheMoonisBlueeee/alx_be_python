weather= input("What's the weather like today? (sunny/rainy/cold:")

if weather == "sunny":
       print("Wear a t-shirt and sunglasses.")
elif "rainy":
      print("Don't forget your umbrella and a raincoat.")
elif "cold":
        print("Make sure to wear a warm coat and a scarf.")
else:
        print("Sorry, I don't have recommendations for this weather.")
weather= input("What's the weather like today?(sunny/rainy/cold:")

match weather:
    case "sunny":
        print("Wear a t-shirt and sunglasses.")
    case "rainy":
        print("Don't forget your umbrella and a raincoat.")
    case "cold":
        print("Make sure to wear a warm coat and a scarf.")
    case _:
        print("Sorry, I don't have recommendations for this weather.")

