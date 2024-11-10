
#@return String:complete_prompt
#Asks for user input, then uses all user input to generate a complete prompt to send to Gemini API
def questionnaire():
    
    artists_input =[]
    for x in range (3):
        artists_input.append(input("Welcome to Music Recommender (temp title)! To start the questionnaire, please enter up to 3 music artists you enjoy."))

    genre_input=[]
    for x in range (3):
        genre_input.append(input("Great! Next, please enter 3 music genres you enjoy."))
        
    context_input = input("Now, please type out what occasion or location you’ll be listening to your music at.")
    time_input = input("What’s your favorite decade in music?") 
    age_input = input("Great taste! Finally, would you like your music to be filled with older music, newer music, or a mix of both?")
    
    print("Awesome. Just hang on while we generate results.")
    
    complete_prompt= """Use the following information to produce a spotify-based playlist of recommended music.
            Do not include a title for the playlist, include only the songs.
            Format the songs as following without deviation: Title ### Artist (Year)
            Music artists I like include %s, %s, and %s. 
            I like %s, %s, and %s. 
            I want to listen to music in/at %s. 
            My favorite period of music was the %s. 
            I prefer %s music recommendations.""" % (artists_input[0],artists_input[1],artists_input[2],
                                                     genre_input[0],genre_input[1],genre_input[2],
                                                     context_input,time_input,age_input)
    
    return complete_prompt