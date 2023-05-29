# Cryptography 👩‍💻🔐
> Este projeto apresenta uma estratégia de criptografia que utiliza matrizes para
garantir mensagens seguras e confidenciais. Sua finalidade é proteger informações
confidenciais de partes não autorizadas. A estratégia
de criptografia proposta codifica cada caractere da mensagem em um número
usando matrizes e o transmite de forma segura ao destinatário.

## Linguagem
<table>
  <tr>
    <td>Python</td>
  </tr>
  <tr>
    <td>3.9.13</td>
  </tr>
</table>

## Tabela de caracteres
<p>Cada letra da mensagem foi associada a um número de acordo com a tabela
previamente definida. Esta etapa é crucial para garantir a precisão na decodificação
da mensagem.
</p>

<table>
  <tr>
    <td>A</td>
    <td>B</td>
    <td>C</td>
    <td>D</td>
    <td>E</td>
    <td>F</td>
    <td>G</td>
    <td>H</td>
    <td>I</td>
    <td>J</td>
    <td>K</td>
    <td>L</td>
    <td>M</td>
    <td>N</td>
    <td>O</td>
    <td>P</td>
    <td>Q</td>
    <td>R</td>
    <td>S</td>
    <td>T</td>
    <td>U</td>
    <td>V</td>
    <td>W</td>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td>7</td>
    <td>8</td>
    <td>9</td>
    <td>10</td>
    <td>11</td>
    <td>12</td>
    <td>13</td>
    <td>14</td>
    <td>15</td>
    <td>16</td>
    <td>17</td>
    <td>18</td>
    <td>19</td>
    <td>20</td>
    <td>21</td>
    <td>22</td>
    <td>23</td>
  </tr>
</table>

<table>
  <tr>
    <td>X</td>
    <td>Y</td>
    <td>Z</td>
    <td>.</td>
    <td>,</td>
    <td>!</td>
    <td>?</td>
    <td>[SPACE]</td>
    <td>Ç</td>
    <td>Á</td>
    <td>É</td>
    <td>Í</td>
    <td>Ó</td>
    <td>Ú</td>
    <td>Â</td>
    <td>Ê</td>
    <td>Ô</td>
  </tr>
  <tr>
    <td>24</td>
    <td>25</td>
    <td>26</td>
    <td>27</td>
    <td>28</td>
    <td>29</td>
    <td>30</td>
    <td>31</td>
    <td>32</td>
    <td>33</td>
    <td>34</td>
    <td>35</td>
    <td>36</td>
    <td>37</td>
    <td>38</td>
    <td>39</td>
    <td>40</td>
  </tr>
</table>

## Matriz Codificadora
<p>Para codificar a mensagem, utilizou-se o conhecimento em multiplicação entre
matrizes, realizando a multiplicação da matriz da mensagem principal pela
matriz da codificação (COD).</p>
<table>
  <tr>
    <td>COD</td>
    <td>4</td>
    <td>1</td>
  </tr>
  <tr>
   <tr>
     <td> </td>
     <td>3</td>
     <td>1</td>
  </tr>
</table>
  
 ## Matriz Inversa
 <p>Para decodificar a mensagem codificada, foi utilizada a matriz inversa (o
decodificador) multiplicada pela matriz da mensagem codificada, o que resulta na
mensagem original novamente. </p>
<table>
  <tr>
    <td>DECOD</td>
    <td>1</td>
    <td>-1</td>
  </tr>
  <tr>
   <tr>
     <td> </td>
     <td>-3</td>
     <td>4</td>
  </tr>
</table>

### A matriz inversa é encontrada através do seguinte cálculo:
1. A matriz inversa foi representada inicialmente pelos elementos a, b, c, d
<table>
  <tr>
    <td>DECOD</td>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
   <tr>
     <td></td>
     <td>c</td>
     <td>d</td>
  </tr>
</table>

2. A matriz COD multiplicada pelo seu inverso resulta na matriz identidade

<table>
  <tr>
    <td>IDEN</td>
    <td>1</td>
    <td>0</td>
  </tr>
  <tr>
   <tr>
     <td></td>
     <td>0</td>
     <td>1</td>
  </tr>
</table>

3. A matriz COD foi multiplicada pela matriz inversa, com o objetivo de encontrar os valores de seus elementos. O resultado de cada expressão é igualado ao seu respectivo elemento da matriz de identidade.

<table>
  <tr>
    <td>COD</td>
    <td>4</td>
    <td>1</td>
  </tr>
  <tr>
   <tr>
     <td> </td>
     <td>3</td>
     <td>1</td>
  </tr>
</table>

<table>
  <tr>
    <td>DECOD</td>
    <td>a</td>
    <td>b</td>
  </tr>
  <tr>
   <tr>
     <td></td>
     <td>c</td>
     <td>d</td>
  </tr>
</table>

<p>4a + 1c = 1 | 4b + 1d = 0</p>
<p>3a + 1c = 0 | 3b + 1d = 1</p>

4. Foi utilizado a fórmula para resolver equações de primeiro grau que acha a diferença entre duas incógnitas que resulta em zero. Assim podendo isolar o cálculo da cada incógnita.







