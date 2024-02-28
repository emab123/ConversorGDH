# Conversor GDH (Grade de Horários) - UFSC

O Conversor GDH (Grade de Horários) é uma ferramenta em Python desenvolvida para facilitar o processo de adicionar as aulas da UFSC (Universidade Federal de Santa Catarina) ao calendário. Este script lê uma página em HTML baixada do CAGR da UFSC e gera um arquivo ICS contendo as informações das aulas, como nome da aula, horário, local, professor e turma.

## Como usar

1. **Baixe a página HTML da grade de horários do CAGR da UFSC**:
   - No CAGR, clique no botão de imprimir grade de horários.
   - Salve a página HTML baixada em seu computador.

2. **Instale as dependências**:
   - Antes de executar o script, é necessário instalar as dependências listadas no arquivo `requirements.txt`.
   - Para instalar as dependências, execute o seguinte comando no terminal:
     ```
     pip install -r requirements.txt
     ```

3. **Execute o script**:
   - Abra o terminal na pasta onde o script `conversor_gdh.py` está localizado.
   - Execute o script usando o comando:
     ```
     python conversor_gdh.py
     ```

4. **Interface Gráfica**:
   - Na interface gráfica, insira as datas de início e fim das aulas.
   - Clique no botão "Selecione arquivo HTML da grade de horarios" para escolher o arquivo HTML baixado do CAGR.
   - Clique no botão "Gerar ICS" para criar o arquivo ICS com os eventos das aulas.

5. **Arquivo ICS**:
   - Após clicar em "Gerar ICS", o arquivo ICS será criado no local especificado na interface gráfica.
   - Você pode importar esse arquivo ICS em seu aplicativo de calendário preferido para visualizar as aulas.

<br>

   >Obs.: O Google Calendar tem um bug conhecido com a recorrência do evento ao arrastar o arquivo ICS para a tela principal.
   >
   >Para melhores resultados, recomenda-se seguir o seguintes passos:
   > 1. Criar uma nova agenda (Menu a esquerda - Outros calendarios - Botão "+" - Criar nova agenda);
   > 2. Nomear a nova agenda (Ex.: Aulas UFSC) e salvar a nova agenda;
   > 3. Clicar em importar (Menu a esquerda);
   > 4. Selecionar o arquivo ICS e selecionar a nova agenda criada como destino.

<br>

## Contribuindo

Contribuições são bem-vindas! Se você encontrou algum problema ou tem sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença GNU GPL 3.0. Consulte o arquivo `LICENSE` para obter mais detalhes.

---

<p>
   <table style="undefined; width: 200px" align="center">
   <colgroup>
      <col style="width: 220px">
      <col style="width: 220px">
   </colgroup>
   <thead>
      <tr>
         <th colspan="2">Se este script facilitou a sua via, considere uma doação!</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td>Ethereum</td>
         <td>PIX<br></td>
      </tr>
      <tr>
         <td><img alt="0xc70f35d3579e631b6a824855f898b27c13fab481" src="./.github/Ethereum.png " width="200" height="200"></td>
         <td><img alt="0xc70f35d3579e631b6a824855f898b27c13fab481" src="./.github/PIX.png" width="200" height="200"></td>
      </tr>
      <tr>
         <td>0xc70f35d3579e631b6a8<br/>24855f898b27c13fab481</td>
         <td>00020126580014BR.GOV.<br/>BCB.PIX01368305270b-a<br/>962-47ef-869a-2255357<br/>c44dc5204000053039865<br/>802BR5925Eric Marcel <br/>Andrade Blies6009SAO <br/>PAULO62140510qgNBKJwY<br/>86630488EA</td>
      </tr>
   </tbody>
</p>
