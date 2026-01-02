def create_profile():
  profile = {}

  profile["name"] = input("Enter your name: ")
  profile["age"] = input("Enter your age: ")
  profile["city"] = input("Enter your city: ")
  hobby = input("Enter your hobby:")
  profile["hobby"]= hobby
 
  return profile

def display_profile(profile):
  print("\n--- User Profile ---")
  for key, value in profile.items():
    print(f"{key}: {value}")

user_profile = create_profile()
display_profile(user_profile)
