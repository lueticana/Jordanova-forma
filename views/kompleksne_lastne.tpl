%rebase osnova

Vnešena matrika: <br><br>
<table>
    %for vrstica in matrika:
        <tr>
        %for vrednost in vrstica:
            <td>{{vrednost}}</td>
        %end
        </tr>
    %end
</table>
<br><br>


Matrika ima kompleksne lastne vrednosti.
<br>
Ta program deluje samo za matrike z realnimi lastnimi vrednostmi.

<br><br>

Opomba: Lastne vrednosti program računa numerično, zato lahko pride do nekaj napak. Za nevšečnosti se opravičujemo.

<br><br>
<form action='/'>
    <input type='submit' value='Na začetek'>
</form>
