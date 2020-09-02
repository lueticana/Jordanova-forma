# Jordanova-forma

Program sprejme matriko ter nato vrne pripadajočo Jordanovo kanonično formo.

Ker program uporablja funkcijo roots() knjižnice NumPy, ki ničle polinoma računa numerično, in je zaradi tega potrebno tudi nekaj zaokroževanja, program večinoma deluje samo za matrike s celoštevilskimi lastnimi vrednostmi. V ostalih primerih pride do komplikacij pri Gaussovi eliminaciji.