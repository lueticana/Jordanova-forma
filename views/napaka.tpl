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


Program ne zna izračunati Jordanove forme vnešene matrike. Do napake je najbrž prišlo zaradi numeričnega izračuna lastnih vrednosti. Prosimo za razumevanje.
<br><br>
<form action='/'>
    <input type='submit' value='V redu'>
</form>