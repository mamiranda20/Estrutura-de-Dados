#include <iostream>
#include <string>
using namespace std;

int main() {
    string senhaCorreta = "1234";  // senha definida no programa
    string senhaDigitada;

    // Pede senha ao usuário
    cout << "Digite a senha: ";
    cin >> senhaDigitada;

    // Enquanto a senha for incorreta
    while (senhaDigitada != senhaCorreta) {
        cout << "❌ Senha incorreta! Tente novamente: ";
        cin >> senhaDigitada;
    }

    // Quando acertar
    cout << "✅ Senha correta!" << endl;

    return 0;
}
