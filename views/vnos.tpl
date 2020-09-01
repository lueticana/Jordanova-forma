%rebase osnova
Vpisite matriko: <br><br>

<form action='/nov_izracun/'>
    <table>
        %for vrstica in range(velikost):
            <tr>
            %for i in range(vrstica * velikost, (vrstica + 1) * velikost):
                <td><input type="text" name={{str(i)}} size="4"></td>
            %end
            </tr>
        %end
        </table>
        <br>
    <input type="submit" value="Izračunaj!">
</form>

