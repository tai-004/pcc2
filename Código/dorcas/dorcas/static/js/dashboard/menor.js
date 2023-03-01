
function menor(){
    var y;
    var idade = prompt("digite sua idade: ");

 

    if (idade == 15 || idade == 16 || idade == 17){
        y = "vc tem menos de 18 anos, sua idade é:" + idade + "anos.";
        document.getElementById("anos").innerHTML=y;
        window.location="/responsavel/responsavel";
      
    }
    else if (idade > 18){
        y = "vc é de maior" + idade + "anos";
        document.getElementById("anos").innerHTML=y;
	    window.location="/accounts/profile";
    }
    else if (idade < 15){
        y = "vc não pode se cadastrar";
        document.getElementById("anos").innerHTML=y;
	    
    }
    else{
        y = "Sua idade encontra-se incorreta, repita o processo!";
        document.getElementById("anos").innerHTML=y;
	 
    }
}
