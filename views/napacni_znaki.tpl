%rebase osnova

Vnesli ste znake, ki ne predstavljajo števil.
<br><br>

Vaš vnos: <br><br>
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


<form action='/'>
    <input type='submit' value='V redu'>
</form>