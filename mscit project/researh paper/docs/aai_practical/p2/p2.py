import aiml

# Create an instance of the AIML kernel (the brain of the chatbot)
kernel = aiml.Kernel()

# Load the AIML startup file (std-startup.xml) to initialize learning
kernel.learn("std-startup1.xml")

# Respond to the command that loads additional AIML patterns
kernel.respond("load aiml b")

# Start an infinite loop to receive user input and respond
while True:
    input_text = input(">Human: ")  # Get input from the user
    response = kernel.respond(input_text)  # Get the bot's response
    print(">Bot: " + response)  # Output the response to the user
