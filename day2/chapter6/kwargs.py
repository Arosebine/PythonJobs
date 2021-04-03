def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(state1='Imo', capital1='Owerri', state2='Lagos', capital2='Ikeja')

def state_capital(**kwargs):
    for s, c in kwargs.items():
        print(f'{s} ==> {c}')


state_capital(state1='Imo', capital1='Owerri',
              state2='Lagos', capital2='Ikeja')
