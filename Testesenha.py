## function to generate key 

## As soon as the files are encrypted ## 

## help with the bugs i'll apreciatte! 

def generated_key(size):
        caracters = '~{}^=+()@#$%*¨\/[]&ABCDEFGHIJKLMNOPQRSTUVXZY0123456789abcdefghijlmnopqrstuwvxz'
        password = ''
        for char in xrange(size):
                password += choice(caracters)
        return  password

print generated_key(18) 

