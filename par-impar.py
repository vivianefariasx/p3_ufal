#Verificar se o numero digitado é impar ou par

def entrada_numero():
        x = int( input("Informe um numero inteiro:"))
        if x<0 and x%2==0:
            print("O numero informado é negativo e é par.")
        elif x<0 and not x%2==0:
              print("O numero informado é negativo e é impar.")      
        
        elif x > 0 and x%2==0:
            print("O numero informado é positivo e é par.")
        elif x>0 and not x%2==0:
              print("O numero informado é positivo e é impar.")     
        else:
            print("O numero informado é 0 e é par.")              
                  
         
entrada_numero()