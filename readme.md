# DESAFIO - CALCULAR A MÉDIA ANUAL DE UM ALUNO DA FIAP NO MODELO PRESENCIAL

. A FIAP utiliza o modelo anual e separa as médias em duas grandes médias, denominadas Médias Semestrais, para encontrar a Média Anual

## DETALHES DO PRIMEIRO SEMESTRE

1º O aluno submete-se a três checkpoints (Provas CP1, CP2 e CP3).
A média dos checkpoints (MCP1Sem) equivale á media simples das duas maiores notas.

2º O aluno participa do Challenge, que é composto de duas notas denominadas Sprint1 e Sprint2 (S1 e S2), a média dos sprints (MS1Sem) é calculada com base na média simples das notas S1 e S2.

3º O aluno submete-se a uma prova semestral chamada Global Solution (GS1Sem).

4º A média do primeiro semestre (M1Sem) é calculado com a ponderação:

* MCP1Sem = 20%
* MS1Sem = 20%
* GS1Sem = 60%

### Fórmula

![alt text](/public/image.png)

## DETALHES DO SEGUNDO SEMESTRE

1º O aluno submete-se a três checkpoints (Provas CP4, CP5 e CP6).
A média dos checkpoints (MCP2Sem) equivale á media simples das duas maiores notas.

2º O aluno participa do Challenge, que é composto de duas notas denominadas Sprint3 e Sprint4 (S3 e S4), a média dos sprints (MS2Sem) é calculada com base na média simples das notas S3 e S4.

3º O aluno submete-se a uma prova semestral chamada Global Solution (GS2Sem).

4º A média do segundo semestre (M2Sem) é calculado com a ponderação:

* MCP2Sem = 20%
* MS2Sem = 20%
* GS2Sem = 60%

### Fórmula

![alt text](/public/image2.png)

## CALCULANDO A MÉDIA ANUAL

Calculada pela proporção:

* M1Sem = 40%
* M2Sem = 60%
  
### Fórmula

![alt text](/public/image3.png)

## REGRAS DE STATUS

* Se MA for maior ou igual a 6, o Status será "APROVADO" (exibir juntamente com a MA atingida).
* Se a MA for menor do que 4, o Status será " REPROVADO" (exibir juntamente com a MA atingida).
* Se a MA estiver entre 4 e 5.9, o aluno poderá por meio do processo de exame. Nesse caso, o programa devera pedir a NOTA DE EXAME (NE) ao aluno e calcular a nova Média Final (MF) considerando a média simples entre MA e NE, logo:

### Fórmula

![alt text](/public/image4.png)

## REQUISITOS PARA DESENVOLVER A SOLUÇÃO PLENAMENTE

1º Todas as notas digitadas pelo usuário devem ser válidas (entre 0 e 10).

2º Caso uma nota não esteja nesse intervalo, advertir o usuário e pedir para ele digitar novamente a mesma nota.

3º Toda média calculada deve ser exibida na tela.

4º Utilize a boa prática: cada subalgoritmo deve resolver apenas um problema.

5º Ao final da execução do cálculo da Média Anual, perguntar se o aluno deseja continuar executando o programa digitando [S]im ou [N]ão. 

6º A digitação do S ou N também deve ser verificada e somente essas duas letras serão aceitas.
