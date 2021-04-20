function isVisible()
{
    var x = document.getElementById("typeSelect").value;
    console.log(x);
    if (x == 'Sarpanch')
    {
        document.getElementById('villagex').style.visibility = "visible";
        document.getElementById('cityx').style.visibility = "hidden";
    }
    else
    {
        document.getElementById('villagex').style.visibility = "hidden";
        document.getElementById('cityx').style.visibility = "visible";
    }
}
