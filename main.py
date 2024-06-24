# def greetings(name):  
#     print("Hi " + name)  
  
# greetings('Peter Parker') 

def submit_input(*args, **kwargs):
    input_box = Element("textBox")
    player_input = input_box.value
    # print("Player Input: " + player_input)
    output = Element("output_div")
    output.write("Input: " + player_input)

# # submit_input()

# def clickButton():
#     submit_input()

# # submit_input()
# # clickButton()

def runPython(*args, **kwargs):
            output = Element("output_div")
            # output.write("clicked???")
            submit_input()