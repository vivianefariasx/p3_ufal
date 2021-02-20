
def entrada_numero():
        x = int( input("Informe um numero inteiro:"))
        if x>0 and x%2==0:
            print("O numero é positivo e é par.")
        else :
            if x>0 and not x%2==0: 
              print("O numero é positivo e é impar.")      
        
        if x < 0 and x%2==0:
            print("O numero é negativo e é par.")
        else:
            if x<0 and not x%2==0:
              print("O numero é negativo e é impar.")     
        if x == 0:
            print("O numero é 0 e é par.")              
                  
         
entrada_numero()


 
