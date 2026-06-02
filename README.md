Este README é um resumo do projeto de análise de despesas do governo brasileiro, desenvolvido durante o curso
de Análise de Dados na EBAC.
 
---
 
# 📊 Análise de Gastos do Governo Federal Brasileiro
 
## 🎬 Dashboard no Power BI
<video controls src="20260602-1112-32.0262014.mp4" title="Title"></video>
---
 
# 📝 Dissertação sobre o problema
 
## Descrição detalhada do problema

O governo federal brasileiro executa anualmente um orçamento de trilhões de reais distribuídos entre dezenas de
ministérios e órgãos. No entanto, a população em geral desconhece como esse dinheiro é efetivamente gasto: quais
ministérios concentram a maior parte dos recursos, quais tipos de despesas predominam e se o dinheiro planejado é
de fato pago ao longo do ano. Além disso, o orçamento federal brasileiro é elaborado anualmente por meio da Lei
Orçamentária Anual (LOA), que define quanto cada ministério pode gastar. Ao longo do ano, esse valor é ajustado por
meio de créditos adicionais, cortes e remanejamentos, resultando na chamada dotação atual.

## A importância e relevância do problema na sociedade

A execução orçamentária é o retrato mais fiel das prioridades reais do governo. Enquanto o orçamento aprovado
representa intenções, o que foi efetivamente pago revela as escolhas concretas feitas ao longo do ano. Compreender
essa distribuição é fundamental por múltiplas razões, mas destaco especialmente duas: a concentração de recursos em
poucos órgãos, como o Ministério da Fazenda, que sozinho responde por mais de 50% dos gastos devido à dívida
pública e que mascara a distribuição real entre saúde, educação e infraestrutura. E ainda, identificar o impacto de
marcos legais importantes, como a Emenda Constitucional do Teto de Gastos (2016) e o Novo Arcabouço Fiscal (2023),
na distribuição do orçamento entre as áreas sociais e administrativas.

## Como a análise de dados pode ajudar a solucionar ou mitigar o problema.

- Agrupa automaticamente milhões de registros mensais por órgão e tipo de despesa, eliminando o trabalho manual e
garantindo que nenhum dado seja omitido ou duplicado.
- Permite identificar quais órgãos concentram mais recursos, quais tipos de despesa cresceram mais e como a
distribuição mudou ao longo dos meses e anos, algo impossível de enxergar em planilhas brutas.
- Transforma números de bilhões e trilhões em gráficos e dashboards acessíveis, permitindo que qualquer pessoa
compreenda para onde vai o dinheiro público e questione as escolhas do governo.
- Calcula automaticamente o percentual de execução de cada órgão em cada ano, identificando padrões de sub ou
superexecução orçamentária e seus possíveis impactos nos serviços públicos entregues à população.

---
 
# 🗂️ Coleta de dados
 
## Descrição de cada fonte de dados

**Execução Orçamentária da Despesa:**
Registro oficial de todas as despesas pagas pelo governo federal, alimentado diretamente pelo SIAFI — o sistema
interno de contabilidade pública. Organiza os gastos por ministérios, tipo de despesa e data. Cada arquivo mensal
contém as três fases do gasto público: valor empenhado (compromisso assumido), liquidado (serviço confirmado como
entregue) e pago (dinheiro efetivamente transferido). Para este projeto foram utilizados os arquivos mensais de
2015 a 2024, consolidados em uma única base analítica utilizando o python.

**Série Histórica do Orçamento Federal:**
Base consolidada com o comparativo entre o orçamento planejado e o executado para cada órgão do governo federal,
com série histórica disponível desde o ano 2000. Contém os valores da Lei Orçamentária Anual (LOA), a dotação atual
após ajustes ao longo do ano e o valor efetivamente executado. Permite identificar como as prioridades
orçamentárias mudaram ao longo de diferentes governos e contextos econômicos. Para este projeto foram utilizados os
dados filtrados por órgão superior de 2015 a 2024.

## Os tipos de dados disponíveis.

As duas bases de dados utilizadas neste projeto disponibilizam exclusivamente dados estruturados, organizados em
linhas e colunas com tipos bem definidos, prontos para análise sem necessidade de pré-processamento avançado ou
técnicas de extração de texto.

## Métodos para acessar e coletar esses dados.

