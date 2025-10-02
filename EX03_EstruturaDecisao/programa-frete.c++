#include <iostream>
using namespace std;

int main() 
{
  int valor_pedido, valor_final;
  cout << "Qual valor do pedido!";
  cin >> valor_pedido;
  
  if (valor_pedido >= 100){
  cout << "frete gratis";
  }
  else {
    valor_final=valor_pedido+= 15;
    
    cout <<valor_final;
    
  }
}