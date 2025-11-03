capital=str(input('What is the Capital of France? '))
print('Your Answer: ', capital)
correctanswer=('Paris')
if capital.lower()==correctanswer.lower():
    print('Correct Answer!')
else:
    print('Wrong Answer!')