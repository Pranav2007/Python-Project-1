MyName = "Pranav"
MyAge = 12
print( "My name is", MyName, "and I am", MyAge, "years old." )

MyFriendList = ["Agastya", "Srivardhan", "Mritunjoy", "Samuel", "Aditya", "Shourya"]
print( MyFriendList[3] )

PocketMoney = int( input( "Enter your pocket money" ) )
if(PocketMoney >= 500):
  print( "You are rich!")
elif(PocketMoney >= 100):
  print( "You have a good life." )
else:
  print( "I feel sorry for you." )

IntroString = str( input( "Enter a string." ) )
CharacterCount = 0
WordCount = 1
for i in IntroString:
  CharacterCount = CharacterCount + 1
  if( i == ' ' ):
    WordCount = WordCount + 1
print( "Total number of words:", WordCount )
print( "Total number of characters:", CharacterCount )