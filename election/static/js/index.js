function isVisible(){
  var x = document.getElementById("typeSelect").value;
  console.log(x);
  if(x == 'Sarpanch'){
    document.getElementById('villagex').style.visibility = "visible";
  }
  else{
    document.getElementById('villagex').style.visibility = "hidden";
  }
}
