import aiml

# Create an instance of the Kernel, which is the heart of the AIML interpreter.
kernel = aiml.Kernel()

# Load the AIML startup file and initialize the learning process.
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Start an infinite loop to communicate with the bot.
while True:
    input_text = input(">Human: ")
    response = kernel.respond(input_text)
    print(">Bot: " + response)
