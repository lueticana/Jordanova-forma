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


Pripadajoča Jordanova kanonična forma: <br><br>
<table>
    %for vrstica in jordanova:
        <tr>
        %for vrednost in vrstica:
            <td>{{round(vrednost, 3)}}</td>
        %end
        </tr>
        
    %end
</table>

<br><br>
Opomba: Lastne vrednosti program računa numerično, zato lahko pride do nekaj napak. Za nevšečnosti se opravičujemo.
<br><br>
<form action='/'>
    <input type='submit' value='Na začetek'>
</form>
