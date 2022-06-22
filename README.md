# nau-openedx-problem-analysis
Analisa os dados do ficheiro CSV obtido na tab Formador -> Seleccione uma secção ou um problema -> Download a CSV of problem responses
É necessário selecionar um problema: type@problem+block

Funciona para qualquer número de questões dentro do problema. 

Abre um file dialog que pede o ficheiro CSV, e de seguida outro para selecionar o ficheiro onde se pretende guardar o output.
Output: X ficheiros JPEG (um por cada questão) e um ficheiro Excel.

Bibliotecas necessárias: pandas, matplotlib, seaborn, tkinter
