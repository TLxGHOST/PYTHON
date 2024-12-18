 psychobabble = [ 
     [r'I need (.*)', 
      ["Why do you need {0}?", 
       "Would it really help you to get {0}?", 
       "Are you sure you need {0}?"]], 
  
     [r'Why don\'?t you ([^\?]*)\??', 
      ["Do you really think I don't {0}?", 
       "Perhaps eventually I will {0}.", 
       "Do you really want me to {0}?"]], 
  
     [r'Why can\'?t I ([^\?]*)\??', 
      ["Do you think you should be able to {0}?", 
       "If you could {0}, what would you do?", 
       "I don't know -- why can't you {0}?", 
       "Have you really tried?"]], 
  
     [r'I can\'?t (.*)', 
      ["How do you know you can't {0}?", 
       "Perhaps you could {0} if you tried.", 
       "What would it take for you to {0}?"]], 
  
     [r'I am (.*)', 
      ["Did you come to me because you are {0}?", 
       "How long have you been {0}?", 
       "How do you feel about being {0}?"]], 
  
     [r'I\'?m (.*)', 
      ["How does being {0} make you feel?", 
       "Do you enjoy being {0}?", 
       "Why do you tell me you're {0}?", 
       "Why do you think you're {0}?"]], 
  
     [r'Are you ([^\?]*)\??', 
      ["Why does it matter whether I am {0}?", 
       "Would you prefer it if I were not {0}?", 
       "Perhaps you believe I am {0}.", 
       "I may be {0} -- what do you think?"]], 
  
     [r'What (.*)', 
      ["Why do you ask?", 
       "How would an answer to that help you?", 
       "What do you think?"]], 
  
     [r'How (.*)', 
      ["How do you suppose?", 
       "Perhaps you can answer your own question.", 
       "What is it you're really asking?"]], 
  
     [r'Because (.*)', 
      ["Is that the real reason?", 
       "What other reasons come to mind?", 
       "Does that reason apply to anything else?", 
       "If {0}, what else must be true?"]], 
  
     [r'(.) sorry (.)', 
      ["There are many times when no apology is needed.", 
       "What feelings do you have when you apologize?"]], 
  
     [r'Hello(.*)', 
      ["Hello... I'm glad you could drop by today.", 
       "Hi there... how are you today?", 
       "Hello, how are you feeling today?"]], 
  
     [r'I think (.*)', 
      ["Do you doubt {0}?", 
       "Do you really think so?", 
       "But you're not sure {0}?"]], 
  
     [r'(.) friend (.)', 
      ["Tell me more about your friends.", 
       "When you think of a friend, what comes to mind?", 
       "Why don't you tell me about a childhood friend?"]], 
  
     [r'Yes', 
      ["You seem quite sure.", 
       "OK, but can you elaborate a bit?"]], 
  
     [r'(.) computer(.)', 
      ["Are you really talking about me?", 
       "Does it seem strange to talk to a computer?", 
       "How do computers make you feel?", 
       "Do you feel threatened by computers?"]], 
  
     [r'Is it (.*)', 
      ["Do you think it is {0}?", 
       "Perhaps it's {0} -- what do you think?", 
       "If it were {0}, what would you do?", 
       "It could well be that {0}."]], 