#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define tam_linha 200
#define separador ","

typedef struct dado{
    int id;
    char cidade[100];
    float casos;
    float idh;
    float populacao;
}Dado;

void leitura(Dado dado[853]){
    FILE *arq;
    arq = fopen("covid_31_10.csv","r");
    if (arq == NULL){
        printf("Arquivo não existe \n");
    }
    char linha[tam_linha];
    char *campo;
    int i = 0;
    while(fgets(linha,tam_linha,arq) != NULL){
        campo = strtok(linha,separador);
        if (i != 0){
            dado[i-1].id = atoi(campo);
            campo = strtok(NULL,separador);
            strcpy(dado[i-1].cidade,campo);
            campo = strtok(NULL,separador);
            dado[i-1].casos = atof(campo);
            campo = strtok(NULL,separador);
            dado[i-1].idh = atof(campo);
            campo = strtok(NULL,separador);
            dado[i-1].populacao = atof(campo);
        }
        i++;
    }
}
int main(){
    Dado dado[853];
    leitura(dado);
    printf("%f\n" ,dado[351].idh);
    FILE *arq2;
    arq2 = fopen("covid_31_10.gml","a");
    fprintf(arq2,"graph\n");
    fprintf(arq2,"[\n");
    for(int i = 0;i<853;i++){
        if(dado[i].populacao > 50000){
            fprintf(arq2,"  node\n");
            fprintf(arq2,"  [\n");
            fprintf(arq2,"      id %i\n",dado[i].id);
            printf("%s\n",dado[i].cidade);
            fprintf(arq2,"      label \"%s\"\n",dado[i].cidade);
            float porcentagem;
            porcentagem = (dado[i].casos /dado[i].populacao) * 1000;
            fprintf(arq2,"      casos %f\n",dado[i].casos);
            fprintf(arq2,"      IDH %.3f\n",dado[i].idh);
            fprintf(arq2,"      populacao %f\n",dado[i].populacao);
            fprintf(arq2,"      porcentagem %.2f\n",porcentagem);
            fprintf(arq2,"  ]\n");
        }
    }
    for(int i = 0;i<853;i++){
        if(dado[i].populacao > 50000){
            for(int j = 0;j<853;j++){
                if(dado[j].populacao > 50000){
                    if(j > i){
                        if(((dado[i].idh - 0.05) < dado[j].idh) && ((dado[i].idh + 0.05) > dado[j].idh)){
                            fprintf(arq2,"  edge\n");
                            fprintf(arq2,"  [\n");
                            fprintf(arq2,"      source %i\n",dado[i].id);
                            fprintf(arq2,"      target %i\n",dado[j].id);
                            fprintf(arq2,"      value 1\n");
                            fprintf(arq2,"  ]\n");
                        }
                    }
                }
            }
        }
        
    }
    fprintf(arq2,"]\n");
    fclose(arq2);
    return 0;
}