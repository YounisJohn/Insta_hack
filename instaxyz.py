import os

if __name__ == "__main__":

   try:

       os.system("git pull");os.system('xdg-open https://youtube.com/@mrhacker4966')

       __import__("instaxyz").menu()

   except Exception as e: 

       exit(str(e))
