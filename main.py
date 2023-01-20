import random
import wikipedia
import sys

def main():
    #prompt
    print("=============\nWelcome")
    print("=============")
    
    #user response
    usr_r  = input(str("Would you like to gerate some random article Y/N or qq to EXIT:"))
    print("\n")

     # generating a a random int
    rand_int = random.randint(0, 10)

        #using the rand_int to gerate a list of random articles
    rand_acticles = wikipedia.random(rand_int)
        
    print(rand_acticles)
    print("-"*50)

    if usr_r == 'Y' or usr_r =='y':
 
       
        #allowing user to choose a specific article
        choosing_an_art = input(str("Here's a list of Articles which one is more exiting to read: "))
        print("-"*50)
        if choosing_an_art == 'none' or choosing_an_art =="None" or choosing_an_art =="None of them":

            regenerate = random.choice([num for num in range(0, 11)])

            #regerating a new list of articles
            regenerate_articles = wikipedia.random(regenerate)
            print("\n")
            print("-"*50)
            print(regenerate_articles)
            pick_another_art = input(str("What about now? if 'yes' enter the article you like otherwise enter 'q' to quit the program and re-run it to get a new list of articles: "));
            for new_article in regenerate_articles:
                if pick_another_art == new_article:
                    print(f"You chose '{new_article}'")
                    print("\n")
                    print("="*10)
                    chosen_article = wikipedia.page(new_article)
                    print(wikipedia.summary(chosen_article, sentences=5))

                    #data == the url(link) of the article
                    data = {"Title: ": chosen_article.title,
                            "URL: ": chosen_article.url}
                    
                    print(data)
                elif pick_another_art == "q":
                    break
                else:
                    print("/"*50)
                    print("Wrong command re-run the program")
                    print("/"*50)
                    break
    # if the user's not intrested we'll in picking an article we'll just print one for them            
    elif usr_r == 'n' or usr_r =='N':
        print("=*30")
        print("Well I'll generate You a random one")
        print("=*30")

        print("\n")
        
        #printing a random article from the first list 
        first_article = random.choice(rand_acticles)

# information about the article from the first list
        first_article_info = wikipedia.page(first_article) 
        
        print(wikipedia.summary(first_article, sentences=6))

        first_article_data = {"Title: ": first_article_info.title,
                                "URL: ": first_article_info.url}
    elif usr_r == 'qq':
        sys.exit(f"You enter '{usr_r}' to exit")


main()