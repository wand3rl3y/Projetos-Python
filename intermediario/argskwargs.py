#não precisa ser args isso e uma conveção 
def func(*args):
    #fazer um cast
    args = list(args)
    args[0] = 20
    print(args)

func(1,2,3,4,5)

#key words 
def func2 (**kwargs):
    print(kwargs)
func2(nome="luis",sobrenome= "silva")