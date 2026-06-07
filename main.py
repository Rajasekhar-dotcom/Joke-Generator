import requests as req

categories = ['Programming', 'Misc', 'Pun', 'Spooky', 'Christmas', 'Any', 'Dark']
choice = input("Enter your preferred joke category(Programming/Misc/Pun/Spooky/Christmas/Any/Dark): ")
if not choice.strip():
  print("Please enter a category")
elif choice.title().strip() not in categories:
  print("Please enter a valid category from the list given")
else:
  try:
    response = req.get(f"https://v2.jokeapi.dev/joke/{choice.title()}?type=single")
    if response.status_code == 200:
      print(response.json()['joke'])
    else:
        print("Unable to fetch a joke at the moment. Please try again later!")
  except req.exceptions.ConnectionError:
    print("Unable to process your request. Please check your network connection and try again!")