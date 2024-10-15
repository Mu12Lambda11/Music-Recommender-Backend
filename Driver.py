import Questionnaire
import GeminiConnect
import SpotifyConnect

def main():
    user_input = int(input("Please enter a number: 1. Questionnaire, 2. Playlist , 3. Artist, 4. Spotify Account \n"))
    
    prompt=""
    
    if user_input==1:
        prompt=Questionnaire.questionnaire()
        
    print(useGemini(prompt))
        
def useGemini(prompt):
    return GeminiConnect.generate_playlist(prompt)

def useSpotify():
    print("Spotify implementation goes here")
    
if __name__ == "__main__":
    main()
