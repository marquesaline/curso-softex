// Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

// - use a função realloc;
// - use a função sizeof;
// - que tenha tamanho 22 de vetor;
// - depois libere o bloco utilizando a função free.

#include <stdio.h>
#include <stdlib.h>
int main() {
      int * ponteiro; 
      int tamanho = 22;

      ponteiro = (int *) malloc(5 * sizeof (int)); 
         
      ponteiro = (int *) realloc(ponteiro , tamanho * sizeof (int));

      for(int i = 0; i < tamanho; i++) {
        ponteiro[i] = i + 1;
        printf("%d \n", ponteiro[i]);
      }

      free(ponteiro);
      printf("Memória limpa.\n");
      
}
  