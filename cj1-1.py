#A program that prints a brief introduction
def introduce(name, pronouns, food, movie):
	print("My name is " + name + "!")
	print("My pronouns are " + pronouns + "!")
	print(food)
	print(movie)


def main():
	food = "My favorite food is a good bowl of tonkotsu ramen. A completely different experience from the packet stuff, the nutty flavors of the bone broth bring the noodles, meat and vegetables together wonderfully."
	movie = "My current favorite movie is Crimes of the Future by David Cronenberg. I appreciate how it treats often taboo subjects, such as sexual deviance and physical abnormality, with love and even reverence."
	introduce("Carolyn Hope", "she/her", food, movie)

if __name__ =="__main__":
	main()