Ambas as bases são disponibilizadas pelo governo federal de forma aberta, em arquivos prontos para download, sem
necessidade de autenticação, cadastro ou técnicas de raspagem de dados. 

**Execução Orçamentária disponivel em:** https://portaldatransparencia.gov.br/download-de-dados/despesas-execucao
**Série Histórica do Orçamento Federal disponivel em:** https://www1.siop.planejamento.gov.br/QvAJAXZfc/opendoc.htmdocument=IAS%2FExecucao_Orcamentaria.qvw&host=QVS%40pqlk04&anonymous=true

Embora ambas as fontes ofereçam APIs públicas para consultas automatizadas (a API REST do Portal da Transparência e
a API do SIDRA/IBGE), o método de download direto foi adotado neste projeto por garantir maior controle sobre os
dados coletados, facilitar a documentação do processo e ser acessível independentemente do nível técnico. O uso de
API seria recomendado em projetos com atualização automática e recorrente dos dados.

---
 
# 📈 Conclusões
 
## Resumo dos principais achados da análise

**O governo federal não atingiu a meta de execução em nenhum ano analisado**
Com execução acumulada de 73.6%, o governo deixou de executar R$ 11,41 Tri ao longo de 10 anos. Isso significa que
recursos aprovados pelo Congresso e destinados a serviços públicos não chegaram à ponta final, seja por
contingenciamento, falha de planejamento ou incapacidade de execução dos órgãos.

**Em todos os anos analisados, o Ministério da Fazenda sempre concentra a maior fatia de todo o gasto federal**
A maior fatia do orçamento não vai para saúde, educação ou infraestrutura, vai para a gestão da dívida pública. O
Principal Corrigido da Dívida Mobiliária praticamente dobrou em 10 anos. Isso significa que a dívida pública
consome sozinha mais do que todos os outros ministérios combinados.

**A Previdência Social cresceu 128% em uma década**
As Aposentadorias do RGPS saltaram de R$ 203 Bi para R$ 464 Bi entre 2015 e 2024, um crescimento de 128%. Somadas
às pensões e aposentadorias rurais, a Previdência representa 25% de todo o gasto federal e é a segunda maior área,
atrás apenas da dívida pública, evidenciando uma pressão fiscal estrutural e crescente ligada ao envelhecimento da
população brasileira.

**A pandemia de 2020 gerou o maior salto de gastos do período**
O heatmap da página 2 revela que 2020 e 2021 foram os anos com maiores anomalias nos gastos, especialmente em
"Outros Auxílios Financeiros", que saltou de R$ 29 Bi em 2019 para R$ 347 Bi em 2020, um crescimento de 1.090%,
reflexo direto do Auxílio Emergencial criado para enfrentar a pandemia de COVID-19. Esse pico é o evento mais
visível em toda a série histórica. 
Outros principais aumentos no periodo da pandemia de COVID-19 foram:

| Tipo de despesa | 2019 | 2020 | Variação |
|---|---|---|---|
| Principal Corrigido da Dívida Mobiliária | R$ 468 Bi | R$ 709 Bi | +51% |
| Juros, Deságios e Descontos da Dívida Mobiliária | R$ 277 Bi | R$ 339 Bi | +22% |
| Outros Auxílios Financeiros | R$ 29 Bi | R$ 347 Bi | +1.090% |

**Saúde e Educação representam apenas 10% do orçamento total**
Ministério da Saúde (5%) e Ministério da Educação (5%) somados representam menos de 1/10 do orçamento federal,
enquanto a dívida pública e a previdência juntas concentram mais de 87%. Esse contraste evidencia a rigidez
orçamentária brasileira: a maior parte do gasto é obrigatória e de difícil redução, deixando pouco espaço para
investimentos discricionários em áreas que impactam diretamente a qualidade de vida da população.

## Relevância desses achados para a problemática abordada.

**A dívida pública como limitador do desenvolvimento social**
O achado mais crítico deste projeto — a Fazenda consumindo 62% do orçamento — tem implicação direta na vida de todo
cidadão. Cada real pago em juros e amortizações da dívida é um real que não financia escola, hospital, saneamento
ou segurança pública. O crescimento da dívida de R$ 626 Bi para R$ 1 Tri em 10 anos não é um número abstrato:
representa o encolhimento relativo da capacidade do Estado de investir em serviços essenciais, mesmo quando o
orçamento total cresce.
O Brasil gasta mais com juros da dívida do que com saúde e educação juntos, e a análise de dados torna essa
realidade visível de forma irrefutável, algo que seria impossível sem o tratamento das bases utilizadas neste
projeto.

**A crise previdenciária como tendência estrutural irreversível**
O crescimento de 128% nos gastos com aposentadorias não é uma anomalia, é a manifestação fiscal do envelhecimento
da população brasileira. Com a taxa de natalidade em queda, a expectativa de vida aumentando e inúmeros casos de
corrupçãp, a proporção de trabalhadores ativos sustentando aposentados diminui ano a ano. Os dados mostram que, sem
ajustes estruturais, a pressão previdenciária sobre o orçamento será crescente nas próximas décadas, comprometendo
ainda mais os recursos disponíveis para saúde, educação e infraestrutura.

**A subexecução como sintoma de planejamento ineficiente**
R$ 6,17 Tri não executados em 10 anos representam serviços públicos que foram prometidos no orçamento, aprovados
pelo Congresso, e que simplesmente não foram entregues. Esse padrão crônico de subexecução, com execução sempre
abaixo de 90%, indica falhas sistêmicas no planejamento e na capacidade operacional dos órgãos públicos. Para o
cidadão, isso significa escolas não construídas, rodovias não pavimentadas e equipamentos hospitalares não
comprados, apesar de o dinheiro ter sido formalmente reservado no orçamento.

**O impacto da pandemia como evidência da importância da reserva fiscal**
O salto de R$ 29 Bi para R$ 347 Bi em auxílios financeiros em 2020 mostra como crises inesperadas demandam
capacidade de resposta fiscal imediata. A análise histórica revela que o Brasil não dispunha de reservas
estruturadas para eventos dessa magnitude, o que exigiu medidas emergenciais que ampliaram significativamente o
déficit público naquele ano, cujos efeitos ainda se refletem no crescimento da dívida em 2021 e 2022.

## Sugestões de ações ou soluções com base nos insights obtidos.

**Criar um painel contínuo de monitoramento da execução orçamentária**
A subexecução de 85,12% evidencia a necessidade de monitoramento em tempo real da execução por órgão. Um dashboard
atualizado mensalmente, similar ao desenvolvido neste projeto, permitiria identificar órgãos com baixa execução
ainda no primeiro semestre, possibilitando ações corretivas antes do encerramento do exercício.

**Revisão da metodologia de planejamento orçamentário**
A diferença sistemática de R$ 6,17 Tri entre dotação e execução sugere que o orçamento é superestimado de forma
recorrente. Uma análise histórica da capacidade de execução real de cada órgão deveria alimentar diretamente a
elaboração da LOA seguinte, tornando o planejamento mais realista e diminuindo o descompasso entre o prometido e o
entregue.

**Política estruturada de gestão da dívida pública**
O crescimento de quase 100% no serviço da dívida em 10 anos demanda uma estratégia de longo prazo para seu
controle. Os dados indicam que sem uma política fiscal consistente de geração de superávits primários, a tendência
de crescimento da dívida continuará comprimindo o espaço para gastos sociais e de investimento nas próximas décadas.

**Monitoramento contínuo da sustentabilidade previdenciária**
O crescimento de 128% nas aposentadorias exige um modelo de projeção atuarial integrado aos dados orçamentários.
Cruzar a série histórica do SIOP com dados demográficos do IBGE permitiria projetar cenários futuros de pressão
previdenciária sobre o orçamento e avaliar o impacto de reformas, fornecendo subsídios mais robustos para decisões
de política pública.


**Ampliar a análise para cruzar gastos com indicadores de resultado**
O próximo passo natural deste projeto seria cruzar os dados de execução orçamentária com indicadores de resultado,
como IDEB para educação, mortalidade infantil para saúde, variação do PIB para crescimento e evolução da taxa
básica de juros para monitorar o desenvolvimento econômico. Isso permitiria responder se o aumento dos gastos se
traduz em melhoria dos serviços, indo além do diagnóstico de quanto foi gasto para entender o que foi entregue.

---
*Projeto desenvolvido durante o curso de Análise de Dados na EBAC.*
